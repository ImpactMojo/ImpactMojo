#!/usr/bin/env python3
"""Write walkthrough.html, a slide deck that walks through the whole site.

The deck is a description of the site, so it goes stale the moment the site
changes unless nothing in it is typed by hand. Everything that can change is
read from the place the site itself keeps it:

  data/counts.json            every number (the same file check-counts.py enforces)
  js/site-chrome.js  MENU     the five header groups, their links and descriptions
  js/translate-sarvam.js      the languages the translation switch offers
  premium.html                the Membership tiers, prices and what each adds
  products.html               the paid products, by section, with their prices
  partnerships.html           the partners named on the partnerships page

The "What's new" slide reads data/whats-new.json in the browser, so it is as
current as the homepage's own list without a rebuild.

The shell (CSS, theme switch, scaling, keyboard and touch navigation) is the
101 deck shell, taken from the same donor deck as scripts/deck-builder/build.py.

    python3 scripts/build-walkthrough.py          # write walkthrough.html
    python3 scripts/build-walkthrough.py --check  # fail if it is stale or a source moved
"""
import html
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "walkthrough.html"
SLUG = "walkthrough"
TITLE = "ImpactMojo walkthrough"
DESC = ("A slide-by-slide walkthrough of ImpactMojo: what is on the site, how it is organised, "
        "what is free, what Membership and the paid products add, and how teachers and "
        "organisations use it.")


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B = _load("deck_build", "scripts/deck-builder/build.py")
E = html.escape


def text(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def fail(msg):
    raise SystemExit(f"[walkthrough] {msg}")


# ------------------------------------------------------------------ sources
C = json.loads((ROOT / "data/counts.json").read_text(encoding="utf-8"))


def n(key):
    if key not in C:
        fail(f"data/counts.json has no '{key}'")
    return C[key]


def read_menu():
    src = (ROOT / "js/site-chrome.js").read_text(encoding="utf-8")
    m = re.search(r"var MENU = (\[[\s\S]*?\]\]\]\s*\]);", src)
    if not m:
        fail("could not find MENU in js/site-chrome.js")
    groups = []
    for g in re.finditer(r"\['([^']+)', \[([\s\S]*?)\]\]", m.group(1)):
        links = re.findall(r"\['([^']+)', '([^']+)', '([^']+)'", g.group(2))
        groups.append((html.unescape(g.group(1)), [(h, html.unescape(l), html.unescape(d)) for h, l, d in links]))
    if len(groups) < 4 or any(not ls for _, ls in groups):
        fail("MENU in js/site-chrome.js did not parse into groups of links")
    return groups


def read_langs():
    src = (ROOT / "js/translate-sarvam.js").read_text(encoding="utf-8")
    block = re.search(r"var LANGS = \{([\s\S]*?)\};", src)
    if not block:
        fail("could not find LANGS in js/translate-sarvam.js")
    return [m.group(2) for m in re.finditer(r"\b(\w\w): \{ label: \"[^\"]+\", native: \"([^\"]+)\"", block.group(1))
            if m.group(1) != "en"]


def read_tiers():
    src = (ROOT / "premium.html").read_text(encoding="utf-8")
    tiers = []
    for t in re.finditer(r'<div class="tier [^"]*">([\s\S]*?)<a href="#detail-', src):
        b = t.group(1)
        name = text(re.search(r'<div class="tname">(.*?)</div>', b).group(1))
        tag = text(re.search(r'<div class="ttag">(.*?)</div>', b).group(1))
        price = text(re.search(r'<div class="price">(.*?)</div>', b, re.S).group(1)).replace("₹ ", "₹")
        annual = text(re.search(r'<div class="annual">(.*?)</div>', b).group(1))
        feats = [text(f) for f in re.findall(r"<li[^>]*>(.*?)</li>", b, re.S)]
        tiers.append(dict(name=name, tag=tag, price=price, annual=annual, feats=feats))
    if len(tiers) < 3:
        fail(f"premium.html: expected the tier cards, found {len(tiers)}")
    return tiers


def read_products():
    src = (ROOT / "products.html").read_text(encoding="utf-8")
    parts = re.split(r'<h2 class="anchor">', src)[1:]
    out = []
    for p in parts:
        head = text(p.split("</h2>", 1)[0])
        items = re.findall(r'<div class="dl">([\s\S]*?)</a></div>', p)
        if not items:
            continue
        prices = sorted({int(x.replace(",", "")) for it in items
                         for x in re.findall(r"₹([\d,]+)", html.unescape(re.sub(r"<s>.*?</s>", "", it)))})
        count = len(items)
        if "101" in head:  # one card stands for the notes to every 101 deck
            count = len(json.loads((ROOT / "data/course-notes-101.json").read_text(encoding="utf-8")))
        out.append(dict(name=head, count=count, prices=prices))
    if not out:
        fail("products.html: no product sections found")
    return out


def read_partners():
    src = (ROOT / "partnerships.html").read_text(encoding="utf-8")
    body = text(src)
    names = [p for p in ("Populi", "India Institute", "PinPoint Ventures") if p in body]
    if not names:
        fail("partnerships.html names none of the partners this deck describes")
    return names


def link_ok(href):
    """A link in the deck must point at a page that exists."""
    if href.startswith(("http", "mailto:")):
        return True
    p = href.split("#")[0].split("?")[0]
    if p in ("", "/"):
        return True
    cand = [ROOT / p.lstrip("/")]
    if p.endswith("/"):
        cand = [ROOT / p.lstrip("/") / "index.html"]
    elif not p.endswith(".html"):
        cand += [ROOT / (p.lstrip("/") + ".html"), ROOT / p.lstrip("/") / "index.html"]
    low = {str(c).lower() for c in cand}
    return any(c.exists() for c in cand) or any(
        str(f).lower() in low for f in ROOT.glob(p.lstrip("/").split("/")[0] + "*"))


# ------------------------------------------------------------------ slides
MENU = read_menu()
LANGS = read_langs()
TIERS = read_tiers()
PRODUCTS = read_products()
PARTNERS = read_partners()
LINKS = []


def a(href, label):
    LINKS.append(href)
    return f'<a href="{E(href)}">{label}</a>'


# How many of each menu item there are, where counts.json knows.
COUNT_FOR = {
    "/courses/": "flagship-courses", "/101-courses/": "foundational-courses",
    "/practice-packs/": "practice-packs", "/Games/": "game-simulations", "/game-library.html": "games",
    "/Labs/": "labs", "/premium-tools/": "premium-tools", "/law-guides/": "law-guides",
    "/libraries.html": "libraries", "/explorers.html": "data-explorers", "/by-the-numbers/": "by-the-numbers",
    "/dataverse.html": "dataverse",
    "/BookSummaries/": "reading-companions", "/DeepDives/": "deep-dives", "/handouts.html": "handouts",
}
COLORS = ["cyan", "green", "amber", "indigo", "red"]
GROUP_LEAD = {
    "Learn": "Courses and practice, from a short primer to a multi-module course.",
    "Tools": "Browser tools for the work itself: plans, frameworks, analyses, documents.",
    "Data": "Official Indian data, explored in the browser and listed by source.",
    "Read": "Companions to books, curated readings and printable notes.",
    "Membership": "What is paid, what is free, and everything on the site in one list.",
}


def group_slide(i, name, links):
    cards = []
    for j, (href, label, desc) in enumerate(links):
        key = COUNT_FOR.get(href)
        num = f'<div class="stat-number" style="font-size:26px">{n(key)}</div>' if key else ""
        cards.append(f'<div class="stat-card {COLORS[j % 5]}">{num}'
                     f'<div class="col-panel-title" style="margin:4px 0 6px">{a(href, E(label))}</div>'
                     f'<div class="stat-label">{E(desc)}</div></div>')
    cols = 3 if len(links) > 4 else max(2, len(links))
    lead = GROUP_LEAD.get(name, "")
    # The descriptions are the header's own words, numbers included; the numbers on the
    # cards come from counts.json, so check-counts.py need not read this slide twice.
    return dict(label=f"The menu &middot; {E(name)}", title=E(name), titleSize="lg", blocks=[
        dict(t="body", html=E(lead)),
        dict(t="raw", html=f'<div class="stat-grid c{cols}">{"".join(cards)}</div><!-- count-ignore -->')])


def tiers_table():
    head = ["Plan", "Price", "Adds"]
    rows = []
    for t in TIERS:
        adds = [f for f in t["feats"] if not f.startswith("Everything in")]
        price = t["price"] + (f' <span style="opacity:.75">({E(t["annual"])})</span>' if t["annual"] else "")
        rows.append([f"<strong>{E(t['name'])}</strong><br>{E(t['tag'])}", price,
                     "; ".join(E(f) for f in adds[:4]) + ("; and more" if len(adds) > 4 else "")])
    return dict(t="table", head=head, rows=rows)


def products_table():
    rows = []
    for p in PRODUCTS:
        if not p["prices"]:
            price = "See the page"
        elif len(p["prices"]) == 1:
            price = f"₹{p['prices'][0]:,}"
        else:
            price = f"₹{p['prices'][0]:,} to ₹{p['prices'][-1]:,}"
        rows.append([E(p["name"]), str(p["count"]), price])
    return dict(t="table", head=["Section of the Products page", "Items", "Price"], rows=rows)


WHATS_NEW = """<div id="wt-new" class="stat-grid c3" aria-live="polite"></div>
<p class="slide-body sm" id="wt-new-note" style="margin-top:10px">The newest additions, read from the same list as the homepage. """ + a("/updates#whats-new", "See every change") + """.</p>
<script>
(function(){
  var box=document.getElementById('wt-new');
  if(!box||!window.fetch)return;
  fetch('/data/whats-new.json').then(function(r){return r.json();}).then(function(d){
    var items=(d.items||[]).slice(0,6), cls=['cyan','green','amber','indigo','red','cyan'];
    box.innerHTML=items.map(function(it,i){
      var e=function(s){return String(s||'').replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});};
      return '<div class="stat-card '+cls[i]+'"><div class="stat-source">'+e(it.type)+' &middot; '+e(it.date)+'</div>'+
        '<div class="col-panel-title" style="margin:6px 0"><a href="'+e(it.url)+'">'+e(it.title)+'</a></div>'+
        '<div class="stat-label">'+e(it.desc)+'</div></div>';
    }).join('');
  }).catch(function(){});
})();
</script>"""


def slides():
    S = []
    S.append(dict(type="title", main="ImpactMojo,<br>a walkthrough",
                  sub="Free development education for South Asia: what is on the site, how to find it, "
                      "and what the paid parts add.",
                  tags=["Courses", "Tools", "Data", "Reading", "Membership"]))
    S.append(dict(type="toc", title="What this walkthrough covers", items=[
        {"name": "What ImpactMojo is"}, {"name": "The site, menu by menu"},
        {"name": "Features on every page"}, {"name": "Teaching and organisations"},
        {"name": "Membership and products"}, {"name": "What's new"}]))

    # 1. What it is
    S.append(dict(type="divider", num="01", label="Section one", title="What ImpactMojo is"))
    S.append(dict(label="What ImpactMojo is", title="A free library for people who do development work", blocks=[
        dict(t="twocol", ratio="a32", left=[
            dict(t="body", html="ImpactMojo is a free educational platform for development professionals, NGOs, "
                                "researchers and impact practitioners across South Asia. The courses, tools and "
                                "readings are written by practitioners, with South Asian cases and Indian data."),
            dict(t="bullets", items=[
                "The core library is free and needs no login.",
                "Paid plans and products build on top and never lock the basics away.",
                "Content is released under CC BY-NC-ND 4.0."])],
            right=[dict(t="hbox", color="green",
                        html="<strong>Who it is for.</strong> Programme staff, MEL teams, researchers, students, "
                             "teachers and the organisations that train them.")])]))
    S.append(dict(label="What ImpactMojo is", title="The library in numbers", blocks=[
        dict(t="stats", cols=4, cards=[
            dict(num=str(n("courses")), label="courses across the library"),
            dict(num=str(n("labs")), label="Free Studio tools", color="green"),
            dict(num=str(n("games")), label="games in the Game Library", color="amber"),
            dict(num=str(n("reading-companions")), label="reading companions to key books", color="indigo"),
            dict(num=str(n("data-explorers")), label="Data Room explorers on official data", color="green"),
            dict(num=str(n("deep-dives")), label="Deep Dives, curated readings on one question", color="red"),
            dict(num=str(n("handouts")), label="printable handouts", color="cyan"),
            dict(num=str(n("law-guides")), label="law guides for the social sector", color="amber")]),
        dict(t="body", cls="sm", html="Every number on these slides is read from the site's own count file when the deck is built.")]))

    # 2. Menu
    S.append(dict(type="divider", num="02", label="Section two", title="The site, menu by menu"))
    S.append(dict(label="The menu", title="Five groups at the top of every page", blocks=[
        dict(t="table", head=["Group", "What is in it"],
             rows=[[f"<strong>{E(g)}</strong>", ", ".join(a(h, E(l)) for h, l, _ in ls)] for g, ls in MENU]),
        dict(t="body", cls="sm", html="The footer of every page lists the rest: About, the full catalogue, the roadmap, "
                                     "community, partnerships, help and the legal pages.")]))
    for i, (g, ls) in enumerate(MENU):
        S.append(group_slide(i, g, ls))

    # 3. Features
    S.append(dict(type="divider", num="03", label="Section three", title="Features on every page"))
    S.append(dict(label="Features", title="What works the same way everywhere", blocks=[
        dict(t="twocol", ratio="half", left=[
            dict(t="panel", color="cyan", title="Search",
                 html="Press Ctrl+K or Cmd+K, or the search button, to search courses, tools, readings and data at once."),
            dict(t="panel", color="green", title="Reading settings",
                 html="Light and dark themes, and an OpenDyslexic reading font, from the settings button in the header.")],
            right=[
            dict(t="panel", color="amber", title="Translation",
                 html=f"Pages can be switched into {', '.join(E(x) for x in LANGS)} from the language switch."),
            dict(t="panel", color="indigo", title="Accessibility",
                 html="Core pages target WCAG 2.1 AA, and an automated audit runs over every page each day. "
                      + a("/accessibility.html", "Read the accessibility statement"))])]))
    S.append(dict(label="Features", title="An account is optional, and adds a few things", blocks=[
        dict(t="bullets", items=[
            "Bookmarks, notes and progress tracking across courses.",
            "Free certificates on completion, which anyone can check on " + a("/verify-certificate.html", "Verify a certificate") + ".",
            "Offline reading: pages you have visited open without a connection, and a flagship course can be downloaded.",
            "Nothing in the free library requires an account. " + a("/signup.html", "Create one") + " only if you want these."])]))

    # 4. Teaching
    S.append(dict(type="divider", num="04", label="Section four", title="Teaching and organisations"))
    S.append(dict(label="Teaching", title="Three ways instructors use the material", blocks=[
        dict(t="twocol", ratio="half", left=[
            dict(t="panel", color="cyan", title="Semester companion",
                 html="A flagship course as the backbone, one module a week, with its self-check as a formative test "
                      "and a Studio output as coursework."),
            dict(t="panel", color="green", title="Workshop kit",
                 html="Open with a game, teach from a 101 deck, then run a Studio as the hands-on block. "
                      "No accounts needed.")],
            right=[
            dict(t="panel", color="amber", title="Team cohort",
                 html=f"A team takes a flagship together and finishes on one of {n('challenges')} live case challenges."),
            dict(t="hbox", color="indigo", html=a("/teach.html", "Teach with ImpactMojo") + " maps the courses to syllabi.")])]))
    S.append(dict(label="Teaching", title="Tools for classrooms and LMSs", blocks=[
        dict(t="stats", cols=3, cards=[
            dict(num=str(n("facilitator-kits")), label="facilitator kits for running sessions"),
            dict(num=str(n("challenges")), label="live case challenges with rubrics", color="green"),
            dict(num=str(n("practice-packs")), label="Practice Packs of worked exercises", color="amber")]),
        dict(t="bullets", items=[
            a("/lms-export.html", "LMS Export") + " packages a course as SCORM 1.2, SCORM 2004, Common Cartridge or one offline HTML file, built in your browser.",
            a("/gradebook.html", "Gradebook") + " turns a folder of student Studio submissions into one CSV on your own machine.",
            "Organisations can take the Team Plan for a dashboard of completion, scores and certificates."])]))

    # 5. Membership and products
    S.append(dict(type="divider", num="05", label="Section five", title="Membership and products"))
    S.append(dict(label="Membership", title="The plans, as listed on the Membership page", compact=True, blocks=[
        tiers_table(),
        dict(t="body", cls="sm", html="Prices in Indian rupees, paid by UPI; monthly or annual. "
                                     + a("/premium.html", "Compare the plans") + ".")]))
    S.append(dict(label="Products", title="Files you buy once and keep", blocks=[
        products_table(),
        dict(t="body", cls="sm", html="Products are sold separately from Membership. The courses behind the course notes stay free online. "
                                     + a("/products.html", "Browse the products") + ".")]))
    S.append(dict(label="Services", title="Working with ImpactMojo", blocks=[
        dict(t="bullets", items=[
            "Capacity building and workshops for organisations, alongside the Team Plan.",
            "Partners named on the " + a("/partnerships.html", "partnerships page") + ": " + ", ".join(E(p) for p in PARTNERS) + ".",
            "Contribute content or corrections through " + a("/contribute.html", "Contribute") + "; every known defect is listed on " + a("/known-issues.html", "Known issues") + ".",
            "Write to the team from " + a("/contact.html", "Contact") + "."])]))

    # 6. What's new
    S.append(dict(type="divider", num="06", label="Section six", title="What's new"))
    S.append(dict(label="What's new", title="Recently added", blocks=[dict(t="raw", html=WHATS_NEW)]))

    S.append(dict(type="end", eyebrow="Start anywhere", headline="Everything above is one click from the header",
                  byline="This walkthrough is rebuilt from the site's own data, so it changes when the site does.",
                  ctas=[dict(label="Go to the homepage", href="/"), dict(label="Full catalogue", href="/catalog.html"),
                        dict(label="Membership", href="/premium.html")],
                  meta=["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo"]))
    for s in S:
        for c in s.get("ctas", []):
            LINKS.append(c["href"])
    return S


# ------------------------------------------------------------------ assemble
def build():
    B._CHARTS.clear()
    donor = B.DONOR.read_text(encoding="utf-8")
    head, rest = donor.split(B.VIEWPORT_OPEN, 1)
    _, tail = rest.split(B.VIEWPORT_CLOSE, 1)
    sl = B.apply_auto_toc(slides())
    total = len(sl)
    out_slides = "\n\n".join(B.render_slide(s, i, total, TITLE) for i, s in enumerate(sl, start=1))
    out_slides = (out_slides
                  .replace("ImpactMojo 101 Series &middot; Free Forever", "ImpactMojo &middot; Site walkthrough")
                  .replace("ImpactMojo 101 Series", "ImpactMojo walkthrough")
                  .replace('href="https://www.impactmojo.in/101-courses/" class="logo-mark" target="_blank"',
                           'href="https://www.impactmojo.in/" class="logo-mark"'))

    donor_desc = re.search(r'<meta name="description" content="([^"]*)"', head).group(1)
    # The share block is the donor's; build-social-tags.py writes this page's own below.
    head = re.sub(r"<!-- share:start -->[\s\S]*?<!-- share:end -->",
                  f'<!-- share:start -->\n<meta name="description" content="{E(DESC, quote=True)}">\n<!-- share:end -->', head)
    ld_desc = json.dumps(html.unescape(donor_desc))[1:-1]
    head = head.replace("Development Economics 101 | ImpactMojo", f"{TITLE} | ImpactMojo")
    head = head.replace(f'"name": "Development Economics 101", "description": "{ld_desc}"',
                        f'"name": {json.dumps(TITLE)}, "description": {json.dumps(DESC)}')
    head = head.replace(donor_desc, E(DESC, quote=True))
    head = head.replace("101-courses/dev-economics.html", "walkthrough.html").replace("dev-economics.html", "walkthrough.html")
    head = head.replace(">Development Economics 101<", f">{TITLE}<").replace('content="Development Economics 101"', f'content="{TITLE}"')
    if "Development Economics" in head or "dev-economics" in head:
        fail("the donor deck's title or description is left in <head>")
    head = head.replace('"@type": "Course"', '"@type": "PresentationDigitalDocument"')

    ids = ",".join(f"'s{i}'" for i in range(1, total + 1))
    tail = re.sub(r"const SLIDE_IDS = \[[\s\S]*?\];", f"const SLIDE_IDS = [{ids}];", tail, count=1)
    tail = re.sub(r'<span id="prog-text">1 / \d+</span>', f'<span id="prog-text">1 / {total}</span>', tail)
    # The donor's charts belong to the donor; this deck has none.
    tail = re.sub(
        r"(function initChart\(slideIdx\) \{\s*\n\s*const id = SLIDE_IDS\[slideIdx\];\s*\n\s*const mk = \(id, type, data, opts\) => \{\s*\n\s*const el = document\.getElementById\(id\);\s*\n\s*if \(!el\) return;\s*\n\s*new Chart\(el, \{ type, data, options: \{ \.\.\.CHART_DEFAULTS, \.\.\.opts \} \}\);\s*\n\s*\};\n)[\s\S]*?(\n\}\n\n\n// Theme)",
        lambda m: m.group(1) + "\n" + B.build_chartjs_body() + m.group(2), tail, count=1)
    tail = re.sub(r"(const initECharts = \(\) => \{)[\s\S]*?(\n  \};\n  // Defer until DOM ready)",
                  lambda m: m.group(1) + "\n" + B.build_echarts_body() + m.group(2), tail, count=1)

    # The donor's course-notes buy link sells the donor's notes; this deck sells nothing.
    tail = re.sub(r"<!--notes-101-->[\s\S]*?<!--/notes-101-->", "", tail)
    out = head + B.VIEWPORT_OPEN + "\n\n" + out_slides + "\n\n" + B.VIEWPORT_CLOSE + tail
    out = B._relativise(out)
    out = B._share().apply("walkthrough.html", out)
    bad = sorted({h for h in LINKS if not link_ok(h)})
    if bad:
        fail("links to pages that do not exist: " + ", ".join(bad))
    return out, total


def main():
    out, total = build()
    if "--check" in sys.argv:
        cur = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if cur != out:
            fail("walkthrough.html is stale. Run python3 scripts/build-walkthrough.py and commit the result.")
        print(f"PASS - walkthrough.html is current ({total} slides)")
        return
    OUT.write_text(out, encoding="utf-8")
    print(f"wrote walkthrough.html ({total} slides, {len(out) // 1024} KB)")


if __name__ == "__main__":
    main()
