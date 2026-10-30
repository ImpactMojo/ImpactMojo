/**
 * ImpactMojo Site Chrome — one standard thin top bar + footer for every page.
 * Version 2.0.0 — October 2026
 *
 * Drop-in: add <script src="/js/site-chrome.js" defer></script> to any page.
 * The script (1) removes whatever legacy top bar / footer the page already has,
 * (2) injects the standard thin top bar and standard footer, and (3) wires the
 * theme buttons to the same contract as theme.js (it writes every theme key the
 * site reads, and sets data-theme on <html> plus the body mode class).
 * All future chrome changes happen in this one file.
 *
 * Top bar (left to right): logo (home) · "Section › Page" breadcrumb · [spacer] ·
 *   Search · Language · Membership · About · reading font (Aa) · theme ·
 *   Home · Log in / My account · Menu.
 * The Menu button opens the footer's link columns as a side sheet, so the
 * site's sections are one tap away from every page, not 30,000px down.
 * Footer: link columns (Learn, Explore, ImpactMojo, Help & legal) + licence line.
 *
 * Also on every page (homepage included): the WhatsApp share button, one slot
 * manager that stacks every floating button bottom-right without overlap, and
 * an analytics-cookie notice on pages that do not carry their own.
 *
 * Opt out (homepage only): put data-im-home on <html> or <body>, or set
 *   <meta name="im-chrome" content="off">.
 * Page name: from <meta name="im-page" content="…"> if present, else derived
 *   from <title> (text before the first | or —), else the <h1>, else the path.
 *
 * Layout shift: the bar is inserted after first paint, because this script is
 * deferred. A page that wants no shift links /css/site-chrome.css in <head>,
 * which reserves the bar's 46px before this script runs (see that file).
 */
(function () {
  'use strict';
  if (window.__imChrome) return;
  window.__imChrome = true;

  var root = document.documentElement;
  var meta = function (n) { var m = document.querySelector('meta[name="' + n + '"]'); return m && m.getAttribute('content'); };
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  // ── Analytics consent, as early as this script runs ────────────────
  // gtag is defined inline in <head> on ~1,000 pages and loads with no consent
  // signal. Until the reader chooses, analytics storage is denied. A deferred
  // script cannot run before the page's own gtag('config'), so pages that want
  // the default applied to the first hit need it in their head snippet too.
  var CONSENT_KEY = 'im-analytics-consent';
  function consentChoice() {
    var v = store(CONSENT_KEY);
    if (v === 'granted' || v === 'denied') return v;
    // The homepage's older widget stored only an acceptance, under its own key.
    return store('cookieConsent') === 'true' ? 'granted' : null;
  }
  (function consentDefault() {
    if (typeof window.gtag !== 'function') return;
    var c = consentChoice();
    try {
      if (c) window.gtag('consent', 'update', { analytics_storage: c });
      else window.gtag('consent', 'default', { analytics_storage: 'denied' });
    } catch (e) {}
  })();

  // ── Reading font (OpenDyslexic) ────────────────────────────────────
  // Applied here, at script execution, rather than inside boot(): a reader who
  // has chosen the font should not watch each page render in Inter first. The
  // rules and the four @font-face declarations live in /css/fonts.css, which
  // downloads nothing until this class is present.
  var DYS_KEY = 'im-reading-font';
  function dysOn() { return store(DYS_KEY) === 'opendyslexic'; }
  if (dysOn()) root.classList.add('im-dyslexic');

  // ── Accessibility choices ──────────────────────────────────────────
  // The header's Accessibility menu stores these together and they are put on
  // <html> here, before the page paints, the same way as the reading font:
  // text size (zoom on <body>, so pages set in px grow too), wider spacing,
  // underlined links, reduced motion and a stronger focus outline. They replace
  // the third-party UserWay widget, which loaded on about 50 pages and on none
  // of the rest.
  var A11Y_KEY = 'im-a11y';
  var A11Y_FLAGS = ['spacing', 'links', 'motion', 'focus'];
  function a11yGet() { try { var v = JSON.parse(store(A11Y_KEY) || '{}'); return v && typeof v === 'object' ? v : {}; } catch (e) { return {}; } }
  function a11yApply(v) {
    root.classList.remove('im-a11y-text-1', 'im-a11y-text-2');
    if (v.text === 1 || v.text === 2) root.classList.add('im-a11y-text-' + v.text);
    A11Y_FLAGS.forEach(function (k) { root.classList.toggle('im-a11y-' + k, !!v[k]); });
  }
  a11yApply(a11yGet());

  // ── Opt-out (homepage) ─────────────────────────────────────────────
  var path = location.pathname.replace(/index\.html$/, '');
  var lpath = path.toLowerCase(); // Netlify lowercases paths, so match case-insensitively
  // Pages that keep their own chrome opt out with data-im-home or
  // <meta name="im-chrome" content="off">. The homepage itself takes the bar,
  // so every page has the same header. The WhatsApp button, the floating-button
  // slots and the consent notice (below) run on every page either way.
  var isHome = root.hasAttribute('data-im-home') || (document.body && document.body.hasAttribute('data-im-home'))
    || meta('im-chrome') === 'off';
  var isFront = path === '/' || path === '';

  // 101 decks: the slide pager, notes button and theme pill fill the bottom of
  // the screen, and the WhatsApp button covered them. Index, poster and practice
  // pages live elsewhere in the folder and are ordinary pages.
  // A 101 deck, at /101-courses/<slug>.html or /101-courses/native/<slug>.html,
  // with or without .html (Netlify serves both); never the series index.
  var isDeck = /^\/101-courses\/(native\/)?(?!index(\.html)?$)[^/]+$/i.test(location.pathname);

  // ── Page name for the breadcrumb ───────────────────────────────────
  function pageName() {
    var m = meta('im-page'); if (m) return m;
    var t = (document.title || '').split(/[|—–]/)[0].trim();
    if (t && t.length <= 60) return t;
    var h1 = document.querySelector('h1'); if (h1 && h1.textContent.trim()) return h1.textContent.trim().slice(0, 48);
    var seg = path.split('/').filter(Boolean).pop() || '';
    return seg.replace(/[-_]/g, ' ').replace(/\.html$/, '').replace(/\b\w/g, function (c) { return c.toUpperCase(); }) || 'Page';
  }
  var SITE = ''; // root-relative so links work from any page depth and on any host

  // ── Sections, for the breadcrumb ───────────────────────────────────
  // [path prefix (lower case), section name, section hub]. First match wins, so
  // keep longer prefixes above shorter ones that share a start.
  var SECTIONS = [
    ['/labs/', 'Free Studio', '/Labs/'],
    ['/premium-tools/', 'Pro Studio', '/premium-tools/'],
    ['/practice-packs/', 'Practice Packs', '/practice-packs/'],
    ['/101-courses/', '101 Series', '/101-courses/'],
    ['/courses/', 'Flagship courses', '/courses/'],
    ['/code/', 'Code School', '/code/'],
    ['/booksummaries/', 'Reading Companions', '/BookSummaries/'],
    ['/bookcompaniontools/', 'Reading Companions', '/BookSummaries/'],
    ['/deepdives/', 'Deep Dives', '/DeepDives/'],
    ['/games/', 'Simulations', '/Games/'],
    ['/handouts/', 'Handouts', '/handouts.html'],
    ['/datanotes/', 'Data Notes', '/DataNotes/'],
    ['/fundamentals/', 'Fundamentals', '/fundamentals/'],
    ['/theories/', 'Theories', '/theories/'],
    ['/law-guides/', 'Law guides', '/law-guides/'],
    ['/blog/', 'Blog', '/blog.html'],
    ['/facilitator-kits/', 'Facilitator Kits', '/facilitator-kits/'],
    ['/community/', 'Community', '/community/'],
    ['/products/', 'Products', '/products.html'],
    ['/impactlex/', 'ImpactLex', '/impactlex/'],
    ['/timelines/', 'Timelines', '/timelines/'],
    ['/maps/', 'Maps', '/maps/'],
    ['/research-to-action/', 'Research to Action', '/research-to-action/']
  ];
  // The Data Room explorers sit at the site root, so they are listed by name
  // (the set linked from explorers.html).
  var EXPLORERS = ['aishe', 'aqi', 'aser', 'castes', 'cities', 'crime', 'csr', 'eci', 'energy', 'fiscal', 'hpi',
    'ihds', 'justice', 'mgnrega', 'migration', 'nas', 'nfhs-state', 'nfhs', 'nhts', 'plfs', 'scheme-tracker', 'udise'];
  function section() {
    for (var i = 0; i < SECTIONS.length; i++) {
      if (lpath.indexOf(SECTIONS[i][0]) === 0) {
        var hub = SECTIONS[i][2].toLowerCase().replace(/index\.html$/, '');
        return { name: SECTIONS[i][1], href: SECTIONS[i][2], isHub: lpath === hub };
      }
    }
    var m = lpath.match(/^\/([a-z0-9-]+)\.html$/);
    if (m && EXPLORERS.indexOf(m[1]) !== -1) return { name: 'Data Room', href: '/explorers.html', isHub: false };
    return null;
  }

  // ── "Recently updated" dots ────────────────────────────────────────
  // scripts/stamp-nav-dots.py writes the dots into the homepage's own nav. The
  // bar replaces that nav, so build() reads them first and keeps the list for
  // a week, and the Menu sheet marks the same links on every page.
  var FRESH_KEY = 'im-fresh-nav';
  function normHref(h) {
    return String(h || '').toLowerCase().replace(/^https?:\/\/[^/]+/, '').replace(/index\.html$/, '').replace(/\.html$/, '').replace(/\/$/, '');
  }
  function harvestFresh() {
    var dots = document.querySelectorAll('[title="Recently updated"]');
    if (!dots.length) return;
    var list = [];
    [].forEach.call(dots, function (d) { var a = d.closest('a'); if (a) list.push(normHref(a.getAttribute('href'))); });
    try { localStorage.setItem(FRESH_KEY, JSON.stringify({ t: Date.now(), l: list })); } catch (e) {}
  }
  function freshHrefs() {
    try {
      var v = JSON.parse(localStorage.getItem(FRESH_KEY) || 'null');
      if (v && Date.now() - v.t < 7 * 864e5) return v.l || [];
    } catch (e) {}
    return [];
  }

  // ── Site links ─────────────────────────────────────────────────────
  // MENU is the header: four groups and Membership, the grouping the owner
  // chose on 2026-10-14 in place of a 22-link list. NAV is the footer and the
  // phone Menu sheet, and holds everything MENU does plus the pages that left
  // the header (About, Impact, Testimonials, Contribute, Roadmap...).
  var MENU = [
    ['Learn', [
      ['/courses/', 'Flagship courses', '22 courses with several modules each'],
      ['/101-courses/', '101 Series', '84 short courses, each a slide deck'],
      ['/code/', 'Code School', 'R, Python and SQL in your browser'],
      ['/practice-packs/', 'Practice Packs', 'Worked exercises by topic'],
      ['/Games/', 'Simulations', 'Play out a policy or a programme'],
      ['/game-library.html', 'Game Library', 'Classroom games and activities']]],
    ['Tools', [
      ['/Labs/', 'Free Studio', 'Browser tools for the work itself'],
      ['/premium-tools/', 'Pro Studio', 'Research tools, exports with Membership'],
      ['/law-guides/', 'Law guides', 'Indian laws for the social sector'],
      ['/libraries.html', 'Libraries', 'Every collection in one place']]],
    ['Data', [
      ['/explorers.html', 'Data Room', 'Explorers built on official data'],
      ['/by-the-numbers/', 'By the numbers', 'One figure at a time, with the working'],
      ['/dataverse.html', 'Dataverse', 'Data sources, listed and described']]],
    ['Read', [
      ['/BookSummaries/', 'Reading Companions', 'Companions to key books'],
      ['/DeepDives/', 'Deep Dives', 'Curated readings on one question'],
      ['/handouts.html', 'Handouts', 'Printable notes by track'],
      ['/blog.html', 'Blog', 'Essays and updates']]],
    ['Membership', [
      ['/premium.html', 'Plans', 'What Membership adds'],
      ['/walkthrough.html', 'Site walkthrough', 'A slide tour of the whole site'],
      ['/catalog.html', 'Catalogue', 'Everything on the site, filterable'],
      ['/updates#whats-new', 'What&rsquo;s new', 'Recent additions and changes']]]
  ];
  var NAV = [
    ['Learn', [
      ['/courses/', 'Flagship courses'], ['/101-courses/', '101 Series'], ['/code/', 'Code School'],
      ['/practice-packs/', 'Practice Packs'], ['/Games/', 'Simulations'], ['/game-library.html', 'Game Library'],
      ['/teach.html', 'Teach with ImpactMojo'], ['/facilitator-kits/', 'Facilitator Kits'],
      ['/teaching-principles.html', 'Teaching Principles']]],
    ['Tools', [
      ['/Labs/', 'Free Studio'], ['/premium-tools/', 'Pro Studio'], ['/law-guides/', 'Law guides'],
      ['/law-guides/development-law-docket.html', 'Law Docket'], ['/libraries.html', 'Libraries'], ['/products.html', 'Products']]],
    ['Data', [
      ['/explorers.html', 'Data Room'], ['/by-the-numbers/', 'By the numbers'], ['/dataverse.html', 'Dataverse'], ['/fundamentals/', 'Fundamentals'],
      ['/field-radio.html', 'Field Radio']]],
    ['Read', [
      ['/BookSummaries/', 'Reading Companions'], ['/DeepDives/', 'Deep Dives'], ['/handouts.html', 'Handouts'],
      ['/blog.html', 'Blog'], ['/dojos.html', 'Dojos &amp; Practice']]],
    ['ImpactMojo', [
      ['/about.html', 'About'], ['/walkthrough.html', 'Site walkthrough'], ['/premium.html', 'Membership'], ['/catalog.html', 'Full catalogue'],
      ['/updates#whats-new', 'What&rsquo;s new'], ['/impact-dashboard.html', 'Impact'], ['/testimonials.html', 'Testimonials'],
      ['/updates#roadmap', 'Roadmap'], ['/community/', 'Community'], ['/partnerships.html', 'Partnerships'],
      ['/contribute.html', 'Contribute'], ['/support.html', 'Support us'], ['/transparency.html', 'Transparency'], ['/known-issues.html', 'Known issues'],
      ['https://github.com/ImpactMojo/ImpactMojo', 'GitHub']]],
    ['Help &amp; legal', [
      ['/contact.html', 'Contact'], ['/faq.html', 'FAQ'], ['/sitemap.html', 'Sitemap'],
      ['/verify-certificate.html', 'Verify a certificate'], ['/privacy-policy.html', 'Privacy'],
      ['/terms-of-service.html', 'Terms'], ['/refund-policy.html', 'Refunds'], ['/accessibility.html', 'Accessibility'],
      ['/disclaimer.html', 'Disclaimer'], ['/grievance.html', 'Grievance'], ['/data-protection.html', 'Data protection'],
      ['/ai-policy.html', 'AI policy']]]
  ];
  // grid: wrap each column's links in a <div> (the sheet lays them out in two
  // columns; the footer lists them straight).
  function navCols(colClass, grid) {
    return NAV.map(function (col) {
      var links = col[1].map(function (l) {
        var href = /^https?:/.test(l[0]) ? l[0] : SITE + l[0];
        var dot = grid && freshHrefs().indexOf(normHref(l[0])) !== -1
          ? '<span class="im-sc-dot" title="Recently updated" aria-label="Recently updated"></span>' : '';
        return '<a href="' + href + '">' + l[1] + dot + '</a>';
      }).join('');
      return '<div class="' + colClass + '"><h3>' + col[0] + '</h3>' + (grid ? '<div>' + links + '</div>' : links) + '</div>';
    }).join('');
  }
  // The phone Menu sheet. SHEET holds every link in NAV, regrouped so that
  // no screen of the sheet lists more than six rows: a row is either a link
  // ([href, label]) or a section ([label, [rows]]) that opens a screen of its
  // own with a Back button. A link's third item is the line under it, used
  // where MENU has no description. When a link is added to NAV, add it here
  // too, with its line.
  var SHEET = [
    ['Learn', [
      ['Courses', [['/courses/', 'Flagship courses'], ['/101-courses/', '101 Series'], ['/code/', 'Code School'], ['/practice-packs/', 'Practice Packs']]],
      ['Games', [['/Games/', 'Simulations'], ['/game-library.html', 'Game Library']]],
      ['Teaching', [['/teach.html', 'Teach with ImpactMojo', 'Run a course or workshop with our material'], ['/facilitator-kits/', 'Facilitator Kits', 'Workshop kits you can edit and run yourself'], ['/teaching-principles.html', 'Teaching Principles', 'How every course, Studio and game is designed']]]]],
    ['Tools', [
      ['Studios and products', [['/Labs/', 'Free Studio'], ['/premium-tools/', 'Pro Studio'], ['/products.html', 'Products', 'Everything you can buy, in one place']]],
      ['Law', [['/law-guides/', 'Law guides'], ['/law-guides/development-law-docket.html', 'Law Docket', 'Court judgments that changed development work']]],
      ['/libraries.html', 'Libraries']]],
    ['Data', [
      ['/explorers.html', 'Data Room'], ['/by-the-numbers/', 'By the numbers'], ['/dataverse.html', 'Dataverse'], ['/fundamentals/', 'Fundamentals', 'Development frameworks, made interactive'], ['/field-radio.html', 'Field Radio', 'Voice notes and videos from practitioners']]],
    ['Read', [
      ['/BookSummaries/', 'Reading Companions'], ['/DeepDives/', 'Deep Dives'], ['/handouts.html', 'Handouts'],
      ['/blog.html', 'Blog'], ['/dojos.html', 'Dojos &amp; Practice', '90-minute skill sessions, in person and online']]],
    ['ImpactMojo', [
      ['About us', [['/about.html', 'About', 'Who we are and why ImpactMojo exists'], ['/walkthrough.html', 'Site walkthrough', 'A slide tour of the whole site'], ['/impact-dashboard.html', 'Impact', 'What learners have done with what they learned'], ['/testimonials.html', 'Testimonials', 'What learners say about ImpactMojo'], ['/transparency.html', 'Transparency', 'Our numbers, methods and revenue'], ['/known-issues.html', 'Known issues', 'Every bug we know about, open and fixed']]],
      ['Membership and updates', [['/premium.html', 'Membership', 'What Membership adds'], ['/catalog.html', 'Full catalogue'], ['/updates#whats-new', 'What&rsquo;s new'], ['/updates#roadmap', 'Roadmap', 'What we are building next']]],
      ['Get involved', [['/community/', 'Community', 'Practitioners on WhatsApp and Discord'], ['/partnerships.html', 'Partnerships', 'Who we work with, and how to partner'], ['/contribute.html', 'Contribute', 'Propose a free course of your own'], ['/support.html', 'Support us', 'Pay what you can to keep the site free'], ['https://github.com/ImpactMojo/ImpactMojo', 'GitHub', 'The open-source code behind the site']]]]],
    ['Help &amp; legal', [
      ['Help', [['/contact.html', 'Contact', 'Questions about courses, workshops or partnerships'], ['/faq.html', 'FAQ', 'Answers on courses, certificates and accounts'], ['/verify-certificate.html', 'Verify a certificate', 'Check that a certificate number is real'], ['/accessibility.html', 'Accessibility', 'Our standard, and how to report a barrier'], ['/sitemap.html', 'Sitemap', 'Every page, in one filterable map']]],
      ['Privacy and data', [['/privacy-policy.html', 'Privacy', 'What we collect and how we use it'], ['/data-protection.html', 'Data protection', 'How we follow the DPDP Act, 2023'], ['/ai-policy.html', 'AI policy', 'How we use AI in courses and tools']]],
      ['Terms and complaints', [['/terms-of-service.html', 'Terms', 'Your rights and ours when you use the site'], ['/refund-policy.html', 'Refunds', 'Refunds and cancellations for paid services'], ['/disclaimer.html', 'Disclaimer', 'What our educational content is, and is not'], ['/grievance.html', 'Grievance', 'Raise a complaint or concern']]]]]
  ];
  function isSection(r) { return Array.isArray(r[1]); }
  // Panes for the sheet: 'root', then one per section, keyed by its path
  // ('0', '0-1'). Descriptions come from MENU where the header has one.
  function sheetPanes() {
    var desc = {};
    MENU.forEach(function (g) { g[1].forEach(function (l) { desc[normHref(l[0])] = l[2]; }); });
    var fresh = freshHrefs(), here = normHref(location.pathname);
    var panes = [];
    function names(rows) { return rows.map(function (r) { return isSection(r) ? r[0] : r[1]; }); }
    function hint(rows) {
      var n = names(rows);
      // Up to four names in full; past that, three and a count, never "and 1 more".
      return n.length <= 4 ? n.join(', ') : n.slice(0, 3).join(', ') + ' and ' + (n.length - 3) + ' more';
    }
    // Renders rows; returns {html, here, fresh} so a section row can say it
    // holds the current page or something recently updated.
    function render(rows, path) {
      var anyHere = false, anyFresh = false;
      var html = rows.map(function (r, i) {
        if (isSection(r)) {
          var id = path ? path + '-' + i : String(i);
          var sub = pane(r[0], r[1], id, path || 'root', path ? paneTitle[path] : 'Menu');
          anyHere = anyHere || sub.here; anyFresh = anyFresh || sub.fresh;
          return '<li><button type="button" class="im-sc-row" data-open="' + id + '">' +
            '<span class="im-sc-row-tx"><span class="im-sc-row-t">' + r[0] +
              (sub.here ? '<span class="im-sc-row-here">This page</span>' : '') +
              (sub.fresh ? '<span class="im-sc-dot" title="Recently updated" aria-label="Recently updated"></span>' : '') +
            '</span><span class="im-sc-row-h">' + hint(r[1]) + '</span></span>' + I.next + '</button></li>';
        }
        var href = /^https?:/.test(r[0]) ? r[0] : SITE + r[0];
        var n = normHref(r[0]), isFresh = fresh.indexOf(n) !== -1;
        var cur = n && n !== '/' && here === normHref(r[0].split('#')[0]);
        anyHere = anyHere || cur; anyFresh = anyFresh || isFresh;
        var d = (r[2] || desc[n]) ? '<span class="im-sc-ld">' + (r[2] || desc[n]) + '</span>' : '';
        var dot = isFresh ? '<span class="im-sc-dot" title="Recently updated" aria-label="Recently updated"></span>' : '';
        return '<li><a href="' + href + '"' + (cur ? ' aria-current="page"' : '') + '><span class="im-sc-lt">' + r[1] + dot + '</span>' + d + '</a></li>';
      }).join('');
      return { html: html, here: anyHere, fresh: anyFresh };
    }
    var paneTitle = {};
    function pane(title, rows, id, parent, parentTitle) {
      paneTitle[id] = title;
      var out = render(rows, id);
      var list = rows.some(isSection) ? 'im-sc-rows' : 'im-sc-links';
      panes.push('<div class="im-sc-pane" data-pane="' + id + '" role="group" aria-labelledby="im-sc-pane-h' + id + '" hidden>' +
        '<button type="button" class="im-sc-back" data-back="' + parent + '">' + I.prev + parentTitle + '</button>' +
        '<h3 id="im-sc-pane-h' + id + '">' + title + '</h3><ul class="' + list + '">' + out.html + '</ul></div>');
      return out;
    }
    var root = render(SHEET, '');
    return { rows: '<ul class="im-sc-rows">' + root.html + '</ul>', panes: panes.join('') };
  }
  // The group the current page belongs to, so its heading can say so.
  function currentGroup() {
    var here = normHref(location.pathname);
    for (var i = 0; i < MENU.length; i++) {
      for (var j = 0; j < MENU[i][1].length; j++) {
        var h = normHref(MENU[i][1][j][0].split('#')[0]);
        if (h && h !== '/' && (here === h || here.indexOf(h + '/') === 0)) return MENU[i][0];
      }
    }
    var sec = section();
    if (sec && sec.name === 'Data Room') return 'Data';
    return null;
  }
  function menuHtml() {
    var cur = currentGroup();
    return MENU.map(function (g, i) {
      var id = 'im-sc-dd-' + i;
      var items = g[1].map(function (l) {
        return '<li><a href="' + SITE + l[0] + '"><b>' + l[1] + '</b><span>' + l[2] + '</span></a></li>';
      }).join('');
      return '<div class="im-sc-dd">' +
        '<button class="im-sc-dd-btn" type="button" aria-expanded="false" aria-controls="' + id + '"' +
          (cur === g[0] ? ' data-current="true"' : '') + '>' + g[0] + I.chev + '</button>' +
        '<ul class="im-sc-dd-panel" id="' + id + '" hidden>' + items + '</ul></div>';
    }).join('');
  }

  // ── Styles ─────────────────────────────────────────────────────────
  // Injected on every page (the consent notice and the floating slots need the
  // tokens on the homepage too). Rules for the bar only bite once build() has
  // put body.im-sc-on.
  function css() {
    return [
'.im-sc,.im-sc *{box-sizing:border-box}',
// --sc-ink is the accent as TEXT (hover, links); --sc-sel is the same hue as a
// FILL under --sc-sel-ink. #0EA5E9 (--sc-acc) is a tint for washes and borders
// only: as text on white it is 2.77:1.
'.im-sc{--sc-bg:rgba(255,255,255,.82);--sc-solid:#FFFFFF;--sc-fg:#0F172A;--sc-mut:#475569;--sc-bd:#E7EBF0;--sc-acc:#0EA5E9;--sc-ink:#0369A1;--sc-sel:#0369A1;--sc-sel-ink:#fff;--sc-grad:linear-gradient(135deg,#0369A1,#4F46E5)}',
// Dark --sc-mut is #CBD5E1, not #94A3B8: the bar is 85% opaque, and over a
// light page #94A3B8 fell to 4.41:1 on the Search label (#1281).
'html[data-theme="dark"] .im-sc,html.dark .im-sc{--sc-bg:rgba(11,17,32,.85);--sc-solid:#0B1120;--sc-fg:#F1F5F9;--sc-mut:#CBD5E1;--sc-bd:#25304A;--sc-ink:#7DD3FC;--sc-sel:#38BDF8;--sc-sel-ink:#0B1120;--sc-grad:linear-gradient(135deg,#38BDF8,#A5B4FC)}',
'@media(prefers-color-scheme:dark){html:not([data-theme]) .im-sc{--sc-bg:rgba(11,17,32,.85);--sc-solid:#0B1120;--sc-fg:#F1F5F9;--sc-mut:#CBD5E1;--sc-bd:#25304A;--sc-ink:#7DD3FC;--sc-sel:#38BDF8;--sc-sel-ink:#0B1120;--sc-grad:linear-gradient(135deg,#38BDF8,#A5B4FC)}}',
'.im-sc-bar{position:sticky;top:0;z-index:9999;display:flex;align-items:center;gap:14px;height:46px;padding:0 clamp(10px,3vw,28px);',
 'background:var(--sc-bg);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--sc-bd);',
 "font-family:'Inter',system-ui,-apple-system,sans-serif;font-size:14px;color:var(--sc-fg)}",
// Home link: the logo and the wordmark are one target, padded out to 44px.
'.im-sc-crumb{display:inline-flex;align-items:center;gap:9px;min-height:44px;min-width:44px;padding:0 6px;margin-left:-6px;border-radius:8px;text-decoration:none;color:var(--sc-fg);flex:none}',
'.im-sc-crumb img{width:24px;height:24px;border-radius:6px;flex:none}',
"html .im-sc-site,html.im-dyslexic .im-sc-site{font-family:'Amaranth','Inter',system-ui,sans-serif;font-weight:700;font-size:19px;letter-spacing:0;color:var(--sc-fg);white-space:nowrap}",
// Header groups: a disclosure button and a panel of links under it.
'.im-sc-nav{display:flex;align-items:center;gap:2px;flex:none}',
'.im-sc-dd{position:relative}',
'.im-sc-dd-btn{display:inline-flex;align-items:center;gap:4px;height:34px;padding:0 10px;border:0;border-radius:8px;background:transparent;color:var(--sc-fg);font:500 14px/1 inherit;cursor:pointer;white-space:nowrap}',
'.im-sc-dd-btn:hover,.im-sc-dd-btn[aria-expanded="true"]{background:color-mix(in srgb,var(--sc-acc) 10%,transparent);color:var(--sc-ink)}',
'.im-sc-dd-btn[data-current="true"]{color:var(--sc-ink);box-shadow:inset 0 -2px 0 var(--sc-sel)}',
'.im-sc-dd-btn .im-sc-i{width:13px;height:13px;transition:transform .15s}',
'.im-sc-dd-btn[aria-expanded="true"] .im-sc-i{transform:rotate(180deg)}',
'.im-sc-dd-panel{position:absolute;top:calc(100% + 6px);left:-6px;min-width:280px;margin:0;padding:6px;list-style:none;background:var(--sc-solid);border:1px solid var(--sc-bd);border-radius:12px;box-shadow:0 12px 32px rgba(15,23,42,.14);z-index:10000}',
'.im-sc-dd-panel[hidden]{display:none}',
'.im-sc-dd-panel a{display:flex;flex-direction:column;gap:2px;padding:9px 12px;border-radius:8px;color:var(--sc-fg);text-decoration:none}',
'.im-sc-dd-panel a b{font-weight:600;font-size:14px}',
'.im-sc-dd-panel a span{font-size:12.5px;color:var(--sc-mut);line-height:1.4}',
'.im-sc-dd-panel a:hover,.im-sc-dd-panel a:focus-visible{background:color-mix(in srgb,var(--sc-acc) 10%,transparent);color:var(--sc-ink)}',
'.im-sc-dd-panel a:hover span{color:var(--sc-mut)}',
'.im-sc-trail{display:none;align-items:center;gap:6px;min-width:0;color:var(--sc-mut);font-weight:500;white-space:nowrap}',
'.im-sc-sec{display:inline-flex;align-items:center;gap:4px;min-height:32px;min-width:0;color:var(--sc-mut);text-decoration:none;font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}',
'.im-sc-sec:hover{color:var(--sc-ink);text-decoration:underline}',
'.im-sc-sec span{overflow:hidden;text-overflow:ellipsis}',
'.im-sc-back{font-size:17px;line-height:1;font-weight:700}',
'.im-sc-spacer{flex:1}',
'.im-sc-right{display:flex;align-items:center;gap:6px;flex:none;min-height:38px}',
'.im-sc-btn{display:inline-flex;align-items:center;gap:6px;height:34px;padding:0 11px;border-radius:8px;border:1px solid transparent;',
 'background:transparent;color:var(--sc-fg);font:500 14px/1 inherit;text-decoration:none;cursor:pointer;white-space:nowrap;transition:background .15s,border-color .15s}',
'.im-sc-btn:hover{background:color-mix(in srgb,var(--sc-acc) 10%,transparent);color:var(--sc-ink)}',
'.im-sc-btn:focus-visible,.im-sc-dd-btn:focus-visible,.im-sc-dd-panel a:focus-visible,.im-sc-tbtn:focus-visible,.im-sc-crumb:focus-visible,.im-sc-sec:focus-visible,.im-sc-sheet a:focus-visible,.im-sc-consent button:focus-visible,.im-sc-close:focus-visible{outline:2px solid var(--sc-sel);outline-offset:2px}',
'.im-sc-i{width:16px;height:16px;flex:none;opacity:.85}',
'.im-sc-btn:hover .im-sc-i{opacity:1}',
// Search looks like a field, so it reads as the way in that it is.
'.im-sc-search{min-width:200px;justify-content:flex-start;border-color:var(--sc-bd);background:color-mix(in srgb,var(--sc-fg) 3%,transparent);color:var(--sc-mut)}',
'.im-sc-search .im-sc-label{flex:1;text-align:left}',
'.im-sc-kbd{font:500 11.5px/1 Inter,system-ui,sans-serif!important;border:1px solid var(--sc-bd);border-radius:5px;padding:3px 6px;color:var(--sc-mut);background:var(--sc-solid)}',
'.im-sc-icon{width:36px;height:34px;padding:0;justify-content:center}',
'.im-sc-setbtn{border-color:var(--sc-bd)}.im-sc-aa{font:700 15px/1 Inter,system-ui,sans-serif!important;letter-spacing:-.3px}',
'.im-sc-signup{background:var(--sc-sel);color:var(--sc-sel-ink);font-weight:600}',
'html body .im-sc .im-sc-signup,html body .im-sc .im-sc-signup:visited{background:var(--sc-sel);color:var(--sc-sel-ink)!important}',
'html body .im-sc .im-sc-signup:hover{background:var(--sc-sel);color:var(--sc-sel-ink)!important;opacity:.92}',
'.im-sc-signup[hidden],.im-sc-menu[hidden]{display:none}',
'.im-sc-acct.is-in{border-color:var(--sc-bd)}',
// Display settings: theme and reading font in one small panel.
'.im-sc-setwrap{position:relative}',
'.im-sc-setpanel{position:absolute;top:calc(100% + 6px);right:0;width:260px;padding:14px;background:var(--sc-solid);border:1px solid var(--sc-bd);border-radius:12px;box-shadow:0 12px 32px rgba(15,23,42,.14);z-index:10000}',
'.im-sc-setpanel[hidden]{display:none}',
'.im-sc-setpanel h3{font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:var(--sc-mut);margin:0 0 8px;font-weight:700}',
'.im-sc-setpanel h3+*{margin-bottom:14px}',
'.im-sc-theme{display:flex;gap:2px;background:color-mix(in srgb,var(--sc-fg) 6%,transparent);border:1px solid var(--sc-bd);border-radius:9px;padding:3px}',
'.im-sc-tbtn{flex:1;height:34px;border:0;border-radius:6px;background:transparent;color:var(--sc-fg);cursor:pointer;display:inline-flex;align-items:center;justify-content:center;gap:6px;font:500 13px/1 inherit}',
'html body .im-sc-tbtn[aria-pressed="true"]{background:var(--sc-sel);color:var(--sc-sel-ink)!important}',
'.im-sc-tbtn[aria-pressed="true"] .im-sc-i{opacity:1}',
'.im-sc-setpanel .im-sc-btn{width:100%;height:40px;border-color:var(--sc-bd)}',
'.im-sc-setpanel .im-sc-btn[aria-pressed="true"]{border-color:var(--sc-sel);background:color-mix(in srgb,var(--sc-sel) 14%,transparent)}',
'.im-sc-setpanel{width:300px;max-height:calc(100vh - 64px);overflow-y:auto;overscroll-behavior:contain}',
'.im-sc-setpanel .im-sc-a11y-list{display:grid;gap:6px;margin-bottom:14px}',
'.im-sc-setpanel .im-sc-a11y-list .im-sc-btn{justify-content:flex-start;gap:10px;font-weight:500}',
'.im-sc-tick{width:16px;height:16px;flex:none;border:1.5px solid var(--sc-mut);border-radius:4px;display:inline-flex;align-items:center;justify-content:center}',
'.im-sc-btn[aria-pressed="true"] .im-sc-tick{background:var(--sc-sel);border-color:var(--sc-sel)}',
'.im-sc-btn[aria-pressed="true"] .im-sc-tick::after{content:"";width:8px;height:4px;border:solid var(--sc-sel-ink);border-width:0 0 2px 2px;transform:translateY(-1px) rotate(-45deg)}',
'.im-sc-size{display:flex;gap:2px;background:color-mix(in srgb,var(--sc-fg) 6%,transparent);border:1px solid var(--sc-bd);border-radius:9px;padding:3px;margin-bottom:14px}',
'.im-sc-size button{flex:1;height:36px;border:0;border-radius:6px;background:transparent;color:var(--sc-fg);cursor:pointer;font-family:inherit;font-weight:600;line-height:1}',
'html body .im-sc-size button[aria-pressed="true"]{background:var(--sc-sel);color:var(--sc-sel-ink)!important}',
'.im-sc-size button:focus-visible{outline:2px solid var(--sc-sel);outline-offset:2px}',
'.im-sc-reset{width:100%;height:38px;border:0;background:transparent;color:var(--sc-ink);font:600 13.5px/1 inherit;text-decoration:underline;cursor:pointer}',
// The choices themselves, on every page that loads this script.
'html.im-a11y-text-1 body{zoom:1.15}html.im-a11y-text-2 body{zoom:1.3}',
'html.im-a11y-spacing body :is(p,li,dd,dt,td,th,blockquote,figcaption,label,summary){line-height:1.8!important;letter-spacing:.04em!important;word-spacing:.12em!important}',
'html.im-a11y-links body a:not(.im-sc-btn):not(.im-sc-crumb){text-decoration:underline!important;text-underline-offset:2px}',
'html.im-a11y-motion *,html.im-a11y-motion *::before,html.im-a11y-motion *::after{animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important;scroll-behavior:auto!important}',
'html.im-a11y-focus :focus-visible{outline:3px solid #B45309!important;outline-offset:3px!important;box-shadow:0 0 0 6px rgba(245,158,11,.45)!important}',

// Narrower screens: the keyboard hint goes, then the search label, then the
// groups move into the Menu sheet and the trail back to the section appears.
'@media(max-width:1180px){.im-sc-kbd{display:none}.im-sc-search{min-width:0}}',
'@media(max-width:1060px){.im-sc-search .im-sc-label,.im-sc-acct .im-sc-label{display:none}.im-sc-search,.im-sc-acct{padding:0 9px}}',
'@media(min-width:961px){.im-sc-menu{display:none!important}}',
'@media(max-width:960px){.im-sc-nav{display:none}.im-sc-trail{display:flex}.im-sc-bar .im-sc-site{display:none}}',
'@media(max-width:600px){.im-sc-bar{gap:6px;padding:0 10px}.im-sc-right{gap:2px}.im-sc-btn{padding:0 8px}.im-sc-signup{display:none}.im-sc-menu .im-sc-label{display:none}.im-sc-sec{max-width:38vw}}',
// Menu sheet
'.im-sc-sheet-wrap{position:fixed;inset:0;z-index:10001}',
'.im-sc-sheet-wrap[hidden]{display:none}',
'.im-sc-scrim{position:absolute;inset:0;background:rgba(15,23,42,.45)}',
'.im-sc-sheet{position:absolute;top:0;right:0;bottom:0;width:min(420px,92vw);overflow-y:auto;overscroll-behavior:contain;background:var(--sc-solid);color:var(--sc-fg);',
 "border-left:1px solid var(--sc-bd);box-shadow:-12px 0 40px rgba(15,23,42,.25);padding:14px 20px 32px;font-family:'Inter',system-ui,-apple-system,sans-serif}",
'.im-sc-sheet-head{display:flex;align-items:center;justify-content:space-between;margin:0 0 6px}',
'.im-sc-sheet-head h2{font-size:15px;font-weight:800;margin:0;color:var(--sc-fg)}',
'.im-sc-close{width:44px;height:44px;border:0;border-radius:10px;background:transparent;color:var(--sc-fg);cursor:pointer;display:inline-flex;align-items:center;justify-content:center}',
'.im-sc-close:hover{background:color-mix(in srgb,var(--sc-acc) 12%,transparent)}',
'.im-sc-close .im-sc-i{width:20px;height:20px}',
// The phone menu is one short list of sections; each opens its own page of
// links with a Back button, so the sheet never scrolls past one screen.
'.im-sc-pane[hidden]{display:none}',
'.im-sc-rows{list-style:none;margin:12px 0 0;padding:0;border-top:1px solid var(--sc-bd)}',
'.im-sc-pane h3+.im-sc-rows{margin-top:4px}',
'.im-sc-rows li{border-bottom:1px solid var(--sc-bd)}',
'.im-sc-row{display:flex;align-items:center;gap:10px;width:100%;min-height:60px;padding:8px 0;border:0;background:none;color:var(--sc-fg);font:inherit;text-align:left;cursor:pointer}',
'.im-sc-row:hover .im-sc-row-t{color:var(--sc-ink)}',
'.im-sc-row:focus-visible,.im-sc-back:focus-visible{outline:2px solid var(--sc-sel);outline-offset:2px;border-radius:6px}',
'.im-sc-row-tx{flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}',
'.im-sc-row-t{font-size:15.5px;font-weight:700}',
'.im-sc-row-h{font-size:12.5px;color:var(--sc-mut);line-height:1.35}',
'.im-sc-row-here{font-size:10.5px;font-weight:700;letter-spacing:.6px;text-transform:uppercase;color:var(--sc-ink);margin-left:6px}',
'.im-sc-row .im-sc-chev{width:18px;height:18px;flex:none;color:var(--sc-mut)}',
'.im-sc-back{display:inline-flex;align-items:center;gap:4px;min-height:44px;padding:0 10px 0 2px;border:0;background:none;color:var(--sc-ink);font:inherit;font-size:14px;font-weight:600;cursor:pointer}',
'.im-sc-back .im-sc-chev{width:18px;height:18px}',
'.im-sc-pane h3{font-size:20px;font-weight:800;margin:6px 0 8px;color:var(--sc-fg)}',
'.im-sc-links{list-style:none;margin:0;padding:0}',
'.im-sc-links li{border-bottom:1px solid var(--sc-bd)}',
'.im-sc-links li:last-child{border-bottom:0}',
'.im-sc-sheet :is(.im-sc-links,.im-sc-rows) a{flex-direction:column;align-items:flex-start;justify-content:center;gap:2px;min-height:52px;padding:6px 0}',
'.im-sc-sheet .im-sc-lt{font-size:15px;font-weight:600}',
'.im-sc-sheet .im-sc-ld{font-size:12.5px;color:var(--sc-mut);font-weight:400}',
'.im-sc-sheet :is(.im-sc-links,.im-sc-rows) a,.im-sc-sheet :is(.im-sc-links,.im-sc-rows) a:hover{text-decoration:none}',
'.im-sc-sheet a:hover .im-sc-lt{color:var(--sc-ink);text-decoration:underline}',
'.im-sc-sheet a[aria-current=page] .im-sc-lt{color:var(--sc-ink);font-weight:700}',
'.im-sc-sheet a{display:flex;align-items:center;min-height:40px;color:var(--sc-fg);text-decoration:none;font-size:14px;font-weight:500}',
'.im-sc-sheet a:hover{color:var(--sc-ink);text-decoration:underline}',
'.im-sc-tour-row{margin:10px 0 4px}',
'.im-sc-sheet-acct{display:flex;gap:8px;margin:6px 0 4px}.im-sc-sheet-acct a{flex:1;justify-content:center;border:1px solid var(--sc-bd);border-radius:8px}',
'.im-sc-cookie-set{background:none;border:0;padding:0;color:var(--sc-mut);font:inherit;text-decoration:underline;cursor:pointer}',
'.im-sc-cookie-set:hover{color:var(--sc-ink)}',
'.im-sc-cookie-set:focus-visible{outline:2px solid var(--sc-sel);outline-offset:2px}',
'.im-sc-dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:#D97706;margin-left:6px;vertical-align:middle}',
// footer
'.im-sc-foot{background:var(--sc-bg);border-top:1px solid var(--sc-bd);color:var(--sc-fg);font-family:\'Inter\',system-ui,sans-serif;padding:40px clamp(16px,4vw,32px) 28px;margin-top:48px}',
'html[data-theme="dark"] .im-sc-foot,html.dark .im-sc-foot{--sc-bg:#0B1120}',
'.im-sc-foot-in{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:minmax(180px,1.4fr) repeat(6,minmax(0,1fr));gap:28px 28px}',
'.im-sc-foot-brand{max-width:280px}',
'@media(max-width:1100px){.im-sc-foot-in{grid-template-columns:repeat(3,minmax(0,1fr))}.im-sc-foot-brand{grid-column:1/-1}}',
'@media(max-width:600px){.im-sc-foot-in{grid-template-columns:repeat(2,minmax(0,1fr));gap:24px 20px}}',
'.im-sc-foot-brand .im-sc-site{font-size:18px}',
'.im-sc-foot-brand p{margin:8px 0 0;color:var(--sc-mut);font-size:13px;line-height:1.6}',
'.im-sc-foot-col h3{font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:var(--sc-mut);margin:0 0 10px;font-weight:700}',
'.im-sc-foot-col a{display:block;color:var(--sc-fg);text-decoration:none;font-size:13.5px;font-weight:500;padding:4px 0}',
'.im-sc-foot-col a:hover{color:var(--sc-ink);text-decoration:underline}',
'.im-sc-foot-meta{max-width:1200px;margin:26px auto 0;padding-top:18px;border-top:1px solid var(--sc-bd);color:var(--sc-mut);',
 'font-size:12px;display:flex;flex-wrap:wrap;gap:8px 18px;justify-content:space-between;align-items:center}',
// Consent notice: one slim strip along the bottom edge, text and buttons on a
// single line where they fit. It never covers the page with a scrim, and the
// floating buttons are lifted above it.
'.im-sc-consent{position:fixed;left:0;right:0;bottom:0;z-index:9997;background:var(--sc-solid);color:var(--sc-fg);border-top:1px solid var(--sc-bd);',
 "box-shadow:0 -4px 16px rgba(15,23,42,.10);padding:8px 16px;font:400 13px/1.45 'Inter',system-ui,-apple-system,sans-serif;",
 'display:flex;align-items:center;justify-content:center;gap:8px 16px;flex-wrap:wrap}',
'.im-sc-consent p{margin:0;max-width:720px}',
'.im-sc-consent a{color:var(--sc-ink);text-decoration:underline}',
'.im-sc-consent div{display:flex;gap:8px;flex:0 0 auto}',
'.im-sc-consent button{min-height:36px;min-width:88px;padding:0 14px;border-radius:8px;font:600 13px/1 inherit;cursor:pointer;border:1px solid var(--sc-sel)}',
'html body .im-sc-consent button.is-yes{background:var(--sc-sel)!important;color:var(--sc-sel-ink)!important}',
'html body .im-sc-consent button.is-no{background:transparent!important;color:var(--sc-fg)!important}',
'@media(max-width:600px){.im-sc-consent{padding:8px 12px}.im-sc-consent div{flex:1 1 100%}.im-sc-consent button{flex:1;min-height:40px}}',
// The share button waits until the reader has scrolled past the first screen,
// so nothing but the consent strip covers the opening of a page.
'#im-wa-fab.im-wa-wait{display:none!important}',
// On a 101 deck the slide controls sit along the bottom edge, so the card goes
// under the top bar instead of covering them.
'.im-sc-consent.is-deck{top:56px;bottom:auto!important;border-top:0;border-bottom:1px solid var(--sc-bd)}',
'@media(prefers-reduced-motion:reduce){.im-sc *{transition:none!important}}',
'.im-sc-inv{filter:invert(.92) hue-rotate(180deg)}',
// reconcile app-like pages (course shells): kill dead reserved padding + offset fixed sidebar/progress below the 46px bar
'body.im-sc-on{padding-top:0!important}',
'body.im-sc-on .sidebar{top:46px!important;height:calc(100dvh - 46px)!important}',
'body.im-sc-on .sidebar-overlay{top:46px!important}',
'body.im-sc-on .reading-progress{top:46px!important}',
// One theme control per page (L1). Once the bar carries its theme group, the
// page's own copies are duplicates: the 101 deck pill (#theme-bar), the Free
// Studio and handout selectors, and the flagship toggles. The bar writes every
// key those controls read (see applyTheme), so hiding them loses nothing.
'body.im-sc-on.im-sc-has-theme #theme-bar,body.im-sc-on.im-sc-has-theme .theme-selector,body.im-sc-on.im-sc-has-theme .im-theme-selector,',
 'body.im-sc-on.im-sc-has-theme .theme-toggle,body.im-sc-on.im-sc-has-theme #theme-toggle,body.im-sc-on.im-sc-has-theme #themeToggle{display:none!important}',
// The chrome hides itself on paper.
//
// It has to be here rather than in each page's own print stylesheet, because
// build() above DELETES the legacy chrome -- .im-topbar, .site-header, .header,
// footer, .im-footer -- and injects its own under .im-sc names. Sixty pages
// still tell the printer to hide the old names, so those rules match nothing
// and the nav bar and footer printed on every lab worksheet, practice pack and
// companion tool: 60 of 60 measured, 22 nav links each (#1080). Any page added
// later inherits this instead of needing its own copy, which is the point --
// sixty copies of a name is how the last rename got lost.
// Page titles and section headings share the homepage's Amaranth, so every
// page reads as one family; h3 and below stay in the running-text Inter.
// build() sets .im-sc-type only on pages that do not carry their own type
// (slide decks, games and the print handouts keep theirs). Skipped for the
// reading font, which must win, and for pages in another language, because
// Amaranth has Latin letters only and would push Indian scripts onto a
// fallback face instead of the page's own Noto.
"html:not(.im-dyslexic):is([lang^=en],:not([lang])) body.im-sc-type :is(h1,h2):not(.im-sc *){font-family:'Amaranth','Inter',system-ui,-apple-system,sans-serif!important}",
'@media print{.im-sc,.im-sc-bar,.im-sc-foot,.im-sc-consent,#im-wa-fab{display:none!important}body.im-sc-on{padding-top:0!important}}'
    ].join('');
  }
  function injectCss() {
    if (document.getElementById('im-sc-style')) return;
    var st = document.createElement('style'); st.id = 'im-sc-style'; st.textContent = css(); document.head.appendChild(st);
  }

  // ── Icons: inline SVG, drawn in currentColor ───────────────────────
  // These used to be Sargam SVGs fetched from jsDelivr with onerror hiding the
  // <img>. With the CDN blocked or slow, Membership, About, Home and the three
  // theme buttons rendered as blank boxes on a phone (M10), and each late or
  // failed load nudged the row (a small layout shift). Every icon is now a few
  // hundred bytes in this file. aria-hidden: the control carries the name.
  function svg(d, cls) {
    return '<svg class="' + (cls || 'im-sc-i') + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
      + 'stroke-linecap="round" stroke-linejoin="round" width="15" height="15" aria-hidden="true" focusable="false">' + d + '</svg>';
  }
  var I = {
    search: svg('<circle cx="11" cy="11" r="7.5"/><path d="m21 21-4-4"/>'),
    globe: svg('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3Z"/>'),
    star: svg('<path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2-5.6-2.9-5.6 2.9 1.1-6.2L3 9.6l6.2-.9Z"/>'),
    info: svg('<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/>'),
    home: svg('<path d="M4 10.5 12 4l8 6.5V20h-5v-6H9v6H4Z"/>'),
    sys: svg('<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>'),
    sun: svg('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'),
    moon: svg('<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/>'),
    menu: svg('<path d="M4 7h16M4 12h16M4 17h16"/>'),
    user: svg('<circle cx="12" cy="8" r="4"/><path d="M4 21c1.2-4 4.3-6 8-6s6.8 2 8 6"/>'),
    close: svg('<path d="M6 6l12 12M18 6 6 18"/>'),
    chev: svg('<path d="m6 9 6 6 6-6"/>'),
    next: svg('<path d="m9 6 6 6-6 6"/>', 'im-sc-i im-sc-chev'),
    prev: svg('<path d="m15 6-6 6 6 6"/>', 'im-sc-i im-sc-chev'),
    a11y: svg('<circle cx="12" cy="12" r="9.5"/><circle cx="12" cy="7.2" r="1.3"/><path d="M7.5 10h9M12 10v4.5M12 14.5l-2.5 4M12 14.5l2.5 4"/>'),
    sliders: svg('<path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12M20 18h0"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/>')
  };
  var LOGO = SITE + '/assets/images/apple-touch-icon.png'; // 7KB vs the 599KB full logo

  // ── Theme (same contract as theme.js) ──────────────────────────────
  // The site has three canonical theme keys depending on the page's age:
  // theme.js reads 'im-theme', the flagship courses and Free Studio read
  // 'impactmojo-theme', and older pages read 'theme'. Writing only one of them
  // meant a reader's choice in this bar was overridden on the next load of any
  // page that reads another, so every key is written, as theme.js does.
  var THEME_KEYS = ['im-theme', 'impactmojo-theme', 'theme', 'imx_theme'];
  function normMode(v) { v = String(v || '').replace(/^ineq-/, ''); return v === 'light' || v === 'dark' || v === 'system' ? v : null; }
  function currentMode() {
    for (var i = 0; i < THEME_KEYS.length; i++) { var v = normMode(store(THEME_KEYS[i])); if (v) return v; }
    return 'system';
  }
  function applyTheme(mode, quiet) {
    if (!quiet) for (var i = 0; i < THEME_KEYS.length; i++) store(THEME_KEYS[i], mode);
    var resolved = mode === 'system'
      ? (window.matchMedia && matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light')
      : mode;
    // Always the resolved value, as theme.js does: several Free Studio pages are
    // dark by default and only turn light on data-theme="light", so removing
    // the attribute for "system" rendered them dark on a light-mode device.
    root.setAttribute('data-theme', resolved);
    root.classList.toggle('dark', resolved === 'dark');
    if (document.body) {
      document.body.classList.remove('dark-mode', 'light-mode');
      document.body.classList.add(resolved === 'dark' ? 'dark-mode' : 'light-mode');
    }
    // 101 decks keep their own body classes behind window.setTheme; their
    // "system" resolves to the key written above, so hand it the mode.
    if (document.getElementById('theme-bar') && typeof window.setTheme === 'function') {
      try { window.setTheme(mode); } catch (e) {}
    }
    syncTheme(mode);
    scheduleFloating(30); // a theme can switch a body filter on or off (hostFixed)
  }
  function syncTheme(mode) {
    var btns = document.querySelectorAll('.im-sc-tbtn');
    for (var i = 0; i < btns.length; i++) btns[i].setAttribute('aria-pressed', btns[i].getAttribute('data-m') === mode ? 'true' : 'false');
  }
  function themeGroup(withText) {
    function b(m, icon, label) {
      return '<button class="im-sc-tbtn" type="button" data-m="' + m + '" title="' + label + '" aria-label="' + label + ' theme">'
        + icon + (withText ? '<span>' + label + '</span>' : '') + '</button>';
    }
    return '<div class="im-sc-theme" role="group" aria-label="Theme">' + b('system', I.sys, 'System') + b('light', I.sun, 'Light') + b('dark', I.moon, 'Dark') + '</div>';
  }

  // ── Sign-in state, without waiting on the network ──────────────────
  // auth.js (window.ImpactMojoAuth) is on a minority of pages and resolves its
  // session asynchronously. The Supabase client keeps the session in
  // localStorage, so reading it there gives the right answer at first paint;
  // authStateChanged corrects it if auth.js later finds otherwise.
  function hasToken(raw) {
    try { var v = JSON.parse(raw); return !!(v && (v.access_token || (v.currentSession && v.currentSession.access_token))); } catch (e) { return false; }
  }
  function signedIn() {
    try { if (window.ImpactMojoAuth && window.ImpactMojoAuth.user) return true; } catch (e) {}
    try {
      if (hasToken(localStorage.getItem('impactmojo-auth'))) return true;
      for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i);
        if (k && k.indexOf('sb-') === 0 && /-auth-token$/.test(k) && hasToken(localStorage.getItem(k))) return true;
      }
    } catch (e) {}
    return false;
  }
  function syncAccount(force) {
    var a = document.querySelector('.im-sc-acct'); if (!a) return;
    var inn = typeof force === 'boolean' ? force : signedIn();
    var label = inn ? 'My account' : 'Log in';
    a.href = SITE + (inn ? '/account.html' : '/login.html');
    a.setAttribute('aria-label', label);
    a.classList.toggle('is-in', inn);
    a.querySelector('.im-sc-label').textContent = label;
    document.querySelectorAll('.im-sc-signup').forEach(function (b) { b.hidden = inn; });
    var sa = document.querySelector('[data-sheet-acct]');
    if (sa) { sa.textContent = label; sa.href = a.href; }
  }

  // ── Accessibility menu ─────────────────────────────────────────────
  function syncA11y() {
    var v = a11yGet(), t = v.text === 1 || v.text === 2 ? v.text : 0;
    document.querySelectorAll('[data-a11y-text]').forEach(function (b) { b.setAttribute('aria-pressed', String(+b.getAttribute('data-a11y-text') === t)); });
    document.querySelectorAll('[data-a11y]').forEach(function (b) { b.setAttribute('aria-pressed', String(!!v[b.getAttribute('data-a11y')])); });
  }
  function a11ySet(v) {
    store(A11Y_KEY, JSON.stringify(v));
    a11yApply(v); syncA11y(); scheduleFloating(60);
  }
  function wireA11y(bar) {
    bar.querySelectorAll('[data-a11y-text]').forEach(function (b) {
      b.addEventListener('click', function () { var v = a11yGet(); v.text = +b.getAttribute('data-a11y-text'); a11ySet(v); });
    });
    bar.querySelectorAll('[data-a11y]').forEach(function (b) {
      b.addEventListener('click', function () { var v = a11yGet(), k = b.getAttribute('data-a11y'); v[k] = !v[k]; a11ySet(v); });
    });
    bar.querySelector('[data-a11y-reset]').addEventListener('click', function () {
      a11ySet({});
      if (root.classList.contains('im-dyslexic')) toggleDys();
      applyTheme('system');
    });
    syncA11y();
  }

  // ── Header groups and the settings panel ───────────────────────────
  // Disclosure buttons: one panel open at a time; a click outside, Escape or
  // moving focus out closes it, and Escape returns focus to its button.
  function wireDropdowns(bar) {
    var btns = [].slice.call(bar.querySelectorAll('.im-sc-dd-btn,.im-sc-setbtn'));
    function panel(b) { return document.getElementById(b.getAttribute('aria-controls')); }
    function closeAll(except) {
      btns.forEach(function (b) {
        if (b === except) return;
        b.setAttribute('aria-expanded', 'false');
        var p = panel(b); if (p) p.hidden = true;
      });
    }
    btns.forEach(function (b) {
      b.addEventListener('click', function (e) {
        e.stopPropagation();
        var open = b.getAttribute('aria-expanded') !== 'true';
        closeAll(b);
        b.setAttribute('aria-expanded', open ? 'true' : 'false');
        var p = panel(b); if (p) p.hidden = !open;
      });
      // With a pointer, moving across the groups opens the next one while
      // another is already open, the way a menu bar behaves.
      if (b.classList.contains('im-sc-dd-btn')) b.addEventListener('mouseenter', function () {
        if (!btns.some(function (o) { return o !== b && o.classList.contains('im-sc-dd-btn') && o.getAttribute('aria-expanded') === 'true'; })) return;
        closeAll(b); b.setAttribute('aria-expanded', 'true'); var p = panel(b); if (p) p.hidden = false;
      });
    });
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.im-sc-dd,.im-sc-setwrap')) closeAll();
    });
    bar.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      var open = btns.filter(function (b) { return b.getAttribute('aria-expanded') === 'true'; })[0];
      if (open) { e.preventDefault(); closeAll(); open.focus(); }
    });
    bar.addEventListener('focusout', function (e) {
      if (!e.relatedTarget || !bar.contains(e.relatedTarget)) closeAll();
    });
  }

  // ── Search, from the bar and from Ctrl/Cmd+K on every page ─────────
  // search.js ships on a minority of pages, so it is loaded on first use.
  // Where it is already on the page it binds Ctrl/Cmd+K itself, and this
  // handler stands aside.
  function openSearch() {
    if (window.ImpactMojoSearch && window.ImpactMojoSearch.open) return window.ImpactMojoSearch.open();
    if (document.getElementById('im-search-loader')) return;
    var s = document.createElement('script');
    s.id = 'im-search-loader';
    s.src = '/js/search.js';
    s.onload = function () {
      if (window.ImpactMojoSearch && window.ImpactMojoSearch.open) window.ImpactMojoSearch.open();
    };
    document.head.appendChild(s);
  }
  function wireSearchKey() {
    document.addEventListener('keydown', function (e) {
      if (!(e.ctrlKey || e.metaKey) || e.altKey || String(e.key).toLowerCase() !== 'k') return;
      if (window.ImpactMojoSearch) return; // search.js handles its own shortcut
      e.preventDefault();
      openSearch();
    });
  }

  // ── Build ──────────────────────────────────────────────────────────
  function build() {
    harvestFresh();
    // 1. remove legacy chrome (broad: catches the many header/footer patterns across the site)
    var sel = '.im-topbar,#imTopbar,.top-nav,.site-header,header.header,.navbar,.site-nav,.main-nav,'
            + '.nav-container,.masthead,header.mobile-header,.mobile-header,'
            + 'footer,.footer,.foot,.site-footer,.im-footer';
    var kill = [].slice.call(document.querySelectorAll(sel));
    // also any top-level <header>/<nav> that's a direct child of <body> (the site bar)
    [].slice.call(document.body.children).forEach(function (el) {
      var t = el.tagName; if ((t === 'HEADER' || t === 'NAV') && kill.indexOf(el) === -1) kill.push(el);
    });
    for (var i = 0; i < kill.length; i++) { if (kill[i].closest && kill[i].closest('.im-sc')) continue; kill[i].parentNode && kill[i].parentNode.removeChild(kill[i]); }

    // 2. state classes (styles are already in from boot)
    document.body.classList.add('im-sc-on', 'im-sc-has-theme');
    if (!/^\/(games|handouts)\/|^\/101-courses\/(native\/)?(?!index(\.html)?$)[^/]+$/i.test(location.pathname)) document.body.classList.add('im-sc-type');

    // 3. top bar
    var sec = section();
    // On a phone the groups live in the Menu sheet, so the bar carries one
    // "‹ Section" link back to where this page belongs (desktop shows the
    // section by underlining its group instead).
    var trail = (sec && !sec.isHub)
      ? '<a class="im-sc-sec" href="' + sec.href + '"><span class="im-sc-back" aria-hidden="true">&lsaquo;</span><span>' + escapeHtml(sec.name) + '</span></a>'
      : '';
    var mac = /Mac|iPhone|iPad/.test(navigator.platform || navigator.userAgent || '');
    var bar = document.createElement('div');
    bar.className = 'im-sc im-sc-bar'; bar.setAttribute('role', 'navigation'); bar.setAttribute('aria-label', 'Site');
    bar.innerHTML =
      '<a class="im-sc-crumb" href="/" aria-label="ImpactMojo home">' +
        '<img src="' + LOGO + '" alt="" width="24" height="24">' +
        '<span class="im-sc-site">ImpactMojo</span>' +
      '</a>' +
      '<div class="im-sc-nav">' + menuHtml() + '</div>' +
      '<span class="im-sc-trail">' + trail + '</span>' +
      '<span class="im-sc-spacer"></span>' +
      '<div class="im-sc-right">' +
        '<button class="im-sc-btn im-sc-lang im-sc-icon" type="button" aria-label="Language">' + I.globe + '</button>' +
        '<button class="im-sc-btn im-sc-search" type="button" aria-label="Search ' + (mac ? '&#8984;K' : 'Ctrl K') + '">' + I.search + '<span class="im-sc-label">Search</span> ' +
          '<kbd class="im-sc-kbd" aria-hidden="true">' + (mac ? '&#8984;K' : 'Ctrl K') + '</kbd></button>' +
        '<div class="im-sc-setwrap">' +
          '<button class="im-sc-btn im-sc-icon im-sc-setbtn" type="button" aria-expanded="false" aria-controls="im-sc-setpanel" aria-label="Accessibility and display" title="Accessibility"><span class="im-sc-aa" aria-hidden="true">Aa</span></button>' +
          '<div class="im-sc-setpanel" id="im-sc-setpanel" role="region" aria-label="Accessibility and display" hidden>' +
            '<h3>Theme</h3>' + themeGroup(true) +
            '<h3 id="im-sc-size-h">Text size</h3><div class="im-sc-size" role="group" aria-labelledby="im-sc-size-h">' +
              '<button type="button" data-a11y-text="0" aria-pressed="false" aria-label="Default text size" style="font-size:13px">A</button>' +
              '<button type="button" data-a11y-text="1" aria-pressed="false" aria-label="Larger text" style="font-size:16px">A</button>' +
              '<button type="button" data-a11y-text="2" aria-pressed="false" aria-label="Largest text" style="font-size:19px">A</button></div>' +
            '<h3>Reading</h3><div class="im-sc-a11y-list">' +
              '<button class="im-sc-btn" type="button" data-im-dys aria-pressed="false"><span class="im-sc-tick" aria-hidden="true"></span>Dyslexia-friendly font</button>' +
              '<button class="im-sc-btn" type="button" data-a11y="spacing" aria-pressed="false"><span class="im-sc-tick" aria-hidden="true"></span>Wider line and letter spacing</button>' +
              '<button class="im-sc-btn" type="button" data-a11y="links" aria-pressed="false"><span class="im-sc-tick" aria-hidden="true"></span>Underline every link</button>' +
              '<button class="im-sc-btn" type="button" data-a11y="motion" aria-pressed="false"><span class="im-sc-tick" aria-hidden="true"></span>Reduce motion</button>' +
              '<button class="im-sc-btn" type="button" data-a11y="focus" aria-pressed="false"><span class="im-sc-tick" aria-hidden="true"></span>Stronger focus outline</button>' +
            '</div>' +
            '<button class="im-sc-reset" type="button" data-a11y-reset>Reset all</button>' +
          '</div>' +
        '</div>' +
        '<a class="im-sc-btn im-sc-acct" href="' + SITE + '/login.html" aria-label="Log in">' + I.user + '<span class="im-sc-label">Log in</span></a>' +
        '<a class="im-sc-btn im-sc-signup" href="' + SITE + '/signup.html">Sign up free</a>' +
        '<button class="im-sc-btn im-sc-menu" type="button" aria-expanded="false" aria-controls="im-sc-sheet" aria-haspopup="dialog" aria-label="Menu">' + I.menu + '<span class="im-sc-label">Menu</span></button>' +
      '</div>';
    document.body.insertBefore(bar, document.body.firstChild);

    // A 101 deck's stage (#deck) is fixed to the whole window, so on a laptop
    // the bar covered the top of every slide: 46px of it on a 16:9 screen,
    // which is the slide header. Start the stage below the bar; each deck
    // sizes its slide to #deck's height, so a resize event re-fits it. Phones
    // (820px and under) read decks as a scrolling page and are left alone.
    if (isDeck) {
      var fitDeck = function () {
        var d = document.getElementById('deck');
        if (!d) return;
        var wide = window.innerWidth > 820;
        var top = wide ? Math.round(bar.getBoundingClientRect().bottom) + 'px' : '';
        d.style.background = wide ? '#111' : '';
        // The deck's own resize handler ran before this one, so if the stage
        // moved it measured the old height: fire once more.
        if (d.style.top !== top) { d.style.top = top; window.dispatchEvent(new Event('resize')); }
      };
      window.addEventListener('resize', fitDeck);
      fitDeck();
    }

    // 4. footer. Not on a 101 deck (isDeck): a deck fills the screen and has
    // its own footer line, so this one sat behind the slides on a laptop and
    // below them on a phone, where the page scrolled down into it. Cookie
    // settings are on the footer of every other page.
    if (!isDeck) {
    var foot = document.createElement('footer');
    foot.className = 'im-sc im-sc-foot'; foot.setAttribute('role', 'contentinfo');
    foot.innerHTML =
      '<div class="im-sc-foot-in">' +
        '<div class="im-sc-foot-brand"><span class="im-sc-site">ImpactMojo</span>' +
          '<p>Free, open-source development education for South Asia: flagship courses, the 101 Series, Free Studio, games, data and research tools.</p></div>' +
        navCols('im-sc-foot-col') +
      '</div>' +
      '<div class="im-sc-foot-meta"><span>CC BY-NC-ND 4.0 &middot; Free Forever &middot; &copy; ImpactMojo</span>' +
        '<button type="button" class="im-sc-cookie-set" data-im-cookies>Cookie settings</button>' +
        '<span>Made for South Asian development practitioners</span></div>';
    document.body.appendChild(foot);
    // Cookie settings forgets the stored choice and asks again with the strip.
    foot.querySelector('[data-im-cookies]').addEventListener('click', function () {
      try { localStorage.removeItem(CONSENT_KEY); localStorage.removeItem('cookieConsent'); } catch (e) {}
      injectConsent();
      var box = document.getElementById('im-consent');
      if (box) { var first = box.querySelector('button'); if (first) first.focus(); }
    });
    }

    // 5. menu sheet (H2): the footer's groups as a list of sections, each
    // opening its own pane of links (sheetPanes).
    var sp = sheetPanes();
    var wrap = document.createElement('div');
    wrap.className = 'im-sc im-sc-sheet-wrap'; wrap.hidden = true;
    wrap.innerHTML =
      '<div class="im-sc-scrim" data-close></div>' +
      '<div class="im-sc-sheet" id="im-sc-sheet" role="dialog" aria-modal="true" aria-labelledby="im-sc-sheet-h">' +
        '<div class="im-sc-sheet-head"><h2 id="im-sc-sheet-h">Menu</h2>' +
          '<button class="im-sc-close" type="button" data-close aria-label="Close menu">' + I.close + '</button></div>' +
        '<div class="im-sc-pane" data-pane="root">' +
          '<div class="im-sc-sheet-acct"><a class="im-sc-btn" href="' + SITE + '/login.html" data-sheet-acct>Log in</a><a class="im-sc-btn im-sc-signup" href="' + SITE + '/signup.html">Sign up free</a></div>' +
          (isFront ? '<div class="im-sc-tour-row"><button class="im-sc-btn" type="button" data-im-tour>Take a tour of this page</button></div>' : '') +
          sp.rows +
        '</div>' + sp.panes +
      '</div>';
    document.body.appendChild(wrap);
    wireSheet(bar.querySelector('.im-sc-menu'), wrap);
    bar.querySelector('[data-im-dys]').addEventListener('click', toggleDys);
    wireA11y(bar);
    wireDropdowns(bar);

    // 6. wire theme
    // theme.js always sets data-theme. A page without it (the homepage among
    // them) never applied a saved choice on load, so a reader who chose dark
    // got the light page on every visit. Apply it here in that case only.
    if (!root.hasAttribute('data-theme')) applyTheme(currentMode(), true);
    syncTheme(currentMode());
    document.querySelectorAll('.im-sc-tbtn').forEach(function (b) {
      b.addEventListener('click', function () { applyTheme(b.getAttribute('data-m')); });
    });
    if (window.matchMedia) matchMedia('(prefers-color-scheme:dark)').addEventListener('change', function () {
      if (currentMode() === 'system') applyTheme('system', true);
    });

    // 7. account item
    syncAccount();
    bar.querySelector('.im-sc-acct').addEventListener('click', function () {
      // auth.js sends a reader back here after signing in.
      if (!signedIn() && !/\/login\.html$/i.test(location.pathname)) {
        try { sessionStorage.setItem('authRedirect', location.href); } catch (e) {}
      }
    });
    window.addEventListener('authStateChanged', function (e) {
      syncAccount(e && e.detail && typeof e.detail.isLoggedIn === 'boolean' ? e.detail.isLoggedIn : undefined);
    });
    window.addEventListener('storage', function () { syncAccount(); });

    // 7b. full-width bar. On a page whose <body> is a narrow centred column
    // (the 84 handouts, 8.5in) the bar is the body's first child and ran only
    // as wide as the column, so on a desktop its right-hand buttons met the
    // screen edge outside it. Margins are measured and applied in pixels, not
    // as calc(50% - 50vw), which counts the scrollbar and would scroll the page.
    function bleedBar() {
      if (bar.parentNode !== document.body) return;
      bar.style.marginLeft = ''; bar.style.marginRight = '';
      var cs = getComputedStyle(bar), vw = document.documentElement.clientWidth, r = bar.getBoundingClientRect();
      var l = Math.round(r.left), rt = Math.round(vw - r.right);
      if (l > 1 || rt > 1) {
        bar.style.marginLeft = ((parseFloat(cs.marginLeft) || 0) - Math.max(0, l)) + 'px';
        bar.style.marginRight = ((parseFloat(cs.marginRight) || 0) - Math.max(0, rt)) + 'px';
      }
    }
    bleedBar();
    window.addEventListener('load', bleedBar);
    window.addEventListener('resize', bleedBar);

    // 8. search
    bar.querySelector('.im-sc-search').addEventListener('click', openSearch);
    // 9. language: reuse translate-sarvam if present, else ask the page
    bar.querySelector('.im-sc-lang').addEventListener('click', function () {
      if (typeof window.ImpactMojoTranslate === 'function') return window.ImpactMojoTranslate();
      var w = document.querySelector('[data-sarvam-widget],.sarvam-translate,#sarvam-translate,.translate-widget');
      if (w) { w.scrollIntoView({ behavior: 'smooth' }); w.click && w.click(); return; }
      document.dispatchEvent(new CustomEvent('im:open-language'));
    });
  }

  // ── Menu sheet behaviour ───────────────────────────────────────────
  // A modal dialog: focus moves in, Tab cycles inside it, Escape or the scrim
  // closes it, and focus returns to the Menu button.
  function wireSheet(btn, wrap) {
    var sheet = wrap.querySelector('.im-sc-sheet');
    function focusables() {
      return [].slice.call(sheet.querySelectorAll('a[href],button:not([disabled])')).filter(function (el) { return el.offsetParent !== null; });
    }
    function show(name) {
      [].forEach.call(sheet.querySelectorAll('.im-sc-pane'), function (p) { p.hidden = p.getAttribute('data-pane') !== name; });
      sheet.scrollTop = 0;
    }
    function open() {
      show('root');
      wrap.hidden = false;
      btn.setAttribute('aria-expanded', 'true');
      var f = sheet.querySelector('.im-sc-close'); f && f.focus();
      document.addEventListener('keydown', onKey, true);
    }
    function close() {
      if (wrap.hidden) return;
      wrap.hidden = true;
      btn.setAttribute('aria-expanded', 'false');
      document.removeEventListener('keydown', onKey, true);
      btn.focus();
    }
    function onKey(e) {
      if (e.key === 'Escape') { e.preventDefault(); e.stopPropagation(); close(); return; }
      if (e.key !== 'Tab') return;
      var f = focusables(); if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (!sheet.contains(document.activeElement)) { e.preventDefault(); first.focus(); }
      else if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
    btn.addEventListener('click', function () { if (wrap.hidden) open(); else close(); });
    wrap.addEventListener('click', function (e) {
      if (e.target.closest('[data-close]')) close();
      var row = e.target.closest('[data-open]');
      if (row) {
        show(row.getAttribute('data-open'));
        var b = sheet.querySelector('.im-sc-pane:not([hidden]) [data-back]'); b && b.focus();
      }
      // Back returns to the parent screen and puts focus on the row that
      // opened this one.
      var back = e.target.closest('[data-back]');
      if (back) {
        var from = back.closest('.im-sc-pane').getAttribute('data-pane');
        show(back.getAttribute('data-back'));
        var r = sheet.querySelector('[data-open="' + from + '"]'); r && r.focus();
      }
      if (e.target.closest('[data-im-tour]')) {
        close();
        if (window.ImpactMojoTour) window.ImpactMojoTour.start('index');
      }
    });
    // A link to a #fragment on this page should not leave the sheet over it.
    sheet.addEventListener('click', function (e) { if (e.target.closest('a[href]')) { wrap.hidden = true; btn.setAttribute('aria-expanded', 'false'); document.removeEventListener('keydown', onKey, true); } });
  }

  function escapeHtml(s) { return String(s).replace(/[&<>"]/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]; }); }

  // ── Reading-font control — every page, homepage included ───────────
  // It rides next to whichever theme control the page has: .im-sc-right on the
  // pages this script builds, .theme-selector on the homepage, which keeps
  // its own chrome and so never reaches build(). Takes the host's own button
  // class so it inherits that bar's styling instead of carrying a second one.
  // A second toggle sits in the Menu sheet for phones; both are [data-im-dys]
  // and stay in step.
  function syncDys() {
    var on = root.classList.contains('im-dyslexic');
    document.querySelectorAll('[data-im-dys]').forEach(function (b) {
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      if (b.id === 'im-dys-btn') b.title = on ? 'Dyslexia-friendly font: on' : 'Dyslexia-friendly font';
    });
  }
  function toggleDys() {
    var on = !root.classList.contains('im-dyslexic');
    root.classList.toggle('im-dyslexic', on);
    store(DYS_KEY, on ? 'opendyslexic' : 'default');
    syncDys();
  }
  function injectReadingFont() {
    if (document.getElementById('im-dys-btn')) return;
    // The built bar carries the switch in its settings panel.
    if (document.querySelector('.im-sc-setpanel')) { syncDys(); return; }
    var host = document.querySelector('.theme-selector');
    if (!host) return;
    var inBar = host.classList.contains('im-sc-right');

    // The "on" state has to be styled here rather than in css(): the homepage
    // styles its own .theme-btn, and this rule has to reach it as well.
    if (!document.getElementById('im-dys-style')) {
      var st = document.createElement('style');
      st.id = 'im-dys-style';
      // "On" is the bar's accent as an outline and a wash of itself, with the
      // label left at the bar's own ink. The obvious version -- copy the theme
      // buttons, fill with --sc-grad and set the text white -- was measured and
      // fails: the gradient starts at #0EA5E9, and imx-main.css says in as many
      // words that white on that is 2.77:1, which is why --accent-solid
      // (#0369A1, 5.93:1) exists at all. An outline avoids the question, and
      // matches how the same control looks on the sibling sites. State is not
      // carried by colour alone: with the switch on, the label renders in
      // OpenDyslexic, and aria-pressed says so for a screen reader.
      var acc = 'var(--sc-acc,var(--accent-solid,#0369A1))';
      st.textContent = '#im-dys-btn{cursor:pointer}'
        + '#im-dys-btn[aria-pressed="true"]{border-color:' + acc + ';'
        + 'background:color-mix(in srgb,' + acc + ' 16%,transparent)}';
      document.head.appendChild(st);
    }

    var b = document.createElement('button');
    b.id = 'im-dys-btn';
    b.type = 'button';
    b.setAttribute('data-im-dys', '');
    b.className = inBar ? 'im-sc-btn im-sc-dys' : 'theme-btn im-sc-dys';
    b.innerHTML = '<span aria-hidden="true" style="font-weight:700;font-size:13px;line-height:1;letter-spacing:.02em">Aa</span>';
    // The label says what it does, not what it is called: "OpenDyslexic" means
    // nothing to a reader who has never been told the name of the typeface.
    b.setAttribute('aria-label', 'Dyslexia-friendly font');

    // Before the theme group in the built bar (reading settings together, and
    // clear of the Home link at the end); appended on the homepage's own group.
    var themeGroupEl = host.querySelector('.im-sc-theme');
    if (themeGroupEl) host.insertBefore(b, themeGroupEl); else host.appendChild(b);
    b.addEventListener('click', toggleDys);
    syncDys();
  }

  // The message names the page being read: its own title, its description and
  // its address, so a learner sharing a course shares that course. It states no
  // counts, which go stale, and carries no emoji or em dashes (house style).
  function waMessage() {
    var url = location.origin + location.pathname;
    var canon = document.querySelector('link[rel="canonical"]');
    if (canon && canon.href) url = canon.href;
    var p = location.pathname.replace(/\/index\.html?$/, '/');
    if (p === '/' || p === '') {
      return 'ImpactMojo has free courses, Studios, datasets and book companions for people working in development in South Asia.\n' + url;
    }
    function m(sel) { var el = document.querySelector(sel); return el ? (el.getAttribute('content') || '').trim() : ''; }
    var title = m('meta[property="og:title"]') || document.title || '';
    // Drop a trailing " | ImpactMojo" or section name (" | Learning Loops").
    title = title.replace(/\s+[|–—]\s+[^|–—]+$/, '').trim();
    var desc = m('meta[property="og:description"]') || m('meta[name="description"]');
    var parts = [title || 'ImpactMojo'];
    if (desc && desc !== title) parts.push(desc);
    parts.push(url);
    return parts.join('\n');
  }

  // ── Shared WhatsApp "share this page" button ──────────────────────
  // Every page except the 101 decks (see isDeck). Guarded against duplicates.
  // Its height above the bottom edge is set by layoutFloating(), not here.
  function injectWhatsApp() {
    if (!document.body || isDeck || document.getElementById('im-wa-fab')) return;
    var a = document.createElement('a');
    a.id = 'im-wa-fab';
    a.className = 'im-wa-wait';
    a.href = 'https://wa.me/?text=' + encodeURIComponent(waMessage());
    a.target = '_blank'; a.rel = 'noopener noreferrer';
    a.setAttribute('aria-label', 'Share this page on WhatsApp');
    a.title = 'Share this page on WhatsApp';
    a.style.cssText = 'position:fixed;right:18px;bottom:18px;z-index:9998;width:52px;height:52px;border-radius:50%;background:#25D366;box-shadow:0 6px 20px rgba(37,211,102,.45);display:flex;align-items:center;justify-content:center;text-decoration:none;transition:transform .15s ease';
    a.addEventListener('mouseenter', function () { a.style.transform = 'scale(1.08)'; });
    a.addEventListener('mouseleave', function () { a.style.transform = 'scale(1)'; });
    a.innerHTML = '<svg viewBox="0 0 24 24" width="28" height="28" fill="#fff" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>';
    var wrap = document.createElement('aside');
    wrap.setAttribute('aria-label', 'Share this page');
    wrap.appendChild(a);
    document.body.appendChild(wrap);
    function reveal() {
      if (window.scrollY < window.innerHeight * 0.6) return;
      a.classList.remove('im-wa-wait');
      window.removeEventListener('scroll', reveal);
      scheduleFloating(30);
    }
    window.addEventListener('scroll', reveal, { passive: true });
    reveal();
  }

  // ── Floating-button slots (R4) ─────────────────────────────────────
  // Pages carry up to four floating buttons from different eras (WhatsApp,
  // Mojini, the chatbot, feedback, the cookie and tools speed-dial), each
  // positioned by its own stylesheet and none aware of the others: 13 measured
  // overlaps. This places them once everything has loaded. A button keeps the
  // position its page gave it unless that collides with one already placed,
  // in which case it moves up to clear it. Big things (an open chat panel, an
  // expanded cookie card) and anything anchored by `top` are obstacles that
  // others move around, never moved themselves.
  var FLOAT_SEL = '#im-wa-fab,#mojini-chat-toggle,.chatbot-fab,.mojini-fab,.feedback-fab,.imx-speed-dial,'
                + '#cookieConsent,.cookie-consent,#im-lang-switch.im-lang-floating,#im-consent,.userway_buttons_wrapper';
  var GAP = 10;
  function layoutFloating() {
    if (!document.body) return;
    hostFixed();
    var vh = window.innerHeight;
    var seen = [], items = [];
    [].slice.call(document.querySelectorAll(FLOAT_SEL)).forEach(function (el) {
      if (seen.indexOf(el) !== -1) return; seen.push(el);
      // Each pass starts from where the page itself puts the button (its own
      // media queries included), so undo our last move first. Transitions are
      // off while we measure and move: several buttons animate `bottom`, and a
      // reset-then-move would otherwise play as a jump down and back up.
      if (el.getAttribute('data-im-ib') === null) el.setAttribute('data-im-ib', el.style.getPropertyValue('bottom') || '');
      el.setAttribute('data-im-tr', el.style.transition || '');
      el.style.transition = 'none';
      if (el.hasAttribute('data-im-moved')) {
        var ib = el.getAttribute('data-im-ib');
        if (ib) el.style.setProperty('bottom', ib); else el.style.removeProperty('bottom');
        el.removeAttribute('data-im-moved');
      }
      var cs = getComputedStyle(el);
      if (cs.position !== 'fixed' || cs.display === 'none' || cs.visibility === 'hidden') return;
      var r = el.getBoundingClientRect();
      if (!r.width || !r.height) return;
      // Anything anchored by `top`, anything big (an open chat panel, an
      // expanded cookie card) and the consent card stay put.
      var fixedObstacle = cs.bottom === 'auto' || r.height > 180 || el.id === 'im-consent';
      items.push({ el: el, l: r.left, r: r.right, h: r.height, b: vh - r.bottom, fixed: fixedObstacle,
                   wa: el.id === 'im-wa-fab' });
    });
    // Obstacles first, then the page's own buttons from the bottom up; the
    // WhatsApp button goes last so it is the one that yields.
    items.sort(function (a, b) { return (b.fixed - a.fixed) || (a.wa - b.wa) || (a.b - b.b); });
    var placed = [];
    items.forEach(function (it) {
      var bottom = it.b;
      if (!it.fixed) {
        for (var guard = 0; guard < 12; guard++) {
          var hit = null;
          for (var i = 0; i < placed.length; i++) {
            var p = placed[i];
            var xOverlap = it.l < p.r + 4 && it.r > p.l - 4;
            var yOverlap = bottom < p.b + p.h + GAP && bottom + it.h + GAP > p.b;
            if (xOverlap && yOverlap) { hit = p; break; }
          }
          if (!hit) break;
          bottom = hit.b + hit.h + GAP;
        }
        if (Math.abs(bottom - it.b) > 0.5) {
          it.el.style.setProperty('bottom', Math.round(bottom) + 'px', 'important');
          it.el.setAttribute('data-im-moved', '');
        }
      }
      placed.push({ l: it.l, r: it.r, h: it.h, b: bottom });
    });
    // Commit the positions, then give each button its own transition back.
    if (seen.length) seen[0].getBoundingClientRect();
    seen.forEach(function (el) { el.style.transition = el.getAttribute('data-im-tr') || ''; });
  }

  // ── Pages whose <body> carries a filter ────────────────────────────
  // 83 pages load assets/css/dark-mode-fallback.css, which in dark mode puts
  // `filter: invert()` on <body>. A filter makes <body> the containing block
  // for position:fixed, so the sheet, the consent card and the WhatsApp button
  // would sit at the top or the foot of the whole document instead of the
  // screen. While that filter is on, they are hosted on <html> instead, and
  // the bar and footer (which stay in <body>) get the counter-filter that the
  // fallback stylesheet gives the legacy .im-topbar.
  function hostFixed() {
    var b = document.body; if (!b) return;
    var cs = getComputedStyle(b);
    var filtered = cs.filter !== 'none' || cs.transform !== 'none';
    var host = filtered ? root : b;
    ['.im-sc-sheet-wrap', '#im-consent', '#im-wa-fab'].forEach(function (s) {
      var el = document.querySelector(s); if (!el) return;
      if (s === '#im-wa-fab' && el.parentNode && el.parentNode.tagName === 'ASIDE') el = el.parentNode;
      if (el.parentNode !== host) host.appendChild(el);
    });
    var inv = cs.filter !== 'none';
    document.querySelectorAll('.im-sc-bar,.im-sc-foot').forEach(function (el) { el.classList.toggle('im-sc-inv', inv); });
  }
  var floatTimer;
  function scheduleFloating(ms) { clearTimeout(floatTimer); floatTimer = setTimeout(layoutFloating, ms || 120); }
  function watchFloating() {
    layoutFloating();
    window.addEventListener('load', function () { scheduleFloating(50); setTimeout(layoutFloating, 1500); setTimeout(layoutFloating, 4000); });
    window.addEventListener('resize', function () { scheduleFloating(150); });
    // Assistants (mojini-ai.js and friends) append their buttons to <body>
    // after load; a direct-children observer catches them cheaply.
    if (window.MutationObserver) new MutationObserver(function () { scheduleFloating(200); }).observe(document.body, { childList: true });
    // A click can open or close a chat panel or the cookie card.
    document.addEventListener('click', function () { scheduleFloating(350); }, true);
  }

  // ── Analytics consent notice (M9) ──────────────────────────────────
  // A reader who has not chosen sees a slim strip with two equal buttons. The
  // choice is stored, and passed to gtag's consent mode when the page has gtag.
  function injectConsent() {
    if (consentChoice() || document.getElementById('im-consent')) return;
    var box = document.createElement('div');
    box.id = 'im-consent';
    box.className = 'im-sc im-sc-consent' + (isDeck ? ' is-deck' : '');
    box.setAttribute('role', 'region');
    box.setAttribute('aria-label', 'Cookie choice');
    box.innerHTML = '<p>We use analytics cookies to see which pages are useful. The site works the same if you decline. '
      + '<a href="' + SITE + '/privacy-policy.html">Privacy policy</a>.</p>'
      + '<div><button type="button" class="is-yes" data-c="granted">Accept</button><button type="button" class="is-no" data-c="denied">Decline</button></div>';
    box.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-c]'); if (!b) return;
      var c = b.getAttribute('data-c');
      store(CONSENT_KEY, c);
      if (typeof window.gtag === 'function') { try { window.gtag('consent', 'update', { analytics_storage: c }); } catch (err) {} }
      if (c === 'granted' && typeof window.imLoadGA === 'function') window.imLoadGA();
      box.parentNode && box.parentNode.removeChild(box);
      scheduleFloating(30);
    });
    document.body.appendChild(box);
  }

  // Register the service worker everywhere the chrome loads. js/pwa.js only
  // ships on ~23 pages; without this, most entry points never get offline
  // support or CDN caching. Guarded so pages that DO load pwa.js don't
  // double-register (register() with the same scope is idempotent anyway).
  function registerSW() {
    if (!('serviceWorker' in navigator)) return;
    if (location.protocol !== 'https:' && location.hostname !== 'localhost') return;
    try { navigator.serviceWorker.register('/service-worker.js'); } catch (e) { /* non-fatal */ }
  }

  // Small hook for pages that add a floating button of their own later.
  window.ImpactMojoChrome = { layoutFloating: layoutFloating };

  function boot() {
    injectCss();
    if (!isHome) build();
    injectReadingFont();
    injectWhatsApp();
    injectConsent();
    wireSearchKey();
    registerSW();
    watchFloating();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
