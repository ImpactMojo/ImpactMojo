#!/usr/bin/env python3
"""Write the 'Data retrieved' line on every data explorer page.

Reads data/explorer-freshness.json and puts one line after the page's lede,
between <!-- data-retrieved:begin --> and <!-- data-retrieved:end -->. An
explorer with no date recorded gets empty markers, so the line appears the
day its date is recorded and no date is ever invented.

    python3 scripts/build-explorer-freshness.py           # write
    python3 scripts/build-explorer-freshness.py --check   # fail if a page is stale
"""
import datetime as dt
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
rows = json.loads((ROOT / "data" / "explorer-freshness.json").read_text(encoding="utf-8"))["explorers"]
BEGIN, END = "<!-- data-retrieved:begin -->", "<!-- data-retrieved:end -->"
LEDE = re.compile(r'(<p class="(?:ph-)?lede"[^>]*>.*?</p>)', re.S)
BLOCK = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)


def human(iso):
    d = dt.date.fromisoformat(iso)
    return "%d %s %d" % (d.day, d.strftime("%B"), d.year)


def line(e):
    parts = []
    if e.get("retrieved"):
        parts.append("Data retrieved %s." % human(e["retrieved"]))
    if e.get("as_of_date"):
        parts.append("%s %s." % (e["as_of_label"], human(e["as_of_date"])))
    if not parts:
        return BEGIN + END
    return '%s\n<p class="data-retrieved" style="font-size:.9rem;margin:.6rem 0 0">%s</p>\n%s' % (
        BEGIN, html.escape(" ".join(parts)), END)


def render(text, e):
    block = line(e)
    if BEGIN in text:
        return BLOCK.sub(lambda m: block, text, count=1)
    m = LEDE.search(text)
    if not m:
        raise SystemExit("%s: no <p class=\"lede\"> to put the line after" % e["page"])
    return text[:m.end()] + "\n" + block + text[m.end():]


def main():
    check = "--check" in sys.argv
    stale = []
    for e in rows:
        p = ROOT / e["page"]
        old = p.read_text(encoding="utf-8")
        new = render(old, e)
        if new != old:
            stale.append(e["page"])
            if not check:
                p.write_text(new, encoding="utf-8")
    if check:
        if stale:
            print("FAIL - the Data retrieved line is stale on: " + ", ".join(stale))
            print("Run: python3 scripts/build-explorer-freshness.py")
            return 1
        print("PASS - the Data retrieved line is current on %d explorer pages" % len(rows))
        return 0
    print("wrote the Data retrieved line on %d pages" % len(stale))
    return 0


if __name__ == "__main__":
    sys.exit(main())
