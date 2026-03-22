---
name: housekeeping
description: Run post-feature housekeeping — clean branches, update docs, issues, roadmap, README. Use when the user says "clean up", "housekeeping", "we're done with this feature", or after completing a major change.
---

# Post-Change Housekeeping

Run through this checklist after completing major work on ImpactMojo.

## Steps

1. **Git cleanup**
   - List stale branches: `git branch -vv | grep gone`
   - Delete merged local branches: `git branch -d <branch>`
   - Prune remote refs: `git fetch --prune`
   - Verify working tree is clean: `git status`

2. **Update CHANGELOG.md**
   - Add entry under current version with date
   - Categorize as Added/Changed/Fixed/Removed

3. **Update docs/ (GitBook)**
   - Review `docs/` files for accuracy
   - Update `docs/games-guide.md` if games changed
   - Update `docs/platform-overview.md` if structure changed
   - Update `docs/content-guide.md` if content added

4. **Update ROADMAP.md**
   - Move completed items to done
   - Add new planned work if applicable

5. **Update README.md**
   - Verify project structure tree is current
   - Update feature descriptions if scope changed

6. **Update search & sitemap**
   - Add new content to `data/search-index.json`
   - Add new pages to `sitemap.xml`

7. **GitHub housekeeping**
   - Close resolved issues (link to commits/PRs)
   - Update project board
   - Post to Discussions if relevant

8. **Backup**
   - Copy current working `index.html` to `Backups/` with a descriptive name
   - Verify existing backups are not stale (delete if superseded)

9. **Update counts & references**
   - Verify game, lab, course counts are consistent across all docs, index, catalog, admin dashboards, and transparency pages
   - Check for stale `101.impactmojo.in` references that should now point to self-hosted files

10. **Quality checks**
    - Verify no broken navigation links
    - Check text contrast on new UI elements (WCAG AA)
    - Test all forms submit to correct Formspree endpoint
