# Content Management

When adding or modifying content:

- Backup `index.html` to `Backups/` before major changes
- Update content counts in ALL locations (nav, hero, feature cards, sidebar) — grep to find them
- Add new content to `data/search-index.json` with proper id, title, description, type, category, url, tags
- Update relevant docs: `docs/games-guide.md`, `docs/labs-guide.md`, `docs/content-guide.md`
- Update `docs/changelog.md` for user-facing changes
- Update `sitemap.xml` for new pages
- Check for stale `101.impactmojo.in` links that should point to self-hosted files
- All forms must submit to Formspree endpoint `xpwdvgzp`
