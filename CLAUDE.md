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
- **Labs**: Browser-based in `/Labs/*-lab.html`
- **Courses**: 19 flagship (`/courses/{name}/`), 58 foundational (`/101-courses/`, all native HTML decks; canonical count in `data/counts.json`)
- **Handouts**: 84 in `/Handouts/{Track}/`
- **Data**: JSON in `/data/` (search-index, dataverse, BCT repository)
- **Docs**: GitBook in `/docs/`
- **NotebookLM**: 12 AI Study Companion notebooks managed via `notebooklm-py`. Registry: `data/notebooklm-registry.json`. Script: `scripts/notebooklm-manage.py`

## Conventions

- Games: single self-contained HTML (inline CSS + JS, Indian folk art illustrations)
- Forms use Netlify Forms (`data-netlify="true"` with `netlify-honeypot="bot-field"`)
- Content counts: canonical values in `data/counts.json` — update there first, then `python3 scripts/check-counts.py` lists every stale occurrence (CI-enforced)

## Watch out for

- `index.html` is ~620KB — backup to `Backups/` before major changes
- Content counts in nav, hero, cards, sidebar — update ALL occurrences
- Stale `101.impactmojo.in` links — should point to self-hosted files
- `data/search-index.json` must stay valid JSON
- Update `docs/changelog.md` for user-facing changes
- **ImpactLex entries are not all equal, and the page now says so.** 159 of 494 terms are unreviewed `seed`, 226 were drafted by a language model, 460 have no citation. `impactlex/app.js` renders provenance on every term and offers a filter for it; `scripts/check-impactlex.py` keeps it wired and watches the offline snapshot's age. Do not regenerate that snapshot with `scripts/impactlex-migrate.mjs` — it would overwrite 385 curated definitions with the original import.
- **A colour token is either ink or a fill, and one token cannot be both.** `#0EA5E9` is 2.77:1 under white *and* 2.77:1 as ink on white; darkening it to fix a link makes the button it fills worse unless the ink moves with it. `css/imx-main.css` splits them: `--accent-color` is the brand sky for fills, borders and icons, `--accent-solid` (#0369A1) is a surface carrying white text, `--accent-ink` (#075985) is text on a light ground. Use the one that matches the job, and remember a token declared only in a dark block has **no value** in the light theme — `scripts/check-theme-tokens.py` catches that, nothing catches the rest. See `.claude/rules/testing.md` item 25.
- **The ink/fill token pair is `--im-ink-*` (flips with the theme) and `--im-fill-*` (a surface carrying white, never flips).** 36 Studios and 16 data explorers use them. A page that declares one palette and no dark block is the trap underneath: the site chrome paints the body dark while every token on it stays light.
- **Fixing a defect? File a `bug` issue first, then fix, then cite it as `(#NNN)` in `### Fixed`** — the public Known Issues page can only show what was filed. See `docs/bug-reporting.md`

## API Keys

`$GITHUB_PAT` · `$SUPABASE_PAT` · `$NETLIFY_PAT` · `$GAMMA_API_KEY` · `$GEMINI_API_KEY` · `$NAPKIN_API_KEY` · `$GROK_API_KEY` · `$DEEPSEEK_API_KEY` · `$SARVAM_API_KEY`

See `.claude/rules/api-conventions.md` for endpoints and auth patterns.

## Memory

Persistent project context lives in `.claude/memory.md` — carries state, decisions, and session logs across Claude Code sessions. Use `/memory` to read, update, or query it.

## .claude/ Structure

- **memory.md** — persistent context across sessions (project state, decisions, known issues, session log)
- **rules/** — modular instructions (code-style, content-management, api-conventions, testing)
- **commands/** — `/project:review`, `/project:fix-issue`, `/project:deploy-check`, `/project:audit`, `/project:add-game`
- **skills/** — auto-invoked workflows (add-files, housekeeping, github-ops, netlify-ops, supabase-ops, gamma-ops, gemini-ai, grok-ai, deepseek-ai, sarvam-ai, napkin-ai, threads-writer, blog-writer, dojo-ops, book-summaries, memory, frontend-design, seo, deep-research, debugging, tufte-viz)
- **agents/** — subagent personas (code-reviewer, content-auditor)
- **hooks/** — session-start (API key bootstrap), pre-tool-use (destructive command guard), stop (memory sync prompt)

## References (not loaded by default — saves tokens)

- **Community resources** (skills, MCP servers, repos): `.claude/references.md`
- **Claude Code best practices** (vendored guides): `.claude/vendor/claude-code-synthesis/` — sync with `/project:sync-guides`
- **Open-source AI catalog**: [alvinunreal/awesome-opensource-ai](https://github.com/alvinunreal/awesome-opensource-ai) — curated models, frameworks, tools & infrastructure (14 categories)
