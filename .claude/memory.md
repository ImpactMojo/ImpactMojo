# Claude Memory — ImpactMojo

Persistent context that carries across Claude Code sessions. Updated automatically via the `memory` skill.

## Project State

- **Current content counts**: 16 Games, **12 Flagship Courses** (Public Choice added v10.23), 38 Foundational Courses (4 native HTML, 34 Gamma iframe), 85 Handouts, 11 Labs, **31 BookSummary companion pages** (50 *.html files including interactive variants), **5 Deep Dives** (new content type, v10.22), 28 Blog Posts, 47 top-level HTML pages, **6 Reference Libraries** (ImpactLex, DevDiscourses, FieldCases, PolicyDhara, Dataverse, NudgeKit)
- **Last verified**: 2026-05-01
- **Sitemap coverage**: 173+ URLs (added Public Choice + lexicon)
- **Catalog coverage**: 128 items across 9 content types (was 85 across 6 before v10.23.1)
- **Deploy target**: Netlify (auto-deploy on push to main, HTML now edge-cached for 5 min)
- **Backend**: Supabase project `ddyszmfffyedolkcugld`
- **Edge functions**: `netlify/edge-functions/policydhara.ts` + `devdiscourses.ts` proxy GitHub Pages content with `<base>` injection

## Known drift (open)

- `data/search-index.json` has only ~9 BookSummary / reference entries vs **31 BookSummaries + 6 Reference Libraries** now in catalog. Search-index backfill is a separate maintenance task — flagged but not done in v10.23.1.
- `data/search-index.json` doesn't include Public Choice (missed during pubchoice launch).
- BookSummary catalog title for `gog-companion.html` reads "The Great Greenwashing" — wrong; gog is The Goal by Goldratt. One title-string review pass would catch others like this.

## Recent Decisions

<!-- Append new decisions at the top -->
- **2026-05-01 (later same day — Group 1 audit follow-through)**: Catalog overhaul + Browse access on inner pages. Closed all 4 open items from morning audit. 133 files changed in one commit (`951e9c9`):
  - **Catalog** (`catalog.html`): now indexes 128 items across 9 content types (was 85 across 6). Added 4 missing games (digital-ethics, public-health, climate-action, gender-equity), 1 missing lab (gender-studies), 31 BookSummaries with hand-written 1-line descriptions, 6 Reference Libraries (one card per platform: ImpactLex, DevDiscourses, FieldCases, PolicyDhara, Dataverse, NudgeKit), and 1 collective Handouts entry → /handouts.html. New filter chips: Book Companions (31), Reference (6), Handouts. Bumped Labs chip 10→11. Added 3 new `.card-type` colour rules with light + dark variants.
  - **Browse access from inner pages**: Course pages, BookSummaries, DeepDives, lexicons, premium-tools, etc. only had a minimal im-topbar with logo + Premium button. Users couldn't reach the catalog from a course page. Injected an `<a class="im-browse-btn" href="/catalog.html">Browse</a>` into the `im-topbar` of 132 inner pages, just left of the Premium button. Used a Python regex to find files containing `class="im-premium-btn"` and inserted the link + a small `.im-browse-btn` CSS rule inline. Homepage skipped (has the full nav with Specials dropdown).
  - **Decision**: Don't add 400+ individual Handouts to catalog allContent — would bloat the JS array. Single collective entry → /handouts.html keeps catalog browseable.
  - **Decision**: Reference Libraries get one card per platform (not one card per item) since each is its own searchable surface.
  - **Reusable learning**: Use Python with `git ls-files` (not `find`) to enumerate tracked HTML files for bulk injection; safely handles paths-with-spaces by avoiding shell `.split()`.
- **2026-05-01 (Public Choice launch + perf overhaul + nav fixes)**: Major session, 26 commits to main. Highlights:
  - **Public Choice flagship** added as the 12th flagship course at `/courses/pubchoice/`. Title aligned to flagship pattern: "Public Choice: Decisions, Incentives & Institutions" (matches "Public Policy: Process, Design & Governance"). Indigo gradient card. 13 modules imported to Supabase `course_content` table — table is `course_content` not `modules` (deployment notes were wrong). Module 1 only has `is_preview=true` to match convention used by other flagships.
  - **CSS extraction perf win**: Pulled 215 KB of inline `<style>` (4 head blocks) out of `index.html` into `/css/imx-main.css`. HTML brotli wire size 96 KB → 64 KB. Cascade preserved by concatenating in document order. Body-position `<style>` blocks (5, 14 KB total) left inline because cascade-position-sensitive.
  - **HTML edge cache**: Added `[[headers]]` for `/*.html` and `/` in `netlify.toml`: `public, max-age=300, must-revalidate`. TTFB dropped from 1.4s → 175 ms (8×). Was previously `max-age=0, must-revalidate`. Auto-purge on deploy means freshness is preserved.
  - **Eliminated `on-web.link`** from all live pages. Replaced `_redirects` proxies with **Netlify Edge Functions** because `_redirects` rules can't differentiate trailing-slash forms (Netlify normalises) → caused redirect loops AND blank pages (relative asset paths broke). Edge functions proxy `varnasr.github.io/PolicyDhara` and `varnasr.github.io/development-discourses`, inject a `<base href>` into HTML so relative paths resolve. Updated 4 pages that linked to old `on-web.link/DevDiscourses`.
  - **Specials nav redesigned** as 4-section accordion (Reference Libraries / Long-form Reading / Practice & Programs / Behind the Scenes), all collapsed by default, single-open behaviour. CSS appended to extracted `imx-main.css`. Mobile cap (`max-height: 500px`) was clipping accordion items — lifted for `.specials-grouped` specifically.
  - **Navigation bug chain solved**: ALL Specials links now absolute (`/#flagship-courses`, `/#case-studies`, `/#dev-discourses`, `/dataverse.html`, `/challenges.html`). The actual blocker was **`js/router.js` matching path `/` to the `home` route and overriding the hash** — fixed by checking `window.location.hash` first in `handleRoute()`. Hash always wins over path-based default route. Same fix benefits all hash-based nav.
  - **Mobile margin safety net** appended to `imx-main.css`: forces `padding-left/right: 1.25rem` on top-level sections, named `imx-*` sections, and id'd sections. Tightens to 1rem at ≤380px. Card grids collapse to single column. Worst offender was `.imx-libraries-grid-section` (was `padding: 2rem 0`).
  - **Public Choice hero**: 3 inline `color: rgba(255,255,255,...)` elements were invisible on light bg. Switched to `var(--color-text-secondary)` / `var(--color-text)`. Boundary callout strong/link wrapped in `.pubchoice-boundary-strong` class with theme-aware amber (#92400E light / #FCD34D dark).
  - **DevEcon CSS shim**: `var(--indigo)`, `--cyan`, `--orange`, `--success` referenced 17 times but never defined. Added to all 4 :root / theme blocks. Same bug pattern that was fixed in pubchoice earlier.
  - **Catalog WCAG fix**: `.track-filter.active` was sky-500 on sky-500-at-20% (~2.8:1, fails AA). Switched to amber-700 light / sky-300 dark.
  - **`js/faq-bank.js` line 167** had stray `""` mid-string — killed file parsing. Fixed.
  - **PolicyDhara link** updated from `https://on-web.link/PolicyDhara` to `https://www.impactmojo.in/policydhara` on the homepage card. Also changed `#policy-dhara` anchor in nav to `/policydhara`.
  - **Bylines for Deep Dives**: Sukhmeet Bedi role corrected from "Founder, ImpactMojo" to "Series Editor — Deep Dives" (user is the founder, not Sukhmeet). 3 of 5 Deep Dives now bylined "ImpactMojo Editorial / House Pick" instead of all-Sukhmeet.
  - **Key reusable learnings:**
    - Netlify `_redirects` normalises trailing slashes when matching → can't reliably differentiate `/foo` from `/foo/` for proxy rules. Use Edge Functions when you need exact-form matching.
    - When proxying a third-party HTML page through Netlify, inject `<base href="/your-path/">` into the HTML or its relative asset URLs will resolve against the wrong base and the page will render unstyled.
    - Site-wide JS routers can override browser-native hash navigation. Always check `window.location.hash` BEFORE matching path → route in any client router.
    - Capture-phase click handlers + `stopPropagation` will block bubble-phase mobile-menu-close handlers. If you need to force navigation on capture, also explicitly close any UI that's expected to dismiss on click.
    - Inline `style="color: rgba(255,255,255,...)"` on hero text is the most common dark-mode-residue bug — pages designed for a dark hero get re-skinned to light without removing white text.
    - When extracting inline `<style>` to external file, preserve document order. Brace-balance check is a fast sanity test.
    - 215 KB CSS extraction also saves brotli bytes (96 KB → 64 KB) and lets browsers parallelise download.
- **2026-04-29 (Deep Dives content type launch)**: New content type `Deep Dives` at `/DeepDives/` — themed annotated reading lists curated by named scholars/practitioners. 5 starter lists (Indian Political Economy, Impact Measurement, Climate & Just Transitions, Caste & Identity, Data & Power), bylined as Sukhmeet Bedi (Editor's Pick × 2) or ImpactMojo Editorial (House Pick × 3). Brand-aligned: Sargam icons (no emojis), Amaranth body / Inter headings, paper plane SVG, skip link. Supporting infra: `/data/deep-dives.json` registry, landing page with topic filters, per-list HTML template, shared CSS/JS, sitemap entries, search-index entries, catalog filter chip "Deep Dives (5)", homepage section card grid, nav dropdown link. Inspired by CASI Deep Dive series (credit removed in subsequent commit per user request).
- **2026-04-28 (global Claude Code + infra)**: Added Supabase user `taranga.sriraman@gmail.com` (org tier, learner role, ID: `b8726430-c343-408f-820d-cb0322aca632`). Promoted 16 general-purpose skills to global `~/.claude/` (gemini/grok/deepseek/sarvam/github/netlify/supabase/gamma/napkin/pdf/pptx/frontend-design/web-artifacts/seo/deep-research/memory). 8 project-specific stay in `.claude/`. Vendored griffinhilly/claude-code-synthesis to `~/.claude/vendor/` with `/sync-guides`. Housekeeping expanded: step 11 (GA `G-JRCMEB9TBW`), step 12 (10-element branding check). Added alvinunreal/awesome-opensource-ai to dataverse (#271) + CLAUDE.md. LinkedIn article drafted. Version: v10.21.0.
- **2026-04-12 (docs/README/roadmap refresh)**: Second housekeeping pass. README.md: labs 19→11 (split into Labs/Tools/Premium), added Gender Studies + Public Policy flagships, added BookSummaries (28) + AI Study Companions (11), Formspree→Netlify Forms, version→10.18.0. Marketing kit: 15→16 games, 10→11 labs, 9→11 flagship across ~20 locations. PressKit: 39→38 foundational. Roadmap: moved 5 completed items, added v10.13–v10.18 history. GitHub: closed Q1 milestone, replied to #361 contributor, updated #272 BookSummaries target to 40+. 9 Dependabot PRs still open (CI bumps + deps).
- **2026-04-12 (service consolidation + engagement pipeline)**: Major session — consolidated from 3 services to 2 (eliminated Formspree), built full engagement pipeline from scratch. Key changes:
  - **Formspree → Netlify Forms**: 12 forms migrated, `ignore_html_forms` was `true` in Netlify (turned on via API), email notifications configured for all 12 forms to info@impactmojo.in via hooks API.
  - **Resend email integration**: API key `re_EjPJ...` configured in Supabase secrets. Domain `impactmojo.in` verified with DKIM/SPF/DMARC DNS records added via Netlify DNS API. Free tier: 3K emails/month.
  - **Notifications infrastructure**: `notifications` + `notification_preferences` tables applied to production (migration existed but was never run). 14 users backfilled. `notify_user()` function, `update_streak()` function, auto-preference trigger all live.
  - **Engagement drip**: 5-email sequence (Day 0/3/7/14/21) with deduplication via `metadata.drip_stage`. Day 21 pitches Premium + one-time support. 63 emails sent to 15 users.
  - **Streak tracking**: `auth.js` calls `update_streak()` RPC on every profile fetch. Increments on daily login, resets on miss.
  - **Certificate upsell**: `issue-certificate` Edge Function sends branded congrats email with premium mention for free-tier users.
  - **Monthly newsletter**: `netlify/functions/monthly-newsletter.mjs` runs 15th at 10:00 IST, auto-generates from `docs/changelog.md` + `search-index.json`.
  - **Daily cron**: `netlify/functions/daily-engagement.mjs` at 08:00 IST runs drip + streak-reminders + cohort-deadlines.
  - **New pages**: `/premium-letter.html` (long-form sales letter), `/starter-kit.html` (10 curated handouts).
  - **Branded email template**: Navy gradient header, stacked logo, amber accent bar, dark footer.
  - **Test user**: `connectwithvarna@gmail.com` created (password: `ImpactMojo2026!`).
  - **Supabase usage**: 15 MB database, 15 users, 0 paying subscribers — well within free tier.
  - **Branch cleanup**: 20 stale remote branches deleted via GitHub API.
  - **Known issue**: 39 files have `.im-topbar { position: sticky }` conflict — pre-existing, not introduced this session.
- **2026-04-12 (repo housekeeping)**: Comprehensive platform audit and cleanup. Sitemap 84→171 URLs (added 2 courses, 35 foundational, 23 BookSummaries, 18 blog posts, 9 public pages). Migrated ~100 stale `101.impactmojo.in` links to local paths across 4 JS files + 4 docs. Cleaned search-index.json: removed 6 phantom lab entries, added 3 missing labs (17→13 entries). Fixed count drifts in content-guide.md (flagship 9→11, labs 19→11), premium.html, catalog.html comments. Removed 21 .DS_Store files from tracking. Updated content-catalog.md with correct local paths for all 38 foundational courses. Branch: `claude/consolidate-netlify-services-db6pS`.
- **2026-04-08 (post-merge housekeeping)**: After landing PR #368 (homepage count drift + Track Quiz + validate-json hook rewrite) and PR #370 (accessibility statement page + README badges + UserWay statement_url), ran the housekeeping skill. Findings: count drift clean (3 hits all false positives — canonical values or historical changelog); §9a topbar-sticky check returned 10 false positives (all `.im-topbar { position: fixed }` correctly, sticky matched elsewhere — table headers etc.); §11 stale `101.impactmojo.in` links found 2 real bugs in `toc-builder.html:553,558` (TOC Lab and MEL Planning Lab pointing to legacy mirror) — fixed to `/Labs/toc-lab.html` and `/Labs/mel-plan-lab.html`; §7 SEO baseline missing `<link rel="canonical">` and `<meta name="robots">` on the new accessibility.html — added both. Branch: `claude/housekeeping-april-8`. Also confirmed: WCAG 2.1 AA conformance is now formally documented at `/accessibility.html` and the UserWay widget surfaces it via `data_statement_url`.
- **2026-04-08**: Fixed count drift sitewide after user feedback flagged about.html (39/10/12) vs index.html (48/11/16) mismatch. Corrected `about.html`, `catalog.html` (hero + meta + flagship filter chip), `transparency.html`, `org-dashboard.html`, `404.html`, `podcast.html`, Supabase signup/invite email templates, and `docs/{labs-guide,terms-guide,roadmap}.md` — all now show canonical 48 courses / 11 labs / 16 games / 11 flagship. Also added 3 missing flagship cards (Constitution & Law, Public Policy, Gender Studies) to `catalog.html` JS data (they were on the homepage but absent from the searchable catalog). **Learning Track Quiz** promoted from section #6 to directly below the hero at ~L8990 (was L10113); added a tertiary hero CTA "Not sure? Take the 5-question quiz →" linking to `#quiz` at L8956 using the existing `v3-premium-link` class (no new CSS). Branch: `claude/fix-homepage-inconsistencies-SGaT6`. Known remaining drift: catalog.html JS still has `c1-c39` foundational entries (canonical 38) and only 10/12 lab/game entries — a separate issue to open.
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
- **Supabase inactivity risk mitigated**: Supabase pauses/deletes inactive free-tier projects after ~1-2 weeks. Mitigations in place:
  - `netlify/functions/daily-engagement.mjs` hits Edge Functions daily at 02:30 UTC
  - `netlify/functions/supabase-keepalive.mjs` hits Auth/DB/Storage APIs weekly at 03:17 UTC Sundays (redundancy)
  - Requires `SUPABASE_SERVICE_ROLE_KEY` env var set in Netlify dashboard
  - With both functions live, downgrading to free tier should be safe
- **Chamber petition (AOR) lives in `Varnasr/Experiments/chamber-petition/`**: Migrated from Supabase to Netlify Forms on 2026-04-16, then moved out of impactmojo/impactmojo to Varnasr/Experiments as a sandbox project. Netlify site: `chamber-petition` (id `6581a696-c2d1-4a16-bcdf-681dc517762b`) is now linked to that repo (base_dir=`chamber-petition`, deploy_key_id=`69e0d3654796c31483fe0aa4`, GitHub deploy_key=`148764262`) — pushes to Varnasr/Experiments `main` trigger auto-deploy. Form `aor-petition` (id `69e0c835009c6c0008de271a`) routes to devvrat.SCAORA@gmail.com (hook `69e0c8a0add950870abd4b78`). No standalone GitHub repo ever existed for this project. 67-signature backup preserved in the subfolder.

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

- **2026-04-07 (continued)**: Workflow correctness + axe baseline clear marathon. Shipped PR #358 (housekeeping batch, replacing earlier #357) and PR #359 (8-pass a11y baseline clear).

  **#358 (housekeeping):**
  - 213 files: 61 count drift fixes across 28 files, CHANGELOG v10.14.0, ROADMAP Q2 update, 100% Google Analytics coverage on 185 pages (89 added), 100% SEO baseline on 185 pages (1,425 meta tags inserted), `Backups/index-backup-20260407-1001-after-brand-cleanup.html`, `.claude/memory.md` Session Log + 5 Recent Decisions
  - **`.claude/skills/housekeeping/SKILL.md` rewritten 169 → 922 lines** with YAML frontmatter, count-drift script, false-positive avoidance, brand identity audit, duplicate-header detection allowlist, WCAG token canon, emoji→Sargam mapping, Parcel-bundle handling, enliven-repo workflow, content-type checklists. Also installed at `~/.claude/skills/housekeeping/SKILL.md` for global availability.
  - Catalog.html aria-hidden-focus fix (emoji→Sargam script had inserted `<img>` inside `placeholder=""` attribute on `#searchInput`)

  **#359 (workflow + a11y baseline):**
  - **CI workflow correctness fix** — both `.github/workflows/accessibility.yml` and `.github/workflows/ci.yml` had `$?` capture after `npm run test:a11y | tee` which always returned 0 (tee's exit code), so the wrapper script always took the success branch. PRs #350–#358 all silently passed despite real a11y violations. Fixed with `${PIPESTATUS[0]}`. Also discovered `tee` + `2>&1` was truncating pa11y's JSON output to ~17% of full size (65KB vs 393KB) — switched to direct stdout redirection (`pa11y-ci ... > pa11y-results.json`) which avoids the pipe entirely. Pa11y JSON parser also bumped to use depth-counted brace walking with diagnostic catch logging.
  - **Tests config**: Added third-party widget exclusions to `tests/axe-accessibility.js` — `.introjs-*` (auto-starts via `js/tours.js` 1.5s delay), `.userway_*`, `#uwy*`, `.gtranslate_wrapper`. These are vendor-injected DOM that we don't directly own.
  - **8-pass axe baseline clear**: 11 → 6 → 5 → 3 → 2 → 1 → 1 → 1 → **0**. Fixes spanned `index.html` (.imx-tag-muted token bump, 10 inline Explore Course CTA colors, 8 flagship feature spans, .imx-resource-cta, .v3-hero-eyebrow, .imx-track-flagship-pill, community card badges + CTAs, premium tier headers + descriptions, footer link rules, footer compliance opacity), `about.html` (.lang-status both variants, .team-role, .upi-box h4, global a + footer), `catalog.html` (.card-rating, .card-track, 5 .card-type variants), `bct-repository.html` (14 text uses of accent-color via override block, .sector-pill, .technique-id-badge fixed dark bg, .compare-bar-label, .footer-bottom a, --gradient-primary token), `courses/mel/index.html` (global a + link-in-text-block rule), and `js/auth.js` (Sign Up button background #6366f1 → #4f46e5, fallback #94a3b8 → #475569 across Login/Account/Logout).
  - **Pa11y trajectory** (cascade from axe fixes): 720 → 577 → ~414 → ~410 (plateaued — remaining errors are on the 8 pages outside axe's set).
  - **Issue #360** opened to track pa11y baseline cleanup as a clean follow-up (lexicons, handouts, premium, dataverse, etc.). Strategy documented: run pa11y locally, identify top 3-5 token clusters, apply scoped overrides, target 0-20 errors.

  **Final session totals:**
  - 9 PRs merged to main (#350–#356, #358, #359) + 1 closed (#357 superseded)
  - 1 follow-up issue opened (#360)
  - Skill globally available + 922-line checklist locked in
  - axe-core: 0 serious violations on all 5 audited pages (was hiding 11)
  - pa11y: 720 → 410 errors (still red, tracked in #360)
  - Google Analytics: 100% coverage on 185 content pages
  - SEO baseline: 100% coverage on 185 content pages
  - Content counts unified across 28 files
  - CI gates now truthful — any new a11y regression will be caught and reported correctly

  **Key reusable learnings (added to housekeeping skill):**
  - `tee` + `2>&1` mixing stderr into stdout can corrupt large JSON output. Use direct redirection (`> file.json`) for capturing data; let stderr go to the workflow log.
  - `$?` after a pipe captures the LAST command's exit code. Use `${PIPESTATUS[0]}` for the upstream command.
  - Brand color text on light brand-tinted backgrounds is the #1 a11y anti-pattern. Always use a darker variant for text (sky-500 → sky-800, indigo-500 → indigo-700, etc.).
  - `opacity: 0.8` on text using `var(--text-secondary)` puts contrast right at the 4.5:1 threshold. Either remove the opacity or use a darker base color.
  - JS-injected DOM (auth widgets, tours, sticky bots) needs its own a11y audit — fallback colors in `style.cssText` strings often use `#94a3b8` which fails AA.
  - Inline `style="..."` overrides cascade rules unless `!important`. Bulk fixing inline color requires sed or per-element edits.
  - Third-party widget DOM (Intro.js, UserWay, Google Translate) should be excluded from axe via `axe.run({exclude: [...]})` rather than fixing the vendor's HTML.
  - The pa11y JSON parser needs depth-counted brace walking (not `lastIndexOf('}')`) because JSON strings can contain `}` literals.
