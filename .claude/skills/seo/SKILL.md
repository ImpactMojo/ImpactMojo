---
description: "Optimize ImpactMojo pages for search engines — technical audits, meta tags, structured data, Open Graph, sitemap, Core Web Vitals, E-E-A-T content quality, schema markup, image optimization, AI search optimization, and multilingual SEO. Use when the user asks about SEO, search rankings, meta tags, structured data, discoverability, or site audit."
---

# SEO Skill — ImpactMojo

Comprehensive SEO optimization for impactmojo.in. Organized into 12 sub-capabilities.

---

## 1. Technical SEO Audit

Run a 9-category audit across the site:

```bash
# Check meta descriptions exist
grep -rL '<meta name="description"' Games/*.html Labs/*.html courses/*/index.html BookSummaries/*.html

# Check canonical URLs
grep -rn 'rel="canonical"' Games/*.html Labs/*.html | head -20

# Check viewport meta
grep -rL 'name="viewport"' Games/*.html Labs/*.html

# Check title tags
grep -rn '<title>' Games/*.html Labs/*.html | grep -v "ImpactMojo"
```

**Categories:** Crawlability, Indexing, Metadata, Performance, Mobile, Security (HTTPS), Accessibility, Structured Data, Internal Linking.

---

## 2. Required Meta Tags (Every Page)

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{Page Title} | ImpactMojo</title>
<meta name="description" content="{150-160 char description with primary keyword}">
<meta name="keywords" content="development economics, {topic}, South Asia, free education">
<link rel="canonical" href="https://www.impactmojo.in/{path}">
<meta name="robots" content="index, follow">
```

---

## 3. Open Graph (Social Sharing)

```html
<meta property="og:title" content="{Title}">
<meta property="og:description" content="{Description}">
<meta property="og:image" content="https://www.impactmojo.in/assets/images/{image}.png">
<meta property="og:url" content="https://www.impactmojo.in/{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ImpactMojo">
<meta property="og:locale" content="en_IN">
```

### Twitter Card
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{Title}">
<meta name="twitter:description" content="{Description}">
<meta name="twitter:image" content="https://www.impactmojo.in/assets/images/{image}.png">
```

---

## 4. Structured Data (JSON-LD)

### Course Schema
```json
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "{Course Name}",
  "description": "{Description}",
  "provider": {
    "@type": "Organization",
    "name": "ImpactMojo",
    "url": "https://www.impactmojo.in",
    "logo": "https://www.impactmojo.in/assets/images/ImpactMojo Logo.png"
  },
  "isAccessibleForFree": true,
  "educationalLevel": "Introductory",
  "inLanguage": ["en", "hi", "ta", "bn", "te", "mr"],
  "numberOfCredits": 0,
  "hasCourseInstance": {
    "@type": "CourseInstance",
    "courseMode": "online",
    "courseWorkload": "PT2H"
  }
}
```

### Game / Interactive Resource
```json
{
  "@context": "https://schema.org",
  "@type": "LearningResource",
  "name": "{Game Name}",
  "description": "{Description}",
  "learningResourceType": "interactive simulation",
  "isAccessibleForFree": true,
  "interactivityType": "active",
  "educationalUse": "workshop, classroom, self-study"
}
```

### Book Summary
```json
{
  "@context": "https://schema.org",
  "@type": "Book",
  "name": "{Book Title}",
  "author": {"@type": "Person", "name": "{Author}"},
  "review": {
    "@type": "Review",
    "reviewBody": "{Summary description}",
    "author": {"@type": "Organization", "name": "ImpactMojo"}
  }
}
```

### Organization (homepage)
```json
{
  "@context": "https://schema.org",
  "@type": "EducationalOrganization",
  "name": "ImpactMojo",
  "url": "https://www.impactmojo.in",
  "description": "Free development education for social impact across South Asia",
  "areaServed": ["IN", "BD", "NP", "LK"],
  "availableLanguage": ["en", "hi", "ta", "bn", "te", "mr"]
}
```

---

## 5. E-E-A-T Content Quality

Ensure pages demonstrate **Experience, Expertise, Authoritativeness, Trustworthiness**:

- **Author attribution**: Link to Dr. Varna Sri Raman's profile on About page
- **Citations**: Link to DevDiscourses papers, cite real programme evaluations
- **Dates**: Show `lastmod` or "Updated: {date}" on content pages
- **Credentials**: Mention academic background, field experience in South Asia
- **External validation**: Link to GitHub stars, Netlify status, user testimonials

---

## 6. Image Optimization

- **Alt text**: Descriptive, keyword-rich (`alt="Theory of Change workshop diagram for NGO evaluation"`)
- **File size**: Compress via ImgBot (already integrated via PR #254)
- **Format**: Use WebP where possible, PNG for illustrations with transparency
- **Lazy loading**: Add `loading="lazy"` to below-fold images
- **Dimensions**: Always set `width` and `height` to prevent CLS

---

## 7. Sitemap Management

File: `sitemap.xml` — must include every public page.

| Content type | Priority | changefreq |
|---|---|---|
| Homepage | `1.0` | weekly |
| Courses | `0.8` | monthly |
| Games | `0.6` | monthly |
| Labs | `0.6` | monthly |
| BookSummaries | `0.7` | monthly |
| Blog posts | `0.6` | monthly |
| Legal pages | `0.4` | yearly |

**Validation:**
```bash
# Count sitemap URLs vs actual files
python3 -c "
import xml.etree.ElementTree as ET
tree = ET.parse('sitemap.xml')
ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls = tree.getroot().findall('s:url', ns)
print(f'Sitemap URLs: {len(urls)}')
"
```

---

## 8. Core Web Vitals

Target scores for Lighthouse:
- **LCP** (Largest Contentful Paint): < 2.5s
- **FID** (First Input Delay): < 100ms
- **CLS** (Cumulative Layout Shift): < 0.1

Key optimizations for static site:
- Inline critical CSS (already done — no external stylesheets on games/labs)
- Preload Google Fonts with `<link rel="preload">`
- Defer non-critical JS with `defer` attribute
- Set explicit image dimensions to prevent layout shift

---

## 9. AI Search Optimization (GEO)

Optimize for Google AI Overviews and ChatGPT/Perplexity citations:

- **FAQ sections**: Add FAQ schema to key pages (courses, about, pricing)
- **Definition lists**: Structure content as clear Q&A or definition → explanation
- **Concise answers**: First paragraph of each section should directly answer the implied question
- **Cite sources**: Link to authoritative papers and datasets
- **Unique data**: Highlight platform-specific stats (269 Dataverse entries, 203 BCT techniques, 200 case studies from 117 countries)

---

## 10. Multilingual SEO (hreflang)

ImpactMojo supports 6 languages. Add hreflang tags on pages with translations:

```html
<link rel="alternate" hreflang="en" href="https://www.impactmojo.in/{path}">
<link rel="alternate" hreflang="hi" href="https://www.impactmojo.in/{path}?lang=hi">
<link rel="alternate" hreflang="ta" href="https://www.impactmojo.in/{path}?lang=ta">
<link rel="alternate" hreflang="x-default" href="https://www.impactmojo.in/{path}">
```

---

## 11. Internal Linking Strategy

- Every game links to related course modules
- Every lab links to the course it supports
- Every course links to relevant handouts, games, and labs
- BookSummaries link to related DevDiscourses papers
- Blog posts link to relevant platform content

**Anchor text**: Use descriptive text, not "click here".

---

## 12. ImpactMojo Keyword Clusters

| Cluster | Primary keywords |
|---------|-----------------|
| Core platform | free development education, South Asia learning platform, NGO training |
| MEL | monitoring evaluation learning, theory of change, logframe |
| Economics | development economics course free, behavioral economics simulation |
| Gender | gender mainstreaming course, feminist research methods |
| Games | economics simulation game, public goods game, prisoner's dilemma interactive |
| Data | development data tools, India datasets, Dataverse |
| Premium | MEL workshop India, development coaching, research consultation |

---

## Audit Workflow

1. **Technical**: Check meta tags, canonicals, viewport, robots on all pages
2. **Content**: Verify E-E-A-T signals, keyword coverage, internal links
3. **Schema**: Validate JSON-LD with Google Rich Results Test
4. **Sitemap**: Cross-check sitemap vs actual files
5. **Images**: Check alt text coverage, file sizes, lazy loading
6. **Performance**: Run Lighthouse on key pages
7. **Social**: Verify OG/Twitter cards render correctly
