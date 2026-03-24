---
description: "Optimize ImpactMojo pages for search engines — meta tags, structured data, Open Graph, sitemap, and content strategy. Use when the user asks about SEO, search rankings, meta tags, structured data, or discoverability."
---

# SEO Skill

Optimize impactmojo.in for search engine visibility and social sharing.

## Core SEO Checklist

### Every HTML Page Must Have
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{Page Title} | ImpactMojo</title>
<meta name="description" content="{150-160 char description}">
<meta name="keywords" content="development economics, {topic}, South Asia, free education">
<link rel="canonical" href="https://impactmojo.in/{path}">
```

### Open Graph (Social Sharing)
```html
<meta property="og:title" content="{Title}">
<meta property="og:description" content="{Description}">
<meta property="og:image" content="https://impactmojo.in/assets/{image}.png">
<meta property="og:url" content="https://impactmojo.in/{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ImpactMojo">
```

### Twitter Card
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{Title}">
<meta name="twitter:description" content="{Description}">
<meta name="twitter:image" content="https://impactmojo.in/assets/{image}.png">
```

### Structured Data (JSON-LD)
For courses:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "{Course Name}",
  "description": "{Description}",
  "provider": {
    "@type": "Organization",
    "name": "ImpactMojo",
    "url": "https://impactmojo.in"
  },
  "isAccessibleForFree": true,
  "educationalLevel": "Introductory",
  "inLanguage": "en"
}
</script>
```

For games/interactive content:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LearningResource",
  "name": "{Game Name}",
  "description": "{Description}",
  "learningResourceType": "interactive",
  "isAccessibleForFree": true
}
</script>
```

## Sitemap Management
- File: `sitemap.xml`
- Add `<url>` entry for every new page
- Set `<lastmod>` to current date
- Priority: `1.0` (homepage), `0.8` (courses), `0.7` (games/labs), `0.5` (handouts)

## Content SEO Strategy
- **Title tags**: Include primary keyword + "| ImpactMojo"
- **H1**: One per page, matches search intent
- **Internal linking**: Cross-link related courses, games, and handouts
- **Image alt text**: Descriptive, keyword-rich
- **URL structure**: Clean, lowercase, hyphenated (`/courses/behavioral-economics/`)

## Audit Workflow
1. Check all pages have required meta tags: `grep -rn '<meta name="description"' *.html courses/**/*.html Games/**/*.html`
2. Validate sitemap completeness: compare sitemap URLs vs actual files
3. Check for missing Open Graph tags
4. Verify canonical URLs resolve correctly
5. Test structured data with Google Rich Results validator

## ImpactMojo-Specific Keywords
- development economics, South Asia, free courses
- behavioral economics games, RCT simulation
- poverty measurement, microfinance, gender economics
- interactive learning, development studies
