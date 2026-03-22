# Content Guide

This page documents how educational content is structured in ImpactMojo, for contributors who want to add or improve courses, labs, games, and resources.

## Content Types

| Type | Count | Format | Access |
|------|-------|--------|--------|
| Flagship Courses | 9 | Multi-module (12–13 modules each) | Free |
| Foundational Courses | 39 | Single-page or multi-section | Free |
| Interactive Labs | 19 | HTML/JS workbenches | Free |
| Learning Games | 16 | HTML/JS simulations | Free |
| Premium Tools | 9 | Separate Netlify sites | Paid tiers |
| ImpactLex | 500+ terms | PWA dictionary | Free |
| Dev Case Studies | 200 | Curated library | Free |
| DevDiscourses | 500+ | Curated papers/books | Free |
| Handouts | 400+ | HTML pages | Free |
| BookSummaries | 3 | Interactive book companions | Free (Specials) |
| 101 Course Decks | 23 | Visual Gamma presentations | Free |
| Blog posts | Ongoing | HTML articles | Free |
| Podcast | Episodes | Audio (Spotify) | Free |

## Learning Tracks

Content is organized into 6 tracks:

1. **MEL & Research** — Monitoring, evaluation, qualitative/quantitative methods
2. **Economics & Policy** — Development economics, political economy, fundraising
3. **Gender & Equity** — Gender studies, WEE, care economy, data feminism
4. **Governance & Society** — Constitution, decolonization, community development
5. **Health & Wellbeing** — Public health, climate, SEL, livelihoods
6. **Communication & Data** — Data literacy, visual ethnography, BCC, advocacy

## Flagship Course Structure

Each flagship course follows a consistent structure:

- **13 modules** (approximately)
- **Lexicon** of 50–65 key terms
- **South Asian context** — examples from India, Bangladesh, Nepal, Sri Lanka
- **Case studies** — real development programs and evaluations
- **Reflection prompts** — for practitioners to connect to their work
- **Further reading** — curated from DevDiscourses

### Example: MEL for Development
```
Module 1:  What is MEL?
Module 2:  Theories of Change
Module 3:  Indicators & Frameworks
Module 4:  Data Collection Methods
...
Module 13: MEL for Learning & Adaptation
Lexicon:   65 terms with definitions
```

## Interactive Labs

Labs are HTML/JS workbenches that let practitioners apply concepts. Each lab:

- Has a guided workflow (step-by-step)
- Produces an output (framework, plan, analysis)
- Can export results (PDF/PNG in premium versions)
- Requires no server — runs entirely in the browser

## Learning Games

Games are economics simulations built as single HTML pages:

- **Self-contained** — each game is one HTML file
- **Data-driven** — real economic parameters where possible
- **Debriefable** — designed for classroom or workshop use
- **Mobile-friendly** — responsive layouts

## Adding New Content

### Adding a new foundational course

1. Create a new HTML file following the existing course pattern
2. Add the course to the catalog in `catalog.html`
3. Add it to the main site's course listing in `index.html`
4. Update the README content inventory

### Adding a new game

1. Create a single HTML file with the game logic
2. Host it in the appropriate directory or as a separate Netlify site
3. Add it to the games section in `index.html` and `catalog.html`

### Adding handouts

Handouts are loaded dynamically from the repo. Add HTML files to the handouts collection and they will appear automatically.

## Multilingual Content

Content is available in 6 languages:
- English (primary)
- Hindi
- Tamil
- Bengali
- Telugu
- Marathi

Translation contributions are welcome. See [Contributing](Contributing) for guidelines.

## Style Guide

- **Tone:** Accessible but rigorous. Write for a practitioner with 2–3 years of experience.
- **Examples:** Prefer South Asian context (India, Bangladesh, Nepal, Sri Lanka).
- **Jargon:** Define terms on first use. Add to ImpactLex if they're sector-standard.
- **Attribution:** Cite sources. Link to DevDiscourses where possible.
- **Accessibility:** Use semantic HTML, alt text for images, sufficient color contrast.
