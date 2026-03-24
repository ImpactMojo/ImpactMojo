---
description: "Generate polished, accessible HTML/CSS for ImpactMojo pages — games, labs, landing sections, and interactive components. Use when the user asks to build UI, improve design, create a page layout, or wants frontend help."
---

# Frontend Design Skill

Generate high-quality, accessible HTML/CSS/JS for ImpactMojo's static site.

## Design System

ImpactMojo uses a consistent visual language across all pages:

### Colors
- **Primary**: `#667eea` (indigo) → `#764ba2` (purple) gradient
- **Accent**: `#f093fb` (pink), `#4facfe` (blue)
- **Text**: `#2d3748` (dark), `#718096` (muted)
- **Background**: `#f7fafc` (light gray), `#ffffff` (white)
- **Success**: `#48bb78`, **Warning**: `#ed8936`, **Error**: `#fc8181`

### Typography
- **Headings**: system font stack, bold, `#2d3748`
- **Body**: `0.9rem` minimum on mobile, `1rem` on desktop
- **Line height**: 1.6 for readability

### Layout Patterns
- **Cards**: `border-radius: 16px`, `box-shadow: 0 4px 6px rgba(0,0,0,0.1)`, white background
- **Sections**: Max-width `1200px`, centered, `padding: 4rem 2rem`
- **Grid**: CSS Grid with `auto-fit, minmax(300px, 1fr)` for responsive cards
- **Spacing**: `gap: 2rem` between cards, `margin-bottom: 3rem` between sections

### Responsive Rules
- Mobile-first approach
- Breakpoints: `768px` (tablet), `1024px` (desktop)
- Tap targets: minimum `48px`
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">`

### Accessibility (WCAG AA)
- Color contrast ratio ≥ 4.5:1 for text
- All images have `alt` text
- Focus-visible outlines on interactive elements
- Semantic HTML5 (`<nav>`, `<main>`, `<section>`, `<article>`)
- `aria-label` on icon-only buttons

### Indian Folk Art Style (Games)
Games use illustrations inspired by Madhubani, Warli, and Kalamkari art:
- Bold outlines, flat colors
- Geometric patterns and nature motifs
- Inline SVG preferred for illustrations
- Color palette: earth tones with vibrant accents

## Workflow

1. **Understand**: Clarify what page/component is needed and where it fits
2. **Reference**: Check existing pages for consistent patterns (`index.html`, recent games)
3. **Build**: Write semantic HTML with inline CSS (for games) or linked styles
4. **Validate**: Check responsive behavior, accessibility, dark mode support
5. **Integrate**: Update cross-references per content-management rules

## Anti-Patterns to Avoid
- No external CSS frameworks (Bootstrap, Tailwind) — all styles are custom
- No `!important` unless absolutely necessary
- No fixed pixel widths on containers
- No missing viewport meta tags
- No placeholder images — use inline SVG or CSS gradients
