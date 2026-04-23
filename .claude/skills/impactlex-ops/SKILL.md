---
name: impactlex-ops
description: ImpactLex operations — regenerate seed snapshot, run AI rewrites, push to InstantDB, review contributions. Use when the user wants to update ImpactLex data, add terms, run content rewrites, or manage the glossary.
---

# ImpactLex Operations

ImpactLex is ImpactMojo's unified glossary at `/impactlex/`. It's backed by a seed JSON snapshot (offline-first) and optionally InstantDB (real-time + contributions). This skill covers the common operations.

## Architecture recap

- **App**: `/impactlex/index.html`, `app.js`, `styles.css`, `sw.js`, `manifest.webmanifest`, `term.html`, `review.html`
- **Data**: `/impactlex/data/seed-snapshot.json` (390 terms, 5 case studies, 10 formulae as of 2026-04)
- **Migration**: `scripts/impactlex-migrate.mjs`
- **AI rewrite**: `scripts/impactlex-ai-rewrite.mjs` + `scripts/prompts/impactlex-rewrite.md`
- **Lexicon embed** (for course pages): `/impactlex/lexicon-embed.js`
- **Backend**: InstantDB (keys `$INSTANTDB_APP_ID`, `$INSTANTDB_ADMIN_TOKEN`)

## Common operations

### Regenerate the seed snapshot (after adding/editing course lexicons)

```bash
# Local-only (parses 10 course lexicons)
node scripts/impactlex-migrate.mjs

# With external Varnasr/ImpactLex pull (fetches from GitHub raw)
node scripts/impactlex-migrate.mjs --with-external

# And push to InstantDB
INSTANTDB_APP_ID=... INSTANTDB_ADMIN_TOKEN=... node scripts/impactlex-migrate.mjs --with-external --push
```

Writes `/impactlex/data/seed-snapshot.json`. Commit after regenerating.

### Run an AI rewrite pass

```bash
# Rewrite first 5 seed terms for a dry run
node scripts/impactlex-ai-rewrite.mjs --limit 5

# Rewrite specific terms
node scripts/impactlex-ai-rewrite.mjs --only attribution,theory-of-change,rct

# Force a specific provider (default: gemini → grok → deepseek)
node scripts/impactlex-ai-rewrite.mjs --provider grok

# Full pass + push drafts to InstantDB
node scripts/impactlex-ai-rewrite.mjs --push
```

Drafts go into `seed-snapshot.json` with `status: "ai-draft"`, preserving the original in `seedDefinition`. Logs land in `scripts/logs/impactlex-rewrite-{date}.jsonl`.

### Review and publish drafts

1. Open `/impactlex/review.html` in the browser.
2. Enter a reviewer email (must be on `IMPACTLEX_CONFIG.adminEmails` in `/impactlex/index.html`).
3. Side-by-side diff: seed vs. AI draft. Edit inline. Approve → status becomes `published`.
4. To publish programmatically, flip `status` from `ai-draft` to `published` in the snapshot and push:

```bash
node -e "
const fs=require('fs');const p='impactlex/data/seed-snapshot.json';
const s=JSON.parse(fs.readFileSync(p));
s.terms=s.terms.map(t=>t.status==='ai-draft'?{...t,status:'published'}:t);
fs.writeFileSync(p,JSON.stringify(s,null,2));
"
```

### Add an InstantDB app ID

1. Create app at InstantDB dashboard (name: `impactlex`).
2. Capture app ID and admin token.
3. Add to `.claude/.env.keys`:
   ```
   INSTANTDB_APP_ID=...
   INSTANTDB_ADMIN_TOKEN=...
   ```
4. Update `/impactlex/index.html`:
   ```js
   window.IMPACTLEX_CONFIG = {
     instantDbAppId: 'your-app-id',
     snapshotUrl: '/impactlex/data/seed-snapshot.json',
     adminEmails: ['you@impactmojo.in'],
   };
   ```
5. Run the migrate script with `--push` to seed it.

### Full course-lexicon data swap (advanced, not yet executed)

The 10 course lexicon pages currently keep their hardcoded JS arrays. To swap them to query the shared DB:

1. Back up `courses/{slug}/lexicon.html`.
2. Replace the `const LEXICON = [...]` array body with a runtime fetch:
   ```js
   const LEXICON = await ImpactLexEmbed.fetchSnapshot()
     .then(d => d.terms.filter(t => t.courses.includes('{slug}')));
   ```
3. Test offline (snapshot cache) and online.

This is deferred until ImpactLex content is fully rewritten so course pages don't regress.

## Validation checklist (before ship)

- [ ] `python3 -m json.tool impactlex/data/seed-snapshot.json > /dev/null` passes
- [ ] `python3 -m json.tool data/search-index.json > /dev/null` passes
- [ ] No stale `on-web.link/ImpactLex` URLs: `grep -rn "on-web.link/ImpactLex" index.html README.md docs/ catalog.html` → 0 hits
- [ ] Count drift: "390" appears in index.html hero card + README + docs consistently (update all when terms grow past ~450, ~500, etc.)
- [ ] Pre-flight per brand-guidelines skill — viewport, GA, theme toggle, footer, favicons, Sargam icons
- [ ] Open `/impactlex/` in a browser, test: search, filter, open term modal, bookmark, deep-link, offline (DevTools → Network → Offline)
- [ ] Service worker registers (`navigator.serviceWorker.getRegistrations()` in console)

## Related

- `rules/api-conventions.md` for InstantDB credentials
- `rules/content-management.md` for the full cross-reference update checklist when the term count changes
- `skills/add-files` for adding new content types
- Backend decision doc: `/impactlex/BACKEND-DECISION.md`
