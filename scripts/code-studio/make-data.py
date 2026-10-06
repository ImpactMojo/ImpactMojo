#!/usr/bin/env python3
"""Write the illustrative teaching datasets in code/data/.

Every number here is invented by a seeded random generator. The files exist so
that a learner has enough rows to group, join and plot; they describe no real
households and must never be quoted as data. District and state names are real
so the joins look like real work; the values attached to them are not.

    python3 scripts/code-studio/make-data.py          # rewrite the files
    python3 scripts/code-studio/make-data.py --check  # exit 1 if they would change
"""
import csv, io, random, sys
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "code" / "data"

DISTRICTS = [  # district, state, region (real names, invented values below)
    ("Rewa", "Madhya Pradesh", "Central"), ("Betul", "Madhya Pradesh", "Central"),
    ("Indore", "Madhya Pradesh", "Central"), ("Gaya", "Bihar", "East"),
    ("Purnia", "Bihar", "East"), ("Patna", "Bihar", "East"),
    ("Udaipur", "Rajasthan", "West"), ("Barmer", "Rajasthan", "West"),
    ("Kozhikode", "Kerala", "South"), ("Wayanad", "Kerala", "South"),
]

def households(rng):
    rows = []
    hid = 1
    for district, state, region in DISTRICTS:
        urban_share = 0.6 if district in ("Indore", "Patna", "Kozhikode") else 0.2
        base = {"Kerala": 3200, "Madhya Pradesh": 2100, "Rajasthan": 2200, "Bihar": 1700}[state]
        for _ in range(24):
            area = "Urban" if rng.random() < urban_share else "Rural"
            caste = rng.choices(["SC", "ST", "OBC", "General"], [0.18, 0.12 if district in ("Betul", "Wayanad", "Udaipur") else 0.06, 0.44, 0.32])[0]
            head_gender = "Female" if rng.random() < 0.14 else "Male"
            edu = max(0, min(17, int(rng.gauss(8 if area == "Urban" else 5, 4))))
            size = max(1, min(11, int(rng.gauss(4.6, 1.6))))
            mult = (1.6 if area == "Urban" else 1.0) * (0.75 if caste in ("SC", "ST") else 1.0) * (1 + 0.05 * edu)
            exp = int(round(base * mult * rng.lognormvariate(0, 0.35), -1))
            land = 0.0 if area == "Urban" else round(max(0.0, rng.gauss(1.2, 1.3)), 2)
            toilet = "Yes" if rng.random() < (0.9 if area == "Urban" else 0.62) else "No"
            bank = "Yes" if rng.random() < 0.82 else "No"
            shg = "Yes" if (head_gender == "Female" or rng.random() < 0.3) and rng.random() < 0.55 else "No"
            transfer = "Yes" if (exp < base * 1.1 and rng.random() < 0.7) or rng.random() < 0.15 else "No"
            rows.append([hid, district, area, caste, head_gender, edu, size, exp, land, toilet, bank, shg, transfer])
            hid += 1
    return ["hh_id", "district", "area", "caste", "head_gender", "head_edu_years", "hh_size",
            "monthly_pc_exp", "land_acres", "has_toilet", "has_bank_account", "shg_member", "received_transfer"], rows

def districts():
    # Programme attributes, not statistics: an invented rollout, so no column
    # here can be read as a claim about the real district.
    rng = random.Random(7)
    rows = [[d, s, r, 1 + i % 3, rng.choice(["Team A", "Team B", "Team C"])]
            for i, (d, s, r) in enumerate(DISTRICTS)]
    return ["district", "state", "region", "programme_phase", "field_team"], rows

def render(head, rows):
    b = io.StringIO()
    w = csv.writer(b, lineterminator="\n")
    w.writerow(head); w.writerows(rows)
    return b.getvalue()

def main():
    files = {"households.csv": render(*households(random.Random(2026))), "districts.csv": render(*districts())}
    stale = [n for n, t in files.items() if not (OUT / n).exists() or (OUT / n).read_text() != t]
    if "--check" in sys.argv:
        if stale:
            print("FAIL - code/data out of date: %s" % ", ".join(stale)); sys.exit(1)
        print("PASS - code/data matches its generator."); return
    for n, t in files.items():
        (OUT / n).write_text(t)
    print("wrote", ", ".join(files))

if __name__ == "__main__":
    main()
