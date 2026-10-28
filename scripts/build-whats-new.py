#!/usr/bin/env python3
"""Build the home page's "Recently added" list from the release notes.

The list used to be written by hand in index.html, so it went stale the day
after each release. It is now drawn from the "### For Learners" notes in
docs/changelog.md: every note whose bold title matches a page in
data/search-index.json becomes an item, with the note's first sentence as its
description. Notes about features ("One menu on every page") match no single
page and are left out, which is the point: the list carries things to open.

Writes:
  data/whats-new.json   the pool: items from releases in the WINDOW_DAYS before
                        the newest release, newest first. Only known kinds of
                        page count (courses, guides, companions, Deep Dives,
                        blog posts and so on), never a section's own index. The home page picks
                        from it each day (index.html, "Recently added").
  index.html            the newest SHOWN items between the whats-new markers,
                        so a reader without JavaScript sees a current list.

Usage:
  python3 scripts/build-whats-new.py           write both
  python3 scripts/build-whats-new.py --check   fail if either is out of date
"""
import datetime
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHANGELOG = ROOT / "docs" / "changelog.md"
INDEX = ROOT / "data" / "search-index.json"
OUT = ROOT / "data" / "whats-new.json"
HOME = ROOT / "index.html"
WINDOW_DAYS = 30
SHOWN = 7
START, END = "<!-- whats-new:start -->", "<!-- whats-new:end -->"

# Label and colour family by address. The families are the home page's three
# tints: blue (t-course), violet (t-101), slate (t-law).
KINDS = [
    ("/courses/", "Flagship course", "t-course"),
    ("/101-courses/", "101 course", "t-101"),
    ("/law-guides/", "Law guide", "t-law"),
    ("/booksummaries/", "Reading companion", "t-101"),
    ("/deepdives/", "Deep Dive", "t-course"),
    ("/code/", "Code School", "t-course"),
    ("/labs/", "Free Studio", "t-law"),
    ("/premium-tools/", "Pro Studio", "t-law"),
    ("/games/", "Simulation", "t-101"),
    ("/practice-packs/", "Practice Pack", "t-course"),
    ("/datanotes/", "Data Note", "t-law"),
    ("/theories/", "Theory", "t-101"),
    ("/blog/", "Blog post", "t-course"),
    ("/survey-instruments.html", "Library", "t-law"),
]
MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July", "August",
     "September", "October", "November", "December"], 1)}


def kind(url):
    low = url.lower()
    for prefix, label, cls in KINDS:
        if low.startswith(prefix):
            return label, cls
    return None, None


def first_sentence(text, limit=150):
    text = re.sub(r"\s+", " ", text).strip()
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    if len(s) > limit:
        s = s[:limit].rsplit(" ", 1)[0].rstrip(",;") + "."
    return s[:1].upper() + s[1:]


def resolve(title, entries):
    t = title.lower()
    exact = [e for e in entries if e["title"].lower() == t]
    if exact:
        return exact[0]
    for e in entries:
        et = e["title"].lower()
        if et.startswith(t) and et[len(t):len(t) + 1] in (" ", "(", ":"):
            return e
    return None


def build():
    entries = [e for e in json.loads(INDEX.read_text()) if e.get("url", "").startswith("/")]
    releases = re.split(r"^## ", CHANGELOG.read_text(), flags=re.M)[1:]
    items, seen, newest = [], set(), None
    for rel in releases:
        head = rel.split("\n", 1)[0]
        m = re.search(r"([A-Z][a-z]+) (\d{1,2}), (\d{4})", head)
        if not m or m.group(1) not in MONTHS:
            continue
        date = datetime.date(int(m.group(3)), MONTHS[m.group(1)], int(m.group(2)))
        newest = newest or date
        if (newest - date).days > WINDOW_DAYS:
            break
        block = re.search(r"### For Learners\n(.*?)(?=\n### |\Z)", rel, re.S)
        if not block:
            continue
        for title, desc in re.findall(r"^- \*\*(.+?)\*\*\s*[—:-]\s*(.+)$", block.group(1), re.M):
            e = resolve(title, entries)
            if not e or e["url"] in seen:
                continue
            label, cls = kind(e["url"])
            # Only things to open: a known kind of page, not a section's own
            # index (/Games/, /code/), and not a note about a change ("Now opens
            # with ...").
            if not label or re.fullmatch(r"/[^/]+/(index\.html)?", e["url"]) or desc.lower().startswith("now "):
                continue
            seen.add(e["url"])
            items.append({"title": title, "desc": first_sentence(desc), "url": e["url"],
                          "type": label, "cls": cls, "date": date.isoformat()})
    return {"source": "docs/changelog.md, For Learners notes that match a page",
            "window_days": WINDOW_DAYS, "items": items}


def li(it):
    esc = lambda s: html.escape(s, quote=True)
    return (f'      <li class="{it["cls"]}"><a href="{esc(it["url"])}"><span class="h-type">{esc(it["type"])}</span>'
            f'<span class="h-title">{esc(it["title"])}</span><span class="h-desc">{esc(it["desc"])}</span></a></li>')


def newest_mixed(items, n=SHOWN, per_kind=3):
    """The newest items, at most per_kind of any one kind, so a release of
    seven companions does not fill the list. index.html applies the same rule
    to its daily pick."""
    out, count = [], {}
    for it in items:
        if count.get(it["type"], 0) < per_kind:
            out.append(it)
            count[it["type"]] = count.get(it["type"], 0) + 1
        if len(out) == n:
            break
    return out


def render_home(data, page):
    a, b = page.index(START), page.index(END)
    body = "\n".join(li(it) for it in newest_mixed(data["items"]))
    return page[:a + len(START)] + "\n" + body + "\n      " + page[b:]


def main():
    data = build()
    out = json.dumps(data, indent=1, ensure_ascii=False) + "\n"
    page = HOME.read_text()
    new_page = render_home(data, page)
    if "--check" in sys.argv:
        bad = []
        if not OUT.exists() or OUT.read_text() != out:
            bad.append("data/whats-new.json")
        if page != new_page:
            bad.append("index.html (the Recently added list)")
        if len(data["items"]) < SHOWN:
            bad.append(f"only {len(data['items'])} items in the last {WINDOW_DAYS} days; the home page shows {SHOWN}")
        if bad:
            print("FAIL - out of date: " + "; ".join(bad) + "\nRun: python3 scripts/build-whats-new.py")
            sys.exit(1)
        print(f"PASS - {len(data['items'])} recent items, home page list current")
        return
    OUT.write_text(out)
    HOME.write_text(new_page)
    print(f"wrote data/whats-new.json ({len(data['items'])} items) and the home page list")


if __name__ == "__main__":
    main()
