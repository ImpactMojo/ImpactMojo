#!/usr/bin/env python3
"""Every 101 deck is listed, and every listing gives its real slide count.

Found on 2026-10-10: twelve of the twenty decks added that month were missing
from data/decks.json, which the partner API serves as the deck catalogue, and
eight were missing from catalog_data.json. Six slide counts were wrong where
they were stated: Development Finance has 116 slides and its card and
catalogue entry said 100; CSR & ESG has 100 and said 88; four more said 100
against 102 to 107. Nothing compared a listing with the deck it describes.

Checks, for every /101-courses/<slug>.html deck on disk:
  1. data/decks.json has an entry, its slide count is the deck's, and
     meta.count and meta.totalSlides add up;
  2. catalog_data.json links it;
  3. the card on 101-courses/index.html states the deck's slide count;
  4. the catalog.html entry states the deck's slide count;
  5. no two catalog.html entries share an id.
A slide is a <div class="slide ..."> carrying an id="sN".
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECKS = ROOT / "101-courses"
SLIDE = re.compile(r'<div class="slide[ "][^>]*id="(s\d+)"')


def main():
    disk = {}
    for p in sorted(DECKS.glob("*.html")):
        if p.name == "index.html":
            continue
        disk[p.stem] = len(set(SLIDE.findall(p.read_text(encoding="utf-8"))))

    errors = []
    dj = json.loads((ROOT / "data" / "decks.json").read_text(encoding="utf-8"))
    listed = {d["slug"]: d for d in dj["decks"]}
    for slug, n in disk.items():
        d = listed.get(slug)
        if not d:
            errors.append("decks.json: no entry for %s" % slug)
        elif d.get("slides") != n:
            errors.append("decks.json: %s says %s slides, deck has %d" % (slug, d.get("slides"), n))
    for slug in set(listed) - set(disk):
        errors.append("decks.json: %s has no deck file" % slug)
    if dj["meta"].get("count") != len(dj["decks"]):
        errors.append("decks.json: meta.count %s, entries %d" % (dj["meta"].get("count"), len(dj["decks"])))
    total = sum(d.get("slides", 0) for d in dj["decks"])
    if dj["meta"].get("totalSlides") != total:
        errors.append("decks.json: meta.totalSlides %s, entries sum to %d" % (dj["meta"].get("totalSlides"), total))

    cd = (ROOT / "catalog_data.json").read_text(encoding="utf-8")
    index = (DECKS / "index.html").read_text(encoding="utf-8")
    catalog = (ROOT / "catalog.html").read_text(encoding="utf-8")
    for slug, n in disk.items():
        url = "/101-courses/%s.html" % slug
        if '"%s"' % url not in cd:
            errors.append("catalog_data.json: no entry for %s" % slug)
        k = index.find('href="%s"' % url)
        if k < 0:
            errors.append("101 index: no card for %s" % slug)
        else:
            card = index[max(0, k - 300):k + 900]
            stated = set(int(x) for x in re.findall(r"(\d+) slides", card[300:]))
            if stated and stated != {n}:
                errors.append("101 index: %s card says %s slides, deck has %d" % (slug, sorted(stated), n))
        m = re.search(r"\{ id: '[^']+'[^}]*?url: '%s'" % re.escape(url), catalog)
        if not m:
            errors.append("catalog.html: no entry for %s" % slug)
        else:
            s = re.search(r"slides: (\d+)", m.group(0))
            if s and int(s.group(1)) != n:
                errors.append("catalog.html: %s says %s slides, deck has %d" % (slug, s.group(1), n))

    # The catalogue's bookmark and compare features key on these ids, so two
    # entries sharing one are bookmarked together. Three pairs did.
    dup = sorted(k for k, v in Counter(re.findall(r"\{ id: '([^']+)'", catalog)).items() if v > 1)
    if dup:
        errors.append("catalog.html: ids used more than once: " + ", ".join(dup))

    if errors:
        print("FAIL — 101 deck listings")
        for e in errors:
            print("  " + e)
        sys.exit(1)
    print("PASS — %d decks, each listed in decks.json, catalog_data.json, the 101 index and the catalogue with its real slide count" % len(disk))


if __name__ == "__main__":
    main()
