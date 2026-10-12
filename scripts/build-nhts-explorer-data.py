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


def checks(d):
    problems = []
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
