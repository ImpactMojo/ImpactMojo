#!/usr/bin/env python3
"""Write the travel survey explorer's inline data and check the tables agree.

    python3 scripts/build-nhts-explorer-data.py           # write nhts.html's inline block
    python3 scripts/build-nhts-explorer-data.py --check   # CI: fail if stale or inconsistent

data/nhts-india.json holds the figures of the National Household Travel Survey
(NSO, July 2025 to June 2026), transcribed by hand from the press note of
5 October 2026. nhts.html carries the same figures inline, so the two copies
can drift; this script writes the page's copy from the file and fails when
they differ.

It also checks the transcription against the note itself, because a misread
digit renders as a confident chart:

  * every person figure lies between the male and female figures beside it;
  * the overnight bus and rail shares add to the 73.5% the note states, and
    the departure bands add to its 82.0% and 94.9%;
  * the headline numbers in the note's text equal the table cells they quote;
  * each mode table's columns add to between 99.5% and 102%. They do not add
    to 100: every column of Tables 2 and 4 sums to about 101 as printed. The
    note does not say why, and the page says so rather than rescaling.

The state and UT figures come from the NSO's own spreadsheets, the 17 tables
of the factsheet's Appendix A, read once with

    python3 scripts/build-nhts-explorer-data.py --extract DIR   # needs openpyxl

where DIR holds the downloaded Table_N.xlsx files. Extraction refuses to write
unless each table's all-India row equals the all-India figure already in the
file from the press note, and the ordinary run checks the same thing again,
so the two sources cannot drift apart without failing CI. The urban metro
shares the note's text quotes for Maharashtra, West Bengal and Delhi must
equal their cells in the state table too. The state mode shares add to as much
as 103.4% as printed (Andaman and Nicobar students in rural areas), so the
sum check allows 98 to 104 there.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "nhts-india.json"
PAGE = ROOT / "nhts.html"
SLOT = re.compile(r'(<script id="nhts-data" type="application/json">)(.*?)(</script>)', re.S)


def fail(msg):
    sys.exit("FAIL: " + msg)


def close(a, b, tol=0.051):
    return abs(a - b) <= tol


def between(p, m, f):
    return min(m, f) - 0.051 <= p <= max(m, f) + 0.051


SECTORS = ("Rural", "Urban", "Rural+Urban")
# Table 1 as published: its state rows add to 6 villages, 47 households and
# 190 rural persons fewer than its own all-India row. The urban columns agree
# exactly. Pinned, so a different gap fails.
TABLE1_GAP = 190
# Table number, column holding the Person figure (0-based after the name), key.
SCALARS = [
    (2, 3, "students_travelling"),   # all (6 years and above)
    (4, 3, "workers_travelling"),    # all (15 years and above)
    (10, 8, "student_minutes"),      # average minutes to the institution
    (11, 8, "worker_minutes"),       # average minutes to a fixed workplace
]
MODE_COLUMNS = ["Walk", "Bicycle", "Cycle or pull rickshaw", "Two-wheeler", "Car",
                "Auto-rickshaw", "Bus", "Train, monorail or tram", "Rail", "Water",
                "Air", "Others"]


def num(v):
    if v is None or (isinstance(v, str) and v.strip() in ("-", "")):
        return None
    return float(v)


def extract(src_dir):
    """Read the NSO state tables into the shape data/nhts-india.json keeps."""
    import glob
    import openpyxl

    def sheet(n):
        found = glob.glob(str(Path(src_dir) / ("*Table_%d.xlsx" % n)))
        found = [f for f in found if "RSE" not in f]
        if len(found) != 1:
            fail("expected one Table_%d.xlsx in %s, found %d" % (n, src_dir, len(found)))
        return openpyxl.load_workbook(found[0], data_only=True).worksheets[0]

    def blocks(n):
        """Yield (sector, sex, {state: [values]}) for a nine-block table."""
        rows = list(sheet(n).iter_rows(values_only=True))
        out, i = {}, 0
        while i < len(rows):
            r = rows[i]
            if r and r[0] in SECTORS and i + 1 < len(rows) and rows[i + 1][0] in ("Male", "Female", "Person"):
                sector, sex, data = r[0], rows[i + 1][0], {}
                j = i + 2
                while j < len(rows) and not (rows[j][0] or "").startswith("Table"):
                    name = rows[j][0]
                    if isinstance(name, str) and name.strip() and not name.startswith(("State", "(")) and rows[j][1] is not None:
                        data[name.strip()] = [num(v) for v in rows[j][1:] if v is not None]
                    j += 1
                out[(sector, sex)] = data
                i = j
            else:
                i += 1
        if len(out) != 9:
            fail("Table %d: found %d sector and sex blocks, expected 9" % (n, len(out)))
        return out

    st = {"_table": ("Appendix A of the factsheet, State/UT Tables 1 to 13, read from the NSO's "
                     "spreadsheets. Figures are for persons. A dash in the source, meaning no "
                     "estimate, is kept as null."),
          "sectors": list(SECTORS), "mode_columns": MODE_COLUMNS}
    for n, col, key in SCALARS:
        b = blocks(n)
        st[key] = {sec: {k: v[col] for k, v in b[(sec, "Person")].items()} for sec in SECTORS}
    for n, key in ((3, "student_modes"), (5, "worker_modes")):
        b = blocks(n)
        st[key] = {sec: {k: v[:12] for k, v in b[(sec, "Person")].items()} for sec in SECTORS}
    for n, key in ((12, "student_cost"), (13, "worker_cost")):
        st[key] = {sec: {} for sec in SECTORS}
        for r in sheet(n).iter_rows(values_only=True):
            name = r[0]
            if isinstance(name, str) and len(r) >= 10 and isinstance(r[9], (int, float)):
                vals = [num(v) for v in r[1:10]]
                for k, sec in enumerate(SECTORS):
                    st[key][sec][name.strip()] = vals[3 * k + 2]
    st["persons_surveyed"] = {}
    for r in sheet(1).iter_rows(values_only=True):
        if isinstance(r[0], str) and len(r) >= 13 and isinstance(r[12], (int, float)):
            st["persons_surveyed"][r[0].strip()] = int(num(r[8]) or 0) + int(num(r[12]) or 0)
    names = sorted(k for k in st["students_travelling"]["Rural+Urban"] if k != "all-India")
    st["names"] = names
    return st


def state_checks(d):
    problems = []
    st = d.get("states")
    if not st:
        return ["no state block"]
    names = st["names"]
    if len(names) != 36:
        problems.append("expected 36 states and UTs, found %d" % len(names))
    for key in ("students_travelling", "workers_travelling", "student_minutes", "worker_minutes",
                "student_cost", "worker_cost", "student_modes", "worker_modes"):
        for sec in SECTORS:
            have = set(st[key][sec])
            if have != set(names) | {"all-India"}:
                problems.append("%s %s: states differ from the list (%s)" % (key, sec, sorted(have ^ (set(names) | {"all-India"}))[:4]))
    if set(st["persons_surveyed"]) != set(names) | {"all-India"}:
        problems.append("persons surveyed: states differ from the list")
    elif st["persons_surveyed"]["all-India"] != d["sample"]["persons"]:
        problems.append("persons surveyed all-India %d != note's %d" % (st["persons_surveyed"]["all-India"], d["sample"]["persons"]))
    elif d["sample"]["persons"] - sum(v for k, v in st["persons_surveyed"].items() if k != "all-India") != TABLE1_GAP:
        problems.append("persons surveyed by state fall short of the all-India total by other than the %d the source shows" % TABLE1_GAP)
    # Each table's all-India row against the press note's own figure.
    for sec in SECTORS:
        a = lambda key: st[key][sec]["all-India"]
        pairs = [
            ("students travelling", a("students_travelling"), d["students_travelling"]["rows"][sec]["Person"][2]),
            ("workers travelling", a("workers_travelling"), d["workers_travelling"]["rows"][sec]["Person"][2]),
            ("student minutes", a("student_minutes"), d["travel_time"]["average_minutes"]["students"][sec]),
            ("worker minutes", a("worker_minutes"), d["travel_time"]["average_minutes"]["workers"][sec]),
            ("student cost", a("student_cost"), d["monthly_cost"]["students"][sec]),
            ("worker cost", a("worker_cost"), d["monthly_cost"]["workers"][sec]["Person"]),
        ]
        col = SECTORS.index(sec) + 1
        for row in d["worker_modes"]["rows"]:
            pairs.append(("worker mode %s" % row[0], a("worker_modes")[MODE_COLUMNS.index(row[0])], row[col]))
        if sec == "Rural+Urban":
            for row in d["student_modes"]["rows"]:
                pairs.append(("student mode %s" % row[0], a("student_modes")[MODE_COLUMNS.index(row[0])], row[3]))
        for name, got, want in pairs:
            if got is None or not close(got, want):
                problems.append("%s %s: state table all-India %s, note %s" % (name, sec, got, want))
        for key in ("student_modes", "worker_modes"):
            for nm, row in st[key][sec].items():
                vals = [v for v in row if v is not None]
                if vals and not 98.0 <= sum(vals) <= 104.0:
                    problems.append("%s %s %s sums to %.1f" % (key, sec, nm, sum(vals)))
    for nm, v in d["urban_mass_transit"]["states"]:
        got = st["worker_modes"]["Urban"].get(nm, [None] * 8)[7]
        if got is None or not close(got, v):
            problems.append("urban metro share %s: state table %s, note text %s" % (nm, got, v))
    return problems


def checks(d):
    problems = state_checks(d)
    for key in ("students_travelling", "workers_travelling"):
        for sector, row in d[key]["rows"].items():
            for i, age in enumerate(d[key]["ages"]):
                m, f, p = row["Male"][i], row["Female"][i], row["Person"][i]
                if not between(p, m, f):
                    problems.append("%s %s %s: person %.1f not between %.1f and %.1f" % (key, sector, age, p, m, f))
    for sector, row in d["monthly_cost"]["workers"].items():
        if not between(row["Person"], row["Male"], row["Female"]):
            problems.append("monthly cost %s: person outside male and female" % sector)
    for key in ("student_modes", "worker_modes"):
        t = d[key]
        for j, col in enumerate(t["columns"]):
            s = sum(r[j + 1] for r in t["rows"])
            if not 99.5 <= s <= 102.0:
                problems.append("%s column %s sums to %.1f" % (key, col, s))
    for who in ("students", "workers"):
        for sector, bands in d["travel_time"][who].items():
            if not 97.0 <= sum(bands) <= 100.05:
                problems.append("travel time %s %s sums to %.1f" % (who, sector, sum(bands)))
    o = d["overnight"]
    bus = dict(o["modes"])
    if not close(bus["Bus"] + bus["Railway"], o["bus_and_rail"]):
        problems.append("overnight bus + rail != %.1f" % o["bus_and_rail"])
    dep = d["departure"]
    if not close(sum(v for _, v in dep["students"]), dep["students_7_to_10"], 0.11):
        problems.append("student departure bands do not add to %.1f" % dep["students_7_to_10"])
    if not close(sum(v for _, v in dep["workers"]), dep["workers_before_10"], 0.11):
        problems.append("worker departure bands do not add to %.1f" % dep["workers_before_10"])
    # Headline sentences in the note against the cells they quote.
    wm = {r[0]: r for r in d["worker_modes"]["rows"]}
    sm = {r[0]: r for r in d["student_modes"]["rows"]}
    heads = [
        ("two-wheeler share of workers, all India", wm["Two-wheeler"][3], 42.6),
        ("two-wheeler share of workers, rural", wm["Two-wheeler"][1], 37.1),
        ("two-wheeler share of workers, urban", wm["Two-wheeler"][2], 52.3),
        ("students walking", sm["Walk"][3], 37.0),
        ("students by bus", sm["Bus"][3], 29.5),
        ("students by bicycle", sm["Bicycle"][3], 15.8),
        ("students travelling 1 km", d["students_travelling"]["rows"]["Rural+Urban"]["Person"][2], 66.4),
        ("workers travelling 1 km", d["workers_travelling"]["rows"]["Rural+Urban"]["Person"][2], 57.6),
        ("male workers travelling", d["workers_travelling"]["rows"]["Rural+Urban"]["Male"][2], 61.9),
        ("female workers travelling", d["workers_travelling"]["rows"]["Rural+Urban"]["Female"][2], 41.9),
        ("worker monthly cost", d["monthly_cost"]["workers"]["Rural+Urban"]["Person"], 785),
    ]
    for name, got, want in heads:
        if not close(got, want):
            problems.append("%s: table says %s, note text says %s" % (name, got, want))
    s = d["sample"]
    if (s["households"], s["persons"]) != (492023, 2034371):
        problems.append("sample size differs from the note")
    return problems


def main():
    check = "--check" in sys.argv[1:]
    raw = json.loads(RAW.read_text(encoding="utf-8"))
    if "--extract" in sys.argv[1:]:
        raw["states"] = extract(sys.argv[sys.argv.index("--extract") + 1])
        problems = state_checks(raw)
        if problems:
            fail("state tables disagree with the press note:\n  " + "\n  ".join(problems))
        # Keep the hand-laid national block as written; the state block goes last,
        # one state per line.
        text = RAW.read_text(encoding="utf-8")
        cut = text.find(',\n  "states": ')
        text = (text[:cut] if cut >= 0 else text.rstrip().rstrip("}").rstrip()) 
        block = json.dumps(raw["states"], ensure_ascii=False, indent=2)
        block = re.sub(r"\[\s+([^\[\]{}]*?)\s+\]", lambda m: "[" + re.sub(r",\s+", ", ", m.group(1)) + "]", block)
        block = re.sub(r"\n", "\n  ", block)
        RAW.write_text(text + ',\n  "states": ' + block + "\n}\n", encoding="utf-8")
        if json.loads(RAW.read_text(encoding="utf-8")) != raw:
            fail("rewritten data/nhts-india.json does not parse back to the same data")
        print("wrote %d states and UTs into %s" % (len(raw["states"]["names"]), RAW.relative_to(ROOT)))
    problems = checks(raw)
    if problems:
        fail("data/nhts-india.json disagrees with the press note:\n  " + "\n  ".join(problems))
    inline = json.dumps(raw, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = PAGE.read_text(encoding="utf-8")
    if not SLOT.search(page):
        fail("nhts.html has no nhts-data slot")
    new_page = SLOT.sub(lambda m: m.group(1) + inline + m.group(3), page, count=1)
    if check:
        if new_page != page:
            fail("nhts.html inline data is stale. Run python3 scripts/build-nhts-explorer-data.py")
        print("PASS — travel survey explorer data current; tables agree with the press note")
        return
    PAGE.write_text(new_page, encoding="utf-8")
    print("wrote nhts.html inline data from %s" % RAW.relative_to(ROOT))


if __name__ == "__main__":
    main()
