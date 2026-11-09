#!/usr/bin/env python3
"""Add ILO hours and productivity for comparison countries to
data/deep-dives/working-hours.json.

Two ILOSTAT series, read from the ILO SDMX service (sdmx.ilo.org):
  DF_HOW_TEMP_SEX_AGE_NB  average weekly hours actually worked per employed
                          person, both sexes, ages 15+, national labour force
                          surveys (India: PLFS)
  DF_GDP_2HRW_NOC_NB      output per hour worked, GDP in constant 2021
                          international dollars at PPP (ILO modelled estimates)
For each country the latest year with hours is kept, and productivity is
taken for that same year so the two describe one year.

    python3 scripts/working-hours/fetch_ilo.py
"""
import csv, io, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "deep-dives" / "working-hours.json"
C = {"IND": "India", "BGD": "Bangladesh", "LKA": "Sri Lanka", "VNM": "Viet Nam", "IDN": "Indonesia",
     "MEX": "Mexico", "BRA": "Brazil", "KOR": "Republic of Korea", "USA": "United States",
     "GBR": "United Kingdom", "FRA": "France", "DEU": "Germany", "NLD": "Netherlands",
     "PAK": "Pakistan", "THA": "Thailand", "ZAF": "South Africa", "TUR": "Türkiye", "PHL": "Philippines"}


def get(flow, key):
    url = f"https://sdmx.ilo.org/rest/data/ILO,{flow},1.0/{key}?startPeriod=2018"
    r = subprocess.run(["curl", "-sS", "-m", "120", "-H", "Accept: application/vnd.sdmx.data+csv;version=1.0.0", url],
                       capture_output=True, text=True, check=True)
    return list(csv.DictReader(io.StringIO(r.stdout)))


areas = "+".join(C)
hours = [r for r in get("DF_HOW_TEMP_SEX_AGE_NB", areas + "....")
         if r["SEX"] == "SEX_T" and r["AGE"] == "AGE_YTHADULT_YGE15" and r["FREQ"] == "A"]
prod = {(r["REF_AREA"], r["TIME_PERIOD"]): float(r["OBS_VALUE"]) for r in get("DF_GDP_2HRW_NOC_NB", areas + "..")}
rows = []
for a, name in C.items():
    h = sorted((r for r in hours if r["REF_AREA"] == a), key=lambda r: r["TIME_PERIOD"])
    h = [r for r in h if (a, r["TIME_PERIOD"]) in prod]
    if not h:
        continue
    r = h[-1]
    rows.append(dict(iso3=a, country=name, year=int(r["TIME_PERIOD"]), weekly_hours=round(float(r["OBS_VALUE"]), 1),
                     output_per_hour=round(prod[(a, r["TIME_PERIOD"])], 1), hours_source=r["SOURCE"]))
d = json.loads(OUT.read_text())
d["international"] = {"source": "ILOSTAT via sdmx.ilo.org: average weekly hours actually worked per employed person (ages 15+); output per hour worked, GDP constant 2021 international $ at PPP (ILO modelled estimates)",
                      "rows": sorted(rows, key=lambda r: -r["weekly_hours"])}
OUT.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
for r in d["international"]["rows"]:
    print(r["country"], r["year"], r["weekly_hours"], r["output_per_hour"], r["hours_source"][:40])
