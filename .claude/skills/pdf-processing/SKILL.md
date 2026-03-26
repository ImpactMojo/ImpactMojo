---
description: "Read, extract, create, merge, split, and manipulate PDF files. Use when the user asks to generate handout packs, extract tables from reports, create PDF exports, merge BookSummary chapters, fill forms, or work with any PDF content."
---

# PDF Processing Skill

Comprehensive PDF manipulation for ImpactMojo content — handout packs, course exports, report generation, and data extraction.

## Setup

Install required Python libraries (run once):
```bash
pip install pdfplumber reportlab pypdf Pillow
```

## Capabilities

### 1. Extract Text & Tables

Use `pdfplumber` to extract text preserving layout and convert tables to structured data:

```python
import pdfplumber

with pdfplumber.open("report.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        tables = page.extract_tables()
        for table in tables:
            # Each table is a list of rows, each row a list of cells
            for row in table:
                print(row)
```

### 2. Create PDFs from Scratch

Use `reportlab` to generate branded ImpactMojo PDFs:

```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor

# ImpactMojo brand colors
PRIMARY = HexColor('#667eea')
TEXT = HexColor('#2d3748')
MUTED = HexColor('#718096')

doc = SimpleDocTemplate("output.pdf", pagesize=A4,
    leftMargin=1*inch, rightMargin=1*inch,
    topMargin=1*inch, bottomMargin=1*inch)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    'ImpactMojoTitle',
    parent=styles['Title'],
    fontName='Helvetica-Bold',
    fontSize=24,
    textColor=PRIMARY,
    spaceAfter=20
))
styles.add(ParagraphStyle(
    'ImpactMojoBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=11,
    textColor=TEXT,
    leading=16,
    spaceAfter=8
))
```

**Important**: Avoid Unicode subscript/superscript characters in ReportLab — built-in fonts render them as black boxes. Use `<sub>` and `<super>` XML tags instead.

### 3. Merge PDFs

Combine multiple handouts or chapters into a single pack:

```python
from pypdf import PdfMerger

merger = PdfMerger()
merger.append("handout-1.pdf")
merger.append("handout-2.pdf")
merger.append("handout-3.pdf")
merger.write("handout-pack.pdf")
merger.close()
```

### 4. Split PDFs

Extract specific pages:

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("full-document.pdf")
writer = PdfWriter()

# Extract pages 3-7
for page_num in range(2, 7):
    writer.add_page(reader.pages[page_num])

writer.write("excerpt.pdf")
```

### 5. HTML to PDF (Handouts)

Convert ImpactMojo HTML handouts to PDF using browser print:

```python
import subprocess

# Using wkhtmltopdf (if available)
subprocess.run([
    'wkhtmltopdf',
    '--page-size', 'A4',
    '--margin-top', '15mm',
    '--margin-bottom', '15mm',
    '--margin-left', '15mm',
    '--margin-right', '15mm',
    'Handouts/MEL/handout-1.html',
    'output/mel-handout-1.pdf'
])
```

Alternative: Use Puppeteer (already in package.json):
```javascript
const puppeteer = require('puppeteer');
const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto('file:///path/to/handout.html');
await page.pdf({ path: 'output.pdf', format: 'A4', printBackground: true });
await browser.close();
```

## ImpactMojo Use Cases

### Handout Packs
Generate track-specific PDF packs by merging handouts:
```
/Handouts/MEL Track/*.html → mel-track-pack.pdf
/Handouts/Gender Equity Track/*.html → gender-track-pack.pdf
```

### Course Export
Generate a complete course as a single PDF — all 13 modules + lexicon.

### BookSummary Chapters
Extract individual chapters from BookSummaries for offline reading.

### Workshop Materials
Combine selected handouts + game instructions + lab guides into a workshop-ready pack.

## Output Location

Place generated PDFs in `/exports/` or deliver directly to user. Never commit large PDFs to the repo.
