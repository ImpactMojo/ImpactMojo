#!/usr/bin/env python3
"""Write DeepDives/womens-work-india.html from page.template.html and
data/deep-dives/womens-work.json. Every number in the text and every chart is
filled from the data. --check fails if the page on disk is stale.

    python3 scripts/womens-work/build_page.py
    python3 scripts/womens-work/build_page.py --check
"""
import json, re, sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "deep-dives" / "womens-work.json"
TPL = Path(__file__).with_name("page.template.html")
OUT = ROOT / "DeepDives" / "womens-work-india.html"
REL = "DeepDives/womens-work-india.html"

D = json.loads(DATA.read_text())
A, B = D["rounds"]
GA, GB = A["groups"], B["groups"]
TYPES = [("helper", "Unpaid helper in a family enterprise", "t1"), ("own", "Own-account work", "t2"),
         ("regular", "Regular wage or salary", "t3"), ("casual", "Casual labour", "t4"), ("employer", "Employer", "t5")]
MIN_N = 2500  # women 15+ in the sample, both years, for a state to be shown


def f1(x):
    return f"{x:.1f}"


def pct(x):
    return f"{x:.1f}%"


N = {}
for key, g in (("a", GA), ("b", GB)):
    for grp, short in (("all_women", "w"), ("rural_women", "rw"), ("urban_women", "uw"), ("all_men", "m")):
        for fld in ("lfpr", "wpr", "helper", "own", "regular", "casual", "subsidiary_only", "agri", "nonagri"):
            N[f"{fld}_{short}_{key}"] = f1(g[grp][fld])
w_rise = GB["all_women"]["wpr"] - GA["all_women"]["wpr"]
ho_rise = (GB["all_women"]["helper"] + GB["all_women"]["own"]) - (GA["all_women"]["helper"] + GA["all_women"]["own"])
ag_rise = GB["all_women"]["agri"] - GA["all_women"]["agri"]
reg_rise = GB["all_women"]["regular"] - GA["all_women"]["regular"]
sub_rise = GB["all_women"]["subsidiary_only"] - GA["all_women"]["subsidiary_only"]
N.update(w_rise=f1(w_rise), ho_rise=f1(ho_rise), ho_share=str(round(100 * ho_rise / w_rise)),
         ag_rise=f1(ag_rise), ag_share=str(round(100 * ag_rise / w_rise)), reg_rise=f1(reg_rise),
         sub_rise=f1(sub_rise), sub_share=str(round(100 * sub_rise / w_rise)))
for key, g in (("a", GA), ("b", GB)):
    for grp, short in (("all_women", "w"), ("all_men", "m")):
        N[f"subsh_{short}_{key}"] = f1(100 * g[grp]["subsidiary_only"] / g[grp]["wpr"])
N["n_a"] = f"{A['n_15plus']:,}"
N["n_b"] = f"{B['n_15plus']:,}"

SA, SB = A["states_women"], B["states_women"]
STATES = [s for s in SA if SA[s]["n"] >= MIN_N and SB[s]["n"] >= MIN_N]
DROPPED = [s for s in SA if s not in STATES]
N["n_states"] = str(len(STATES))
N["dropped_states"] = " and ".join(DROPPED) if len(DROPPED) <= 2 else ", ".join(DROPPED[:-1]) + " and " + DROPPED[-1]
N["min_n"] = f"{MIN_N:,}"


def st_share(s):
    r = SB[s]["wpr"] - SA[s]["wpr"]
    return (SB[s]["helper_own"] - SA[s]["helper_own"]) / r if r > 0 else None


for key, s in (("as", "Assam"), ("bi", "Bihar"), ("ke", "Kerala"), ("up", "Uttar Pradesh"), ("ap", "Andhra Pradesh"), ("mp", "Madhya Pradesh")):
    N[f"{key}_a"] = f1(SA[s]["wpr"]); N[f"{key}_b"] = f1(SB[s]["wpr"])
    sh = st_share(s)
    N[f"{key}_sh"] = str(round(100 * sh)) if sh is not None else "n/a"


def svg(w, h, ids, body):
    (tid, title), (did, desc) = ids
    return (f'<svg class="whc" viewBox="0 0 {w} {h}" role="img" aria-labelledby="{tid} {did}">'
            f'<title id="{tid}">{escape(title)}</title><desc id="{did}">{escape(desc)}</desc>{body}</svg>')


def t(x, y, s, cls="lab", anchor="start"):
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}">{escape(s)}</text>'


def stacked(rows, maxv, ids, keys, legend):
    W_, L, R, rh = 680, 150, 70, 40
    H_ = 16 + rh * len(rows) + 26
    x = lambda v: L + v / maxv * (W_ - L - R)
    b = []
    for v in range(0, int(maxv) + 1, 10):
        b.append(f'<line x1="{x(v):.1f}" x2="{x(v):.1f}" y1="8" y2="{H_ - 22}" class="grid"/>')
        b.append(t(x(v), H_ - 6, f"{v}%", "tick", "middle"))
    for i, (lab, segs) in enumerate(rows):
        yy = 12 + i * rh
        b.append(t(L - 10, yy + 19, lab, "rlab", "end"))
        x0 = 0
        for v, cl in segs:
            b.append(f'<rect x="{x(x0):.1f}" y="{yy + 4}" width="{max(x(x0 + v) - x(x0), 0):.1f}" height="{rh - 12}" class="bar {cl}"/>')
            x0 += v
        b.append(t(x(x0) + 6, yy + 20, f"{x0:.1f}%", "val"))
    leg = "".join(f'<span class="key {cl}">{escape(n)}</span>' for n, cl in legend)
    return svg(W_, H_, ids, "".join(b)) + f'<div class="wh-legend">{leg}</div>'


def chart_types():
    rows = [(y, [(g["all_women"][k], cl) for k, _, cl in TYPES]) for y, g in (("2017-18", GA), ("2023-24", GB))]
    desc = "; ".join(f"{y}: " + ", ".join(f"{n.lower()} {g['all_women'][k]:.1f}%" for k, n, _ in TYPES)
                     for y, g in (("2017-18", GA), ("2023-24", GB)))
    return stacked(rows, 50, (("c1t", "Women aged 15 and over who work, by kind of work, as a share of all women 15+"), ("c1d", desc)),
                   TYPES, [(n, cl) for _, n, cl in TYPES])


def chart_farm():
    rows = []
    for lab, grp in (("All India", "all_women"), ("Rural", "rural_women"), ("Urban", "urban_women")):
        for y, g in (("2017-18", GA), ("2023-24", GB)):
            rows.append((f"{lab}, {y}", [(g[grp]["agri"], "t1"), (round(g[grp]["wpr"] - g[grp]["agri"], 1), "t3")]))
    desc = "; ".join(f"{lab} {v[0][0]:.1f}% in agriculture, {v[1][0]:.1f}% outside it" for lab, v in rows)
    return stacked(rows, 50, (("c2t", "Women aged 15 and over who work, in agriculture and outside it"), ("c2d", desc)),
                   None, [("Agriculture, forestry and fishing", "t1"), ("Every other industry", "t3")])


def chart_sub():
    rows = []
    for lab, grp in (("Women", "w"), ("Men", "m")):
        for y, k in (("2017-18", "a"), ("2023-24", "b")):
            rows.append((f"{lab}, {y}", [(float(N[f'subsh_{grp}_{k}']), "t2" if grp == "w" else "t4")]))
    desc = "; ".join(f"{lab}: {v[0][0]:.1f}%" for lab, v in rows)
    return stacked(rows, 30, (("c4t", "Of workers aged 15 and over, the share counted as working only through a subsidiary activity"), ("c4d", desc)),
                   None, [("Women", "t2"), ("Men", "t4")])


def chart_states():
    rows = sorted(STATES, key=lambda s: SB[s]["wpr"], reverse=True)
    W_, L, R, rh, T = 680, 150, 110, 24, 40
    H_ = T + rh * len(rows) + 28
    x = lambda v: L + v / 70 * (W_ - L - R)
    b = [t(W_ - 6, 14, "rise | part from unpaid", "tick", "end"), t(W_ - 6, 28, "and own-account work", "tick", "end")]
    for v in range(0, 71, 10):
        b.append(f'<line x1="{x(v):.1f}" x2="{x(v):.1f}" y1="{T - 4}" y2="{H_ - 24}" class="grid"/>')
        b.append(t(x(v), H_ - 8, f"{v}%", "tick", "middle"))
    for i, s in enumerate(rows):
        yy = T + i * rh + rh / 2
        a, z = SA[s]["wpr"], SB[s]["wpr"]
        b.append(t(L - 10, yy + 4, s, "rlab", "end"))
        b.append(f'<line x1="{x(a):.1f}" x2="{x(z):.1f}" y1="{yy:.1f}" y2="{yy:.1f}" class="link"/>')
        b.append(f'<circle cx="{x(a):.1f}" cy="{yy:.1f}" r="4.5" class="dot lo"/>')
        b.append(f'<circle cx="{x(z):.1f}" cy="{yy:.1f}" r="5" class="dot hi"/>')
        b.append(t(W_ - 6, yy + 4, f"+{z - a:.1f} | +{SB[s]['helper_own'] - SA[s]['helper_own']:.1f}", "val", "end"))
    desc = "; ".join(f"{s} {SA[s]['wpr']:.1f}% to {SB[s]['wpr']:.1f}%" for s in rows)
    leg = '<span class="key lo">2017-18</span><span class="key hi">2023-24</span>'
    return svg(W_, H_, (("c3t", "Share of women aged 15 and over who work, by state, 2017-18 and 2023-24"), ("c3d", desc)), "".join(b)) + f'<div class="wh-legend">{leg}</div>'


CHARTS = {"chart_types": chart_types, "chart_farm": chart_farm, "chart_states": chart_states, "chart_sub": chart_sub}


def _share():
    import importlib.util as _u
    sp = _u.spec_from_file_location("build_social_tags", ROOT / "scripts" / "build-social-tags.py")
    m = _u.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


def render():
    s = TPL.read_text()
    for k, fn in CHARTS.items():
        s = s.replace("{{" + k + "}}", fn())

    def sub(m):
        k = m.group(1)
        if k not in N:
            sys.exit(f"FAIL - template asks for {{{{{k}}}}}, which the data does not provide")
        return N[k]
    s = re.sub(r"\{\{([a-z0-9_]+)\}\}", sub, s)
    return _share().apply(REL, s)


if __name__ == "__main__":
    out = render()
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text() != out:
            sys.exit(f"FAIL - {REL} is stale. Run python3 scripts/womens-work/build_page.py")
        print("PASS - womens-work-india.html matches data/deep-dives/womens-work.json")
    else:
        OUT.write_text(out)
        print("wrote", REL)
        if "--keys" in sys.argv:
            for k, v in sorted(N.items()):
                print(k, "=", v)
