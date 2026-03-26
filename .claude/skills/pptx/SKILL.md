---
description: "Create and edit PowerPoint presentations (.pptx) from course content, workshop plans, or plain language descriptions. Use when the user asks to generate slides, create a presentation, build a deck, or export course content as PPTX. Complements the Gamma API skill for generating 101 Course Decks."
---

# PPTX Skill — ImpactMojo

Create branded PowerPoint presentations from ImpactMojo course content, workshop outlines, or plain language descriptions.

## Setup

```bash
pip install python-pptx Pillow
```

## Design Standards

### Avoid "AI Slop" Slides
- No walls of bullet points
- No generic blue/gray color schemes
- No clip art or stock photo placeholders
- No identical layouts repeated across all slides

### ImpactMojo Slide Design Principles

**Color strategy**: Match the learning track's folk art color:
| Track | Primary Color | Art Style |
|-------|--------------|-----------|
| MEL & Research | `#3182ce` | Warli |
| Data & Technology | `#38a169` | Gond |
| Policy & Economics | `#d69e2e` | Kalamkari |
| Gender & Equity | `#d53f8c` | Madhubani |
| Health & Communication | `#e53e3e` | Pattachitra |
| Philosophy & Governance | `#805ad5` | Pichwai |

**Layout variety**: Rotate between these layouts:
1. **Title + subtitle** (opening)
2. **Big stat + context** (data points)
3. **Two-column** (comparison, before/after)
4. **Image + text** (case study, example)
5. **Grid of 3-4 cards** (key concepts)
6. **Quote + attribution** (key takeaway)
7. **Timeline / process flow** (sequences)

**Typography**:
- Title slides: 36-44pt, bold
- Section headers: 28-32pt
- Body text: 18-22pt
- Never below 16pt
- Use Inter for headings, system fonts for body

**Visual requirement**: Every slide needs at least one visual element — a shape, chart, icon, or colored block. Text-only slides are forgettable.

## Creating Presentations

### From Course Content

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

prs = Presentation()
prs.slide_width = Inches(13.33)  # 16:9 widescreen
prs.slide_height = Inches(7.5)

# Title slide
slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
txBox = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(11), Inches(3))
tf = txBox.text_frame
p = tf.add_paragraph()
p.text = "MEL for Development"
p.font.size = Pt(44)
p.font.bold = True
p.font.color.rgb = RGBColor(0x31, 0x82, 0xce)  # Track color
p.alignment = PP_ALIGN.LEFT

# Subtitle
p2 = tf.add_paragraph()
p2.text = "Module 1: What is Monitoring, Evaluation & Learning?"
p2.font.size = Pt(22)
p2.font.color.rgb = RGBColor(0x71, 0x80, 0x96)

# Add ImpactMojo footer
add_footer(slide, "ImpactMojo — impactmojo.in")

prs.save("mel-module-1.pptx")
```

### Slide Templates

#### Big Stat Slide
```python
def add_stat_slide(prs, stat, label, context):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    # Big number
    txBox = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(11), Inches(2.5))
    p = txBox.text_frame.add_paragraph()
    p.text = stat  # e.g., "73%"
    p.font.size = Pt(96)
    p.font.bold = True
    p.font.color.rgb = RGBColor(0x66, 0x7e, 0xea)
    # Label
    p2 = txBox.text_frame.add_paragraph()
    p2.text = label  # e.g., "of Indian NGOs lack formal M&E frameworks"
    p2.font.size = Pt(24)
    # Context
    p3 = txBox.text_frame.add_paragraph()
    p3.text = context
    p3.font.size = Pt(16)
    p3.font.color.rgb = RGBColor(0x71, 0x80, 0x96)
```

#### Two-Column Comparison
```python
def add_comparison_slide(prs, title, left_title, left_items, right_title, right_items):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    # Title
    txBox = slide.shapes.add_textbox(Inches(1), Inches(0.5), Inches(11), Inches(1))
    p = txBox.text_frame.add_paragraph()
    p.text = title
    p.font.size = Pt(32)
    p.font.bold = True
    # Left column
    left = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(5), Inches(4.5))
    # Right column
    right = slide.shapes.add_textbox(Inches(7), Inches(2), Inches(5), Inches(4.5))
    # ... populate columns
```

## ImpactMojo Use Cases

### 101 Course Decks
Generate the remaining 16 foundational course decks (complementing Gamma):
- ~60 slides per deck
- Indian folk art illustration style matching the track
- Each slide: concept → example → reflection

### Workshop Slide Packs
Generate slide decks for the 3-day workshop programme:
- Day 1: MEL Essentials (20 slides)
- Day 2: Data & Methods (25 slides)
- Day 3: Applied Practice (15 slides)

### Pitch Decks
Generate partnership/funder presentations showing platform impact metrics.

### Course Summary Decks
Condense a 13-module flagship course into a 15-slide summary deck.

## Quality Checklist

- [ ] No text below 16pt
- [ ] Every slide has a visual element
- [ ] No more than 2 consecutive same-layout slides
- [ ] Track color applied consistently
- [ ] ImpactMojo footer on every slide
- [ ] 16:9 aspect ratio
- [ ] Spelling/grammar checked
- [ ] South Asian examples used (not Western defaults)

## Output

Save to `/exports/` or deliver to user. Typical output: `{course-slug}-deck.pptx`.
