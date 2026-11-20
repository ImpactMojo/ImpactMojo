// Supabase Edge Function — status-alert
//
// Sends an outage / recovery email for the ImpactMojo status monitor. Kept
// deliberately separate from `send-notification` so the status pipeline can
// never affect onboarding/newsletter email delivery.
//
// Called server-to-server by netlify/functions/status-probe.mjs:
//   POST /functions/v1/status-alert
//   Authorization: Bearer <SERVICE_ROLE_KEY>
//   { "to": "hello@impactmojo.in", "subject": "...", "html": "...",
//     "attachments": [{ "filename": "x.pdf", "content": "<base64>" }] }   // optional
//
// Environment:
//   RESEND_API_KEY            — required for delivery (shared with send-notification)
//   STATUS_ALERT_FROM         — optional From address (default below)
//   SUPABASE_SERVICE_ROLE_KEY — used only to authorize the caller
//
// If RESEND_API_KEY is unset it returns 200 {skipped:true} so the probe never
// breaks; auth failures return 401.

import { serve } from "https://deno.land/std@0.177.0/http/server.ts";

const FROM = Deno.env.get("STATUS_ALERT_FROM") || "ImpactMojo Status <notifications@impactmojo.in>";
const SERVICE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") || "";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, content-type",
  "Content-Type": "application/json",
};

serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: corsHeaders });
  if (req.method !== "POST") {
    return new Response(JSON.stringify({ error: "POST only" }), { status: 405, headers: corsHeaders });
  }

  // Only the service role may trigger alerts.
  const auth = req.headers.get("Authorization") || "";
  if (!SERVICE_KEY || auth !== `Bearer ${SERVICE_KEY}`) {
    return new Response(JSON.stringify({ error: "unauthorized" }), { status: 401, headers: corsHeaders });
  }

  let body: { to?: string; subject?: string; html?: string; attachments?: unknown };
  try { body = await req.json(); } catch { return new Response(JSON.stringify({ error: "bad json" }), { status: 400, headers: corsHeaders }); }
  const { to, subject, html } = body;
  if (!to || !subject || !html) {
    return new Response(JSON.stringify({ error: "to, subject, html required" }), { status: 400, headers: corsHeaders });
  }

  // Optional attachments, passed to Resend as given. Resend refuses a message
  // over 40 MB once encoded, so the caller keeps well under that; this only
  // checks the shape and a ceiling so a bad call cannot send junk.
  let attachments: { filename: string; content: string }[] | undefined;
  if (body.attachments !== undefined) {
    const a = body.attachments;
    const ok = Array.isArray(a) && a.length > 0 && a.length <= 10 &&
      a.every((x) => x && typeof x.filename === "string" && x.filename.length > 0 && x.filename.length <= 200 &&
        typeof x.content === "string" && x.content.length > 0);
    const total = ok ? (a as { content: string }[]).reduce((n, x) => n + x.content.length, 0) : 0;
    if (!ok || total > 30 * 1024 * 1024) {
      return new Response(JSON.stringify({ error: "attachments must be 1 to 10 items of {filename, content} under 30 MB" }), { status: 400, headers: corsHeaders });
    }
    attachments = a as { filename: string; content: string }[];
  }

  const resendKey = Deno.env.get("RESEND_API_KEY");
  if (!resendKey) {
    console.log("RESEND_API_KEY not set — skipping status email");
    return new Response(JSON.stringify({ skipped: true, reason: "no RESEND_API_KEY" }), { headers: corsHeaders });
  }

  const wrapped = `<div style="font-family:Inter,Helvetica,Arial,sans-serif;max-width:560px;margin:0 auto;color:#0F172A">
    <h2 style="font-size:18px;margin:0 0 12px">${subject}</h2>
    <div style="font-size:15px;line-height:1.6;color:#334155">${html}</div>
    <hr style="border:none;border-top:1px solid #E2E8F0;margin:20px 0">
    <p style="font-size:12px;color:#94A3B8">Automated message from ImpactMojo · impactmojo.in</p>
  </div>`;

  try {
    const resp = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: `Bearer ${resendKey}`, "Content-Type": "application/json" },
      body: JSON.stringify({ from: FROM, to: [to], subject, html: wrapped, ...(attachments ? { attachments } : {}) }),
    });
    if (!resp.ok) {
      const txt = await resp.text();
      console.error("Resend error:", resp.status, txt);
      return new Response(JSON.stringify({ error: "resend failed", status: resp.status }), { status: 502, headers: corsHeaders });
    }
    return new Response(JSON.stringify({ sent: true }), { headers: corsHeaders });
  } catch (err) {
    console.error("status-alert send failed:", err);
    return new Response(JSON.stringify({ error: String(err) }), { status: 500, headers: corsHeaders });
  }
});
