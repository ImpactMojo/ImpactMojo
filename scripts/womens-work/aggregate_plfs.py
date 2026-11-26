#!/usr/bin/env python3
"""Aggregate the PLFS unit-level data into data/deep-dives/womens-work.json.

Source: National Statistical Office, Periodic Labour Force Survey, annual
rounds July 2017-June 2018 (MoSPI Microdata Catalogue 204) and July 2023-June
2024 (Catalogue 213), first-visit person files as released in CSV
(hh_per_fv_2017-18.csv and perv1.csv). The microdata are not redistributed;
pass their paths on the command line.

Method, as in MoSPI's annual reports:
  weight      = MULT/100 where NSS = NSC, else MULT/200, divided by the number
                of quarters (No_qtr), which gives annual estimates from the
                first-visit schedule;
  usual status (principal + subsidiary): a person is in the labour force
                if the principal status code is 11-81, or the principal status
                is outside the labour force and the subsidiary status is 11-51;
                a person works if either code is 11-51.
  work type   = the principal status code if it is a work code, else the
                subsidiary status code (11 own-account, 12 employer, 21 unpaid
                helper in a household enterprise, 31 regular wage/salary,
                41 casual labour in public works, 51 other casual labour);
  agriculture = NIC-2008 section A (divisions 01-03) for the activity that
                makes the person a worker (principal, else subsidiary).

The script stops unless the all-India labour force participation rates it
computes equal MoSPI's published figures.

    python3 scripts/working-hours/... (see README in this folder)
    python3 scripts/womens-work/aggregate_plfs.py PLFS1718_PERSON.csv PLFS2324_PERSON.csv
"""
import json, sys
from pathlib import Path
import numpy as np, pandas as pd

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "deep-dives" / "womens-work.json"

# Published usual-status LFPR, ages 15+, PLFS annual reports 2017-18 and 2023-24.
PUBLISHED = {
    "2017-18": {("all", 2): 23.3, ("rural", 2): 24.6, ("urban", 2): 20.4, ("all", 1): 75.8},
    "2023-24": {("all", 2): 41.7, ("rural", 2): 47.6, ("urban", 2): 28.0, ("all", 1): 78.8},
}
STATES = {"01": "Jammu & Kashmir", "02": "Himachal Pradesh", "03": "Punjab", "05": "Uttarakhand",
          "06": "Haryana", "07": "Delhi", "08": "Rajasthan", "09": "Uttar Pradesh", "10": "Bihar",
          "18": "Assam", "19": "West Bengal", "20": "Jharkhand", "21": "Odisha", "22": "Chhattisgarh",
          "23": "Madhya Pradesh", "24": "Gujarat", "27": "Maharashtra", "28": "Andhra Pradesh",
          "29": "Karnataka", "32": "Kerala", "33": "Tamil Nadu", "36": "Telangana"}
TYPES = [(21, "helper"), (11, "own"), (12, "employer"), (31, "regular"), (41, "casual"), (51, "casual")]


def load(path, sfx):
    h = pd.read_csv(path, nrows=0).columns
    want = {f"b1q3_{sfx}": "sector", f"b4q5_{sfx}": "sex", f"b4q6_{sfx}": "age", f"b5pt1q3_{sfx}": "ps",
            f"b5pt2q3_{sfx}": "ss", f"state_{sfx}": "st", f"b5pt1q5_{sfx}": "nic1", f"b5pt2q5_{sfx}": "nic2"}
    for c in h:
        for k, v in (("nss", "nss"), ("nsc", "nsc"), ("mult", "mult"), ("no_qtr", "nq")):
            if c.lower() == f"{k}_{sfx.lower()}":
                want[c] = v
    d = pd.read_csv(path, usecols=list(want), dtype=str).rename(columns=want)
    for c in ("sector", "sex", "age", "ps", "ss", "nss", "nsc", "mult", "nq"):
        d[c] = pd.to_numeric(d[c], errors="coerce")
    d["w"] = np.where(d.nss == d.nsc, d.mult / 100, d.mult / 200) / d.nq
    pw = d.ps.between(11, 51)
    sw = d.ss.between(11, 51)
    d["lf"] = d.ps.between(11, 81) | sw
    d["work"] = pw | sw
    d["subonly"] = ~pw & sw
    d["code"] = np.where(pw, d.ps, np.where(sw, d.ss, np.nan))
    nic = np.where(pw, d.nic1.fillna(""), np.where(sw, d.nic2.fillna(""), ""))
    d["agri"] = d.work & pd.Series(nic, index=d.index).str[:2].isin(["01", "02", "03"])
    return d[d.age >= 15]


def share(b, mask):
    return round(100 * b.w[mask].sum() / b.w.sum(), 1)


def summarise(d, year):
    out = {"year": year, "n_15plus": int(len(d)), "groups": {}}
    for sec, sn in ((None, "all"), (1, "rural"), (2, "urban")):
        for sx, sxn in ((2, "women"), (1, "men")):
            b = d[(d.sex == sx) & ((d.sector == sec) if sec else True)]
            g = {"lfpr": share(b, b.lf), "wpr": share(b, b.work), "subsidiary_only": share(b, b.subonly),
                 "agri": share(b, b.agri), "nonagri": share(b, b.work & ~b.agri), "n": int(len(b)),
                 "workers_crore": round(b.w[b.work].sum() / 1e7, 2)}
            for code, k in TYPES:
                g[k] = round(g.get(k, 0) + share(b, b.code == code), 1)
            out["groups"][f"{sn}_{sxn}"] = g
            pub = PUBLISHED[year].get((sn, sx))
            if pub is not None and g["lfpr"] != pub:
                sys.exit(f"FAIL - {year} {sn} {sxn} LFPR {g['lfpr']} against published {pub}")
    st = {}
    for code, name in STATES.items():
        b = d[(d.sex == 2) & (d.st == code)]
        st[name] = {"wpr": share(b, b.work), "helper_own": round(share(b, b.code == 21) + share(b, b.code == 11), 1),
                    "subsidiary_only": share(b, b.subonly), "n": int(len(b))}
    out["states_women"] = st
    return out


def main():
    a = summarise(load(sys.argv[1], "per_fv"), "2017-18")
    b = summarise(load(sys.argv[2], "perv1"), "2023-24")
    res = {"source": "NSO Periodic Labour Force Survey, unit-level first-visit person files, July 2017-June 2018 and July 2023-June 2024 (MoSPI Microdata Catalogues 204 and 213)",
           "method": "usual status (principal and subsidiary), persons aged 15 and over, MoSPI annual weights",
           "benchmark": "all-India LFPR for women (all, rural, urban) and men equals the published figures in both years",
           "rounds": [a, b]}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    print("PASS - benchmark matched; wrote", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
