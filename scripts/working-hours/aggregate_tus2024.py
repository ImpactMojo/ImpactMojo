#!/usr/bin/env python3
"""Aggregate the NSO Time Use Survey 2024 unit-level data for the Deep Dive
"Nobody tells you it is five o'clock" (DeepDives/indian-working-hours.html).

The unit-level files are not in this repository: MoSPI releases them to
registered users at https://microdata.gov.in/NADA/index.php/catalog/236 and
they are not ours to redistribute. This script turns them into the small table
of aggregates in data/deep-dives/working-hours.json, which the page is drawn
from.

How the input was prepared (6 November 2026):
  1. Download TUS2024.zip from catalogue 236; it holds TUS2024.Nesstar.
  2. Read it in R with the CRAN package nesstarR 0.1.0 and export every
     column of dataset 2 (person diary records, 10,211,478 rows) except
     Stratum and Sub_Stratum, which that version cannot decode. They are used
     only for standard errors, not for estimates.
  3. Save the result as a parquet file and pass its path below.

Checks. Run with --bench first: it must reproduce MoSPI's published minutes
per participant per day (eSankhyiki TUS indicator 7, 2024, all India) for
employment, unpaid domestic and unpaid care work, men and women, ages 6+ and
15-59. On 6 November 2026 all twelve matched exactly.

Method, as MoSPI's: a 30-minute slot with several activities is divided
equally among them; weight is MULT/100; every diary covers 24 hours from
04:00. A worker is a person aged 15+ whose usual principal activity status is
11, 12, 21 (self-employed), 31 (regular salaried) or 41, 51 (casual labour).
Paid work is activity division 11 to 15 (ICATUS 2016); commuting is division
18; unpaid work is major divisions 3 and 4. Government employment is the
enterprise type recorded for the day's paid work (3 or 4), so it can only be
known on a day with paid work: the government/private split is used only in
measures conditional on working that day.

    python3 scripts/working-hours/aggregate_tus2024.py PERSONS.parquet --bench
    python3 scripts/working-hours/aggregate_tus2024.py PERSONS.parquet
"""
import json, sys
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "deep-dives" / "working-hours.json"
BENCH = {  # eSankhyiki TUS indicator 7, 2024, all India, minutes per participant per day
    ("1", 6, 200): (473, 88, 75), ("1", 15, 59): (480, 86, 74),
    ("2", 6, 200): (341, 289, 137), ("2", 15, 59): (344, 305, 140)}
COLS = ["FSU_Serial_No", "Sample_HH_No", "Person_Serial_No", "Gender", "Age",
        "Principal_Activity_Status", "Day_of_Week", "Type_of_Day", "Time_From",
        "Time_To", "Activity_Code_3Digit", "Enterprise_Type", "MULT"]


def load(path):
    d = pd.read_parquet(path, columns=COLS)
    d = d[d.Time_From.astype(str) != ""].copy()          # under-6 roster rows carry no diary
    for c in COLS:
        if c not in ("Age", "MULT"):
            d[c] = d[c].astype(str)
    hm = lambda s: s.str[:2].astype(int) * 60 + s.str[3:5].astype(int)
    f, t = hm(d.Time_From), hm(d.Time_To)
    t = np.where(t <= f, t + 1440, t)
    d["dur"] = t - f
    d["from_m"] = np.where(f < 240, f + 1440, f)          # the diary day runs 04:00 to 04:00
    d["pid"] = d.FSU_Serial_No + "-" + d.Sample_HH_No + "-" + d.Person_Serial_No
    d["share"] = d.dur / d.groupby(["pid", "Time_From"]).dur.transform("size")
    d["w"] = d.MULT.astype(float) / 100
    d["age"] = pd.to_numeric(d.Age, errors="coerce")
    d["code"] = d.Activity_Code_3Digit
    day = d.drop_duplicates(["pid", "Time_From"]).groupby("pid").dur.sum()
    if not (day == 1440).all():
        sys.exit("FAIL - a diary does not cover 24 hours")
    return d


def bench(d):
    major = d.code.str[0]
    pm = d.assign(m=major).groupby(["pid", "m"]).share.sum().unstack(fill_value=0)
    p = d.groupby("pid").agg(w=("w", "first"), g=("Gender", "first"), age=("age", "first")).join(pm)
    ok = True
    for (g, lo, hi), want in BENCH.items():
        q = p[(p.g == g) & (p.age >= lo) & (p.age <= hi)]
        got = tuple(round((q[q[m] > 0][m] * q[q[m] > 0].w).sum() / q[q[m] > 0].w.sum()) for m in "134")
        ok &= got == want
        print(("ok  " if got == want else "FAIL"), "sex", g, f"{lo}-{hi}", got, "published", want)
    sys.exit(0 if ok else "FAIL - the microdata do not reproduce MoSPI's published minutes")


def wmean(x, col):
    return float((x[col] * x.w).sum() / x.w.sum())


def build(d):
    paid = d.code.str[0].eq("1") & ~d.code.str[:2].isin(["16", "17", "18"])
    P = d.groupby("pid").agg(w=("w", "first"), sex=("Gender", "first"), age=("age", "first"),
                             upas=("Principal_Activity_Status", "first"), dow=("Day_of_Week", "first"),
                             dtype=("Type_of_Day", "first"))
    P["paid"] = d[paid].groupby("pid").share.sum()
    P["unpaid"] = d[d.code.str[0].isin(["3", "4"])].groupby("pid").share.sum()
    P["commute"] = d[d.code.str[:2].eq("18")].groupby("pid").share.sum()
    P[["paid", "unpaid", "commute"]] = P[["paid", "unpaid", "commute"]].fillna(0)
    ent = (d[paid & d.Enterprise_Type.ne("")].groupby(["pid", "Enterprise_Type"]).share.sum()
           .reset_index().sort_values("share").drop_duplicates("pid", keep="last").set_index("pid").Enterprise_Type)
    P["ent"] = ent
    pa = d[paid]
    P["last_end"] = (pa.from_m + pa.dur).groupby(pa.pid).max()
    T3 = {"11": "Self-employed", "12": "Self-employed", "21": "Self-employed", "31": "Salaried",
          "41": "Casual labour", "51": "Casual labour"}
    W = P[(P.age >= 15) & P.upas.isin(T3) & P.sex.isin(["1", "2"])].copy()
    W["t3"] = W.upas.map(T3)
    W["sexn"] = W.sex.map({"1": "Men", "2": "Women"})
    W["t4"] = W.t3
    sal = W.t3 == "Salaried"
    W.loc[sal, "t4"] = np.where(W.loc[sal, "ent"].isin(["3", "4"]), "Salaried, government", "Salaried, private")
    out = {"source": "NSO Time Use Survey 2024 (January to December 2024), unit-level data, MoSPI microdata catalogue 236; aggregated by scripts/working-hours/aggregate_tus2024.py",
           "universe": "Workers aged 15 and over by usual principal activity status", "groups": []}
    for (t, s), g in W.groupby(["t3", "sexn"]):
        n = g[g.dtype == "1"]
        dow = []
        for k in range(1, 8):
            x = g[g.dow == str(k)]
            dow.append(round(float((x.paid.gt(0) * x.w).sum() / x.w.sum()), 4))
        out["groups"].append(dict(type=t, sex=s, n=int(len(g)), workers_share=round(float(g.w.sum() / W.w.sum()), 4),
            weekly_paid_h=round(wmean(g, "paid") / 60 * 7, 2),
            workday_paid_h=round(wmean(n, "paid") / 60, 2), workday_unpaid_h=round(wmean(n, "unpaid") / 60, 2),
            workday_commute_h=round(wmean(n, "commute") / 60, 2), any_paid_by_dow=dow))
    base = W[(W.dtype == "1") & (W.paid > 0)]
    slots = []
    for s in range(48):
        t0 = 240 + s * 30
        on = pa[(pa.from_m <= t0) & (pa.from_m + pa.dur > t0)].pid.unique()
        slots.append(set(on))
    out["clock"] = {"slot_start": "04:00", "slot_minutes": 30, "groups": []}
    for (t, s), g in base.groupby(["t4", "sexn"]):
        wt = g.w.sum()
        o = np.argsort(g.last_end.values)
        c = np.cumsum(g.w.values[o])
        q = lambda p: int(g.last_end.values[o][np.searchsorted(c, p * c[-1])])
        out["clock"]["groups"].append(dict(type=t, sex=s, n=int(len(g)),
            at_work=[round(float(g.w[g.index.isin(slots[k])].sum() / wt), 4) for k in range(48)],
            end_median_min=q(.5), end_p25_min=q(.25), end_p75_min=q(.75),
            past_17=round(float(g.w[g.last_end > 1020].sum() / wt), 4),
            past_19=round(float(g.w[g.last_end > 1140].sum() / wt), 4),
            past_21=round(float(g.w[g.last_end > 1260].sum() / wt), 4),
            paid_h=round(wmean(g, "paid") / 60, 2), unpaid_h=round(wmean(g, "unpaid") / 60, 2)))
    allw = W
    out["all_workers_weekly_paid_h"] = {"All": round(wmean(allw, "paid") / 60 * 7, 2),
        "Men": round(wmean(allw[allw.sexn == "Men"], "paid") / 60 * 7, 2),
        "Women": round(wmean(allw[allw.sexn == "Women"], "paid") / 60 * 7, 2)}
    return out


if __name__ == "__main__":
    d = load(sys.argv[1])
    if "--bench" in sys.argv:
        bench(d)
    res = build(d)
    old = json.loads(OUT.read_text()) if OUT.exists() else {}
    res["international"] = old.get("international")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    print("wrote", OUT.relative_to(ROOT))
