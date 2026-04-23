# ImpactLex Backend Decision

_Phase 0 of the ImpactLex upgrade. This file is ephemeral — delete after Phase 2 ships._

## TL;DR

**Pick InstantDB.** The workload is read-heavy, the real-time + offline-first story is a first-class fit, the browser SDK is tiny, and we already have Supabase holding the rest of the platform — keeping ImpactLex on a separate backend is a feature, not a cost, because it isolates public-facing anonymous traffic from the authenticated learner data store.

## Workload

| Trait | Value |
|---|---|
| Rows | ~500–700 terms, growing slowly |
| Read/write ratio | ~1000:1 (glossary lookups vs. contributions) |
| Auth | Anonymous-first; login only for contribute + cloud bookmarks |
| Real-time | Nice for contribution moderation; not critical for readers |
| Offline | Required — current ImpactLex is a PWA |
| Search | Client-side over cached snapshot is fine at this row count |

## Comparison

| Dimension | InstantDB | Supabase | Winner |
|---|---|---|---|
| SDK size (gz) | ~30 KB `@instantdb/core` | ~50 KB `@supabase/supabase-js` | InstantDB |
| Real-time sync | Built-in, opt-in per query, no pub/sub wiring | Postgres CHANGES via Realtime channel, extra setup | InstantDB |
| Offline-first | Local-first by design; queries hydrate cache | Not offline-first; needs custom cache layer | InstantDB |
| Magic-link auth | Built-in, no email provider config | Built-in + configurable | Tie |
| RLS for draft/published | Permission rules in InstantDB schema | Postgres RLS (we already author these) | Tie |
| Full-text search | Client-side over snapshot is sufficient | Same, or `tsvector` server-side | Tie |
| Free-tier at ~5k MAU | Generous | Generous | Tie |
| Operational load on us | One more vendor | Zero (already running) | Supabase |
| Isolation of anon traffic from learner data | Separate DB = clean blast radius | Same DB = RLS-only isolation | InstantDB |

## Trade-off we accept

Taking on InstantDB means one more vendor + one more key (`$INSTANTDB_APP_ID`) + one more outage surface. We accept that because (a) ImpactLex is self-contained with a seed-snapshot fallback so a vendor outage never kills reads, (b) the offline-first + real-time story would otherwise cost us a few hundred lines of custom code on Supabase, and (c) anonymous glossary traffic is the wrong shape to mix with our learner RLS policies.

## Action items

1. Provision `impactlex` app on InstantDB, capture app ID.
2. Add to `.claude/.env.keys`: `INSTANTDB_APP_ID=<id>`.
3. Document the key in `.claude/rules/api-conventions.md` (new row).
4. Proceed to Phase 1 (schema + migration).

## Escape hatch

If InstantDB proves wrong in production (cost spike, maturity issue), the swap is:
- Replace `@instantdb/core` client in `impactlex/app.js` with `@supabase/supabase-js`.
- Port the three collections (`terms`, `bookmarks`, `contributions`) to Postgres tables with RLS.
- Rest of the app (UI, snapshot fallback, AI pipeline, embed helper) is backend-agnostic and stays.

Estimated swap cost: ~1 day.
