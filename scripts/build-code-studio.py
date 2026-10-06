#!/usr/bin/env python3
"""Build the Code Studio pages under /code/ from small content specs.

Each page is a spec module in scripts/code-studio/specs/<name>.py defining PAGE.
The shell (head, top bar, tabs, footer, scripts) is written here once, so every
page looks and behaves the same; the specs carry only the teaching.

    python3 scripts/build-code-studio.py            # write every page
    python3 scripts/build-code-studio.py --check    # exit 1 if any page is stale

Spec format (PAGE dict):
    slug         output file, /code/<slug>.html ("index" for the landing page)
    kind         "runnable" (code runs in the browser) or "guide" (tool you install)
    title        <title> and card heading
    h1, lede     page heading and one-paragraph introduction
    description  meta description (one or two sentences)
    card         short line for the landing page card
    tool         for guides: the software name, shown on the card
    datasets     list of /code/data/<name>.csv files the engines should load
    engine_note  optional HTML shown above the tabs
    modules      list of {"tab", "title", "blocks": [...]}
    next         list of {"href", "title", "desc"} shown on the last module

Blocks: {"t": "p"|"h3"|"info"|"ul"|"steps"|"code"|"dual"|"syntax"|"html", ...}
    p, h3:   html
    info:    html, optional tone "warning"|"success"
    ul:      items (list of html)
    steps:   items (list of html), numbered
    code:    lang ("r"|"py"|"sql"|"shiny-r"|"shiny-py"), code, optional pkgs
    dual:    r, py, optional pkgs (R packages) and pypkgs (Python packages)
    syntax:  label, code. Read-only code for software that cannot run here
             (Stata, SPSS). Never paired with an invented output.
    html:    html, raw escape hatch
"""
import html
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPECS = ROOT / "scripts" / "code-studio" / "specs"
OUT = ROOT / "code"
SITE = "https://www.impactmojo.in"

TOPBAR = """<div class="im-topbar" id="imTopbar">
    <div class="im-topbar-left">
        <a href="/" class="im-topbar-home">
            <img src="/assets/images/ImpactMojo%20Logo.png" alt="ImpactMojo" width="24" height="24" style="border-radius:4px;">
            <span>ImpactMojo</span>
        </a>
    </div>
    <div class="im-topbar-right">
        <a href="/catalog.html" class="im-browse-btn" title="Browse all content"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>Browse</a>
        <a href="/premium.html" class="im-premium-btn">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            Membership
        </a>
        <div class="im-theme-selector" aria-label="Theme selection">
            <button class="im-theme-btn" data-theme="system" title="System theme" aria-label="Use system theme"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></button>
            <button class="im-theme-btn" data-theme="light" title="Light theme" aria-label="Use light theme"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg></button>
            <button class="im-theme-btn" data-theme="dark" title="Dark theme" aria-label="Use dark theme"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg></button>
        </div>
    </div>
</div>"""

FOOTER = """<footer class="im-footer" role="contentinfo">
<div class="im-footer-content">
<p class="im-footer-made">Made with &#10084; by <a href="https://www.pinpointventures.in" rel="noopener noreferrer" target="_blank">PinPoint Ventures</a></p>
<div class="im-footer-grid">
<div class="im-footer-section"><h4>Learn</h4><ul>
<li><a href="/code/">Code Studio</a></li>
<li><a href="/101-courses/">101 Series</a></li>
<li><a href="/courses/">Courses</a></li>
<li><a href="/catalog.html">Full Catalog</a></li>
</ul></div>
<div class="im-footer-section"><h4>Explore</h4><ul>
<li><a href="/">Home</a></li>
<li><a href="/blog.html">Blog</a></li>
<li><a href="/premium-tools/code-converter-pro.html">Code Convert Pro</a></li>
<li><a href="/premium.html">Membership</a></li>
</ul></div>
<div class="im-footer-section"><h4>About</h4><ul>
<li><a href="/about.html">About ImpactMojo</a></li>
<li><a href="/contact.html">Contact</a></li>
</ul></div>
</div>
<div class="im-footer-bottom">
<p>&copy; 2026 ImpactMojo. Free development education for South Asia.</p>
<p>R runs via <a href="https://webr.r-wasm.org" rel="noopener" target="_blank">WebR</a>, Python via <a href="https://pyodide.org" rel="noopener" target="_blank">Pyodide</a> and SQL via <a href="https://sql.js.org" rel="noopener" target="_blank">sql.js</a>: open source, in your browser. Shiny apps open in <a href="https://shinylive.io" rel="noopener" target="_blank">Shinylive</a>.</p>
</div>
</div>
</footer>"""

BACK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
        'stroke-linejoin="round"><path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/></svg>')

PLANE = """<svg class="v3-paper-plane" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M50,150 L150,50 L50,100 L80,130 Z" fill="none" stroke="#0EA5E9" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M80,130 L150,50" stroke="#10B981" stroke-width="2" stroke-dasharray="4,4"/>
        <circle cx="150" cy="50" r="4" fill="#6366F1"/>
    </svg>"""


def esc(s):
    return html.escape(s, quote=True)


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.PAGE


def block(b):
    t = b["t"]
    if t == "p":
        return "<p>%s</p>" % b["html"]
    if t == "h3":
        return "<h3>%s</h3>" % b["html"]
    if t == "info":
        tone = (" " + b["tone"]) if b.get("tone") else ""
        return '<div class="info-box%s">%s</div>' % (tone, b["html"])
    if t == "ul":
        return "<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in b["items"])
    if t == "steps":
        return '<ol class="guide-steps">%s</ol>' % "".join("<li>%s</li>" % i for i in b["items"])
    if t == "code":
        attrs = ' data-lang="%s"' % b["lang"]
        if b.get("pkgs"):
            attrs += ' data-pkgs="%s"' % esc(b["pkgs"])
        return ('<div class="code-cell"%s><textarea class="code-input" spellcheck="false" '
                'aria-label="%s code editor">%s</textarea></div>'
                % (attrs, {"r": "R", "py": "Python", "sql": "SQL", "shiny-r": "Shiny R",
                           "shiny-py": "Shiny Python"}[b["lang"]], esc(b["code"])))
    if t == "dual":
        attrs = ' data-r="%s" data-py="%s"' % (esc(b["r"]), esc(b["py"]))
        if b.get("pkgs"):
            attrs += ' data-pkgs="%s"' % esc(b["pkgs"])
        if b.get("pypkgs"):
            attrs += ' data-pypkgs="%s"' % esc(b["pypkgs"])
        return ('<div class="code-cell"%s><textarea class="code-input" spellcheck="false" '
                'aria-label="Code editor">%s</textarea></div>' % (attrs, esc(b["r"])))
    if t == "syntax":
        return ('<div class="syntax-label">%s</div><pre class="syntax-block">%s</pre>'
                % (esc(b["label"]), esc(b["code"])))
    if t == "html":
        return b["html"]
    raise ValueError("unknown block type %r" % t)


def head(page, canonical):
    ld = {
        "@context": "https://schema.org",
        "@type": "LearningResource" if page["slug"] != "index" else "CollectionPage",
        "name": page["title"],
        "description": page["description"],
        "url": canonical,
        "isAccessibleForFree": True,
        "inLanguage": "en",
        "provider": {"@type": "Organization", "name": "ImpactMojo", "url": SITE},
    }
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
    <meta name="theme-color" content="#0F172A">
    <title>%(title)s | ImpactMojo</title>
    <meta name="description" content="%(desc)s">
    <link rel="canonical" href="%(canon)s">
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-JRCMEB9TBW"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-JRCMEB9TBW');
</script>
    <link rel="stylesheet" href="/css/fonts.css">
    <link rel="stylesheet" href="/css/code-studio.css">
<meta name="robots" content="index, follow">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:image" content="https://www.impactmojo.in/assets/images/og-card.png">
<meta property="og:url" content="%(canon)s">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ImpactMojo">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(title)s">
<meta name="twitter:description" content="%(desc)s">
<meta name="twitter:image" content="https://www.impactmojo.in/assets/images/og-card.png">
<link rel="icon" type="image/png" href="/assets/images/favicon.png">
<link rel="apple-touch-icon" href="/assets/images/apple-touch-icon.png">
<script type="application/ld+json">%(ld)s</script>
</head>""" % {"title": esc(page["title"]), "desc": esc(page["description"]),
              "canon": canonical, "ld": json.dumps(ld, ensure_ascii=False)}


def render_lesson(page):
    canonical = "%s/code/%s.html" % (SITE, page["slug"])
    mods = page["modules"]
    tabs = "".join('<button class="tab-btn%s" type="button" role="tab"><span class="tab-num">%d</span> %s</button>'
                   % (" active" if i == 0 else "", i + 1, esc(m["tab"])) for i, m in enumerate(mods))
    panels = []
    for i, m in enumerate(mods):
        body = "\n".join(block(b) for b in m["blocks"])
        if i == len(mods) - 1 and page.get("next"):
            items = "".join('<div class="road-item"><div class="road-num">&rarr;</div><div><h4><a href="%s" '
                            'style="color:var(--text-primary)">%s</a></h4><p>%s</p></div></div>'
                            % (n["href"], n["title"], n["desc"]) for n in page["next"])
            body += '\n<h3>Where next</h3><div class="roadmap">%s</div>' % items
        prev_btn = ('<button class="btn" type="button" data-goto="%d">&larr; Back</button>' % (i - 1)) if i else "<span></span>"
        if i < len(mods) - 1:
            next_btn = ('<button class="btn btn-primary" type="button" data-goto="%d">Next: %s &rarr;</button>'
                        % (i + 1, esc(mods[i + 1]["tab"])))
        else:
            next_btn = '<a class="btn btn-primary" href="/code/">All Code Studio courses &rarr;</a>'
        panels.append('<div class="tab-panel lesson%s" data-panel="%d" role="tabpanel">\n'
                      '<div class="eyebrow">Module %d of %d</div>\n<h2>%s</h2>\n%s\n'
                      '<div class="nav-row">%s%s</div>\n</div>'
                      % (" active" if i == 0 else "", i, i + 1, len(mods), m["title"], body, prev_btn, next_btn))
    kind_badge = "Runs in your browser" if page["kind"] == "runnable" else "Guided tool course"
    note = ('<div class="info-box warning" style="margin-bottom:1.25rem;">%s</div>' % page["engine_note"]
            if page.get("engine_note") else "")
    return """%(head)s
<body data-datasets="%(datasets)s">
<a href="#main-content" class="im-skip-link">Skip to content</a>
%(topbar)s
<a id="main-content" tabindex="-1"></a>
<div class="container" id="main">
    %(plane)s
    <a href="/code/" class="back-link">%(back)s Back to Code Studio</a>
    <div class="header">
        <div class="header-badge">Code Studio &middot; %(kind)s</div>
        <h1>%(h1)s</h1>
        <p>%(lede)s</p>
    </div>
    %(note)s
    <div class="progress-bar"><div class="progress-bar-fill" id="progressFill"></div></div>
    <div class="tabs" id="tabs" role="tablist">%(tabs)s</div>
%(panels)s
</div>
%(footer)s
<script src="/js/code-studio.js"></script>
<script src="/js/translate-sarvam.js" defer></script>
<script src="/js/site-chrome.js" defer></script>
</body>
</html>
""" % {"head": head(page, canonical), "datasets": ",".join(page.get("datasets", [])), "topbar": TOPBAR,
       "plane": PLANE, "back": BACK, "kind": kind_badge, "h1": page["h1"], "lede": page["lede"], "note": note,
       "tabs": tabs, "panels": "\n".join(panels), "footer": FOOTER}


def render_index(page, others):
    canonical = SITE + "/code/"
    sections = []
    for kind, title, note in page["sections"]:
        cards = "".join('<a class="studio-card" href="/code/%s.html"><span class="studio-kind">%s</span>'
                        '<h3>%s</h3><p>%s</p></a>'
                        % (o["slug"], esc(o.get("tool") or ("Runs in your browser" if o["kind"] == "runnable" else "Guided")),
                           esc(o["title"]), o["card"])
                        for o in others if o["kind"] == kind)
        sections.append('<h2 class="studio-section-title">%s</h2><p class="studio-section-note">%s</p>'
                        '<div class="studio-grid">%s</div>' % (title, note, cards))
    return """%(head)s
<body>
<a href="#main-content" class="im-skip-link">Skip to content</a>
%(topbar)s
<a id="main-content" tabindex="-1"></a>
<div class="container" id="main">
    %(plane)s
    <a href="/" class="back-link">%(back)s Back to ImpactMojo</a>
    <div class="header">
        <div class="header-badge">Code Studio</div>
        <h1>%(h1)s</h1>
        <p>%(lede)s</p>
    </div>
    %(intro)s
    %(sections)s
</div>
%(footer)s
<script src="/js/code-studio.js"></script>
<script src="/js/translate-sarvam.js" defer></script>
<script src="/js/site-chrome.js" defer></script>
</body>
</html>
""" % {"head": head(page, canonical), "topbar": TOPBAR, "plane": PLANE, "back": BACK, "h1": page["h1"],
       "lede": page["lede"], "intro": page.get("intro", ""), "sections": "\n".join(sections), "footer": FOOTER}


def main():
    check = "--check" in sys.argv
    pages = [load(p) for p in sorted(SPECS.glob("*.py")) if not p.name.startswith("_")]
    index = [p for p in pages if p["slug"] == "index"]
    others = sorted([p for p in pages if p["slug"] != "index"], key=lambda p: p.get("order", 99))
    out = {}
    for p in others:
        out["%s.html" % p["slug"]] = render_lesson(p)
    if index:
        out["index.html"] = render_index(index[0], others)
    stale = []
    OUT.mkdir(exist_ok=True)
    for name, text in out.items():
        path = OUT / name
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if check:
            # stamp-assets.py adds ?v= hashes after the build; compare without them.
            import re
            norm = lambda s: re.sub(r'\?v=[0-9a-f]+', '', s or '')
            if norm(current) != norm(text):
                stale.append(name)
        else:
            path.write_text(text, encoding="utf-8")
    if check:
        if stale:
            print("FAIL - Code Studio pages out of date: %s. Run python3 scripts/build-code-studio.py"
                  % ", ".join(stale))
            sys.exit(1)
        print("PASS - %d Code Studio pages match their specs." % len(out))
    else:
        print("wrote %d pages to code/" % len(out))


if __name__ == "__main__":
    main()
