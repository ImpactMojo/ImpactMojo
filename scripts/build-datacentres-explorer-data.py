#!/usr/bin/env python3
"""Data centres explorer: keep the page's inline data equal to the snapshot.

    python3 scripts/build-datacentres-explorer-data.py           # write datacentres.html's inline block
    python3 scripts/build-datacentres-explorer-data.py --check   # CI: fail if stale or inconsistent
    python3 scripts/build-datacentres-explorer-data.py --extract DIR   # needs shapely

data/datacentres-india.json is a snapshot of the public data released with
deSouza, Paul, Mathew, Lippert, Ratti and Duarte, "The Environmental Geography
of Data Centers in India" (SSRN preprint, 2026):

    https://github.com/pdez90/india-datacentre-ej

The facility table and the policy tables are CC BY-NC 4.0. The power plants
are from the WRI Global Power Plant Database (CC BY 4.0) and the state
outlines are dissolved from DataMeet's Census 2011 districts (CC BY 2.5 IN).
The page that shows them is free, carries no buy link, and credits the authors
on every view. The Prayas ESMI outage tables in that repository are not
copied here.

datacentres.html carries the same data inline, so there are two copies and an
edit to one is invisible in the other. This script writes the page's copy from
the snapshot, and before it writes anything it checks the snapshot against the
figures the authors publish beside it:

  - the facilities by status equal the authors' own headline counts
    (233 operating, 60 under construction, 36 announced, 329 in all);
  - the facilities per state equal the counts in the authors' policy table,
    for both the operating set and the whole inventory, in all 18 states;
  - the operating facilities in states with a dedicated policy equal the
    authors' figure (200), and so does the whole-inventory figure (293);
  - every facility has a status, a state and coordinates inside India;
  - a capacity that was not published is null, never zero.

A facility with no published IT load stays null on the page. The authors model
a load for those sites to run their pollution estimates; that modelled figure
is an allocation, they say so, and it is not shown here as if it were measured.

--extract reads a clone of the repository above and rewrites the snapshot. It
needs shapely for the state outlines. Do it once per release of the inventory.
"""
import csv
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "datacentres-india.json"
PAGE = ROOT / "datacentres.html"
SLOT = re.compile(r'(<script id="dc-data" type="application/json">)(.*?)(</script>)', re.S)

STATUSES = ["operating", "under construction", "announced (planned)"]
TYPES = ["colocation", "hyperscale", "telecom", "enterprise", "government"]
# Map frame, in degrees. The outline and the points share it.
LON0, LON1, LAT0, LAT1 = 67.5, 98.0, 6.0, 37.6
W = 600.0
KX = W / (LON1 - LON0)


def merc(lat):
    return math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))


M1, M0 = merc(LAT1), merc(LAT0)
H = round(KX * math.degrees(M1 - M0), 1)


def project(lon, lat):
    x = (lon - LON0) * KX
    y = (M1 - merc(lat)) * KX * 180 / math.pi
    return round(x, 1), round(y, 1)


def fail(msg):
    sys.exit("FAIL: " + msg)


def num(s):
    s = (s or "").strip()
    return float(s) if s else None


def extract(src):
    """Read a clone of pdez90/india-datacentre-ej into the snapshot's shape."""
    try:
        from shapely.geometry import shape
        from shapely.ops import unary_union
    except ImportError:
        fail("--extract needs shapely (pip install shapely)")
    src = Path(src)
    d = src / "data"
    rows = list(csv.DictReader(open(d / "india_datacentres_public.csv", encoding="utf-8")))
    fac = []
    for r in rows:
        fac.append({
            "id": r["facility_id"],
            "name": r["facility_name"].strip(),
            "operator": r["operator"].strip(),
            "type": r["facility_type"].strip(),
            "status": r["status"].strip(),
            "city": r["city"].strip(),
            "state": r["state_current"].strip(),
            "lat": round(float(r["latitude"]), 4),
            "lon": round(float(r["longitude"]), 4),
            "precision": r["location_precision"].strip(),
            "mw": num(r["mw_it_reported_current"]),
            "mw_buildout": num(r["mw_it_reported_buildout"]),
            "mw_uncertain": r["mw_certainty"].strip().startswith("reported, but uncertain"),
            "confidence": r["confidence"].strip(),
            "source": r["source_url"].strip(),
        })
    pol = []
    for r in csv.DictReader(open(d / "policies.csv", encoding="utf-8")):
        pol.append({
            "state": r["state"].strip(),
            "policy": r["policy_name"].strip(),
            "year": r["policy_year"].strip(),
            "has_policy": r["has_policy"].strip().upper() == "TRUE",
            "capital_subsidy": r["capital_subsidy"].strip(),
            "stamp_duty": r["stamp_duty_exemption"].strip(),
            "electricity_duty": r["electricity_duty_exemption"].strip(),
            "land": r["land_incentive"].strip(),
            "single_window": r["single_window"].strip(),
            "eia_required": r["eia_required"].strip(),
            "operating": int(r["dc_count"]),
            "all": int(r["dc_count_all"]),
            "share_high_stress": num(r["share_dists_high_stress"]),
        })
    plants = []
    for f in json.load(open(d / "plants.geojson", encoding="utf-8"))["features"]:
        p = f["properties"]
        lon, lat = f["geometry"]["coordinates"]
        plants.append({"name": p["name"], "fuel": p["fuel"], "state": p["state"],
                       "mw": round(p["capacity_mw"]), "lat": round(lat, 3), "lon": round(lon, 3)})
    # State outlines: dissolve the districts, simplify, project.
    by_state = {}
    for f in json.load(open(d / "districts.geojson", encoding="utf-8"))["features"]:
        by_state.setdefault(f["properties"]["state_name"], []).append(shape(f["geometry"]).buffer(0))
    paths = []
    for name in sorted(by_state):
        g = unary_union(by_state[name]).simplify(0.06, preserve_topology=True)
        polys = [g] if g.geom_type == "Polygon" else list(g.geoms)
        seg = []
        for poly in polys:
            if poly.area < 0.01:
                continue
            pts = [project(x, y) for x, y in poly.exterior.coords]
            seg.append("M" + "L".join("%g,%g" % p for p in pts) + "Z")
        if seg:
            paths.append("".join(seg))
    head = json.load(open(d / "headline.json", encoding="utf-8"))
    out = {
        "_note": "Snapshot of the public data released with deSouza et al. (2026). "
                 "Rebuild with scripts/build-datacentres-explorer-data.py --extract; do not edit by hand.",
        "source": {
            "paper": "deSouza, P., Paul, S., Mathew, D., Lippert, A.M., Ratti, C., Duarte, F. (2026). "
                     "The Environmental Geography of Data Centers in India. SSRN preprint.",
            "repository": "https://github.com/pdez90/india-datacentre-ej",
            "inventory_cutoff": rows[0]["inventory_version"],
            "licence": "CC BY-NC 4.0 (facility and policy tables); WRI Global Power Plant Database, "
                       "CC BY 4.0 (power plants); DataMeet Census 2011 districts, CC BY 2.5 IN (outlines)",
        },
        "headline": {k: head[k] for k in (
            "n_operating", "n_all", "n_construction", "n_announced",
            "hosting_districts_operating", "hosting_districts_all",
            "policy_states_dedicated", "policy_states_reviewed",
            "facilities_in_policy_states", "facilities_in_policy_states_all",
            "twh_operating", "pct_nat_gen_operating")},
        "map": {"w": W, "h": H, "paths": paths},
        "facilities": fac,
        "policies": pol,
        "plants": plants,
    }
    RAW.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print("wrote %s: %d facilities, %d policy rows, %d plants, %d outlines" % (
        RAW.relative_to(ROOT), len(fac), len(pol), len(plants), len(paths)))


def validate(data):
    problems = []
    fac, head, pol = data["facilities"], data["headline"], data["policies"]
    by_status = Counter(f["status"] for f in fac)
    want = {"operating": head["n_operating"], "under construction": head["n_construction"],
            "announced (planned)": head["n_announced"]}
    for s in STATUSES:
        if by_status.get(s, 0) != want[s]:
            problems.append("%s: %d facilities, the authors' headline says %d" % (s, by_status.get(s, 0), want[s]))
    if set(by_status) - set(STATUSES):
        problems.append("unknown status: %s" % sorted(set(by_status) - set(STATUSES)))
    if len(fac) != head["n_all"]:
        problems.append("%d facilities, the authors' headline says %d" % (len(fac), head["n_all"]))
    if len({f["id"] for f in fac}) != len(fac):
        problems.append("duplicate facility id")
    op_state = Counter(f["state"] for f in fac if f["status"] == "operating")
    all_state = Counter(f["state"] for f in fac)
    alias = {"Delhi (NCT)": "Delhi"}
    in_policy = in_policy_all = 0
    for p in pol:
        names = [p["state"], alias.get(p["state"], p["state"])]
        o = max(op_state.get(n, 0) for n in names)
        a = max(all_state.get(n, 0) for n in names)
        if o != p["operating"] or a != p["all"]:
            problems.append("%s: %d operating and %d in all, the policy table says %d and %d" % (
                p["state"], o, a, p["operating"], p["all"]))
        if p["has_policy"]:
            in_policy += o
            in_policy_all += a
    if in_policy != head["facilities_in_policy_states"]:
        problems.append("%d operating facilities in policy states, the authors say %d" % (
            in_policy, head["facilities_in_policy_states"]))
    if in_policy_all != head["facilities_in_policy_states_all"]:
        problems.append("%d facilities in policy states, the authors say %d" % (
            in_policy_all, head["facilities_in_policy_states_all"]))
    if sum(1 for p in pol if p["has_policy"]) != head["policy_states_dedicated"]:
        problems.append("policy states with a dedicated policy do not number %d" % head["policy_states_dedicated"])
    for f in fac:
        if not (f["name"] and f["state"] and f["operator"]):
            problems.append("%s: missing name, operator or state" % f["id"])
        if f["type"] not in TYPES:
            problems.append("%s: unknown type %r" % (f["id"], f["type"]))
        if not (LON0 < f["lon"] < LON1 and LAT0 < f["lat"] < LAT1):
            problems.append("%s: coordinates outside India" % f["id"])
        for k in ("mw", "mw_buildout"):
            if f[k] is not None and f[k] <= 0:
                problems.append("%s: %s is %r; an unpublished capacity must be null" % (f["id"], k, f[k]))
        if not f["source"].startswith("http"):
            problems.append("%s: no source link" % f["id"])
    for p in data["plants"]:
        if p["fuel"] not in ("Coal", "Gas") or not (LON0 < p["lon"] < LON1 and LAT0 < p["lat"] < LAT1):
            problems.append("plant %s: bad fuel or coordinates" % p["name"])
    if len(data["map"]["paths"]) < 30:
        problems.append("fewer than 30 state outlines")
    return problems


def main():
    if "--extract" in sys.argv:
        i = sys.argv.index("--extract")
        if len(sys.argv) <= i + 1:
            fail("--extract needs the path of a clone of pdez90/india-datacentre-ej")
        extract(sys.argv[i + 1])
    data = json.loads(RAW.read_text(encoding="utf-8"))
    problems = validate(data)
    if problems:
        fail("data/datacentres-india.json is inconsistent:\n  " + "\n  ".join(problems[:20]))
    payload = json.dumps({k: v for k, v in data.items() if k != "_note"},
                         ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = PAGE.read_text(encoding="utf-8")
    m = SLOT.search(page)
    if not m:
        fail("datacentres.html has no dc-data slot")
    if "--check" in sys.argv:
        if m.group(2) != payload:
            fail("datacentres.html inline data is stale. Run python3 scripts/build-datacentres-explorer-data.py")
        print("PASS: datacentres.html matches data/datacentres-india.json (%d facilities; counts by status and by "
              "state equal the authors' own)" % len(data["facilities"]))
        return
    PAGE.write_text(page[:m.start(2)] + payload + page[m.end(2):], encoding="utf-8")
    print("wrote datacentres.html inline data from %s" % RAW.relative_to(ROOT))


if __name__ == "__main__":
    main()
