# Changelog

All notable changes to ImpactMojo are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [10.11.0] - 2026-03-28

### Added
- **Blog: Introducing the ImpactMojo MCP Server** — New blog post at `/blog/impactmojo-mcp-server.html` with 2 napkin.ai-generated illustrations, added card to `blog.html`
- **Napkin.ai blog illustrations** — Generated real infographics for the open source blog post (`github-open-dev-ecosystem`) replacing placeholder images, using the Napkin.ai API
- **CMK: 5 new LinkedIn posts** (LI-11 through LI-15) — Climate & Sustainability, Gender & Inclusion, AI in Development, Book Companions, MCP Server Launch. Total assets: 25 → 30
- **Housekeeping: CMK brochure update step** — Added Content Marketing Kit and brochure PDF to the counts/references checklist in `housekeeping/SKILL.md`

### Changed
- **CMK: Broadened scope beyond economics** — Renamed "Economics Games" to "Interactive Learning Games" across IG-04, LI-07, CR-03; updated headlines and hashtags
- **CMK: Corrected content counts** — 48 → 9 courses, 16 → 15 games, 247 → 270 dataverse throughout all captions and visuals
- **CMK: Redesigned brochure thumbnails** — Replaced plain colored boxes with content-preview thumbnails showing actual page content
- **CMK: Updated year** — "Content Kit 2025" → "Content Kit 2026"

## [10.10.0] - 2026-03-27

### Added
- **ImpactMojo MCP Server** — New `/mcp-server/` directory with a standalone TypeScript MCP server exposing the full knowledge base via Model Context Protocol. 11 tools (search_content, lookup_bct, search_bcts, list_bct_categories, browse_dataverse, search_dataverse, list_challenges, get_challenge, list_courses, get_game_info, query_climate_data) and 3 resources (overview, catalog, tracks). Compatible with Claude Desktop, Claude Code, Cursor, and any MCP client.
- **Dataverse entry** — Added `impactmojo-mcp` to Education & Learning category (269→270 items)
- **Search index entry** — Added MCP server to `data/search-index.json`
- **Published to GitHub Packages** — `@varnasr/impactmojo-mcp-server@1.0.0` with auto-publish GitHub Action on `mcp-server/v*` tags

## [10.8.1] - 2026-03-20

### Added
- **BookSummaries landing page** — `/BookSummaries/index.html` so navigation goes to a browsable landing page instead of directly to the Hanna book

### Fixed
- **RQ Premium redirect loop** — Race condition in `resource-launch.js` where clicking Research Question Builder before `premium.js` initializes redirected to login instead of showing the upgrade modal
- **Premium page design consistency** — Updated `premium.html` cards to use main site design standards (3px borders, 20px radius, offset box-shadows)
- **Premium tool fonts** — Updated `code-converter-pro.html` and `qual-insights-lab.html` to use ImpactMojo fonts (Amaranth/Inter/JetBrains Mono) and color palette instead of Segoe UI

## [10.8.0] - 2026-03-20

### Added
- **Cohort-based learning** — Supabase-backed cohorts with start/end dates, member enrollment, progress tracking, and deadline countdown (org dashboard Training tab)
- **Cohort discussion threads** — Real-time discussion within cohorts with post/delete support
- **Notification system** — `send-notification` Edge Function with streak reminders, cohort deadline alerts, and manual notification API
- **Notification preferences** — Per-user email opt-in/out (course updates, streak reminders, cohort deadlines, discussions, assignments, certificates) with digest frequency
- **In-app notification feed** — Recent notifications card on account page with unread badges and mark-as-read
- **Database migration** — `cohorts`, `cohort_members`, `cohort_discussions`, `notifications`, `notification_preferences` tables with full RLS policies, indexes, and triggers

### Changed
- **Auth session recovery** — Faster safety-net (1.5s + 4s fallback), increased SIGNED_OUT debounce to 1000ms, aggressive `_recoverSessionFromStorage()` for stored sessions, window.load recovery
- **API token documentation** — Added Gemini, DeepSeek, Grok, Sarvan.ai, Gamma to CLAUDE.md and .env.example

### Fixed
- **Gender equity game** — SVG viewBox too short, causing Madhubani art heads to be clipped
- **Info asymmetry game** — Pattachitra frame and end-story-art missing `width:100%`, appearing too small on mobile
- **Login persistence** — Session not surviving page navigation due to timing gaps in token refresh cycle

## [10.7.0] - 2026-03-20

### Added
- **BookSummaries** — New content type under Specials: interactive book summaries
- **The Handbook of Social Protection** (Hanna & Olken, MIT Press 2026) — first interactive book companion with chapter navigator, evidence explorer, data playground, programme compare, glossary, South Asia lens, and AI-powered Q&A
- BookSummaries entry added to Specials dropdown nav, catalog, sitemap, and search index
- **Claude Code global skills** — 6 repo-level skills (github-ops, netlify-ops, supabase-ops, gemini-ai, gamma-ops, housekeeping) for Claude Code on the web
- **SessionStart hook** — auto-loads API keys (Gemini, Gamma, DeepSeek, Grok, Sarvan.ai) from gitignored `.claude/.env.keys`
- **API token documentation** — CLAUDE.md updated with all 8 environment tokens

### Changed
- **`.env.example` updated** with Grok, Sarvan.ai, and Gamma API key placeholders
- **`.claude/settings.json`** now registers both SessionStart and Stop hooks
- **`.gitignore`** updated to protect `.claude/.env.keys` from commits

## [10.6.0] - 2026-03-19

### Added
- **Field Notes Pro** — 70 curated development economics field notes deployed as premium tool at `impactmojo-field-notes-pro.netlify.app`
- **Workshop Pro** — 7 interactive workshop templates (ToC, Logframe, Chart Selector, Stakeholder Mapping, Empathy Canvas, Policy Canvas, AI Canvas) deployed at `impactmojo-workshop-pro.netlify.app`
- **Field Notes JSON editor** link added to admin dashboard — edit `data/notes.json` directly from GitHub
- **Server-side auth-gate** on all new premium Netlify resource sites with `RESOURCE_TOKEN_SECRET` env vars configured

### Changed
- **Removed `mobile-index.html`** — `index.html` is now fully responsive, no separate mobile page needed
- **Updated all doc counts** — labs 10→19, games 12→16, Dataverse 215→247 across platform-overview, content-guide, architecture docs
- **Architecture docs updated** — full tier access control matrix with all 16 resource IDs
- **GitBook changelog updated** through v10.5.1
- **Sitemap timestamps refreshed** to 2026-03-19
- **ROADMAP.md updated** with Q1 2026 completions (workshop templates, field notes, auth-gate, mobile removal)
- **CLAUDE.md updated** — removed stale mobile-index.html checklist item
- **GitHub repo description updated** with current counts

## [10.5.1] - 2026-03-19

### Fixed
- **Admin tier reset bug** — admin accounts (varna.sr@gmail.com, varna@pinpointventures.in, vsoni.1986@gmail.com) were intermittently shown as free/explorer tier due to stale localStorage cache when profile fetch timed out
- **Profile fetch timeout** increased from 5s to 8s to reduce cache fallback on slow connections
- **Profile fetch retry** — failed fetches now auto-retry after 5 seconds so stale cached tier doesn't persist

### Added
- **Admin tier protection trigger** (`protect_admin_tier`) — database trigger prevents client-side downgrades of admin role, subscription tier, or subscription status
- **Idempotent profile creation** — `handle_new_user()` trigger now uses `ON CONFLICT DO NOTHING` to prevent overwriting existing profiles on re-authentication

## [10.5.0] - 2026-03-19

### Added
- **RQ Builder Pro** premium card — Practitioner tier, guided research question builder with PICO/SPIDER framing
- **TOC Workbench Pro** premium card — Practitioner tier, advanced Theory of Change building with assumption mapping and PDF/PNG export
- Both new tools added to premium modal, mobile-index.html, and search index

### Changed
- **Premium tool count updated from 7 → 9** across all pages and docs (catalog.html, content-catalog.md, faq.md, architecture.md, premium-tools-guide.md)
- **All 9 premium cards modernized with unique Sargam icons** — replaced generic si_Flare/imx-star badges with contextual icons (si_Search, si_Crosshair_detailed, si_Direction_alt, si_Library_books, si_Bar_chart, si_Database, si_Chat, si_Activity, si_Lightning)
- **Compact premium cards reformatted** to consistent expanded multi-line style matching the rest of the section
- **Tier access matrix updated** in architecture.md to include `toc-workbench-pro`

## [10.4.1] - 2026-03-19

### Changed
- **All 11 labs aligned to ImpactMojo standard design** — 3-button theme selector (System/Light/Dark), floating paper plane SVG decoration, sargamicon header badges
- **Theme persistence** — labs now share the `impactmojo-theme` localStorage key with system-preference awareness

## [10.4.0] - 2026-03-18

### Added
- **7 new self-hosted interactive labs** — Design Thinking, Impact Partnerships, Resource Sustainability, Policy Advocacy, MEL Design, MEL Plan Builder, Gender Analysis (all in `/courses/`)
- **Lab links updated** — all lab links in index.html now point to self-hosted files instead of `101.impactmojo.in`

### Changed
- **Lab count updated** from 12 to 19 across README and platform pages
- **Sitemap updated** with 7 new lab page entries
- **Search index updated** with entries for all new labs

## [10.3.0] - 2026-03-18

### Added
- **3 new games** beyond economics: Climate Action (Warli art), Gender Equity/Care Economy (Madhubani art), Public Health/Epidemic Response (Pattachitra art)
- **Indian folk art story illustrations** across all 12 existing games — intro screens, mid-game interludes, and adaptive ending art in 6 styles (Warli, Madhubani, Gond, Kalamkari, Pichwai, Pattachitra)
- **Sample Size Calculator** lab tool — 4 modes (proportion, mean, two-group, cluster sampling) with educational content
- **Budget Template Generator** lab tool — 7 budget categories, 5 smart templates, CSV/clipboard export
- **Admin dashboard panels** — User Management (search, filter, pagination) and Site Settings (feature flags, metadata, integrations, backups)
- **Accessibility improvements** — skip-nav links, ARIA landmarks, focus-visible styles, screen-reader labels on index, mobile-index, about, catalog
- **Claude Code project config** — `.claude/CLAUDE.md`, Stop hook for housekeeping, `/housekeeping` skill

### Changed
- **Renamed "Economics Games" → "Games"** across 14 files (now covers broader topics)
- **Fixed card text contrast** across 8 games — increased badge opacity, darkened text, added text-shadows (WCAG AA)
- **Fixed Dojos nav icon** — was duplicating Flagship Courses icon, now uses Activity icon
- **Fixed PolicyDhara workflow** — commit-msg prefix mismatch causing all scheduled runs to fail

### Removed
- **12 old Netlify game sites** deleted — all games now self-hosted in `/Games/`

## [10.2.0] - 2026-03-17

### Added
- **Self-hosted interactive games** in `/Games/` folder — replacing old Netlify-hosted apps at 101.impactmojo.in
- **MiroFish AI agent engine** (`supabase/functions/game-agent/`) — multi-provider LLM support with automatic fallback chain (DeepSeek → Groq → Gemini → Together → OpenAI)
- **30+ AI agent personas** (`data/game-agents.json`) — South Asian development practitioners with distinct personalities, backstories, and strategic behaviours
- **Game agents client library** (`js/game-agents.js`) — browser-side integration with Edge Function + local fallback engine
- **LLM provider secrets** configured: Groq, Google Gemini, DeepSeek API keys set as Supabase secrets

### Changed
- **Game links in index.html** — all 12 game links updated from `101.impactmojo.in/*` to `/Games/*.html`
- **game-agents.js Supabase URL** — corrected to actual project endpoint

### Games Built
- Public Good Game (free-rider problem, 4 AI agents)
- Prisoners' Dilemma (strategic interdependence, 4 AI agents)
- Commons Crisis (tragedy of the commons, 4 AI agents)
- Cooperation Paradox (Nash vs Pareto, 2 AI agents)
- Opportunity Cost (budget allocation, 2 AI agents)
- Risk & Reward Explorer (prospect theory, 3 AI agents)
- Bidding Wars (auction theory, 3 AI agents)
- Information Asymmetry (lemons problem, 3 AI agents)
- Network Effects (platform adoption, 3 AI agents)
- Externality Game (Pigouvian tax, 3 AI agents)
- The Real Middle (India income inequality)
- Econ Concepts Puzzle (12 brain-teasers)

## [10.1.0] - 2026-03-16

### Added
- **Git best-practice standards** propagated across all 29 Varnasr repos: `.gitattributes`, `.editorconfig`, `.githooks/pre-commit`, `.githooks/commit-msg`, `.gitmessage`, `.github/CODEOWNERS`, `.github/SECURITY.md`, `.github/dependabot.yml`, `.github/pull_request_template.md`, `.github/ISSUE_TEMPLATE/` (bug report, feature request, content issue)
- **Dependabot** configured per-repo (npm, pip, github-actions ecosystems auto-detected)
- **Pre-commit hook** blocks secrets (.env, .pem, .key), debugger statements, merge conflict markers; warns on console.log and files >500KB
- **Commit-msg hook** enforces prefix convention (Add/Fix/Update/Translate/Docs/Refactor/Test/CI/Chore)

### Fixed
- **Broken GitBook sidebar links**: Added `/impactmojo/*` → `/docs/*` Netlify redirects so sidebar navigation on impactmojo.in/docs works correctly

## [10.0.0] - 2026-03-16

### Added
- **What's New section** on mobile homepage — 8 feature cards highlighting new courses, DevData, Case Studies, DevDiscourses
- **Wall of Love section** on mobile homepage — horizontally scrollable testimonial cards in 6 languages (English, Hindi, Tamil, Bengali, Telugu, Marathi)
- **4 new course pages** linked: Politics of Aspiration, Media for Development, Constitution & Law, Social-Emotional Learning
- **Canvas line charts** on admin dashboard and transparency page — smooth Catmull-Rom spline rendering with gradient fills, replacing bar charts
- **Revenue model section** on transparency page — Explorer (free) vs Practitioner/Organisation (paid) tier cards

### Changed
- **Font standardization across 80 files**: Amaranth (body text) + Inter (headings) + JetBrains Mono (code). Removed Poppins, Fraunces, Merriweather, Source Serif 4, Source Sans 3, Cormorant Garamond. All fallback chains standardized
- **Google Fonts loading standardized**: Amaranth:400,700 + Inter:400-800 + JetBrains Mono:400,500. Consistent weight ranges across all pages
- **Transparency page redesigned**: renamed from "Transparency & Analytics", simplified data model (Legacy + GA4 = Totals), added methodology section
- **Admin dashboard redesigned**: removed one-time Supabase setup section, replaced bar charts with canvas line charts, games & tools charts in two-column layout
- **Org dashboard modal polished**: Create Learning Path modal — tighter padding, compact course rows, pill-shaped category buttons, proper light theme checkbox styling
- **Dashboard tabs** now accept profile parameter directly, fixing race condition where tabs showed wrong role/tier

### Fixed
- **Auth gate race condition**: `authStateChanged` event fired before profile fetch completed, causing premature access denial. Both `admin-gate.js` and `auth-gate.js` now await `fetchProfile()` before checking roles
- **Dashboard tabs wrong role**: `DashboardTabs.init()` relied on global `ImpactMojoAuth.profile` which wasn't set yet. Fixed by passing profile from auth callback
- **Mobile hamburger cutting off logo**: hidden desktop-only elements (theme selector, tour toggle, starburst badge, nav buttons) on mobile across `index.html`, `account.html`, `org-dashboard.html`, `mobile-index.html`
- **Mobile logo truncation**: removed `overflow:hidden` + `text-overflow:ellipsis` that was truncating "ImpactMojo" to "Impact..." on mobile-index.html

### Removed
- One-off fonts: Fraunces (dojos), Merriweather (about), Source Serif 4 (lexicons), Source Sans 3 (gandhi), Cormorant Garamond (gandhi)
- Supabase one-time setup section from admin dashboard
- Bar chart rendering code from admin and transparency pages

## [9.5.0] - 2026-03-15

### Added
- Unified dashboard tab navigation across account, org, admin, and analytics pages
- Team training packages for organizations (pre-built training paths, facilitator guides, assessment rubrics, cohort management)

## [9.1.0] - 2026-03-07

### Added
- **PolicyDhara** as 4th free resource (homepage, mobile, nav dropdown) linking to https://on-web.link/PolicyDhara
- Organization Dashboard content: welcome getting-started guide, "What's Included" feature grid, "Coming Soon for Teams" roadmap preview
- New roadmap items: Open Badges & Micro-credentials (#30), Live Case Challenges (#31)
- GitHub Issues for all roadmap features (#25-#31)

### Changed
- Org dashboard loads members and paths in parallel (`Promise.all`) for faster rendering
- Added `preconnect` hints for Supabase and CDN on org dashboard

### Fixed
- Org dashboard auth gate now waits for auth to fully resolve before checking tier access
- Google OAuth sign-in no longer triggers redundant profile fetch/sync on redirect

### Removed
- "Qualitative Data Lab" from roadmap (already live as Qual Insights Lab)
- "AI Learning Assistant" from roadmap (commoditized by general AI agents)

## [9.0.0] - 2026-03-06

### Added
- JWT-based premium access control for all resource sites
- Netlify Edge Functions (auth-gate) on 4 premium tool sites
- Supabase Edge Function for minting resource tokens
- `resource-launch.js` — client-side JWT launcher for premium tools
- `token-gate.js` — client-side token verification
- GitHub Wiki with 7 documentation pages
- GitHub Discussions with 12 seed conversations
- GitHub Actions CI for broken links and accessibility checks
- `.editorconfig` for consistent formatting
- `CHANGELOG.md` (this file)
- JSON-LD structured data for SEO

### Changed
- README rewritten with business models (Workshops, Coaching, Dojos, Premium tiers)
- README Netlify badge fixed (was using wrong site ID format)
- README version bumped to 9.0.0

### Fixed
- Broken Netlify deploy status badge in README
- `RESOURCE_SECRET_TOKEN` typo on premium resource site (renamed to `RESOURCE_TOKEN_SECRET`)

## [8.0.0] - 2026-02-28

### Added
- Performance optimization: extracted 160KB inline JS to deferred external files
- `js/bookmarks-compare.js` — bookmarks and course comparison logic
- `js/cookie-ui.js` — cookie consent banner
- `js/learning-tracks.js` — learning track navigation
- `js/mobile-ui.js` — mobile-specific UI logic
- Service worker upgraded with versioned cache and network-first strategy
- Font subsetting (Latin + Devanagari only)
- Community channels added to premium registration form

### Changed
- Inline JavaScript extracted from `index.html` (reduced from ~200KB to ~40KB)
- Service worker cache version bumped with proper invalidation

## [7.0.0] - 2026-02-15

### Added
- Premium membership tiers (Explorer, Practitioner, Professional, Organization)
- Supabase authentication (Email, Google OAuth, Magic Links)
- User profiles with progress tracking
- Bookmarks, personal notes, and reading lists
- Course comparison feature
- 39 foundational courses across 6 learning tracks
- 12 economics learning games
- 10 interactive labs
- ImpactLex PWA with 500+ terms
- Dev Case Studies library (200 cases, 117 countries)
- DevDiscourses (500+ curated papers and books)
- 400+ downloadable handouts
- Multilingual support (English, Hindi, Tamil, Bengali, Telugu, Marathi)
- Coaching and workshop booking pages
- Dojos skill session page
- Blog (Learning Loops) and podcast (Between the Logframes)

[10.7.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.6.0...v10.7.0
[10.6.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.5.1...v10.6.0
[10.5.1]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.5.0...v10.5.1
[10.5.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.4.1...v10.5.0
[10.4.1]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.4.0...v10.4.1
[10.4.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.3.0...v10.4.0
[10.3.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.2.0...v10.3.0
[10.2.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.1.0...v10.2.0
[10.1.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.0.0...v10.1.0
[10.0.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v9.5.0...v10.0.0
[9.5.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v9.1.0...v9.5.0
[9.1.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v9.0.0...v9.1.0
[9.0.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v8.0.0...v9.0.0
[8.0.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v7.0.0...v8.0.0
[7.0.0]: https://github.com/ImpactMojo/ImpactMojo/releases/tag/v7.0.0
