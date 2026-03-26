# SEO & Content Marketing Strategy — ImpactMojo

Last updated: 2026-03-26

## Current SEO Health: ~8.5/10

### What's Implemented

| Element | Coverage | Status |
|---------|----------|--------|
| Meta descriptions | 90%+ | Games, Labs, Courses, Blog, BookSummaries |
| Canonical URLs | 80%+ | Games, Labs, Courses |
| Open Graph tags | 85%+ | Games, Blog, Courses, BookSummaries |
| Twitter Cards | 85%+ | Games, Blog, Courses, BookSummaries |
| JSON-LD Schema | 28 pages | Homepage (Organization), Games (LearningResource), Courses (Course) |
| Sitemap | 119 URLs | All content types covered |
| robots.txt | Correct | Allows all, disallows admin scripts |
| Google Analytics | All pages | G-JRCMEB9TBW |

### Remaining Gaps

- Labs (11): Missing Open Graph tags
- Blog posts (26): Missing JSON-LD Article schema
- BookSummaries: Missing Book schema with author/ISBN
- BreadcrumbList schema on all pages
- FAQ schema on faq.html
- hreflang tags for multilingual pages

---

## Content Marketing Funnel

### TOFU — Top of Funnel (Awareness)

**Assets:** 26 blog posts, 16 games, Substack newsletter, Threads content

**Strategy:**
- Blog posts target long-tail development economics keywords (MEL, theory of change, logframes)
- Games are shareable viral content — "Play the Prisoner's Dilemma" drives social shares
- Each blog post should target one primary keyword cluster (see Keyword Clusters below)

### MOFU — Middle of Funnel (Consideration)

**Assets:** 13 courses, 100+ handouts, 9 labs, 29 BookSummaries

**Missing (implement next):**
- Email capture on game completion screens
- Gated handout bundles as lead magnets by persona
- Learning Path landing pages connecting free content to premium
- Blog → Course CTAs at the end of every blog post

**Lead Magnet Ideas:**
- NGO Programme Managers: "MEL Framework Template Pack" (15 handouts)
- Students: "Development Economics Reading List + Flashcards"
- Consultants: "Proposal Writing Toolkit for MEL Consultants"
- Gender Specialists: "Gender Mainstreaming Toolkit" (12 handouts)

### BOFU — Bottom of Funnel (Conversion)

**Assets:** premium.html (4 tiers), coaching.html (sliding scale), signup.html

**Long-Form Sales Letter Structure for coaching.html:**

```
1. HEADLINE — Specific outcome
   "Go from reading about MEL to designing evaluations that funders trust"

2. PROBLEM — 3 pain points
   - "You understand theory but freeze in real evaluations"
   - "Your logframes get rejected by donors"
   - "You can't translate academic knowledge into field practice"

3. AUTHORITY — Dr. Varna's credentials, countries, programmes

4. BRIDGE — "Free courses gave you knowledge. Coaching gives you confidence."

5. SOCIAL PROOF — 3-5 testimonials from testimonials.html by outcome type

6. THE OFFER — Clear pricing + what's included at each tier

7. FAQ — Address objections (sliding scale, refund policy, time commitment)

8. CTA — "Book a free 15-min discovery call" (Google Calendar integration)
```

### Retention

**Assets:** account.html, Supabase streak tracking, certificates

**Missing:**
- Automated email sequences (course completion → next course suggestion)
- Re-engagement triggers (30-day inactive → "You were making progress on MEL")

---

## Keyword Clusters

| Cluster | Primary Keywords | Target Pages |
|---------|-----------------|-------------|
| Core platform | free development education, South Asia learning platform, NGO training | index.html, about.html |
| MEL | monitoring evaluation learning, theory of change, logframe | courses/mel/, blog/meal-demystified.html |
| Economics | development economics course free, behavioral economics simulation | courses/devecon/, Games/ |
| Gender | gender mainstreaming course, feminist research methods | courses/gender/, Games/gender-equity-game.html |
| Games | economics simulation game, public goods game, prisoner's dilemma interactive | Games/*.html |
| Data | development data tools, India datasets, Dataverse | dataverse.html, Labs/ |
| Premium | MEL workshop India, development coaching, research consultation | premium.html, coaching.html |
| Books | development economics books, book summary, reading companion | BookSummaries/*.html |

---

## Technical SEO Checklist (for new content)

Every new HTML page must include:

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{Page Title} | ImpactMojo</title>
<meta name="description" content="{150-160 chars with primary keyword}">
<link rel="canonical" href="https://www.impactmojo.in/{path}">
<meta name="robots" content="index, follow">
<meta property="og:title" content="{Title}">
<meta property="og:description" content="{Description}">
<meta property="og:url" content="https://www.impactmojo.in/{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ImpactMojo">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{Title}">
<meta name="twitter:description" content="{Description}">
```

Plus appropriate JSON-LD schema for the content type (Course, LearningResource, Article, Book).

And the page must be added to `sitemap.xml`.

---

## Next Actions (Priority Order)

1. Add email capture CTAs to game completion screens
2. Create Learning Path landing pages (MEL Practitioner, DevEcon Student, Gender Specialist)
3. Rewrite coaching.html with long-form sales narrative
4. Add Blog → Course CTAs to all 26 blog posts
5. Create 3 gated handout bundles as lead magnets
6. Add Article schema to blog posts
7. Add FAQ schema to faq.html
8. Add hreflang tags to pages with language switchers
