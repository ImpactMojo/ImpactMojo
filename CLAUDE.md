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
- **NotebookLM**: 11 AI Study Companion notebooks managed via `notebooklm-py`. Registry: `data/notebooklm-registry.json`. Script: `scripts/notebooklm-manage.py`

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

Curated skills, MCP servers, and repos worth tracking (sourced from [@zodchiii's Top 50 roundup](https://x.com/i/status/2036832679895740788), 6.6M views):

### Official Anthropic Skills (install from [anthropics/skills](https://github.com/anthropics/skills))
- **PDF Processing** — Read, extract tables, fill forms, merge/split
- **DOCX** — Create & edit Word docs with tracked changes
- **PPTX** — Slide decks from natural language (charts, speaker notes)
- **XLSX** — Formulas, analysis, charts via plain English
- **Doc Coauthoring** — Collaborative document editing
- **Frontend Design** (277k+ installs) — Real design systems, bold typography
- **Canvas Design** — Social graphics, posters, covers (PNG/PDF out)
- **Algorithmic Art** — Fractal patterns, geometric compositions via p5.js
- **Theme Factory** — Batch-generate color schemes from one prompt
- **Web Artifacts Builder** — Calculators, dashboards via natural language
- **Skill Creator** — Meta-skill: describe a workflow, get a SKILL.md in 5 min
- **Brand Guidelines** — Encode your brand into a skill, auto-applies everywhere

### Community Skills
- **Superpowers** (96k+ stars) — 20+ battle-tested skills: TDD, debugging, plan-to-execute. [obra/superpowers](https://github.com/obra/superpowers)
- **Claude SEO** (12 sub-skills) — Full-site audits, schema validation. [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)
- **Systematic Debugging** — Root cause analysis first, fix second
- **Context Optimization** — Reduce token costs, KV-cache tricks. [muratcankoylan/agent-skills-for-context-engineering](https://github.com/muratcankoylan/agent-skills-for-context-engineering)
- **Marketing Skills** — 20+ skills: CRO, copywriting, SEO, growth. [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)
- **File Search** (massgen) — Ripgrep + ast-grep mastery. [massgen/massgen](https://github.com/massgen/massgen)
- **Remotion Best Practices** — AI video generation (117k weekly installs). [remotion-dev/remotion](https://github.com/remotion-dev/remotion)
- Browse 80k+ at [skillsmp.com](https://skillsmp.com) · [aitmpl.com/skills](https://aitmpl.com/skills) · [skillhub.club](https://skillhub.club)

### MCP Servers
- [tavily-ai/tavily-mcp](https://github.com/tavily-ai/tavily-mcp) — AI-native search (not just links — synthesized answers)
- [upstash/context7](https://github.com/upstash/context7) — Library docs injection (Supabase, React, etc.)
- [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) — Manipulate Excel without Excel
- [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) — Browser automation for LLMs
- [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) — PDFs, images, audio → Markdown
- [jlowin/fastmcp](https://github.com/jlowin/fastmcp) — Build MCP servers in minimal Python
- [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) — Codebase → persistent knowledge graph

### GitHub Repos to Watch
- [anthropics/skills](https://github.com/anthropics/skills) — Official Anthropic skills repository
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) — Curated community skills (22k+ stars)
- [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) — Security review skill
- [199-biotechnologies/claude-deep-research-skill](https://github.com/199-biotechnologies/claude-deep-research-skill) — Deep research patterns
- [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) — AI project management (PRD → structured tasks)
- [mendableai/firecrawl](https://github.com/mendableai/firecrawl) — Any website → LLM-ready data
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — Prompt/output testing + security testing
- [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) — Autonomous research → compiled reports
- [vanna-ai/vanna](https://github.com/vanna-ai/vanna) — Natural language → SQL
- [karpathy/rendergit](https://github.com/karpathy/rendergit) — Git repo → single file for humans and LLMs
- [github/spec-kit](https://github.com/github/spec-kit) — Spec-driven dev (50k+ stars)

## Claude Code Best Practices (Vendored)

General-purpose Claude Code operating guides synced from [griffinhilly/claude-code-synthesis](https://github.com/griffinhilly/claude-code-synthesis). Load on demand — not always in context.

- **Operating model**: `.claude/vendor/claude-code-synthesis/CLAUDE.md`
- **Guides**: `.claude/vendor/claude-code-synthesis/guides/` (shell-rules, delegation-templates, skills-reference, context-efficiency, postgres-batching, overnight-runner, prefer-apis, bookmark-archive)

Sync with: `/project:sync-guides`
