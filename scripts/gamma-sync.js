#!/usr/bin/env node
/**
 * gamma-sync.js — Regenerate all ImpactMojo 101 courses via Gamma API
 * with consistent branding, fonts, imagery, and footer.
 *
 * Usage:
 *   GAMMA_API_KEY=sk-gamma-... node scripts/gamma-sync.js [--dry-run] [--course mel-basics]
 *
 * Options:
 *   --dry-run       Print payloads without calling the API
 *   --course SLUG   Regenerate a single course by slug
 *   --delay MS      Delay between API calls in ms (default: 5000)
 *   --resume        Skip courses already completed in gamma-sync-results.json
 */

const { execSync } = require("child_process");
const fs = require("fs");
const path = require("path");
const os = require("os");

// ─── Config ──────────────────────────────────────────────────────────────────

const API_BASE = "https://public-api.gamma.app/v1.0";
const API_KEY = process.env.GAMMA_API_KEY;
const FOLDER_ID = "fw1e4twcu3rypew"; // "101 Decks" folder
const POLL_INTERVAL = 5000; // 5s between status checks
const POLL_TIMEOUT = 900000; // 15min max wait per generation (60-slide decks can take 10min+)

// Closest built-in theme: clean, light, blue — matches ImpactMojo palette
const THEME_ID = "cornflower";

// ─── Art style per category ─────────────────────────────────────────────────

const ART_STYLES = {
  "MEL & Research": "Sepia-toned documentary photography of rural Indian communities, framed with Warli tribal art borders — geometric white dot-pattern margins on earthy terracotta edges",
  "Data & Technology": "Sepia-toned documentary photography of Indian village data collection and technology use, framed with Gond art borders — intricate dot-and-line nature patterns on dark margins",
  "Policy & Economics": "Sepia-toned documentary photography of Indian governance, markets, and public life, framed with Kalamkari art borders — flowing hand-drawn textile patterns in terracotta and indigo margins",
  "Gender & Equity": "Sepia-toned documentary photography of Indian women, girls, and diverse communities, framed with Madhubani art borders — bold crosshatched patterns in vibrant primary colors on margins",
  "Health & Communication": "Sepia-toned documentary photography of Indian rural health workers and community health settings, framed with Pattachitra art borders — ornamental narrative panels in jewel tones on margins",
  "Philosophy & Governance": "Sepia-toned documentary photography of Indian democratic institutions and community gatherings, framed with Pichwai art borders — lotus and nature motifs in deep green and gold margins",
};

// ─── Shared image & content style ───────────────────────────────────────────

const IMAGE_STYLE_BASE = [
  "MANDATORY: All photographs must show ONLY brown-skinned South Asian / Indian people. NEVER generate white, East Asian, or Western-looking people.",
  "MANDATORY: Settings must be rural Indian villages, peri-urban small towns, fields, mandis (markets), anganwadis, primary health centers, gram panchayat offices, community halls, river banks, farms. NEVER show glass offices, luxury interiors, Western cities, or affluent urban settings.",
  "Sepia-toned warm documentary photography style — like archival National Geographic or PRADAN field documentation.",
  "Show diverse people: women in sarees and salwar kameez, men in kurta-pyjama and dhotis, children in school uniforms, elders, transgender individuals (hijra community). Mixed ages and genders in every group shot.",
  "Include working animals where contextually relevant: cows, buffaloes, goats, bullocks with carts, chickens, dogs, elephants in forest/tribal areas.",
  "Activities: farming, hand-pumping water, SHG meetings, mid-day meals, ASHA workers visiting homes, children studying under trees, panchayat meetings, market days, brick kilns, handloom weaving, fishing.",
  "Emotional tone: dignity, agency, warmth, resilience. NOT poverty-porn. People should look engaged and capable, not helpless.",
  "Folk art borders from each category's tradition frame the photographs — visible decorative margins around the photo content.",
].join(" ");

// ─── Footer config ──────────────────────────────────────────────────────────

const HEADER_FOOTER = {
  bottomLeft: {
    type: "cardNumber",
  },
  bottomCenter: {
    type: "text",
    value: "www.impactmojo.in",
  },
  bottomRight: {
    type: "text",
    value: "CC BY-NC-SA 4.0",
  },
  hideFromFirstCard: false,
  hideFromLastCard: false,
};

// ─── Additional instructions for font & style enforcement ───────────────────

const ADDITIONAL_INSTRUCTIONS = [
  "FONTS: Use Inter for all headings and titles (bold/semibold). Use Amaranth for all body text and descriptions.",
  "BRANDING: This is an ImpactMojo course — a free development education platform for South Asia.",
  "AUDIENCE: Development professionals, students, researchers, and practitioners in South Asia.",
  "TONE: Educational, accessible, warm, rigorous but not academic. Avoid jargon where possible.",
  "",
  "STRUCTURE (follow this order strictly):",
  "1. TITLE CARD — Course name, subtitle, ImpactMojo branding, category label",
  "2. AGENDA / OUTLINE CARD — Numbered list of all sections covered in the deck, styled as a visual table of contents",
  "3-N. CONTENT SECTIONS (10-12 major sections) — Each major topic gets:",
  "   - A SECTION SEPARATOR CARD with the section number, title, and a relevant folk art illustration (full-bleed)",
  "   - 4-6 content cards for that section with concepts, case studies, diagrams, exercises",
  "CLOSING: Quiz/Self-Assessment, Key Takeaways, Glossary, Further Reading",
  "LAST CARD: Thank You — 'Thank You for Learning with ImpactMojo' with contact email: hello@impactmojo.in and link to www.impactmojo.in. Suggest 2-3 related courses to explore next.",
  "TARGET: 60 slides (the maximum). Do NOT compress. Every concept deserves its own slide.",
  "",
  "DIAGRAMS & CHARTS: Use plenty of diagrams, flowcharts, comparison tables, process flows, frameworks, and data visualizations.",
  "Make charts beautiful, colorful, and non-boring — use creative layouts like radial diagrams, Sankey flows, pyramid charts, matrix grids.",
  "Every section should have at least one visual framework, diagram, or chart. Never have 3+ text-only slides in a row.",
  "",
  "SECTION SEPARATORS: Use bold, visually distinct separator cards between major sections. Full-width background color or illustration. Section number + title only, no body text.",
  "",
  "LAYOUT: Clean layouts with generous whitespace. Use card-based sections.",
  "DIVERSITY: All human illustrations must show South Asian / brown-skinned people.",
  "IMAGERY: Use sepia-toned documentary photography of rural/peri-urban India. Frame photos with Indian folk art borders. All people MUST be brown-skinned South Asian. NO white people, NO Western/urban/luxury settings.",
  "CONTEXT: Rural India, community development, grassroots settings. Democratic and inclusive.",
  "ACCESSIBILITY: High contrast text. No text over busy backgrounds.",
].join("\n");

// ─── Course catalog ─────────────────────────────────────────────────────────

const COURSES = [
  // MEL & Research
  { slug: "mel-basics", title: "MEAL 101 — Monitoring, Evaluation, Accountability and Learning", category: "MEL & Research", description: "Monitoring, Evaluation, Accountability and Learning frameworks for impact measurement. Build foundational skills in MEL systems that drive adaptive management and demonstrate program impact." },
  { slug: "research-ethics", title: "Research Ethics 101", category: "MEL & Research", description: "Navigate ethical complexities of conducting research in development settings, from informed consent to data privacy and community benefit-sharing." },
  { slug: "visual-eth", title: "Visual Ethnography 101", category: "MEL & Research", description: "Harness the power of visual methods in development research, from participatory photography to video documentation and visual storytelling." },
  { slug: "obs2insight", title: "Getting to Insights from Field Observations 101", category: "MEL & Research", description: "Transform raw field observations into actionable insights through systematic observation techniques, pattern recognition, and analytical frameworks." },
  { slug: "eng-dev", title: "English for Development Professionals 101", category: "MEL & Research", description: "Master specialized vocabulary and communication strategies for international development work, from policy briefs to stakeholder consultations." },
  { slug: "qual-methods", title: "Qualitative Research Methods 101", category: "MEL & Research", description: "Master in-depth interviewing, focus group facilitation, and ethnographic techniques that capture rich contextual insights in development research." },

  // Data & Technology
  { slug: "data-lit", title: "Data Literacy 101", category: "Data & Technology", description: "Develop critical skills for understanding, interpreting, and communicating with data in development contexts, from survey design to visualization." },
  { slug: "data-feminism", title: "Data Feminism 101", category: "Data & Technology", description: "Explore how power dynamics shape data collection, analysis, and interpretation through an intersectional feminist framework." },
  { slug: "eda-hhs", title: "Exploratory Data Analysis for Household Surveys 101", category: "Data & Technology", description: "Develop skills for cleaning, exploring, and visualizing household survey data using statistical software and reproducible research practices." },
  { slug: "bi-analysis", title: "Bivariate Analysis 101", category: "Data & Technology", description: "Master techniques for examining relationships between two variables, from correlation analysis to cross-tabulations and simple regression." },
  { slug: "multivariate-basics", title: "Multivariate Analysis 101", category: "Data & Technology", description: "Master advanced statistical techniques for analyzing complex relationships among multiple variables, from factor analysis to structural equation modeling." },
  { slug: "irt-basics", title: "Item Response Theory 101", category: "Data & Technology", description: "Learn advanced psychometric techniques for developing and validating measurement instruments, from poverty indices to learning assessments." },
  { slug: "econometrics-101", title: "Econometrics 101", category: "Data & Technology", description: "Master statistical techniques for causal inference in development economics, from randomized controlled trials to quasi-experimental methods." },
  { slug: "digital-ethics", title: "Digital Ethics 101", category: "Data & Technology", description: "Navigate ethical challenges in digital development, from data privacy and algorithmic bias to digital divides and surveillance concerns." },

  // Policy & Economics
  { slug: "climate-essentials", title: "Climate Essentials 101", category: "Policy & Economics", description: "Understand the science, economics, and politics of climate change through a development lens, exploring mitigation, adaptation, and climate justice." },
  { slug: "dev-economics", title: "Development Economics 101", category: "Policy & Economics", description: "Master core theories of economic development from structural transformation to behavioral economics, examining why nations succeed or fail." },
  { slug: "pol-economy", title: "Political Economy 101", category: "Policy & Economics", description: "Unpack how political institutions, power structures, and economic systems interact to shape development outcomes and policy choices." },
  { slug: "cost-effectiveness", title: "Cost Effectiveness Analysis 101", category: "Policy & Economics", description: "Master economic evaluation techniques for comparing development interventions, from cost-benefit analysis to cost-utility assessments." },
  { slug: "livelihood-basics", title: "Livelihoods 101", category: "Policy & Economics", description: "Understand sustainable livelihoods frameworks and design interventions that build resilient economic opportunities for vulnerable populations." },
  { slug: "advocacy-basics", title: "Advocacy Basics 101", category: "Policy & Economics", description: "Develop skills for policy advocacy, from stakeholder mapping and message framing to campaign strategy and coalition building." },
  { slug: "fundraising-basics", title: "Fundraising Basics 101", category: "Policy & Economics", description: "Develop skills for resource mobilization in development, from grant writing to donor engagement and partnership building." },
  { slug: "post-truth-101", title: "Post Truth Politics 101", category: "Policy & Economics", description: "Analyze how misinformation, polarization, and erosion of institutional trust shape development outcomes in the digital age." },
  { slug: "dev-architecture", title: "Global Development Governance and Architecture 101", category: "Policy & Economics", description: "Navigate the complex ecosystem of development institutions from the UN system to multilateral banks and bilateral agencies." },

  // Gender & Equity
  { slug: "edu-pedagogy", title: "Education and Pedagogy 101", category: "Gender & Equity", description: "Discover evidence-based teaching methodologies and learning theories that drive educational outcomes in diverse developmental contexts." },
  { slug: "SRHR-basics", title: "Sexual and Reproductive Health and Rights 101", category: "Gender & Equity", description: "Understand fundamentals of SRHR, from clinical services to rights-based approaches and gender-transformative programming." },
  { slug: "wee-studies", title: "Women's Economic Empowerment 101", category: "Gender & Equity", description: "Explore strategies for enhancing women's economic participation, from financial inclusion to entrepreneurship and labor market interventions." },
  { slug: "social-margins", title: "Marginalised Identities 101", category: "Gender & Equity", description: "Examine how caste, ethnicity, disability, sexuality, and other identity markers create overlapping systems of marginalization." },
  { slug: "decent-work", title: "Decent Work For All 101", category: "Gender & Equity", description: "Explore ILO frameworks for promoting productive employment, labor rights, social protection, and social dialogue." },
  { slug: "care-economy-101", title: "Care Economy 101", category: "Gender & Equity", description: "Understand the economic value of unpaid care work and explore policies that support care workers while redistributing care responsibilities." },
  { slug: "sel-basics", title: "Social and Emotional Learning 101", category: "Gender & Equity", description: "Understand SEL frameworks and their application in education and youth development programs worldwide." },

  // Health & Communication
  { slug: "pub-health-basics", title: "Public Health 101", category: "Health & Communication", description: "Navigate fundamentals of epidemiology, health systems, and disease prevention strategies that underpin global health interventions." },
  { slug: "bcc-comms", title: "Behaviour Change Communications 101", category: "Health & Communication", description: "Master the psychology and practice of designing communication interventions that shift behaviors, from health to environmental conservation." },

  // Philosophy & Governance
  { slug: "ind-constitution", title: "Indian Constitution 101", category: "Philosophy & Governance", description: "Examine the constitutional framework guiding India's democracy, including fundamental rights, directive principles, and federal structure." },
  { slug: "inequality-basics", title: "Poverty and Inequality 101", category: "Philosophy & Governance", description: "Examine multidimensional poverty measurement, inequality indices, and structural drivers of economic disparities." },
  { slug: "decolonize-dev", title: "Decolonial Development 101", category: "Philosophy & Governance", description: "Challenge dominant development paradigms through postcolonial and decolonial frameworks questioning Western-centric approaches." },
  { slug: "community-dev", title: "Community Development 101", category: "Philosophy & Governance", description: "Master participatory approaches to community mobilization, from asset-based development to collective action and social capital." },
  { slug: "env-justice", title: "Environmental Justice 101", category: "Philosophy & Governance", description: "Explore how environmental degradation disproportionately impacts marginalized communities and frameworks for equitable environmental governance." },
  { slug: "toc-workbench", title: "Theory of Change Workbench 101", category: "MEL & Research", description: "Build and test Theories of Change for development programs using logical frameworks and results chains." },
];

// ─── HTTP helpers (using curl for DNS reliability) ───────────────────────────

function apiRequestOnce(method, apiPath, body) {
  const url = API_BASE + apiPath;
  const curlArgs = [
    "curl", "-s", "-w", "'\\n%{http_code}'",
    "-X", method,
    "-H", `'X-API-KEY: ${API_KEY}'`,
    "-H", "'Content-Type: application/json'",
    "--connect-timeout", "30",
    "--max-time", "120",
  ];

  let tmpFile;
  if (body) {
    tmpFile = path.join(os.tmpdir(), `gamma-payload-${Date.now()}.json`);
    fs.writeFileSync(tmpFile, JSON.stringify(body));
    curlArgs.push("-d", `@${tmpFile}`);
  }

  curlArgs.push(`'${url}'`);

  let raw;
  try {
    raw = execSync(curlArgs.join(" "), {
      encoding: "utf8",
      timeout: 120000,
      shell: "/bin/bash",
      maxBuffer: 10 * 1024 * 1024,
    }).trim();
  } finally {
    if (tmpFile && fs.existsSync(tmpFile)) fs.unlinkSync(tmpFile);
  }

  const lines = raw.split("\n");
  const statusCode = parseInt(lines.pop(), 10);
  const responseBody = lines.join("\n");

  let data;
  try {
    data = JSON.parse(responseBody);
  } catch {
    data = responseBody;
  }
  return { status: statusCode, data };
}

const MAX_RETRIES = 4;
const RETRY_BACKOFF = [2000, 4000, 8000, 16000];

async function apiRequest(method, apiPath, body) {
  for (let attempt = 0; attempt <= MAX_RETRIES; attempt++) {
    try {
      return apiRequestOnce(method, apiPath, body);
    } catch (err) {
      if (attempt === MAX_RETRIES) {
        throw new Error(`API ${method} ${apiPath} failed after ${MAX_RETRIES + 1} attempts: ${err.message}`);
      }
      const backoff = RETRY_BACKOFF[attempt] || 16000;
      console.log(`  ⚠ Network error (attempt ${attempt + 1}/${MAX_RETRIES + 1}), retrying in ${backoff / 1000}s...`);
      await sleep(backoff);
    }
  }
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// ─── Build generation payload for a course ──────────────────────────────────

function buildPayload(course) {
  const artStyle = ART_STYLES[course.category] || ART_STYLES["MEL & Research"];

  const inputText = [
    `# ${course.title}`,
    "",
    `## ImpactMojo 101 Course`,
    "",
    course.description,
    "",
    `Category: ${course.category}`,
    "",
    "Create a comprehensive, visually rich educational deck covering key concepts, frameworks, case studies, and practical applications for this topic in the South Asian development context.",
    "",
    "Structure (follow strictly):",
    "1. TITLE CARD — Course name, subtitle, 'ImpactMojo 101 Series', category badge",
    "2. AGENDA CARD — Visual outline/table of contents listing all sections",
    "3. LEARNING OBJECTIVES — What participants will be able to do after this course",
    "",
    "Then 10-12 MAJOR SECTIONS, each with:",
    "  - A bold SECTION SEPARATOR card (section number + title, full visual, no body text)",
    "  - 4-6 content cards per section covering:",
    "    * Core concepts and definitions",
    "    * A diagram, flowchart, or framework visual (EVERY section must have at least one)",
    "    * A real-world case study from India, Bangladesh, Nepal, Sri Lanka, or Pakistan",
    "    * Practical exercise, reflection prompt, or discussion question",
    "    * Comparison tables, matrix grids, or data visualizations where relevant",
    "  - Use flowcharts, process diagrams, matrix grids, radial charts, pyramid models, Venn diagrams, timelines — make them beautiful and non-boring",
    "",
    "Then closing cards:",
    "  - QUIZ / SELF-ASSESSMENT — 5-8 multiple choice or reflection questions to test understanding",
    "  - KEY TAKEAWAYS — Bullet summary of core learnings from all sections",
    "  - GLOSSARY — Key terms and definitions introduced in the course",
    "  - FURTHER READING — Books, papers, websites, and resources for deeper study",
    "  - THANK YOU — 'Thank You for Learning with ImpactMojo' / hello@impactmojo.in / www.impactmojo.in / suggest 2-3 related ImpactMojo 101 courses to explore next",
    "",
    "IMPORTANT: This deck MUST use all 60 slides. Do not compress content. Each concept deserves its own slide. Use generous visual slides between text-heavy ones. Fill every available slide.",
  ].join("\n");

  const imageStyle = `${artStyle}. ${IMAGE_STYLE_BASE}`;

  return {
    inputText,
    textMode: "generate",
    format: "presentation",
    numCards: 60,
    themeId: THEME_ID,
    additionalInstructions: ADDITIONAL_INSTRUCTIONS,
    imageOptions: {
      source: "aiGenerated",
      style: imageStyle,
    },
    textOptions: {
      amount: "medium",
      tone: "Educational, accessible, warm. Rigorous but approachable. South Asian development context.",
      audience: "Development professionals, students, researchers, and practitioners in South Asia. Beginner to intermediate level.",
      language: "en",
    },
    cardOptions: {
      dimensions: "16x9",
      headerFooter: HEADER_FOOTER,
    },
    folderIds: [FOLDER_ID],
    exportAs: "pdf",
  };
}

// ─── Poll for generation completion ─────────────────────────────────────────

async function pollGeneration(generationId) {
  const startTime = Date.now();
  let consecutiveErrors = 0;
  const MAX_CONSECUTIVE_ERRORS = 5;

  while (Date.now() - startTime < POLL_TIMEOUT) {
    await sleep(POLL_INTERVAL);

    let res;
    try {
      res = await apiRequest("GET", `/generations/${generationId}`);
    } catch (err) {
      consecutiveErrors++;
      console.error(`  Poll network error (${consecutiveErrors}/${MAX_CONSECUTIVE_ERRORS}): ${err.message}`);
      if (consecutiveErrors >= MAX_CONSECUTIVE_ERRORS) {
        throw new Error(`Polling abandoned after ${MAX_CONSECUTIVE_ERRORS} consecutive network failures`);
      }
      continue;
    }

    consecutiveErrors = 0; // reset on successful request

    if (res.status !== 200) {
      console.error(`  Poll HTTP error (${res.status}):`, JSON.stringify(res.data));
      continue;
    }

    const { status, gammaUrl, exportUrl } = res.data;
    console.log(`  Status: ${status}`);

    if (status === "completed") {
      return { gammaUrl, exportUrl };
    }
    if (status === "failed") {
      throw new Error(`Generation failed: ${JSON.stringify(res.data)}`);
    }
  }

  throw new Error(`Generation timed out after ${POLL_TIMEOUT / 1000}s`);
}

// ─── Main ───────────────────────────────────────────────────────────────────

async function main() {
  const args = process.argv.slice(2);
  const dryRun = args.includes("--dry-run");
  const courseIdx = args.indexOf("--course");
  const singleSlug = courseIdx !== -1 ? args[courseIdx + 1] : null;
  const delayIdx = args.indexOf("--delay");
  const delay = delayIdx !== -1 ? parseInt(args[delayIdx + 1], 10) : 5000;

  const resume = args.includes("--resume");

  if (!API_KEY) {
    console.error("Error: GAMMA_API_KEY environment variable not set");
    process.exit(1);
  }

  // Load existing results for resume and merge
  const resultsPath = path.join(__dirname, "..", "data", "gamma-sync-results.json");
  let existingResults = { results: [] };
  if (fs.existsSync(resultsPath)) {
    try {
      existingResults = JSON.parse(fs.readFileSync(resultsPath, "utf8"));
    } catch { /* start fresh */ }
  }
  const completedSlugs = new Set(
    existingResults.results
      .filter((r) => r.status === "completed")
      .map((r) => r.slug)
  );

  let courses = COURSES;
  if (singleSlug) {
    courses = COURSES.filter((c) => c.slug === singleSlug);
    if (courses.length === 0) {
      console.error(`No course found with slug: ${singleSlug}`);
      console.error("Available slugs:", COURSES.map((c) => c.slug).join(", "));
      process.exit(1);
    }
  }

  if (resume) {
    const before = courses.length;
    courses = courses.filter((c) => !completedSlugs.has(c.slug));
    console.log(`\n🔄 Resume mode: skipping ${before - courses.length} already-completed courses`);
  }

  console.log(`\n🎓 ImpactMojo Gamma Sync`);
  console.log(`   Courses: ${courses.length}`);
  console.log(`   Theme: ${THEME_ID}`);
  console.log(`   Folder: ${FOLDER_ID} (101 Decks)`);
  console.log(`   Mode: ${dryRun ? "DRY RUN" : "LIVE"}${resume ? " (RESUME)" : ""}\n`);

  const results = [];

  for (let i = 0; i < courses.length; i++) {
    const course = courses[i];
    console.log(`[${i + 1}/${courses.length}] ${course.title} (${course.slug})`);
    console.log(`   Category: ${course.category}`);

    const payload = buildPayload(course);

    if (dryRun) {
      console.log(`   Payload preview:`);
      console.log(`     textMode: ${payload.textMode}`);
      console.log(`     numCards: ${payload.numCards}`);
      console.log(`     theme: ${payload.themeId}`);
      console.log(`     imageStyle: ${payload.imageOptions.style.substring(0, 80)}...`);
      console.log(`     footer: ${JSON.stringify(HEADER_FOOTER.bottomCenter)} | ${JSON.stringify(HEADER_FOOTER.bottomRight)}`);
      console.log("");
      results.push({ slug: course.slug, status: "dry-run" });
      continue;
    }

    try {
      // Start generation
      const res = await apiRequest("POST", "/generations", payload);

      if (res.status !== 201 && res.status !== 200) {
        console.error(`   API error (${res.status}):`, JSON.stringify(res.data));
        results.push({ slug: course.slug, status: "error", error: res.data });
        continue;
      }

      const { generationId } = res.data;
      console.log(`   Generation started: ${generationId}`);

      // Poll for completion
      const { gammaUrl, exportUrl } = await pollGeneration(generationId);
      console.log(`   Done: ${gammaUrl}`);
      if (exportUrl) console.log(`   PDF: ${exportUrl}`);

      results.push({
        slug: course.slug,
        status: "completed",
        gammaUrl,
        exportUrl,
        generationId,
      });

      // Rate-limit delay between courses
      if (i < courses.length - 1) {
        console.log(`   Waiting ${delay / 1000}s before next...\n`);
        await sleep(delay);
      }
    } catch (err) {
      console.error(`   Failed: ${err.message}`);
      results.push({ slug: course.slug, status: "failed", error: err.message });
    }
  }

  // ─── Summary ────────────────────────────────────────────────────────────

  console.log("\n═══ Summary ═══");
  const completed = results.filter((r) => r.status === "completed");
  const failed = results.filter((r) => r.status === "failed" || r.status === "error");

  console.log(`Completed: ${completed.length}/${results.length}`);
  if (failed.length) {
    console.log(`Failed: ${failed.length}`);
    failed.forEach((f) => console.log(`  - ${f.slug}: ${f.error}`));
  }

  // Merge results into existing file (don't overwrite previous completions)
  if (!dryRun && results.length > 0) {
    const outputDir = path.dirname(resultsPath);
    if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

    // Merge: update existing entries or add new ones
    for (const result of results) {
      const idx = existingResults.results.findIndex((r) => r.slug === result.slug);
      if (idx >= 0) {
        // Only overwrite if new result is completed, or old was not completed
        if (result.status === "completed" || existingResults.results[idx].status !== "completed") {
          existingResults.results[idx] = result;
        }
      } else {
        existingResults.results.push(result);
      }
    }

    existingResults.syncDate = new Date().toISOString();
    existingResults.theme = THEME_ID;

    fs.writeFileSync(resultsPath, JSON.stringify(existingResults, null, 2));

    const totalCompleted = existingResults.results.filter((r) => r.status === "completed").length;
    console.log(`\nResults merged to: ${resultsPath}`);
    console.log(`Total completed across all runs: ${totalCompleted}/${COURSES.length}`);
  }
}

main().catch((err) => {
  console.error("Fatal error:", err);
  process.exit(1);
});
