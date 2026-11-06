#!/usr/bin/env python3
"""Read the NCRB case-disposal tables into data/crime-india.json.

    python3 scripts/fetch-crime-data.py VOL1.pdf VOL2.pdf VOL3.pdf

This explorer deliberately covers what happens to a case after it is
registered, and leaves aside how much crime a state has. Registered crime is a
measure of how willing people are to go to a police station and how willing
that station is to write it down, and comparing states on it says more about
reporting than about safety. Chargesheeting, conviction and pendency describe
the machinery handling the cases it did receive, which is a question the data
can answer.

Source: National Crime Records Bureau, Crime in India 2024, the three volumes
as published on ncrb.gov.in. The 2023 snapshot came from data.gov.in, which did
not carry the 2024 tables when this was written, so the twelve state-wise
tables are read from the PDFs instead:

    police disposal  17A.2 (IPC/BNS), 3A.6, 7A.4, 7C.4, 9A.5, 6A.4
    court disposal   18A.2 (IPC/BNS), 3A.8, 7A.6, 7C.6, 9A.7, 6A.6

The PDFs are not committed. Their SHA-256 is recorded and must match, so a
different printing is refused rather than read. Each table is checked before
anything is written:

  * every page carries all 36 serial numbers and NCRB's three total rows;
  * for every count column, the 28 states add to 'TOTAL STATE(S)', the 8 UTs
    to 'TOTAL UT(S)', and the two to 'TOTAL ALL INDIA';
  * the arithmetic NCRB prints in the column headings holds for every row
    (for example cases for investigation = pending from last year + reported +
    reopened, and the chargesheeting rate = chargesheeted / disposed of).

Crime in India 2024 is the first edition to straddle the new criminal laws:
the Bharatiya Nyaya Sanhita replaced the IPC on 1 July 2024, and NCRB reports
the two together as 'IPC/BNS'. The population series (Census 2011, from
data.gov.in) is carried over unchanged from the previous snapshot.
"""
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "crime-india.json"
YEAR = 2024

DOCS = {
    "vol1": ("https://www.ncrb.gov.in/uploads/files/1CrimeinIndia2024-VolumeI.pdf",
             "900349a1ba4a2564046a56f4eb03494c3e872221244c9a4e819842d710c4478b",
             "Crime in India 2024, Volume I"),
    "vol2": ("https://www.ncrb.gov.in/uploads/files/2CrimeinIndia2024-VolumeII.pdf",
             "423af46b6704338d9241fc95411fbca706b70662e79becdd4dc8f7ab0c16ae50",
             "Crime in India 2024, Volume II"),
    "vol3": ("https://www.ncrb.gov.in/uploads/files/3CrimeinIndia2024-VolumeIII.pdf",
             "44d813b8935b186645fdba1d299f865a00057706ad225f5d857b1e09e0a7a898",
             "Crime in India 2024, Volume III"),
}

# (document, table) for each stage of each track the page offers.
TRACKS = {
    "ipc": {"label": "All IPC and BNS crime",
            "police": ("vol3", "17A.2", "Police Disposal of IPC/BNS Crime Cases (State/UT-wise) - 2024"),
            "court": ("vol3", "18A.2", "Court Disposal of IPC/BNS Crime Cases (State/UT-wise) - 2024")},
    "women": {"label": "Crime against women",
              "police": ("vol1", "3A.6", "Police Disposal of Crime against Women (State/UT-wise) - 2024"),
              "court": ("vol1", "3A.8", "Court Disposal of Crime against Women (State/UT-wise) - 2024")},
    "sc": {"label": "Atrocities against Scheduled Castes",
           "police": ("vol2", "7A.4", "Police Disposal of Crime/Atrocities against Scheduled Caste(s) (State/UT-wise) - 2024"),
           "court": ("vol2", "7A.6", "Court Disposal of Crime/Atrocities against Scheduled Caste(s) (State/UT-wise) - 2024")},
    "st": {"label": "Atrocities against Scheduled Tribes",
           "police": ("vol2", "7C.4", "Police Disposal of Crime/Atrocities against Scheduled Tribe(s) (State/UT-wise) - 2024"),
           "court": ("vol2", "7C.6", "Court Disposal of Crime/Atrocities against Scheduled Tribe(s) (State/UT-wise) - 2024")},
    "cyber": {"label": "Cyber crime",
              "police": ("vol2", "9A.5", "Police Disposal of Cyber Crime Cases (State/UT-wise) - 2024"),
              "court": ("vol2", "9A.7", "Court Disposal of Cyber Crime Cases (State/UT-wise) - 2024")},
    "senior": {"label": "Crime against senior citizens",
               "police": ("vol2", "6A.4", "Police Disposal of Crime against Senior Citizen (State/UT-wise) - 2024"),
               "court": ("vol2", "6A.6", "Court Disposal of Crime against Senior Citizen (State/UT-wise) - 2024")},
}

# Every NCRB state-wise table uses the same 36 serial numbers.
NAMES = {1: "Andhra Pradesh", 2: "Arunachal Pradesh", 3: "Assam", 4: "Bihar",
         5: "Chhattisgarh", 6: "Goa", 7: "Gujarat", 8: "Haryana", 9: "Himachal Pradesh",
         10: "Jharkhand", 11: "Karnataka", 12: "Kerala", 13: "Madhya Pradesh",
         14: "Maharashtra", 15: "Manipur", 16: "Meghalaya", 17: "Mizoram", 18: "Nagaland",
         19: "Odisha", 20: "Punjab", 21: "Rajasthan", 22: "Sikkim", 23: "Tamil Nadu",
         24: "Telangana", 25: "Tripura", 26: "Uttar Pradesh", 27: "Uttarakhand",
         28: "West Bengal", 29: "Andaman and Nicobar Islands", 30: "Chandigarh",
         31: "Dadra and Nagar Haveli and Daman and Diu", 32: "Delhi",
         33: "Jammu and Kashmir", 34: "Ladakh", 35: "Lakshadweep", 36: "Puducherry"}
# The first letters of the printed name, to catch a row read against the
# wrong serial. Serial 31 prints its name on the lines around the figures.
PRINTED = {29: "a&n", 31: "", 32: "delhi", 33: "jammu"}

POLICE_COLS, COURT_COLS = 22, 20          # columns [3] onwards
POLICE_RATES, COURT_RATES = {23, 24}, {21, 22}

# Gaps in NCRB's own arithmetic, pinned so that any other gap fails. In Table
# 6A.4 (police disposal, crime against senior citizens) column 6, 'Total Cases
# for Investigation (Col.3+Col.4+Col.5)', is smaller than the sum it names in
# 13 rows, by 140 cases nationally. Column 6 is the one the rest of the table
# is built on: pending at year end (col 22 = col 6 - 9 - 19 - 20) and the
# pendency percentage (col 22 / col 6) both agree with it, so it is used as
# printed and the page says so. The gap is computed minus printed.
KNOWN_GAPS = {
    ("6A.4", "col6"): {
        "Andhra Pradesh": 15, "Chhattisgarh": 1, "Goa": 1, "Haryana": 2,
        "Himachal Pradesh": 1, "Jharkhand": 1, "Karnataka": 20, "Kerala": 22,
        "Rajasthan": 5, "Telangana": 48, "West Bengal": 16,
        "Andaman and Nicobar Islands": 1, "Delhi": 7,
        "states": 132, "uts": 8, "india": 140},
}

NUM = r"(?:-?\d+(?:\.\d+)?|-|NA)"
TOTALS = {"TOTAL STATE(S)": "states", "TOTAL UT(S)": "uts", "TOTAL ALL INDIA": "india"}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def text(pdf):
    return subprocess.run(["pdftotext", "-layout", pdf, "-"], check=True,
                          capture_output=True, text=True).stdout


def cell(s):
    if s in ("-", "NA"):
        return None
    return float(s) if "." in s else int(s)


def read_table(txt, tid):
    """{serial: {col: value}}, {'states'|'uts'|'india': {col: value}}."""
    pages = [p for p in txt.split("\f")
             if re.search(r"TABLE\s+" + re.escape(tid) + r"\s+Page \d+ of \d+", p)]
    if not pages:
        raise SystemExit(f"FAIL - table {tid}: no pages found")
    rows, tots = {}, {}
    for p in pages:
        hdr = [ln for ln in p.splitlines() if re.match(r"^\s*\[1\]\s+\[2\]", ln)]
        if len(hdr) != 1:
            raise SystemExit(f"FAIL - table {tid}: no column-number row on a page")
        cols = [int(c) for c in re.findall(r"\[(\d+)\]", hdr[0])][2:]
        n = len(cols)
        pat_row = re.compile(r"^\s*(\d{1,2})\s+(.*?)\s*((?:" + NUM + r"\s+){%d}" % (n - 1)
                             + NUM + r")\s*$")
        pat_tot = re.compile(r"^\s*(TOTAL STATE\(S\)|TOTAL UT\(S\)|TOTAL ALL INDIA)\s+((?:"
                             + NUM + r"\s+){%d}" % (n - 1) + NUM + r")\s*$")
        seen, seen_t = set(), set()
        for ln in p.splitlines():
            m = pat_tot.match(ln)
            if m:
                k = TOTALS[m.group(1)]
                tots.setdefault(k, {}).update(zip(cols, map(cell, m.group(2).split())))
                seen_t.add(k)
                continue
            m = pat_row.match(ln)
            if m and 1 <= int(m.group(1)) <= 36 and not re.search(r"\d", m.group(2)):
                sl, printed = int(m.group(1)), m.group(2).lower()
                want = PRINTED.get(sl, NAMES[sl].lower()[:4])
                if not printed.startswith(want):
                    raise SystemExit(f"FAIL - table {tid}: serial {sl} prints "
                                     f"'{m.group(2)}', expected {NAMES[sl]}")
                rows.setdefault(sl, {}).update(zip(cols, map(cell, m.group(3).split())))
                seen.add(sl)
        if seen != set(NAMES) or seen_t != set(TOTALS.values()):
            raise SystemExit(f"FAIL - table {tid}, columns {cols[0]}-{cols[-1]}: read "
                             f"{len(seen)} of 36 rows and {sorted(seen_t)} of the totals")
    return rows, tots


def close(a, b, tol):
    return a is not None and b is not None and abs(a - b) <= tol


def check_table(tid, rows, tots, ncols, rates, stage):
    """Totals and the printed column arithmetic. Returns a list of problems."""
    bad, known = [], {}
    want = list(range(3, 3 + ncols))
    for sl, r in rows.items():
        if sorted(r) != want:
            bad.append(f"{NAMES[sl]}: columns {sorted(r)}")
    if bad:
        return bad
    for c in want:
        if c in rates:
            continue
        st = sum(rows[s][c] or 0 for s in range(1, 29))
        ut = sum(rows[s][c] or 0 for s in range(29, 37))
        if st != tots["states"][c] or ut != tots["uts"][c] or st + ut != tots["india"][c]:
            bad.append(f"col {c}: states {st} vs {tots['states'][c]}, UTs {ut} vs "
                       f"{tots['uts'][c]}, all India {tots['india'][c]}")

    def rate(num, den):
        return None if not den else round(100 * num / den, 1)

    for label, r in [(NAMES[s], rows[s]) for s in rows] + [(k, v) for k, v in tots.items()]:
        if stage == "police":
            ids = [(r[6], r[3] + r[4] + r[5], "col6"), (r[18], r[16] + r[17], "col18"),
                   (r[19], r[7] + r[8] + r[15] + r[18], "col19"),
                   (r[22], r[6] - r[9] - r[19] - r[20], "col22")]
            rt = [(r[23], rate(r[18], r[19])), (r[24], rate(r[22], r[6]))]
        else:
            ids = [(r[5], r[3] + r[4], "col5"), (r[15], r[13] + r[14], "col15"),
                   (r[18], r[15] + r[16] + r[17], "col18"), (r[19], r[11] + r[18], "col19"),
                   (r[20], r[5] - r[19], "col20")]
            rt = [(r[21], rate(r[15], r[18])), (r[22], rate(r[20], r[5]))]
        for printed, computed, col in ids:
            if printed == computed:
                continue
            if KNOWN_GAPS.get((tid, col), {}).get(label) == computed - printed:
                known[(tid, col)] = known.get((tid, col), 0) + 1
                continue
            bad.append(f"{label}: printed {printed} in {col}, its own columns give {computed}")
        for printed, computed in rt:
            if printed is None and computed is None:
                continue
            if not close(printed, computed, 0.11):
                bad.append(f"{label}: printed rate {printed}, its own columns give {computed}")
    for k, gaps in KNOWN_GAPS.items():
        if k[0] == tid and known.get(k, 0) != len(gaps):
            bad.append(f"{k}: {len(gaps)} pinned gaps, {known.get(k, 0)} found. The "
                       "source has changed; read it again before moving the pin.")
    return bad


def main():
    if len(sys.argv) != 4:
        print(__doc__.split("\n\n")[1])
        return 2
    paths = dict(zip(("vol1", "vol2", "vol3"), sys.argv[1:4]))
    texts = {}
    for k, p in paths.items():
        got = sha(p)
        if got != DOCS[k][1]:
            print(f"FAIL - {p} is not the edition this script reads: SHA-256 {got}, "
                  f"expected {DOCS[k][1]} ({DOCS[k][2]}).")
            return 1
        texts[k] = text(p)

    prev = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    if "population" not in prev.get("series", {}):
        print("FAIL - the population series is carried over from the previous "
              "snapshot and there is none to carry.")
        return 1

    out = {
        "_source": ("National Crime Records Bureau, Crime in India 2024 (Volumes I to III), "
                    "and the Office of the Registrar General of India, Census 2011 via "
                    "data.gov.in"),
        "_licence": "Government Open Data Licence - India",
        "_note": (f"Case disposal by police and by courts, {YEAR}, read from the NCRB PDFs. "
                  "Refresh with scripts/fetch-crime-data.py."),
        "_fetched": time.strftime("%Y-%m-%d"),
        "_year": YEAR,
        "_documents": {k: {"title": t, "url": u, "sha256": h} for k, (u, h, t) in DOCS.items()},
        "tracks": {},
        "series": {"population": prev["series"]["population"]},
    }
    problems = 0
    for name, t in TRACKS.items():
        entry = {"label": t["label"]}
        for stage, ncols, rates in (("police", POLICE_COLS, POLICE_RATES),
                                    ("court", COURT_COLS, COURT_RATES)):
            doc, tid, title = t[stage]
            rows, tots = read_table(texts[doc], tid)
            bad = check_table(tid, rows, tots, ncols, rates, stage)
            print(f"  {name}/{stage}: Table {tid}, {len(rows)} rows, "
                  + ("checks pass" if not bad else f"{len(bad)} problems"))
            for b in bad:
                print(f"    {b}")
            problems += len(bad)
            entry[stage] = {
                "document": doc, "table": tid, "title": title,
                "rows": [{"sl": s, "name": NAMES[s],
                          "cols": {str(c): v for c, v in sorted(rows[s].items())}}
                         for s in sorted(rows)],
                "totals": {k: {str(c): v for c, v in sorted(v.items())}
                           for k, v in tots.items()},
            }
        out["tracks"][name] = entry
    if problems:
        print(f"\nFAIL - {problems} problems; nothing written.")
        return 1
    OUT.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    print(f"\nwrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
