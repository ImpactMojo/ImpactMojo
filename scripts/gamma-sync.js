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
const POLL_TIMEOUT = 600000; // 10min max wait per generation (45-card decks take ~3-4min)

// Closest built-in theme: clean, light, blue — matches ImpactMojo palette
const THEME_ID = "cornflower";

// ─── Art style per category ─────────────────────────────────────────────────

const ART_STYLES = {
  "MEL & Research": "Warli tribal art style — geometric white figures on earthy backgrounds, dot-pattern borders, minimalist folk storytelling",
  "Data & Technology": "Gond art style — intricate dot-and-line patterns, nature motifs with data elements, vibrant earth tones on dark backgrounds",
  "Policy & Economics": "Kalamkari art style — flowing hand-drawn textile patterns, detailed narrative scenes, warm terracotta and indigo palette",
  "Gender & Equity": "Madhubani art style — bold outlines with crosshatching fill, symmetric compositions, vibrant primary colors on natural backgrounds",
  "Health & Communication": "Pattachitra art style — ornamental borders, narrative panel structure, rich jewel tones with fine line detail",
  "Philosophy & Governance": "Pichwai art style — devotional painting traditions, lotus and nature motifs, deep greens and golds with fine brushwork",
};

// ─── Shared image & content style ───────────────────────────────────────────

const IMAGE_STYLE_BASE = [
  "Sargam-style clean line SVG illustrations.",
  "Indian folk art inspired, South Asian context.",
  "Show diverse brown-skinned South Asian people — women, men, children, transgender individuals, elders.",
  "Include animals (cows, goats, birds, elephants) where relevant.",
  "Rural and semi-urban Indian settings — villages, fields, markets, community spaces, schools, health centers.",
  "No white/Western people. No luxury or upper-class settings.",
  "Inclusive, democratic, warm. Community-centered compositions.",
  "Flat illustration style with clean outlines, minimal gradients.",
].join(" ");

// ─── Footer config ──────────────────────────────────────────────────────────

const HEADER_FOOTER = {
  bottomLeft: {
    type: "cardNumber",
  },
  bottomCenter: {
    type: "text",
    value: "impactmojo.in",
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
  "3-N. CONTENT SECTIONS — Each major topic gets:",
  "   - A SECTION SEPARATOR CARD with the section number, title, and a relevant folk art illustration (full-bleed)",
  "   - 2-5 content cards for that section with text, diagrams, charts, or illustrations",
  "SECOND-TO-LAST CARD: Key Takeaways — bullet summary of core learnings",
  "LAST CARD: Thank You — 'Thank You for Learning with ImpactMojo' with contact email: hello@impactmojo.in and link to impactmojo.in. Suggest 2-3 related courses to explore next.",
  "",
  "DIAGRAMS & CHARTS: Use plenty of diagrams, flowcharts, comparison tables, process flows, frameworks, and data visualizations.",
  "Make charts beautiful, colorful, and non-boring — use creative layouts like radial diagrams, Sankey flows, pyramid charts, matrix grids.",
  "Every section should have at least one visual framework, diagram, or chart. Never have 3+ text-only slides in a row.",
  "",
  "SECTION SEPARATORS: Use bold, visually distinct separator cards between major sections. Full-width background color or illustration. Section number + title only, no body text.",
  "",
  "LAYOUT: Clean layouts with generous whitespace. Use card-based sections.",
  "DIVERSITY: All human illustrations must show South Asian / brown-skinned people.",
  "IMAGERY: Prefer line-art SVG style illustrations over photographs. Indian folk art motifs.",
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

function apiRequest(method, apiPath, body) {
  const url = API_BASE + apiPath;
  const curlArgs = [
    "curl", "-s", "-w", "'\\n%{http_code}'",
    "-X", method,
    "-H", `'X-API-KEY: ${API_KEY}'`,
    "-H", "'Content-Type: application/json'",
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
  return Promise.resolve({ status: statusCode, data });
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
    "Then 6-8 MAJOR SECTIONS, each with:",
    "  - A bold SECTION SEPARATOR card (section number + title, full visual, no body text)",
    "  - 2-5 content cards covering concepts, frameworks, examples, diagrams",
    "  - Use examples from India, Bangladesh, Nepal, Sri Lanka, Pakistan",
    "  - Include at least one diagram, chart, framework visual, or comparison table per section",
    "  - Use flowcharts, process diagrams, matrix grids, radial charts, pyramid models — make them beautiful and non-boring",
    "",
    "Then closing cards:",
    "  - KEY TAKEAWAYS — Bullet summary of core learnings",
    "  - FURTHER READING — Books, papers, and resources",
    "  - THANK YOU — 'Thank You for Learning with ImpactMojo' / hello@impactmojo.in / impactmojo.in / suggest 2-3 related ImpactMojo 101 courses to explore next",
  ].join("\n");

  const imageStyle = `${artStyle}. ${IMAGE_STYLE_BASE}`;

  return {
    inputText,
    textMode: "generate",
    format: "presentation",
    numCards: 45,
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

  while (Date.now() - startTime < POLL_TIMEOUT) {
    await sleep(POLL_INTERVAL);
    const res = await apiRequest("GET", `/generations/${generationId}`);

    if (res.status !== 200) {
      console.error(`  Poll error (${res.status}):`, JSON.stringify(res.data));
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

  if (!API_KEY) {
    console.error("Error: GAMMA_API_KEY environment variable not set");
    process.exit(1);
  }

  let courses = COURSES;
  if (singleSlug) {
    courses = COURSES.filter((c) => c.slug === singleSlug);
    if (courses.length === 0) {
      console.error(`No course found with slug: ${singleSlug}`);
      console.error("Available slugs:", COURSES.map((c) => c.slug).join(", "));
      process.exit(1);
    }
  }

  console.log(`\n🎓 ImpactMojo Gamma Sync`);
  console.log(`   Courses: ${courses.length}`);
  console.log(`   Theme: ${THEME_ID}`);
  console.log(`   Folder: ${FOLDER_ID} (101 Decks)`);
  console.log(`   Mode: ${dryRun ? "DRY RUN" : "LIVE"}\n`);

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

  // Write results to file
  if (!dryRun && completed.length > 0) {
    const outputPath = path.join(__dirname, "..", "data", "gamma-sync-results.json");
    const outputDir = path.dirname(outputPath);
    if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

    fs.writeFileSync(
      outputPath,
      JSON.stringify(
        {
          syncDate: new Date().toISOString(),
          theme: THEME_ID,
          results,
        },
        null,
        2
      )
    );
    console.log(`\nResults saved to: ${outputPath}`);
  }
}

main().catch((err) => {
  console.error("Fatal error:", err);
  process.exit(1);
});
