# ImpactMojo

Free development education platform for South Asia. Static HTML/CSS/JS, Supabase backend, Netlify hosting.

## Commands

```
# No build step — static site, auto-deploys on push to main via Netlify
# Tests: open HTML files directly in browser
```

## Architecture

- **Site**: impactmojo.in
- **Games**: Self-contained HTML in `/Games/` (single file, no deps)
- **Labs**: Browser-based in `/courses/*-lab.html`
- **Courses**: 9 flagship (`/courses/{name}/`), 39 foundational (catalog)
- **Handouts**: 400+ in `/Handouts/{Track}/`
- **Data**: JSON in `/data/` (search-index, dataverse, BCT repository)
- **Docs**: GitBook in `/docs/`

## Conventions

- Games: single self-contained HTML (inline CSS + JS, Indian folk art illustrations)
- Forms submit to Formspree endpoint `xpwdvgzp`
- Content counts hardcoded in multiple places — grep before updating

## Watch out for

- `index.html` is ~620KB — backup to `Backups/` before major changes
- Content counts in nav, hero, cards, sidebar — update ALL occurrences
- Stale `101.impactmojo.in` links — should point to self-hosted files
- `data/search-index.json` must stay valid JSON
- Update `docs/changelog.md` for user-facing changes

## API Keys

`$GITHUB_PAT` · `$SUPABASE_PAT` · `$NETLIFY_PAT` · `$GAMMA_API_KEY` · `$GEMINI_API_KEY` · `$NAPKIN_API_KEY` · `$GROK_API_KEY` · `$DEEPSEEK_API_KEY` · `$SARVAM_API_KEY`

See `.claude/rules/api-conventions.md` for endpoints and auth patterns.

## .claude/ Structure

- **rules/** — modular instructions (code-style, content-management, api-conventions, testing)
- **commands/** — `/project:review`, `/project:fix-issue`, `/project:deploy-check`, `/project:audit`, `/project:add-game`
- **skills/** — auto-invoked workflows (add-files, housekeeping, github-ops, netlify-ops, supabase-ops, gamma-ops, gemini-ai, grok-ai, deepseek-ai, sarvam-ai, napkin-ai, threads-writer)
- **agents/** — subagent personas (code-reviewer, content-auditor)
- **hooks/** — session-start (API key bootstrap), pre-tool-use (destructive command guard)
