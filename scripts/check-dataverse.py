#!/usr/bin/env python3
"""The Dataverse says how many resources it holds; make that true.

Found on 2026-10-10: four resources were listed twice (Bhuvan and ACLED in
two categories each, Climate Watch and Semantic Scholar twice in one), so the
site said 336 while it held 332 distinct entries. And 106 entries had no row
in data/search-index.json, so site search could not find them. Nothing
compared any of these.

Checks:
  1. every entry id is unique;
  2. meta.totalItems equals the number of entries;
  3. data/counts.json "dataverse" equals the same number;
  4. every entry has a search row linking /dataverse.html#<id>, and no
     search row links an id that no longer exists.
"""
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    dv = json.loads((ROOT / "data" / "dataverse.json").read_text(encoding="utf-8"))
    counts = json.loads((ROOT / "data" / "counts.json").read_text(encoding="utf-8"))
    index = json.loads((ROOT / "data" / "search-index.json").read_text(encoding="utf-8"))

    ids = [i["id"] for c in dv["categories"] for i in c["items"]]
    errors = []
    dup = sorted(k for k, v in Counter(ids).items() if v > 1)
    if dup:
        errors.append("ids listed more than once: " + ", ".join(dup))
    if dv["meta"]["totalItems"] != len(ids):
        errors.append("meta.totalItems is %d, entries %d" % (dv["meta"]["totalItems"], len(ids)))
    if counts.get("dataverse") != len(ids):
        errors.append("counts.json dataverse is %s, entries %d" % (counts.get("dataverse"), len(ids)))

    linked = set()
    for row in index:
        url = row.get("url", "")
        if url.startswith("/dataverse.html#"):
            linked.add(url.split("#", 1)[1])
    missing = sorted(set(ids) - linked)
    stale = sorted(linked - set(ids))
    if missing:
        errors.append("%d entries have no search row: %s" % (len(missing), ", ".join(missing[:10])))
    if stale:
        errors.append("search rows link removed entries: " + ", ".join(stale))

    if errors:
        print("FAIL — Dataverse")
        for e in errors:
            print("  " + e)
        sys.exit(1)
    print("PASS — Dataverse: %d distinct entries, totals agree, every entry is searchable" % len(ids))


if __name__ == "__main__":
    main()
