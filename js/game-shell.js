/**
 * ImpactMojo Game Shell v3
 * Injects shared header, footer, 3-way theme, Indian folk art motifs,
 * and visual enhancements into all game pages.
 * Inspired by FolkLog's use of Madhubani, Warli, and Gond art traditions.
 * Usage: <script src="/js/game-shell.js"></script> (at end of <body>)
 */
(function() {
  'use strict';

  // ── Theme System (System / Light / Dark) ──────────────────
  var THEME_KEY = 'imx_theme';
  var saved = localStorage.getItem(THEME_KEY);

  function getSystemPref() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
  }
  function resolveTheme(pref) {
    if (pref === 'light') return 'light';
    if (pref === 'dark') return 'dark';
    return getSystemPref();
  }
  function applyTheme(pref) {
    var resolved = resolveTheme(pref);
    document.body.classList.toggle('light-mode', resolved === 'light');
    document.querySelectorAll('.imx-theme-btn').forEach(function(btn) {
      btn.classList.toggle('active', btn.getAttribute('data-theme') === (pref || 'system'));
    });
  }
  function setTheme(pref) {
    if (pref === 'system' || !pref) localStorage.removeItem(THEME_KEY);
    else localStorage.setItem(THEME_KEY, pref);
    applyTheme(pref);
  }
  applyTheme(saved);
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', function() {
      if (!localStorage.getItem(THEME_KEY)) applyTheme(null);
    });
  }

  // ── Header ─────────────────────────────────────────────────
  var header = document.createElement('nav');
  header.id = 'imx-game-header';
  header.innerHTML =
    '<a href="/" class="imx-gh-logo">' +
      '<img src="/assets/images/ImpactMojo%20Logo.png" alt="ImpactMojo" width="32" height="32">' +
      '<span>ImpactMojo</span>' +
    '</a>' +
    '<div class="imx-gh-right">' +
      '<a href="/#games" class="imx-gh-link">All Games</a>' +
      '<div class="imx-gh-theme-group">' +
        '<button class="imx-theme-btn' + (!saved ? ' active' : '') + '" data-theme="system" title="System theme" aria-label="System theme">' +
          '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>' +
        '</button>' +
        '<button class="imx-theme-btn' + (saved === 'light' ? ' active' : '') + '" data-theme="light" title="Light theme" aria-label="Light theme">' +
          '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>' +
        '</button>' +
        '<button class="imx-theme-btn' + (saved === 'dark' ? ' active' : '') + '" data-theme="dark" title="Dark theme" aria-label="Dark theme">' +
          '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>' +
        '</button>' +
      '</div>' +
    '</div>';
  document.body.insertBefore(header, document.body.firstChild);
  document.querySelectorAll('.imx-theme-btn').forEach(function(btn) {
    btn.addEventListener('click', function() { setTheme(btn.getAttribute('data-theme')); });
  });

  // ── Paper Plane SVG ────────────────────────────────────────
  var plane = document.createElement('div');
  plane.className = 'imx-game-plane';
  plane.setAttribute('aria-hidden', 'true');
  plane.innerHTML =
    '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">' +
      '<path d="M50,150 L150,50 L50,100 L80,130 Z" fill="none" stroke="#0EA5E9" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>' +
      '<path d="M80,130 L150,50" stroke="#10B981" stroke-width="2" stroke-dasharray="4,4"/>' +
      '<circle cx="150" cy="50" r="4" fill="#6366F1"/>' +
    '</svg>';
  document.body.appendChild(plane);

  // ── Indian Folk Art Decorations ────────────────────────────

  // Warli-inspired village scene (bottom-left) — stick figures, huts, trees
  var warli = document.createElement('div');
  warli.className = 'imx-game-motif imx-motif-warli';
  warli.setAttribute('aria-hidden', 'true');
  warli.innerHTML =
    '<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">' +
      // Ground line
      '<line x1="0" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="0.8" opacity="0.15"/>' +
      // Hut
      '<polygon points="50,180 50,140 75,115 100,140 100,180" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.2"/>' +
      '<line x1="70" y1="180" x2="70" y2="155" stroke="currentColor" stroke-width="0.8" opacity="0.15"/>' +
      '<line x1="80" y1="180" x2="80" y2="155" stroke="currentColor" stroke-width="0.8" opacity="0.15"/>' +
      // Tree (Warli style - trunk + circles)
      '<line x1="150" y1="180" x2="150" y2="120" stroke="currentColor" stroke-width="1" opacity="0.18"/>' +
      '<circle cx="150" cy="110" r="18" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.15"/>' +
      '<circle cx="140" cy="120" r="12" fill="none" stroke="currentColor" stroke-width="0.6" opacity="0.12"/>' +
      '<circle cx="160" cy="118" r="14" fill="none" stroke="currentColor" stroke-width="0.6" opacity="0.12"/>' +
      // Dancing figures (Warli tarpa dance)
      '<g opacity="0.2" transform="translate(200,140)">' +
        // Figure 1 - triangle body
        '<polygon points="0,0 -8,25 8,25" fill="none" stroke="currentColor" stroke-width="1"/>' +
        '<circle cx="0" cy="-6" r="5" fill="none" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="-10" y1="8" x2="10" y2="8" stroke="currentColor" stroke-width="0.8"/>' +
        '<line x1="-4" y1="25" x2="-8" y2="40" stroke="currentColor" stroke-width="0.8"/>' +
        '<line x1="4" y1="25" x2="8" y2="40" stroke="currentColor" stroke-width="0.8"/>' +
      '</g>' +
      '<g opacity="0.2" transform="translate(225,138)">' +
        '<polygon points="0,0 -8,25 8,25" fill="none" stroke="currentColor" stroke-width="1"/>' +
        '<circle cx="0" cy="-6" r="5" fill="none" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="-12" y1="6" x2="12" y2="10" stroke="currentColor" stroke-width="0.8"/>' +
        '<line x1="-4" y1="25" x2="-10" y2="42" stroke="currentColor" stroke-width="0.8"/>' +
        '<line x1="4" y1="25" x2="10" y2="42" stroke="currentColor" stroke-width="0.8"/>' +
      '</g>' +
      '<g opacity="0.18" transform="translate(250,142)">' +
        '<polygon points="0,0 -7,22 7,22" fill="none" stroke="currentColor" stroke-width="1"/>' +
        '<circle cx="0" cy="-5" r="4.5" fill="none" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="-10" y1="10" x2="8" y2="5" stroke="currentColor" stroke-width="0.8"/>' +
        '<line x1="-3" y1="22" x2="-6" y2="38" stroke="currentColor" stroke-width="0.8"/>' +
        '<line x1="3" y1="22" x2="6" y2="38" stroke="currentColor" stroke-width="0.8"/>' +
      '</g>' +
      // Sun (Warli spiral)
      '<circle cx="270" cy="30" r="15" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.15"/>' +
      '<path d="M270,30 m-8,0 a8,8 0 1,1 16,0 a12,12 0 1,0 -24,0" fill="none" stroke="currentColor" stroke-width="0.5" opacity="0.12"/>' +
    '</svg>';
  document.body.appendChild(warli);

  // Madhubani-inspired border pattern (top-right) — fish, peacock, geometric
  var madhubani = document.createElement('div');
  madhubani.className = 'imx-game-motif imx-motif-madhubani';
  madhubani.setAttribute('aria-hidden', 'true');
  madhubani.innerHTML =
    '<svg viewBox="0 0 200 300" xmlns="http://www.w3.org/2000/svg">' +
      // Vertical border strip with geometric patterns
      // Outer border
      '<rect x="5" y="5" width="40" height="290" fill="none" stroke="#D97706" stroke-width="0.8" opacity="0.15" rx="4"/>' +
      '<rect x="10" y="10" width="30" height="280" fill="none" stroke="#DC2626" stroke-width="0.5" opacity="0.12" rx="3"/>' +
      // Fish motifs (Madhubani signature)
      '<g transform="translate(25,40)" opacity="0.2">' +
        '<ellipse cx="0" cy="0" rx="12" ry="6" fill="none" stroke="#D97706" stroke-width="1"/>' +
        '<path d="M12,0 L18,-5 L18,5Z" fill="none" stroke="#D97706" stroke-width="0.8"/>' +
        '<circle cx="-5" cy="-1" r="1.5" fill="#D97706" opacity="0.5"/>' +
        '<line x1="-3" y1="0" x2="8" y2="0" stroke="#D97706" stroke-width="0.4" stroke-dasharray="1,2"/>' +
      '</g>' +
      // Peacock (simplified Madhubani style)
      '<g transform="translate(25,100)" opacity="0.18">' +
        '<ellipse cx="0" cy="0" rx="8" ry="10" fill="none" stroke="#059669" stroke-width="0.8"/>' +
        '<circle cx="0" cy="-14" r="4" fill="none" stroke="#059669" stroke-width="0.8"/>' +
        '<line x1="0" y1="-18" x2="0" y2="-22" stroke="#059669" stroke-width="0.6"/>' +
        '<circle cx="0" cy="-23" r="1" fill="#059669" opacity="0.4"/>' +
        // Tail feathers (fan)
        '<path d="M-8,5 Q-20,-15 -5,-25" fill="none" stroke="#2563EB" stroke-width="0.6" opacity="0.8"/>' +
        '<path d="M0,5 Q0,-20 0,-28" fill="none" stroke="#2563EB" stroke-width="0.6" opacity="0.8"/>' +
        '<path d="M8,5 Q20,-15 5,-25" fill="none" stroke="#2563EB" stroke-width="0.6" opacity="0.8"/>' +
        '<circle cx="-10" cy="-18" r="2" fill="none" stroke="#D97706" stroke-width="0.5" opacity="0.6"/>' +
        '<circle cx="0" cy="-22" r="2" fill="none" stroke="#D97706" stroke-width="0.5" opacity="0.6"/>' +
        '<circle cx="10" cy="-18" r="2" fill="none" stroke="#D97706" stroke-width="0.5" opacity="0.6"/>' +
      '</g>' +
      // Lotus (Madhubani style)
      '<g transform="translate(25,170)" opacity="0.18">' +
        '<ellipse cx="0" cy="0" rx="5" ry="12" fill="none" stroke="#EC4899" stroke-width="0.8"/>' +
        '<ellipse cx="0" cy="0" rx="5" ry="12" fill="none" stroke="#EC4899" stroke-width="0.8" transform="rotate(30)"/>' +
        '<ellipse cx="0" cy="0" rx="5" ry="12" fill="none" stroke="#EC4899" stroke-width="0.8" transform="rotate(60)"/>' +
        '<ellipse cx="0" cy="0" rx="5" ry="12" fill="none" stroke="#EC4899" stroke-width="0.8" transform="rotate(90)"/>' +
        '<ellipse cx="0" cy="0" rx="5" ry="12" fill="none" stroke="#EC4899" stroke-width="0.8" transform="rotate(120)"/>' +
        '<ellipse cx="0" cy="0" rx="5" ry="12" fill="none" stroke="#EC4899" stroke-width="0.8" transform="rotate(150)"/>' +
        '<circle cx="0" cy="0" r="4" fill="none" stroke="#D97706" stroke-width="0.8" opacity="0.6"/>' +
      '</g>' +
      // Geometric diamond pattern
      '<g transform="translate(25,230)" opacity="0.15">' +
        '<rect x="-10" y="-10" width="20" height="20" fill="none" stroke="#D97706" stroke-width="0.8" transform="rotate(45)"/>' +
        '<rect x="-6" y="-6" width="12" height="12" fill="none" stroke="#DC2626" stroke-width="0.5" transform="rotate(45)"/>' +
        '<circle cx="0" cy="0" r="3" fill="#D97706" opacity="0.2"/>' +
      '</g>' +
      // Another fish (bottom)
      '<g transform="translate(25,270) rotate(180)" opacity="0.17">' +
        '<ellipse cx="0" cy="0" rx="12" ry="6" fill="none" stroke="#059669" stroke-width="1"/>' +
        '<path d="M12,0 L18,-5 L18,5Z" fill="none" stroke="#059669" stroke-width="0.8"/>' +
        '<circle cx="-5" cy="-1" r="1.5" fill="#059669" opacity="0.4"/>' +
      '</g>' +
    '</svg>';
  document.body.appendChild(madhubani);

  // Gond-inspired tree of life (right side, lower)
  var gond = document.createElement('div');
  gond.className = 'imx-game-motif imx-motif-gond';
  gond.setAttribute('aria-hidden', 'true');
  gond.innerHTML =
    '<svg viewBox="0 0 160 200" xmlns="http://www.w3.org/2000/svg">' +
      // Tree trunk with Gond dot-and-line pattern
      '<line x1="80" y1="200" x2="80" y2="80" stroke="currentColor" stroke-width="2" opacity="0.15"/>' +
      '<line x1="75" y1="200" x2="75" y2="90" stroke="currentColor" stroke-width="0.5" opacity="0.1" stroke-dasharray="2,3"/>' +
      '<line x1="85" y1="200" x2="85" y2="90" stroke="currentColor" stroke-width="0.5" opacity="0.1" stroke-dasharray="2,3"/>' +
      // Branches
      '<path d="M80,130 Q50,110 30,90" fill="none" stroke="currentColor" stroke-width="1" opacity="0.15"/>' +
      '<path d="M80,130 Q110,110 130,90" fill="none" stroke="currentColor" stroke-width="1" opacity="0.15"/>' +
      '<path d="M80,100 Q55,85 40,60" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.13"/>' +
      '<path d="M80,100 Q105,85 120,60" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.13"/>' +
      '<path d="M80,80 Q65,60 55,35" fill="none" stroke="currentColor" stroke-width="0.6" opacity="0.12"/>' +
      '<path d="M80,80 Q95,60 105,35" fill="none" stroke="currentColor" stroke-width="0.6" opacity="0.12"/>' +
      // Gond-style leaf circles (dots-within-dots)
      '<circle cx="30" cy="85" r="10" fill="none" stroke="#059669" stroke-width="0.8" opacity="0.18"/>' +
      '<circle cx="30" cy="85" r="5" fill="none" stroke="#059669" stroke-width="0.5" opacity="0.12"/>' +
      '<circle cx="30" cy="85" r="2" fill="#059669" opacity="0.15"/>' +
      '<circle cx="130" cy="85" r="10" fill="none" stroke="#D97706" stroke-width="0.8" opacity="0.18"/>' +
      '<circle cx="130" cy="85" r="5" fill="none" stroke="#D97706" stroke-width="0.5" opacity="0.12"/>' +
      '<circle cx="130" cy="85" r="2" fill="#D97706" opacity="0.15"/>' +
      '<circle cx="40" cy="55" r="8" fill="none" stroke="#EC4899" stroke-width="0.6" opacity="0.15"/>' +
      '<circle cx="40" cy="55" r="3" fill="#EC4899" opacity="0.1"/>' +
      '<circle cx="120" cy="55" r="8" fill="none" stroke="#3B82F6" stroke-width="0.6" opacity="0.15"/>' +
      '<circle cx="120" cy="55" r="3" fill="#3B82F6" opacity="0.1"/>' +
      '<circle cx="55" cy="30" r="7" fill="none" stroke="#8B5CF6" stroke-width="0.5" opacity="0.13"/>' +
      '<circle cx="55" cy="30" r="2.5" fill="#8B5CF6" opacity="0.1"/>' +
      '<circle cx="105" cy="30" r="7" fill="none" stroke="#10B981" stroke-width="0.5" opacity="0.13"/>' +
      '<circle cx="105" cy="30" r="2.5" fill="#10B981" opacity="0.1"/>' +
      // Birds (Gond style — simple)
      '<path d="M20,40 Q25,32 30,38 L35,35" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.15"/>' +
      '<path d="M130,25 Q135,18 140,24 L145,21" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.15"/>' +
    '</svg>';
  document.body.appendChild(gond);

  // ── Footer ─────────────────────────────────────────────────
  var footer = document.createElement('footer');
  footer.id = 'imx-game-footer';
  footer.innerHTML =
    '<div class="imx-gf-inner">' +
      '<div class="imx-gf-divider"></div>' +
      '<p>Made with \u2764\uFE0F by <a href="https://www.pinpointventures.in" target="_blank" rel="noopener noreferrer">PinPoint Ventures</a></p>' +
      '<div class="imx-gf-links">' +
        '<a href="/">Home</a>' +
        '<a href="/about">About</a>' +
        '<a href="/privacy-policy">Privacy</a>' +
        '<a href="/terms-of-service">Terms</a>' +
        '<a href="https://github.com/Varnasr/ImpactMojo" target="_blank" rel="noopener noreferrer">GitHub</a>' +
      '</div>' +
      '<p class="imx-gf-copy">\u00A9 ' + new Date().getFullYear() + ' ImpactMojo. MIT + CC BY-NC-ND 4.0</p>' +
    '</div>';
  document.body.appendChild(footer);

  // ── Inject Styles ──────────────────────────────────────────
  var css = document.createElement('style');
  css.textContent =

    /* ═══ DARK MODE CONTRAST FIX ═══════════════════════════ */
    /* Fix black cards with grey text — boost contrast */
    'body:not(.light-mode) .card, body:not(.light-mode) [class*="card"] { background: #1E293B !important; color: #F1F5F9 !important; border-color: #475569 !important; }' +
    'body:not(.light-mode) p, body:not(.light-mode) span, body:not(.light-mode) li, body:not(.light-mode) label, body:not(.light-mode) td { color: #E2E8F0 !important; }' +
    'body:not(.light-mode) h1, body:not(.light-mode) h2, body:not(.light-mode) h3, body:not(.light-mode) h4 { color: #F8FAFC !important; }' +
    'body:not(.light-mode) small, body:not(.light-mode) .text-muted, body:not(.light-mode) .subtitle { color: #CBD5E1 !important; }' +
    'body:not(.light-mode) th { background: #334155 !important; color: #F1F5F9 !important; }' +
    'body:not(.light-mode) td { border-color: #475569 !important; }' +
    'body:not(.light-mode) input, body:not(.light-mode) select, body:not(.light-mode) textarea { background: #334155 !important; color: #F1F5F9 !important; border-color: #475569 !important; }' +
    'body:not(.light-mode) button:not(.imx-theme-btn) { color: #F1F5F9 !important; }' +
    'body:not(.light-mode) .hint, body:not(.light-mode) .tip, body:not(.light-mode) blockquote, body:not(.light-mode) .note { background: #1E3A5F !important; border-color: #3B82F6 !important; color: #E2E8F0 !important; }' +

    /* ═══ LIGHT MODE ═══════════════════════════════════════ */
    'body.light-mode { background: #FFFBF5 !important; color: #1E293B !important; }' +
    'body.light-mode .card, body.light-mode [class*="card"] { background: #FFFFFF !important; border-color: #E7DDD0 !important; color: #1E293B !important; box-shadow: 0 2px 8px rgba(139,90,43,0.08); }' +
    'body.light-mode input, body.light-mode select, body.light-mode textarea { background: #FFF8F0 !important; color: #1E293B !important; border-color: #D4C4B0 !important; }' +
    'body.light-mode button:not(.imx-theme-btn) { color: #1E293B; }' +
    'body.light-mode h1, body.light-mode h2, body.light-mode h3, body.light-mode h4 { color: #1A1207 !important; }' +
    'body.light-mode p, body.light-mode span, body.light-mode li, body.light-mode td, body.light-mode th, body.light-mode label, body.light-mode small { color: #3D2E1C !important; }' +
    'body.light-mode a:not(.imx-gh-logo):not(.imx-gh-link):not(.imx-gf-inner a) { color: #B45309 !important; }' +
    'body.light-mode table { border-color: #E7DDD0 !important; }' +
    'body.light-mode th { background: #FFF3E6 !important; color: #1A1207 !important; }' +
    'body.light-mode td { border-color: #E7DDD0 !important; }' +
    'body.light-mode [class*="stat"] { background: #FFFFFF !important; border-color: #E7DDD0 !important; }' +
    'body.light-mode .progress-bar, body.light-mode [class*="progress"]:not([class*="fill"]) { background: #E7DDD0 !important; }' +
    'body.light-mode .hint, body.light-mode .tip, body.light-mode blockquote, body.light-mode .note { background: #FFF8F0 !important; border-color: #D97706 !important; color: #78350F !important; }' +

    /* ═══ HEADER ═══════════════════════════════════════════ */
    '#imx-game-header {' +
      'position: sticky; top: 0; z-index: 999;' +
      'display: flex; align-items: center; justify-content: space-between;' +
      'padding: 0.5rem 1.25rem;' +
      'background: rgba(15,23,42,0.92); backdrop-filter: blur(12px);' +
      'border-bottom: 1px solid rgba(255,255,255,0.08);' +
    '}' +
    'body.light-mode #imx-game-header { background: rgba(255,251,245,0.95); border-bottom-color: #E7DDD0; }' +
    '.imx-gh-logo { display: flex; align-items: center; gap: 0.5rem; text-decoration: none; color: #F8FAFC; font-weight: 700; font-size: 1rem; }' +
    'body.light-mode .imx-gh-logo { color: #1A1207; }' +
    '.imx-gh-logo img { width: 32px; height: 32px; border-radius: 6px; }' +
    '.imx-gh-right { display: flex; align-items: center; gap: 0.75rem; }' +
    '.imx-gh-link { color: #94A3B8; text-decoration: none; font-size: 0.85rem; font-weight: 500; transition: color 0.2s; }' +
    '.imx-gh-link:hover { color: #F59E0B; }' +
    'body.light-mode .imx-gh-link { color: #78350F; }' +

    /* Theme toggle group */
    '.imx-gh-theme-group { display: flex; gap: 2px; background: rgba(255,255,255,0.08); border-radius: 8px; padding: 2px; }' +
    'body.light-mode .imx-gh-theme-group { background: #E7DDD0; }' +
    '.imx-theme-btn { background: none; border: none; border-radius: 6px; width: 32px; height: 32px; cursor: pointer; color: #94A3B8; display: flex; align-items: center; justify-content: center; transition: all 0.2s; }' +
    '.imx-theme-btn:hover { color: #F1F5F9; background: rgba(255,255,255,0.1); }' +
    '.imx-theme-btn.active { background: rgba(245,158,11,0.2); color: #F59E0B; }' +
    'body.light-mode .imx-theme-btn { color: #92400E; }' +
    'body.light-mode .imx-theme-btn:hover { color: #1A1207; background: rgba(139,90,43,0.1); }' +
    'body.light-mode .imx-theme-btn.active { background: rgba(217,119,6,0.2); color: #B45309; }' +
    '.imx-theme-btn svg { stroke-linecap: round; stroke-linejoin: round; }' +

    /* ═══ DECORATIVE ELEMENTS ═════════════════════════════ */

    /* Paper plane */
    '.imx-game-plane { position: fixed; top: 12%; right: 6%; width: 100px; height: 100px; opacity: 0.12; z-index: 0; pointer-events: none; animation: imx-fly 25s ease-in-out infinite; }' +
    'body.light-mode .imx-game-plane { opacity: 0.08; }' +
    '.imx-game-plane svg { width: 100%; height: 100%; }' +
    '@keyframes imx-fly { 0%,100% { transform: translate(0,0) rotate(0deg); } 20% { transform: translate(50px,-30px) rotate(10deg); } 40% { transform: translate(100px,20px) rotate(-6deg); } 60% { transform: translate(30px,50px) rotate(12deg); } 80% { transform: translate(-20px,15px) rotate(-4deg); } }' +

    /* Indian folk art motifs */
    '.imx-game-motif { position: fixed; pointer-events: none; z-index: 0; }' +
    '.imx-game-motif svg { width: 100%; height: 100%; }' +
    '.imx-motif-warli { bottom: 0; left: 0; width: 300px; height: 200px; opacity: 0.7; color: #F59E0B; }' +
    'body.light-mode .imx-motif-warli { color: #92400E; opacity: 0.5; }' +
    '.imx-motif-madhubani { top: 60px; right: 0; width: 50px; height: 300px; opacity: 0.8; }' +
    'body.light-mode .imx-motif-madhubani { opacity: 0.6; }' +
    '.imx-motif-gond { bottom: 5%; right: 8%; width: 140px; height: 180px; opacity: 0.6; color: #94A3B8; animation: imx-sway 30s ease-in-out infinite; }' +
    'body.light-mode .imx-motif-gond { color: #78350F; opacity: 0.4; }' +
    '@keyframes imx-sway { 0%,100% { transform: rotate(0deg); } 50% { transform: rotate(2deg); } }' +

    /* ═══ FOOTER ═══════════════════════════════════════════ */
    '#imx-game-footer { margin-top: 3rem; padding: 2rem 1.25rem; border-top: 1px solid rgba(255,255,255,0.08); text-align: center; font-size: 0.8rem; color: #94A3B8; }' +
    'body.light-mode #imx-game-footer { border-top-color: #E7DDD0; }' +
    'body.light-mode #imx-game-footer, body.light-mode #imx-game-footer p { color: #92400E !important; }' +
    '.imx-gf-inner { max-width: 700px; margin: 0 auto; }' +
    '.imx-gf-divider { height: 2px; background: linear-gradient(90deg, transparent, #D97706 20%, #DC2626 40%, #EC4899 60%, #8B5CF6 80%, transparent); margin-bottom: 1.5rem; opacity: 0.3; border-radius: 1px; }' +
    'body.light-mode .imx-gf-divider { opacity: 0.5; }' +
    '.imx-gf-inner a { color: #F59E0B; text-decoration: none; }' +
    'body.light-mode .imx-gf-inner a { color: #B45309; }' +
    '.imx-gf-inner a:hover { text-decoration: underline; }' +
    '.imx-gf-links { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem 1rem; margin: 0.75rem 0; }' +
    '.imx-gf-copy { margin-top: 0.5rem; opacity: 0.6; }' +

    /* ═══ GAMIFICATION & VISUAL ENHANCEMENTS ═══════════════ */

    /* Button interactions */
    'button:not(.imx-theme-btn) { transition: all 0.2s ease; }' +
    'button:not(.imx-theme-btn):hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(245,158,11,0.2); }' +
    'button:not(.imx-theme-btn):active { transform: translateY(0) scale(0.97); }' +

    /* Animations */
    '@keyframes imx-celebrate { 0% { transform: scale(0.8) rotate(-3deg); opacity: 0; } 60% { transform: scale(1.08) rotate(1deg); } 100% { transform: scale(1) rotate(0); opacity: 1; } }' +
    '@keyframes imx-glow { 0%,100% { box-shadow: 0 0 8px rgba(245,158,11,0.3); } 50% { box-shadow: 0 0 24px rgba(245,158,11,0.5); } }' +
    '@keyframes imx-confetti { 0% { opacity: 1; transform: translateY(0) rotate(0); } 100% { opacity: 0; transform: translateY(-60px) rotate(360deg); } }' +

    /* Cards — warmer borders, more depth */
    '[class*="card"], .card { transition: all 0.25s ease; border-radius: 12px !important; }' +
    '[class*="card"]:hover, .card:hover { transform: translateY(-3px); box-shadow: 0 8px 30px rgba(0,0,0,0.2); }' +
    'body.light-mode [class*="card"]:hover, body.light-mode .card:hover { box-shadow: 0 8px 30px rgba(139,90,43,0.12); }' +

    /* Choice cards — distinct warm colors */
    '.choice-card:nth-child(1), [class*="option"]:nth-child(1) { border-left: 4px solid #D97706 !important; }' +
    '.choice-card:nth-child(2), [class*="option"]:nth-child(2) { border-left: 4px solid #059669 !important; }' +
    '.choice-card:nth-child(3), [class*="option"]:nth-child(3) { border-left: 4px solid #DC2626 !important; }' +
    '.choice-card:nth-child(4), [class*="option"]:nth-child(4) { border-left: 4px solid #7C3AED !important; }' +

    /* Agent/opponent — indigo accent */
    '.agent-card, [class*="agent"], [class*="opponent"] { border-left: 4px solid #6366F1 !important; }' +

    /* Results — celebration pop */
    '.result, [class*="result"], [class*="outcome"] { animation: imx-celebrate 0.5s ease-out; }' +

    /* Scores — golden emphasis */
    '.score, [class*="score"], [class*="points"], [class*="payoff"] { font-weight: 700; font-size: 1.15em; color: #F59E0B !important; }' +
    'body.light-mode .score, body.light-mode [class*="score"], body.light-mode [class*="points"], body.light-mode [class*="payoff"] { color: #B45309 !important; }' +

    /* Progress bars — warm gradient */
    '.progress-fill, [class*="progress-fill"], [class*="bar-fill"] { background: linear-gradient(90deg, #D97706, #059669) !important; border-radius: 999px; transition: width 0.6s ease; }' +

    /* Welcome/title — folk art inspired gradient */
    '.welcome-title, .game-title { background: linear-gradient(135deg, #D97706, #DC2626, #EC4899, #7C3AED); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }' +
    'body.light-mode .welcome-title, body.light-mode .game-title { background: linear-gradient(135deg, #92400E, #991B1B, #BE185D, #5B21B6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }' +

    /* CTA buttons — warm gradient */
    '.btn-primary, .start-btn, [class*="start"], [class*="play"], [class*="begin"] { background: linear-gradient(135deg, #D97706, #B45309) !important; color: #FFFFFF !important; border: none !important; box-shadow: 0 4px 15px rgba(217,119,6,0.3); }' +
    '.btn-primary:hover, .start-btn:hover, [class*="start"]:hover, [class*="play"]:hover, [class*="begin"]:hover { background: linear-gradient(135deg, #F59E0B, #D97706) !important; box-shadow: 0 6px 20px rgba(245,158,11,0.4); }' +

    /* ═══ MOBILE ═══════════════════════════════════════════ */
    '@media (max-width: 640px) {' +
      '#imx-game-header { padding: 0.4rem 0.75rem; }' +
      '.imx-gh-logo span { font-size: 0.9rem; }' +
      '.imx-gh-link { display: none; }' +
      '.imx-game-plane { width: 60px; height: 60px; top: 8%; right: 3%; }' +
      '.imx-motif-warli { width: 180px; height: 120px; opacity: 0.5; }' +
      '.imx-motif-madhubani { width: 30px; height: 180px; opacity: 0.5; }' +
      '.imx-motif-gond { width: 80px; height: 100px; opacity: 0.4; }' +
      '.imx-theme-btn { width: 28px; height: 28px; }' +
      '.imx-theme-btn svg { width: 14px; height: 14px; }' +
    '}';
  document.head.appendChild(css);
})();
