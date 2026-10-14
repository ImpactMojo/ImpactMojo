/**
 * Netlify Function — pack-content
 *
 * Serves the paid modules of a Practice Pack to a reader who has access. The
 * pages carry only the free modules; the rest live in the private Supabase
 * "products" bucket at practice-packs/<slug>.json, written there by
 * scripts/practice-packs/split-gated.py.
 *
 *   GET /api/pack-content?slug=tor-writing
 *   Authorization: Bearer <the reader's Supabase access token>
 *
 * Access is the same rule js/practice-pack-gate.js shows in the page: a
 * Practitioner tier or above with a subscription that has not lapsed, a
 * purchase of this one pack in profiles.resource_grants, or a site admin. The
 * difference is that here the profile is read with the service key after the
 * token is checked with Supabase Auth, so editing the browser's copy of the
 * profile unlocks nothing.
 *
 * Environment (Netlify): SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY
 */
import { originAllowed, clientIp, rateLimit } from "../lib/guard.mjs";

const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

export const PACKS = new Set([
  "climate-evaluation", "critiquing-evidence", "donor-reporting", "education-evaluation",
  "focus-group-discussion", "gender-impact", "governance-evaluation", "health-evaluation",
  "livelihoods-evaluation", "logframe-building", "media-evaluation", "mel-from-scratch",
  "policy-evaluation", "programme-costing", "sel-evaluation", "stakeholder-mapping",
  "survey-instrument", "tor-writing",
]);

const TIERS = ["explorer", "practitioner", "professional", "organization"];

/** The same rule as evaluate() in js/practice-pack-gate.js, plus site admins. */
export function hasAccess(profile, slug) {
  if (!profile) return false;
  if (profile.role === "admin") return true;
  const status = profile.subscription_status;
  const lapsed = status && status !== "active" && status !== "trialing";
  if (!lapsed && TIERS.indexOf(profile.subscription_tier || "explorer") >= TIERS.indexOf("practitioner")) return true;
  const g = profile.resource_grants;
  if (Array.isArray(g) && g.includes(slug)) return true;
  if (g && typeof g === "object" && !Array.isArray(g) && g[slug]) return true;
  return false;
}

const json = (o, s = 200) =>
  new Response(JSON.stringify(o), {
    status: s,
    headers: { "Content-Type": "application/json", "Cache-Control": "private, no-store" },
  });

export default async (req, context) => {
  if (req.method !== "GET") return json({ error: "method not allowed" }, 405);
  if (!originAllowed(req)) return json({ error: "forbidden" }, 403);
  if (!SERVICE_KEY) return json({ error: "not configured" }, 503);

  const slug = new URL(req.url).searchParams.get("slug") || "";
  if (!PACKS.has(slug)) return json({ error: "unknown pack" }, 404);

  const auth = req.headers.get("authorization") || "";
  const token = auth.startsWith("Bearer ") ? auth.slice(7).trim() : "";
  if (!token) return json({ error: "sign in required" }, 401);

  const limit = await rateLimit({ bucket: "pack-content-ip", id: clientIp(req, context), limit: 120, windowSec: 3600 });
  if (!limit.ok) return json({ error: "too many requests" }, 429);

  try {
    const u = await fetch(`${SUPABASE_URL}/auth/v1/user`, { headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${token}` }, signal: AbortSignal.timeout(8000) });
    if (!u.ok) return json({ error: "sign in required" }, 401);
    const user = await u.json();
    if (!user || !user.id) return json({ error: "sign in required" }, 401);

    const p = await fetch(
      `${SUPABASE_URL}/rest/v1/profiles?id=eq.${encodeURIComponent(user.id)}&select=role,subscription_tier,subscription_status,resource_grants`,
      { headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}` } },
    );
    if (!p.ok) return json({ error: "could not check access" }, 502);
    const rows = await p.json();
    if (!hasAccess(rows[0], slug)) return json({ error: "no access" }, 403);

    const f = await fetch(`${SUPABASE_URL}/storage/v1/object/products/practice-packs/${slug}.json`, {
      headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}` },
    });
    if (!f.ok) {
      console.log("[pack-content] storage read failed:", slug, f.status);
      return json({ error: "content unavailable" }, 502);
    }
    const data = await f.json();
    return json({ slug, panels: data.panels || {} });
  } catch (e) {
    console.log("[pack-content] failed:", e && e.message);
    return json({ error: "something went wrong" }, 500);
  }
};

export const config = { path: "/api/pack-content" };
