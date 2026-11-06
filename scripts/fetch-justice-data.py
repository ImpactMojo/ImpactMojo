#!/usr/bin/env python3
"""Read the prison and court-pendency tables into data/justice-india.json.

    python3 scripts/fetch-justice-data.py PSI-2024.pdf

Sources:
  National Crime Records Bureau, Prison Statistics India 2024 (published on
  ncrb.gov.in; the PDF is not committed and its SHA-256 must match), Tables
  1.2, 2.1, 2.11A, 2.11C, 2.11D, 6.4 and 7.4. Figures are as on 31 December
  2024, except West Bengal, which sent no 2024 data: NCRB reprints its 2023
  figures in every table, and the page says so.

  Lok Sabha Unstarred Question 3501, answered on 13 March 2026 by the Ministry
  of Law and Justice, Annexure I (pending cases in each High Court) and
  Annexure II (pending cases in district and subordinate courts, by state),
  both from the National Judicial Data Grid as on 9 March 2026. The answer is
  a scanned image, so its rows are transcribed below, and each row and each
  column total is checked against the figures printed beside it.

  Carried over unchanged from the previous snapshot, from data.gov.in: the
  Census 2011 population, SC and ST tables, and the age-wise pendency table.

Every NCRB table carries three total rows, 'TOTAL (STATES)', 'TOTAL (UTs)' and
'TOTAL (ALL-INDIA)'. For every count column the 28 states must add to the
first, the 8 UTs to the second, and the two to the third, or nothing is
written. The rows are written in the shape the build script reads, with the
three totals renamed 'Total (States)', 'Total (UTs)' and 'Total (All India)'.
"""
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "justice-india.json"

PSI = ("https://www.ncrb.gov.in/uploads/files/PSI-2024ason26022026.pdf",
       "4f82f813fe1fb36d7a8ec07a0d81891662aabb1933b0c8129719a5d29346cdb4",
       "Prison Statistics India 2024")
LS3501 = ("https://www.doj.gov.in/static/uploads/2026/04/c393f1e761f310476a68fe8f1f87c16a.pdf",
          "ffcf80693327ba90319028825f11ca5561dc1eb334533c5d2924f49663565a9e",
          "Department of Justice, Lok Sabha replies, second part of the Budget Session 2026, "
          "Unstarred Question 3501 of 13 March 2026, Annexures I and II")

NAMES = {1: "Andhra Pradesh", 2: "Arunachal Pradesh", 3: "Assam", 4: "Bihar",
         5: "Chhattisgarh", 6: "Goa", 7: "Gujarat", 8: "Haryana", 9: "Himachal Pradesh",
         10: "Jharkhand", 11: "Karnataka", 12: "Kerala", 13: "Madhya Pradesh",
         14: "Maharashtra", 15: "Manipur", 16: "Meghalaya", 17: "Mizoram", 18: "Nagaland",
         19: "Odisha", 20: "Punjab", 21: "Rajasthan", 22: "Sikkim", 23: "Tamil Nadu",
         24: "Telangana", 25: "Tripura", 26: "Uttar Pradesh", 27: "Uttarakhand",
         28: "West Bengal", 29: "Andaman and Nicobar Islands", 30: "Chandigarh",
         31: "Dadra and Nagar Haveli and Daman and Diu", 32: "Delhi",
         33: "Jammu and Kashmir", 34: "Ladakh", 35: "Lakshadweep", 36: "Puducherry"}
PRINTED = {29: "a & n", 31: "dnh", 33: "jammu"}
TOTALS = {"TOTAL (STATES)": "Total (States)", "TOTAL (UTs)": "Total (UTs)",
          "TOTAL (ALL-INDIA)": "Total (All India)"}

G = ("male", "female", "transgender", "total")


def mft(prefix):
    return [f"{prefix}___{g}" for g in G]


# PSI table -> (series name, title, {page index: [field for each column from (3)]}).
# Rate columns are listed in RATES and left out of the totals check.
TABLES = {
    "1.2": ("occupancy", "Capacity, Inmate Population and Occupancy Rate of Jails as on 31-12-2024",
            {0: mft("available_capacity") + mft("inmate_population")
                + [f"occupancy_rate_in_percentage____{g}" for g in G]}),
    "2.1": ("types", "Types of Prison Inmates as on 31-12-2024",
            {0: [f"convicts___{g}__col_{c}_" for g, c in zip(G, range(3, 7))]
                + [f"undertrials___{g}__col_{c}_" for g, c in zip(G, range(7, 11))],
             1: [f"detenues___{g}__col_{c}_" for g, c in zip(G, range(11, 15))]
                + [f"others___{g}__col_{c}_" for g, c in zip(G, range(15, 19))]
                + ["total__col_6_10__14_18___col_19_"]}),
    "6.4": ("duration", "Number of Undertrial Prisoners by Duration of Confinement as on 31-12-2024",
            {0: mft("upto_3_months") + mft("_3_to_6_months") + mft("_6_to_12_months")
                + mft("_1_to_2_years"),
             1: mft("_2_to_3_years") + mft("_3_to_5_years") + mft("above_5_years")
                + ["total___male", "total___female", "total___transgender", "_total"]}),
    "7.4": ("s436a", "Status of Undertrial Inmates under Section 479 BNSS/436A of Cr.P.C. during 2024",
            {0: mft("number_of_inmates_eligible_for_pre__mature_release_under_section_436a")
                + mft("number_of_inmates_released_under_section_436a_of_cr_p_c_"),
             3: mft("eligible_under_479_bnss_or_436a") + mft("applications_under_479_bnss_or_436a")
                + mft("released_under_479_bnss_or_436a")}),
    "2.11D": ("caste", "Caste of Undertrial Prisoners as on 31-12-2024",
              {0: ["scheduled_castes__sc_", "scheduled_tribes__st_",
                   "other_backward_classes__obc_", "others", "_total"]}),
    "2.11C": ("religion", "Religion of Undertrial Prisoners as on 31-12-2024",
              {0: ["hindu", "muslim", "sikh", "christian", "others", "_total"]}),
    "2.11A": ("education", "Education Profile of Undertrial Prisoners as on 31-12-2024",
              {0: ["educational_standard___illiterate", "educational_standard___below_class_x",
                   "educational_standard___class_x_and_above_but_below_graduation",
                   "educational_standard___graduate",
                   "educational_standard___holding_tech__degree_diploma",
                   "educational_standard___post_graduate", "educational_standard___total"]}),
}
RATES = {f"occupancy_rate_in_percentage____{g}" for g in G}

# Lok Sabha USQ 3501 (13-03-2026), Annexure II: (civil, criminal, total),
# transcribed from the scan. Printed column totals: 11,167,873 / 38,387,519 /
# 49,562,229. Meghalaya's row prints civil and criminal as 4,917 each, which do
# not add to its total of 16,671; each national column adds up only with the
# figures as printed, so the error is inside that row, and the total is used.
DISTRICT = {
    "Andaman and Nicobar Islands": (4031, 4501, 8532),
    "Andhra Pradesh": (436522, 511287, 947809),
    "Arunachal Pradesh": (3621, 12145, 15766),
    "Assam": (113792, 463784, 577576),
    "Bihar": (538592, 3177552, 3716144),
    "Chandigarh": (22839, 78400, 101239),
    "Chhattisgarh": (87413, 403750, 491163),
    "Delhi": (217341, 1383042, 1600383),
    "Goa": (28169, 33820, 61989),
    "Gujarat": (325786, 1641937, 1967723),
    "Haryana": (427948, 1112559, 1540507),
    "Himachal Pradesh": (178567, 443609, 622176),
    "Jammu and Kashmir": (119520, 232165, 351685),
    "Jharkhand": (96274, 474955, 571229),
    "Karnataka": (1056085, 1334144, 2390229),
    "Kerala": (541843, 1259672, 1801515),
    "Ladakh": (789, 842, 1631),
    "Lakshadweep": (151, 406, 557),
    "Madhya Pradesh": (426046, 1691148, 2117194),
    "Maharashtra": (1766653, 4310083, 6076736),
    "Manipur": (9157, 4938, 14095),
    "Meghalaya": (4917, 4917, 16671),
    "Mizoram": (4028, 3319, 7347),
    "Nagaland": (1043, 2876, 3919),
    "Odisha": (269938, 1547258, 1817196),
    "Puducherry": (11757, 24657, 36414),
    "Punjab": (363976, 608245, 972221),
    "Rajasthan": (514668, 2162933, 2677601),
    "Sikkim": (933, 1339, 2272),
    "Tamil Nadu": (704363, 1064754, 1769117),
    "Telangana": (339582, 651905, 991487),
    "Dadra and Nagar Haveli and Daman and Diu": (3681, 4702, 8383),
    "Tripura": (13524, 52082, 65606),
    "Uttar Pradesh": (1843158, 10161311, 12004469),
    "Uttarakhand": (48932, 262101, 311033),
    "West Bengal": (642234, 3260381, 3902615),
}
DISTRICT_TOTAL = (11167873, 38387519, 49562229)
DISTRICT_ROW_EXCEPTIONS = {"Meghalaya"}

# Annexure I. Manipur's civil figure is printed '51,40'; the row's total and
# criminal figures (6,031 and 891) make it 5,140, and only the total is used.
HIGH = {
    "Allahabad High Court": (617265, 576081, 1193346),
    "Bombay High Court": (546634, 115416, 662050),
    "Calcutta High Court": (172454, 32179, 204633),
    "Gauhati High Court": (47555, 16954, 64509),
    "High Court for State of Telangana": (204131, 32376, 236507),
    "High Court of Andhra Pradesh": (206581, 42278, 248859),
    "High Court of Chhattisgarh": (52888, 22463, 75351),
    "High Court of Delhi": (93069, 32893, 125962),
    "High Court of Gujarat": (116691, 57849, 174540),
    "High Court of Himachal Pradesh": (90576, 13542, 104118),
    "High Court of Jammu and Kashmir": (33869, 9321, 43190),
    "High Court of Jharkhand": (32269, 40890, 73159),
    "High Court of Karnataka": (274093, 57016, 331109),
    "High Court of Kerala": (200587, 47131, 247718),
    "High Court of Madhya Pradesh": (283994, 194767, 478761),
    "High Court of Manipur": (5140, 891, 6031),
    "High Court of Meghalaya": (1351, 432, 1783),
    "High Court of Punjab and Haryana": (255401, 165653, 421054),
    "High Court of Rajasthan": (479427, 192415, 671842),
    "High Court of Sikkim": (208, 88, 296),
    "High Court of Tripura": (1106, 283, 1389),
    "High Court of Uttarakhand": (33735, 27092, 60827),
    "Madras High Court": (477589, 75555, 553144),
    "Orissa High Court": (122040, 41487, 163527),
    "Patna High Court": (114535, 103100, 217635),
}
HIGH_TOTAL = (4463188, 1898152, 6361340)

CARRIED = ("population", "sc_st", "st_mota", "pendency_age")
NUM = r"(?:-?\d+(?:\.\d+)?|-)"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def cell(s):
    if s == "-":
        return None
    return float(s) if "." in s else int(s)


def read_psi(txt, tid, layout):
    """{serial: {field: value}}, {total name: {field: value}} for one PSI table."""
    pages = [p for p in txt.split("\f")
             if re.search(r"Table " + re.escape(tid) + r" – Page \d+ of \d+", p)]
    rows, tots = {}, {}
    for idx, fields in layout.items():
        if idx >= len(pages):
            raise SystemExit(f"FAIL - table {tid}: page {idx + 1} not found")
        n = len(fields)
        tail = r"((?:" + NUM + r"\s+){%d}" % (n - 1) + NUM + r")\s*$"
        pat_row = re.compile(r"^\s*(\d{1,2})\s+([A-Z][A-Z &.]*?)\s*[#$]?\s+" + tail)
        pat_tot = re.compile(r"^\s*(TOTAL \(STATES\)|TOTAL \(UTs\)|TOTAL \(ALL-INDIA\))\s+" + tail)
        pat_name = re.compile(r"^\s*(\d{1,2})\s+([A-Z][A-Z &.]*?)\s*[#$]?\s*$")
        pat_bare = re.compile(r"^\s*" + tail)
        seen, seen_t, wrapped = set(), set(), None
        for ln in pages[idx].splitlines():
            # A long name wraps its figures onto the next line.
            m = pat_name.match(ln)
            if m and 1 <= int(m.group(1)) <= 36:
                wrapped = m
                continue
            m = pat_bare.match(ln)
            if m and wrapped:
                ln = f"{wrapped.group(1)} {wrapped.group(2)} {m.group(1)}"
            wrapped = None
            m = pat_tot.match(ln)
            if m:
                vals = dict(zip(fields, map(cell, m.group(2).split())))
                k = TOTALS[m.group(1)]
                prev = tots.setdefault(k, {})
                if any(f in prev and prev[f] != v for f, v in vals.items()):
                    raise SystemExit(f"FAIL - table {tid}: {k} printed twice, differently")
                prev.update(vals)
                seen_t.add(k)
                continue
            m = pat_row.match(ln)
            if m and 1 <= int(m.group(1)) <= 36:
                sl = int(m.group(1))
                want = PRINTED.get(sl, NAMES[sl].lower()[:4])
                if not m.group(2).lower().startswith(want):
                    raise SystemExit(f"FAIL - table {tid}: serial {sl} prints "
                                     f"'{m.group(2)}', expected {NAMES[sl]}")
                vals = dict(zip(fields, map(cell, m.group(3).split())))
                if sl in seen and rows[sl] != {**rows[sl], **vals}:
                    raise SystemExit(f"FAIL - table {tid}: serial {sl} printed twice, differently")
                rows.setdefault(sl, {}).update(vals)
                seen.add(sl)
        if seen != set(NAMES) or seen_t != set(TOTALS.values()):
            raise SystemExit(f"FAIL - table {tid}, page {idx + 1}: read {len(seen)} of 36 rows "
                             f"and {sorted(seen_t)} of the totals")
    return rows, tots


def check_psi(tid, rows, tots, fields):
    bad = []
    for f in fields:
        if f in RATES:
            continue
        st = [rows[s][f] for s in range(1, 29)]
        ut = [rows[s][f] for s in range(29, 37)]
        # A '-' is a state that gave no breakdown; NCRB's totals add up the
        # states that did, so it counts as nothing here and stays null in
        # the output.
        a, b = sum(v or 0 for v in st), sum(v or 0 for v in ut)
        if (a, b, a + b) != (tots["Total (States)"][f], tots["Total (UTs)"][f],
                             tots["Total (All India)"][f]):
            bad.append(f"{tid} {f}: states {a} vs {tots['Total (States)'][f]}, UTs {b} vs "
                       f"{tots['Total (UTs)'][f]}, all India {tots['Total (All India)'][f]}")
    return bad


def check_courts():
    bad = []
    for label, table, total, exceptions in (("Annexure II", DISTRICT, DISTRICT_TOTAL,
                                             DISTRICT_ROW_EXCEPTIONS),
                                            ("Annexure I", HIGH, HIGH_TOTAL, set())):
        for name, (c, r, t) in table.items():
            if c + r != t and name not in exceptions:
                bad.append(f"{label} {name}: {c} + {r} is not {t}")
            if c + r == t and name in exceptions:
                bad.append(f"{label} {name}: listed as an exception but adds up")
        sums = tuple(sum(v[i] for v in table.values()) for i in range(3))
        if sums != total:
            bad.append(f"{label}: columns sum to {sums}, printed totals {total}")
    if len(DISTRICT) != 36 or set(DISTRICT) != set(NAMES.values()):
        bad.append("Annexure II does not name the 36 states and union territories")
    return bad


def main():
    if len(sys.argv) != 2:
        print(__doc__.split("\n\n")[1])
        return 2
    got = sha(sys.argv[1])
    if got != PSI[1]:
        print(f"FAIL - {sys.argv[1]}: SHA-256 {got}, expected {PSI[1]} ({PSI[2]}).")
        return 1
    txt = subprocess.run(["pdftotext", "-layout", sys.argv[1], "-"], check=True,
                         capture_output=True, text=True).stdout
    prev = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {"series": {}}
    missing = [k for k in CARRIED if k not in prev["series"]]
    if missing:
        print(f"FAIL - nothing to carry over for {missing}")
        return 1

    out = {
        "_source": ("National Crime Records Bureau (Prison Statistics India 2024); Ministry of "
                    "Law and Justice, reply to Lok Sabha Unstarred Question 3501 of 13 March "
                    "2026 (National Judicial Data Grid as on 9 March 2026); and Census 2011 "
                    "and Department of Justice tables via data.gov.in"),
        "_licence": "Government Open Data Licence - India",
        "_note": ("Prison figures are a single-day census as on 31-12-2024. Court pendency is "
                  "as on 9 March 2026. Refresh with scripts/fetch-justice-data.py."),
        "_fetched": time.strftime("%Y-%m-%d"),
        "_year": 2024,
        "_documents": {
            "psi": {"title": PSI[2], "url": PSI[0], "sha256": PSI[1]},
            "ls3501": {"title": LS3501[2], "url": LS3501[0], "sha256": LS3501[1]},
        },
        "series": {},
    }
    bad = check_courts()
    for tid, (name, title, layout) in TABLES.items():
        rows, tots = read_psi(txt, tid, layout)
        fields = [f for fs in layout.values() for f in fs]
        problems = check_psi(tid, rows, tots, fields)
        print(f"  Table {tid} ({name}): 36 rows, "
              + ("totals agree" if not problems else f"{len(problems)} problems"))
        bad += problems
        out["series"][name] = {
            "source": f"{PSI[2]}, Table {tid}", "title": title,
            "rows": [dict(state_ut=NAMES[s], **rows[s]) for s in sorted(rows)]
                    + [dict(state_ut=k, **v) for k, v in tots.items()]}
    # The build reads the types table's state column under the old name.
    for r in out["series"]["types"]["rows"]:
        r["state_ut__col_2_"] = r.pop("state_ut")

    out["series"]["district_courts"] = {
        "source": f"{LS3501[2]} (Annexure II)",
        "title": "State/UT-wise Pendency of Cases in District and Subordinate Courts as on 09-03-2026",
        "rows": [{"state_ut": k, "civil": c, "criminal": r, "_total": t}
                 for k, (c, r, t) in DISTRICT.items()]
                + [{"state_ut": "Total", "civil": DISTRICT_TOTAL[0],
                    "criminal": DISTRICT_TOTAL[1], "_total": DISTRICT_TOTAL[2]}]}
    out["series"]["high_courts"] = {
        "source": f"{LS3501[2]} (Annexure I)",
        "title": "High Court-wise Pendency of Cases as on 09-03-2026",
        "rows": [{"high_court": k, "civil": c, "criminal": r, "_total": t}
                 for k, (c, r, t) in HIGH.items()]
                + [{"high_court": "Total", "civil": HIGH_TOTAL[0],
                    "criminal": HIGH_TOTAL[1], "_total": HIGH_TOTAL[2]}]}
    for k in CARRIED:
        out["series"][k] = prev["series"][k]

    if bad:
        for b in bad:
            print(f"    {b}")
        print(f"\nFAIL - {len(bad)} problems; nothing written.")
        return 1
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nwrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
