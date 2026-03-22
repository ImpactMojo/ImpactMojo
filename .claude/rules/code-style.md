---
paths:
  - "Games/**/*.html"
  - "courses/**/*.html"
---

# Code Style

- Games are single self-contained HTML files — all CSS and JS inline, no external dependencies
- Use Indian folk art styles for illustrations: Warli, Madhubani, Gond, Kalamkari, Pichwai, Pattachitra
- Include responsive `<meta name="viewport" content="width=device-width, initial-scale=1.0">` in all HTML files
- Use semantic HTML5 elements (`<header>`, `<main>`, `<section>`, `<nav>`, `<footer>`)
- Dark mode support via CSS custom properties (`--bg-color`, `--text-color`, etc.)
- Mobile: minimum `0.9rem` font size, `48px` tap targets, single-column grid at 768px
- Reference existing games for structure: `Games/prisoners-dilemma-game.html`

## Related

- Agent `code-reviewer` enforces these standards during PR reviews
- Skill `add-files` applies these when creating new content files
