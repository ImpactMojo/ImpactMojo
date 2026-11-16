#!/usr/bin/env python3
"""District Lineage Explorer: keep the page's inline data equal to the snapshot.

    python3 scripts/build-districts-explorer-data.py           # write districts.html's inline block
    python3 scripts/build-districts-explorer-data.py --check   # CI: fail if stale or inconsistent
    python3 scripts/build-districts-explorer-data.py --extract DIR

data/districts-india.json is a snapshot of four tables published by India State
Stories (Shivakumar Jolad and Mehr Kalra, FLAME University,
https://www.indiastatestory.in/datadownloads):

    District_Timeseries_1951-2024.csv            one row per line of descent
    District_splits_and_carveouts_1951_to_2024.csv
    New_districts_created_1951_to_2024.csv
    District_name_changes_1951_to_2021.csv

--extract reads them from a folder. The copies used here came from the public
mirror github.com/yashveeeeeeer/india-geodata (data/census/historical), and the
splits table was compared with the authors' own Google Sheet.

What this script changes in the source, all of it listed in FIXES and shown on
the page: three duplicate rows in the crosswalk are dropped, the 2024 state of
one row reads "Visakhapatnam" and is set to Andhra Pradesh, and five 2024 rows
that say "Delhi" are set to "NCT of Delhi" to match the other nine. Leading and
trailing spaces are removed. Nothing else is altered: spellings, and years that
fall outside their own decade, are kept as printed and flagged.

Before writing anything it checks:

  - the crosswalk has 640 districts in 2011, the Census of India's own count,
    and 466, 412 and 356 in 1991, 1981 and 1971;
  - 2001 has 592 against the census's 593, a gap pinned in KNOWN so that any
    other figure fails;
  - every row of the crosswalk names a state and a district in all eight years;
  - the number of rows whose year lies outside its decade equals the pinned
    count, so a new one is noticed.
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "districts-india.json"
PAGE = ROOT / "districts.html"
SLOT = re.compile(r'(<script id="dl-data" type="application/json">)(.*?)(</script>)', re.S)
YEARS = [1951, 1961, 1971, 1981, 1991, 2001, 2011, 2024]
CENSUS = {1971: 356, 1981: 412, 1991: 466, 2011: 640}
KNOWN = {"districts_2001": 592, "census_2001": 593, "duplicate_rows": 3}
FIXES = [
    "Three duplicate rows in the crosswalk were dropped.",
    "One 2024 row gave its state as Visakhapatnam; it is set to Andhra Pradesh.",
    "Five 2024 rows gave the state as Delhi; they are set to NCT of Delhi, as the other nine rows have it.",
]


def fail(msg):
    sys.exit("FAIL: " + msg)


def rows(path):
    r = list(csv.reader(open(path, encoding="utf-8-sig")))
    return [[c.strip() for c in x] for x in r[1:] if any(c.strip() for c in x)]


def year(s):
    m = re.match(r"(\d{4})", s)
    return int(m.group(1)) if m else None


def extract(src):
    src = Path(src)
    t = rows(src / "District_Timeseries_1951-2024.csv")
    seen, links_raw, dups = set(), [], 0
    for r in t:
        r = r[:16]
        if r[14] == "Visakhapatnam":
            r[14] = "Andhra Pradesh"
        if r[14] == "Delhi":
            r[14] = "NCT of Delhi"
        k = tuple(r)
        if k in seen:
            dups += 1
            continue
        seen.add(k)
        links_raw.append(r)
    units, index = [[] for _ in YEARS], [{} for _ in YEARS]
    links = []
    for r in links_raw:
        row = []
        for i in range(8):
            key = (r[2 * i], r[2 * i + 1])
            if key not in index[i]:
                index[i][key] = len(units[i])
                units[i].append(list(key))
            row.append(index[i][key])
        links.append(row)
    splits = [[r[0], r[1], year(r[2]), r[3], r[4]] for r in rows(src / "District_splits_and_carveouts_1951_to_2024.csv")]
    created = [[r[0], r[1], year(r[2]), r[3], r[4]] for r in rows(src / "New_districts_created_1951_to_2024.csv")]
    renames = [[r[0], r[1], r[2], r[3], r[4]] for r in rows(src / "District_name_changes_1951_to_2021.csv")]
    out = {
        "_note": "Snapshot of four India State Stories tables. Rebuild with "
                 "scripts/build-districts-explorer-data.py --extract; do not edit by hand.",
        "source": {
            "name": "India State Stories, FLAME University (Shivakumar Jolad and Mehr Kalra)",
            "url": "https://www.indiastatestory.in/datadownloads",
            "copy": "https://github.com/yashveeeeeeer/india-geodata/tree/main/data/census/historical",
        },
        "duplicates_dropped": dups,
        "fixes": FIXES,
        "years": YEARS,
        "units": units,
        "links": links,
        "splits": splits,
        "created": created,
        "renames": renames,
    }
    RAW.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print("wrote %s: %d lines of descent, %d split rows, %d creation rows, %d renamings" % (
        RAW.relative_to(ROOT), len(links), len(splits), len(created), len(renames)))


def off_decade(table):
    n = 0
    for r in table:
        m = re.match(r"(\d{4})-(\d{4})", r[1])
        if r[2] is None or not m or not (int(m.group(1)) <= r[2] <= int(m.group(2))):
            n += 1
    return n


def validate(d):
    p = []
    counts = {y: len(u) for y, u in zip(d["years"], d["units"])}
    for y, n in CENSUS.items():
        if counts[y] != n:
            p.append("%d has %d districts, the Census of India counted %d" % (y, counts[y], n))
    if counts[2001] != KNOWN["districts_2001"]:
        p.append("2001 has %d districts; %d is the pinned figure (census: %d)" % (
            counts[2001], KNOWN["districts_2001"], KNOWN["census_2001"]))
    if d["duplicates_dropped"] != KNOWN["duplicate_rows"]:
        p.append("%d duplicate rows dropped, %d expected" % (d["duplicates_dropped"], KNOWN["duplicate_rows"]))
    for i, u in enumerate(d["units"]):
        if any(not s or not n for s, n in u):
            p.append("%d: a blank state or district" % d["years"][i])
        if len({tuple(x) for x in u}) != len(u):
            p.append("%d: a district listed twice" % d["years"][i])
    for r in d["links"]:
        if len(r) != 8 or any(not (0 <= r[i] < len(d["units"][i])) for i in range(8)):
            p.append("a line of descent points outside the district lists")
            break
    if len({tuple(r) for r in d["links"]}) != len(d["links"]):
        p.append("duplicate lines of descent")
    if any(s == "Visakhapatnam" or s == "Delhi" for s, _ in d["units"][7]):
        p.append("the 2024 state fixes were not applied")
    for name, pin in (("splits", OFF["splits"]), ("created", OFF["created"])):
        n = off_decade(d[name])
        if n != pin:
            p.append("%s: %d rows have a year outside their decade, %d pinned" % (name, n, pin))
    return p


OFF = {"splits": 6, "created": 3}  # rows whose printed year lies outside their decade; shown flagged on the page


def main():
    if "--extract" in sys.argv:
        i = sys.argv.index("--extract")
        if len(sys.argv) <= i + 1:
            fail("--extract needs the folder holding the four CSV files")
        extract(sys.argv[i + 1])
    d = json.loads(RAW.read_text(encoding="utf-8"))
    if "--report" in sys.argv:
        print({y: len(u) for y, u in zip(d["years"], d["units"])}, off_decade(d["splits"]), off_decade(d["created"]))
        return
    problems = validate(d)
    if problems:
        fail("data/districts-india.json is inconsistent:\n  " + "\n  ".join(problems[:20]))
    payload = json.dumps({k: v for k, v in d.items() if k != "_note"},
                         ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = PAGE.read_text(encoding="utf-8")
    m = SLOT.search(page)
    if not m:
        fail("districts.html has no dl-data slot")
    if "--check" in sys.argv:
        if m.group(2) != payload:
            fail("districts.html inline data is stale. Run python3 scripts/build-districts-explorer-data.py")
        print("PASS: districts.html matches data/districts-india.json (%d lines of descent; 2011 has the census's "
              "640 districts)" % len(d["links"]))
        return
    PAGE.write_text(page[:m.start(2)] + payload + page[m.end(2):], encoding="utf-8")
    print("wrote districts.html inline data from %s" % RAW.relative_to(ROOT))


if __name__ == "__main__":
    main()
