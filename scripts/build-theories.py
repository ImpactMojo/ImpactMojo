#!/usr/bin/env python3
"""Build the Theories of Development library from data/theories/.

Why this exists
---------------
The library keeps its content in one JSON file per theory under
`data/theories/`, and ships three things derived from them: the browser data
file `js/theories-data.js`, one static page per theory under `theories/`, and
the catalogue page `theories/index.html`.

Deriving them is the point. A causal diagram is a graph, and a hand-maintained
graph rots in a specific way: an edge keeps pointing at a node that was renamed,
and the renderer silently drops the edge rather than erroring, so the diagram
goes on looking fine while an arrow the argument depends on is missing. The same
is true of the compare/contrast pairing, which is a link between two files that
nothing checks. Both are validated here and both refuse to build.

Static pages rather than one page with a query string, because the repo's
search-coverage and sitemap guards work on paths, and a `?t=` page is a single
path however many theories it holds.

Run:  python3 scripts/build-theories.py
CI:   python3 scripts/build-theories.py --check
"""

import datetime
import hashlib
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "theories"
OUT_JS = ROOT / "js" / "theories-data.js"
OUT_DIR = ROOT / "theories"

AXIS_MIN, AXIS_MAX = -3.0, 3.0
REQUIRED = ["id", "name", "short", "thinkers", "year", "years_label", "era",
            "tradition", "topics", "claim", "summary", "axes", "axis_notes",
            "layers", "evidence", "unsettled", "india", "compare", "contrast",
            "compare_note", "contrast_note", "reading"]


def load():
    meta = json.loads((SRC / "_meta.json").read_text(encoding="utf-8"))
    theories = []
    for path in sorted(SRC.glob("*.json")):
        if path.name == "_meta.json":
            continue
        t = json.loads(path.read_text(encoding="utf-8"))
        t["_file"] = path.name
        theories.append(t)
    theories.sort(key=lambda t: (t["year"], t["id"]))
    return meta, theories


def validate(meta, theories):
    """Every failure here is one that would otherwise ship looking correct."""
    problems = []
    ids = [t["id"] for t in theories]
    axis_ids = {a["id"] for a in meta["axes"]}
    traditions = set(meta["traditions"])
    topics = set(meta["topics"])
    eras = {e["id"] for e in meta["eras"]}

    for dup in {i for i in ids if ids.count(i) > 1}:
        problems.append(f"duplicate theory id: {dup}")

    for t in theories:
        where = t["_file"]
        for field in REQUIRED:
            if field not in t:
                problems.append(f"{where}: missing required field '{field}'")
        if problems and any(where in p for p in problems):
            continue

        if t["id"] != Path(where).stem:
            problems.append(f"{where}: id '{t['id']}' does not match the filename")
        if t["tradition"] not in traditions:
            problems.append(f"{where}: tradition '{t['tradition']}' is not in _meta.json")
        if t["era"] not in eras:
            problems.append(f"{where}: era '{t['era']}' is not in _meta.json")
        for topic in t["topics"]:
            if topic not in topics:
                problems.append(f"{where}: topic '{topic}' is not in _meta.json")

        # Axes: all four, in range, each with a note that justifies it.
        for axis in axis_ids:
            if axis not in t["axes"]:
                problems.append(f"{where}: no score on axis '{axis}'")
            elif not AXIS_MIN <= float(t["axes"][axis]) <= AXIS_MAX:
                problems.append(f"{where}: axis '{axis}' score out of range")
            if axis not in t["axis_notes"]:
                problems.append(f"{where}: axis '{axis}' scored with no note explaining it")
        for axis in t["axes"]:
            if axis not in axis_ids:
                problems.append(f"{where}: unknown axis '{axis}'")

        # The graph. An edge to a node that does not exist is the failure this
        # guard exists for: the renderer drops it and the diagram looks fine.
        seen = {}
        for i, layer in enumerate(t["layers"], start=1):
            for key in ("title", "text", "nodes", "edges"):
                if key not in layer:
                    problems.append(f"{where}: layer {i} has no '{key}'")
            for node in layer.get("nodes", []):
                if node["id"] in seen:
                    problems.append(f"{where}: node id '{node['id']}' reused "
                                    f"(layers {seen[node['id']]} and {i})")
                seen[node["id"]] = i
                if node.get("kind") not in ("cause", "mechanism", "outcome"):
                    problems.append(f"{where}: node '{node['id']}' has kind "
                                    f"'{node.get('kind')}' (want cause/mechanism/outcome)")
        for i, layer in enumerate(t["layers"], start=1):
            for edge in layer.get("edges", []):
                src, dst = edge[0], edge[1]
                for end in (src, dst):
                    if end not in seen:
                        problems.append(f"{where}: layer {i} edge references "
                                        f"unknown node '{end}'")
                label = edge[2] if len(edge) > 2 else ""
                if src in seen and dst in seen and seen[src] > seen[dst] and label != "feedback":
                    # A loop back to an earlier layer is usually a typo and
                    # occasionally the whole point (reinvested surplus feeding
                    # the next round). Declaring it keeps the typo catchable.
                    problems.append(f"{where}: edge {src} -> {dst} runs backwards "
                                    f"(layer {seen[src]} to layer {seen[dst]}). If the loop "
                                    f"is deliberate, mark the edge: [\"{src}\", \"{dst}\", \"feedback\"]")

        # Evidence must be sourced. This library's whole claim over the site it
        # is modelled on is that the claims are checkable.
        for ev in t["evidence"]:
            for key in ("claim", "finding", "source", "year"):
                if not ev.get(key):
                    problems.append(f"{where}: an evidence entry has no '{key}'")

        for rel in ("compare", "contrast"):
            if t[rel] not in ids:
                problems.append(f"{where}: {rel} points at '{t[rel]}', which is not a theory")
            if t[rel] == t["id"]:
                problems.append(f"{where}: {rel} points at itself")

    return problems


# ---------------------------------------------------------------- rendering

def stamp(rel):
    """Content hash for a shared asset, matching scripts/stamp-assets.py.

    The generated pages carry ?v=<hash> on every /css/ and /js/ reference for
    the reason that script documents: the service worker serves HTML
    network-first and static assets stale-while-revalidate, so fresh markup can
    pair with a previous deploy's script and the page renders wrong with
    nothing in the console. Computing the stamp here rather than letting
    stamp-assets.py add it afterwards keeps --check on both scripts agreeing;
    if the two ever disagree the asset-stamps job fails, which is the intent.
    """
    f = ROOT / rel.lstrip("/")
    if not f.is_file():
        return rel
    return rel + "?v=" + hashlib.md5(f.read_bytes()).hexdigest()[:8]


def esc(s):
    return html.escape(str(s), quote=True)


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def page_shell(title, description, keywords, og_title, og_desc, path, body, scripts):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<!-- Google tag (gtag.js) - G-JRCMEB9TBW -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-JRCMEB9TBW"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-JRCMEB9TBW');
</script>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- SEO Meta Tags -->
<meta name="description" content="{esc(description)}">
<meta name="keywords" content="{esc(keywords)}">
<meta property="og:title" content="{esc(og_title)}">
<meta property="og:description" content="{esc(og_desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.impactmojo.in{path}">
<meta property="og:image" content="https://www.impactmojo.in/assets/images/og-card.png">
<meta property="og:site_name" content="ImpactMojo">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(og_title)}">
<meta name="twitter:description" content="{esc(og_desc)}">
<meta name="twitter:image" content="https://www.impactmojo.in/assets/images/og-card.png">

<title>{esc(title)}</title>

<!-- Favicons -->
<link href="/assets/images/favicon.png" rel="icon" type="image/png">
<link href="/assets/images/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png">
<link href="/assets/images/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png">
<link href="/assets/images/apple-touch-icon.png" rel="apple-touch-icon">
<meta name="theme-color" content="#667eea">

<!-- Self-hosted fonts -->
<link rel="stylesheet" href="{stamp('/css/fonts.css')}">
<link rel="stylesheet" href="{stamp('/css/fundamentals.css')}">
<link rel="stylesheet" href="{stamp('/css/theories.css')}">
</head>
<body>
<div class="skip-nav" role="navigation" aria-label="Skip links"><a href="#main-content" class="skip-link">Skip to content</a></div>

<!-- ===== Top bar ===== -->
<div class="im-topbar" id="imTopbar">
  <div class="im-topbar-left">
    <a href="/index.html" class="im-topbar-home">
      <img src="/assets/images/ImpactMojo%20Logo.png" alt="ImpactMojo" width="28" height="28" style="border-radius:6px;">
      <span>ImpactMojo</span>
    </a>
  </div>
  <div class="im-topbar-right">
    <a href="/premium.html" class="im-premium-btn">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
      Premium
    </a>
    <div class="im-theme-selector" aria-label="Theme selection">
      <button class="im-theme-btn" data-imtheme="system" title="System theme" aria-label="Use system theme">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
      </button>
      <button class="im-theme-btn" data-imtheme="light" title="Light theme" aria-label="Use light theme">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
      </button>
      <button class="im-theme-btn" data-imtheme="dark" title="Dark theme" aria-label="Use dark theme">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
      </button>
    </div>
  </div>
</div>

<main id="main-content">
{body}
</main>

<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-col">
      <h4>About ImpactMojo</h4>
      <a href="/about.html">About Us</a>
      <a href="/ImpactMojo_PressKit.html">Press Kit</a>
      <a href="/contact.html">Contact</a>
    </div>
    <div class="footer-col">
      <h4>Related</h4>
      <a href="/fundamentals/">Fundamentals</a>
      <a href="/theories/">Theories of Development</a>
      <a href="/bct-repository.html">Behaviour Change Techniques</a>
    </div>
    <div class="footer-col">
      <h4>Legal</h4>
      <a href="/privacy-policy.html">Privacy Policy</a>
      <a href="/terms-of-service.html">Terms of Service</a>
      <a href="/disclaimer.html">Disclaimer</a>
    </div>
  </div>
  <p class="footer-note">Content CC BY-NC-ND 4.0 &middot; code MIT &middot; ImpactMojo</p>
</footer>

<script>
(function() {{
  function applyTheme(t) {{
    if (t === 'system') document.documentElement.removeAttribute('data-theme');
    else document.documentElement.setAttribute('data-theme', t);
  }}
  function updateButtons(t) {{
    document.querySelectorAll('.im-theme-btn').forEach(function(b) {{
      b.classList.toggle('active', b.getAttribute('data-imtheme') === t);
    }});
  }}
  var saved = 'system';
  try {{ saved = localStorage.getItem('im-theme') || 'system'; }} catch (e) {{}}
  applyTheme(saved);
  document.addEventListener('DOMContentLoaded', function() {{
    updateButtons(saved);
    document.querySelectorAll('.im-theme-btn').forEach(function(btn) {{
      btn.addEventListener('click', function() {{
        var t = this.getAttribute('data-imtheme');
        try {{ localStorage.setItem('im-theme', t); }} catch (e) {{}}
        applyTheme(t); updateButtons(t);
      }});
    }});
  }});
}})();
</script>

<script src="{stamp('/js/site-chrome.js')}" defer></script>
{scripts}
</body>
</html>
"""


def axis_bar(meta, t):
    rows = []
    for axis in meta["axes"]:
        score = float(t["axes"][axis["id"]])
        pct = (score - AXIS_MIN) / (AXIS_MAX - AXIS_MIN) * 100.0
        rows.append(f"""      <div class="ax-row">
        <div class="ax-head"><span class="ax-name">{esc(axis['name'])}</span></div>
        <div class="ax-track" role="img" aria-label="{esc(axis['name'])}: {score:+g} on a scale from {esc(axis['low'])} to {esc(axis['high'])}">
          <span class="ax-end ax-end--low">{esc(axis['low'])}</span>
          <span class="ax-line"><span class="ax-dot" style="left:{pct:.1f}%"></span></span>
          <span class="ax-end ax-end--high">{esc(axis['high'])}</span>
        </div>
        <p class="ax-note">{esc(t['axis_notes'][axis['id']])}</p>
      </div>""")
    return "\n".join(rows)


def theory_body(meta, t, by_id):
    thinkers = "".join(
        f"""        <div class="credit-card">
          <h3>{esc(th['name'])}{(' <span class="yrs">' + esc(th['years']) + '</span>') if th.get('years') else ''}</h3>
          <p>{esc(th.get('note', ''))}</p>
        </div>""" for th in t["thinkers"])

    summary = "".join(f"    <p>{esc(p)}</p>\n" for p in t["summary"])

    evidence = "".join(f"""      <div class="ev-card">
        <p class="ev-claim"><span class="ev-tag">The claim</span> {esc(ev['claim'])}</p>
        <p class="ev-find">{esc(ev['finding'])}</p>
        <p class="ev-src">{esc(ev['source'])} &middot; {esc(ev['year'])}</p>
      </div>""" for ev in t["evidence"])

    reading = "".join(f"""        <li><b>{esc(r['author'])}</b>, <i>{esc(r['title'])}</i> ({esc(r['year'])}). {esc(r.get('note', ''))}</li>""" for r in t["reading"])

    cmp_t, con_t = by_id[t["compare"]], by_id[t["contrast"]]
    names = {a["id"]: a["name"] for a in meta["axes"]}
    del names

    return f"""
<section class="hero">
  <div class="hero-inner">
    <span class="eyebrow"><a href="/theories/">Theories of Development</a> &middot; {esc(t['tradition'])} &middot; {esc(t['years_label'])}</span>
    <h1>{esc(t['name'])}</h1>
    <p class="claim">{esc(t['claim'])}</p>
    <p class="hero-credit">{esc(', '.join(th['name'] for th in t['thinkers']))} &middot; <a href="#credits">Credits and sources &darr;</a></p>
  </div>
</section>

<section class="wrap">
  <div class="section-head">
    <span class="kicker">The argument</span>
    <h2>What it says</h2>
  </div>
{summary}</section>

<section class="band" id="diagram-section">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">The causal chain</span>
      <h2>Drawn one step at a time</h2>
      <p>The theory as a graph, revealed a layer at a time. Use the buttons, or the left and right arrow keys. Each step adds the boxes that step introduces and the arrows into them.</p>
    </div>
    <div class="dg-layout">
      <div class="dg-canvas" id="dgCanvas" tabindex="0" role="group"
           aria-label="Causal diagram. Scrolls sideways on a narrow screen; left and right arrow keys step through it."></div>
      <div class="dg-side">
        <p class="dg-step" id="dgStep"></p>
        <h3 id="dgTitle"></h3>
        <p id="dgText"></p>
        <div class="dg-controls">
          <button type="button" id="dgBack" class="dg-btn">&larr; Back</button>
          <button type="button" id="dgNext" class="dg-btn dg-btn--primary">Next &rarr;</button>
        </div>
        <ul class="dg-key">
          <li><span class="key-swatch key-swatch--cause"></span> Starting condition</li>
          <li><span class="key-swatch key-swatch--mechanism"></span> Mechanism</li>
          <li><span class="key-swatch key-swatch--outcome"></span> Outcome or policy</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="wrap" id="axes-section">
  <div class="section-head">
    <span class="kicker">Where it sits</span>
    <h2>Four placements, and the reason for each</h2>
    <p>{esc(meta['axis_disclaimer'])}</p>
  </div>
  <div class="axes">
{axis_bar(meta, t)}
  </div>
</section>

<section class="band" id="evidence-section">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">What happened</span>
      <h2>The theory against the record</h2>
      <p>Each entry takes one claim the theory makes and reports what the evidence says about it, with a named source and a year. This section is the reason the library exists; a catalogue of positions without it is a reading list.</p>
    </div>
    <div class="ev-grid">
{evidence}
    </div>
    <div class="notice">
      <h3>What this does not settle</h3>
      <p>{esc(t['unsettled'])}</p>
    </div>
  </div>
</section>

<section class="wrap" id="india-section">
  <div class="section-head">
    <span class="kicker">In India</span>
    <h2>How it landed here</h2>
  </div>
  <p>{esc(t['india'])}</p>
</section>

<section class="band" id="neighbours">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Read next</span>
      <h2>One that agrees, one that does not</h2>
    </div>
    <div class="nb-grid">
      <div class="nb-card nb-card--compare">
        <span class="nb-tag">Closest to it</span>
        <h3><a href="/theories/{esc(cmp_t['id'])}.html">{esc(cmp_t['name'])}</a></h3>
        <p>{esc(t['compare_note'])}</p>
      </div>
      <div class="nb-card nb-card--contrast">
        <span class="nb-tag">Furthest from it</span>
        <h3><a href="/theories/{esc(con_t['id'])}.html">{esc(con_t['name'])}</a></h3>
        <p>{esc(t['contrast_note'])}</p>
      </div>
    </div>
  </div>
</section>

<section class="wrap" id="credits">
  <div class="section-head">
    <span class="kicker">Credit where it is owed</span>
    <h2>Whose theory this is</h2>
  </div>
  <div class="credits">
{thinkers}
    <div class="credit-card">
      <h3>What ImpactMojo added</h3>
      <p>The causal diagram, the four placements and the notes justifying them, and the evidence section: what each claim predicted and what the record shows, with a named source and year for every entry.</p>
      <p class="who-line">ImpactMojo &middot; content CC BY-NC-ND 4.0 &middot; code MIT</p>
    </div>
  </div>
  <div class="notice">
    <h3>Start with these</h3>
    <ul class="reading">
{reading}
    </ul>
    <p>More on this and neighbouring arguments in <a href="https://varnasr.github.io/development-discourses/">Development Discourses</a>, an open-access reference library of research and grey literature for South Asian development work.</p>
  </div>
</section>
"""


def index_body(meta, theories):
    cards = []
    for t in theories:
        topics = "".join(f'<span class="th-chip">{esc(x)}</span>' for x in t["topics"])
        cards.append(f"""      <article class="th-card" data-id="{esc(t['id'])}"
          data-tradition="{esc(t['tradition'])}" data-era="{esc(t['era'])}"
          data-topics="{esc('|'.join(t['topics']))}"
          data-search="{esc((t['name'] + ' ' + t['short'] + ' ' + t['claim'] + ' ' + ' '.join(th['name'] for th in t['thinkers'])).lower())}">
        <div class="th-card-top">
          <span class="th-years">{esc(t['years_label'])}</span>
          <span class="th-trad">{esc(t['tradition'])}</span>
        </div>
        <h3><a href="/theories/{esc(t['id'])}.html">{esc(t['name'])}</a></h3>
        <p class="th-who">{esc(', '.join(th['name'] for th in t['thinkers']))}</p>
        <p class="th-claim">{esc(t['claim'])}</p>
        <div class="th-chips">{topics}</div>
      </article>""")

    def filter_group(key, label, options):
        opts = "".join(
            f'<button type="button" class="fbtn" data-filter="{key}" data-value="{esc(v)}">{esc(lab)}</button>'
            for v, lab in options)
        return f"""      <div class="fgroup">
        <span class="flabel">{esc(label)}</span>
        <div class="fbtns">{opts}</div>
      </div>"""

    used_trad = [x for x in meta["traditions"] if any(t["tradition"] == x for t in theories)]
    used_topics = [x for x in meta["topics"] if any(x in t["topics"] for t in theories)]
    used_eras = [e for e in meta["eras"] if any(t["era"] == e["id"] for t in theories)]

    axes_legend = "".join(
        f"""      <div class="lg-row">
        <b>{esc(a['name'])}</b>
        <span class="lg-scale">{esc(a['low'])} <span class="lg-arrow">&harr;</span> {esc(a['high'])}</span>
        <p>{esc(a['question'])}</p>
      </div>""" for a in meta["axes"])

    return f"""
<section class="hero">
  <div class="hero-inner">
    <span class="eyebrow">Theories of Development</span>
    <h1>How development is supposed to work.<br><span class="accent">{len(theories)} answers, drawn as causal chains.</span></h1>
    <p>Development policy runs on theories about why some places are poor, and most of them are argued about without anybody drawing what they actually claim. Each entry here is one theory turned into a diagram you can step through, placed on four axes with the reason for each placement, and then set against the record: what it predicted, what happened, and what is still open.</p>
    <p>Global canon and South Asian traditions in one catalogue, so that Rostow and Nehru, or Ambedkar and Gandhi, can be read side by side rather than in separate literatures.</p>
    <nav class="series-nav" aria-label="Related libraries">
      <a href="/fundamentals/">Fundamentals: the diagrams</a>
      <a href="/bct-repository.html">Behaviour change techniques</a>
    </nav>
  </div>
</section>

<section class="wrap" id="browse">
  <div class="section-head">
    <span class="kicker">The catalogue</span>
    <h2>Filter it</h2>
  </div>
  <div class="filters" id="filters">
    <div class="fgroup fgroup--search">
      <label class="flabel" for="thSearch">Search</label>
      <input type="search" id="thSearch" placeholder="A theory, a thinker, a claim" autocomplete="off">
    </div>
{filter_group('tradition', 'Tradition', [(x, x) for x in used_trad])}
{filter_group('topics', 'Topic', [(x, x) for x in used_topics])}
{filter_group('era', 'When', [(e['id'], e['label']) for e in used_eras])}
    <div class="fgroup fgroup--reset">
      <button type="button" id="thReset" class="fbtn fbtn--reset">Clear all</button>
    </div>
  </div>
  <p class="fcount" id="thCount" role="status" aria-live="polite"></p>
  <div class="th-grid" id="thGrid">
{chr(10).join(cards)}
  </div>
  <p class="fempty" id="thEmpty" hidden>Nothing matches that combination. <button type="button" class="linkish" id="thResetInline">Clear the filters</button>.</p>
</section>

<section class="band" id="axes-legend">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">How the placements work</span>
      <h2>Four axes, chosen for this material</h2>
      <p>Catalogues of political thought usually sort on a left-to-right axis. That axis sorts Indian thought badly: it puts Ambedkar and Nehru far apart while they share most of their economics, and it has nowhere to put Gandhi at all. These four ask questions that the theories on this shelf actually disagree about.</p>
    </div>
    <div class="legend">
{axes_legend}
    </div>
    <div class="notice">
      <h3>The placements are ours, so argue with them</h3>
      <p>{esc(meta['axis_disclaimer'])}</p>
    </div>
  </div>
</section>

<section class="wrap">
  <div class="section-head">
    <span class="kicker">Using this</span>
    <h2>In a classroom or a workshop</h2>
  </div>
  <p>Give a group two theories that contrast, one from the global canon and one from South Asia, and have them find the sentence in each that the other would refuse. The disagreement is usually not about facts and usually not about values either; it is about which mechanism is doing the work, which is what the diagrams are for.</p>
  <p>The evidence section on each page is deliberately unkind to the theory it belongs to, including the ones we find persuasive. If you reproduce a diagram or the evidence, credit ImpactMojo. If you reproduce a theory, credit the person who thought of it, which each page names.</p>
</section>
"""


def build(meta, theories, today):
    """Return {relative path: text} for everything this script owns."""
    by_id = {t["id"]: t for t in theories}
    out = {}

    payload = {
        "meta": {k: v for k, v in meta.items() if not k.startswith("_")},
        "theories": [{k: v for k, v in t.items() if k != "_file"} for t in theories],
    }
    out["js/theories-data.js"] = (
        "/* Generated by scripts/build-theories.py from data/theories/. Do not edit by hand:\n"
        "   edit the JSON under data/theories/ and re-run the script. CI checks this file\n"
        "   against the source with `python3 scripts/build-theories.py --check`. */\n"
        "window.THEORIES = " + json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False) + ";\n"
    )

    for t in theories:
        who = ", ".join(th["name"] for th in t["thinkers"])
        desc = f"{t['claim']} {who}, {t['years_label']}. The causal chain drawn step by step, four placements with the reason for each, and what the evidence says about the claims."
        kw = ", ".join([t["name"], t["short"], t["tradition"]] +
                       [th["name"] for th in t["thinkers"]] + t["topics"] +
                       ["development theory", "India", "ImpactMojo"])
        out[f"theories/{t['id']}.html"] = page_shell(
            title=f"Theories of Development | {t['name']}",
            description=desc[:320],
            keywords=kw,
            og_title=f"Theories of Development | {t['name']}",
            og_desc=t["claim"][:300],
            path=f"/theories/{t['id']}.html",
            body=theory_body(meta, t, by_id),
            scripts=(f'<script src="{stamp("/js/theories-data.js")}"></script>\n'
                     f'<script src="{stamp("/js/theories.js")}" data-theory="{t["id"]}"></script>'),
        )

    out["theories/index.html"] = page_shell(
        title="Theories of Development | ImpactMojo",
        description=(f"{len(theories)} theories of development, each drawn as a causal chain you can step "
                     "through, placed on four axes built for South Asian material, and set against what the "
                     "evidence actually shows. Global canon and Indian traditions in one filterable catalogue."),
        keywords=("development theory, theories of development, Rostow, Lewis, dependency theory, Ambedkar, "
                  "Gandhi, Mahalanobis, development economics, South Asia, India, ImpactMojo"),
        og_title="Theories of Development",
        og_desc=("How development is supposed to work: theories drawn as causal chains, placed on four axes, "
                 "and set against the record."),
        path="/theories/index.html",
        body=index_body(meta, theories),
        scripts=f'<script src="{stamp("/js/theories-index.js")}"></script>',
    )
    out.update(shared_files(theories, today))
    return out


SITEMAP = ROOT / "sitemap.xml"
SEARCH_INDEX = ROOT / "data" / "search-index.json"


def shared_files(theories, today):
    """Return updated sitemap.xml and search-index.json text.

    These two files are shared with the rest of the site, so this script owns
    only the rows whose URL starts /theories/ and rewrites those in place. The
    reason it touches them at all is rules/testing.md item 13: adding a page
    updates the sitemap, the search index is a separate file nobody is forced to
    touch, and the two had drifted 127 pages apart before anyone noticed.
    """
    out = {}

    sitemap = SITEMAP.read_text(encoding="utf-8")
    # Keep the lastmod a page already has. Stamping today's date on every run
    # would make --check fail tomorrow on an unchanged repo, and would tell
    # search engines that twelve pages changed when none did.
    seen_dates = dict(re.findall(
        r"<loc>https://www\.impactmojo\.in(/theories/[^<]*)</loc><lastmod>([0-9-]+)</lastmod>", sitemap))
    kept = [ln for ln in sitemap.splitlines()
            if "impactmojo.in/theories/" not in ln]
    def row(path, priority):
        stamp = seen_dates.get(path, today)
        return (f'  <url><loc>https://www.impactmojo.in{path}</loc><lastmod>{stamp}</lastmod>'
                f'<changefreq>monthly</changefreq><priority>{priority}</priority></url>')

    rows = [row("/theories/", "0.8")]
    for t in theories:
        rows.append(row(f"/theories/{t['id']}.html", "0.7"))
    idx = kept.index("</urlset>")
    out["sitemap.xml"] = "\n".join(kept[:idx] + rows + kept[idx:]) + "\n"

    entries = json.loads(SEARCH_INDEX.read_text(encoding="utf-8"))
    entries = [e for e in entries if not str(e.get("url", "")).startswith("/theories/")]
    entries.append({
        "id": "THEORY000",
        "title": "Theories of Development",
        "description": (f"{len(theories)} theories of how development is supposed to work, each drawn as a "
                        "causal chain you can step through, placed on four axes built for South Asian "
                        "material, and set against what the evidence shows. Global canon and Indian "
                        "traditions in one filterable catalogue."),
        "type": "theory",
        "category": "Frameworks",
        "url": "/theories/",
        "tags": ["development theory", "theories of development", "development economics",
                 "South Asia", "India", "causal diagram", "ImpactMojo"],
    })
    for i, t in enumerate(theories, start=1):
        entries.append({
            "id": f"THEORY{i:03d}",
            "title": t["name"],
            "description": (t["claim"] + " " + " ".join(th["name"] for th in t["thinkers"]) +
                            f", {t['years_label']}. The causal chain drawn step by step, four placements "
                            "with the reason for each, and what the evidence says about the claims."),
            "type": "theory",
            "category": "Frameworks",
            "url": f"/theories/{t['id']}.html",
            "tags": ([th["name"] for th in t["thinkers"]] + [t["tradition"]] + t["topics"] +
                     [t["short"], "development theory", "India"]),
        })
    out["data/search-index.json"] = json.dumps(entries, ensure_ascii=False, indent=2) + "\n"
    return out


def main():
    check = "--check" in sys.argv
    meta, theories = load()
    if not theories:
        print("FAIL - no theory files found in data/theories/")
        return 1

    problems = validate(meta, theories)
    if problems:
        print(f"FAIL - {len(problems)} problem(s) in data/theories/:")
        for p in problems:
            print(f"  - {p}")
        return 1

    today = datetime.date.today().isoformat()
    out = build(meta, theories, today)

    if check:
        drift = []
        for rel, text in out.items():
            path = ROOT / rel
            if not path.exists():
                drift.append(f"{rel} is missing")
            elif path.read_text(encoding="utf-8") != text:
                drift.append(f"{rel} is out of date")
        stale = {p.name for p in OUT_DIR.glob("*.html")} - {Path(r).name for r in out}
        for name in sorted(stale):
            drift.append(f"theories/{name} is not generated by any file in data/theories/")
        if drift:
            print(f"FAIL - {len(drift)} generated file(s) out of sync. "
                  f"Run: python3 scripts/build-theories.py")
            for d in drift:
                print(f"  - {d}")
            return 1
        print(f"PASS - {len(theories)} theories, {len(out)} generated files in sync.")
        return 0

    OUT_DIR.mkdir(exist_ok=True)
    written = 0
    for rel, text in out.items():
        path = ROOT / rel
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            path.write_text(text, encoding="utf-8")
            written += 1
    for path in sorted(OUT_DIR.glob("*.html")):
        if f"theories/{path.name}" not in out:
            path.unlink()
            print(f"  removed stale {path.relative_to(ROOT)}")
    print(f"PASS - {len(theories)} theories validated, {written} of {len(out)} files rewritten.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
