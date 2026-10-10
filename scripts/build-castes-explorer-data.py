#!/usr/bin/env python3
"""Build the data behind castes.html from the Database of Castes.

Source: Jolad, S. and Kalyani, G., "Database of castes: SC, ST, OBC and 1931
Caste Census", Harvard Dataverse, doi:10.7910/DVN/WT5VIY, version 1.1
(released 9 October 2026), CC0.

Two modes.

  --extract DIR   Read the five workbooks downloaded from Dataverse into DIR
                  and write data/castes-india.json, the raw snapshot. Needs
                  openpyxl. Run once per release of the dataset.
  (default)       Read data/castes-india.json, derive the explorer tables,
                  write data/castes-explorer.json and the inline block in
                  castes.html. Standard library only, so CI can run it.
  --check         As the default, but fail if either output is stale.

Three things here are easy to get wrong, and each one changes a number on
the page without any error:

  1. The OBC "first notified" year in the workbook is the year printed in
     the gazette FILE NUMBER (12011/14/2004-BCC), not the date of the
     resolution ("dt. 12/03/2007"). For 37% of the resolutions that carry a
     date the two differ by one to five years. The page dates each entry by
     the earliest resolution date it carries, and falls back to the file
     year only where no date is printed. Both counts are kept so the gap is
     visible.
  2. A Scheduled Caste entry that matches no 1931 caste name has not been
     shown to be absent in 1931. The match is by spelling, within the 1931
     unit that covered most of the present state. "Matched" is therefore a
     name-match rate, and the page says so. Matches on an alternative name
     alone are kept apart from matches on the main name, because the
     dataset's own README warns they can point to a different community.
  3. Four present-day units (Goa, Dadra & Nagar Haveli, Daman & Diu,
     Puducherry) were outside the 1931 Census of India. Their entries
     cannot match, and are excluded from match rates rather than counted
     as zero.

The 1931 exterior-caste table is checked against its own printed subtotals:
the numbered province rows must sum to "Provinces", the state and agency
rows to "States and Agencies", and the two to "INDIA".
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "castes-india.json"
OUT = ROOT / "data" / "castes-explorer.json"
PAGE = ROOT / "castes.html"
SLOT = re.compile(
    r'(<script id="castes-data" type="application/json">)(.*?)(</script>)', re.S)

FILES = {
    "exterior": "Exterior Caste-Census1931_VolI-PtI.xlsx",
    "sc": "Scheduled_Castes_2000_Linked_to_Boundaries_1931.xlsx",
    "obc": "OBC_Central_List + Mandal Commission list.xlsx",
    "st": "Scheduled_Tribes_by_State_UT.xlsx",
}
# Dataverse file ids, for --extract from a directory of f<id>.xlsx downloads.
IDS = {"exterior": 14317519, "sc": 14317516, "obc": 14317517, "st": 14317524}

SOURCE = {
    "citation": "Jolad, S. and Kalyani, G. (2026). Database of castes: SC, ST, OBC and 1931 Caste Census. Harvard Dataverse, V1.1.",
    "doi": "https://doi.org/10.7910/DVN/WT5VIY",
    "licence": "CC0 1.0",
    "producer": "FLAME Center for Legislative Education and Research, FLAME University, Pune",
}

# "dt. 12/03/2007", "dt.10 /09/1993", "dated 21/09/2000" all occur.
DT = re.compile(r"(?:dt|dated)\.?\s*(\d{1,2})\s*[./-]\s*(\d{1,2})\s*[./-]\s*(\d{2,4})")


def fail(msg):
    sys.exit("FAIL: " + msg)


# ---------------------------------------------------------------- extract

def extract(src_dir):
    import openpyxl  # only needed here

    src = Path(src_dir)

    def path(key):
        for name in (FILES[key], "f%d.xlsx" % IDS[key]):
            if (src / name).exists():
                return src / name
        fail("missing workbook for %s in %s" % (key, src))

    def sheet(key, name):
        ws = openpyxl.load_workbook(path(key), read_only=True)[name]
        rows = list(ws.iter_rows(values_only=True))
        return [r for r in rows[1:] if r and any(v is not None for v in r)]

    def num(v):
        return None if v is None else (int(v) if float(v).is_integer() else float(v))

    exterior = []
    for r in sheet("exterior", "Table B - Provincial Summary"):
        name = (r[0] or "").strip()
        if not name:
            continue
        m = re.match(r"(\d+)\.\s+(.*)", name)
        if m:
            kind, label = "unit", m.group(2)
        elif name.startswith(" ") or r[0] != r[0].lstrip():
            kind, label = "part", name.strip()
        else:
            kind, label = "total", name
        exterior.append({
            "name": label, "kind": kind,
            "population": num(r[1]), "hindu": num(r[2]), "exterior": num(r[3]),
            "printed_pct_hindu": num(r[4]), "printed_pct_total": num(r[5]),
            "pct_literate": num(r[6]) if len(r) > 6 else None,
            "note": (r[7] if len(r) > 7 else None),
        })

    sc = []
    for r in sheet("sc", "SC_List"):
        sc.append({
            "state": r[2], "region": r[1], "entry": r[4],
            "units_1931": r[9], "pop_1931": num(r[11]),
            "match": r[13], "exterior_1931": r[14] == "Yes",
        })

    # Earliest printed resolution date per OBC entry.
    dated = {}
    for r in sheet("obc", "Resolutions"):
        if r[0] is None:
            continue
        m = DT.search(str(r[4] or ""))
        if not m:
            continue
        y = int(m.group(3))
        if y < 100:
            y += 1900 if y > 50 else 2000
        oid = int(r[0])
        dated[oid] = min(y, dated.get(oid, 9999))

    obc = []
    for r in sheet("obc", "OBC_List"):
        oid = int(r[0])
        obc.append({
            "id": oid, "state": r[1], "entry": r[2], "status": r[3],
            "religion": r[8], "file_year": r[12],
            "dated_year": dated.get(oid),
            "pop_1931": num(r[18]), "match_1931": r[19],
        })

    mandal_state = {int(r[0]): r[1] for r in sheet("obc", "Mandal_List")}
    mandal = []
    for r in sheet("obc", "Mandal_vs_NCBC"):
        mid = int(r[0])
        mandal.append({"id": mid, "state": mandal_state.get(mid), "status": r[3]})

    st = Counter()
    for r in sheet("st", "ST_By_State_Long"):
        st[r[0]] += 1

    raw = {
        "_source": SOURCE,
        "_extracted_by": "scripts/build-castes-explorer-data.py --extract",
        "exterior_1931": exterior,
        "sc": sc,
        "obc": obc,
        "mandal_vs_ncbc": mandal,
        "st_rows_by_state": dict(sorted(st.items())),
    }
    RAW.write_text(json.dumps(raw, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("wrote %s: %d exterior rows, %d SC, %d OBC, %d Mandal" % (
        RAW.relative_to(ROOT), len(exterior), len(sc), len(obc), len(mandal)))


# ---------------------------------------------------------------- build

# Two places where the 1931 table as transcribed does not add up, both
# found by this script on 2026-10-10. Pinned so that any new one fails.
#   States and Agencies, population: the rows sum to 79,098,008 and the
#     subtotal reads 79,098,088. The rows are right: with 79,098,008,
#     Provinces + States equals the printed INDIA total exactly.
#   States and Agencies, Hindu: the subtotal agrees with INDIA and the rows
#     are 1,000 short, so one state row is off by one digit in the
#     thousands. A transcription slip or a 1931 misprint; the scan decides.
# Neither moves any percentage on the page.
KNOWN_GAPS = {("States and Agencies", "population"): -80,
              ("States and Agencies", "hindu"): -1000}
KNOWN_INDIA_GAP = {"hindu": -1000}

OUTSIDE_1931 = {"Goa", "Dadra & Nagar Haveli", "Daman & Diu", "Puducherry"}
# State sections on the source page that repeat another state's list.
REPEATS = {"Meghalaya": "Assam", "Mizoram": "Assam"}


def build(raw):
    # 1. Exterior castes, 1931, with the printed subtotals as the check.
    rows = raw["exterior_1931"]
    tot = {r["name"]: r for r in rows if r["kind"] == "total"}
    for k in ("INDIA", "Provinces", "States and Agencies"):
        if k not in tot:
            fail("exterior table lost its %r row" % k)
    units = [r for r in rows if r["kind"] == "unit"]
    if len(units) != 35:
        fail("expected 35 numbered units in Table B, found %d" % len(units))
    prov, states = units[:15], units[15:]
    found = {}
    for part, key in ((prov, "Provinces"), (states, "States and Agencies")):
        for col in ("population", "hindu", "exterior"):
            s = sum(r[col] or 0 for r in part)
            if s != tot[key][col]:
                found[(key, col)] = s - tot[key][col]
    if found != KNOWN_GAPS:
        fail("1931 Table B subtotals: expected gaps %s, found %s" % (KNOWN_GAPS, found))
    # Whatever the subtotals say, the rows must add up to the printed INDIA
    # figure in every column except the one known row error.
    for col in ("population", "hindu", "exterior"):
        s = sum(r[col] or 0 for r in units) - tot["INDIA"][col]
        if s != KNOWN_INDIA_GAP.get(col, 0):
            fail("1931 Table B %s: rows differ from INDIA by %d" % (col, s))

    ext_units = []
    for r in units:
        if not r["exterior"]:  # Burma: no exterior count printed
            continue
        ext_units.append({
            "name": r["name"],
            "group": "Province" if r in prov else "State or agency",
            "population": r["population"], "hindu": r["hindu"], "exterior": r["exterior"],
            "pct_hindu": round(100 * r["exterior"] / r["hindu"], 1),
            "pct_total": round(100 * r["exterior"] / r["population"], 1),
            "pct_literate": r["pct_literate"],
        })
    ext_units.sort(key=lambda r: -r["pct_hindu"])
    parts = [{"name": r["name"], "population": r["population"], "hindu": r["hindu"],
              "exterior": r["exterior"],
              "pct_hindu": round(100 * r["exterior"] / r["hindu"], 1)}
             for r in rows if r["kind"] == "part"]
    india = tot["INDIA"]
    burma = [r for r in units if not r["exterior"]]

    # 2. SC lists traced to 1931.
    by_state = defaultdict(list)
    for r in raw["sc"]:
        by_state[r["state"]].append(r)
    sc_states = []
    for state, rs in by_state.items():
        n = len(rs)
        main = sum(1 for r in rs if r["match"] in ("main name", "alternative name & main name"))
        alt = sum(1 for r in rs if r["match"] == "alternative name")
        ext = sum(1 for r in rs if r["exterior_1931"])
        sc_states.append({
            "state": state, "region": rs[0]["region"], "entries": n,
            "units_1931": None if state in OUTSIDE_1931 else rs[0]["units_1931"],
            "main_name": main, "alt_only": alt, "exterior_1931": ext,
            "outside_1931": state in OUTSIDE_1931,
            "repeats": REPEATS.get(state),
        })
    sc_states.sort(key=lambda r: (r["outside_1931"], -r["entries"]))
    inside = [r for r in sc_states if not r["outside_1931"]]
    sc_total = {
        "entries": sum(r["entries"] for r in sc_states),
        "entries_in_1931_units": sum(r["entries"] for r in inside),
        "main_name": sum(r["main_name"] for r in inside),
        "alt_only": sum(r["alt_only"] for r in inside),
        "exterior_1931": sum(r["exterior_1931"] for r in inside),
    }
    if sum(r["main_name"] + r["alt_only"] for r in sc_states if r["outside_1931"]):
        fail("an entry outside the 1931 Census has a 1931 match")

    # 3. OBC Central List, dated by resolution.
    active = [r for r in raw["obc"] if r["status"] == "Active"]
    if len(active) != 2428:
        fail("expected 2,428 active OBC entries, found %d" % len(active))
    def year(r):
        return r["dated_year"] or r["file_year"]
    for r in active:
        if r["dated_year"] and r["file_year"] and not 0 <= r["dated_year"] - r["file_year"] <= 5:
            fail("OBC entry %d dated %d against file year %d: check the date parser"
                 % (r["id"], r["dated_year"], r["file_year"]))
    undated = sum(1 for r in active if not r["dated_year"])
    by_year_dated = Counter(year(r) for r in active if year(r))
    by_year_file = Counter(r["file_year"] for r in active if r["file_year"])
    moved = sum(1 for r in active if r["dated_year"] and r["file_year"]
                and r["dated_year"] != r["file_year"])
    years = sorted(set(by_year_dated) | set(by_year_file))
    obc_growth = [{"year": y, "dated": by_year_dated.get(y, 0), "file": by_year_file.get(y, 0)}
                  for y in years]
    first = min(years)
    obc_states = defaultdict(lambda: {"active": 0, "first_list": 0, "later": 0,
                                      "muslim": 0, "christian": 0})
    for r in active:
        s = obc_states[r["state"]]
        s["active"] += 1
        if year(r) == first:
            s["first_list"] += 1
        elif year(r):
            s["later"] += 1
        rel = r["religion"] or ""
        s["muslim"] += "Muslim" in rel
        s["christian"] += "Christian" in rel
    obc_states = [dict(state=k, **v) for k, v in obc_states.items()]
    obc_states.sort(key=lambda r: -r["active"])
    obc_total = {
        "active": len(active),
        "first_year": first,
        "first_list": sum(1 for r in active if year(r) == first),
        "later": sum(1 for r in active if year(r) and year(r) != first),
        "undated": undated, "moved": moved,
        "muslim": sum(1 for r in active if "Muslim" in (r["religion"] or "")),
        "christian": sum(1 for r in active if "Christian" in (r["religion"] or "")),
        "last_year": max(years),
    }

    # 4. Mandal (1980) against today's Central List.
    order = ["Same names", "NCBC entry all within Mandal entry (Mandal wider)",
             "Mandal names all in one NCBC entry (NCBC wider)", "Covered by several NCBC entries",
             "Partial: some names shared", "No match", "State / UT not in OBC_List"]
    mc = Counter(r["status"] for r in raw["mandal_vs_ncbc"])
    if set(mc) - set(order):
        fail("unknown Mandal match status: %s" % (set(mc) - set(order)))
    mandal = [{"status": s, "entries": mc.get(s, 0)} for s in order]

    return {
        "_source": raw["_source"],
        "_built_by": "scripts/build-castes-explorer-data.py",
        "exterior": {
            "india": {k: india[k] for k in ("population", "hindu", "exterior")},
            "provinces": {k: tot["Provinces"][k] for k in ("population", "hindu", "exterior")},
            "states": {k: tot["States and Agencies"][k] for k in ("population", "hindu", "exterior")},
            "units": ext_units, "parts": parts,
            "no_count": [r["name"] for r in burma],
            "row_error_hindu": -KNOWN_INDIA_GAP["hindu"],
            "pages": "Census of India 1931, Vol. I, Part I, Appendix I, pp. 474-494",
        },
        "sc": {"total": sc_total, "states": sc_states,
               "outside_1931": sorted(OUTSIDE_1931)},
        "obc": {"total": obc_total, "growth": obc_growth, "states": obc_states},
        "mandal": {"entries": sum(mc.values()), "status": mandal},
        "st_rows_by_state": raw["st_rows_by_state"],
    }


def main():
    args = sys.argv[1:]
    if args[:1] == ["--extract"]:
        if len(args) < 2:
            fail("--extract needs the directory holding the workbooks")
        extract(args[1])
        return
    check = "--check" in args
    raw = json.loads(RAW.read_text(encoding="utf-8"))
    data = build(raw)
    out = json.dumps(data, ensure_ascii=False, indent=1) + "\n"
    inline = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = PAGE.read_text(encoding="utf-8")
    if not SLOT.search(page):
        fail("castes.html has no castes-data slot")
    new_page = SLOT.sub(lambda m: m.group(1) + inline + m.group(3), page, count=1)
    if check:
        stale = []
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != out:
            stale.append(str(OUT.relative_to(ROOT)))
        if new_page != page:
            stale.append("castes.html inline data")
        if stale:
            fail("stale: %s. Run python3 scripts/build-castes-explorer-data.py" % ", ".join(stale))
        print("PASS — castes explorer data current; 1931 exterior table agrees with its printed totals")
        return
    OUT.write_text(out, encoding="utf-8")
    PAGE.write_text(new_page, encoding="utf-8")
    t = data["obc"]["total"]
    print("wrote %s and castes.html: %d exterior units, %d SC states, %d OBC entries (%d dated differently from file year)"
          % (OUT.relative_to(ROOT), len(data["exterior"]["units"]), len(data["sc"]["states"]),
             t["active"], t["moved"]))


if __name__ == "__main__":
    main()
