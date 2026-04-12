/**
 * Netlify Scheduled Function — Monthly Newsletter
 *
 * Runs on the 15th of every month at 10:00 IST (04:30 UTC).
 * Reads CHANGELOG.md and docs/changelog.md for what's new in the past 30 days,
 * reads search-index.json for current content counts, and sends a monthly
 * update email to all users via the send-notification Edge Function.
 *
 * Environment variables (set in Netlify dashboard):
 *   SUPABASE_URL              — Supabase project URL
 *   SUPABASE_SERVICE_ROLE_KEY — service role key
 */

const SUPABASE_URL = process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co";
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const SITE_URL = "https://www.impactmojo.in";

// Parse the user-facing changelog (docs/changelog.md) for recent "Added" items
async function getRecentChanges() {
  try {
    const resp = await fetch(`${SITE_URL}/docs/changelog.md`);
    const text = await resp.text();

    // Find entries from the last 35 days
    const cutoff = new Date();
    cutoff.setDate(cutoff.getDate() - 35);

    const highlights = [];
    const lines = text.split("\n");
    let currentDate = null;
    let inAdded = false;

    for (const line of lines) {
      // Match version headers like "## v10.16.0 — April 8, 2026"
      const versionMatch = line.match(/^## .+?—\s*(.+)$/);
      if (versionMatch) {
        const parsed = new Date(versionMatch[1].trim());
        if (!isNaN(parsed.getTime())) {
          currentDate = parsed;
        }
        inAdded = false;
        continue;
      }

      // Track if we're in an "Added" section
      if (line.match(/^### Added/i)) {
        inAdded = true;
        continue;
      }
      if (line.match(/^### /)) {
        inAdded = false;
        continue;
      }

      // Only collect "Added" items from recent dates
      if (inAdded && currentDate && currentDate >= cutoff) {
        const itemMatch = line.match(/^- \*\*(.+?)\*\*\s*[—–-]\s*(.+)/);
        if (itemMatch) {
          highlights.push({
            title: itemMatch[1].replace(/`/g, ""),
            description: itemMatch[2].substring(0, 150).replace(/`/g, ""),
          });
        }
      }
    }

    return highlights.slice(0, 5); // Max 5 highlights
  } catch (err) {
    console.error("Failed to parse changelog:", err);
    return [];
  }
}

// Get content counts from search index
async function getContentCounts() {
  try {
    const resp = await fetch(`${SITE_URL}/data/search-index.json`);
    const items = await resp.json();
    const counts = {};
    for (const item of items) {
      const t = (item.type || "other").toLowerCase();
      counts[t] = (counts[t] || 0) + 1;
    }
    return { counts, total: items.length };
  } catch (err) {
    console.error("Failed to fetch search index:", err);
    return { counts: {}, total: 0 };
  }
}

function getMonthName() {
  return new Date().toLocaleString("en-IN", { month: "long", year: "numeric" });
}

export default async () => {
  if (!SERVICE_KEY) {
    console.log("SUPABASE_SERVICE_ROLE_KEY not set — skipping");
    return new Response(JSON.stringify({ error: "Missing service key" }), { status: 500 });
  }

  const month = getMonthName();
  console.log(`[${new Date().toISOString()}] Sending monthly newsletter for ${month}`);

  const [recentChanges, stats] = await Promise.all([
    getRecentChanges(),
    getContentCounts(),
  ]);

  const subject = `What's new on ImpactMojo — ${month}`;

  // Build intro with real counts
  const gameCount = stats.counts.game || 16;
  const labCount = stats.counts.lab || 11;
  const courseCount = stats.counts.course || 49;
  const intro = `Here's your monthly update from ImpactMojo. The platform now has <strong>${gameCount} games</strong>, <strong>${labCount} labs</strong>, <strong>${courseCount} courses</strong>, and <strong>${stats.total}+ resources</strong> — all free, as always.`;

  // Build highlights from changelog + evergreen content
  const highlights = [];

  // Add recent changes (with best-guess URLs)
  for (const change of recentChanges) {
    highlights.push({
      title: change.title,
      description: change.description,
      url: "/docs/#/changelog",
    });
  }

  // If no recent changes found, use evergreen highlights
  if (highlights.length === 0) {
    highlights.push(
      {
        title: "Practitioner Starter Kit",
        description: "Our 10 most essential handouts — research design, econometrics, policy tracking, and more.",
        url: "/starter-kit.html",
      },
      {
        title: "Interactive Games",
        description: `${gameCount} games covering public goods, cooperation, climate action, network effects, and more.`,
        url: "/#games",
      },
      {
        title: "Browser Labs",
        description: "Build a Theory of Change, design an M&E plan, or map stakeholders — all in your browser.",
        url: "/#labs",
      },
    );
  }

  // Always add the starter kit as a final highlight if not already there
  if (!highlights.some((h) => h.url === "/starter-kit.html")) {
    highlights.push({
      title: "Practitioner Starter Kit",
      description: "Haven't seen it yet? 10 hand-picked handouts for development practitioners.",
      url: "/starter-kit.html",
    });
  }

  const premiumNote = `Enjoying ImpactMojo? <strong>Premium</strong> gives you professional tools like VaniScribe AI transcription, realistic datasets, and workshop templates — starting at \u20B9399/month. <a href="${SITE_URL}/premium-letter.html" style="color:#F59E0B">Learn more</a> &middot; Or <a href="${SITE_URL}/index.html#support" style="color:#F59E0B">make a one-time contribution</a> to keep the platform free.`;

  // Call the monthly-update endpoint
  try {
    const resp = await fetch(`${SUPABASE_URL}/functions/v1/send-notification/monthly-update`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${SERVICE_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ subject, intro, highlights, premium_note: premiumNote }),
    });
    const data = await resp.json();
    console.log("Monthly newsletter result:", JSON.stringify(data));
    return new Response(JSON.stringify(data), {
      headers: { "Content-Type": "application/json" },
    });
  } catch (err) {
    console.error("Monthly newsletter failed:", err);
    return new Response(JSON.stringify({ error: err.message }), { status: 500 });
  }
};

// Schedule: 04:30 UTC on the 15th = 10:00 IST on the 15th of every month
export const config = {
  schedule: "30 4 15 * *",
};
