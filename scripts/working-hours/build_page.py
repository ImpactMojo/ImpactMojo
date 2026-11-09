#!/usr/bin/env python3
"""Write DeepDives/indian-working-hours.html from its template and the
aggregates in data/deep-dives/working-hours.json.

Every number in the page text is filled from the data ({{key}} in the
template), and every chart is drawn here as inline SVG, so the prose, the
charts and the data cannot drift apart. --check fails if the page on disk is
not what this script would write.

    python3 scripts/working-hours/build_page.py
    python3 scripts/working-hours/build_page.py --check
"""
import json, re, sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "deep-dives" / "working-hours.json"
TPL = Path(__file__).with_name("page.template.html")
OUT = ROOT / "DeepDives" / "indian-working-hours.html"

D = json.loads(DATA.read_text())
G = {(g["type"], g["sex"]): g for g in D["groups"]}
C = {(g["type"], g["sex"]): g for g in D["clock"]["groups"]}
I = {r["iso3"]: r for r in D["international"]["rows"]}
TYPES4 = ["Salaried, private", "Salaried, government", "Self-employed", "Casual labour"]
TYPES3 = ["Salaried", "Self-employed", "Casual labour"]
CLS = {"Salaried, private": "s1", "Salaried, government": "s2", "Self-employed": "s3", "Casual labour": "s4",
       "Salaried": "s1"}
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def pct(x):
    return f"{round(100 * x):d}%"


def clock(m):
    h, mi = divmod(int(m) % 1440, 60)
    ap = "am" if h < 12 else "pm"
    h12 = h % 12 or 12
    return f"{h12}:{mi:02d} {ap}" if mi else f"{h12} {ap}"


def h1(x):
    return f"{x:.1f}"


# ---------- numbers used in the prose ----------
N = {}
for t in TYPES4:
    for s in ("Men", "Women"):
        c = C[(t, s)]
        k = {"Salaried, private": "priv", "Salaried, government": "gov", "Self-employed": "self", "Casual labour": "cas"}[t] + ("_m" if s == "Men" else "_w")
        N[f"at5_{k}"] = pct(c["at_work"][26])          # slot 26 starts 17:00
        N[f"at8_{k}"] = pct(c["at_work"][32])          # 20:00
        N[f"end_{k}"] = clock(c["end_median_min"])
        N[f"past7_{k}"] = pct(c["past_19"])
        N[f"paid_{k}"] = h1(c["paid_h"])
        N[f"unpaid_{k}"] = h1(c["unpaid_h"])
        N[f"total_{k}"] = h1(c["paid_h"] + c["unpaid_h"])
for t in TYPES3:
    for s in ("Men", "Women"):
        g = G[(t, s)]
        k = {"Salaried": "sal", "Self-employed": "self", "Casual labour": "cas"}[t] + ("_m" if s == "Men" else "_w")
        N[f"sun_{k}"] = pct(g["any_paid_by_dow"][6])
        N[f"wed_{k}"] = pct(g["any_paid_by_dow"][2])
        N[f"week_{k}"] = h1(g["weekly_paid_h"])
        N[f"share_{k}"] = pct(g["workers_share"])
N["nonsal_share"] = pct(sum(g["workers_share"] for g in D["groups"] if g["type"] != "Salaried"))
N["sal_share"] = pct(sum(g["workers_share"] for g in D["groups"] if g["type"] == "Salaried"))
W = D["all_workers_weekly_paid_h"]
N.update(week_all=h1(W["All"]), week_men=h1(W["Men"]), week_women=h1(W["Women"]))
N["n_diaries"] = f"{sum(g['n'] for g in D['groups']):,}"
for iso, k in (("IND", "ind"), ("NLD", "nld"), ("DEU", "deu"), ("USA", "usa"), ("BGD", "bgd"), ("PAK", "pak")):
    r = I[iso]
    N[f"h_{k}"] = h1(r["weekly_hours"]); N[f"p_{k}"] = h1(r["output_per_hour"]); N[f"y_{k}"] = str(r["year"])
N["nld_x"] = f"{I['NLD']['output_per_hour'] / I['IND']['output_per_hour']:.1f}"
N["ilo_n"] = str(len(I))


# ---------- charts ----------
def svg(w, h, title, desc, body, cls="whc"):
    return (f'<svg class="{cls}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="{title[0]} {desc[0]}">'
            f'<title id="{title[0]}">{escape(title[1])}</title><desc id="{desc[0]}">{escape(desc[1])}</desc>{body}</svg>')


def t(x, y, s, cls="lab", anchor="start", extra=""):
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}"{extra}>{escape(s)}</text>'


def chart_clock():
    W_, H_, L, R, T, B = 340, 250, 44, 12, 26, 34
    pw, ph = W_ - L - R, H_ - T - B
    k0, k1 = 4, 40                                     # 06:00 .. 24:00
    x = lambda k: L + (k - k0) / (k1 - k0) * pw
    y = lambda v: T + (1 - v) * ph
    panels = []
    for si, s in enumerate(("Men", "Women")):
        b = [t(L, 14, f"{s}", "ptitle")]
        for v in (0, .25, .5, .75, 1):
            b.append(f'<line x1="{L}" x2="{L + pw}" y1="{y(v):.1f}" y2="{y(v):.1f}" class="grid"/>')
            b.append(t(L - 6, y(v) + 4, pct(v), "tick", "end"))
        for k, lbl in ((4, "6am"), (16, "noon"), (26, "5pm"), (36, "10pm")):
            b.append(t(x(k), T + ph + 18, lbl, "tick", "middle"))
        b.append(f'<line x1="{x(26):.1f}" x2="{x(26):.1f}" y1="{T}" y2="{T + ph}" class="five"/>')
        for ty in TYPES4:
            v = C[(ty, s)]["at_work"]
            pts = " ".join(f"{x(k):.1f},{y(v[k]):.1f}" for k in range(k0, k1 + 1))
            b.append(f'<polyline points="{pts}" class="ln {CLS[ty]}"/>')
        panels.append(f'<g transform="translate({si * (W_ + 8)},0)">{"".join(b)}</g>')
    leg = "".join(f'<span class="key {CLS[ty]}">{escape(ty)}</span>' for ty in TYPES4)
    desc = "; ".join(f"{ty} {s.lower()}: {pct(C[(ty, s)]['at_work'][26])} at 5 pm" for s in ("Men", "Women") for ty in TYPES4)
    return (svg(2 * W_ + 8, H_, ("c1t", "Share of workers doing paid work, half hour by half hour, on a working day"),
                ("c1d", desc), "".join(panels)) + f'<div class="wh-legend">{leg}</div>')


def chart_week():
    W_, H_, L, R, T, B = 220, 200, 40, 10, 26, 30
    pw, ph = W_ - L - R, H_ - T - B
    x = lambda i: L + i / 6 * pw
    y = lambda v: T + (1 - v) * ph
    panels = []
    for pi, ty in enumerate(TYPES3):
        b = [t(L, 14, ty, "ptitle")]
        for v in (0, .5, 1):
            b.append(f'<line x1="{L}" x2="{L + pw}" y1="{y(v):.1f}" y2="{y(v):.1f}" class="grid"/>')
            b.append(t(L - 6, y(v) + 4, pct(v), "tick", "end"))
        b.append(f'<rect x="{x(5.5):.1f}" y="{T}" width="{x(6) - x(5.5) + 8:.1f}" height="{ph}" class="sun"/>')
        for i, dname in enumerate(DAYS):
            b.append(t(x(i), T + ph + 18, dname[0] if dname != "Sun" else "Sun", "tick", "middle"))
        for s, cl in (("Men", "m"), ("Women", "w")):
            v = G[(ty, s)]["any_paid_by_dow"]
            pts = " ".join(f"{x(i):.1f},{y(v[i]):.1f}" for i in range(7))
            b.append(f'<polyline points="{pts}" class="ln {cl}"/>')
            b.append(f'<circle cx="{x(6):.1f}" cy="{y(v[6]):.1f}" r="3.5" class="dot {cl}"/>')
            b.append(t(x(6) - 6, y(v[6]) + (14 if s == "Women" else -12), pct(v[6]), f"val {cl}", "end"))
        panels.append(f'<g transform="translate({pi * (W_ + 6)},0)">{"".join(b)}</g>')
    desc = "; ".join(f"{ty}: men {pct(G[(ty, 'Men')]['any_paid_by_dow'][6])}, women {pct(G[(ty, 'Women')]['any_paid_by_dow'][6])} on Sunday" for ty in TYPES3)
    leg = '<span class="key m">Men</span><span class="key w">Women</span>'
    return svg(3 * W_ + 12, H_, ("c2t", "Share of workers who did any paid work, by day of the week"), ("c2d", desc), "".join(panels)) + f'<div class="wh-legend">{leg}</div>'


def hbars(rows, maxv, ref, ids, unit, fmt):
    W_, L, R, rh = 680, 200, 60, 30
    H_ = 20 + rh * len(rows) + 24
    x = lambda v: L + v / maxv * (W_ - L - R)
    b = []
    for i, (lab, segs) in enumerate(rows):
        yy = 14 + i * rh
        b.append(t(L - 10, yy + 15, lab, "rlab", "end"))
        x0 = 0
        for v, cl in segs:
            b.append(f'<rect x="{x(x0):.1f}" y="{yy + 4}" width="{x(x0 + v) - x(x0):.1f}" height="{rh - 10}" class="bar {cl}"/>')
            x0 += v
        b.append(t(x(x0) + 6, yy + 15, fmt(x0, segs), "val"))
    if ref:
        b.append(f'<line x1="{x(ref[0]):.1f}" x2="{x(ref[0]):.1f}" y1="6" y2="{H_ - 20}" class="five"/>')
        b.append(t(x(ref[0]), H_ - 6, ref[1], "tick", "middle"))
    return svg(W_, H_, ids[0], ids[1], "".join(b))


def chart_hours():
    rows = []
    for ty in TYPES3:
        for s in ("Men", "Women"):
            g = G[(ty, s)]
            rows.append((f"{ty}, {s.lower()}", [(g["weekly_paid_h"], "m" if s == "Men" else "w")]))
    desc = "; ".join(f"{lab}: {segs[0][0]:.1f} hours" for lab, segs in rows)
    return hbars(rows, 56, (48, "48-hour weekly limit"), (("c3t", "Estimated paid hours a week, by kind of work"), ("c3d", desc)),
                 "h", lambda v, s: f"{v:.1f} h") + '<div class="wh-legend"><span class="key m">Men</span><span class="key w">Women</span></div>'


def chart_total():
    rows = []
    for ty in TYPES4:
        for s in ("Men", "Women"):
            c = C[(ty, s)]
            rows.append((f"{ty}, {s.lower()}", [(c["paid_h"], "pd"), (c["unpaid_h"], "up")]))
    desc = "; ".join(f"{lab}: {segs[0][0]:.1f} paid plus {segs[1][0]:.1f} unpaid hours" for lab, segs in rows)
    out = hbars(rows, 11, None, (("c5t", "Hours of paid and unpaid work on a working day"), ("c5d", desc)), "h",
                lambda v, s: f"{v:.1f} h")
    return out + '<div class="wh-legend"><span class="key pd">Paid work</span><span class="key up">Unpaid housework and care</span></div>'


def chart_scatter():
    W_, H_, L, R, T, B = 680, 360, 54, 20, 16, 44
    pw, ph = W_ - L - R, H_ - T - B
    x = lambda h: L + (h - 28) / (50 - 28) * pw
    y = lambda p: T + (1 - p / 100) * ph
    b = []
    for p in (0, 25, 50, 75, 100):
        b.append(f'<line x1="{L}" x2="{L + pw}" y1="{y(p):.1f}" y2="{y(p):.1f}" class="grid"/>')
        b.append(t(L - 6, y(p) + 4, f"${p}", "tick", "end"))
    for h in (30, 35, 40, 45, 50):
        b.append(t(x(h), T + ph + 18, f"{h} h", "tick", "middle"))
    b.append(t(L + pw / 2, H_ - 4, "Average weekly hours actually worked", "tick", "middle"))
    b.append(t(12, T + ph / 2, "Output per hour (2021 PPP $)", "tick", "middle", f' transform="rotate(-90 12 {T + ph / 2:.1f})"'))
    off = {"IND": (8, -10), "NLD": (8, 4), "PAK": (8, -4), "BGD": (8, 14), "LKA": (8, 6), "THA": (-8, 2), "ZAF": (8, -6),
           "MEX": (-8, -6), "TUR": (8, 4), "VNM": (-8, -8), "PHL": (-8, 14), "BRA": (-8, -8), "KOR": (8, 4), "IDN": (-8, 14),
           "USA": (8, 4), "FRA": (8, 12), "GBR": (8, 4), "DEU": (-8, -8)}
    for r in D["international"]["rows"]:
        cx, cy = x(r["weekly_hours"]), y(r["output_per_hour"])
        hi = r["iso3"] in ("IND", "NLD")
        b.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{6 if hi else 4.5}" class="dot {"hi" if hi else "lo"}"/>')
        dx, dy = off.get(r["iso3"], (8, 4))
        b.append(t(cx + dx, cy + dy, r["country"], "val" if hi else "tick", "start" if dx > 0 else "end"))
    desc = "; ".join(f"{r['country']} {r['year']}: {r['weekly_hours']} hours, ${r['output_per_hour']} per hour" for r in D["international"]["rows"])
    return svg(W_, H_, ("c4t", "Weekly hours worked against output per hour worked, by country"), ("c4d", desc), "".join(b))


CHARTS = {"chart_clock": chart_clock, "chart_week": chart_week, "chart_hours": chart_hours,
          "chart_scatter": chart_scatter, "chart_total": chart_total}


def render():
    s = TPL.read_text()
    for k, f in CHARTS.items():
        s = s.replace("{{" + k + "}}", f())
    def sub(m):
        k = m.group(1)
        if k not in N:
            sys.exit(f"FAIL - template asks for {{{{{k}}}}}, which the data does not provide")
        return N[k]
    s = re.sub(r"\{\{([a-z0-9_]+)\}\}", sub, s)
    return _share().apply("DeepDives/indian-working-hours.html", s)


def _share():
    # The share-tag pass every page generator applies (build-social-tags.py).
    import importlib.util as _u
    sp = _u.spec_from_file_location("build_social_tags", ROOT / "scripts" / "build-social-tags.py")
    m = _u.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


if __name__ == "__main__":
    out = render()
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text() != out:
            sys.exit("FAIL - DeepDives/indian-working-hours.html is stale. Run python3 scripts/working-hours/build_page.py")
        print("PASS - indian-working-hours.html matches data/deep-dives/working-hours.json")
    else:
        OUT.write_text(out)
        print("wrote", OUT.relative_to(ROOT))
        if "--keys" in sys.argv:
            for k, v in sorted(N.items()):
                print(k, "=", v)
