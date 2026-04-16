/**
 * Netlify Scheduled Function — Supabase Keepalive
 *
 * Supabase free-tier projects pause after ~1 week of inactivity.
 * This function runs weekly and makes a lightweight database query
 * via the REST API to guarantee activity, providing redundancy on top
 * of daily-engagement.mjs (which hits Edge Functions daily).
 *
 * Runs: every Sunday at 03:17 UTC (offset from daily-engagement's 02:30)
 *
 * Environment variables (set in Netlify dashboard):
 *   SUPABASE_URL              — e.g. https://ddyszmfffyedolkcugld.supabase.co
 *   SUPABASE_SERVICE_ROLE_KEY — service role key for the project
 */

const SUPABASE_URL = process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co";
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

export default async () => {
  if (!SERVICE_KEY) {
    console.log("[keepalive] SUPABASE_SERVICE_ROLE_KEY not set — skipping");
    return new Response(JSON.stringify({ error: "Missing service key" }), { status: 500 });
  }

  const timestamp = new Date().toISOString();
  const results = {};

  // 1. Auth API ping (counts as activity, no DB required)
  try {
    const authResp = await fetch(`${SUPABASE_URL}/auth/v1/settings`, {
      headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}` },
    });
    results.auth = { status: authResp.status };
  } catch (err) {
    results.auth = { error: err.message };
  }

  // 2. Database query — HEAD request on profiles table (minimal cost)
  try {
    const dbResp = await fetch(
      `${SUPABASE_URL}/rest/v1/profiles?select=id&limit=1`,
      {
        method: "HEAD",
        headers: {
          apikey: SERVICE_KEY,
          Authorization: `Bearer ${SERVICE_KEY}`,
          Prefer: "count=exact",
        },
      }
    );
    results.db = {
      status: dbResp.status,
      count: dbResp.headers.get("content-range"),
    };
  } catch (err) {
    results.db = { error: err.message };
  }

  // 3. Storage API ping
  try {
    const storageResp = await fetch(`${SUPABASE_URL}/storage/v1/bucket`, {
      headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}` },
    });
    results.storage = { status: storageResp.status };
  } catch (err) {
    results.storage = { error: err.message };
  }

  console.log(`[keepalive ${timestamp}]`, JSON.stringify(results));

  return new Response(
    JSON.stringify({ timestamp, ...results }),
    { headers: { "Content-Type": "application/json" } }
  );
};

// Schedule: Sundays at 03:17 UTC (weekly, offset from daily-engagement)
export const config = {
  schedule: "17 3 * * 0",
};
