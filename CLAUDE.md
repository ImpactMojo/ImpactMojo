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

## Memory

Persistent project context lives in `.claude/memory.md` — carries state, decisions, and session logs across Claude Code sessions. Use `/memory` to read, update, or query it.

## .claude/ Structure

- **memory.md** — persistent context across sessions (project state, decisions, known issues, session log)
- **rules/** — modular instructions (code-style, content-management, api-conventions, testing)
- **commands/** — `/project:review`, `/project:fix-issue`, `/project:deploy-check`, `/project:audit`, `/project:add-game`
- **skills/** — auto-invoked workflows (add-files, housekeeping, github-ops, netlify-ops, supabase-ops, gamma-ops, gemini-ai, grok-ai, deepseek-ai, sarvam-ai, napkin-ai, threads-writer, blog-writer, dojo-ops, book-summaries, memory, frontend-design, seo, deep-research, debugging)
- **agents/** — subagent personas (code-reviewer, content-auditor)
- **hooks/** — session-start (API key bootstrap), pre-tool-use (destructive command guard), stop (memory sync prompt)

## Community Resources

Curated skills, MCP servers, and repos worth tracking (sourced from [@zodchiii's roundup](https://x.com/i/status/2034924354337714642)):

### GitHub Repos to Watch
- [anthropics/skills](https://github.com/anthropics/skills) — Official Anthropic skills repository
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) — Curated community skills (22k+ stars)
- [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) — Security review skill
- [199-biotechnologies/claude-deep-research-skill](https://github.com/199-biotechnologies/claude-deep-research-skill) — Deep research patterns
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — Prompt/output testing
- [mendableai/firecrawl](https://github.com/mendableai/firecrawl) — Web scraping for content research
- [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) — AI project management
- [upstash/context7](https://github.com/upstash/context7) — Library docs injection MCP
- [tavily-ai/tavily-mcp](https://github.com/tavily-ai/tavily-mcp) — AI-native search MCP

### Notable Community Skills
- **Frontend Design** (277k+ installs) — UI generation patterns
- **Claude SEO** (12 sub-skills) — Search optimization
- **Systematic Debugging** — Structured troubleshooting
- **Context Optimization** — Better context window usage
- Browse more at [skillsmp.com](https://skillsmp.com)
