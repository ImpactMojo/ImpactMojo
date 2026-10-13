/**
 * Netlify Function: subscribe (HTTP POST /api/subscribe)
 *
 * Free, gateway-less subscriptions. Creates a subscription row + the first
 * invoice in Supabase, emails the subscriber a UPI pay link, and returns a
 * payUrl the signup page redirects to. Renewals are handled monthly by
 * subscription-billing.mjs (a fresh QR/link each cycle).
 *
 * The plan and the amount are checked against PRICES below, so a request
 * cannot invent a plan or a price. Every value put into the email is escaped.
 * Each address and each caller can trigger only a few emails, because this
 * endpoint sends mail from the ImpactMojo sender to an address the caller
 * chooses. When the counter store is unavailable it sends nothing.
 *
 * Env (Netlify): SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, URL
 */
import { originAllowed, clientIp, rateLimit, esc, looksLikeEmail, jsonResponse as j, tooMany } from "../lib/guard.mjs";

const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const SITE = (process.env.URL || "https://www.impactmojo.in").replace(/\/$/, "");

// Prices as premium.html, upgrade.html and js/premium.js state them.
// "Organisation" is what /subscribe/ offers today, at the amounts that page
// charges. It is kept so that form keeps working.
export const PRICES = {
  practitioner: { name: "Practitioner", monthly: 399, annual: 3990 },
  professional: { name: "Professional", monthly: 999, annual: 9990 },
  organisation: { name: "Organisation", monthly: 999, annual: 9990 },
  team: { name: "Team", perSeatMonthly: 1499, maxSeats: 500 },
};

/** Resolve a request to a known plan and its server-side price, or explain why not. */
export function priceFor(planIn, cadenceIn, amountIn, seatsIn) {
  const plan = PRICES[String(planIn || "").trim().toLowerCase()];
  if (!plan) return { error: "unknown plan" };
  const cadence = cadenceIn === "annual" ? "annual" : "monthly";
  const given = amountIn == null || amountIn === "" ? null : Number(amountIn);
  let amount;
  if (plan.perSeatMonthly) {
    if (cadence !== "monthly") return { error: "the Team plan is billed monthly" };
    const seats = seatsIn != null ? Number(seatsIn) : (given != null ? given / plan.perSeatMonthly : NaN);
    if (!Number.isInteger(seats) || seats < 1 || seats > plan.maxSeats) return { error: "invalid number of seats" };
    amount = seats * plan.perSeatMonthly;
  } else {
    amount = plan[cadence];
  }
  if (given != null && given !== amount) return { error: "amount does not match the plan" };
  return { plan: plan.name, cadence, amount };
}

const sb = (path, opts = {}) => fetch(`${SUPABASE_URL}/rest/v1/${path}`, {
  ...opts,
  headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}`, "Content-Type": "application/json", ...(opts.headers || {}) },
});
function addInterval(d, cadence) { const x = new Date(d); cadence === "annual" ? x.setFullYear(x.getFullYear() + 1) : x.setMonth(x.getMonth() + 1); return x.toISOString().slice(0, 10); }

export const payLink = (ref, amount, plan, period) =>
  `${SITE}/subscribe/pay/?ref=${encodeURIComponent(ref)}&amt=${encodeURIComponent(amount)}&plan=${encodeURIComponent(plan)}${period ? `&period=${encodeURIComponent(period)}` : ""}`;

export function invoiceHtml(name, plan, amount, link, period) {
  const a = esc(amount);
  return `<p>Hi ${esc(name) || "there"},</p>
    <p>Thanks for subscribing to <strong>ImpactMojo ${esc(plan)}</strong>${period ? ` for ${esc(period)}` : ""}.</p>
    <p>Please complete your payment of <strong>₹${a}</strong> by UPI:</p>
    <p style="margin:20px 0"><a href="${esc(link)}" style="background:#0369A1;color:#fff;text-decoration:none;padding:12px 22px;border-radius:8px;font-weight:700;font-family:Inter,Arial">Pay ₹${a} by UPI →</a></p>
    <p>Scan the QR on that page, or pay to <strong>impactmojo@ibl</strong> and add the reference shown. We activate within 24 hours of payment.</p>`;
}

export async function emailInvoice(to, name, plan, amount, link, period) {
  if (!SERVICE_KEY) return;
  const subject = `Your ImpactMojo ${String(plan).replace(/[\r\n]+/g, " ")} subscription: pay ₹${amount}`;
  try {
    await fetch(`${SUPABASE_URL}/functions/v1/status-alert`, {
      method: "POST",
      headers: { Authorization: `Bearer ${SERVICE_KEY}`, "Content-Type": "application/json" },
      body: JSON.stringify({ to, subject, html: invoiceHtml(name, plan, amount, link, period) }),
      signal: AbortSignal.timeout(8000),
    });
  } catch (e) { console.log("[subscribe] email failed:", e.message); }
}

// Mail limits. A person subscribing once sends one request. These leave room
// for a retry or two and stop a script from mailing strangers.
const PER_IP_HOUR = 5;
const PER_RECIPIENT_DAY = 3;
const UNAVAILABLE = "Subscriptions are briefly unavailable. Please try again shortly.";

export default async (req, context) => {
  if (req.method !== "POST") return j({ error: "POST only" }, 405);
  if (!originAllowed(req)) return j({ error: "forbidden" }, 403);
  if (!SERVICE_KEY) return j({ error: "not configured" }, 503);
  let b; try { b = await req.json(); } catch { return j({ error: "bad json" }, 400); }
  if (!b || typeof b !== "object") return j({ error: "bad json" }, 400);
  const name = String(b.name || "").trim().slice(0, 100);
  const email = String(b.email || "").trim().toLowerCase();
  if (!looksLikeEmail(email)) return j({ error: "a valid email is required" }, 400);
  const price = priceFor(b.plan, b.cadence, b.amount, b.seats);
  if (price.error) return j({ error: price.error }, 400);
  const { plan, cadence, amount } = price;

  const ipLimit = await rateLimit({ bucket: "subscribe-ip", id: clientIp(req, context), limit: PER_IP_HOUR, windowSec: 3600, failClosed: true });
  if (!ipLimit.ok) return ipLimit.reason === "limited"
    ? tooMany("Too many requests. Please try again later.", ipLimit.retryAfter)
    : j({ error: UNAVAILABLE }, 503);
  const toLimit = await rateLimit({ bucket: "subscribe-to", id: email, limit: PER_RECIPIENT_DAY, windowSec: 86400, failClosed: true });
  if (!toLimit.ok) return toLimit.reason === "limited"
    ? tooMany("This address has already been sent an invoice today. Please check your inbox.", toLimit.retryAfter)
    : j({ error: UNAVAILABLE }, 503);

  const today = new Date().toISOString().slice(0, 10);
  const period = today.slice(0, 7);
  try {
    const res = await sb("subscriptions", {
      method: "POST", headers: { Prefer: "return=representation" },
      body: JSON.stringify({ name, email, plan, cadence, amount, status: "pending", next_due: addInterval(today, cadence) }),
    });
    if (!res.ok) {
      console.log("[subscribe] insert failed:", res.status, (await res.text()).slice(0, 400));
      return j({ error: "could not create the subscription" }, 502);
    }
    const row = (await res.json())[0];
    const ref = `IMX-${plan.slice(0, 4).toUpperCase()}-${period.replace("-", "")}-${row.id.slice(0, 6).toUpperCase()}`;
    await sb("subscription_payments", { method: "POST", body: JSON.stringify({ subscription_id: row.id, period, amount, reference: ref, status: "invoiced" }) });
    const link = payLink(ref, amount, plan, period);
    await emailInvoice(email, name, plan, amount, link, period);
    return j({ ok: true, payUrl: link });
  } catch (e) {
    console.log("[subscribe] failed:", e && e.message);
    return j({ error: "something went wrong" }, 500);
  }
};

export const config = { path: "/api/subscribe" };
