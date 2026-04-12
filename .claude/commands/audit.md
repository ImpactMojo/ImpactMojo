---
description: Run a full content consistency audit across the platform
---

Spawn the `content-auditor` agent to verify:

1. Game count matches across `index.html`, `catalog.html`, `docs/games-guide.md`, `README.md`
2. Lab count matches across the same files
3. Course count matches across the same files
4. Every `.html` file in `/Games/` has an entry in `data/search-index.json`
5. Every `*-lab.html` in `/courses/` has an entry in `data/search-index.json`
6. `data/search-index.json` is valid JSON
7. No broken internal links in `index.html`
8. No stale `101.impactmojo.in` references that should be self-hosted
9. `sitemap.xml` includes all public pages
10. All forms use Netlify Forms (`data-netlify="true"` with unique `name` attribute)

Report discrepancies with specific file paths and line numbers. Summarize pass/fail for each check.
