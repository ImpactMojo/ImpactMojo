#!/usr/bin/env python3
"""Reshape the NCRB disposal tables into one table for crime.html.

The same total-row trap as the prisons data: every NCRB table carries
'Total (States)', 'Total (UTs)' and 'Total (All India)', so summing a column
returns exactly three times the real figure. Totals are read from the total
row, the parts are summed separately, and the build refuses to write if the
two disagree.

The input is data/crime-india.json, written by scripts/fetch-crime-data.py from
the Crime in India PDFs. Fields are mapped by NCRB's printed column number.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "crime-india.json"
OUT = ROOT / "data" / "crime-explorer.json"
PAGE = ROOT / "crime.html"

SLOT = re.compile(
    r'(<script id="crime-data" type="application/json">)(.*?)(</script>)', re.S)

# Columns by the number NCRB prints over them ([3], [4] ...). The layout is
# the same in all twelve state-wise disposal tables of Crime in India 2024, and
# scripts/fetch-crime-data.py has already checked every table's printed
# arithmetic, so a column read against the wrong number would have failed
# there. The build re-checks the totals below anyway.
POLICE_FIELDS = {
    "reported": 4,               # cases reported during the year
    "for_investigation": 6,      # total cases for investigation
    "chargesheeted": 18,         # cases charge-sheeted (col 16 + col 17)
    "pending_police": 22,        # pending investigation at the end of the year
    "chargesheeting_rate": 23,   # col 18 / col 19 * 100
    "police_pendency": 24,       # col 22 / col 6 * 100
}
COURT_FIELDS = {
    "for_trial": 5,              # total cases for trial
    "convicted": 15,             # cases convicted (col 13 + col 14)
    "acquitted": 17,
    "trials_completed": 18,      # col 15 + col 16 + col 17
    "pending_court": 20,         # pending trial at the end of the year
    "conviction_rate": 21,       # col 15 / col 18 * 100
    "court_pendency": 22,        # col 20 / col 5 * 100
}

ALIAS = {"nct of delhi": "delhi", "orissa": "odisha", "pondicherry": "puducherry",
         "uttaranchal": "uttarakhand", "a n island": "andaman nicobar island",
         "dadra nagar haveli": "dadra nagar haveli daman diu",
         "daman diu": "dadra nagar haveli daman diu"}


def norm(s):
    s = (s or "").lower().strip().replace("&", " and ")
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[^a-z]+", " ", s).strip()
    s = re.sub(r"\band\b", " ", s)
    s = re.sub(r"\bislands?\b", "island", s)
    s = re.sub(r"\but\b|\bstate\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def key(s):
    k = norm(s)
    return ALIAS.get(k, k)


def num(x):
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return float(x)
    t = str(x).strip().replace(",", "")
    if t in ("", "NA", "N/A", "-", "--"):
        return None
    try:
        return float(t)
    except ValueError:
        return None


def read_stage(block, mapping):
    """({state key: {field: value, name}}, {field: all-India value})."""
    if not block:
        return None, None
    real = {}
    for r in block["rows"]:
        vals = {short: num(r["cols"].get(str(col))) for short, col in mapping.items()}
        real[key(r["name"])] = dict(vals, name=r["name"])
    total = {short: num(block["totals"]["india"].get(str(col)))
             for short, col in mapping.items()}
    return real, total


def payload_for_page(d):
    js = json.dumps(d, ensure_ascii=True, separators=(",", ":"))
    assert "</" not in js, "data contains a tag close; would end the script block"
    return js


def sync_page(js, check_only):
    if not PAGE.exists():
        print(f"FAIL - {PAGE.name} is missing")
        return 1
    html = PAGE.read_text(encoding="utf-8")
    m = SLOT.search(html)
    if not m:
        print(f'FAIL - no <script id="crime-data"> block in {PAGE.name}')
        return 1
    if m.group(2) == js:
        print(f"  {PAGE.name} data is current")
        return 0
    if check_only:
        print(f"FAIL - {PAGE.name} carries stale data. Run "
              "`python3 scripts/build-crime-explorer-data.py`.")
        return 1
    PAGE.write_text(html[:m.start(2)] + js + html[m.end(2):], encoding="utf-8")
    print(f"  injected {len(js):,} bytes into {PAGE.name}")
    return 0


def main():
    check_only = "--check" in sys.argv
    raw = json.loads(SRC.read_text(encoding="utf-8"))

    pop = {}
    for r in raw["series"]["population"]["rows"]:
        p = num(r.get("population_2011"))
        k = key(r["india___state__union_territory"])
        if p and k != "india":
            pop[k] = pop.get(k, 0) + p

    tracks = {}
    for name, t in raw["tracks"].items():
        pol, pol_tot = read_stage(t.get("police"), POLICE_FIELDS)
        crt, crt_tot = read_stage(t.get("court"), COURT_FIELDS)

        # The double-count guard, per stage. Summing a column that contains
        # Total (States), Total (UTs) and Total (All India) returns 3x.
        counts = [("police", pol, pol_tot, f) for f in POLICE_FIELDS
                  if not f.endswith(("_rate", "_pendency"))]
        counts += [("court", crt, crt_tot, f) for f in COURT_FIELDS
                   if not f.endswith(("_rate", "_pendency"))]
        for stage, real, total, field in counts:
            if real is None:
                continue
            if total is None:
                print(f"FAIL - {name}/{stage}: no 'Total (All India)' row, so the "
                      "double-count guard cannot be trusted. Check the source.")
                return 1
            parts = sum(v.get(field) or 0 for v in real.values())
            whole = total.get(field)
            if whole is None or parts != whole:
                print(f"FAIL - {name}/{stage}: states sum to {parts:,.0f} on "
                      f"'{field}' but the source's own total says "
                      f"{(whole or 0):,.0f}.")
                return 1

        states = []
        for k in sorted(set(list(pol or {}) + list(crt or {}))):
            p = (pol or {}).get(k, {})
            c = (crt or {}).get(k, {})
            row = {"name": p.get("name") or c.get("name"),
                   "population_2011": pop.get(k)}
            for f in POLICE_FIELDS:
                row[f] = p.get(f)
            for f in COURT_FIELDS:
                row[f] = c.get(f)
            states.append(row)

        national = {}
        for f in POLICE_FIELDS:
            national[f] = (pol_tot or {}).get(f)
        for f in COURT_FIELDS:
            national[f] = (crt_tot or {}).get(f)

        tracks[name] = {
            "label": t["label"],
            "has_court": crt is not None,
            "national": national,
            "states": sorted(states, key=lambda s: s["name"] or ""),
        }

    out = {
        "_source": raw["_source"],
        "_licence": raw["_licence"],
        "_fetched": raw["_fetched"],
        "_year": raw["_year"],
        "_documents": raw["_documents"],
        "_built_by": "scripts/build-crime-explorer-data.py",
        "_caveats": [
            "Registered crime measures reporting as much as it measures crime. "
            "Whether an incident becomes a case depends on whether the person "
            "harmed goes to a police station and whether that station writes it "
            "down, and both vary enormously between states. A state with more "
            "registered cases may be a state where reporting works.",
            "This page therefore ranks states on what happened to the cases they "
            "did register -- chargesheeting, conviction, how much is still "
            "pending -- rather than on how much crime they have.",
            "Conviction rate here is convictions as a share of trials completed "
            "in the year, which is how NCRB defines it. It is not the share of "
            "reported cases that end in a conviction: most cases are still "
            "pending, and they are counted in the pendency figures instead.",
            "Cases pending at the end of the year include cases carried over "
            "from previous years, so a state can charge-sheet everything it "
            "received and still show high pendency from an older backlog.",
            "The Bharatiya Nyaya Sanhita replaced the Indian Penal Code on 1 July "
            "2024. NCRB reports cases under the two codes together as IPC/BNS, so "
            "the general category here covers both.",
            "In NCRB's table of police disposal of crime against senior citizens "
            "(Table 6A.4), the total of cases for investigation is smaller than the "
            "sum of its own parts in 13 states and union territories, by 140 cases "
            "nationally. The rest of that table, including pendency, is built on the "
            "printed total, so the printed total is used here.",
        ],
        "tracks": tracks,
    }

    js = payload_for_page(out)
    serialised = json.dumps(out, ensure_ascii=False, indent=1)
    if check_only:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != serialised:
            print(f"FAIL - {OUT.name} is stale. Run "
                  "`python3 scripts/build-crime-explorer-data.py`.")
            return 1
        print(f"  {OUT.name} is current")
    else:
        OUT.write_text(serialised, encoding="utf-8")
    rc = sync_page(js, check_only)
    if rc:
        return rc

    print("PASS" if check_only else f"wrote {OUT.relative_to(ROOT)}")
    for name, t in tracks.items():
        n = t["national"]
        print(f"  {t['label']:36s} {len(t['states'])} states  "
              f"reported {(n.get('reported') or 0):>9,.0f}  "
              f"chargesheet {(n.get('chargesheeting_rate') or 0):5.1f}%  "
              + (f"conviction {(n.get('conviction_rate') or 0):5.1f}%"
                 if t["has_court"] else "no state-wise court data"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
