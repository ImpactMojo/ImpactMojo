# Claude Memory — ImpactMojo

Persistent context that carries across Claude Code sessions. Updated automatically via the `memory` skill.

## Project State

- **Current content counts**: 16 Games, 9 Flagship Courses, 39 Foundational Courses, 400+ Handouts, 10 Labs, 3 Book Summaries
- **Last verified**: 2026-03-22
- **Deploy target**: Netlify (auto-deploy on push to main)
- **Backend**: Supabase project `ddyszmfffyedolkcugld`

## Recent Decisions

<!-- Append new decisions at the top -->
- **2026-03-26**: Major SEO upgrade — sitemap 76→119 URLs, added meta descriptions/canonical/OG/Twitter cards to 16 Games + 23 BookSummaries, added JSON-LD LearningResource schema to 16 Games + Course schema to 11 courses. SEO score ~6.5→8.5. Created `docs/seo-strategy.md` with content marketing funnel framework. Remaining SEO gaps: Labs OG tags, blog Article schema, FAQ schema, hreflang tags.
- **2026-03-24**: Added 14 new tools to Dataverse (247→261): Tavily MCP, Context7 MCP, Promptfoo, Ollama, LangGraph, CrewAI, DSPy, Pydantic AI to Developer Infra; dlt, n8n, Langflow, Dify to Data Infra. Created MCP servers reference at `.claude/mcp-servers.md`. Added 4 new skills (frontend-design, seo, deep-research, debugging) inspired by @zodchiii's curated AI tools roundup. Added community resources section to CLAUDE.md with GitHub repos to watch and notable community skills. Total skills now: 20.

## Known Issues

<!-- Track recurring problems and workarounds -->
- `index.html` is ~620KB — always backup before major edits
- Content counts are hardcoded in 4+ locations — grep before updating
- Some `101.impactmojo.in` links are stale — migrate to self-hosted paths

## Session Log

<!-- Auto-appended by memory skill: date, summary of what was done -->
- **2026-03-26**: SEO & Content Marketing session. Fixed sitemap (76→119 URLs: +18 blog, +2 courses, +23 BookSummaries). Added SEO meta tags (description, canonical, OG, Twitter) to 16 Games + 23 BookSummaries. Added JSON-LD structured data to 16 Games (LearningResource) + 11 Courses (Course). Updated docs/changelog.md (v10.9.2). Created docs/seo-strategy.md with content marketing funnel strategy, keyword clusters, and long-form sales letter framework. Branch: claude/seo-content-marketing-GtsUG.
