#!/usr/bin/env python3
"""
pdf-to-slides.py — Convert Gamma PDF exports to self-hosted HTML slide decks
with ImpactMojo branding (Inter, Amaranth, JetBrains Mono, sepia folk art).

Usage:
  python3 scripts/pdf-to-slides.py                    # Convert all PDFs in /tmp/gamma-pdfs/
  python3 scripts/pdf-to-slides.py --slug data-lit     # Convert one deck
  python3 scripts/pdf-to-slides.py --dry-run           # Preview without writing
"""

import json, os, re, sys, html
from PyPDF2 import PdfReader

# ─── Config ─────────────────────────────────────────────────────────────────

PDF_DIR = "/tmp/gamma-pdfs"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "101-courses")
RESULTS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "gamma-sync-results.json")

# Category → folk art style for CSS decorative borders
CATEGORY_STYLES = {
    "MEL & Research": {"art": "Warli", "border_color": "#8B4513", "accent": "#A0522D"},
    "Data & Technology": {"art": "Gond", "border_color": "#2F4F4F", "accent": "#556B2F"},
    "Policy & Economics": {"art": "Kalamkari", "border_color": "#800020", "accent": "#8B0000"},
    "Gender & Equity": {"art": "Madhubani", "border_color": "#B22222", "accent": "#DC143C"},
    "Health & Communication": {"art": "Pattachitra", "border_color": "#DAA520", "accent": "#B8860B"},
    "Philosophy & Governance": {"art": "Pichwai", "border_color": "#006400", "accent": "#228B22"},
}

# Course metadata from gamma-sync.js (slug → {title, category})
COURSE_META = {
    "mel-basics": {"title": "MEAL 101", "category": "MEL & Research"},
    "research-ethics": {"title": "Research Ethics 101", "category": "MEL & Research"},
    "visual-eth": {"title": "Visual Ethnography 101", "category": "MEL & Research"},
    "qual-methods": {"title": "Qualitative Research Methods 101", "category": "MEL & Research"},
    "obs2insight": {"title": "Getting to Insights from Field Observations 101", "category": "MEL & Research"},
    "toc-workbench": {"title": "Theory of Change Workbench 101", "category": "MEL & Research"},
    "eng-dev": {"title": "English for Development Professionals 101", "category": "MEL & Research"},
    "data-lit": {"title": "Data Literacy 101", "category": "Data & Technology"},
    "data-feminism": {"title": "Data Feminism 101", "category": "Data & Technology"},
    "eda-hhs": {"title": "Exploratory Data Analysis for Household Surveys 101", "category": "Data & Technology"},
    "bi-analysis": {"title": "Bivariate Analysis 101", "category": "Data & Technology"},
    "multivariate-basics": {"title": "Multivariate Analysis 101", "category": "Data & Technology"},
    "irt-basics": {"title": "Item Response Theory 101", "category": "Data & Technology"},
    "econometrics-101": {"title": "Econometrics 101", "category": "Data & Technology"},
    "digital-ethics": {"title": "Digital Ethics 101", "category": "Data & Technology"},
    "climate-essentials": {"title": "Climate Essentials 101", "category": "Policy & Economics"},
    "dev-economics": {"title": "Development Economics 101", "category": "Policy & Economics"},
    "pol-economy": {"title": "Political Economy 101", "category": "Policy & Economics"},
    "cost-effectiveness": {"title": "Cost-Effectiveness Analysis 101", "category": "Policy & Economics"},
    "livelihood-basics": {"title": "Livelihoods 101", "category": "Policy & Economics"},
    "advocacy-basics": {"title": "Advocacy Basics 101", "category": "Policy & Economics"},
    "fundraising-basics": {"title": "Fundraising Basics 101", "category": "Policy & Economics"},
    "post-truth-101": {"title": "Post-Truth Politics 101", "category": "Policy & Economics"},
    "dev-architecture": {"title": "Global Development Governance 101", "category": "Policy & Economics"},
    "edu-pedagogy": {"title": "Education and Pedagogy 101", "category": "Health & Communication"},
    "SRHR-basics": {"title": "Sexual and Reproductive Health and Rights 101", "category": "Health & Communication"},
    "pub-health-basics": {"title": "Public Health 101", "category": "Health & Communication"},
    "bcc-comms": {"title": "Behaviour Change Communications 101", "category": "Health & Communication"},
    "wee-studies": {"title": "Women's Economic Empowerment 101", "category": "Gender & Equity"},
    "social-margins": {"title": "Marginalised Identities 101", "category": "Gender & Equity"},
    "decent-work": {"title": "Decent Work For All 101", "category": "Gender & Equity"},
    "care-economy-101": {"title": "Care Economy 101", "category": "Gender & Equity"},
    "sel-basics": {"title": "Social and Emotional Learning 101", "category": "Gender & Equity"},
    "ind-constitution": {"title": "Indian Constitution 101", "category": "Philosophy & Governance"},
    "inequality-basics": {"title": "Poverty and Inequality 101", "category": "Philosophy & Governance"},
    "decolonize-dev": {"title": "Decolonial Development 101", "category": "Philosophy & Governance"},
    "community-dev": {"title": "Community Development 101", "category": "Philosophy & Governance"},
    "env-justice": {"title": "Environmental Justice 101", "category": "Philosophy & Governance"},
}


# ─── PDF Text Cleaning ──────────────────────────────────────────────────────

def fix_pdf_text(text):
    """Fix common PDF extraction artifacts."""
    # Fix split characters (e.g., "W hat" → "What", "m ake" → "make")
    # This happens when PDF has character spacing
    text = re.sub(r'(?<=[A-Z])\s(?=[a-z])', '', text)  # "W hat" → "What"
    text = re.sub(r'(?<=[a-z])\s(?=[a-z]{2,})', '', text)  # "m ake" → "make" but preserve real spaces
    # More targeted fixes for common patterns
    text = re.sub(r'\bm\s([aeiou])', r'm\1', text)  # "m ake" → "make"
    text = re.sub(r'\bp\s([aeiou])', r'p\1', text)  # "p olicy" → "policy"
    text = re.sub(r'\bf\s([aeiou])', r'f\1', text)  # "f or" → "for"
    text = re.sub(r'\bs\s([aeiou])', r's\1', text)  # "s urvey" → "survey"
    text = re.sub(r'\bt\s([aeiou])', r't\1', text)  # "t ool" → "tool"
    text = re.sub(r'\bd\s([aeiou])', r'd\1', text)  # "d ata" → "data"
    text = re.sub(r'\bl\s([aeiou])', r'l\1', text)  # "l earn" → "learn"
    text = re.sub(r'\br\s([aeiou])', r'r\1', text)  # "r esearch" → "research"
    text = re.sub(r'\bn\s([aeiou])', r'n\1', text)  # "n ot" → "not"
    text = re.sub(r'\bg\s([aeiou])', r'g\1', text)  # "g oals" → "goals"
    text = re.sub(r'\bw\s([aeiou])', r'w\1', text)  # "w ork" → "work"
    text = re.sub(r'\bc\s([aeiou])', r'c\1', text)  # "c ase" → "case"
    text = re.sub(r'\bh\s([aeiou])', r'h\1', text)  # "h ealth" → "health"
    # Fix double spaces
    text = re.sub(r'  +', ' ', text)
    return text.strip()


# ─── PDF Parsing ─────────────────────────────────────────────────────────────

def parse_pdf(pdf_path):
    """Parse a Gamma PDF into structured slides."""
    reader = PdfReader(pdf_path)
    slides = []

    for i, page in enumerate(reader.pages):
        raw = page.extract_text() or ""
        raw = fix_pdf_text(raw)

        lines = [l.strip() for l in raw.split('\n') if l.strip()]

        # Remove footer artifacts
        cleaned = []
        for line in lines:
            if re.match(r'^\d{1,2}$', line):  # bare slide number
                continue
            if 'CC BY-NC-SA' in line:
                continue
            if line in ('www.impactmojo.in', 'www.im pactm ojo.in', 'www.impactmojo.in'):
                continue
            cleaned.append(line)

        slides.append({
            'number': i + 1,
            'lines': cleaned,
        })

    return slides


def classify_slide(slide, total_slides):
    """Classify slide type based on content heuristics."""
    lines = slide['lines']
    num = slide['number']

    if not lines:
        return 'blank'

    text = ' '.join(lines).lower()
    first = lines[0] if lines else ''

    # Title slide (first slide)
    if num == 1:
        return 'title'

    # Agenda/TOC slide (slide 2, or contains "what we'll cover" / "agenda")
    if num == 2 or 'what we' in text[:50].lower() or 'agenda' in text[:30].lower():
        if num <= 3:
            return 'agenda'

    # Learning objectives
    if 'learning objective' in text[:50].lower():
        return 'objectives'

    # Section separator (short slides with "SECTION" or just 2-3 short lines)
    if re.match(r'^SECTION\s+\d', first, re.IGNORECASE):
        return 'section'
    if len(lines) <= 3 and len(' '.join(lines)) < 80:
        return 'section'

    # Quiz slide
    if 'quiz' in text[:30].lower() or 'test your' in text[:40].lower():
        return 'quiz'

    # Key takeaways
    if 'key takeaway' in text[:40].lower():
        return 'takeaways'

    # Glossary
    if 'glossary' in text[:30].lower():
        return 'glossary'

    # Further reading
    if 'further reading' in text[:40].lower() or 'recommended' in text[:40].lower():
        return 'reading'

    # Thank you (last 2 slides)
    if num >= total_slides - 1 and ('thank you' in text.lower() or 'keep exploring' in text.lower()):
        return 'thankyou'

    return 'content'


def lines_to_html(lines, slide_type):
    """Convert raw lines to structured HTML based on slide type."""
    if not lines:
        return ''

    if slide_type == 'title':
        parts = []
        if lines:
            parts.append(f'<p class="category-badge">{html.escape(lines[0])}</p>')
        if len(lines) > 1:
            parts.append(f'<h1>{html.escape(lines[1])}</h1>')
        subtitle_lines = [html.escape(l) for l in lines[2:]]
        if subtitle_lines:
            parts.append(f'<p class="subtitle">{" ".join(subtitle_lines)}</p>')
        return '\n'.join(parts)

    if slide_type == 'section':
        parts = []
        for line in lines:
            if re.match(r'^SECTION\s+\d', line, re.IGNORECASE):
                parts.append(f'<p class="section-number">{html.escape(line)}</p>')
            else:
                parts.append(f'<h2>{html.escape(line)}</h2>')
        return '\n'.join(parts)

    if slide_type == 'thankyou':
        parts = ['<h2>Thank You for Learning with ImpactMojo</h2>',
                  '<p class="subtitle">Keep exploring. Keep questioning. Keep building.</p>',
                  '<div class="thankyou-info">',
                  '<p>hello@impactmojo.in</p>',
                  '<p>www.impactmojo.in</p>',
                  '<p>CC BY-NC-SA 4.0</p>',
                  '</div>']
        return '\n'.join(parts)

    # General content slides: first line is heading, rest is body
    parts = []
    if lines:
        parts.append(f'<h2>{html.escape(lines[0])}</h2>')

    body_lines = lines[1:]
    if not body_lines:
        return '\n'.join(parts)

    # Try to detect bullet points vs paragraphs
    in_list = False
    for line in body_lines:
        escaped = html.escape(line)

        # Numbered items (e.g., "1Define & Classify" or "01 What Is Data")
        num_match = re.match(r'^(\d{1,2})\s*([A-Z])', line)
        if num_match:
            if not in_list:
                parts.append('<ul>')
                in_list = True
            parts.append(f'<li><strong>{escaped}</strong></li>')
            continue

        # Bullet-like lines (start with dash, bullet, or are short descriptors after numbered items)
        if line.startswith(('- ', '• ', '→ ', '▸ ', '◆ ')):
            if not in_list:
                parts.append('<ul>')
                in_list = True
            parts.append(f'<li>{html.escape(line[2:])}</li>')
            continue

        # Close list if we were in one
        if in_list:
            parts.append('</ul>')
            in_list = False

        # Check for key-value patterns (e.g., "Term: Definition" or bold headers)
        kv_match = re.match(r'^([A-Z][^:]{2,30}):\s*(.+)', line)
        if kv_match:
            parts.append(f'<p><strong>{html.escape(kv_match.group(1))}:</strong> {html.escape(kv_match.group(2))}</p>')
            continue

        # Check for quoted text
        if line.startswith('"') or line.startswith('\u201c'):
            parts.append(f'<blockquote>{escaped}</blockquote>')
            continue

        # Regular paragraph
        parts.append(f'<p>{escaped}</p>')

    if in_list:
        parts.append('</ul>')

    return '\n'.join(parts)


# ─── HTML Template ───────────────────────────────────────────────────────────

def build_html(slug, title, category, slides_html, total_slides):
    """Generate a self-contained HTML slideshow file."""
    style = CATEGORY_STYLES.get(category, CATEGORY_STYLES["MEL & Research"])
    border_color = style["border_color"]
    accent = style["accent"]
    art_name = style["art"]

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)} | ImpactMojo</title>
<meta name="description" content="{html.escape(title)} — Free development education course from ImpactMojo.">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Amaranth:wght@400;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
  --brand-primary: #0EA5E9;
  --brand-accent: {accent};
  --border-art: {border_color};
  --bg-slide: #FFFDF7;
  --bg-section: {border_color};
  --text-primary: #1a1a1a;
  --text-secondary: #4a4a4a;
  --text-muted: #777;
  --sepia-bg: #F5E6D0;
  --sepia-dark: #3E2723;
}}

html, body {{ height: 100%; overflow: hidden; background: #111; }}

/* ─── Slide Container ─────────────────────────────────────────── */
.deck {{
  position: relative;
  width: 100vw;
  height: 100vh;
}}

.slide {{
  position: absolute;
  inset: 0;
  display: none;
  flex-direction: column;
  justify-content: center;
  padding: 4rem 6rem;
  background: var(--bg-slide);
  color: var(--text-primary);
  overflow-y: auto;
  border: 6px solid var(--border-art);
  border-image: repeating-linear-gradient(
    45deg,
    var(--border-art) 0px,
    var(--border-art) 4px,
    transparent 4px,
    transparent 8px,
    var(--brand-accent) 8px,
    var(--brand-accent) 12px,
    transparent 12px,
    transparent 16px
  ) 6;
}}

.slide.active {{ display: flex; }}

/* ─── Typography ──────────────────────────────────────────────── */
h1, h2, h3 {{
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  line-height: 1.2;
  color: var(--text-primary);
}}

h1 {{ font-size: 2.8rem; margin-bottom: 0.5rem; }}
h2 {{ font-size: 2rem; margin-bottom: 1rem; color: var(--border-art); }}
h3 {{ font-size: 1.4rem; margin-bottom: 0.5rem; }}

p, li, blockquote, td {{
  font-family: 'Amaranth', sans-serif;
  font-size: 1.15rem;
  line-height: 1.7;
  color: var(--text-secondary);
}}

code, pre {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.95rem;
  background: #f0ebe3;
  padding: 0.15em 0.4em;
  border-radius: 3px;
}}

strong {{ color: var(--text-primary); }}

ul {{
  margin: 0.8rem 0 0.8rem 1.5rem;
  list-style: none;
}}

ul li {{
  position: relative;
  padding-left: 1.2rem;
  margin-bottom: 0.5rem;
}}

ul li::before {{
  content: '▸';
  position: absolute;
  left: 0;
  color: var(--brand-accent);
  font-weight: bold;
}}

blockquote {{
  border-left: 4px solid var(--border-art);
  padding: 0.8rem 1.2rem;
  margin: 1rem 0;
  background: rgba(0,0,0,0.03);
  font-style: italic;
  color: var(--text-muted);
}}

.subtitle {{
  font-size: 1.3rem;
  color: var(--text-muted);
  margin-top: 0.3rem;
}}

.category-badge {{
  display: inline-block;
  background: var(--border-art);
  color: #fff;
  font-family: 'Inter', sans-serif;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 0.3rem 0.8rem;
  border-radius: 4px;
  margin-bottom: 1rem;
}}

.section-number {{
  font-family: 'Inter', sans-serif;
  font-size: 1rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--text-muted);
  margin-bottom: 0.5rem;
}}

/* ─── Slide Types ─────────────────────────────────────────────── */
.slide--title {{
  text-align: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--sepia-bg) 0%, var(--bg-slide) 100%);
}}

.slide--title h1 {{ font-size: 3.2rem; }}

.slide--section {{
  text-align: center;
  justify-content: center;
  background: var(--bg-section);
  color: #fff;
}}

.slide--section h2 {{ color: #fff; font-size: 2.6rem; }}
.slide--section .section-number {{ color: rgba(255,255,255,0.7); }}

.slide--thankyou {{
  text-align: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--sepia-bg) 0%, var(--bg-slide) 100%);
}}

.slide--thankyou h2 {{ color: var(--border-art); font-size: 2.4rem; margin-bottom: 0.5rem; }}

.thankyou-info {{
  margin-top: 2rem;
  font-family: 'Amaranth', sans-serif;
  color: var(--text-muted);
}}

.thankyou-info p {{ margin: 0.3rem 0; }}

/* ─── Footer ──────────────────────────────────────────────────── */
.slide-footer {{
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.6rem 2rem;
  font-family: 'Inter', sans-serif;
  font-size: 0.75rem;
  color: var(--text-muted);
  background: rgba(255,253,247,0.95);
  border-top: 1px solid #e8e0d4;
}}

/* ─── Navigation ──────────────────────────────────────────────── */
.nav-controls {{
  position: fixed;
  bottom: 2.5rem;
  right: 2rem;
  display: flex;
  gap: 0.5rem;
  z-index: 100;
}}

.nav-btn {{
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: 2px solid var(--border-art);
  background: var(--bg-slide);
  color: var(--border-art);
  font-size: 1.2rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  font-family: 'Inter', sans-serif;
}}

.nav-btn:hover {{ background: var(--border-art); color: #fff; }}

.progress-bar {{
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: var(--border-art);
  transition: width 0.3s ease;
  z-index: 100;
}}

/* ─── Responsive ──────────────────────────────────────────────── */
@media (max-width: 768px) {{
  .slide {{ padding: 2rem 1.5rem 3rem; }}
  h1 {{ font-size: 2rem; }}
  .slide--title h1 {{ font-size: 2.2rem; }}
  h2 {{ font-size: 1.5rem; }}
  p, li {{ font-size: 1rem; }}
  .nav-controls {{ bottom: 1rem; right: 1rem; }}
}}

@media print {{
  .slide {{ page-break-after: always; display: flex !important; position: relative; height: 100vh; }}
  .nav-controls, .progress-bar {{ display: none; }}
}}
</style>
</head>
<body>

<div class="progress-bar" id="progress"></div>

<div class="deck" id="deck">
{slides_html}
</div>

<div class="nav-controls">
  <button class="nav-btn" onclick="prev()" aria-label="Previous slide">&#8592;</button>
  <button class="nav-btn" onclick="next()" aria-label="Next slide">&#8594;</button>
</div>

<script>
(function() {{
  'use strict';
  var current = 0;
  var slides = document.querySelectorAll('.slide');
  var total = slides.length;
  var progress = document.getElementById('progress');

  function show(n) {{
    if (n < 0 || n >= total) return;
    slides[current].classList.remove('active');
    current = n;
    slides[current].classList.add('active');
    progress.style.width = ((current + 1) / total * 100) + '%';
  }}

  window.next = function() {{ show(current + 1); }};
  window.prev = function() {{ show(current - 1); }};

  document.addEventListener('keydown', function(e) {{
    if (e.key === 'ArrowRight' || e.key === ' ') {{ e.preventDefault(); show(current + 1); }}
    if (e.key === 'ArrowLeft') {{ e.preventDefault(); show(current - 1); }}
    if (e.key === 'Home') {{ e.preventDefault(); show(0); }}
    if (e.key === 'End') {{ e.preventDefault(); show(total - 1); }}
  }});

  // Touch support
  var touchX = 0;
  document.addEventListener('touchstart', function(e) {{ touchX = e.changedTouches[0].screenX; }});
  document.addEventListener('touchend', function(e) {{
    var dx = e.changedTouches[0].screenX - touchX;
    if (Math.abs(dx) > 50) {{ dx > 0 ? show(current - 1) : show(current + 1); }}
  }});

  show(0);
}})();
</script>
</body>
</html>'''


# ─── Main ────────────────────────────────────────────────────────────────────

def convert_deck(slug, dry_run=False):
    """Convert a single PDF to an HTML slideshow."""
    pdf_path = os.path.join(PDF_DIR, f"{slug}.pdf")
    if not os.path.exists(pdf_path):
        print(f"  SKIP: {pdf_path} not found")
        return False

    if os.path.getsize(pdf_path) < 1000:
        print(f"  SKIP: {pdf_path} too small ({os.path.getsize(pdf_path)} bytes)")
        return False

    meta = COURSE_META.get(slug, {"title": slug.replace('-', ' ').title() + " 101", "category": "MEL & Research"})
    title = meta["title"]
    category = meta["category"]

    print(f"  Parsing: {slug} ({title})")
    slides = parse_pdf(pdf_path)
    total = len(slides)

    # Build slide HTML
    slides_parts = []
    for slide in slides:
        stype = classify_slide(slide, total)
        content_html = lines_to_html(slide['lines'], stype)

        type_class = f"slide--{stype}" if stype in ('title', 'section', 'thankyou') else ''

        footer = f'''<div class="slide-footer">
  <span>{slide['number']} / {total}</span>
  <span>www.impactmojo.in</span>
  <span>CC BY-NC-SA 4.0</span>
</div>'''

        slides_parts.append(
            f'<div class="slide {type_class}" data-slide="{slide["number"]}">\n'
            f'<div class="slide-content">\n{content_html}\n</div>\n'
            f'{footer}\n</div>'
        )

    slides_html = '\n\n'.join(slides_parts)
    full_html = build_html(slug, title, category, slides_html, total)

    if dry_run:
        print(f"  DRY RUN: would write {len(full_html)} bytes, {total} slides")
        return True

    out_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    size_kb = len(full_html) / 1024
    print(f"  Written: {out_path} ({size_kb:.0f}KB, {total} slides)")
    return True


def main():
    args = sys.argv[1:]
    dry_run = '--dry-run' in args

    slug_idx = None
    for i, a in enumerate(args):
        if a == '--slug' and i + 1 < len(args):
            slug_idx = args[i + 1]

    if slug_idx:
        slugs = [slug_idx]
    else:
        # All PDFs in the directory
        slugs = sorted([
            f.replace('.pdf', '')
            for f in os.listdir(PDF_DIR)
            if f.endswith('.pdf')
        ])

    print(f"\nImpactMojo PDF → HTML Converter")
    print(f"  Decks: {len(slugs)}")
    print(f"  Output: {OUTPUT_DIR}")
    print(f"  Mode: {'DRY RUN' if dry_run else 'LIVE'}\n")

    success = 0
    for slug in slugs:
        ok = convert_deck(slug, dry_run)
        if ok:
            success += 1

    print(f"\nDone: {success}/{len(slugs)} converted")


if __name__ == "__main__":
    main()
