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

## Pre-Flight Checklist (MANDATORY)

Before considering ANY new or modified HTML page complete, verify ALL of these are present. **Do not submit work that is missing any item.** This is the most common source of branding failures.

| # | Element | How to check | What to add if missing |
|---|---------|-------------|----------------------|
| 1 | **Logo image** | `grep 'ImpactMojo%20Logo.png'` | `<img src="/assets/images/ImpactMojo%20Logo.png" alt="ImpactMojo" width="28" height="28">` in topbar |
| 2 | **3-mode theme toggle** | `grep 'im-theme-selector'` | System/Light/Dark buttons with `data-imtheme` + CSS + JS (see templates below) |
| 3 | **Theme toggle JS** | `grep 'applyTheme'` | Full theme JS block with `localStorage`, `matchMedia`, button click handlers |
| 4 | **translate.js** | `grep 'translate.js'` | `<script defer src="/js/translate.js"></script>` |
| 5 | **4-section footer** | `grep 'site-footer'` | Full footer: About, Legal, Quick Links, Resources + copyright |
| 6 | **Paper plane SVG** | `grep 'paper-plane'` | Floating decorative SVG with CSS animation |
| 7 | **Skip link** | `grep 'skip-link'` | `<a href="#main-content" class="skip-link">Skip to content</a>` |
| 8 | **Google Analytics** | `grep 'G-JRCMEB9TBW'` | GA4 tag in `<head>` |
| 9 | **Google Fonts** | `grep 'fonts.googleapis'` | Amaranth + Inter + JetBrains Mono import |
| 10 | **Auth scripts** | `grep 'auth.js'` | supabase-js, state-manager.js, config.js, auth.js (sync, not defer) |
| 11 | **Button contrast** | Visual check | CTA buttons on gradients MUST use `color: #ffffff; -webkit-text-fill-color: #ffffff;` |
| 12 | **Absolute URLs** | `grep 'href="[a-z]'` (no leading /) | All internal links must use absolute paths (`/premium.html` not `premium.html`) |
| 13 | **Viewport meta** | `grep 'viewport'` | `<meta name="viewport" content="width=device-width, initial-scale=1.0">` |
| 14 | **Favicons** | `grep 'favicon'` | `<link href="/assets/images/favicon.png" rel="icon">` |
| 15 | **Topbar position: fixed** | `grep 'im-topbar.*sticky'` (should find NOTHING) | Topbar MUST be `position: fixed` not `sticky` — sticky breaks on `display:flex` body layouts |
| 16 | **Body padding-top** | Check body/main has `padding-top:44px` or `margin-top:44px` | Required to prevent content hiding behind fixed topbar |

## Required Page Elements

### 1. Viewport Meta
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### 2. Fixed Top Bar
Must include: **logo image**, home link, Premium button, and **3-mode theme toggle**.

**CRITICAL**: The topbar MUST use `position: fixed` (NOT `sticky`). Many pages use `body{display:flex}` for sidebar layouts. A `sticky` topbar becomes a flex child and pushes all content to the right. Use `fixed` with `left:0; right:0` and add `padding-top: 44px` or `margin-top: 44px` to the body/main content.

Required CSS for the topbar:
```css
.im-topbar {
    position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
    background: var(--im-nav-bg, rgba(15, 23, 42, 0.95));
    backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border, #334155);
    padding: 0.5rem 1rem;
    display: flex; align-items: center; justify-content: space-between;
    gap: 0.75rem;
}
```
And on the body or main content area:
```css
body { padding-top: 44px; }
/* OR if body uses display:flex with a sidebar: */
main { margin-top: 44px; }
nav.sidebar { top: 44px; height: calc(100vh - 44px); }
```
```html
<div class="im-topbar" id="imTopbar">
    <div class="im-topbar-left">
        <a href="/index.html" class="im-topbar-home">
            <img src="/assets/images/ImpactMojo%20Logo.png" alt="ImpactMojo" width="28" height="28" style="border-radius:6px;">
            <span>ImpactMojo</span>
        </a>
    </div>
    <div class="im-topbar-right">
        <a href="/premium.html" class="im-premium-btn">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            Premium
        </a>
        <div class="im-theme-selector" aria-label="Theme selection">
            <button class="im-theme-btn" data-imtheme="system" title="System theme" aria-label="Use system theme">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
            </button>
            <button class="im-theme-btn" data-imtheme="light" title="Light theme" aria-label="Use light theme">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
            </button>
            <button class="im-theme-btn" data-imtheme="dark" title="Dark theme" aria-label="Use dark theme">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
            </button>
        </div>
    </div>
</div>
```

### Required Theme Toggle CSS
```css
.im-theme-selector {
    display: flex; gap: 2px;
    background: var(--color-bg-card, #2d3748);
    border: 1px solid var(--border, #4a5568);
    border-radius: 8px; padding: 2px;
}
.im-theme-btn {
    background: transparent; border: none;
    color: var(--color-text-muted, #a0aec0);
    padding: 6px; border-radius: 5px; cursor: pointer;
    transition: all 0.2s; display: flex; align-items: center;
    justify-content: center; width: 30px; height: 30px;
}
.im-theme-btn:hover { background: var(--border, #4a5568); color: var(--color-text, #e2e8f0); }
.im-theme-btn.active { background: var(--color-primary, #667eea); color: #fff; }
.im-theme-btn svg { width: 16px; height: 16px; }
```

### Required Theme Toggle JS (before `</body>`)
```html
<script>
(function() {
    function getSystemTheme() {
        return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
    }
    function applyTheme(theme) {
        var resolved = theme === 'system' ? getSystemTheme() : theme;
        document.documentElement.setAttribute('data-theme', resolved);
        document.body.classList.remove('dark-mode', 'light-mode');
        if (resolved === 'light') document.body.classList.add('light-mode');
        else document.body.classList.add('dark-mode');
    }
    function updateButtons(pref) {
        document.querySelectorAll('.im-theme-btn').forEach(function(btn) {
            btn.classList.toggle('active', btn.getAttribute('data-imtheme') === pref);
        });
    }
    var saved = localStorage.getItem('im-theme') || 'system';
    applyTheme(saved);
    document.addEventListener('DOMContentLoaded', function() {
        updateButtons(saved);
        document.querySelectorAll('.im-theme-btn').forEach(function(btn) {
            btn.addEventListener('click', function() {
                var t = this.getAttribute('data-imtheme');
                localStorage.setItem('im-theme', t);
                applyTheme(t);
                updateButtons(t);
            });
        });
    });
    window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', function() {
        if ((localStorage.getItem('im-theme') || 'system') === 'system') applyTheme('system');
    });
})();
</script>
```

### 3. Floating Paper Plane SVG
```html
<svg class="paper-plane" viewBox="0 0 200 200" width="120" height="120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <path d="M50,150 L150,50 L50,100 L80,130 Z" fill="none" stroke="#667eea" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M80,130 L150,50" stroke="#48bb78" stroke-width="2" stroke-dasharray="4,4"/>
    <circle cx="150" cy="50" r="4" fill="#667eea"/>
</svg>
```
```css
.paper-plane {
  position: fixed; bottom: 2rem; right: 2rem;
  opacity: 0.12; pointer-events: none; z-index: 0;
  animation: float 6s ease-in-out infinite;
}
@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-15px) rotate(3deg); }
}
@media (prefers-reduced-motion: reduce) { .paper-plane { animation: none; } }
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
      <a href="https://github.com/ImpactMojo/ImpactMojo">GitHub</a>
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
