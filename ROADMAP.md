# Roadmap

ImpactMojo development priorities for 2026. Items are roughly ordered by priority within each quarter.

## Q1 2026 (Jan-Mar) — Completed

- [x] JWT-based premium access control for resource sites
- [x] Supabase authentication (Email, Google OAuth, Magic Links)
- [x] W3C Open Badges 3.0 verifiable credentials
- [x] Learning Pathways with milestone progression
- [x] Interactive assessments for flagship courses
- [x] Team training packages for organizations
- [x] Full-text search (Ctrl+K) via Fuse.js
- [x] Offline PWA support for flagship courses
- [x] Unified dashboard architecture (account, org, admin, analytics)
- [x] Canvas line charts on admin & transparency dashboards
- [x] Font standardization (Amaranth + Inter + JetBrains Mono)
- [x] Mobile nav fixes across all pages
- [x] 4 new flagship courses (Politics of Aspiration, Media for Development, Constitution & Law, SEL)
- [x] Git best-practice standards propagated across all 29 repos (hooks, templates, dependabot, CODEOWNERS, SECURITY)
- [x] GitBook docs sidebar link fix (`/impactmojo/*` → `/docs/*` redirects)
- [x] **Self-hosted interactive games** with MiroFish AI agents — replacing Netlify-hosted apps
- [x] **MiroFish AI agent engine** — Supabase Edge Function with multi-provider LLM fallback (Groq/Gemini/DeepSeek)
- [x] **30+ AI agent personas** — South Asian development practitioners across 10 games
- [x] **3 new games** beyond economics — Climate Action, Gender Equity, Public Health (Digital Ethics in progress)
- [x] **Indian folk art story illustrations** — across all games in 6 styles
- [x] **Card text contrast fixes** — WCAG AA compliance across 8 games
- [x] **Sample Size Calculator** — survey planning lab with 4 calculation modes
- [x] **Budget Template Generator** — project budget lab with smart templates and CSV export
- [x] **Admin dashboard** — User Management and Site Settings panels
- [x] **Accessibility improvements** — skip-nav, ARIA landmarks, focus styles on key pages
- [x] **Old Netlify game sites deleted** — freed 12 slots
- [x] **PolicyDhara workflow fix** — commit-msg prefix causing build failures
- [x] **Gender Studies flagship course** — in progress
- [x] **7 interactive workshop templates** — ToC, Logframe, Chart Selector, Stakeholder, Empathy Canvas, Policy Canvas, AI Canvas (premium)
- [x] **Field Notes Pro** — 70 curated development economics field notes (premium)
- [x] **Server-side auth-gate** on all premium Netlify resource sites
- [x] **Removed mobile-index.html** — index.html is now fully responsive
- [x] **Admin tier protection** — database trigger prevents client-side downgrades
- [x] **BookSummaries** — new content type under Specials with interactive book companions
- [x] **Handbook of Social Protection** — first interactive book summary (Hanna & Olken, MIT Press 2026)
- [x] **Gamma API integration** — 23/38 course decks synced as Gamma presentations
- [x] **Claude Code skills & hooks** — 6 global skills, SessionStart hook for API key bootstrap, multi-provider AI token support
- [x] **Cohort-based learning** — Supabase-backed cohorts with discussion threads, deadlines, and progress tracking (#144)
- [x] **Notification system** — Edge Function for email notifications (streak reminders, cohort deadlines), in-app notification feed, per-user preferences (#145)
- [x] **Git standards verified** — all 29 repos confirmed compliant, dependabot PRs arriving (#162)
- [x] **Auth persistence fixes** — faster session recovery, aggressive SIGNED_OUT debounce, window.load recovery
- [x] **Game visual fixes** — gender equity SVG clipping, info asymmetry image sizing
- [x] **API token documentation** — Gemini, DeepSeek, Grok, Sarvan.ai, Gamma added to CLAUDE.md and .env.example

## Q2 2026 (Apr-Jun) — Planned

- [ ] **Vernacular Content** — Full courses in Hindi and Tamil (#29)
- [ ] **Analytics dashboard v2** — Learner analytics with completion funnels, time-on-task, assessment scores
- [ ] **Mobile app (PWA)** — Enhanced PWA with push notifications and background sync

## Q3 2026 (Jul-Sep) — Planned

- [ ] **Peer review system** — Learners review each other's assignments and case analyses
- [ ] **Certificate marketplace** — Employer-facing verification portal
- [ ] **API for partners** — REST API for organizations to integrate ImpactMojo content

## Q4 2026 (Oct-Dec) — Exploratory

- [ ] **Community-contributed courses** — Allow verified practitioners to publish courses
- [ ] **Live workshops integration** — Calendar-based booking with Zoom/Meet integration
- [ ] **Impact measurement dashboard** — Track real-world outcomes from learners' projects

---

## How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Feature requests and roadmap suggestions are welcome via [GitHub Issues](https://github.com/Varnasr/ImpactMojo/issues) or [Discussions](https://github.com/Varnasr/ImpactMojo/discussions).
