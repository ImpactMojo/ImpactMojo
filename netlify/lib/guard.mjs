/**
 * Shared request guards for the Netlify Functions.
 *
 * Lives outside netlify/functions/ on purpose: every top-level file in that
 * folder is deployed as its own function, while a module imported from here is
 * bundled into each function that uses it.
 *
 *   originAllowed(req)   the request came from a page on this site
 *   clientIp(req, ctx)   the caller's address as Netlify reports it
 *   rateLimit({...})     a fixed-window counter in Netlify Blobs
 *   safeEqual(a, b)      constant-time comparison for keys and tokens
 *   esc(v)               HTML escaping for anything put into a page or email
 *
 * Counters are kept under a SHA-256 of the IP address or email, so the store
 * never holds either in readable form.
 */
import crypto from "node:crypto";

export const ALLOWED_ORIGINS = ["https://www.impactmojo.in", "https://impactmojo.in"];
// Production on its Netlify address, deploy previews and branch deploys.
const NETLIFY_ORIGIN = /^https:\/\/([a-z0-9-]+--)?impactmojo\.netlify\.app$/;
const LOCAL_ORIGIN = /^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/;

/**
 * A browser sends Origin on every cross-origin request and on same-origin POST.
 * Where it is absent, Sec-Fetch-Site must say the request is same-origin; a
 * request carrying neither header is not from a page on this site.
 */
export function originAllowed(req) {
  const origin = req.headers.get("origin");
  if (origin) {
    if (ALLOWED_ORIGINS.includes(origin) || NETLIFY_ORIGIN.test(origin)) return true;
    return process.env.NETLIFY_DEV === "true" && LOCAL_ORIGIN.test(origin);
  }
  return req.headers.get("sec-fetch-site") === "same-origin";
}

export function clientIp(req, context) {
  return (
    (context && context.ip) ||
    req.headers.get("x-nf-client-connection-ip") ||
    (req.headers.get("x-forwarded-for") || "").split(",")[0].trim() ||
    "unknown"
  );
}

export function safeEqual(a, b) {
  const x = Buffer.from(String(a == null ? "" : a));
  const y = Buffer.from(String(b == null ? "" : b));
  // Compare digests so unequal lengths take the same time as equal ones.
  const hx = crypto.createHash("sha256").update(x).digest();
  const hy = crypto.createHash("sha256").update(y).digest();
  return crypto.timingSafeEqual(hx, hy) && x.length === y.length;
}

export const esc = (v) => String(v == null ? "" : v)
  .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
  .replace(/"/g, "&quot;").replace(/'/g, "&#39;");

export const looksLikeEmail = (v) =>
  typeof v === "string" && v.length <= 254 && /^[^\s@<>"'`]+@[^\s@<>"'`]+\.[^\s@<>"'`]+$/.test(v);

const hash = (v) => crypto.createHash("sha256").update(String(v)).digest("hex").slice(0, 32);

// ---- Blobs store --------------------------------------------------------
// Tests replace the factory with an in-memory store; production imports
// @netlify/blobs on first use, the same way the other functions do.
let storeFactory = async (name) => {
  const { getStore } = await import("@netlify/blobs");
  return getStore({ name, consistency: "strong" });
};
export function setStoreFactory(fn) { storeFactory = fn; }

const STORE = "rate-limits";

/**
 * Fixed-window counter. Returns one of
 *   { ok: true }                               under the limit, counted
 *   { ok: false, reason: "limited", retryAfter } over the limit
 *   { ok: false, reason: "unavailable" }        store failed and failClosed
 *   { ok: true, degraded: true }               store failed and fail open
 *
 * `cost` lets one request count as several units (a translation batch counts
 * each string it sends upstream).
 */
export async function rateLimit({ bucket, id, limit, windowSec, cost = 1, failClosed = false }) {
  const now = Date.now();
  const win = Math.floor(now / (windowSec * 1000));
  const key = `${bucket}/${win}/${hash(id)}`;
  let store;
  try {
    store = await storeFactory(STORE);
  } catch (e) {
    console.log(`[guard] ${bucket}: store unavailable:`, e && e.message);
    return failClosed ? { ok: false, reason: "unavailable" } : { ok: true, degraded: true };
  }
  try {
    const used = parseInt((await store.get(key)) || "0", 10) || 0;
    if (used + cost > limit) {
      const retryAfter = Math.max(1, Math.ceil(((win + 1) * windowSec * 1000 - now) / 1000));
      return { ok: false, reason: "limited", retryAfter };
    }
    await store.set(key, String(used + cost));
    return { ok: true };
  } catch (e) {
    console.log(`[guard] ${bucket}: counter failed:`, e && e.message);
    return failClosed ? { ok: false, reason: "unavailable" } : { ok: true, degraded: true };
  }
}

/** Read a counter without changing it (used to check a budget before spending it). */
export async function peekCount({ bucket, id, windowSec }) {
  const win = Math.floor(Date.now() / (windowSec * 1000));
  try {
    const store = await storeFactory(STORE);
    return parseInt((await store.get(`${bucket}/${win}/${hash(id)}`)) || "0", 10) || 0;
  } catch {
    return 0;
  }
}

export const jsonResponse = (obj, status = 200, extra = {}) => new Response(JSON.stringify(obj), {
  status,
  headers: { "Content-Type": "application/json", "Cache-Control": "no-store", ...extra },
});

/** The 429 a limited caller receives, with Retry-After set. */
export const tooMany = (message, retryAfter) =>
  jsonResponse({ error: message }, 429, retryAfter ? { "Retry-After": String(retryAfter) } : {});
