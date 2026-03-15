#!/usr/bin/env node
/**
 * convert-to-shells.js
 *
 * Converts course HTML files from static content to dynamic shells.
 * Replaces each module's inline content with a placeholder div that
 * course-loader.js will populate from the Supabase edge function.
 *
 * What it preserves:
 *   - All <head> content (meta, styles, fonts)
 *   - Sidebar navigation
 *   - Hero/intro sections (before module 1)
 *   - Module section headers (number, title, intro)
 *   - Footer, scripts
 *   - checkAnswer() function and quiz CSS
 *
 * What it replaces:
 *   - Everything between section-header and the next module/footer
 *     becomes <div id="moduleN-content" class="module-content-placeholder"></div>
 *
 * Usage:
 *   node scripts/convert-to-shells.js
 *
 * This modifies files in-place. Run extract-course-content.js FIRST
 * to ensure content is backed up in the seed files.
 */

const fs = require('fs');
const path = require('path');

const COURSES_DIR = path.join(__dirname, '..', 'courses');

const COURSE_IDS = [
  'gandhi', 'dataviz', 'devecon', 'mel',
  'media', 'law', 'poa', 'devai', 'SEL',
];

function convertToShell(courseId) {
  const htmlPath = path.join(COURSES_DIR, courseId, 'index.html');
  if (!fs.existsSync(htmlPath)) {
    console.warn(`  [SKIP] ${htmlPath} not found`);
    return false;
  }

  let html = fs.readFileSync(htmlPath, 'utf8');

  // Find all module section starts
  const moduleStartRegex = /<section\s+[^>]*?id="module(\d+)"[^>]*>/gi;
  const starts = [];
  let m;
  while ((m = moduleStartRegex.exec(html)) !== null) {
    starts.push({
      index: m.index,
      num: parseInt(m[1], 10),
      tag: m[0],
      tagEnd: m.index + m[0].length,
    });
  }

  if (starts.length === 0) {
    console.warn(`  [SKIP] No modules found in ${courseId}`);
    return false;
  }

  // Process modules in reverse order so indices stay valid
  for (let si = starts.length - 1; si >= 0; si--) {
    const start = starts[si];
    const nextStart = starts[si + 1] ? starts[si + 1].index : null;

    // Find the closing </section> for this module
    // Look for </section> before the next module start (or end of file)
    const searchEnd = nextStart || html.length;
    const moduleBody = html.substring(start.tagEnd, searchEnd);

    // Find the section-header end to preserve it
    const headerMatch = moduleBody.match(/<div\s+class="section-header">([\s\S]*?)<\/div>\s*<\/div>/i);

    let sectionHeaderHtml = '';
    let headerEndOffset = 0;

    if (headerMatch) {
      // Reconstruct section header with title and intro
      sectionHeaderHtml = `<div class="section-header">${headerMatch[0].match(/<div class="section-header">([\s\S]*)/i)[1]}`;
      // Actually, just keep the matched block as-is
      sectionHeaderHtml = headerMatch[0];
      headerEndOffset = headerMatch.index + headerMatch[0].length;
    }

    // Find closing </section> tag
    const closingSectionIdx = moduleBody.lastIndexOf('</section>');
    const hasClosingSection = closingSectionIdx !== -1;

    // Build the replacement: section tag + header + placeholder + closing
    const placeholder = `\n                    <div id="module${start.num}-content" class="module-content-placeholder">\n                        <!-- Content loaded dynamically by course-loader.js -->\n                    </div>\n                `;

    const replacement = start.tag + '\n                    ' +
      sectionHeaderHtml + '\n' +
      placeholder +
      (hasClosingSection ? '\n                </section>\n' : '');

    // Replace from module start to just before next module (or end of section)
    const replaceEnd = nextStart || (start.tagEnd + (hasClosingSection ? closingSectionIdx + '</section>'.length : moduleBody.length));
    html = html.substring(0, start.index) + replacement + html.substring(replaceEnd);
  }

  // Add course-loader.js script reference (before course-progress.js)
  if (!html.includes('course-loader.js')) {
    html = html.replace(
      /(<script[^>]*src="[^"]*course-progress\.js"[^>]*><\/script>)/i,
      '<script defer src="../../js/course-loader.js"></script>\n$1'
    );

    // Fallback: if course-progress.js uses /js/ path
    if (!html.includes('course-loader.js')) {
      html = html.replace(
        /(<script[^>]*src="[^"]*course-progress\.js"[^>]*><\/script>)/i,
        '<script defer src="/js/course-loader.js"></script>\n$1'
      );
    }
  }

  // Write the modified file
  fs.writeFileSync(htmlPath, html);
  return true;
}

// ── Main ────────────────────────────────────────────────────────
console.log('Converting course HTML files to dynamic shells...\n');

let converted = 0;
for (const courseId of COURSE_IDS) {
  console.log(`Processing: ${courseId}`);
  if (convertToShell(courseId)) {
    converted++;
    console.log(`  ✓ Converted`);
  }
}

console.log(`\nDone. Converted ${converted}/${COURSE_IDS.length} courses.`);
console.log('\nEach module section now contains:');
console.log('  <div id="moduleN-content" class="module-content-placeholder">');
console.log('    <!-- Content loaded dynamically by course-loader.js -->');
console.log('  </div>');
