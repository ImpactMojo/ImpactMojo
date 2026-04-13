# Changelog

What's new on ImpactMojo. For the full technical changelog, see [CHANGELOG.md](https://github.com/ImpactMojo/ImpactMojo/blob/main/CHANGELOG.md) in the repository.

## v10.19.0 — April 13, 2026

### Book Summaries
- **3 new book companions** added (28 → 31 total):
  - *Principles for Navigating Big Debt Crises* — Ray Dalio (2018) — debt cycles, deleveraging, and central bank policy across 48 historical cases
  - *Handbook for IPCC Authors: Climate Communications* — Corner, Shaw & Clarke (Climate Outreach, 2018) — six evidence-based principles for climate communication
  - *Storytelling to Accelerate Climate Solutions* — Coren & Wang (Springer, 2024) — 20 chapters on narrative approaches to climate action
- Updated BookSummaries index page: hero count 28→31, filter counts (dev-econ 5→6, leadership 7→9)
- Added entries to `data/search-index.json`, `sitemap.xml`, and docs

## v10.18.1 — April 12, 2026

### Fixed
- **README.md** — labs 19→11 (separated into Labs, Tools & Calculators, and Premium Tools sections), added 2 missing flagship courses (Gender Studies, Public Policy), added BookSummaries (28) and AI Study Companions (11) to content table, replaced Formspree with Netlify Forms in tech stack, updated version to 10.18.0 and date to April 12.
- **content-marketing-kit.html** — games 15→16, labs 10→11, flagship courses 9→11 across ~20 locations including social posts, carousel slides, brand guidelines, and content calendars. Fixed carousel counts (17 Labs→11, 27 Books→28).
- **ImpactMojo_PressKit.html** — foundational courses 39→38.
- **docs/roadmap.md** — moved Cohort-Based Learning, Notification System, Sample Size Calculator, Budget Template Generator, and full accessibility audit from "In Progress"/"Planned" to "Recently Completed". Added v10.13–v10.18 release entries. Added BookSummaries expansion and native deck migration to "In Progress".

### GitHub
- Closed Q1 2026 milestone (past due, all issues resolved).
- Replied to issue #361 (skill validation workflow proposal).
- Updated issue #272 (BookSummaries target raised from 5-8 to 40+).

## v10.18.0 — April 12, 2026

### Fixed
- **Sitemap coverage** — added 87 missing URLs to `sitemap.xml`: 2 flagship courses (gender, pubpol), 35 foundational 101-courses, 23 BookSummaries, 18 blog posts, and 9 public pages (transparency, dataverse, bct-repository, challenges, climate-trace-india, portfolio, live-projects, toc-builder, verify-certificate). Total URLs: 84 → 171.
- **Stale `101.impactmojo.in` links** — migrated ~100 legacy subdomain links to local paths across `js/faq-bank.js`, `js/bookmarks-compare.js`, `js/learning-tracks.js`, `js/game-agents.js`, and 4 docs files. All course links now point to `/101-courses/*.html`, all lab links to `/Labs/*.html`.
- **Search index phantom labs** — removed 6 duplicate/phantom lab entries from `data/search-index.json` (survey-design-lab, sampling-lab, logframe-builder, data-cleaning-lab, indicator-design-lab, toc-workbench); added missing entries for design-thinking-lab, mel-design-lab, and community-lab. Lab count: 17 → 13 (11 labs + 2 BookCompanionTools).
- **Content count drifts** — fixed `docs/content-guide.md` (flagship 9→11, labs 19→11, BookSummaries 27→28), `premium.html` ("47 foundational courses, labs & games" → "48 free courses, 11 labs & 16 games"), `catalog.html` JS comments (COURSES 39→38, LABS 10→11).
- **21 `.DS_Store` files** removed from git tracking (already in `.gitignore`).

## v10.17.0 — April 12, 2026

### Added
- **Formspree eliminated** — all 12 forms migrated to Netlify Forms with email notifications to info@impactmojo.in. Platform now runs on two services (Netlify + Supabase) instead of three.
- **Engagement email pipeline** — 5-email drip sequence for new users: welcome (Day 0), first course nudge (Day 3), content showcase (Day 7), re-engagement (Day 14), premium soft pitch (Day 21). Runs daily at 08:00 IST via Netlify Scheduled Function.
- **Streak tracking** — learning streaks now increment automatically on every login and reset after a missed day.
- **Post-certificate email** — congratulations email with shareable certificate link, sent automatically when a user completes a course. Includes a subtle premium mention for free-tier users.
- **Monthly newsletter** — automated content roundup on the 15th of every month, pulls highlights from the changelog and content counts from the search index. Includes premium and one-time support links.
- **Premium sales letter** at `/premium-letter.html` — long-form conversational page explaining Premium membership, tools, and pricing. Written as a personal letter, not a pricing table.
- **Practitioner Starter Kit** at `/starter-kit.html` — curated collection of 10 essential handouts for development practitioners.
- **Branded email template** — all platform emails now use a branded template with navy gradient header, ImpactMojo logo, amber accent bar, and dark footer.
- **Resend email integration** — domain verified (DKIM, SPF, DMARC) for transactional emails from notifications@impactmojo.in. Free tier: 3,000 emails/month.
- **Notifications infrastructure** — `notifications` and `notification_preferences` tables created in Supabase with RLS policies, indexes, and auto-preference creation for new signups.

### Changed
- **Netlify form detection** — enabled form processing (was previously disabled: `ignore_html_forms: true`) and configured email notifications for all 12 forms.
- **Supabase Edge Functions** — `send-notification` updated with engagement-drip and monthly-update endpoints; `issue-certificate` updated with congratulations email and premium upsell.

## v10.16.0 — April 8, 2026

### Added
- **Accessibility Statement page** at `/accessibility.html` — formal WCAG 2.1 Level AA conformance statement covering our commitment, how we test (axe-core + pa11y-ci on every PR), accessibility features, known limitations (Gamma iframes, canvas-based games, third-party widgets), and how to report a barrier. Linked from the footer Legal section, the About page, and the UserWay widget's statement link.
- **README badges** — new "Accessibility: WCAG 2.1 AA" shield and a live GitHub Actions status badge for the `accessibility.yml` workflow, so the repo README reflects current CI truth.
- **About page accessibility callout** — a brief paragraph in "What We Offer" announcing WCAG 2.1 AA conformance with a link to the full statement.

### Changed
- **UserWay widget** — the commented-out `data-statement_url` and `data-statement_text` config was wired up to point at the new `/accessibility.html` page. The UserWay button now surfaces "Our Accessibility Statement" as a direct link.

## v10.15.0 — April 8, 2026

### Fixed
- **Content-count drift sitewide** — `about.html`, `catalog.html` (hero + meta + filter chip), `transparency.html`, `org-dashboard.html`, `404.html`, `podcast.html`, Supabase signup/invite email templates, and four `docs/` files all now show the canonical counts: **48 courses (11 flagship + 38 foundational), 11 labs, 16 games**. Previously several of these still read 39 / 10 / 12.
- **`index.html` flagship stat line** — corrected "10 Flagship Courses" → "11 Flagship Courses" in the "What's Included" strip above the flagship course cards.
- **`catalog.html` missing flagship cards** — added Constitution & Law, Public Policy, and Gender Studies to the catalog JS data (they existed on the homepage but weren't in the catalog's searchable/filterable collection). Flagship filter chip now reflects the real 11.

### Changed
- **Learning Track Quiz promoted** — the "Not sure where to start?" quiz CTA has moved from section #6 of the homepage (below Learning Pathways) to directly under the hero area, right after the Daily Tip + Surprise Me buttons. First-time visitors now see the 5-question recommender before any content library listings.
- **New hero quiz shortcut** — added a tertiary "Not sure? Take the 5-question quiz →" link in the hero CTA block for visitors who want to jump straight to the quiz without scrolling.

## v10.14.0 — April 7, 2026

### Added
- **Device-mode default theme** on 70 pages — pages now follow your OS dark/light preference on first paint, and the 3-button theme toggle still wins if you pick explicitly
- **Underlined inline links** in body paragraphs across 74 content pages — meets WCAG 2.1 AA §1.4.1 (Use of Color)
- **CC BY-NC-SA 4.0 attribution** backfilled into 17 handouts that were missing it — all 84 handouts are now uniform
- **Premium topbar link** added to 11 main-site pages
- **Language translation widget** on `climate-trace-india` and `transparency`
- **Paper plane decoration** on `courses/gender/lexicon` and `courses/pubpol/lexicon`; footer landmark on `courses/pubpol/lexicon`

### Changed
- **WCAG AA muted-text contrast** bumped across 115 files (light and dark modes both)
- **`catalog.html` card colours** (ratings + track labels) darker to pass WCAG AA
- **Theme system unified** on a single `im-theme` localStorage key — picks now carry across games, account page, main site, and handouts consistently
- **Brand fonts** — two BookSummaries pages migrated back to the canonical Inter / Amaranth / JetBrains Mono stack
- **10 unbuilt course cards** marked "Coming Soon" with a disabled amber-pill card style
- **39 pictographic emoji → Sargam line icons** across 10 pages

### Fixed
- **Handout 404s** — self-hosted with URL-encoded paths (was linking to a stale mirror)
- **Duplicate headers** on 28 pages where the `im-topbar` was hiding the main site navigation
- **121 stale `101.impactmojo.in` course links** rewritten to self-hosted equivalents

## v10.13.0 — April 5, 2026

**What changed for you:** Three 101 foundational course decks — Development Economics, MEL, and Climate Essentials — are now native HTML slide decks replacing the old Gamma.app embeds. Full 100-slide presentations with light/dark theme, keyboard/touch navigation, interactive Chart.js charts, and content that fills the screen properly.

### Native 101 Slide Decks
- **Development Economics 101** — 100 slides, 12 sections, 17 interactive charts covering poverty, growth, agriculture, human capital, finance, trade, evidence, South Asia, and contemporary challenges
- **MEL 101** — 100 slides covering theory of change, indicators, data collection, evaluation methods, learning systems, and MEL failures
- **Climate Essentials 101** — 100 slides covering climate science, adaptation, mitigation, policy, finance, and South Asian climate vulnerability

### Design System
- Shared CSS/JS template for all future native 101 decks
- Light/dark/system theme toggle
- Keyboard arrows, touch swipe, and fullscreen navigation
- Responsive viewport scaling (1280×720 base, scales to any screen)
- Proportionally sized components that fill the slide area

## v10.12.0 — March 31, 2026

**What changed for you:** Repository moved to the ImpactMojo GitHub org, and documentation is now self-hosted (no more GitBook). Translation support expanded to 14 South Asian languages.

### Organization Migration
- Repository moved from `Varnasr/ImpactMojo` to `ImpactMojo/ImpactMojo` — all site links updated
- GitHub org configured with avatar, description, topics, and profile README
- Netlify reconnected to the new org

### Documentation
- **Self-hosted Docsify** replaces GitBook at `impactmojo.in/docs/`
- Dark/light/system theme toggle, full-text search, code copy buttons, prev/next navigation
- **Google Translate** with 14 languages: Hindi, Bengali, Marathi, Tamil, Telugu, Kannada, Malayalam, Gujarati, Punjabi, Odia, Assamese, Urdu, Nepali, Sinhala
- ImpactMojo branded design (Inter + Amaranth fonts, brand gradient, responsive)

### Infrastructure
- MCP server package scope: `@varnasr` → `@impactmojo`
- `_redirects` updated for self-hosted docs and new GitHub Pages URLs

## v10.11.0 — March 28, 2026

**What changed for you:** Two new blog posts with napkin.ai-generated illustrations, and a significantly expanded Content Marketing Kit with 5 new LinkedIn posts covering all 6 learning tracks.

### Blog
- **Introducing the ImpactMojo MCP Server** — Full blog post explaining what MCP is, what our server offers (11 tools, 3 resources), how to connect it, and example prompts
- **Open source blog illustrations** — Real napkin.ai infographics replacing placeholder images on the GitHub open dev ecosystem post
- Both posts include 2 professionally generated infographics via Napkin.ai API

### Content Marketing Kit
- **5 new LinkedIn posts** (LI-11–LI-15): Climate & Sustainability, Gender & Inclusion, AI in Development, Book Companions, MCP Server Launch
- **Broadened scope** — Renamed "Economics Games" to "Interactive Learning Games" across assets; ImpactMojo covers 6 tracks, not just economics
- **Corrected counts** throughout (9 courses, 16 games, 270 dataverse tools)
- **Redesigned brochure thumbnails** with content previews
- Total assets: 25 → 30

## v10.10.0 — March 27, 2026

**What changed for you:** ImpactMojo now has its own MCP server — connect any AI assistant (Claude Desktop, Claude Code, Cursor, etc.) to search our entire knowledge base: 700+ content items, 203 BCT techniques with South Asian context, 270 dataverse tools, India climate data, 16 economics games, and practice challenges.

### MCP Server (`/mcp-server/`)
- 11 tools: search_content, lookup_bct, search_bcts, list_bct_categories, browse_dataverse, search_dataverse, list_challenges, get_challenge, list_courses, get_game_info, query_climate_data
- 3 resources: platform overview, content catalog, learning tracks
- TypeScript + `@modelcontextprotocol/sdk`, stdio transport
- Published as `@impactmojo/impactmojo-mcp-server` on GitHub Packages
- Added to Dataverse catalog as `impactmojo-mcp`
- Auto-publishes on `mcp-server/v*` tags via GitHub Actions

## v10.9.1 — March 26, 2026

**What changed for you:** Housekeeping release — corrected lab counts across all documentation, added 13 missing games to sitemap for better search discoverability, and cleaned up stale branches.

### Documentation Consistency Sweep
- Fixed **lab count** from 19 → 11 across 12 files (faq, why-impactmojo, mojini-guide, learning-design, getting-started, transparency, premium, platform-overview, content-catalog, welcome, catalog.html, README)
- Fixed **foundational courses count** from 47 → 39 in platform-overview.md
- Fixed **docs/README.md version** from 10.1.0 → 10.9.0
- Fixed **Dataverse count** from 215 → 247 in docs/README.md and welcome.md
- Fixed **BookSummaries count** from 1 → 5 in content-catalog.md summary table
- Added 4 missing games (Climate Action, Gender Equity, Public Health, Digital Ethics) to content-catalog.md games table
- Added Gender Studies Lab to content-catalog.md labs table

### Sitemap
- Added 13 missing games to sitemap.xml (was 3, now all 16 games listed)

### Repository Cleanup
- Pruned stale remote tracking refs
- Identified 9 stale branches for deletion (no open PRs)
- Created pre-housekeeping backup of index.html

## v10.9.0 — March 24, 2026

**What changed for you:** Every page on ImpactMojo now has a consistent look and feel — unified fonts, mobile-responsive design, 3-mode theme toggle (System/Light/Dark), floating paper plane, standardized footer, and a sticky navigation bar with a home link and Premium button.

### Design System — Sitewide Audit & Fix (242 pages)
- Applied **ImpactMojo font stack** (Amaranth body, Inter headings, JetBrains Mono code) with `!important` global overrides across all 242 inner pages
- Added **3-mode theme toggle** (System / Light / Dark) with `localStorage` persistence and device-default loading
- Added **floating paper plane SVG** matching the homepage design to every page
- Added **sticky top bar** with ImpactMojo home link and Premium button on all inner pages
- Added **full 4-section footer** (About, Legal, Quick Links, Resources) to all pages missing it
- Fixed **mobile viewport meta tag** on BookSummary React pages that were missing it
- Added **dark mode CSS variables** and light/dark theme support across the entire site
- Added **GitBook documentation** link to the footer (Resources section) across all pages

### Documentation
- Updated typography docs to reflect 242-page coverage
- Updated roadmap: moved sitewide font/theme audit to Recently Completed
- Added GitBook docs link to index.html footer and all inner page footers

## v10.8.5 — March 22, 2026

**What changed for you:** Two new econometrics book companions added, press kit page linked in site navigation and footer, and book summary counts updated to 5 books / 100+ chapters.

### Book Summaries
- Added **Basic Econometrics** (Gujarati & Porter, McGraw-Hill) — 22-chapter interactive companion covering regression, hypothesis testing, multicollinearity, and more
- Added **Econometrics by Example** (Gujarati, Palgrave Macmillan) — 20-chapter hands-on companion with real-world examples
- Updated BookSummaries landing page: 3→5 books, 55+→100+ chapters

### Press Kit
- Added Press Kit link to About Us navigation dropdown
- Added Press Kit link to footer (About ImpactMojo section)
- Added Press Kit to search index and sitemap

### Documentation
- Added Press Kit page to GitBook navigation (About section)
- Updated content-catalog, platform-overview, and book-summaries-guide with new book entries

## v10.8.4 — March 22, 2026

**What changed for you:** Two new interactive book companions added — Debraj Ray's *Development Economics* and Andrew Pressman's *Design Thinking*. BookSummaries page now matches site-wide theming.

### Book Summaries
- Added **Development Economics** (Debraj Ray, Princeton 1998) — 18-chapter interactive companion with models, concepts, and exercises
- Added **Design Thinking** (Andrew Pressman, Routledge 2019) — 10-chapter interactive companion covering creative problem-solving methodology
- Updated BookSummaries landing page: 1→3 books, 30+→55+ chapters
- Applied ImpactMojo theming: floating paper airplane SVG, standard 4-section footer with social links, responsive + reduced-motion support

## v10.8.3 — March 22, 2026

**What changed for you:** Documentation consistency sweep — fixed stale content counts across all GitBook docs and added API key management template.

### GitBook Documentation Fixes
- Fixed stale lab counts (10→19) in 6 docs: why-impactmojo, getting-started, premium, transparency-and-commitments, mojini-guide, learning-design
- Fixed stale game counts (12→16) in 3 docs: getting-started, premium, learning-design
- Fixed stale Dataverse counts (215→247) in 3 docs: why-impactmojo, premium, dataverse-guide

### Developer Experience
- Added `.claude/.env.keys.example` template documenting all 6 API keys (GitHub, Supabase, Netlify, Gamma, Gemini, Napkin)

## v10.8.2 — March 21, 2026

**What changed for you:** Housekeeping release — updated counts, fixed stale references, and refreshed documentation.

### Documentation & Consistency
- Updated README version to 10.8.1 and date
- Fixed stale content counts across admin dashboard, analytics, transparency, and catalog pages (courses: 41→48, games: 11→16, labs: 15→19)
- Updated Dataverse count from 215 to 247 in index.html and transparency page
- Updated catalog.html header to reflect 11 flagship courses and 19 labs
- Refreshed sitemap.xml lastmod dates to 2026-03-21
- Created pre-housekeeping backup of index.html

## v10.8.1 — March 21, 2026

**What changed for you:** All blog posts now display napkin.ai illustrations, and blog card thumbnails on the blog index page are fixed.

### Blog Illustrations
- Generated 10 napkin.ai illustrations (2 per post) for the 5 blog posts that were missing them: from-learner-to-leader, learning-by-doing, meal-demystified, sample-size-matters, theory-of-change-pitfalls
- Fixed 4 mismatched thumbnail paths in blog.html (smart-vs-spiced → meal-demystified, toc-pitfalls → theory-of-change-pitfalls, qualitative-data → learning-by-doing, why-free → why-impactmojo-exists)

## v10.8.0 — March 20, 2026

**What changed for you:** Two major new features — **cohort-based learning** and **notifications** — plus auth reliability improvements.

### Cohort-Based Learning (#144)
- Organization admins can now create training cohorts with start/end dates, member enrollment, and deadline tracking
- Cohorts show per-member progress bars, average cohort progress, and a color-coded deadline countdown
- **Discussion threads** within each cohort — members can post, view, and delete messages
- Cohort status automatically updates (Upcoming → Active → Completed) based on dates
- Database tables: `cohorts`, `cohort_members`, `cohort_discussions` with full row-level security

### Notification System (#145)
- **In-app notifications** on the account page with unread badges and mark-as-read
- **Email notifications** via Resend (free 3K/month) with branded HTML templates
- **Streak reminders** — automatic email when users with active streaks go inactive for 2+ days
- **Cohort deadline alerts** — notifies enrolled members when cohorts end within 3 days
- **Notification preferences** — per-user opt-in/out for 6 notification categories (course updates, streaks, cohort deadlines, cohort discussions, assignments, certificates) plus digest frequency (daily/weekly/never)
- New Edge Function: `send-notification` with streak-reminders, cohort-deadlines, and manual notification endpoints

### Auth & Login Fixes
- Faster session recovery (1.5s + 4s safety nets, reduced from 3s)
- Increased SIGNED_OUT debounce to 1000ms to handle slow token refresh
- Aggressive session recovery from localStorage when in-memory state is lost
- Window `load` event recovery for `defer` script timing on homepage

### Other Fixes
- Gender equity game: SVG viewBox expanded to prevent Madhubani art head clipping
- Info asymmetry game: Pattachitra frame images now full-width on mobile
- API token documentation added for Gemini, DeepSeek, Grok, Sarvan.ai, Gamma
- Git standards verified across all 29 repos (29/29 compliant, dependabot active)
- 3 stale Claude Code branches cleaned up

## v10.7.0 — March 20, 2026

**What changed for you:** A brand new content type — **BookSummaries** — is now available under Specials. Developer tooling also improved with Claude Code skills and API key management built into the repo.

### BookSummaries
- New `BookSummaries/` directory for self-contained interactive book companions
- First entry: The Handbook of Social Protection — 24 chapters, 17 evidence findings, 5 learning pathways, 40+ glossary concepts
- Interactive data tools: SP Spending Explorer, Targeting Simulator, Transfer Size Calculator, Cost-Effectiveness chart
- Added to Specials dropdown navigation, content catalog, sitemap, and search index

### Claude Code Integration
- 6 repo-level skills for Claude Code (github-ops, netlify-ops, supabase-ops, gemini-ai, gamma-ops, housekeeping)
- SessionStart hook auto-loads API keys for Gemini, Gamma, DeepSeek, Grok, and Sarvan.ai
- All API tokens documented in project config

## v10.6.0 — March 19, 2026

**What changed for you:** ImpactMojo courses are being converted to Gamma presentation decks for visual delivery.

### Gamma API Integration
- 23 of 38 course decks synced as Gamma presentations
- Automated sync pipeline via `scripts/gamma-sync.js`
- Premium tools (Field Notes Pro, Workshop Pro) launched with server-side auth-gate

## v10.5.1 — March 19, 2026

**What changed for you:** Admin accounts are now protected from accidental tier downgrades, and premium resource access is more reliable.

### Premium Resource Gating
- All premium tools now use server-side JWT auth-gate on Netlify Edge Functions
- 7 new interactive workshop templates (ToC, Logframe, Chart Selector, Stakeholder Mapping, Empathy Canvas, Policy Canvas, AI Canvas) added to the premium listing
- Field Notes Pro — 70 curated development economics field notes, now a premium tool

### Admin Fixes
- Admin tier protection: database trigger prevents client-side downgrades
- Profile fetch timeout increased and auto-retry added for slow connections
- Fixed JS syntax errors that broke the org dashboard

### Labs & Design
- 7 new interactive labs (Design Thinking, Impact Partnerships, Resource Sustainability, Policy Advocacy, MEL Design, MEL Plan Builder, Gender Analysis)
- All 19 labs aligned to ImpactMojo standard design (theme selector, floating decorations, sargamicon badges)
- Lab count updated from 12 to 19 across the platform

### Housekeeping
- Removed `mobile-index.html` — `index.html` is now fully responsive
- Updated all documentation counts (labs 10→19, games 12→16, Dataverse 215→247)

## v10.1.0 — March 16, 2026

**What changed for you:** The documentation you're reading right now was completely restructured to be useful for educators, not just developers. We also standardized code quality practices across all 29 ImpactMojo repositories.

### Documentation Overhaul
- New educator-friendly docs: Welcome, Platform Overview, Getting Started, Learning Design, Workshops & Facilitation, Certificates & Progress, FAQ
- New guides: Handouts Guide (how to use and print), Dataverse Guide (all categories explained), Glossary (plain-language tech terms)
- Existing docs rewritten with clearer, more accessible language

### Dataverse Page Update
- Added explanations for all 7 resource types (datasets, tools, platforms, APIs, MCP servers, resources, skills)
- Previously only 3 types were explained

### Git Standards (29 repos)
- Consistent code quality standards across all ImpactMojo repositories
- Automated security checks prevent accidental commits of sensitive files

### GitBook Docs Fix
- Fixed broken sidebar links in the documentation

## v10.1.0 — March 16, 2026

### Git Standards (29 repos)
- Propagated `.gitattributes`, `.editorconfig`, `.githooks/`, `.gitmessage`, `CODEOWNERS`, `SECURITY.md`, `dependabot.yml`, PR & issue templates across all 29 ImpactMojo repos
- Pre-commit hook blocks secrets, debugger, conflict markers; warns on console.log and large files
- Commit-msg hook enforces prefix convention (Add/Fix/Update/Translate/Docs/Refactor/Test/CI/Chore)
- Dependabot auto-configured per ecosystem (npm, pip, github-actions)

### GitBook Docs Fix
- Fixed broken sidebar links — added `/impactmojo/*` → `/docs/*` Netlify redirects

## v10.0.0 — March 16, 2026

**What changed for you:** The site looks more consistent — fonts are unified across all 80+ pages. Mobile experience is significantly improved with new content sections and fixed navigation.

### Visual Consistency
- Standardized fonts across all pages: Amaranth (body text), Inter (headings), JetBrains Mono (code)
- Previously, different pages used different fonts, creating an inconsistent experience

### Mobile Experience
- New "What's New" section on mobile homepage — see the latest courses and features at a glance
- New "Wall of Love" testimonials section on mobile — real feedback from learners in 6 languages
- Fixed hamburger menu and logo display issues on mobile

### Dashboard Improvements
- Smoother charts on admin and transparency pages
- Fixed a bug where dashboard tabs sometimes showed the wrong membership tier
- Polished the "Create Learning Path" modal for organizations

### Transparency
- New revenue model section showing how ImpactMojo sustains itself
- Clearer methodology for usage statistics

## v9.5.0 — March 15, 2026

**What changed for you:** You can now navigate between your account, organization, admin, and analytics dashboards from a single tab bar. Organizations can set up team training packages.

- Unified dashboard navigation across all dashboard pages
- Team training packages for organizations (pre-built paths, facilitator guides, assessment rubrics)
- Full-text search, offline access, and course assessments

## v9.1.0 — March 7, 2026

**What changed for you:** PolicyDhara (policy research resource) was added as the 4th free resource accessible from the homepage. Organization dashboards got a getting-started guide.

- PolicyDhara integration on homepage and navigation
- Organization dashboard: welcome guide, feature grid, roadmap preview
- Login improvements — faster and more reliable

## v9.0.0 — March 6, 2026

**What changed for you:** Premium tools are now properly secured — only subscribers with the right tier can access them. Community features launched.

- Secure access control for premium tools (VaniScribe, Qual Lab Pro, etc.)
- GitHub Wiki with 7 documentation pages
- GitHub Discussions with 12 seed conversations
- Automated quality checks for links and accessibility

## v8.0.0 — February 28, 2026

**What changed for you:** The homepage loads much faster — we moved 160KB of code out of the main page. The site now works better offline.

- Major performance improvement — homepage loads significantly faster
- Improved offline support with smarter caching
- Community channels added to the premium registration flow

## v7.0.0 — February 15, 2026

**What changed for you:** This is when ImpactMojo launched as a full platform with accounts, certificates, and premium features.

- Premium membership tiers (Explorer, Practitioner, Professional, Organization)
- User accounts with Google login and magic links
- 38 foundational courses across 6 learning tracks
- 12 economics simulation games
- 10 interactive labs
- ImpactLex dictionary (500+ terms)
- Dev Case Studies (200 cases from 117 countries)
- DevDiscourses (500+ curated papers and books)
- Multilingual support (English, Hindi, Tamil, Bengali, Telugu, Marathi)
- Coaching, workshop booking, and Dojos skill sessions
- Blog (Learning Loops) and Podcast (Between the Logframes)
