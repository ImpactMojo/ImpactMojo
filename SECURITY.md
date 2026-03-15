# Security Policy

## Supported Versions

ImpactMojo is a static website deployed on Netlify. The `main` branch always reflects the live production site.

| Version | Supported |
|---------|-----------|
| `main` branch (current) | Yes |
| Older commits | No |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Do not** open a public GitHub issue
2. **Email** security concerns to **hello@impactmojo.in** with the subject line "Security: [brief description]"
3. Include steps to reproduce, impact assessment, and any suggested fixes

We will acknowledge your report within 48 hours and aim to resolve critical issues within 7 days.

## Scope

Security concerns relevant to this project include:

- XSS vulnerabilities in client-side JavaScript
- Authentication or authorization bypasses (Supabase integration)
- Exposure of API keys or secrets
- Open redirect vulnerabilities
- Issues with the JWT token-gating system

## Out of Scope

- Denial of service attacks
- Social engineering
- Issues in third-party services (Supabase, Netlify, Formspree) — report these to the respective providers

---

## Content Protection & Fork Policy

ImpactMojo uses a **dual licence** (see [LICENSE](LICENSE)):

| Component | Licence |
|-----------|---------|
| Source code (`js/`, `supabase/`, CSS, configs) | MIT |
| Educational content (courses, handouts, HTML) | CC BY-NC-ND 4.0 |
| Premium-gated content | Proprietary |

### What forks MAY do

- Reuse the technical architecture (JavaScript, CSS, Supabase functions) under the MIT licence with attribution.
- Study and learn from the educational content for personal use.

### What forks MAY NOT do

- Redistribute, mirror, or republish the educational content.
- Host a competing platform using our course materials.
- Offer any ImpactMojo content behind a paywall.
- Redistribute premium-gated content in any form.

---

## DMCA Takedown Process

If you find an unauthorised fork or mirror of ImpactMojo content:

1. **Document the infringement** — screenshot the fork, note the URL and the specific files that contain ImpactMojo content.
2. **File with GitHub** — submit a DMCA takedown notice at https://github.com/contact following GitHub's [DMCA policy](https://docs.github.com/en/site-policy/content-removal-policies/dmca-takedown-policy).
3. **Include these details:**
   - Your contact information (Dr. Varna Sri Raman / ImpactMojo).
   - The original content URL on impactmojo.in.
   - The infringing fork URL.
   - A statement that the content is used without authorisation.
   - A statement of good faith belief and accuracy under penalty of perjury.
4. **Notify us** at hello@impactmojo.in so we can track the takedown.

---

## Architecture Security Notes

### Supabase Anon Key

The Supabase anon key is a **public** API key by design — it is safe for client-side use. All data protection is enforced by:

- **Row-Level Security (RLS)** policies in Supabase.
- **Server-side tier verification** in the `mint-resource-token` Edge Function.
- **Short-lived JWTs** (5-minute TTL) for premium resource access.
- **Rate limiting** (10 requests/user/minute) on the token minting endpoint.
- **CORS origin restrictions** — only `impactmojo.in` can call the Edge Function.

### For Fork Maintainers

If you fork this repository for your own project, you **must**:

1. Create your own Supabase project at https://supabase.com.
2. Replace the credentials in `js/config.js` with your own.
3. Set your own `RESOURCE_TOKEN_SECRET` in your Supabase Edge Function env.
4. Set your own `RESOURCE_TOKEN_SECRET` in each Netlify resource site env.
5. Update CORS origins in `supabase/functions/mint-resource-token/index.ts`.
6. Deploy your own Supabase Edge Functions.

Using the original ImpactMojo Supabase credentials in a fork is a violation of the licence and will result in key rotation and potential legal action.
