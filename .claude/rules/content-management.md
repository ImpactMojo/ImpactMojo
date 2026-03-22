# Content Management

When adding or modifying content:

1. **Backup first**: `cp index.html Backups/index-backup-$(date +%Y%m%d-%H%M).html`
2. **Update content counts** in ALL locations — grep to find them:
   ```bash
   grep -rn "16 Games\|16 games" index.html catalog.html docs/
   ```
3. **Add to search index** (`data/search-index.json`):
   ```json
   {"id": "GAME017", "title": "...", "description": "...", "type": "game", "category": "...", "url": "/Games/...", "tags": [...]}
   ```
4. **Update docs**: `docs/games-guide.md`, `docs/labs-guide.md`, `docs/content-guide.md` as relevant
5. **Update changelog**: `docs/changelog.md` for user-facing changes
6. **Update sitemap**: add `<url>` entry to `sitemap.xml`
7. **Update catalog**: `catalog.html` / `catalog_data.json` for courses
8. **Check stale links**: `grep -rn "101.impactmojo.in" index.html courses/` for refs that should be self-hosted
9. **Validate forms**: all forms submit to Formspree endpoint `xpwdvgzp`
10. **GitHub Wiki**: clone `Varnasr/ImpactMojo.wiki.git`, update affected pages (Content-Guide, Changelog, type-specific pages), push
11. **GitHub Discussion**: create Announcements post for significant new content (games, courses, book summaries)
12. **GitHub Issues**: close related tracking issues with commit/PR links

## Related

- Skill `add-files` has a full matrix of which updates are needed per content type
- Skill `housekeeping` runs the complete post-change checklist
- Agent `content-auditor` verifies consistency across all files
- Command `/project:deploy-check` validates everything before deploy
- See `rules/testing.md` for grep commands and validation steps
