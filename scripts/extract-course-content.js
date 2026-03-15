#!/usr/bin/env node
/**
 * extract-course-content.js
 *
 * One-time migration script that extracts module content from static
 * course HTML files and outputs JSON ready for Supabase insertion.
 *
 * Usage:
 *   node scripts/extract-course-content.js
 *
 * Output:
 *   scripts/course-content-seed.json  — array of rows for course_content table
 *
 * After running, insert into Supabase via the SQL Editor or REST API:
 *   1. Go to Supabase Dashboard → Table Editor → course_content
 *   2. Import the JSON, or
 *   3. Use the Supabase client with service role key
 */

const fs = require('fs');
const path = require('path');

const COURSES_DIR = path.join(__dirname, '..', 'courses');

const COURSE_IDS = [
  'gandhi', 'dataviz', 'devecon', 'mel',
  'media', 'law', 'poa', 'devai', 'SEL',
];

function extractModules(courseId) {
  const htmlPath = path.join(COURSES_DIR, courseId, 'index.html');
  if (!fs.existsSync(htmlPath)) {
    console.warn(`  [SKIP] ${htmlPath} not found`);
    return [];
  }

  const html = fs.readFileSync(htmlPath, 'utf8');
  const modules = [];

  // Match each <section ... id="moduleN" ...> ... up to next module or end
  // Attribute order varies: some have id before class, some after, some include "reveal"
  // Strategy: find all module start positions, then slice between them
  const moduleStartRegex = /<section\s+[^>]*?id="module(\d+)"[^>]*>/gi;
  const starts = [];
  let m;
  while ((m = moduleStartRegex.exec(html)) !== null) {
    starts.push({ index: m.index, num: parseInt(m[1], 10), tagEnd: m.index + m[0].length });
  }

  for (let si = 0; si < starts.length; si++) {
    const start = starts[si];
    const nextStart = starts[si + 1] ? starts[si + 1].index : html.length;
    // Extract from after the opening tag to just before the next module (or EOF)
    const raw = html.substring(start.tagEnd, nextStart);
    // Remove trailing </section> if present
    const moduleHtml = raw.replace(/<\/section>\s*$/, '').trim();
    const moduleNum = start.num;

    // Extract module title from section-header h2
    const titleMatch = moduleHtml.match(/<h2>([\s\S]*?)<\/h2>/i);
    const title = titleMatch
      ? titleMatch[1].replace(/<[^>]+>/g, '').trim()
      : `Module ${moduleNum}`;

    // Extract module intro from section-intro paragraph
    const introMatch = moduleHtml.match(/<p\s+class="section-intro">([\s\S]*?)<\/p>/i);
    const intro = introMatch
      ? introMatch[1].replace(/<[^>]+>/g, '').trim()
      : '';

    // Split content from quiz
    // Quiz sections typically start with <div class="quiz-section">
    const quizSplit = moduleHtml.split(/(<div\s+class="quiz-section">)/i);
    let contentHtml, quizHtml;

    if (quizSplit.length > 1) {
      contentHtml = quizSplit[0];
      quizHtml = quizSplit.slice(1).join('');

      // Close the section tag if needed
      if (!quizHtml.includes('</section>')) {
        // Quiz HTML may not have the closing section tag
      }
    } else {
      contentHtml = moduleHtml;
      quizHtml = '';
    }

    // Clean up: remove the section-header since we store title/intro separately
    contentHtml = contentHtml.replace(
      /<div\s+class="section-header">[\s\S]*?<\/div>\s*<\/div>/i,
      ''
    ).trim();

    modules.push({
      course_id: courseId,
      module_number: moduleNum,
      module_title: title,
      module_intro: intro,
      content_html: contentHtml,
      quiz_html: quizHtml || null,
      is_preview: moduleNum === 1,  // Module 1 is always free preview
    });
  }

  return modules;
}

// ── Main ────────────────────────────────────────────────────────
console.log('Extracting course content from HTML files...\n');

const allContent = [];

for (const courseId of COURSE_IDS) {
  console.log(`Processing: ${courseId}`);
  const modules = extractModules(courseId);
  console.log(`  Extracted ${modules.length} modules`);
  allContent.push(...modules);
}

console.log(`\nTotal modules extracted: ${allContent.length}`);

// Write to JSON file
const outputPath = path.join(__dirname, 'course-content-seed.json');
fs.writeFileSync(outputPath, JSON.stringify(allContent, null, 2));
console.log(`\nSeed data written to: ${outputPath}`);

// Also generate a SQL insert script
const sqlPath = path.join(__dirname, 'seed-course-content.sql');
let sql = '-- Auto-generated seed script for course_content table\n';
sql += '-- Run this in Supabase SQL Editor after creating the table\n\n';

for (const row of allContent) {
  const esc = (s) => s ? s.replace(/'/g, "''") : '';
  sql += `INSERT INTO public.course_content (course_id, module_number, module_title, module_intro, content_html, quiz_html, is_preview)\n`;
  sql += `VALUES ('${esc(row.course_id)}', ${row.module_number}, '${esc(row.module_title)}', '${esc(row.module_intro)}', '${esc(row.content_html)}', ${row.quiz_html ? `'${esc(row.quiz_html)}'` : 'NULL'}, ${row.is_preview})\n`;
  sql += `ON CONFLICT (course_id, module_number) DO UPDATE SET\n`;
  sql += `  module_title = EXCLUDED.module_title,\n`;
  sql += `  module_intro = EXCLUDED.module_intro,\n`;
  sql += `  content_html = EXCLUDED.content_html,\n`;
  sql += `  quiz_html = EXCLUDED.quiz_html,\n`;
  sql += `  is_preview = EXCLUDED.is_preview;\n\n`;
}

fs.writeFileSync(sqlPath, sql);
console.log(`SQL seed script written to: ${sqlPath}`);
console.log('\nNext steps:');
console.log('  1. Run the migration:  supabase/migrations/20260315_course_content.sql');
console.log('  2. Seed the data:      scripts/seed-course-content.sql');
console.log('  3. Deploy edge fn:     supabase functions deploy serve-course-content');
console.log('  4. Convert HTML files to dynamic shells (remove inline content)');
