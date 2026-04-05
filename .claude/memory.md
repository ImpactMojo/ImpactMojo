# Claude Memory — ImpactMojo

Persistent context that carries across Claude Code sessions. Updated automatically via the `memory` skill.

## Project State

- **Current content counts**: 16 Games, 9 Flagship Courses, 39 Foundational Courses (4 native HTML, 34 Gamma iframe), 400+ Handouts, 11 Labs, 27 Book Summaries
- **Last verified**: 2026-04-05
- **Deploy target**: Netlify (auto-deploy on push to main)
- **Backend**: Supabase project `ddyszmfffyedolkcugld`

## Recent Decisions

<!-- Append new decisions at the top -->
- **2026-04-05**: Native 101 slide decks replace Gamma iframes. Workflow: Claude Chat generates 100-slide HTML → user pastes/pushes → Claude Code fixes JS bugs (viewport split after s50, newlines in chart labels, chartsInit order) and applies CSS formatting (inline font bumps, fill overrides). 4 decks live: dev-economics, mel-basics, climate-essentials, inequality-basics. Shared template at `101-courses/native/shared/deck.css` + `deck.js`. CSS overrides needed because Claude Chat output uses inline `style=""` with small font sizes that class rules can't override.
- **2026-03-24**: Added 14 new tools to Dataverse (247→261): Tavily MCP, Context7 MCP, Promptfoo, Ollama, LangGraph, CrewAI, DSPy, Pydantic AI to Developer Infra; dlt, n8n, Langflow, Dify to Data Infra. Created MCP servers reference at `.claude/mcp-servers.md`. Added 4 new skills (frontend-design, seo, deep-research, debugging) inspired by @zodchiii's curated AI tools roundup. Added community resources section to CLAUDE.md with GitHub repos to watch and notable community skills. Total skills now: 20.

## Known Issues

<!-- Track recurring problems and workarounds -->
- `index.html` is ~620KB — always backup before major edits
- Content counts are hardcoded in 4+ locations — grep before updating
- Some `101.impactmojo.in` links are stale — migrate to self-hosted paths

## Session Log

<!-- Auto-appended by memory skill: date, summary of what was done -->
- **2026-04-05**: Native 101 deck project. Created shared CSS/JS template. Converted 4 foundational decks from Gamma iframe to native HTML (dev-economics, mel-basics, climate-essentials, inequality-basics). Fixed viewport split bug (slides 51-100 outside viewport div), JS newline syntax errors in chart labels, chartsInit declaration order. Applied CSS fill overrides (larger fonts, padding, gaps) and inline style font-size bumps across all 4 decks. Fixed CTA "Full Course" → "Flagship Course". Ran full housekeeping: updated CHANGELOG v10.13.0, docs/changelog, 101-decks-guide, README, ROADMAP (Q2 in progress), search-index (+3 entries → 488), sitemap (+3 URLs). Fixed position:sticky topbar across 78 pages. Posted GitHub Discussion #348. Git cleanup: deleted feature branch, pruned remotes.
