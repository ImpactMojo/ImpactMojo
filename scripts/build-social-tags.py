#!/usr/bin/env python3
"""Give every indexable page its own share card and a complete set of share tags.

    python3 scripts/build-social-tags.py           # rewrite heads, write data/social-cards.json
    node scripts/render-social-cards.mjs           # draw any card that is missing
    python3 scripts/build-social-tags.py --check   # CI: heads current, every card drawn

Why this exists
---------------
Measured on 2026-10-12 over 1,008 indexable pages: 836 shared one image,
assets/images/og-card.png, which still advertised "69 courses" and "149 reading
companions"; 120 had no og:image at all, 267 no Twitter card, 290 no canonical
link and 96 no meta description. A link to any page looked, in WhatsApp or
LinkedIn, like a link to every other page.

Worse, the canonical links that did exist pointed at the file path as written
in the repository (/Labs/toc-lab.html, /BookSummaries/...). Netlify lowercases
every path, so all of those answered 301. A canonical that redirects tells a
search engine two different things about which address is the real one.

What this does
--------------
For each page the sitemap would list, it reads what the page already says
(title, description, og:title, og:description, and any bespoke og:image), takes
out every canonical, description, og:* and twitter:* tag in <head>, and writes
one block back in their place, between <!-- share:start --> and
<!-- share:end -->. Values the author chose are kept. Only the generic
og-card.png and the bare logo are replaced, by a card drawn for that page:
its section, its title and, for handouts, its track.

The canonical address is the one the live site answers 200 for: the lowercased
path with spaces encoded, keeping .html, and a directory for an index page.

A missing description is taken from the page's own first paragraph. It is never
written from nothing.

Each card's file name carries a hash of what is drawn on it, so a page whose
title changes points at a file that does not exist yet, and --check fails until
render-social-cards.mjs has drawn it.
"""
import hashlib
import html
import importlib.util
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.impactmojo.in"
MANIFEST = ROOT / "data" / "social-cards.json"
CARD_DIR = "assets/og"
GENERIC = ("og-card.png", "ImpactMojo%20Logo.png", "ImpactMojo Logo.png", "/assets/og/")
START, END = "<!-- share:start -->", "<!-- share:end -->"

# Path prefix -> (section label, accent colour). First match wins.
SECTIONS = [
    ("101-courses/practice/", "101 Practice Workbook", "#8b5cf6"),
    ("101-courses/poster/", "101 Course", "#667eea"),
    ("101-courses/", "101 Course", "#667eea"),
    ("products/notes-101/", "101 Course Notes", "#d97706"),
    ("products/", "ImpactMojo Shop", "#d97706"),
    ("courses/", "Flagship Course", "#4f46e5"),
    ("Handouts/", "Handout", "#0891b2"),
    ("BookSummaries/", "Book Companion", "#c026d3"),
    ("BookCompanionTools/", "Companion Tool", "#c026d3"),
    ("Labs/", "Studio", "#059669"),
    ("premium-tools/", "Pro Studio", "#059669"),
    ("code/", "Code Studio", "#0f766e"),
    ("Games/", "Game", "#e11d48"),
    ("DeepDives/", "Deep Dive", "#2563eb"),
    ("DataNotes/", "Data Note", "#0284c7"),
    ("blog/", "Learning Loops", "#7c3aed"),
    ("law-guides/", "Law Guide", "#b45309"),
    ("theories/", "Theory", "#9333ea"),
    ("timelines/", "Timeline", "#0d9488"),
    ("fundamentals/", "Fundamentals", "#4f46e5"),
    ("specials/", "Special", "#db2777"),
    ("challenges/", "Live Case Challenge", "#ea580c"),
    ("practice-packs/", "Practice Pack", "#8b5cf6"),
    ("the-long-view/", "The Long View", "#0369a1"),
    ("facilitator-kits/", "Facilitator Kit", "#ca8a04"),
    ("work-samples/", "Work Sample", "#64748b"),
    ("maps/", "Map", "#0d9488"),
    ("impactlex/", "ImpactLex", "#6366f1"),
    ("research-to-action/", "Research to Action", "#0891b2"),
    ("", "ImpactMojo", "#667eea"),
]

TAG = re.compile(r"<(?:meta|link)\b[^>]*>", re.I | re.S)
ATTR = re.compile(r'([a-zA-Z:_-]+)\s*=\s*("([^"]*)"|\'([^\']*)\')', re.S)


def load_sitemap_rules():
    spec = importlib.util.spec_from_file_location("bs", ROOT / "scripts" / "build-sitemap.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def canonical(path):
    """The address the live site answers 200 for."""
    p = path.lower()
    if p == "index.html":
        return SITE + "/"
    if p.endswith("/index.html"):
        p = p[: -len("index.html")]
    return SITE + "/" + quote(p, safe="/,")


def attrs(tag):
    out = {}
    for m in ATTR.finditer(tag):
        out[m.group(1).lower()] = m.group(3) if m.group(3) is not None else m.group(4)
    return out


def managed(a):
    """Is this one of the tags the share block owns?"""
    if a.get("rel", "").lower() == "canonical":
        return "canonical"
    prop = a.get("property", "").lower()
    name = a.get("name", "").lower()
    if prop.startswith("og:"):
        return prop
    if name.startswith("twitter:"):
        return name
    if name == "description":
        return "description"
    return None


def text_of(fragment):
    t = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", fragment, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def first_paragraph(body):
    for m in re.finditer(r"<p\b[^>]*>(.*?)</p>", body, re.S | re.I):
        t = text_of(m.group(1))
        if len(t) >= 60:
            if len(t) > 160:
                t = t[:157].rsplit(" ", 1)[0].rstrip(",;:") + "…"
            return t
    return ""


def section(path):
    for prefix, label, colour in SECTIONS:
        if path.startswith(prefix):
            return label, colour
    return "ImpactMojo", "#667eea"


_DECKS = None


def deck_slides(slug):
    global _DECKS
    if _DECKS is None:
        try:
            _DECKS = {d["slug"]: d.get("slides") for d in json.loads((ROOT / "data" / "decks.json").read_text(encoding="utf-8"))["decks"]}
        except (OSError, ValueError, KeyError):
            _DECKS = {}
    return _DECKS.get(slug)


def subline(path, text=""):
    """A second line for the card, only where the page or its data says it."""
    if path.startswith("BookSummaries/"):
        m = re.search(r'"author"\s*:\s*"([^"]{3,90})"', text)
        if m:
            return html.unescape(m.group(1))
    m = re.match(r"101-courses/([^/]+)\.html$", path)
    if m and deck_slides(m.group(1)):
        return "Free course, %d slides" % deck_slides(m.group(1))
    if path.startswith("Handouts/"):
        parts = path.split("/")
        if len(parts) > 2:
            return parts[1]
    if path.startswith("courses/") and path.endswith("/lexicon.html"):
        return "Course lexicon"
    return ""


def clean_title(t):
    t = html.unescape(t or "").strip()
    t = re.sub(r"\s+[|–—-]\s+(?:ImpactMojo|Learning Loops)\b.*$", "", t, flags=re.I)
    t = re.sub(r"\s+\|\s+[^|]{1,40}$", "", t) if " | " in t else t
    t = re.sub(r":\s*Course Notes \(PDF\)$", "", t)
    return t.strip() or "ImpactMojo"


def slug(path):
    s = path.lower()
    s = s[:-5] if s.endswith(".html") else s
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "index"


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def process(path, text):
    head_end = text.lower().find("</head>")
    if head_end < 0:
        return None, None
    head, rest = text[:head_end], text[head_end:]
    found = {}
    def strip(m):
        a = attrs(m.group(0))
        k = managed(a)
        if not k:
            return m.group(0)
        v = a.get("href") if k == "canonical" else a.get("content", "")
        found.setdefault(k, v)
        return ""
    head = TAG.sub(strip, head)
    head = re.sub(r"[ \t]*(?:%s|%s)[ \t]*\n?" % (re.escape(START), re.escape(END)), "", head)
    head = re.sub(r"\n[ \t]*\n(?:[ \t]*\n)+", "\n\n", head)

    tm = re.search(r"<title\b[^>]*>(.*?)</title>", head, re.S | re.I)
    page_title = html.unescape(tm.group(1)).strip() if tm else ""
    title_raw = found.get("og:title") or page_title or "ImpactMojo"
    title = html.unescape(title_raw).strip()
    desc = html.unescape(found.get("description") or found.get("og:description") or "").strip()
    if not desc:
        desc = first_paragraph(rest)
    og_desc = html.unescape(found.get("og:description") or "").strip() or desc

    label, colour = section(path)
    card_title = clean_title(title)
    sub = subline(path, text)
    h = hashlib.sha1(("%s|%s|%s|%s" % (label, card_title, sub, colour)).encode()).hexdigest()[:8]

    image = found.get("og:image") or found.get("twitter:image") or ""
    bespoke = bool(image) and not any(g in image for g in GENERIC)
    card = "%s/%s-%s.jpg" % (CARD_DIR, slug(path), h)
    if bespoke:
        img_url, alt = image, found.get("og:image:alt", "")
        w, hh = found.get("og:image:width", ""), found.get("og:image:height", "")
    else:
        img_url, alt, w, hh = SITE + "/" + card, "%s, %s, ImpactMojo" % (card_title, label), "1200", "630"
    url = canonical(path)
    og_type = found.get("og:type") or ("article" if path.startswith(("blog/", "DeepDives/", "DataNotes/", "BookSummaries/", "specials/")) else "website")

    lines = [START, '<link rel="canonical" href="%s">' % esc(url)]
    if desc:
        lines.append('<meta name="description" content="%s">' % esc(desc))
    lines += [
        '<meta property="og:type" content="%s">' % esc(og_type),
        '<meta property="og:site_name" content="ImpactMojo">',
        '<meta property="og:title" content="%s">' % esc(title),
    ]
    if og_desc:
        lines.append('<meta property="og:description" content="%s">' % esc(og_desc))
    lines.append('<meta property="og:url" content="%s">' % esc(url))
    lines.append('<meta property="og:image" content="%s">' % esc(html.unescape(img_url)))
    if w and hh:
        lines.append('<meta property="og:image:width" content="%s">' % esc(w))
        lines.append('<meta property="og:image:height" content="%s">' % esc(hh))
    if alt:
        lines.append('<meta property="og:image:alt" content="%s">' % esc(html.unescape(alt)))
    lines += [
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="%s">' % esc(title),
    ]
    # Twitter text follows the page's own Open Graph text. Keeping an old
    # twitter:title let a generator's template leak its own title onto every
    # page built from it.
    tdesc = og_desc
    if tdesc:
        lines.append('<meta name="twitter:description" content="%s">' % esc(tdesc))
    lines.append('<meta name="twitter:image" content="%s">' % esc(html.unescape(img_url)))
    if found.get("twitter:site"):
        lines.append('<meta name="twitter:site" content="%s">' % esc(found["twitter:site"]))
    lines.append(END)
    block = "\n".join(lines) + "\n"

    if tm:
        i = head.find(tm.group(0)) + len(tm.group(0))
        head = head[:i] + "\n" + block.rstrip("\n") + head[i:]
        head = re.sub(re.escape(END) + r"[ \t]*\n(?:[ \t]*\n)+", END + "\n", head)
    else:
        head = head.rstrip() + "\n" + block
    entry = None if bespoke else {"card": card, "label": label, "title": card_title, "sub": sub, "colour": colour}
    return fix_ld(head + rest), entry



LDJSON = re.compile(r'(<script[^>]*application/ld\+json[^>]*>)(.*?)(</script>)', re.S | re.I)
SITE_URL = re.compile(r'https://www\.impactmojo\.in(/[^"\s<>#?]*)([#?][^"\s<>]*)?')


def fix_ld(text):
    """Point the structured data at the same addresses as the canonical links.

    JSON-LD carried the repository path (/Labs/..., /BookSummaries/...), which
    Netlify answers with a 301. Only links to pages that exist here are
    rewritten; image and file links are left, because Netlify serves those at
    either case without a redirect."""
    from urllib.parse import unquote

    def url(m):
        raw, tail = m.group(1), m.group(2) or ""
        path = unquote(raw).lstrip("/")
        cand = None
        if path == "" or path.endswith("/"):
            if (ROOT / path / "index.html").exists():
                cand = path + "index.html"
        elif path.endswith(".html") and (ROOT / path).exists():
            cand = path
        if not cand:
            return m.group(0)
        return canonical(cand) + tail

    def block(m):
        return m.group(1) + SITE_URL.sub(url, m.group(2)) + m.group(3)

    return LDJSON.sub(block, text)


def apply(path, text):
    """For generators: the page as this script would leave it."""
    new, _ = process(path, text)
    return text if new is None else new


def load():
    """Import this module from a generator: share = build_social_tags.load()."""
    return sys.modules[__name__]


def pages():
    rules = load_sitemap_rules()
    return [p for p in rules.tracked_html() if rules.include(p)]


def main():
    check = "--check" in sys.argv[1:]
    stale, manifest = [], {}
    for path in pages():
        f = ROOT / path
        text = f.read_text(encoding="utf-8")
        new, entry = process(path, text)
        if new is None:
            continue
        if entry:
            manifest[path] = entry
        if new != text:
            stale.append(path)
            if not check:
                f.write_text(new, encoding="utf-8")
    mtext = json.dumps(manifest, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    cur = MANIFEST.read_text(encoding="utf-8") if MANIFEST.exists() else ""
    if not check:
        MANIFEST.write_text(mtext, encoding="utf-8")
        print("share tags written on %d pages; %d drawn cards in %s" % (len(stale), len(manifest), MANIFEST.name))
        return
    missing = sorted(e["card"] for e in manifest.values() if not (ROOT / e["card"]).exists())
    if stale or mtext != cur or missing:
        print("FAIL - share tags or cards are out of date")
        for s in stale[:20]:
            print("  head not current: %s" % s)
        if len(stale) > 20:
            print("  ... and %d more" % (len(stale) - 20))
        if mtext != cur:
            print("  data/social-cards.json is stale")
        for m in missing[:20]:
            print("  card not drawn: %s" % m)
        print("Run python3 scripts/build-social-tags.py, then node scripts/render-social-cards.mjs")
        sys.exit(1)
    print("PASS - %d pages carry a complete share block; %d drawn cards all present" % (len(pages()), len(manifest)))


if __name__ == "__main__":
    main()
