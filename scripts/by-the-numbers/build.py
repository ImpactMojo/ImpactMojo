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
working) and data/by-the-numbers/cards.json (what render.mjs draws). Each
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
                   highlight=["Bihar", "Maharashtra"]),
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


CARDS = [csr_need]


# ---------------------------------------------------------------- output

def card_hash(c):
    shown = {k: c[k] for k in ("topic", "headline", "sub", "pair", "chart", "note", "sources")}
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
    <h3>Every state</h3>
    <div class="scroll" tabindex="0" role="region" aria-label="{E(c['topic'])}, every state"><table><thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table></div>
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
    manifest = json.dumps(cards, indent=1, ensure_ascii=False) + "\n"
    out = share().apply("by-the-numbers/index.html", page(cards))
    return cards, manifest, out


def main():
    cards, manifest, out = build()
    if "--check" in sys.argv:
        stale = [p for p, new in ((MANIFEST, manifest), (PAGE, out))
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
    for c in cards:
        print(f"{c['id']}: {c['headline']}")
    print(f"wrote {PAGE.relative_to(ROOT)} and {MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
