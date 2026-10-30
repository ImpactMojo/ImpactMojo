#!/usr/bin/env python3
"""By the numbers: one-figure cards computed from data the site already holds.

Each card is a function below that reads the site's own data files, computes
its figures, and returns what the card says, the table behind it, and its
sources. Nothing on a card is typed by hand, so a card cannot drift from the
page that shows its working.

    python3 scripts/by-the-numbers/build.py          # write the page and the manifest
    python3 scripts/by-the-numbers/build.py --check  # fail if either is stale
    node scripts/by-the-numbers/render.mjs           # draw the card images

The script writes by-the-numbers/index.html (the page, with every card's
working), data/by-the-numbers/cards.json (what render.mjs draws), the By the
numbers group on explorers.html, and one site-search row per card in
data/search-index.json, which build-catalog-extras.py then carries into the
catalogue. The number of cards must equal "by-the-numbers" in data/counts.json. Each
image is named by a hash of what it shows, so a changed figure gets a new
file and --check fails until it is drawn.

To add a card: write a function that returns a dict shaped like csr_need()'s,
add it to CARDS, run the build, then render.mjs.
"""
import csv
import hashlib
import html
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "by-the-numbers"
PAGE = ROOT / "by-the-numbers" / "index.html"
MANIFEST = DATA / "cards.json"
EXPLORERS = ROOT / "explorers.html"
SEARCH = ROOT / "data" / "search-index.json"
COUNTS = ROOT / "data" / "counts.json"
EX_START, EX_END = "<!-- by-the-numbers:start -->", "<!-- by-the-numbers:end -->"
IMG_DIR = "assets/by-the-numbers"
SERIES = "By the numbers"
E = html.escape

# The 28 states. Union territories are left out of the state comparisons,
# because the CSR series and the poverty index do not cover the same set of them.
STATES = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa",
          "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala",
          "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
          "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
          "Uttar Pradesh", "Uttarakhand", "West Bengal"]


def fail(msg):
    raise SystemExit("FAIL - " + msg)


def key(name):
    return re.sub(r"\s+", " ", name.lower().replace("&", "and")).strip()


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def rupees(x):
    return "₹" + format(round(x), ",")


def crore(x):
    return "₹" + format(round(x), ",") + " crore"


# ---------------------------------------------------------------- cards

def csr_need():
    year = "2022-23"
    col = "csr_expenditure_2022_23"
    rows = json.loads((ROOT / "data" / "csr-india.json").read_text(encoding="utf-8"))
    csr = {key(r["state_ut"]): r for r in rows["series"]["state"]["rows"]}
    mpi = {key(r["state"]): r for r in read_csv(DATA / "niti-mpi-2023.csv")}
    pop = {key(r["state"]): int(r["persons_1_oct_2022"]) for r in read_csv(DATA / "population-2022-10.csv")}

    total = csr["total"][col]
    unassigned_keys = ("pan india", "pan india (other centralized funds)", "nec/not mentioned")
    unassigned = sum(csr[k][col] for k in unassigned_keys)
    parts = sum(r[col] for k, r in csr.items() if k != "total")
    if abs(parts - total) > 1:
        fail(f"CSR {year}: the rows add to {parts:.2f}, the Total row says {total:.2f}")

    table = []
    for s in STATES:
        k = key(s)
        for src, name in ((csr, "CSR series"), (mpi, "poverty index"), (pop, "population projection")):
            if k not in src:
                fail(f"{s} is missing from the {name}")
        spend = csr[k][col]
        table.append(dict(state=s, mpi=float(mpi[k]["mpi_2019_21"]),
                          headcount=float(mpi[k]["headcount_2019_21"]),
                          crore=spend, pop=pop[k], per_head=spend * 1e7 / pop[k]))
    table.sort(key=lambda r: (-r["mpi"], -r["headcount"]))

    def group(g):
        return sum(r["crore"] for r in g) * 1e7 / sum(r["pop"] for r in g)

    most, least = table[:5], table[-5:]
    # The five at each end must be clear of the sixth, or "the five" is a tie broken by list order.
    # NITI prints the MPI to three decimals, so ties happen; the headcount ratio breaks them.
    rank = [(r["mpi"], r["headcount"]) for r in table]
    if rank[4] == rank[5] or rank[-5] == rank[-6]:
        fail("CSR card: the five-state groups are not separated by MPI and headcount")
    ties = [f"{a['state']} and {b['state']}" for a, b in ((table[4], table[5]), (table[-6], table[-5]))
            if a["mpi"] == b["mpi"]]
    by = {r["state"]: r for r in table}
    top, low = by["Bihar"], by["Maharashtra"]
    ratio_mpi = top["mpi"] / low["mpi"]
    ratio_csr = low["per_head"] / top["per_head"]

    return dict(
        id="csr-need",
        title="CSR spending per resident against multidimensional poverty, by state",
        tags=["CSR", "corporate social responsibility", "multidimensional poverty", "MPI", "NITI Aayog", "state inequality"],
        topic=f"CSR, {year}",
        headline=(f"Bihar received {rupees(top['per_head'])} of company CSR spending per resident "
                  f"in {year}. Maharashtra received {rupees(low['per_head'])}."),
        sub=(f"Bihar's multidimensional poverty index is {ratio_mpi:.1f} times Maharashtra's. "
             f"Maharashtra's CSR per resident is {round(ratio_csr)} times Bihar's."),
        pair=[dict(label="Five states with the most multidimensional poverty",
                   value=rupees(group(most)), unit="CSR per resident",
                   names=[r["state"] for r in most]),
              dict(label="Five states with the least",
                   value=rupees(group(least)), unit="CSR per resident",
                   names=[r["state"] for r in least])],
        chart=dict(title="CSR per resident, states ordered from most to least multidimensional poverty",
                   bars=[[r["state"], round(r["per_head"], 1)] for r in table],
                   highlight=["Bihar", "Maharashtra"],
                   axis=["Most poverty", "Least poverty"], prefix="₹", suffix="", decimals=0),
        note=(f"{crore(unassigned)} ({100 * unassigned / total:.0f}% of the {crore(total)} total) was spent "
              f"\"PAN India\" or with no state named, and is outside every figure here. A project is "
              f"counted in the state the company reported for it."),
        sources=[
            dict(name="Ministry of Corporate Affairs, State/UT-wise CSR expenditure 2018-19 to 2022-23",
                 detail="Open Government Data Platform, resource 80f3abf8-7c91-4966-a37f-8c7b0aae92e9, 2022-23 column",
                 url="https://www.data.gov.in/"),
            dict(name="NITI Aayog, National Multidimensional Poverty Index: A Progress Review 2023",
                 detail="Overview of States and UTs, p. 36; MPI from NFHS-5 (2019-21)",
                 url="https://www.niti.gov.in/sites/default/files/2023-08/India-National-Multidimentional-Poverty-Index-2023.pdf"),
            dict(name="Technical Group on Population Projections, Population Projections for India and States 2011-2036 (MoHFW, November 2019)",
                 detail="Table 14, projected population on 1 October 2022, pp. 121-136",
                 url="https://nhm.gov.in/New_Updates_2018/Report_Population_Projection_2019.pdf")],
        page="/csr.html",
        page_label="CSR Explorer",
        table_title="Every state",
        method=[
            "CSR per resident is a state's 2022-23 CSR spending divided by its projected population on 1 October 2022, the middle of the financial year.",
            "States are ranked by NITI Aayog's multidimensional poverty index (MPI) for 2019-21, and where two share an MPI at the three decimals NITI prints, by the share of people who are poor (the headcount ratio)."
            + (f" That decides {', '.join(ties)}." if ties else ""),
            "The five-state figures pool spending and population across the five, so a small state does not count as much as a large one.",
            f"The {crore(unassigned)} recorded as \"PAN India\", \"PAN India (Other Centralized Funds)\" or \"NEC/Not Mentioned\" is not assigned to any state and is left out. Spreading it by population would raise every state by the same amount per resident and change none of the ranks.",
            "The CSR Explorer divides by the 2011 census, the last count taken, so its per-resident figures run higher than these for fast-growing states.",
            "The ministry records the state the company reported for each project. A company headquartered in Mumbai can report national work as Maharashtra's, so part of the gap measures where companies are based."],
        columns=["State", "MPI 2019-21", "CSR 2022-23 (₹ crore)", "Population, 1 Oct 2022", "CSR per resident"],
        rows=[[r["state"], f"{r['mpi']:.3f}", f"{r['crore']:,.1f}", f"{r['pop']:,}", f"₹{r['per_head']:,.1f}"]
              for r in table],
    )


def pct(x, d=1):
    return f"{x:.{d}f}%"


def undertrials_caste():
    d = json.loads((ROOT / "data" / "justice-explorer.json").read_text(encoding="utf-8"))
    # A state is used only where the prison table records caste for its undertrials
    # and the census population shares passed the explorer's cross-check. Both
    # sides of the national figure are pooled over the same states.
    used, left = [], []
    for s in d["states"]:
        c = s["caste"]
        if not c or any(v is None for v in c.values()) or s["sc_pct"] is None or s["st_pct"] is None:
            left.append(s["name"])
            continue
        used.append(s)
    pop = sum(s["population_2011"] for s in used)
    ut = sum(sum(s["caste"].values()) for s in used)
    sc_u = 100 * sum(s["caste"]["sc"] for s in used) / ut
    st_u = 100 * sum(s["caste"]["st"] for s in used) / ut
    sc_p = sum(s["population_2011"] * s["sc_pct"] for s in used) / pop
    st_p = sum(s["population_2011"] * s["st_pct"] for s in used) / pop
    want = ["Maharashtra", "Andhra Pradesh", "Telangana", "Ladakh"]
    if sorted(left) != sorted(want):
        fail(f"undertrials card: the states left out changed to {sorted(left)}; check why before publishing")

    MIN = 1000
    table = []
    for s in used:
        c = s["caste"]
        t = sum(c.values())
        u = 100 * (c["sc"] + c["st"]) / t
        p = s["sc_pct"] + s["st_pct"]
        table.append(dict(state=s["name"], ut=t, u=u, p=p, ratio=u / p))
    table.sort(key=lambda r: -r["ratio"])
    big = [r for r in table if r["ut"] >= MIN]
    hi, lo = big[0], big[-1]

    return dict(
        id="undertrials-caste",
        title="Undertrial prisoners by caste, against the population",
        tags=["undertrial prisoners", "NCRB", "prison statistics", "Scheduled Castes", "Scheduled Tribes", "criminal justice"],
        topic="Undertrial prisoners, 31 December 2023",
        headline=(f"Scheduled Castes and Tribes are {pct(sc_p + st_p)} of the population "
                  f"and {pct(sc_u + st_u)} of undertrial prisoners."),
        sub=(f"Scheduled Castes are {pct(sc_p)} of the population and {pct(sc_u)} of undertrials. "
             f"Scheduled Tribes are {pct(st_p)} and {pct(st_u)}."),
        pair=[dict(label="Share of undertrial prisoners", value=pct(sc_u + st_u, 0),
                   unit="Scheduled Castes and Tribes"),
              dict(label="Share of the population", value=pct(sc_p + st_p, 0),
                   unit="Scheduled Castes and Tribes")],
        chart=dict(title=f"SC and ST share of undertrials over their share of the population, states with {MIN:,}+ undertrials (1 means in proportion)",
                   bars=[[r["state"], round(r["ratio"], 2)] for r in big],
                   highlight=[hi["state"], lo["state"]],
                   axis=["Most over-represented", "Least"], prefix="", suffix="×", decimals=1),
        note=(f"An undertrial has not been convicted of the offence they are held for. Prisoners are counted "
              f"on 31 December 2023 and people in the 2011 census. {', '.join(sorted(left)[:-1])} and {sorted(left)[-1]} are left out "
              f"(see the working)."),
        sources=[
            dict(name="National Crime Records Bureau, Prison Statistics India 2023",
                 detail="State/UT-wise caste of undertrial prisoners as on 31-12-2023, Open Government Data Platform resource 6e069039-64bd-43da-8f5a-15cb697caf1b",
                 url="https://www.data.gov.in/"),
            dict(name="Census of India 2011, Scheduled Caste population by state",
                 detail="Open Government Data Platform resource c1c221ef-324a-4715-bc02-58172107c162",
                 url="https://www.data.gov.in/"),
            dict(name="Ministry of Tribal Affairs, State/UT-wise Scheduled Tribe population as per Census 2011",
                 detail="Open Government Data Platform resource a5cd7e55-2e13-4017-9f8c-410dad9cc518",
                 url="https://www.data.gov.in/")],
        page="/justice.html",
        page_label="Justice Explorer",
        table_title="Every state",
        method=[
            "A state's share is its Scheduled Caste and Scheduled Tribe undertrials divided by all its undertrials whose caste the prison recorded.",
            "The population share is the state's Scheduled Caste and Scheduled Tribe population in the 2011 census over its total population. The 2021 census was not held, so 2011 is the latest count.",
            "The national figures pool prisoners and people across the same states, so both sides cover the same places.",
            "Maharashtra reported no caste breakdown for its undertrials. Andhra Pradesh and Telangana are left out because the 2011 count covers the undivided state, and Ladakh because it was not a separate unit in 2011.",
            "Scheduled Tribe population is taken from the Ministry of Tribal Affairs table. The ST column of the combined census table on the same platform is scrambled across rows; the Justice Explorer explains how that was found.",
            f"The chart leaves out states with fewer than {MIN:,} undertrials whose caste was recorded, where a few dozen people move the ratio a long way. The table shows every state.",
            "Over-representation among undertrials can come from arrest, from charge, or from who can raise bail. These figures do not say which."],
        columns=["State", "Undertrials, caste recorded", "SC and ST share of undertrials", "SC and ST share of population, 2011", "Ratio"],
        rows=[[r["state"], f"{r['ut']:,.0f}", pct(r["u"]), pct(r["p"]), f"{r['ratio']:.2f}"] for r in table],
    )


def travel_by_sex():
    d = json.loads((ROOT / "data" / "nhts-india.json").read_text(encoding="utf-8"))
    w = d["workers_travelling"]
    i = w["ages"].index("15+")
    get = lambda sector, sex: w["rows"][sector][sex][i]
    cost = d["monthly_cost"]["workers"]
    men, women = get("Rural+Urban", "Male"), get("Rural+Urban", "Female")
    groups = [("Rural men", "Rural", "Male"), ("Rural women", "Rural", "Female"),
              ("Urban men", "Urban", "Male"), ("Urban women", "Urban", "Female")]
    for sector in ("Rural", "Urban", "Rural+Urban"):
        lo, hi = sorted((get(sector, "Male"), get(sector, "Female")))
        if not lo <= get(sector, "Person") <= hi:
            fail(f"travel card: the {sector} person figure is not between the male and female figures")
    src = d["_source"]
    return dict(
        id="travel-by-sex",
        title="How men and women get to work, from the National Household Travel Survey",
        tags=["travel survey", "NHTS", "commuting", "women's work", "female labour force", "transport"],
        topic="Getting to work, 2025-26",
        headline=(f"{pct(men)} of working men made a trip of a kilometre or more to work on the survey's travel day. "
                  f"For working women it was {pct(women)}."),
        sub=(f"Among workers with a fixed workplace, women spend {rupees(cost['Rural+Urban']['Female'])} a month "
             f"on the trip there and back. Men spend {rupees(cost['Rural+Urban']['Male'])}."),
        pair=[dict(label="Working men who travel to work", value=pct(men, 0), unit="aged 15 and over"),
              dict(label="Working women who travel to work", value=pct(women, 0), unit="aged 15 and over")],
        chart=dict(title="Workers aged 15+ who travel 1 km or more to work, %",
                   bars=[[name, get(sec, sex)] for name, sec, sex in groups],
                   highlight=["Rural women", "Urban women"],
                   axis=None, prefix="", suffix="%", decimals=1),
        note=("A worker who works at home or within a kilometre of it makes no trip the survey counts, "
              "so part of the gap is where women's work is."),
        sources=[dict(name=f"{src['publisher']}, {src['title']}",
                      detail="Table 3 (workers who travel, by sector, sex and age) and Figure 5 (monthly cost), released 5 October 2026",
                      url=src["url"])],
        page="/nhts.html",
        page_label="Travel Survey Explorer",
        table_title="By sector and sex",
        method=[
            "Workers are people aged 15 and over working in the week before the survey (current weekly status).",
            "A worker travels if they make a trip of 1 km or more to a fixed or non-fixed workplace on the travel day. Shorter trips were not recorded.",
            "The monthly cost covers trips to and from a fixed workplace only, so it leaves out workers whose place of work changes.",
            "The figures are the survey's own estimates for persons, transcribed from the press note's tables. The survey publishes no breakdown by sex for each state."],
        columns=["Sector", "Men who travel to work", "Women who travel to work", "Men, monthly cost", "Women, monthly cost"],
        rows=[[sec, pct(get(sec, "Male")), pct(get(sec, "Female")),
               rupees(cost[sec]["Male"]), rupees(cost[sec]["Female"])] for sec in ("Rural", "Urban", "Rural+Urban")],
    )


def obc_dates():
    d = json.loads((ROOT / "data" / "castes-india.json").read_text(encoding="utf-8"))
    obc = [r for r in d["obc"] if r["status"] == "Active"]
    dated = [r for r in obc if r["dated_year"] and r["file_year"]]
    first = [r for r in dated if r["dated_year"] == 1993]
    later = [r for r in dated if r["dated_year"] > 1993]
    moved = [r for r in later if r["file_year"] != r["dated_year"]]
    if any(r["file_year"] != 1993 for r in first):
        fail("OBC card: some 1993 entries carry another file year; the card's first sentence no longer holds")
    if len(first) + len(later) != len(dated):
        fail("OBC card: an entry is dated before 1993")
    gaps = sorted({abs(r["file_year"] - r["dated_year"]) for r in moved})
    per = {}
    for r in later:
        n, m = per.get(r["state"], (0, 0))
        per[r["state"]] = (n + 1, m + (r["file_year"] != r["dated_year"]))
    table = sorted(([s, n, m, 100 * m / n] for s, (n, m) in per.items()), key=lambda r: (-r[3], -r[1], r[0]))
    MIN = 20
    chart = [r for r in table if r[1] >= MIN]
    full = sorted(r[0] for r in chart if r[3] == 100)
    year = lambda y, kind: sum(1 for r in later if r[kind] == y)
    f98, d98 = year(1998, "file_year"), year(1998, "dated_year")
    return dict(
        id="obc-dates",
        title="Dates on the Central OBC list, file year against resolution date",
        tags=["OBC list", "Other Backward Classes", "NCBC", "caste", "gazette", "reservations"],
        topic="Central OBC list, 1993-2016",
        headline=(f"{len(moved)} of the {len(later):,} entries added to the Central OBC list after 1993 "
                  f"are filed under a different year from the date on their resolution."),
        sub=(f"The gazette file numbers put {f98} additions in 1998. "
             f"No entry's resolution is dated 1998."),
        pair=[dict(label="Added after 1993, with a printed date", value=f"{len(later):,}", unit="entries"),
              dict(label="Filed under another year", value=f"{len(moved)}", unit=f"{100 * len(moved) / len(later):.0f}% of them")],
        chart=dict(title=f"Share of post-1993 entries filed under another year, states with {MIN}+ such entries",
                   bars=[[r[0], round(r[3], 1)] for r in chart],
                   highlight=[chart[0][0], chart[-1][0]],
                   axis=["Most misdated", "Least"], prefix="", suffix="%", decimals=0),
        note=(f"The difference is {gaps[0]} to {gaps[-1]} years. All {len(first):,} entries in the first list "
              f"of 1993 carry 1993 in both places."),
        sources=[dict(name="Jolad, S. and Kalyani, G. (2026), Database of castes: SC, ST, OBC and 1931 Caste Census, Harvard Dataverse, V1.1",
                      short="Jolad and Kalyani, Database of castes (2026)",
                      detail="OBC list, with the gazette file number and the printed resolution date of every entry",
                      url=d["_source"]["doi"])],
        page="/castes.html",
        page_label="Caste Lists Explorer",
        table_title="Every state",
        method=[
            "The database records, for each entry, the year in its gazette file number (12011/14/2004-BCC is 2004) and the date printed on the resolution that added it.",
            f"An entry counts as filed under another year when the two years differ. {len([r for r in obc if not r['dated_year']])} active entries print no date and are left out.",
            "File 12011/14/2004-BCC, for example, carries a resolution dated 12 March 2007.",
            f"The chart leaves out states with fewer than {MIN} entries added after 1993. The table shows every state."
            + (f" Every later entry is filed under another year in {', '.join(full[:-1])} and {full[-1]}." if len(full) > 1 else ""),
            "A count of castes added each year is right only if it uses the resolution date. Analysis that reads the year off the file number moves the additions back by one to five years."],
        columns=["State", "Entries added after 1993", "Filed under another year", "Share"],
        rows=[[r[0], f"{r[1]:,}", f"{r[2]:,}", pct(r[3])] for r in table],
    )


CARDS = [csr_need, undertrials_caste, travel_by_sex, obc_dates]


# ---------------------------------------------------------------- output

def card_hash(c):
    shown = {k: c[k] for k in ("topic", "headline", "sub", "pair", "chart", "note", "sources")}
    shown["layout"] = 2  # bump when render.mjs changes how a card is drawn
    return hashlib.sha256(json.dumps(shown, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:8]


def shell():
    """Take the site-chrome links from csr.html, so their version stamps cannot drift."""
    src = (ROOT / "csr.html").read_text(encoding="utf-8")
    css = re.findall(r'<link rel="stylesheet" href="/css/(?:fonts|site-chrome)\.css\?v=[^"]+">', src)
    js = re.findall(r'<script src="/js/(?:translate-sarvam|site-chrome)\.js\?v=[^"]+" defer></script>', src)
    if len(css) != 2 or len(js) != 2:
        fail("could not read the site-chrome links from csr.html")
    return "\n".join(css), "\n".join(js)


STYLE = """<style>
:root{--bg:#F6F8FB;--panel:#FFFFFF;--ink:#0F172A;--mut:#5A6B82;--faint:#617087;--bd:#E4EAF1;--acc:#0369A1;--hi:#B45309}
html[data-theme="dark"]{--bg:#0B1120;--panel:#131C2E;--ink:#F1F5F9;--mut:#A8BACF;--faint:#94A3B8;--bd:#25314A;--acc:#38BDF8;--hi:#FBBF24}
@media(prefers-color-scheme:dark){html:not([data-theme]){--bg:#0B1120;--panel:#131C2E;--ink:#F1F5F9;--mut:#A8BACF;--faint:#94A3B8;--bd:#25314A;--acc:#38BDF8;--hi:#FBBF24}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;font-size:15px;line-height:1.6}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px 72px}
a{color:var(--acc)}
h1,h2{font-family:Amaranth,Georgia,serif;line-height:1.2;text-wrap:balance;margin:0}
header.top{padding:34px 0 8px}
.eyebrow{font-size:.74rem;letter-spacing:.11em;text-transform:uppercase;color:var(--faint);font-weight:700}
h1{font-size:clamp(1.85rem,4.6vw,2.7rem);margin:.35em 0 .3em}
.lede{color:var(--mut);max-width:64ch;font-size:1.03rem}
.card{background:var(--panel);border:1px solid var(--bd);border-radius:14px;padding:20px;margin:24px 0;display:grid;grid-template-columns:minmax(0,360px) minmax(0,1fr);gap:24px}
@media(max-width:760px){.card{grid-template-columns:minmax(0,1fr)}}
.card>div{min-width:0}
.card img{width:100%;height:auto;border-radius:10px;border:1px solid var(--bd)}
.card h2{font-size:1.25rem;margin:.2em 0 .4em}
.dl{display:inline-block;margin-top:10px;font-size:.87rem;font-weight:600}
.body p,.body li{color:var(--mut);font-size:.92rem}
.body h3{font-size:.8rem;letter-spacing:.07em;text-transform:uppercase;color:var(--faint);margin:16px 0 4px}
.scroll{overflow-x:auto;border:1px solid var(--bd);border-radius:10px;margin-top:8px}
table{border-collapse:collapse;width:100%;font-size:.84rem}
th,td{text-align:left;padding:6px 10px;border-bottom:1px solid var(--bd);white-space:nowrap}
th{font-size:.72rem;letter-spacing:.05em;text-transform:uppercase;color:var(--faint)}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}
tr.hi td{color:var(--hi);font-weight:700}
.src li{margin-bottom:.4em}
</style>"""


def keep(s):
    """Escape, and keep a year range such as 2022-23 on one line."""
    return re.sub(r"(\d{4}-\d{2})", r'<span style="white-space:nowrap">\1</span>', E(s))


def page(cards):
    css, js = shell()
    parts = []
    for c in cards:
        img = f"/{IMG_DIR}/{c['id']}-{c['hash']}.png"
        num = ' class="n"'
        head = "".join(f"<th{num if i else ''}>{E(h)}</th>" for i, h in enumerate(c["columns"]))
        body = []
        for r in c["rows"]:
            cls = ' class="hi"' if r[0] in c["chart"]["highlight"] else ""
            body.append(f"<tr{cls}>" + "".join(
                f"<td{num if i else ''}>{E(v)}</td>" for i, v in enumerate(r)) + "</tr>")
        srcs = "".join(f'<li><a href="{E(s["url"])}" rel="noopener">{E(s["name"])}</a>, {E(s["detail"])}.</li>'
                       for s in c["sources"])
        meth = "".join(f"<li>{E(m)}</li>" for m in c["method"])
        parts.append(f"""
<section class="card" id="{c['id']}">
  <div><img src="{img}" alt="{E(c['headline'] + ' ' + c['sub'])}" width="1080" height="1350" loading="lazy">
  <a class="dl" href="{img}" download>Download the card</a></div>
  <div class="body">
    <div class="eyebrow">{E(c['topic'])}</div>
    <h2>{keep(c['headline'])}</h2>
    <p>{keep(c['sub'])}</p>
    <h3>How it is worked out</h3>
    <ul>{meth}</ul>
    <h3>{E(c['table_title'])}</h3>
    <div class="scroll" tabindex="0" role="region" aria-label="{E(c['topic'])}, {E(c['table_title'].lower())}"><table><thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table></div>
    <h3>Sources</h3>
    <ul class="src">{srcs}</ul>
    <p>More in the <a href="{E(c['page'])}">{E(c['page_label'])}</a>.</p>
  </div>
</section>""")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>By the numbers | ImpactMojo</title>
<meta name="description" content="One figure at a time from India's development data, each computed from public sources with the working and every source shown.">
<!-- share:start -->
<!-- share:end -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Amaranth:wght@400;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link href="/assets/images/favicon.png" rel="icon" type="image/png">
{STYLE}
{css}
</head>
<body>
<div class="wrap">
<header class="top">
  <div class="eyebrow">{SERIES}</div>
  <h1>One number, and how we got it</h1>
  <p class="lede">Each card here takes one figure from India's public data and sets it beside another. Every figure is
  computed from the sources listed under it, and the table shows the working for every state, so you can check it
  or use it.</p>
</header>
{''.join(parts)}
</div>
{js}
</body>
</html>
"""


def data_room(cards, text):
    """The By the numbers group on the Data Room page, one card per figure."""
    if EX_START not in text or EX_END not in text:
        fail("explorers.html has no by-the-numbers markers")
    items = "".join(f"""
      <a class="card" href="/by-the-numbers/#{c['id']}" style="--sc:#B45309">
        <span class="csrc">{E(c['topic'])} · {E('; '.join(s.get('short') or s['name'].split(',')[0] for s in c['sources']))}</span>
        <span class="cn">{E(c['title'])}</span>
        <span class="cd">{keep(c['headline'])}</span>
        <span class="cgo">See the working →</span>
      </a>""" for c in cards)
    block = f"""{EX_START}
  <section class="group" id="by-the-numbers">
    <div class="group-head">
      <span class="gk">Cards</span><h2><a href="/by-the-numbers/">By the numbers: one figure at a time</a></h2><span class="gn">{len(cards)} cards</span>
    </div>
    <div class="grid">{items}
    </div>
  </section>
  {EX_END}"""
    head, rest = text.split(EX_START, 1)
    return head + block + rest.split(EX_END, 1)[1]


def search_rows(cards, raw):
    """One site-search row per card, after the page's own row. Rows are rewritten each build."""
    rows = json.loads(raw)
    rows = [r for r in rows if not str(r.get("id", "")).startswith("by-the-numbers-")]
    at = next((i for i, r in enumerate(rows) if r.get("id") == "by-the-numbers"), None)
    if at is None:
        fail("data/search-index.json has no by-the-numbers row")
    new = [dict(id=f"by-the-numbers-{c['id']}", title=f"{c['title']} (By the numbers)",
                description=f"{c['headline']} {c['sub']}", type="explorer", category="Data Room",
                url=f"/by-the-numbers/#{c['id']}", tags=c["tags"] + ["by the numbers", "data cards", "India"])
           for c in cards]
    rows[at + 1:at + 1] = new
    return json.dumps(rows, indent=2, ensure_ascii=False) + ("\n" if raw.endswith("\n") else "")


def share():
    spec = importlib.util.spec_from_file_location("build_social_tags", ROOT / "scripts" / "build-social-tags.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def build():
    cards = []
    for fn in CARDS:
        c = fn()
        c["hash"] = card_hash(c)
        c["image"] = f"{IMG_DIR}/{c['id']}-{c['hash']}.png"
        c["series"] = SERIES
        cards.append(c)
    want = json.loads(COUNTS.read_text(encoding="utf-8")).get("by-the-numbers")
    if want != len(cards):
        fail(f"data/counts.json says {want} By the numbers cards and there are {len(cards)}; "
             "change the count there, then run python3 scripts/check-counts.py")
    manifest = json.dumps(cards, indent=1, ensure_ascii=False) + "\n"
    out = share().apply("by-the-numbers/index.html", page(cards))
    ex = data_room(cards, EXPLORERS.read_text(encoding="utf-8"))
    search = search_rows(cards, SEARCH.read_text(encoding="utf-8"))
    return cards, manifest, out, ex, search


def main():
    cards, manifest, out, ex, search = build()
    if "--check" in sys.argv:
        stale = [p for p, new in ((MANIFEST, manifest), (PAGE, out), (EXPLORERS, ex), (SEARCH, search))
                 if not p.exists() or p.read_text(encoding="utf-8") != new]
        if stale:
            fail("stale: " + ", ".join(str(p.relative_to(ROOT)) for p in stale)
                 + ". Run python3 scripts/by-the-numbers/build.py")
        missing = [c["image"] for c in cards if not (ROOT / c["image"]).exists()]
        if missing:
            fail("card images not drawn: " + ", ".join(missing) + ". Run node scripts/by-the-numbers/render.mjs")
        print(f"PASS - {len(cards)} card(s), page and images current")
        return
    DATA.mkdir(parents=True, exist_ok=True)
    PAGE.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(manifest, encoding="utf-8")
    PAGE.write_text(out, encoding="utf-8")
    EXPLORERS.write_text(ex, encoding="utf-8")
    SEARCH.write_text(search, encoding="utf-8")
    for c in cards:
        print(f"{c['id']}: {c['headline']}")
    print(f"wrote {PAGE.relative_to(ROOT)} and {MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
