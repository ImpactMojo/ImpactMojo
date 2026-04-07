# Claude Memory — ImpactMojo

Persistent context that carries across Claude Code sessions. Updated automatically via the `memory` skill.

## Project State

- **Current content counts**: 16 Games, 11 Flagship Courses, 38 Foundational Courses (4 native HTML, 34 Gamma iframe), 400+ Handouts, 11 Labs, 27 Book Summaries
- **Last verified**: 2026-04-07
- **Deploy target**: Netlify (auto-deploy on push to main)
- **Backend**: Supabase project `ddyszmfffyedolkcugld`

## Recent Decisions

<!-- Append new decisions at the top -->
- **2026-04-07**: Theme system fully unified on `im-theme` localStorage key. `js/cookie-ui.js`, `js/account.js`, `js/game-shell.js` all read canonical first then fall back to legacy keys (`theme`, `impactmojo-theme`, `imx_theme`) for one-shot migration; all writes mirror to legacy keys. Never introduce a new theme key.
- **2026-04-07**: Device-mode default is the canonical theme pattern. `:root { LIGHT tokens }` + `@media (prefers-color-scheme: dark) { :root { DARK tokens } }` + explicit `body.{light,dark}-mode` + `[data-theme="*"]` overrides. Class overrides win via specificity. 70 pages converted; only `Games/climate-action-game.html` remains (custom earth-tone palette).
- **2026-04-07**: WCAG AA muted-text canon: `--text-muted` is `#52627A` in light (6.20:1) / `#94A3B8` in dark (6.96:1); `--text-secondary` is `#475569` light (7.58:1) / `#CBD5E1` dark (12.02:1). Never use `#94A3B8` for `--text-muted` in light or `#64748B` for it in dark.
- **2026-04-07**: 10 unbuilt course cards marked `comingSoon: true` with `url: null` instead of dead `101.impactmojo.in` mirror links. Never silently remap unresolvable slugs (`economics-101`, `vaniscribe`, `child-development`, `feminist-research`, `gender-mainstreaming`, `impact-eval`, `maternal-health`, `mixed-methods`, `survey-design`).
- **2026-04-07**: Housekeeping skill rewritten 169→922 lines and made globally available at `~/.claude/skills/housekeeping/`. Comprehensive checks + false-positive guidance + Parcel-bundle handling + enliven-repo workflow.
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

- **2026-04-07**: Brand cleanup + a11y baseline + housekeeping marathon. Shipped 7 PRs in one session (#350–#356) covering: handout 404s + 121 stale `101.impactmojo.in` link rewrites + theme-key unification + brand fonts + handout CC BY-NC-SA backfill (#350); 10 unbuilt course cards → "Coming Soon" with disabled card style (#351); `pull-requests: write` permission for axe-core + pa11y-ci sticky comment bot (#352); device-mode default theme on 70 pages + WCAG AA contrast bumps on 115 files + link-in-text-block underline + missing anchor id (#353); duplicate `im-topbar` removal on 28 pages where it was hiding the legacy `<header class="header">` main nav, with Premium link added back to 11 pages that lost it (#354); brand cleanup batch — device-mode for 37 dark-only pages, 39 emoji → Sargam line icons across 10 pages, 2 lexicon paper-plane + footer additions, language dropdown on 2 pages (#355); link-in-text-block underline rule on 71 more content pages (#356).
  
  Then ran exhaustive housekeeping in a single session:
  - Git: deleted 6 merged branches, pruned remote refs
  - Topbar sticky safety: ZERO direct `.im-topbar { position: sticky }` bugs
  - Backed up `index.html` → `Backups/index-backup-20260407-1001-after-brand-cleanup.html`
  - Fixed **61 count drifts** across 28 files (9→11 flagship, 39→38 foundational, 10→11 Labs, 15→16 Games) including parenthetical forms in `docs/platform-overview.md`, `docs/content-catalog.md`, `docs/faq.md`, `README.md`
  - CHANGELOG.md v10.14.0 + docs/changelog.md user-facing summary
  - ROADMAP.md Q2 2026 updated with completed items + open follow-ups
  - **Google Analytics G-JRCMEB9TBW added to 69 pages** (38 101-courses, 16 Games, 11 BookSummaries, 2 courses, 1 blog post, 1 lexicon)
  - **SEO baseline added to 187 content pages** — 100% coverage now: meta description, canonical, robots, OG (title/description/image/url/type/site_name), Twitter card. Special handling for 17 Parcel-bundled BookSummaries with no `<head>` tag.
  - JSON + sitemap validated clean
  - **Rewrote `.claude/skills/housekeeping/SKILL.md` from 169 → 922 lines** with comprehensive new sections: count-drift audit script, false-positive avoidance principles, brand identity audit, duplicate-header detection allowlist, WCAG AA token reference, emoji→Sargam mapping, Parcel-bundle handling, "enliven repo" living-doc sync, content-type-specific add checklists, efficient execution order. Added YAML frontmatter so the skill description is properly indexed by Claude Code.
  - **Made housekeeping skill globally available** by also installing it at `~/.claude/skills/housekeeping/SKILL.md` (now invokable from any session, any repo on this machine, with a fallback path). Both copies kept in sync.
  
  **Key learnings captured in the new skill:**
  - Always start with a tight allowlist for find-and-replace, not a broad denylist (the duplicate-topbar over-correction taught this — `.v3-organic-bg`, `.reading-progress`, `<th>`, `.result-flash` are NOT navigation)
  - Test on ONE file first, verify diff, THEN run across the repo
  - Compare imbalance against HEAD (delta=0), not absolute, since some files have pre-existing imbalances
  - Skip emoji/string matches inside `<!-- comments -->`, `<script>`, `<style>`, `<svg>`, and `Backups/`
  - The canonical theme localStorage key is `im-theme` — never introduce a new one
  - Handout pages (84) and main site pages use SEPARATE topbar templates and that's correct; never auto-add `im-topbar` to a page that already has a real `<header>` main nav
  - Unresolvable course slugs (`economics-101`, `vaniscribe`, etc.) should stay marked `comingSoon: true`, never silently remap to unrelated content
  - 6 course pages have pre-existing `<div>` imbalances in HEAD — leave them alone unless explicitly asked
  
  **Known gaps flagged for future sessions:**
  - `Games/climate-action-game.html` is the last dark-only page — uses earth-tone palette `#F5F0EB` and needs designer-authored light tokens
  - Some pages have layered topbar conflicts (im-topbar + nav element at top:0) that cause cosmetic z-index hiding but aren't critical bugs — the earlier removal attempt was too aggressive and caught false positives
  - Wiki sync (`ImpactMojo/ImpactMojo.wiki.git`) not done this session — pending
