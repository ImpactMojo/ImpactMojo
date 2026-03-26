---
description: "Enforce ImpactMojo's brand identity across all generated pages, components, and content. Auto-invoked when creating new HTML pages, games, labs, BookSummaries, or any user-facing content. Ensures consistent fonts, colors, layout, and decorative elements."
---

# ImpactMojo Brand Guidelines

Every page on ImpactMojo must follow these brand standards. Apply them automatically — do not ask the user to confirm.

## Typography

| Role | Font | Fallback | Weight |
|------|------|----------|--------|
| Body text | **Amaranth** | Arial, sans-serif | 400 |
| Headings | **Inter** | Helvetica, sans-serif | 600–800 |
| Code / data | **JetBrains Mono** | monospace | 400 |

### Google Fonts Import
```html
<link href="https://fonts.googleapis.com/css2?family=Amaranth:wght@400;700&family=Inter:wght@400;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

### CSS Variables
```css
:root {
  --font-body: 'Amaranth', Arial, sans-serif;
  --font-heading: 'Inter', Helvetica, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --font-size-body: 1rem;
  --line-height: 1.6;
}
```

## Color Palette

### Core Colors
| Token | Light | Dark | Usage |
|-------|-------|------|-------|
| `--color-primary` | `#667eea` | `#7c93f5` | Buttons, links, active states |
| `--color-primary-gradient` | `linear-gradient(135deg, #667eea, #764ba2)` | same | Hero sections, CTAs |
| `--color-accent-pink` | `#f093fb` | `#f5a8ff` | Highlights, badges |
| `--color-accent-blue` | `#4facfe` | `#6bb8ff` | Info, secondary actions |
| `--color-text` | `#2d3748` | `#e2e8f0` | Primary text |
| `--color-text-muted` | `#718096` | `#a0aec0` | Secondary text |
| `--color-bg` | `#f7fafc` | `#1a202c` | Page background |
| `--color-bg-card` | `#ffffff` | `#2d3748` | Card surfaces |
| `--color-success` | `#48bb78` | `#68d391` | Success states |
| `--color-warning` | `#ed8936` | `#f6ad55` | Warning states |
| `--color-error` | `#fc8181` | `#feb2b2` | Error states |

### Learning Track Colors (for folk art and course theming)
| Track | Color | Folk Art Style |
|-------|-------|----------------|
| MEL & Research | `#3182ce` | Warli |
| Data & Technology | `#38a169` | Gond |
| Policy & Economics | `#d69e2e` | Kalamkari |
| Gender & Equity | `#d53f8c` | Madhubani |
| Health & Communication | `#e53e3e` | Pattachitra |
| Philosophy & Governance | `#805ad5` | Pichwai |

## 3-Mode Theme Toggle

Every page must include a theme toggle (System / Light / Dark) with `localStorage` persistence:

```css
[data-theme="dark"] {
  --color-text: #e2e8f0;
  --color-bg: #1a202c;
  --color-bg-card: #2d3748;
}
```

The toggle stores preference in `localStorage.getItem('impactmojo-theme')` and defaults to system preference via `prefers-color-scheme`.

## Required Page Elements

### 1. Viewport Meta
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### 2. Sticky Top Bar
Must include: home button, Premium button, and language selector.
```html
<div class="topbar">
  <a href="/" class="home-btn" aria-label="Return to ImpactMojo home">🏠 ImpactMojo</a>
  <div class="topbar-right">
    <div class="lang-selector">
      <select id="language-select" aria-label="Select language">
        <option value="en">English</option>
        <option value="hi">हिन्दी</option>
        <option value="ta">தமிழ்</option>
        <option value="bn">বাংলা</option>
        <option value="te">తెలుగు</option>
        <option value="mr">मराठी</option>
      </select>
    </div>
    <a href="/premium.html" class="premium-btn">Get Premium</a>
  </div>
</div>
```
- Home button: always links to `/`, visible on all inner pages
- Language selector: triggers Google Translate or equivalent
- Premium button: styled as a CTA (gradient background, white text, rounded)

### 3. Floating Paper Plane SVG
Every inner page includes a decorative floating paper plane (CSS animated, reduced-motion aware):
```css
.paper-plane {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  opacity: 0.15;
  animation: float 6s ease-in-out infinite;
  pointer-events: none;
}
@media (prefers-reduced-motion: reduce) {
  .paper-plane { animation: none; }
}
```

### 4. Full 4-Section Footer
Every page must include the complete footer with all four sections:
```html
<footer class="site-footer">
  <div class="footer-grid">
    <!-- Section 1: About ImpactMojo -->
    <div class="footer-col">
      <h4>About ImpactMojo</h4>
      <a href="/about.html">About Us</a>
      <a href="/ImpactMojo_PressKit.html">Press Kit</a>
      <a href="/contact.html">Contact</a>
      <a href="/coaching.html">Coaching</a>
    </div>
    <!-- Section 2: Legal -->
    <div class="footer-col">
      <h4>Legal</h4>
      <a href="/privacy-policy.html">Privacy Policy</a>
      <a href="/terms-of-service.html">Terms of Service</a>
      <a href="/refund-policy.html">Refund Policy</a>
      <a href="/data-protection.html">Data Protection</a>
      <a href="/disclaimer.html">Disclaimer</a>
    </div>
    <!-- Section 3: Quick Links -->
    <div class="footer-col">
      <h4>Quick Links</h4>
      <a href="/catalog.html">Course Catalog</a>
      <a href="/workshops.html">Workshops</a>
      <a href="/premium.html">Premium</a>
      <a href="/dojos.html">Dojos</a>
    </div>
    <!-- Section 4: Resources -->
    <div class="footer-col">
      <h4>Resources</h4>
      <a href="/blog.html">Blog</a>
      <a href="/podcast.html">Podcast</a>
      <a href="https://impactmojo.gitbook.io/impactmojo">GitBook Docs</a>
      <a href="https://github.com/Varnasr/ImpactMojo">GitHub</a>
    </div>
  </div>
  <div class="footer-bottom">
    <p>© 2026 ImpactMojo. Code: MIT | Content: CC BY-NC-ND 4.0</p>
  </div>
</footer>
```

### 5. Sargam Icons
Use Sargam Icons (`si_` prefix) for all UI icons. Do not use Font Awesome, Heroicons, or emoji as icons.

## Layout Standards

| Element | Value |
|---------|-------|
| Max content width | `1200px` |
| Section padding | `4rem 2rem` |
| Card border-radius | `16px` |
| Card shadow | `0 4px 6px rgba(0,0,0,0.1)` |
| Grid gap | `2rem` |
| Card grid | `auto-fit, minmax(300px, 1fr)` |
| Mobile breakpoint | `768px` |
| Desktop breakpoint | `1024px` |
| Min tap target | `48px` |

## Accessibility (WCAG AA)

- Color contrast ≥ 4.5:1 for body text, ≥ 3:1 for large text
- All images: `alt` text required
- Interactive elements: visible focus outlines
- Semantic HTML5: `<nav>`, `<main>`, `<section>`, `<article>`
- Icon-only buttons: `aria-label` required
- Skip-to-content link on every page

## Anti-Patterns

- No external CSS frameworks (Bootstrap, Tailwind) — all custom
- No `!important` unless overriding third-party styles
- No fixed pixel widths on containers
- No placeholder images — use inline SVG or CSS gradients
- No emoji as icons (use Sargam)
- No purple gradients on cards (reserve for hero only)
- No centered-everything layouts ("AI slop")

## Forms

All forms submit to Formspree endpoint `xpwdvgzp`:
```html
<form action="https://formspree.io/f/xpwdvgzp" method="POST">
```

## File Naming

- Games: `/Games/{kebab-case}-game.html`
- Labs: `/Labs/{kebab-case}-lab.html`
- BookSummaries: `/BookSummaries/{kebab-case}-companion.html`
- Blog: `/blog/{kebab-case}.html`
- Handouts: `/Handouts/{Track Name}/{topic}/handout.html`
