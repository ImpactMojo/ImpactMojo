---
description: Add a new game to ImpactMojo with all cross-references
argument-hint: [game-name or topic]
---

Create a new interactive game for ImpactMojo about: $ARGUMENTS

Follow the `/add-files` skill workflow for games:

1. Create single self-contained HTML file in `/Games/` (kebab-case name)
2. Include: inline CSS, inline JS, responsive viewport meta, Indian folk art SVG illustrations
3. Reference `Games/prisoners-dilemma-game.html` for structure
4. Backup `index.html` first: `cp index.html Backups/index-backup-$(date +%Y%m%d-%H%M).html`
5. Add game link to `index.html` games section
6. Update game count in ALL locations (grep for current count)
7. Add entry to `data/search-index.json`
8. Add `<url>` to `sitemap.xml`
9. Update `docs/games-guide.md`
10. Update `docs/changelog.md`

After creating, validate with `/project:audit`.
