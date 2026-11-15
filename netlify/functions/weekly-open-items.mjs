/**
 * Netlify Scheduled Function: the weekly list of form entries nobody has closed.
 *
 * Every form on the site keeps a copy of each submission in the Supabase table
 * form_submissions, with status "new". Until 2026-11-15 nothing ever changed
 * that status, so the table could not answer "who is still waiting on us?".
 * An enquiry from an NGO sat unanswered-looking for three weeks beside spam,
 * and a grievance was found only by reading Netlify by hand.
 *
 * Each Monday this sends the owner one email listing every entry still "new",
 * oldest first, with a signed "Mark as handled" link per entry (served by
 * /api/confirm, type=handled). A delivered product order is closed by the
 * delivery itself. When nothing is open, no email is sent.
 *
 * Runs: Mondays at 03:30 UTC (09:00 IST).
 * Env: ADMIN_KEY, STATUS_ALERT_EMAIL, SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, URL
 */
import crypto from "node:crypto";
import { looksLikeJunk } from "../lib/guard.mjs";

const SITE = (process.env.URL || "https://www.impactmojo.in").replace(/\/$/, "");
const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const ADMIN_KEY = process.env.ADMIN_KEY || "";
const ADMIN_EMAIL = process.env.STATUS_ALERT_EMAIL || "hello@impactmojo.in";

const esc = (v) => String(v == null ? "" : v)
  .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
  .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
const sign = (parts) => crypto.createHmac("sha256", ADMIN_KEY).update(parts.join("|")).digest("hex").slice(0, 32);

// The fields worth showing for an entry, in the order a reader wants them.
const SHOW = ["name", "contact_name", "organisation", "organization", "organisation-role", "product", "upi_ref", "subject", "category",
  "event_title", "problem", "message", "description", "what", "own-problem-description"];

// Junk that was stored before the form began labelling it is listed last and
// labelled, never dropped.
const isJunk = (row) => looksLikeJunk(row.data);

export function buildEmail(rows, now = Date.now()) {
  const real = rows.filter((r) => !isJunk(r)), junk = rows.filter(isJunk);
  const item = (r) => {
    const d = r.data || {};
    const ts = String(now);
    const link = `${SITE}/api/confirm?type=handled&email=${encodeURIComponent(ADMIN_EMAIL)}&key=${r.id}&ts=${ts}&sig=${sign(["handled", ADMIN_EMAIL, r.id, ts])}`;
    const days = Math.max(0, Math.floor((now - Date.parse(r.submitted_at)) / 86400000));
    const lines = SHOW.filter((k) => String(d[k] == null ? "" : d[k]).trim())
      .map((k) => `<strong>${esc(k.replace(/[-_]/g, " "))}:</strong> ${esc(String(d[k]).trim().slice(0, 400))}`).join("<br>");
    return `<div style="border:1px solid #E2E8F0;border-radius:8px;padding:12px 14px;margin:10px 0;font-family:Inter,Arial;font-size:14px">
      <div style="color:#475569;font-size:12px">${esc(r.form_name)} · ${esc(String(r.submitted_at).slice(0, 10))} · waiting ${days} day${days === 1 ? "" : "s"}</div>
      <div style="margin:6px 0"><strong>${esc(r.email || "(no email)")}</strong></div>
      <div style="color:#334155;line-height:1.5">${lines || "(no details)"}</div>
      <p style="margin:10px 0 0"><a href="${esc(link)}" style="color:#0369A1;font-weight:700">Mark as handled</a></p>
    </div>`;
  };
  const html = `<p style="font-family:Inter,Arial;font-size:14px">${real.length} form ${real.length === 1 ? "entry is" : "entries are"} still open on ImpactMojo, oldest first. Reply to each person from your own mail, then mark the entry as handled so it leaves this list.</p>
    ${real.map(item).join("")}
    ${junk.length ? `<p style="font-family:Inter,Arial;font-size:13px;color:#64748B;margin-top:22px">${junk.length} more ${junk.length === 1 ? "entry looks" : "entries look"} like spam. Mark them as handled to clear them.</p>${junk.map(item).join("")}` : ""}`;
  return { subject: `ImpactMojo: ${real.length} open form ${real.length === 1 ? "entry" : "entries"}`, html, real: real.length, junk: junk.length };
}

export default async () => {
  if (!SERVICE_KEY || !ADMIN_KEY) { console.log("[open-items] not configured"); return new Response("not configured", { status: 500 }); }
  const r = await fetch(`${SUPABASE_URL}/rest/v1/form_submissions?status=eq.new&select=id,form_name,email,data,submitted_at&order=submitted_at.asc&limit=200`, {
    headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}` },
  });
  if (!r.ok) { console.log("[open-items] read failed", r.status); return new Response("read failed", { status: 502 }); }
  const rows = await r.json();
  if (!rows.length) { console.log("[open-items] nothing open"); return new Response("nothing open"); }
  const mail = buildEmail(rows);
  const m = await fetch(`${SUPABASE_URL}/functions/v1/status-alert`, {
    method: "POST", headers: { Authorization: `Bearer ${SERVICE_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({ to: ADMIN_EMAIL, subject: mail.subject, html: mail.html }),
  });
  const j = await m.json().catch(() => ({}));
  console.log("[open-items]", rows.length, "open;", mail.junk, "look like spam; mail", m.status, JSON.stringify(j).slice(0, 120));
  return new Response(JSON.stringify({ open: rows.length, sent: j && j.sent === true }), { headers: { "Content-Type": "application/json" } });
};

export const config = { schedule: "30 3 * * 1" };
