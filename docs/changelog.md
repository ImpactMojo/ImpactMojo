# Changelog

What's new on ImpactMojo. For the full technical changelog, see [CHANGELOG.md](https://github.com/Varnasr/ImpactMojo/blob/main/CHANGELOG.md) in the repository.

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
- Updated catalog.html header to reflect 9 flagship courses and 19 labs
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
- Propagated `.gitattributes`, `.editorconfig`, `.githooks/`, `.gitmessage`, `CODEOWNERS`, `SECURITY.md`, `dependabot.yml`, PR & issue templates across all 29 Varnasr repos
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
- 39 foundational courses across 6 learning tracks
- 12 economics simulation games
- 10 interactive labs
- ImpactLex dictionary (500+ terms)
- Dev Case Studies (200 cases from 117 countries)
- DevDiscourses (500+ curated papers and books)
- Multilingual support (English, Hindi, Tamil, Bengali, Telugu, Marathi)
- Coaching, workshop booking, and Dojos skill sessions
- Blog (Learning Loops) and Podcast (Between the Logframes)
