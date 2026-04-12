/**
 * Netlify Scheduled Function — Daily Engagement Pipeline
 *
 * Runs every day at 08:00 IST (02:30 UTC) and calls three Supabase
 * Edge Function endpoints:
 *   1. engagement-drip   — welcome + day 3/7/14 drip emails
 *   2. streak-reminders  — nudges users with active streaks who went inactive
 *   3. cohort-deadlines  — reminds cohort members of upcoming deadlines
 *
 * Environment variables (set in Netlify dashboard):
 *   SUPABASE_URL            — e.g. https://ddyszmfffyedolkcugld.supabase.co
 *   SUPABASE_SERVICE_ROLE_KEY — service role key for the project
 */

const SUPABASE_URL = process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co";
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

async function callEdgeFunction(path) {
  const url = `${SUPABASE_URL}/functions/v1/send-notification/${path}`;
  try {
    const resp = await fetch(url, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${SERVICE_KEY}`,
        "Content-Type": "application/json",
      },
    });
    const data = await resp.json();
    return { path, status: resp.status, ...data };
  } catch (err) {
    return { path, error: err.message };
  }
}

export default async () => {
  if (!SERVICE_KEY) {
    console.log("SUPABASE_SERVICE_ROLE_KEY not set — skipping");
    return new Response(JSON.stringify({ error: "Missing service key" }), { status: 500 });
  }

  console.log(`[${new Date().toISOString()}] Running daily engagement pipeline`);

  // Run all three in parallel
  const results = await Promise.all([
    callEdgeFunction("engagement-drip"),
    callEdgeFunction("streak-reminders"),
    callEdgeFunction("cohort-deadlines"),
  ]);

  console.log("Results:", JSON.stringify(results, null, 2));

  return new Response(JSON.stringify({ results }), {
    headers: { "Content-Type": "application/json" },
  });
};

// Schedule: 02:30 UTC = 08:00 IST, every day
export const config = {
  schedule: "30 2 * * *",
};
