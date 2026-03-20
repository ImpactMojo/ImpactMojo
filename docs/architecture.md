# Architecture

> **Who is this page for?** This page is primarily for developers and technical contributors. If you're an educator or practitioner, the key takeaway is in the "What This Means for Users" section below — you can skip the technical details.

## What This Means for Users

ImpactMojo is designed for practitioners in South Asia, many of whom are on slow internet connections or older devices. Here's what our technical choices mean for your experience:

- **Fast loading** — The site is built with simple, lightweight code (no heavy frameworks). Pages load quickly even on 2G/3G connections.
- **Works offline** — Once you've visited a page, it's saved on your device. You can access flagship courses without an internet connection.
- **No installation needed** — Everything runs in your web browser. No apps to download, no software to install.
- **Your data is secure** — Login and account data are handled by Supabase (a trusted database service). Premium tools use time-limited security tokens so your access can't be stolen.
- **Works on any device** — Phone, tablet, laptop, desktop — old or new. We deliberately avoid technologies that require modern hardware.

## Technical Overview

ImpactMojo is a static HTML/CSS/JS site with no build step, backed by Supabase for authentication and Netlify for hosting. Premium tools are deployed as separate Netlify sites, each protected by a JWT auth-gate.

## System Diagram

```
┌──────────────────────────────────────────────────────────┐
│                    impactmojo.in                         │
│                  (Netlify — main site)                   │
│                                                          │
│  index.html ─── js/auth.js ──── Supabase Auth            │
│                 js/router.js    (login, signup, profiles) │
│                 js/premium.js                             │
│                 js/resource-launch.js                     │
└──────────┬───────────────────────────────────────────────┘
           │
           │ User clicks premium tool
           ▼
┌──────────────────────────────────────────────────────────┐
│        Supabase Edge Function                            │
│        mint-resource-token                               │
│                                                          │
│  1. Verify user session (access_token)                   │
│  2. Check subscription_tier in profiles table            │
│  3. Check subscription_status = 'active'                 │
│  4. Verify tier permits requested resource               │
│  5. Mint short-lived JWT (5 min, HMAC-SHA256)            │
└──────────┬───────────────────────────────────────────────┘
           │
           │ window.open(resourceUrl + '?token=...')
           ▼
┌──────────────────────────────────────────────────────────┐
│        Resource Site (private Netlify deployment)          │
│        Netlify Edge Function: auth-gate.ts               │
│                                                          │
│  1. Check for resource_session cookie                     │
│  2. If no cookie, check ?token= query parameter          │
│  3. Verify JWT signature (same HMAC secret)              │
│  4. Verify resource claim matches RESOURCE_ID            │
│  5. Set 24h session cookie, redirect to clean URL        │
│                                                          │
│  No cookie + no token → redirect to login                │
└──────────────────────────────────────────────────────────┘
```

## Key Design Decisions

### Why no framework?

ImpactMojo serves practitioners in South Asia, many on low-bandwidth connections and older devices. A vanilla HTML/CSS/JS site:
- Loads fast with zero JS bundle overhead
- Works on any browser without polyfills
- Can be served as a static site with no build step
- Is easy to understand and contribute to

### Why separate Netlify sites for premium tools?

Each premium tool (VaniScribe, Qual Lab, etc.) was built independently. Hosting them as separate sites:
- Allows independent deployment and iteration
- Isolates failures — one tool going down doesn't affect others
- Makes the JWT auth-gate simple: one edge function per site
- Allows different teams to own different tools

### Why JWT over session-based auth?

- **Stateless:** No database lookup on every resource site request
- **Cross-domain:** Main site and resource sites are on different domains
- **Short-lived:** 5-minute tokens limit exposure if intercepted
- **Session cookies:** After initial JWT verification, a 24h cookie avoids re-authentication

### Why Supabase?

- Free tier covers our auth needs
- Built-in Row Level Security for profiles
- Edge Functions for serverless JWT minting
- PostgreSQL for structured data
- Google OAuth + Magic Links out of the box

## Environment Variables

### Main site (impactmojo.in)
No server-side env vars needed — Supabase credentials are in `js/auth.js` (public anon key only).

### Supabase Edge Function (mint-resource-token)
| Variable | Description |
|----------|-------------|
| `RESOURCE_TOKEN_SECRET` | HMAC-SHA256 signing key for JWTs |
| `SUPABASE_URL` | Auto-provided by Supabase |
| `SUPABASE_ANON_KEY` | Auto-provided by Supabase |
| `SUPABASE_SERVICE_ROLE_KEY` | Auto-provided; reads profiles bypassing RLS |

### Resource Netlify sites (per site)
| Variable | Description |
|----------|-------------|
| `RESOURCE_TOKEN_SECRET` | Same HMAC key as above |
| `RESOURCE_ID` | Unique slug: `rq-builder`, `toc-workbench-pro`, `code-convert-pro`, `qual-insights`, `vaniscribe`, `devdata-practice`, `viz-cookbook`, `devecon-toolkit`, `field-notes-pro`, `toc-workshop-pro`, `logframe-pro`, `chart-selector-pro`, `stakeholder-pro`, `empathy-pro`, `policy-canvas-pro`, `ai-canvas-pro` |

## Tier Access Control

```
explorer:      []  (free content only)
practitioner:  [rq-builder, toc-workbench-pro]
professional:  [rq-builder, toc-workbench-pro, code-convert-pro, qual-insights, vaniscribe,
                devdata-practice, viz-cookbook, devecon-toolkit,
                toc-workshop-pro, logframe-pro, chart-selector-pro, stakeholder-pro,
                empathy-pro, policy-canvas-pro, ai-canvas-pro, field-notes-pro]
organization:  [same as professional]
```

## Supabase Database Tables

| Table | Purpose |
|-------|---------|
| `profiles` | User accounts, tier, streak, interests |
| `user_progress` | Per-course progress tracking |
| `bookmarks` | User bookmarks |
| `user_notes` | Personal notes |
| `certificates` | Issued certificates with badge metadata |
| `payments` | Payment history |
| `coaching_bookings` | Coaching session bookings |
| `organizations` | Organization records |
| `organization_members` | User ↔ org membership |
| `learning_paths` | Custom org learning paths |
| `learning_path_assignments` | Path ↔ user assignments with due dates |
| `portfolio_items` | User portfolio entries |
| `challenge_submissions` | Live case challenge submissions |
| `challenge_requests` | Custom challenge requests from orgs |
| `cohorts` | Training cohorts with start/end dates (v10.8.0) |
| `cohort_members` | Cohort enrollment + progress tracking (v10.8.0) |
| `cohort_discussions` | Discussion threads within cohorts (v10.8.0) |
| `notifications` | In-app + email notification log (v10.8.0) |
| `notification_preferences` | Per-user email opt-in/out (v10.8.0) |
| `course_content` | Dynamic course HTML served via Edge Function |
| `badge_shares` | Badge sharing tracking |

## Supabase Edge Functions

| Function | Purpose |
|----------|---------|
| `mint-resource-token` | JWT minting for premium resource access |
| `issue-certificate` | Certificate issuance on course completion |
| `game-agent` | MiroFish AI agent engine for games (multi-provider LLM) |
| `serve-course-content` | Dynamic course content serving |
| `send-notification` | Email notifications: streak reminders, cohort deadlines, manual (v10.8.0) |

## File Structure

See [README → Project Structure](https://github.com/Varnasr/ImpactMojo#project-structure) for the full directory layout.
