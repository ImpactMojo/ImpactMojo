---
name: housekeeping
description: Run post-feature housekeeping — clean branches, update docs, issues, roadmap, README
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

8. **Quality checks**
   - Verify no broken navigation links
   - Check mobile responsiveness
   - Verify text contrast on new UI elements
