#!/usr/bin/env python3
"""Add NFHS-6 (2023-24) to the state explorer's data, beside NFHS-4 and NFHS-5.

data/nfhs-state.json holds, for each of 136 indicators and 39 states and union
territories, six values: rural, urban and combined for NFHS-4 (slots 0-2) and
NFHS-5 (slots 3-5), read from MoSPI's eSankhyiki NFHS service. That service
does not carry NFHS-6, so this script adds slots 6-8 (rural, urban, combined)
from data/nfhs6/states.json. That extract was read from IIPS's NFHS-6 India and
State/UT Fact Sheets (May 2026) by how-india-lives/scripts/extract_nfhs6.py,
commit 2f7bff5, and checked there against NFHS-5 and against each state's urban
and rural figures.

An NFHS-6 indicator is joined to an explorer indicator only by its numbers, not
by its name: each NFHS-6 fact sheet reprints the state's NFHS-5 combined figure,
and the join is kept where that reprint matches MoSPI's NFHS-5 figure within
0.15 points in at least 90 per cent of states (74 indicators). Four more match
by name and differ by under a point because IIPS re-tabulated NFHS-5 for the
NFHS-6 sheets; they are listed in RETABULATED and kept. Antenatal care (four
visits) reprints NFHS-5 values up to four points away, which points to a changed
definition, so it is left out. NFHS-6 does not report the other 57 indicators
(anaemia among them), so they carry no NFHS-6 value.

Manipur has no NFHS-6 fact sheet. A value IIPS prints in parentheses (25 to 49
unweighted cases) is marked as a small sample, and only for the combined
figure, which is the one the extract flags.

    python3 scripts/build-nfhs-state-data.py           # writes data/nfhs-state.json
    python3 scripts/build-nfhs-state-data.py --check   # fails if the file is stale
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "nfhs-state.json"
N6 = ROOT / "data" / "nfhs6" / "states.json"

STATE = {"All India": "India", "Andaman & N. Islands": "Andaman & Nicobar Islands",
         "Puduchery": "Puducherry"}
RETABULATED = {
    "Children age 12-23 months fully vaccinated based on information from either vaccination card or mother's recall (%)",
    "Children age 12-23 months who have received the first dose of measles-containing vaccine (MCV) (%)",
    "Ever-married women age 18-49 years who have ever experienced spousal violence (%)",
    "Men age 15 years and above who use any kind of tobacco (%)",
}
EXCLUDED = {"Mothers who had at least 4 antenatal care visits (for last birth in the 5 years before the survey) (%)"}
SLOT = {"rural": 6, "urban": 7, "total": 8}


def build():
    d = json.loads(DATA.read_text())
    n6 = json.loads(N6.read_text())
    I, S, V = d["I"], d["S"], d["V"]
    st6, ind6 = n6["states"], n6["indicators"]

    def fit(i, j):
        tot = agree = 0
        for si, s in enumerate(S):
            k = STATE.get(s[0], s[0])
            if k not in st6 or j not in st6[k]:
                continue
            a, b = V[i][si][5], st6[k][j].get("nfhs5")
            if a is None or b is None:
                continue
            tot += 1
            agree += abs(a - b) <= 0.15
        return (agree / tot if tot else 0), tot

    join = {}
    for i, (name, _g) in enumerate(I):
        if name in EXCLUDED:
            continue
        best = None
        for j, n in ind6.items():
            sc, tot = fit(i, j)
            if tot >= 15 and (best is None or sc > best[0]):
                best = (sc, j)
        if not best:
            continue
        if best[0] >= 0.9:
            join[i] = best[1]
        elif name in RETABULATED and ind6[best[1]].split(" (")[0][:50] == name.split(" (")[0][:50]:
            join[i] = best[1]
    if len(set(join.values())) != len(join):
        sys.exit("FAIL - two explorer indicators joined to one NFHS-6 indicator")
    retab = [I[i][0] for i in join if I[i][0] in RETABULATED]
    if len(retab) != len(RETABULATED):
        sys.exit("FAIL - a re-tabulated indicator no longer joins: %s" % sorted(RETABULATED - set(retab)))

    low = {k: v for k, v in d.get("LOW", {}).items() if int(k.split(",")[2]) < 6}
    filled = 0
    for i in range(len(I)):
        for si, s in enumerate(S):
            row = list(V[i][si][:6]) + [None, None, None]
            j = join.get(i)
            k = STATE.get(s[0], s[0])
            if j is not None and k in st6 and j in st6[k]:
                rec = st6[k][j]
                for col, slot in SLOT.items():
                    row[slot] = rec.get(col)
                    filled += rec.get(col) is not None
                if rec.get("flag") == "few" and rec.get("total") is not None:
                    low["%d,%d,8" % (i, si)] = 1
            V[i][si] = row
    meta = d["meta"]
    meta["rounds"] = ["NFHS-4 (2015-16)", "NFHS-5 (2019-21)", "NFHS-6 (2023-24)"]
    meta["nfhs6"] = {
        "src": "IIPS, NFHS-6 (2023-24) India and State/UT Fact Sheets, May 2026 (MoHFW)",
        "extract": "how-india-lives/scripts/extract_nfhs6.py, commit 2f7bff5",
        "indicators": len(join),
        "retabulated": sorted(retab),
        "excluded": sorted(EXCLUDED),
        "values": filled,
        "note": "Manipur has no NFHS-6 fact sheet. NFHS-6 does not report the other indicators, anaemia among them.",
    }
    d["LOW"] = low
    return json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "\n", len(join), filled


if __name__ == "__main__":
    out, n, filled = build()
    if "--check" in sys.argv:
        if DATA.read_text() != out:
            sys.exit("FAIL - data/nfhs-state.json is stale. Run python3 scripts/build-nfhs-state-data.py")
        print("PASS - nfhs-state.json carries NFHS-6 for %d indicators (%d values)" % (n, filled))
    else:
        DATA.write_text(out)
        print("wrote data/nfhs-state.json: NFHS-6 for %d indicators, %d values" % (n, filled))
