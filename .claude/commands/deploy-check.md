---
description: Pre-deploy checklist — verify everything is ready for production
---

## Current State

!`git status`
!`git log --oneline -5`

Spawn the following agents **in parallel** for a comprehensive pre-deploy check:

1. **`content-auditor`** agent — verify content counts, search index completeness, link integrity, sitemap, and forms
2. **`deploy-reviewer`** agent — review recent changes for security, cross-references, JSON validity, and mobile responsiveness

Also check directly:
- **Git**: All changes committed and pushed?
- **Backup**: Current `index.html` backed up to `Backups/`?
- **Docs**: `docs/changelog.md` updated for user-facing changes?

Synthesize agent results and direct checks into a single deploy readiness report. Flag anything that needs attention before deploying.
