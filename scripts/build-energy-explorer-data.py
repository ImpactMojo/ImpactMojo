#!/usr/bin/env python3
"""Write the inline data block in energy.html from data/energy-india.json.

The figures are transcribed from Energy Statistics India 2026 (NSO, MoSPI).
This script is the only thing that should change `window.ENERGY_DATA` in the
page, and it refuses to write unless the state rows agree with the
publication's own all-India rows.

Checks, each against a total the source prints:

  * renewable potential (Table 1.4): the 35 state rows plus the "Others" row
    must equal the All India Total, within printed rounding;
  * installed renewables (Table 2.5): the same, against Total (MW). Each row
    total is rounded to the megawatt, so a gap of a few MW is expected;
  * installed capacity (Table 2.4): the state rows must equal "Total States",
    and Total States plus Total Central must equal Total All India, within
    the conversion to GW;
  * coal reserves (Table 1.1): the state rows must equal the All India Total.

Jammu and Kashmir and Ladakh are one row in Table 1.4 and two in Table 2.5;
the data file adds the two Table 2.5 rows so every measure covers the same
area, and keeps the parts so the addition can be checked here.

The energy-intensity series changes GDP base year in 2022-23 (Table 8.1 says
so). The page draws it as two segments and never joins them.

Usage:
    python3 scripts/build-energy-explorer-data.py          # write the page
    python3 scripts/build-energy-explorer-data.py --check  # fail if stale
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "energy-india.json"
PAGE = ROOT / "energy.html"
SLOT = re.compile(r"(window\.ENERGY_DATA=)(\{.*?\n\})(;\n</script>)", re.S)

# Tolerances are the most the printed rounding can explain, not slack.
TOL = {"re_potential_mw": 2, "re_installed_mw": 18, "capacity_gw": 0.2,
       "coal_mt": 8}


def fail(msg):
    sys.exit("build-energy-explorer-data: " + msg)


def check(d):
    st = d["states"]
    ai = d["all_india"]
    if len(st) != 35 or len({s["name"] for s in st}) != 35:
        fail("expected 35 distinct state and UT rows")

    def total(key):
        return sum(s[key] for s in st if s[key] is not None)

    pairs = [
        ("re_potential_mw", total("re_potential_mw") + ai["re_potential_others_mw"], ai["re_potential_mw"]),
        ("re_installed_mw", total("re_installed_mw") + ai["re_installed_others_mw"], ai["re_installed_mw"]),
        ("re_installed_mw", total("re_installed_mw_2024") + ai["re_installed_others_mw"], ai["re_installed_mw_2024"]),
        ("capacity_gw", total("capacity_gw"), ai["capacity_states_gw"]),
        ("capacity_gw", total("capacity_gw_2024"), ai["capacity_states_gw_2024"]),
        ("capacity_gw", ai["capacity_states_gw"] + ai["capacity_central_gw"], ai["capacity_gw"]),
        ("capacity_gw", ai["capacity_states_gw_2024"] + ai["capacity_central_gw_2024"], ai["capacity_gw_2024"]),
        ("coal_mt", total("coal_mt"), ai["coal_mt"]),
        ("coal_mt", total("coal_mt_2024"), ai["coal_mt_2024"]),
    ]
    for key, got, want in pairs:
        if abs(got - want) > TOL[key]:
            fail(f"{key}: rows add to {got:,.2f} against a printed total of {want:,.2f}")

    for s in st:
        parts = s.get("re_installed_parts")
        if parts:
            if sum(v[1] for v in parts.values()) != s["re_installed_mw"] or \
               sum(v[0] for v in parts.values()) != s["re_installed_mw_2024"]:
                fail(f"{s['name']}: parts do not add to the combined row")

    tr = d["trend"]
    n = len(tr["years"])
    for k, se in tr["series"].items():
        if len(se["values"]) != n:
            fail(f"trend {k}: {len(se['values'])} values for {n} years")
    brk = tr["series"]["eint"].get("break_at")
    if brk not in tr["years"]:
        fail("energy intensity break year is not one of the trend years")


def payload(d):
    ai = d["all_india"]
    tr = d["trend"]
    se = tr["series"]
    meta = {
        "src": "Energy Statistics India 2026 (FY 2024-25, provisional), MoSPI",
        "snap": "31 March 2025",
        "trendYears": tr["years"],
        "breaks": {"eint": {"at": tr["years"].index(se["eint"]["break_at"]),
                            "note": se["eint"]["break_note"]}},
    }
    national = {
        "cap": se["cap"]["values"][-1], "gen": se["gen"]["values"][-1],
        "cons": se["cons"]["values"][-1], "reCap": ai["re_installed_mw"],
        "rePot": ai["re_potential_mw"], "percapElec": se["pcelec"]["values"][-1],
        "percapElec0": se["pcelec"]["values"][0],
        "ceaPercap": d["cea_comparison"]["per_capita_kwh"],
    }
    metrics = {
        "pot": {"nat": ai["re_potential_mw"]},
        "reinst": {"nat": ai["re_installed_mw"]},
        "cap": {"nat": ai["capacity_gw"], "stateSum": ai["capacity_states_gw"],
                "central": ai["capacity_central_gw"]},
        "coal": {"nat": ai["coal_mt"]},
    }
    d1 = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
    lines = ["{",
             ' "meta":' + d1(meta) + ",",
             ' "national":' + d1(national) + ",",
             ' "metrics":{']
    lines.append(",\n".join(f'   "{k}":{d1(v)}' for k, v in metrics.items()))
    lines += [" },", ' "states":{']
    rows = []
    for i, s in enumerate(d["states"], 1):
        rows.append(f'   "{i}":' + d1({"n": s["name"], "pot": s["re_potential_mw"],
                                         "reinst": s["re_installed_mw"],
                                         "cap": s["capacity_gw"], "coal": s["coal_mt"]}))
    lines.append(",\n".join(rows))
    lines += [" },", ' "trend":{']
    lines.append(",\n".join(f'   "{k}":{d1(v["values"])}' for k, v in se.items()))
    lines += [" }", "}"]
    js = "\n".join(lines)
    if "</" in js or " " in js or " " in js:
        fail("data would end or break the script block")
    return js


def main():
    d = json.loads(SRC.read_text(encoding="utf-8"))
    check(d)
    js = payload(d)
    html = PAGE.read_text(encoding="utf-8")
    m = SLOT.search(html)
    if not m:
        fail("could not find window.ENERGY_DATA in energy.html")
    if "--check" in sys.argv:
        if m.group(2) != js:
            fail("energy.html is stale; run python3 scripts/build-energy-explorer-data.py")
        print("PASS energy explorer data matches data/energy-india.json")
        return
    PAGE.write_text(html[:m.start(2)] + js + html[m.end(2):], encoding="utf-8")
    print("wrote energy.html data block")


if __name__ == "__main__":
    main()
