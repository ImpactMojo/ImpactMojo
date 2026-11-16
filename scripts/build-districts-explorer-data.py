#!/usr/bin/env python3
"""District Lineage Explorer: keep the page's inline data equal to the snapshot.

    python3 scripts/build-districts-explorer-data.py           # write districts.html's inline block
    python3 scripts/build-districts-explorer-data.py --check   # CI: fail if stale or inconsistent
    python3 scripts/build-districts-explorer-data.py --extract DIR

data/districts-india.json is a snapshot of four tables published by India State
Stories (Shivakumar Jolad and Mehr Kalra, FLAME University,
https://www.indiastatestory.in/datadownloads):

    District_Timeseries_1951-2024.csv            one row per line of descent
    District_splits_and_carveouts_1951_to_2024.csv
    New_districts_created_1951_to_2024.csv
    District_name_changes_1951_to_2021.csv

--extract reads them from a folder. The copies used here came from the public
mirror github.com/yashveeeeeeer/india-geodata (data/census/historical), and the
splits table was compared with the authors' own Google Sheet.

The same folder must hold one more file, districts.<date>.csv: the district list
of the Government of India's Local Government Directory (lgdirectory.gov.in), as
archived daily at github.com/ramSeraph/opendata (release lgd-latest). It becomes
the ninth column, 2026. The source's tables stop at a 2024 list of 760 districts;
the directory had 790 on 16 November 2026. Joining the two is ImpactMojo's work
and every step of it is a table in this file:

    ALIAS    a 2024 district and the directory's spelling of the same district
    ADDED    a directory district the 2024 list lacks, with its parent districts
             and where the parentage was read
    BRIDGE   four places where one list holds a unit the other does not
    DELHI    redrawn in December 2025: all 11 old districts link to all 13 new
    CANCELLED  nine Rajasthan districts of 2023 that were abolished in 2024

What this script changes in the source, all of it listed in FIXES and shown on
the page: three duplicate rows in the crosswalk are dropped, the 2024 state of
one row reads "Visakhapatnam" and is set to Andhra Pradesh, and five 2024 rows
that say "Delhi" are set to "NCT of Delhi" to match the other nine. Leading and
trailing spaces are removed. Nothing else is altered: spellings, and years that
fall outside their own decade, are kept as printed and flagged.

Before writing anything it checks:

  - the crosswalk has 640 districts in 2011, the Census of India's own count,
    and 466, 412 and 356 in 1991, 1981 and 1971;
  - 2001 has 592 against the census's 593, a gap pinned in KNOWN so that any
    other figure fails;
  - every row of the crosswalk names a state and a district in all eight years;
  - the number of rows whose year lies outside its decade equals the pinned
    count, so a new one is noticed;
  - the 2026 column has the directory's 790 districts, every one of them reached
    by at least one line of descent, and every 2024 district leads somewhere;
  - no ALIAS, ADDED or BRIDGE entry is unused, so a stale one fails.
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "districts-india.json"
PAGE = ROOT / "districts.html"
SLOT = re.compile(r'(<script id="dl-data" type="application/json">)(.*?)(</script>)', re.S)
YEARS = [1951, 1961, 1971, 1981, 1991, 2001, 2011, 2024, 2026]
CENSUS = {1971: 356, 1981: 412, 1991: 466, 2011: 640}
KNOWN = {"districts_2001": 592, "census_2001": 593, "duplicate_rows": 3,
         "list_2024": 760, "directory_2026": 790, "added": 32, "with_census_2011_code": 638}
FIXES = [
    "Three duplicate rows in the crosswalk were dropped.",
    "One 2024 row gave its state as Visakhapatnam; it is set to Andhra Pradesh.",
    "Five 2024 rows gave the state as Delhi; they are set to NCT of Delhi, as the other nine rows have it.",
]


def fail(msg):
    sys.exit("FAIL: " + msg)


def rows(path):
    r = list(csv.reader(open(path, encoding="utf-8-sig")))
    return [[c.strip() for c in x] for x in r[1:] if any(c.strip() for c in x)]


def year(s):
    m = re.match(r"(\d{4})", s)
    return int(m.group(1)) if m else None


# ---------------------------------------------------------------- the 2026 column
DIRECTORY = {
    "name": "Local Government Directory, Ministry of Panchayati Raj, Government of India",
    "url": "https://lgdirectory.gov.in/",
    "copy": "https://github.com/ramSeraph/opendata/releases/tag/lgd-latest",
    "as_of": "2026-11-16",
}
# A state of the 2024 list and the directory's name for it, where they differ.
STATE = {
    "Andaman and Nicobar Islands": "Andaman And Nicobar Islands",
    "Jammu & Kashmir": "Jammu And Kashmir",
    "NCT of Delhi": "Delhi",
    "Daman & Diu": "The Dadra And Nagar Haveli And Daman And Diu",
    "Dadara & Nagar Havelli": "The Dadra And Nagar Haveli And Daman And Diu",
}
# (state in the 2024 list, district in the 2024 list) -> the directory's spelling.
# A third item moves the district to another state of the directory.
ALIAS = {
    ("Andaman and Nicobar Islands", "Nicobar"): ("Nicobars",),
    ("Andaman and Nicobar Islands", "South Andaman"): ("South Andamans",),
    ("Andhra Pradesh", "Anantapur"): ("Ananthapuramu",),
    ("Andhra Pradesh", "Y.S.R."): ("Y.S.R. Kadapa",),
    ("Arunachal Pradesh", "Pakke-Kesang"): ("Pakke Kessang",),
    ("Assam", "Kamrup Metropolitan"): ("Kamrup Metro",),
    ("Assam", "Karimganj"): ("Sribhumi",),
    ("Assam", "Morigaon"): ("Marigaon",),
    ("Assam", "South Salmara-Mankachar"): ("South Salmara Mancachar",),
    ("Bihar", "Purba Champaran"): ("Purbi Champaran",),
    ("Chhattisgarh", "Baloda Bazar"): ("Balodabazar-Bhatapara",),
    ("Chhattisgarh", "Balrampur"): ("Balrampur-Ramanujganj",),
    ("Chhattisgarh", "Koriya"): ("Korea",),
    ("Gujarat", "Ahmadabad"): ("Ahmedabad",),
    ("Gujarat", "Aravalli"): ("Arvalli",),
    ("Gujarat", "Dohad"): ("Dahod",),
    ("Gujarat", "The Dangs"): ("Dangs",),
    ("Himachal Pradesh", "Lahul & Spiti"): ("Lahaul And Spiti",),
    ("Jammu & Kashmir", "Badgam"): ("Budgam",),
    ("Jammu & Kashmir", "Bandipore"): ("Bandipora",),
    ("Jammu & Kashmir", "Baramula"): ("Baramulla",),
    ("Jammu & Kashmir", "Punch"): ("Poonch",),
    ("Jammu & Kashmir", "Shupiyan"): ("Shopian",),
    ("Jammu & Kashmir", "Kargil"): ("Kargil", "Ladakh"),
    ("Jammu & Kashmir", "Leh (Ladakh)"): ("Leh Ladakh", "Ladakh"),
    ("Jharkhand", "Kodarma"): ("Koderma",),
    ("Jharkhand", "Pashchimi Singhbhum"): ("West Singhbhum",),
    ("Jharkhand", "Purbi Singhbhum"): ("East Singhbum",),
    ("Jharkhand", "Sahibganj"): ("Sahebganj",),
    ("Karnataka", "Bagalkot"): ("Bagalkote",),
    ("Karnataka", "Bangalore"): ("Bengaluru Urban",),
    ("Karnataka", "Bangalore Rural"): ("Bengaluru Rural",),
    ("Karnataka", "Belgavi"): ("Belagavi",),
    ("Kerala", "Kasargod"): ("Kasaragod",),
    ("Madhya Pradesh", "Annupur"): ("Anuppur",),
    ("Maharashtra", "Ahmadnagar"): ("Ahilyanagar",),
    ("Maharashtra", "Bid"): ("Beed",),
    ("Maharashtra", "Buldana"): ("Buldhana",),
    ("Maharashtra", "Gondiya"): ("Gondia",),
    ("Maharashtra", "Raigarh"): ("Raigad",),
    ("Maharashtra", "Sambhaji Nagar"): ("Chhatrapati Sambhajinagar",),
    ("Mizoram", "Hnathial"): ("Hnahthial",),
    ("Mizoram", "Saiha"): ("Siaha",),
    ("Nagaland", "Tseminyü"): ("Tseminyu",),
    ("Odisha", "Anugul"): ("Anugola",),
    ("Odisha", "Bargarh"): ("Baragada",),
    ("Odisha", "Baudh"): ("Boudh",),
    ("Odisha", "Cuttack"): ("Kataka",),
    ("Odisha", "Debagarh"): ("Debagada",),
    ("Odisha", "Jajapur"): ("Jajpur",),
    ("Odisha", "Kandhamal"): ("Kandhamala",),
    ("Odisha", "Kendrapara"): ("Kendrapada",),
    ("Odisha", "Nabarangapur"): ("Nabarangpur",),
    ("Odisha", "Nayagarh"): ("Nayagada",),
    ("Odisha", "Sundargarh"): ("Sundaragada",),
    ("Punjab", "Firozpur"): ("Ferozepur",),
    ("Punjab", "Sahibzada Ajit Singh Nagar"): ("S.A.S Nagar",),
    ("Rajasthan", "Chittaurgarh"): ("Chittorgarh",),
    ("Rajasthan", "Dhaulpur"): ("Dholpur",),
    ("Rajasthan", "Jalor"): ("Jalore",),
    ("Rajasthan", "Jhunjhunun"): ("Jhunjhunu",),
    ("Tamil Nadu", "Tirupattur"): ("Tirupathur",),
    ("Telangana", "Jagtial"): ("Jagitial",),
    ("Telangana", "Jangaon"): ("Jangoan",),
    ("Telangana", "Jayashankar Bhupalpally"): ("Jayashankar Bhupalapally",),
    ("Telangana", "Kumuram Bheem"): ("Kumuram Bheem Asifabad",),
    ("Telangana", "Mahbubnagar"): ("Mahabubnagar",),
    ("Telangana", "Warangal Rural"): ("Warangal",),
    ("Telangana", "Warangal Urban (Hanamkonda)"): ("Hanumakonda",),
    ("Tripura", "Sipahijala"): ("Sepahijala",),
    ("Uttarakhand", "Garhwal"): ("Pauri Garhwal",),
    ("Uttarakhand", "Hardwar"): ("Haridwar",),
    ("West Bengal", "Darjiling"): ("Darjeeling",),
    ("West Bengal", "Haora"): ("Howrah",),
    ("West Bengal", "Hugli"): ("Hooghly",),
    ("West Bengal", "Koch Bihar"): ("Cooch Behar",),
    ("West Bengal", "Maldah"): ("Malda",),
    ("West Bengal", "North Twenty Four Parganas"): ("North 24 Parganas",),
    ("West Bengal", "Pashchim Barddhaman"): ("Paschim Bardhaman",),
    ("West Bengal", "Purba Barddhaman"): ("Purba Bardhaman",),
    ("West Bengal", "Puruliya"): ("Purulia",),
    ("West Bengal", "South Twenty Four Parganas"): ("South 24 Parganas",),
}
# Districts of the directory that the 2024 list does not have.
# (directory state, directory district, year, [(2024 state, 2024 district), ...], where the parentage was read)
_RJ = "India State Stories split records"
_CG = "https://rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=12434"
_LA = "https://ladakh.gov.in/?p=56271"
_MP = "https://deccanchronicle.com/nation/current-affairs/060923/madhya-pradesh-set-to-get-its-57th-district.html"
_AR = "https://www.theweek.in/wire-updates/national/2024/02/08/ces12-ar-assembly-bill.html"
_AP = "https://www.thenewsminute.com/andhra-pradesh/andhra-pradesh-adds-polavaram-and-markapuram-as-two-new-districts"
ADDED = [
    ("Andhra Pradesh", "Markapuram", 2025, [("Andhra Pradesh", "Prakasam")], _AP),
    ("Andhra Pradesh", "Polavaram", 2025, [("Andhra Pradesh", "Alluri Sitharama Raju")], _AP),
    ("Arunachal Pradesh", "Bichom", 2024, [("Arunachal Pradesh", "East Kameng"), ("Arunachal Pradesh", "West Kameng")], _AR),
    ("Arunachal Pradesh", "Keyi Panyor", 2024, [("Arunachal Pradesh", "Lower Subansiri")], _AR),
    ("Chhattisgarh", "Khairagarh-Chhuikhadan-Gandai", 2022, [("Chhattisgarh", "Rajnandgaon")], _CG),
    ("Chhattisgarh", "Manendragarh-Chirmiri-Bharatpur(M C B)", 2022, [("Chhattisgarh", "Koriya")], _CG),
    ("Chhattisgarh", "Mohla-Manpur-Ambagarh Chouki", 2022, [("Chhattisgarh", "Rajnandgaon")],
     "https://www.drishtiias.com/state-pcs-current-affairs/mohla-manpur-ambagarh-chowki-becomes-29th-district-of-chhattisgarh"),
    ("Chhattisgarh", "Sakti", 2022, [("Chhattisgarh", "Janjgir-Champa")], _CG),
    ("Chhattisgarh", "Sarangarh-Bilaigarh", 2022, [("Chhattisgarh", "Raigarh"), ("Chhattisgarh", "Baloda Bazar")], _CG),
    ("Goa", "Kushavati", 2025, [("Goa", "South Goa")], "https://kushavati.goa.gov.in/?p=1532"),
    ("Gujarat", "Vav-Tharad", 2025, [("Gujarat", "Banas Kantha")],
     "https://newsonair.gov.in/gujarat-govt-approves-creation-of-new-district-named-vav-tharad"),
    ("Haryana", "Hansi", 2025, [("Haryana", "Hisar")],
     "https://www.theweek.in/wire-updates/national/2025/12/17/des102-hr-new-district-cabinet.html"),
    ("Ladakh", "Changthang", 2026, [("Jammu & Kashmir", "Leh (Ladakh)")], _LA),
    ("Ladakh", "Nubra", 2026, [("Jammu & Kashmir", "Leh (Ladakh)")], _LA),
    ("Ladakh", "Sham", 2026, [("Jammu & Kashmir", "Leh (Ladakh)")], _LA),
    ("Ladakh", "Drass", 2026, [("Jammu & Kashmir", "Kargil")], _LA),
    ("Ladakh", "Zanskar", 2026, [("Jammu & Kashmir", "Kargil")], _LA),
    ("Ladakh", "Sankoo", 2026, [("Jammu & Kashmir", "Kargil")],
     "https://www.manoramayearbook.in/current-affairs/india/2026/10/16/ladakh-sankoo-eighth-district.html"),
    ("Madhya Pradesh", "MAUGANJ", 2023, [("Madhya Pradesh", "Rewa")], _MP),
    ("Madhya Pradesh", "Maihar", 2023, [("Madhya Pradesh", "Satna")], _MP),
    ("Madhya Pradesh", "Pandhurna", 2023, [("Madhya Pradesh", "Chhindwara")], _MP),
    ("Meghalaya", "South West Garo Hills", 2012, [("Meghalaya", "West Garo Hills")],
     "https://theshillongtimes.com/2012/08/08/cm-inaugurates-another-district/"),
    ("Nagaland", "Meluri", 2024, [("Nagaland", "Phek")],
     "https://www.newsonair.gov.in/meluri-officially-becomes-17th-district-of-nagaland"),
    ("Nagaland", "Shamator", 2022, [("Nagaland", "Tuensang")],
     "https://morungexpress.com/from-3-to-17-is-the-number-of-districts-affecting-nagalands-good-governance"),
    ("Rajasthan", "Balotra", 2023, [("Rajasthan", "Barmer")], _RJ),
    ("Rajasthan", "Beawar", 2023, [("Rajasthan", "Ajmer"), ("Rajasthan", "Pali"), ("Rajasthan", "Bhilwara")],
     "https://citypopulation.de/en/india/rajasthan/admin/834__beawar"),
    ("Rajasthan", "Deeg", 2023, [("Rajasthan", "Bharatpur")], _RJ),
    ("Rajasthan", "Didwana-Kuchaman", 2023, [("Rajasthan", "Nagaur")], _RJ),
    ("Rajasthan", "Khairthal-Tijara", 2023, [("Rajasthan", "Alwar")], _RJ),
    ("Rajasthan", "Kotputli-Behror", 2023, [("Rajasthan", "Jaipur"), ("Rajasthan", "Alwar")],
     "https://www.citypopulation.de/en/india/rajasthan/admin/842__kotputli_behror"),
    ("Rajasthan", "Phalodi", 2023, [("Rajasthan", "Jodhpur")], _RJ),
    ("Rajasthan", "Salumbar", 2023, [("Rajasthan", "Udaipur")], _RJ),
]
# One list holds a unit the other does not. (2024 state, 2024 district) -> directory districts, and why.
BRIDGE = {
    ("Meghalaya", "Jaintia Hills"): (["East Jaintia Hills", "West Jaintia Hills"],
        "The 2024 list still carries Jaintia Hills, which was divided into East and West Jaintia Hills in 2012. It is linked to both."),
    ("West Bengal", "Barddhaman"): (["Purba Bardhaman", "Paschim Bardhaman"],
        "The 2024 list carries Barddhaman beside the two districts it was divided into in 2017. It is linked to both."),
    ("Puducherry", "Mahe"): (["Puducherry"],
        "The census counts Mahe and Yanam as districts. The directory lists two districts for Puducherry, and Mahe and Yanam are regions of Puducherry district there, so both are linked to it."),
    ("Puducherry", "Yanam"): (["Puducherry"], ""),
}
DELHI = ("Delhi was redrawn on 25 December 2025 from 11 districts into 13, to match the municipal zones. Shahdara was dissolved, "
         "Old Delhi, Central North and Outer North were formed, and the ten districts that kept their names changed their boundaries. "
         "No district of the old map equals one of the new, so all 11 are linked to all 13 and the only safe comparison is Delhi as a whole.")
DELHI_URL = "https://www.theweek.in/wire-updates/national/2025/12/26/des55-dl-districts-notification.html"
# Created on 7 August 2023, abolished by the state cabinet on 28 December 2024. The names are the split records' spellings.
CANCELLED = {
    "state": "Rajasthan", "created": 2023, "ended": 2024,
    "names": ["Anupgarh district", "Dudu district", "Gangapur district", "Jaipur Rural", "Jaipur Urban",
              "Jodhpur Rural", "Jodhpur Urban", "Kekri district", "Neem Ka Thana", "Sanchore district", "Shahpura district"],
    "url": "https://www.newsonair.gov.in/rajasthan-govt-announces-to-dissolve-9-out-of-17-districts-created-by-previous-govt",
    "note": "Rajasthan reorganised its districts on 7 August 2023, which took the count from 33 to 50. "
            "On 28 December 2024 the state cabinet abolished nine of the new districts and kept eight, which leaves 41. "
            "This page assumes the area of each abolished district went back to the district it was taken from. "
            "It has not checked that tehsil by tehsil.",
}


def nd(s):
    s = re.sub(r"\(.*?\)", "", s.lower().replace("&", "and")).strip()
    return re.sub(r"[^a-z]", "", re.sub(r"district$", "", s))


def directory(src, units24, links8):
    """Return the 2026 units and the nine-column links."""
    files = sorted(Path(src).glob("districts.*.csv"))
    if len(files) != 1:
        fail("--extract needs exactly one districts.<date>.csv (the Local Government Directory list) in %s" % src)
    rr = list(csv.DictReader(open(files[0], encoding="utf-8-sig")))
    u26 = sorted(([r["State Name (In English)"].strip(), r["District Name(In English)"].strip(),
                   int(r["District Code"]), int(r["Census 2011 Code"] or 0)] for r in rr), key=lambda x: (x[0], x[1]))
    exact = {(s, n): i for i, (s, n, _, _) in enumerate(u26)}
    loose = {}
    for i, (s, n, _, _) in enumerate(u26):
        if (s, nd(n)) in loose:
            fail("two directory districts of %s read alike: %s" % (s, n))
        loose[(s, nd(n))] = i
    idx24 = {tuple(u): k for k, u in enumerate(units24)}
    for table, what in ((ALIAS, "ALIAS"), (BRIDGE, "BRIDGE")):
        for k in table:
            if k not in idx24:
                fail("%s names %s, %s, which the 2024 list does not have" % (what, k[1], k[0]))
    delhi = [i for i, u in enumerate(u26) if u[0] == "Delhi"]
    tg, direct = {}, {}
    for k, (s, n) in enumerate(units24):
        s26 = STATE.get(s, s)
        if s26 == "Delhi":
            tg[k] = set(delhi)
            continue
        if (s, n) in BRIDGE:
            got = [exact.get((s26, x)) for x in BRIDGE[(s, n)][0]]
        elif (s, n) in ALIAS:
            a = ALIAS[(s, n)]
            got = [exact.get((a[1] if len(a) > 1 else s26, a[0]))]
            if loose.get((s26, nd(n))) is not None and len(a) == 1 and loose[(s26, nd(n))] != got[0]:
                fail("ALIAS for %s, %s is not needed or points elsewhere" % (n, s))
        else:
            got = [loose.get((s26, nd(n)))]
        if any(g is None for g in got):
            fail("no directory district for %s, %s of the 2024 list" % (n, s))
        if (s, n) not in BRIDGE:
            if got[0] in direct:
                fail("%s, %s and %s both map to one directory district" % (n, s, units24[direct[got[0]]][1]))
            direct[got[0]] = k
        tg[k] = set(got)
    for s26, n26, _, parents, _ in ADDED:
        c = exact.get((s26, n26))
        if c is None:
            fail("ADDED names %s, %s, which the directory does not list" % (n26, s26))
        if c in direct:
            fail("ADDED names %s, %s, but the 2024 list already has it" % (n26, s26))
        for p in parents:
            if p not in idx24:
                fail("ADDED gives %s, %s as a parent; the 2024 list has no such district" % (p[1], p[0]))
            tg[idx24[p]].add(c)
    reached = set().union(*tg.values())
    missing = [u26[i][1] + ", " + u26[i][0] for i in range(len(u26)) if i not in reached]
    if missing:
        fail("directory districts with no line of descent: " + "; ".join(missing))
    links, seen = [], set()
    for r in links8:
        for t in sorted(tg[r[7]]):
            row = tuple(r) + (t,)
            if row not in seen:
                seen.add(row)
                links.append(list(row))
    return u26, links, files[0].name


def extract(src):
    src = Path(src)
    t = rows(src / "District_Timeseries_1951-2024.csv")
    seen, links_raw, dups = set(), [], 0
    for r in t:
        r = r[:16]
        if r[14] == "Visakhapatnam":
            r[14] = "Andhra Pradesh"
        if r[14] == "Delhi":
            r[14] = "NCT of Delhi"
        k = tuple(r)
        if k in seen:
            dups += 1
            continue
        seen.add(k)
        links_raw.append(r)
    units, index = [[] for _ in YEARS[:8]], [{} for _ in YEARS[:8]]
    links = []
    for r in links_raw:
        row = []
        for i in range(8):
            key = (r[2 * i], r[2 * i + 1])
            if key not in index[i]:
                index[i][key] = len(units[i])
                units[i].append(list(key))
            row.append(index[i][key])
        links.append(row)
    splits = [[r[0], r[1], year(r[2]), r[3], r[4]] for r in rows(src / "District_splits_and_carveouts_1951_to_2024.csv")]
    created = [[r[0], r[1], year(r[2]), r[3], r[4]] for r in rows(src / "New_districts_created_1951_to_2024.csv")]
    renames = [[r[0], r[1], r[2], r[3], r[4]] for r in rows(src / "District_name_changes_1951_to_2021.csv")]
    u26, links, lgd_file = directory(src, units[7], links)
    units.append(u26)
    notes = [[k[0], v[1]] for k, v in sorted(BRIDGE.items()) if v[1]] + [["Delhi", DELHI]]
    out = {
        "_note": "Snapshot of four India State Stories tables. Rebuild with "
                 "scripts/build-districts-explorer-data.py --extract; do not edit by hand.",
        "source": {
            "name": "India State Stories, FLAME University (Shivakumar Jolad and Mehr Kalra)",
            "url": "https://www.indiastatestory.in/datadownloads",
            "copy": "https://github.com/yashveeeeeeer/india-geodata/tree/main/data/census/historical",
        },
        "directory": dict(DIRECTORY, file=lgd_file, aliases=len(ALIAS)),
        "duplicates_dropped": dups,
        "fixes": FIXES,
        "added": [[a[0], a[1], a[2], [p[1] for p in a[3]], a[4]] for a in ADDED],
        "notes": notes,
        "delhi_url": DELHI_URL,
        "cancelled": CANCELLED,
        "years": YEARS,
        "units": units,
        "links": links,
        "splits": splits,
        "created": created,
        "renames": renames,
    }
    RAW.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print("wrote %s: %d lines of descent, %d districts in the directory, %d split rows, %d creation rows, %d renamings" % (
        RAW.relative_to(ROOT), len(links), len(u26), len(splits), len(created), len(renames)))


def off_decade(table):
    n = 0
    for r in table:
        m = re.match(r"(\d{4})-(\d{4})", r[1])
        if r[2] is None or not m or not (int(m.group(1)) <= r[2] <= int(m.group(2))):
            n += 1
    return n


def validate(d):
    p = []
    counts = {y: len(u) for y, u in zip(d["years"], d["units"])}
    for y, n in CENSUS.items():
        if counts[y] != n:
            p.append("%d has %d districts, the Census of India counted %d" % (y, counts[y], n))
    if counts[2001] != KNOWN["districts_2001"]:
        p.append("2001 has %d districts; %d is the pinned figure (census: %d)" % (
            counts[2001], KNOWN["districts_2001"], KNOWN["census_2001"]))
    if d["duplicates_dropped"] != KNOWN["duplicate_rows"]:
        p.append("%d duplicate rows dropped, %d expected" % (d["duplicates_dropped"], KNOWN["duplicate_rows"]))
    for i, u in enumerate(d["units"]):
        if any(not x[0] or not x[1] for x in u):
            p.append("%d: a blank state or district" % d["years"][i])
        if len({tuple(x[:2]) for x in u}) != len(u):
            p.append("%d: a district listed twice" % d["years"][i])
    for r in d["links"]:
        if len(r) != 9 or any(not (0 <= r[i] < len(d["units"][i])) for i in range(9)):
            p.append("a line of descent points outside the district lists")
            break
    if len({tuple(r) for r in d["links"]}) != len(d["links"]):
        p.append("duplicate lines of descent")
    if any(s == "Visakhapatnam" or s == "Delhi" for s, _ in d["units"][7]):
        p.append("the 2024 state fixes were not applied")
    for i, pin in ((7, "list_2024"), (8, "directory_2026")):
        if counts[d["years"][i]] != KNOWN[pin]:
            p.append("%d has %d districts, %d pinned" % (d["years"][i], counts[d["years"][i]], KNOWN[pin]))
    for i in (7, 8):
        used = {r[i] for r in d["links"]}
        if len(used) != len(d["units"][i]):
            p.append("%d: %d districts have no line of descent" % (d["years"][i], len(d["units"][i]) - len(used)))
    if len(d["added"]) != KNOWN["added"]:
        p.append("%d districts added by hand, %d pinned" % (len(d["added"]), KNOWN["added"]))
    names26 = {(u[0], u[1]) for u in d["units"][8]}
    names24 = {u[1] for u in d["units"][7]}
    for a in d["added"]:
        if (a[0], a[1]) not in names26:
            p.append("added district %s is not in the directory" % a[1])
        if any(x not in names24 for x in a[3]):
            p.append("added district %s has a parent the 2024 list lacks" % a[1])
    codes = [u[2] for u in d["units"][8]]
    if len(set(codes)) != len(codes) or any(not isinstance(c, int) or c <= 0 for c in codes):
        p.append("directory codes are missing or repeated")
    n11 = sum(1 for u in d["units"][8] if u[3])
    if n11 != KNOWN["with_census_2011_code"]:
        p.append("%d directory districts carry a Census 2011 code, %d pinned" % (n11, KNOWN["with_census_2011_code"]))
    if d["directory"]["as_of"] != DIRECTORY["as_of"]:
        p.append("the directory date in the snapshot is not the one this script names")
    for name, pin in (("splits", OFF["splits"]), ("created", OFF["created"])):
        n = off_decade(d[name])
        if n != pin:
            p.append("%s: %d rows have a year outside their decade, %d pinned" % (name, n, pin))
    return p


OFF = {"splits": 6, "created": 3}  # rows whose printed year lies outside their decade; shown flagged on the page


def main():
    if "--extract" in sys.argv:
        i = sys.argv.index("--extract")
        if len(sys.argv) <= i + 1:
            fail("--extract needs the folder holding the four CSV files")
        extract(sys.argv[i + 1])
    d = json.loads(RAW.read_text(encoding="utf-8"))
    if "--report" in sys.argv:
        print({y: len(u) for y, u in zip(d["years"], d["units"])}, off_decade(d["splits"]), off_decade(d["created"]))
        return
    problems = validate(d)
    if problems:
        fail("data/districts-india.json is inconsistent:\n  " + "\n  ".join(problems[:20]))
    payload = json.dumps({k: v for k, v in d.items() if k != "_note"},
                         ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = PAGE.read_text(encoding="utf-8")
    m = SLOT.search(page)
    if not m:
        fail("districts.html has no dl-data slot")
    if "--check" in sys.argv:
        if m.group(2) != payload:
            fail("districts.html inline data is stale. Run python3 scripts/build-districts-explorer-data.py")
        print("PASS: districts.html matches data/districts-india.json (%d lines of descent; 2011 has the census's "
              "640 districts; the 2026 column has the directory's %d)" % (len(d["links"]), len(d["units"][8])))
        return
    PAGE.write_text(page[:m.start(2)] + payload + page[m.end(2):], encoding="utf-8")
    print("wrote districts.html inline data from %s" % RAW.relative_to(ROOT))


if __name__ == "__main__":
    main()
