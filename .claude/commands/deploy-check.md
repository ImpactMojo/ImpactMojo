---
description: Pre-deploy checklist — verify everything is ready for production
---

## Current State

!`git status`
!`git log --oneline -5`

Run through this pre-deploy checklist:

1. **Git**: All changes committed and pushed?
2. **Counts**: Game, lab, course counts consistent across index.html, catalog, docs?
3. **JSON**: Validate `data/search-index.json` is valid JSON
4. **Links**: No broken internal links in recently changed files?
5. **Forms**: All forms submit to Formspree endpoint `xpwdvgzp`?
6. **Sitemap**: New pages added to `sitemap.xml`?
7. **Docs**: `CHANGELOG.md` updated for user-facing changes?
8. **Backup**: Current `index.html` backed up to `Backups/`?

Report status for each item. Flag anything that needs attention before deploying.
