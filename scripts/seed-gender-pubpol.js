#!/usr/bin/env node
/**
 * Extract module content from gender and pubpol courses,
 * then seed it into Supabase via the REST API.
 *
 * Usage: SUPABASE_SERVICE_KEY=... node scripts/seed-gender-pubpol.js
 *
 * Also outputs scripts/gender-pubpol-seed.json for reference.
 */

const fs = require('fs');
const path = require('path');

const SUPABASE_URL = 'https://ddyszmfffyedolkcugld.supabase.co';
const SERVICE_KEY = process.env.SUPABASE_SERVICE_KEY || process.env.SUPABASE_PAT;

if (!SERVICE_KEY) {
  console.error('ERROR: Set SUPABASE_SERVICE_KEY or SUPABASE_PAT env var');
  process.exit(1);
}

const COURSES = [
  { id: 'gender', file: 'courses/gender/index.html', sectionClass: 'module' },
  { id: 'pubpol', file: 'courses/pubpol/index.html', sectionClass: 'section reveal' },
];

function extractModules(courseId, htmlPath, sectionClass) {
  const html = fs.readFileSync(path.join(__dirname, '..', htmlPath), 'utf8');
  const modules = [];

  // Find all module sections
  const moduleRegex = new RegExp(
    `<section\\s+class="${sectionClass.replace(/\s+/g, '\\s+')}"\\s+id="module(\\d+)"[^>]*>`,
    'gi'
  );

  // Also handle reversed attribute order (id before class)
  const moduleRegex2 = new RegExp(
    `<section\\s+id="module(\\d+)"\\s+class="${sectionClass.replace(/\s+/g, '\\s+')}"[^>]*>`,
    'gi'
  );

  const starts = [];
  let m;
  while ((m = moduleRegex.exec(html)) !== null) {
    starts.push({ index: m.index, num: parseInt(m[1], 10), tagEnd: m.index + m[0].length });
  }
  while ((m = moduleRegex2.exec(html)) !== null) {
    // Avoid duplicates
    if (!starts.find(s => s.num === parseInt(m[1], 10))) {
      starts.push({ index: m.index, num: parseInt(m[1], 10), tagEnd: m.index + m[0].length });
    }
  }
  starts.sort((a, b) => a.index - b.index);

  for (let si = 0; si < starts.length; si++) {
    const start = starts[si];
    const nextStart = starts[si + 1] ? starts[si + 1].index : html.length;
    const raw = html.substring(start.tagEnd, nextStart);
    const moduleHtml = raw.replace(/<\/section>\s*$/m, '').trim();
    const moduleNum = start.num;

    // Extract title from h2 (with or without class attribute)
    const titleMatch = moduleHtml.match(/<h2[^>]*>([\s\S]*?)<\/h2>/i);
    const title = titleMatch
      ? titleMatch[1].replace(/<[^>]+>/g, '').trim()
      : `Module ${moduleNum}`;

    // Extract intro - try module-tag span's sibling p, or section-intro
    const introMatch = moduleHtml.match(/<p\s+class="(?:section-intro|module-intro)">([\s\S]*?)<\/p>/i);
    const intro = introMatch
      ? introMatch[1].replace(/<[^>]+>/g, '').trim()
      : '';

    // For gender: content is inside <div class="module-content">...</div>
    // For pubpol: content is directly inside the section (after section-header)
    let contentHtml = moduleHtml;

    // Remove the header block
    // Gender: module-header div
    contentHtml = contentHtml.replace(
      /<div\s+class="module-header">[\s\S]*?<\/div>\s*<\/div>/i,
      ''
    );
    // Pubpol: section-header div
    contentHtml = contentHtml.replace(
      /<div\s+class="section-header">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/i,
      ''
    );

    // Split content from quiz (MCQ section)
    let quizHtml = null;
    const mcqSplitIdx = contentHtml.indexOf('<div class="mcq-section">');
    const quizSplitIdx = contentHtml.indexOf('<div class="quiz-section">');
    const splitIdx = mcqSplitIdx >= 0 ? mcqSplitIdx : quizSplitIdx;

    if (splitIdx >= 0) {
      quizHtml = contentHtml.substring(splitIdx);
      contentHtml = contentHtml.substring(0, splitIdx);
    }

    contentHtml = contentHtml.trim();
    if (quizHtml) quizHtml = quizHtml.trim();

    modules.push({
      course_id: courseId,
      module_number: moduleNum,
      module_title: title,
      module_intro: intro,
      content_html: contentHtml,
      quiz_html: quizHtml,
      is_preview: moduleNum === 1,
    });
  }

  return modules;
}

async function seedToSupabase(rows) {
  const url = `${SUPABASE_URL}/rest/v1/course_content`;

  for (const row of rows) {
    console.log(`  Seeding ${row.course_id} module ${row.module_number}: ${row.module_title}`);

    // Upsert using Prefer: resolution=merge-duplicates
    const res = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'apikey': SERVICE_KEY,
        'Authorization': `Bearer ${SERVICE_KEY}`,
        'Prefer': 'resolution=merge-duplicates',
      },
      body: JSON.stringify(row),
    });

    if (!res.ok) {
      const body = await res.text();
      console.error(`  ERROR ${res.status}: ${body}`);
    }
  }
}

async function main() {
  const allRows = [];

  for (const course of COURSES) {
    console.log(`\nExtracting: ${course.id}`);
    const modules = extractModules(course.id, course.file, course.sectionClass);
    console.log(`  Found ${modules.length} modules`);

    // Verify content looks right
    for (const mod of modules) {
      const contentLen = (mod.content_html || '').length;
      const quizLen = (mod.quiz_html || '').length;
      console.log(`  M${mod.module_number} "${mod.module_title}" — content: ${contentLen} chars, quiz: ${quizLen} chars`);
    }

    allRows.push(...modules);
  }

  // Save JSON for reference
  const jsonPath = path.join(__dirname, 'gender-pubpol-seed.json');
  fs.writeFileSync(jsonPath, JSON.stringify(allRows, null, 2));
  console.log(`\nSaved ${allRows.length} rows to ${jsonPath}`);

  // Seed to Supabase
  console.log('\nSeeding to Supabase...');
  await seedToSupabase(allRows);
  console.log('\nDone!');
}

main().catch(console.error);
