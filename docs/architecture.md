# Architecture

## Overview

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
│        Resource Site (e.g., vaniscribe.netlify.app)       │
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
| `RESOURCE_ID` | Unique slug: `rq-builder`, `code-convert-pro`, `qual-insights`, `vaniscribe` |

## Tier Access Control

```
explorer:      []  (free content only)
practitioner:  [rq-builder]
professional:  [rq-builder, code-convert-pro, qual-insights, vaniscribe, devdata-practice, viz-cookbook, devecon-toolkit]
organization:  [same as professional]
```

## File Structure

See [README → Project Structure](https://github.com/Varnasr/ImpactMojo#project-structure) for the full directory layout.
