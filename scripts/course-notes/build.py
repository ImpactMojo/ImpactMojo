#!/usr/bin/env python3
"""Assemble the paid Flagship Course Notes as print-ready HTML.

    python3 scripts/course-notes/build.py OUT_DIR [course_id ...]

Reads every module of each flagship from Supabase `course_content` (through
the Management API, so it needs $SUPABASE_PAT) and writes OUT_DIR/<file>.html,
one document per course: a cover, a contents page and the modules in order.
`render.mjs` then prints each to A4 PDF, named as the order handler expects
(ImpactMojo-Notes-<file>.pdf in the private `products` bucket).

Why this exists. The first PDFs were printed from module HTML without the
rules that size its inline icons. The course text carries hundreds of them
(`<svg class="external-icon">` after every reading link, Sargam `<img>` icons
in every callout) with no width of their own; on the site the stylesheet
makes them 1em, and printed bare each one grew to the full width of the page.
On 2026-10-10 that was 249 pages of icon and nothing else across 12 of the 18
PDFs (85 of dataviz's 150), all of it sold. PRINT_CSS below sizes every one,
and render.mjs refuses to write a PDF with a page that carries almost no text.
"""
import html
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROJECT = "ddyszmfffyedolkcugld"

# course_id in the database -> (file stem, title, track label)
COURSES = {
    "gandhi": ("gandhi", "Gandhi's Political Thought: Philosophy for Praxis", "Philosophy, Law & Governance"),
    "devecon": ("devecon", "Understanding Development: An Economics Perspective", "Policy & Economics"),
    "dataviz": ("dataviz", "Seeing Data: Visualization for Impact", "Data & Technology"),
    "devai": ("devai", "AI for Impact: Data Monitoring & Evaluation", "Data & Technology"),
    "mel": ("mel", "MEL for Development: Monitoring, Evaluation & Learning", "MEL & Research"),
    "poa": ("poa", "Politics of Aspiration: Rights, Insurance & Social Mobility", "Policy & Economics"),
    "media": ("media", "Media for Development: Communication, Power & Practice", "Health & Communication"),
    "SEL": ("sel", "Social-Emotional Learning for Development", "Health & Communication"),
    "law": ("law", "Constitution & Law for Development Practice", "Philosophy, Law & Governance"),
    "pubpol": ("pubpol", "Public Policy: Process, Design & Governance", "Policy & Economics"),
    "gender": ("gender", "Gender Studies: Feminisms, Power & Social Change", "Gender & Equity"),
    "pubchoice": ("pubchoice", "Public Choice: Decisions, Incentives & Institutions", "Policy & Economics"),
    "livelihoods": ("livelihoods", "Livelihoods in India: Rural, Urban & Skills", "Policy & Economics"),
    "powerBI": ("powerBI", "Power BI for Practitioners", "Data & Technology"),
    "causal": ("causal", "Causal Inference for Development", "Data & Technology"),
    "intervention": ("intervention", "Designing What Works: Development Interventions from Model to Scale", "Policy & Economics"),
    "nvc-rj": ("nvc-rj", "Nonviolence in Practice: NVC, NVR & Restorative Justice", "Health & Communication"),
    "nothing-about-us": ("nothing-about-us", "Nothing About Us Without Us: Disability, Justice & Development", "Gender & Equity"),
    "social-movements": ("social-movements", "Social Movements & Protests: Theory and South Asian Practice", "Policy & Economics"),
    "esg": ("esg", "Sustainability, ESG & Corporate Responsibility for Development Practice", "Policy & Economics"),
    "gender-mel": ("gender-mel", "Gender-Sensitive Monitoring, Evaluation & Learning", "Gender & Equity"),
}

PRINT_CSS = """
@page { size: A4; margin: 18mm 17mm 20mm; }
html, body { background: #fff !important; color: #0F172A !important; }
body { font-family: Inter, 'Segoe UI', Arial, sans-serif; font-size: 10.5pt; line-height: 1.55; margin: 0; }
.notes-cover { position: relative; height: 232mm; display: flex; flex-direction: column; justify-content: center; text-align: center; page-break-after: always; }
.notes-cover .brand { font-size: 9pt; letter-spacing: .14em; font-weight: 700; color: #0369A1; position: absolute; top: 0; left: 0; right: 0; }
.notes-cover .track { font-size: 9pt; letter-spacing: .18em; text-transform: uppercase; color: #475569; }
.notes-cover h1 { font-size: 26pt; line-height: 1.15; margin: .3em 0; color: #0F172A; }
.notes-cover .kind { font-size: 13pt; color: #0369A1; font-weight: 600; }
.notes-cover .meta { color: #475569; margin-top: .4em; }
.notes-cover .blurb { max-width: 135mm; margin: 1.4em auto 0; color: #334155; }
.notes-cover .legal { position: absolute; bottom: 8mm; left: 0; right: 0; font-size: 8pt; color: #64748B; }
.notes-toc { page-break-after: always; }
.notes-toc h2 { font-size: 16pt; color: #0369A1; }
.notes-toc ol { padding-left: 1.6em; } .notes-toc li { margin: .3em 0; }
/* Modules run on: a forced page break per module left the end of almost every
   module mostly blank. A rule and the title mark the start instead. */
.notes-module { margin-top: 14pt; padding-top: 10pt; border-top: 2px solid #0369A1; }
.notes-toc + .notes-module { margin-top: 0; padding-top: 0; border-top: 0; }
.notes-module > h2.module-title { font-size: 17pt; color: #0369A1; margin: 0 0 .5em; break-after: avoid; page-break-after: avoid; }
.notes-module .module-intro { color: #334155; font-style: italic; }
h1, h2, h3, h4 { page-break-after: avoid; break-after: avoid; }
/* Long tables break across pages so they leave no half-empty page behind;
   rows stay whole and the header row repeats. */
thead { display: table-header-group; } tr, thead { break-inside: avoid; page-break-inside: avoid; }
/* Only short blocks are kept whole. Worked examples and data exercises run to
   half a page, and holding them together pushed each one to the next page and
   left the rest of the current page empty. */
figure, .dag-figure, .callout, .coach-callout, .definition, .key-insight, .concept-box, .equation-box,
.reflection-prompt, .stat-card, .comparison-card, .reading-box, li, p { break-inside: avoid; page-break-inside: avoid; }
.data-exercise, .worked-example { break-inside: auto; page-break-inside: auto; }
p { orphans: 3; widows: 3; }
/* Every inline icon gets a size. Unsized, each one printed as wide as the page. */
svg { max-width: 100%; height: auto; }
svg.external-icon, a svg, li svg, p svg, button svg, h2 svg, h3 svg, h4 svg,
svg[viewBox="0 0 24 24"], svg[viewBox="0 0 20 20"], svg[viewBox="0 0 16 16"] { width: 1em !important; height: 1em !important; vertical-align: -0.12em; display: inline-block; }
img { max-width: 100%; height: auto; }
img.sargam-icon, img.section-header-icon, img.callout-icon, img.card-icon, img.feature-card-icon, img.comparison-icon,
img[src*="sargam"], img[src*="/si_"], .ico img, .icon img, .callout-icon img { width: 1.15em !important; height: 1.15em !important; vertical-align: -0.2em; display: inline-block; }
img.coach-photo { width: 34px !important; height: 34px !important; border-radius: 50%; object-fit: cover; }
/* Interactive controls do nothing on paper. */
button, .excerpt-btn, .quiz, .quiz-container, .knowledge-check, input, select, textarea, .no-print { display: none !important; }
a { color: #075985; text-decoration: none; }
pre, code { white-space: pre-wrap; word-break: break-word; }
"""

LEGAL = "© 2026 ImpactMojo · For the personal use of the purchaser · Not for redistribution"


def query(sql):
    body = json.dumps({"query": sql})
    out = subprocess.run(
        ["curl", "-s", "-X", "POST", "-H", "Authorization: Bearer %s" % os.environ["SUPABASE_PAT"],
         "-H", "Content-Type: application/json",
         "https://api.supabase.com/v1/projects/%s/database/query" % PROJECT, "-d", body],
        capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def shell_css():
    """The flagship shell's own component rules, so callouts and tables look as they do online."""
    s = (ROOT / "courses" / "mel" / "index.html").read_text(encoding="utf-8")
    blocks = re.findall(r"<style[^>]*>(.*?)</style>", s, re.S)
    comp = (ROOT / "css" / "course-components.css").read_text(encoding="utf-8")
    return comp + "\n" + "\n".join(blocks)


def clean(h):
    # Interactive blocks and scripts never reach paper.
    h = re.sub(r"<script\b.*?</script>", "", h, flags=re.S | re.I)
    h = re.sub(r"<button\b.*?</button>", "", h, flags=re.S | re.I)
    # Site-relative assets resolve against the live site when printed.
    h = re.sub(r'(src|href)="/(?!/)', r'\1="https://www.impactmojo.in/', h)
    return h


def plain(t):
    return re.sub(r"[^a-z0-9]+", "", html.unescape(re.sub(r"<[^>]+>", "", t or "")).lower())


def bare_title(t):
    """'Module 3: Indicator Design' -> 'Indicator Design'."""
    return re.sub(r"^\s*module\s+\d+\s*[:.\-]\s*", "", t or "", flags=re.I).strip()


def drop_repeated_heading(h, title, n):
    """Remove the content's own opening heading when it only repeats the module title."""
    want = {plain(title), plain("Module %d: %s" % (n, title)), plain("Module %d %s" % (n, title))}
    m = re.search(r"<h([1-3])\b[^>]*>(.*?)</h\1>", h[:1500], re.S | re.I)
    if m and plain(m.group(2)) in want:
        return h[:m.start()] + h[m.end():]
    return h


def build(course_id, out_dir, css):
    stem, title, track = COURSES[course_id]
    rows = query("select module_number, module_title, module_intro, content_html from course_content "
                 "where course_id = '%s' order by module_number" % course_id.replace("'", "''"))
    if not rows:
        raise SystemExit("no modules for %s" % course_id)
    toc = "".join("<li>%s</li>" % html.escape(bare_title(r["module_title"]) or "Module %d" % r["module_number"]) for r in rows)
    mods = []
    for r in rows:
        intro = ('<p class="module-intro">%s</p>' % html.escape(r["module_intro"])) if r.get("module_intro") else ""
        t = bare_title(r["module_title"])
        body = drop_repeated_heading(clean(r["content_html"] or ""), t, r["module_number"])
        mods.append('<section class="notes-module"><h2 class="module-title">Module %d: %s</h2>%s%s</section>'
                    % (r["module_number"], html.escape(t), intro, body))
    doc = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>{title}: ImpactMojo Course Notes</title>
<meta name="author" content="ImpactMojo">
<style>{css}</style><style>{pcss}</style></head><body>
<section class="notes-cover"><div class="brand">IMPACTMOJO · IMPACTMOJO.IN</div>
<div class="track">{track}</div><h1>{title}</h1><div class="kind">Course Notes</div>
<div class="meta">{n} modules · Flagship course</div>
<p class="blurb">The printable companion to the ImpactMojo flagship course. Every module's core ideas, diagrams, worked examples, key readings and reflection prompts are in one document you can keep, annotate and work through offline.</p>
<div class="legal">{legal}</div></section>
<section class="notes-toc"><h2>Contents</h2><ol>{toc}</ol></section>
{mods}
</body></html>""".format(title=html.escape(title), css=css, pcss=PRINT_CSS, track=html.escape(track),
                         n=len(rows), legal=LEGAL, toc=toc, mods="\n".join(mods))
    path = Path(out_dir) / ("%s.html" % stem)
    path.write_text(doc, encoding="utf-8")
    return path, title, len(rows)


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    ids = sys.argv[2:] or list(COURSES)
    css = shell_css()
    manifest = []
    for cid in ids:
        p, title, n = build(cid, out, css)
        manifest.append({"course_id": cid, "html": str(p), "title": title, "modules": n,
                         "pdf": "ImpactMojo-Notes-%s.pdf" % COURSES[cid][0]})
        print("built %s (%d modules)" % (p.name, n))
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
