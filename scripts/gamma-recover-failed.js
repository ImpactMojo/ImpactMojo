#!/usr/bin/env node
/**
 * Recovers Gamma presentations that were created but timed out during polling.
 * Checks generation IDs and patches gamma-sync-results.json with recovered URLs.
 */

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const API_BASE = "https://public-api.gamma.app/v1.0";
const API_KEY = process.env.GAMMA_API_KEY;

if (!API_KEY) {
  console.error("GAMMA_API_KEY env var required");
  process.exit(1);
}

const RESULTS_PATH = path.join(__dirname, "..", "data", "gamma-sync-results.json");
const LOG_PATH = path.join(__dirname, "..", "data", "gamma-sync.log");

function apiGet(endpoint) {
  const cmd = `curl -s -X GET -H "X-API-KEY: ${API_KEY}" -H "Content-Type: application/json" "${API_BASE}${endpoint}"`;
  const out = execSync(cmd, { encoding: "utf8" });
  return JSON.parse(out);
}

// Parse log to find generation IDs for failed courses
function extractFailedGenerations() {
  const log = fs.readFileSync(LOG_PATH, "utf8");
  const lines = log.split("\n");
  const failed = [];
  let currentSlug = null;
  let currentGenId = null;

  for (const line of lines) {
    const courseMatch = line.match(/^\[\d+\/\d+\]\s+.+\(([a-z0-9-]+)\)$/);
    if (courseMatch) {
      currentSlug = courseMatch[1];
      currentGenId = null;
    }
    const genMatch = line.match(/Generation started:\s+(\S+)/);
    if (genMatch) {
      currentGenId = genMatch[1];
    }
    if (line.includes("Failed:") && currentSlug && currentGenId) {
      failed.push({ slug: currentSlug, generationId: currentGenId });
    }
  }
  return failed;
}

async function main() {
  const failedGens = extractFailedGenerations();
  if (failedGens.length === 0) {
    console.log("No failed generations found in log.");
    return;
  }

  console.log(`Found ${failedGens.length} failed generation(s) to recover:`);
  const recovered = [];

  for (const { slug, generationId } of failedGens) {
    console.log(`\n  Checking ${slug} (${generationId})...`);
    try {
      const data = apiGet(`/generations/${generationId}`);
      if (data.status === "completed") {
        console.log(`  ✓ Recovered: ${data.gammaUrl}`);
        recovered.push({
          slug,
          status: "completed",
          gammaUrl: data.gammaUrl,
          exportUrl: data.exportUrl,
          generationId,
          recovered: true,
        });
      } else {
        console.log(`  ✗ Status: ${data.status}`);
      }
    } catch (err) {
      console.error(`  ✗ Error: ${err.message}`);
    }
  }

  if (recovered.length === 0) {
    console.log("\nNo generations recovered.");
    return;
  }

  // Patch results file
  if (fs.existsSync(RESULTS_PATH)) {
    const results = JSON.parse(fs.readFileSync(RESULTS_PATH, "utf8"));
    for (const rec of recovered) {
      const idx = results.results.findIndex((r) => r.slug === rec.slug);
      if (idx >= 0) {
        results.results[idx] = rec;
        console.log(`  Updated existing entry for ${rec.slug}`);
      } else {
        results.results.push(rec);
        console.log(`  Added new entry for ${rec.slug}`);
      }
    }
    results.recoveryDate = new Date().toISOString();
    fs.writeFileSync(RESULTS_PATH, JSON.stringify(results, null, 2));
    console.log(`\nResults file updated: ${RESULTS_PATH}`);
  } else {
    console.log("\nResults file doesn't exist yet (sync still running?).");
    console.log("Recovered URLs:");
    recovered.forEach((r) => console.log(`  ${r.slug}: ${r.gammaUrl}`));
  }

  console.log(`\n${recovered.length} generation(s) recovered.`);
}

main().catch(console.error);
