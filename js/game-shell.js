/**
 * ImpactMojo Game Shell v2
 * Injects shared header, footer, theme system, paper plane, and visual
 * enhancements into all game pages.
 * Usage: <script src="/js/game-shell.js"></script> (at end of <body>)
 */
(function() {
  'use strict';

  // ── Theme System (System / Light / Dark) ──────────────────
  var THEME_KEY = 'imx_theme';
  var saved = localStorage.getItem(THEME_KEY); // 'light', 'dark', or null (system)

  function getSystemPref() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
  }

  function resolveTheme(pref) {
    if (pref === 'light') return 'light';
    if (pref === 'dark') return 'dark';
    return getSystemPref(); // system default
  }

  function applyTheme(pref) {
    var resolved = resolveTheme(pref);
    document.body.classList.toggle('light-mode', resolved === 'light');
    // Update button states
    document.querySelectorAll('.imx-theme-btn').forEach(function(btn) {
      btn.classList.toggle('active', btn.getAttribute('data-theme') === (pref || 'system'));
    });
  }

  function setTheme(pref) {
    if (pref === 'system' || !pref) {
      localStorage.removeItem(THEME_KEY);
    } else {
      localStorage.setItem(THEME_KEY, pref);
    }
    applyTheme(pref);
  }

  // Apply immediately
  applyTheme(saved);

  // Listen for system changes
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

  // Theme button handlers
  document.querySelectorAll('.imx-theme-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
      setTheme(btn.getAttribute('data-theme'));
    });
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
      '<circle cx="40" cy="155" r="2" fill="#0EA5E9" opacity="0.6"/>' +
      '<circle cx="35" cy="165" r="1.5" fill="#6366F1" opacity="0.4"/>' +
      '<circle cx="45" cy="170" r="1" fill="#10B981" opacity="0.5"/>' +
    '</svg>';
  document.body.appendChild(plane);

  // ── Indian Decorative Motifs ──────────────────────────────
  // Rangoli-inspired corner pattern (bottom-left)
  var rangoli = document.createElement('div');
  rangoli.className = 'imx-game-motif imx-motif-rangoli';
  rangoli.setAttribute('aria-hidden', 'true');
  rangoli.innerHTML =
    '<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">' +
      '<circle cx="100" cy="100" r="80" fill="none" stroke="#F59E0B" stroke-width="0.5" opacity="0.3"/>' +
      '<circle cx="100" cy="100" r="60" fill="none" stroke="#EF4444" stroke-width="0.5" opacity="0.25"/>' +
      '<circle cx="100" cy="100" r="40" fill="none" stroke="#EC4899" stroke-width="0.5" opacity="0.2"/>' +
      '<circle cx="100" cy="100" r="20" fill="none" stroke="#8B5CF6" stroke-width="1" opacity="0.3"/>' +
      // Petals
      '<ellipse cx="100" cy="40" rx="8" ry="20" fill="none" stroke="#F59E0B" stroke-width="0.8" opacity="0.2" transform="rotate(0,100,100)"/>' +
      '<ellipse cx="100" cy="40" rx="8" ry="20" fill="none" stroke="#F59E0B" stroke-width="0.8" opacity="0.2" transform="rotate(45,100,100)"/>' +
      '<ellipse cx="100" cy="40" rx="8" ry="20" fill="none" stroke="#F59E0B" stroke-width="0.8" opacity="0.2" transform="rotate(90,100,100)"/>' +
      '<ellipse cx="100" cy="40" rx="8" ry="20" fill="none" stroke="#F59E0B" stroke-width="0.8" opacity="0.2" transform="rotate(135,100,100)"/>' +
      '<ellipse cx="100" cy="40" rx="8" ry="20" fill="none" stroke="#F59E0B" stroke-width="0.8" opacity="0.2" transform="rotate(180,100,100)"/>' +
      '<ellipse cx="100" cy="40" rx="8" ry="20" fill="none" stroke="#F59E0B" stroke-width="0.8" opacity="0.2" transform="rotate(225,100,100)"/>' +
      '<ellipse cx="100" cy="40" rx="8" ry="20" fill="none" stroke="#F59E0B" stroke-width="0.8" opacity="0.2" transform="rotate(270,100,100)"/>' +
      '<ellipse cx="100" cy="40" rx="8" ry="20" fill="none" stroke="#F59E0B" stroke-width="0.8" opacity="0.2" transform="rotate(315,100,100)"/>' +
      // Dots at cardinal points
      '<circle cx="100" cy="10" r="3" fill="#EF4444" opacity="0.25"/>' +
      '<circle cx="190" cy="100" r="3" fill="#10B981" opacity="0.25"/>' +
      '<circle cx="100" cy="190" r="3" fill="#3B82F6" opacity="0.25"/>' +
      '<circle cx="10" cy="100" r="3" fill="#8B5CF6" opacity="0.25"/>' +
      // Inner dots
      '<circle cx="100" cy="100" r="4" fill="#F59E0B" opacity="0.3"/>' +
    '</svg>';
  document.body.appendChild(rangoli);

  // Lotus motif (top-left)
  var lotus = document.createElement('div');
  lotus.className = 'imx-game-motif imx-motif-lotus';
  lotus.setAttribute('aria-hidden', 'true');
  lotus.innerHTML =
    '<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">' +
      // Lotus petals
      '<path d="M60,90 Q60,50 40,30 Q60,45 60,90Z" fill="none" stroke="#EC4899" stroke-width="0.8" opacity="0.2"/>' +
      '<path d="M60,90 Q60,50 80,30 Q60,45 60,90Z" fill="none" stroke="#EC4899" stroke-width="0.8" opacity="0.2"/>' +
      '<path d="M60,90 Q45,55 25,50 Q50,55 60,90Z" fill="none" stroke="#F472B6" stroke-width="0.8" opacity="0.18"/>' +
      '<path d="M60,90 Q75,55 95,50 Q70,55 60,90Z" fill="none" stroke="#F472B6" stroke-width="0.8" opacity="0.18"/>' +
      '<path d="M60,90 Q35,65 15,70 Q40,65 60,90Z" fill="none" stroke="#FB923C" stroke-width="0.8" opacity="0.15"/>' +
      '<path d="M60,90 Q85,65 105,70 Q80,65 60,90Z" fill="none" stroke="#FB923C" stroke-width="0.8" opacity="0.15"/>' +
      // Center
      '<circle cx="60" cy="85" r="3" fill="#EC4899" opacity="0.25"/>' +
      // Water ripples
      '<ellipse cx="60" cy="100" rx="30" ry="5" fill="none" stroke="#3B82F6" stroke-width="0.5" opacity="0.15"/>' +
      '<ellipse cx="60" cy="105" rx="40" ry="5" fill="none" stroke="#3B82F6" stroke-width="0.4" opacity="0.1"/>' +
    '</svg>';
  document.body.appendChild(lotus);

  // ── Footer ─────────────────────────────────────────────────
  var footer = document.createElement('footer');
  footer.id = 'imx-game-footer';
  footer.innerHTML =
    '<div class="imx-gf-inner">' +
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

    /* ── Light mode overrides ──────────────────────────── */
    'body.light-mode { background: #F8FAFC !important; color: #1E293B !important; }' +
    'body.light-mode .card, body.light-mode [class*="card"] { background: #FFFFFF !important; border-color: #E2E8F0 !important; color: #1E293B !important; }' +
    'body.light-mode input, body.light-mode select, body.light-mode textarea { background: #F1F5F9 !important; color: #1E293B !important; border-color: #CBD5E1 !important; }' +
    'body.light-mode button:not(.imx-theme-btn) { color: #1E293B; }' +
    'body.light-mode h1, body.light-mode h2, body.light-mode h3, body.light-mode h4 { color: #0F172A !important; }' +
    'body.light-mode p, body.light-mode span, body.light-mode li, body.light-mode td, body.light-mode th, body.light-mode label, body.light-mode .text-muted, body.light-mode small { color: #334155 !important; }' +
    'body.light-mode a:not(.imx-gh-logo):not(.imx-gh-link):not(.imx-gf-inner a) { color: #2563EB !important; }' +
    'body.light-mode .container, body.light-mode .game-container, body.light-mode .content { color: #1E293B !important; }' +
    'body.light-mode table { border-color: #E2E8F0 !important; }' +
    'body.light-mode th { background: #F1F5F9 !important; color: #0F172A !important; }' +
    'body.light-mode td { color: #334155 !important; border-color: #E2E8F0 !important; }' +
    'body.light-mode .stats-bar, body.light-mode .stat-card, body.light-mode [class*="stat"] { background: #FFFFFF !important; border-color: #E2E8F0 !important; color: #1E293B !important; }' +
    'body.light-mode .progress-bar, body.light-mode [class*="progress"] { background: #E2E8F0 !important; }' +
    'body.light-mode .badge, body.light-mode [class*="badge"] { color: #1E293B !important; }' +
    'body.light-mode .hint, body.light-mode .tip, body.light-mode blockquote, body.light-mode .note { background: #F0F9FF !important; border-color: #BAE6FD !important; color: #0C4A6E !important; }' +

    /* ── Header ──────────────────────────────────────────── */
    '#imx-game-header {' +
      'position: sticky; top: 0; z-index: 999;' +
      'display: flex; align-items: center; justify-content: space-between;' +
      'padding: 0.5rem 1.25rem;' +
      'background: rgba(15,23,42,0.92); backdrop-filter: blur(12px);' +
      'border-bottom: 1px solid rgba(255,255,255,0.08);' +
    '}' +
    'body.light-mode #imx-game-header { background: rgba(248,250,252,0.95); border-bottom-color: #E2E8F0; }' +
    '.imx-gh-logo { display: flex; align-items: center; gap: 0.5rem; text-decoration: none; color: #F8FAFC; font-weight: 700; font-size: 1rem; }' +
    'body.light-mode .imx-gh-logo { color: #0F172A; }' +
    '.imx-gh-logo img { width: 32px; height: 32px; border-radius: 6px; }' +
    '.imx-gh-right { display: flex; align-items: center; gap: 0.75rem; }' +
    '.imx-gh-link { color: #94A3B8; text-decoration: none; font-size: 0.85rem; font-weight: 500; transition: color 0.2s; }' +
    '.imx-gh-link:hover { color: #0EA5E9; }' +
    'body.light-mode .imx-gh-link { color: #64748B; }' +

    /* ── Theme toggle group (3-way) ──────────────────────── */
    '.imx-gh-theme-group { display: flex; gap: 2px; background: rgba(255,255,255,0.08); border-radius: 8px; padding: 2px; }' +
    'body.light-mode .imx-gh-theme-group { background: #E2E8F0; }' +
    '.imx-theme-btn { background: none; border: none; border-radius: 6px; width: 32px; height: 32px; cursor: pointer; color: #94A3B8; display: flex; align-items: center; justify-content: center; transition: all 0.2s; }' +
    '.imx-theme-btn:hover { color: #E2E8F0; background: rgba(255,255,255,0.1); }' +
    '.imx-theme-btn.active { background: rgba(59,130,246,0.2); color: #3B82F6; }' +
    'body.light-mode .imx-theme-btn { color: #94A3B8; }' +
    'body.light-mode .imx-theme-btn:hover { color: #1E293B; background: rgba(0,0,0,0.05); }' +
    'body.light-mode .imx-theme-btn.active { background: rgba(59,130,246,0.15); color: #2563EB; }' +
    '.imx-theme-btn svg { stroke-linecap: round; stroke-linejoin: round; }' +

    /* ── Paper plane ──────────────────────────────────────── */
    '.imx-game-plane { position: fixed; top: 12%; right: 6%; width: 120px; height: 120px; opacity: 0.15; z-index: 0; pointer-events: none; animation: imx-fly 25s ease-in-out infinite; }' +
    'body.light-mode .imx-game-plane { opacity: 0.1; }' +
    '.imx-game-plane svg { width: 100%; height: 100%; }' +
    '@keyframes imx-fly { 0%,100% { transform: translate(0,0) rotate(0deg); } 20% { transform: translate(50px,-30px) rotate(10deg); } 40% { transform: translate(100px,20px) rotate(-6deg); } 60% { transform: translate(30px,50px) rotate(12deg); } 80% { transform: translate(-20px,15px) rotate(-4deg); } }' +

    /* ── Indian decorative motifs ─────────────────────────── */
    '.imx-game-motif { position: fixed; pointer-events: none; z-index: 0; }' +
    '.imx-motif-rangoli { bottom: 5%; left: 3%; width: 150px; height: 150px; animation: imx-spin-slow 60s linear infinite; }' +
    '.imx-motif-lotus { top: 15%; left: 5%; width: 100px; height: 100px; animation: imx-float 20s ease-in-out infinite; }' +
    '.imx-game-motif svg { width: 100%; height: 100%; }' +
    'body.light-mode .imx-motif-rangoli { opacity: 0.7; }' +
    'body.light-mode .imx-motif-lotus { opacity: 0.7; }' +
    '@keyframes imx-spin-slow { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }' +
    '@keyframes imx-float { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-15px); } }' +

    /* ── Footer ──────────────────────────────────────────── */
    '#imx-game-footer { margin-top: 3rem; padding: 2rem 1.25rem; border-top: 1px solid rgba(255,255,255,0.08); text-align: center; font-size: 0.8rem; color: #64748B; }' +
    'body.light-mode #imx-game-footer { border-top-color: #E2E8F0; }' +
    'body.light-mode #imx-game-footer, body.light-mode #imx-game-footer p { color: #94A3B8 !important; }' +
    '.imx-gf-inner { max-width: 700px; margin: 0 auto; }' +
    '.imx-gf-inner a { color: #0EA5E9; text-decoration: none; }' +
    '.imx-gf-inner a:hover { text-decoration: underline; }' +
    '.imx-gf-links { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem 1rem; margin: 0.75rem 0; }' +
    '.imx-gf-copy { margin-top: 0.5rem; opacity: 0.6; }' +

    /* ── Visual Enhancements (injected into all games) ──── */

    /* Colorful accents for interactive elements */
    'button:not(.imx-theme-btn):hover { transform: translateY(-1px); transition: all 0.2s ease; }' +
    'button:not(.imx-theme-btn):active { transform: translateY(0) scale(0.98); }' +

    /* Reward animation for outcomes */
    '@keyframes imx-celebrate { 0% { transform: scale(0.8); opacity: 0; } 50% { transform: scale(1.1); } 100% { transform: scale(1); opacity: 1; } }' +
    '@keyframes imx-shake { 0%,100% { transform: translateX(0); } 25% { transform: translateX(-4px); } 75% { transform: translateX(4px); } }' +
    '@keyframes imx-glow { 0%,100% { box-shadow: 0 0 8px rgba(59,130,246,0.3); } 50% { box-shadow: 0 0 20px rgba(59,130,246,0.6); } }' +

    /* Card hover effects */
    '[class*="card"]:hover, .card:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(0,0,0,0.15); transition: all 0.25s ease; }' +

    /* Colorful borders for different game elements */
    '.choice-card:nth-child(1), [class*="option"]:nth-child(1) { border-left: 3px solid #3B82F6 !important; }' +
    '.choice-card:nth-child(2), [class*="option"]:nth-child(2) { border-left: 3px solid #10B981 !important; }' +
    '.choice-card:nth-child(3), [class*="option"]:nth-child(3) { border-left: 3px solid #F59E0B !important; }' +
    '.choice-card:nth-child(4), [class*="option"]:nth-child(4) { border-left: 3px solid #8B5CF6 !important; }' +

    /* Agent/opponent visual distinction */
    '.agent-card, [class*="agent"], [class*="opponent"] { border-left: 3px solid #6366F1 !important; }' +

    /* Result/outcome emphasis */
    '.result, [class*="result"], [class*="outcome"] { animation: imx-celebrate 0.4s ease-out; }' +

    /* Score/points visual pop */
    '.score, [class*="score"], [class*="points"], [class*="payoff"] { font-weight: 700; font-size: 1.1em; }' +

    /* Progress bars - gradient */
    '.progress-fill, [class*="progress-fill"], [class*="bar-fill"] { background: linear-gradient(90deg, #3B82F6, #10B981) !important; border-radius: 999px; transition: width 0.6s ease; }' +

    /* Round indicators */
    '.round-indicator, [class*="round"] { font-weight: 600; }' +

    /* Welcome screen improvements */
    '.welcome-title, .game-title, [class*="title"]:first-of-type { background: linear-gradient(135deg, #3B82F6, #10B981, #6366F1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }' +
    'body.light-mode .welcome-title, body.light-mode .game-title { background: linear-gradient(135deg, #1D4ED8, #059669, #4F46E5); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }' +

    /* Mobile adjustments */
    '@media (max-width: 640px) {' +
      '#imx-game-header { padding: 0.4rem 0.75rem; }' +
      '.imx-gh-logo span { font-size: 0.9rem; }' +
      '.imx-gh-link { display: none; }' +
      '.imx-game-plane { width: 80px; height: 80px; top: 8%; right: 3%; }' +
      '.imx-motif-rangoli { width: 80px; height: 80px; bottom: 3%; left: 2%; }' +
      '.imx-motif-lotus { width: 60px; height: 60px; top: 10%; left: 2%; }' +
      '.imx-theme-btn { width: 28px; height: 28px; }' +
      '.imx-theme-btn svg { width: 14px; height: 14px; }' +
    '}';
  document.head.appendChild(css);
})();
