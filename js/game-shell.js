/**
 * ImpactMojo Game Shell
 * Injects shared header, footer, theme toggle, and paper plane into game pages.
 * Usage: <script src="/js/game-shell.js"></script> (at end of <body>)
 */
(function() {
  'use strict';

  // ── Theme ──────────────────────────────────────────────────
  var THEME_KEY = 'imx_theme';
  var saved = localStorage.getItem(THEME_KEY);
  if (saved === 'light') document.body.classList.add('light-mode');

  function toggleTheme() {
    var isLight = document.body.classList.toggle('light-mode');
    localStorage.setItem(THEME_KEY, isLight ? 'light' : 'dark');
    var btn = document.getElementById('imx-theme-btn');
    if (btn) btn.textContent = isLight ? '\u263E' : '\u2600';
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
      '<button id="imx-theme-btn" class="imx-gh-theme" aria-label="Toggle theme">' +
        (document.body.classList.contains('light-mode') ? '\u263E' : '\u2600') +
      '</button>' +
    '</div>';
  document.body.insertBefore(header, document.body.firstChild);
  document.getElementById('imx-theme-btn').addEventListener('click', toggleTheme);

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
    /* Light mode overrides */
    'body.light-mode { background: #F8FAFC !important; color: #1E293B !important; }' +
    'body.light-mode .card, body.light-mode [class*="card"] { background: #FFFFFF !important; border-color: #E2E8F0 !important; }' +
    'body.light-mode input, body.light-mode select, body.light-mode textarea { background: #F1F5F9 !important; color: #1E293B !important; border-color: #CBD5E1 !important; }' +
    'body.light-mode button { color: #1E293B; }' +
    'body.light-mode h1, body.light-mode h2, body.light-mode h3 { color: #0F172A !important; }' +

    /* Header */
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
    '.imx-gh-theme { background: none; border: 1px solid rgba(255,255,255,0.15); border-radius: 8px; width: 36px; height: 36px; font-size: 1.1rem; cursor: pointer; color: #F8FAFC; transition: all 0.2s; display: flex; align-items: center; justify-content: center; }' +
    '.imx-gh-theme:hover { background: rgba(255,255,255,0.1); }' +
    'body.light-mode .imx-gh-theme { border-color: #CBD5E1; color: #0F172A; }' +
    'body.light-mode .imx-gh-theme:hover { background: #F1F5F9; }' +

    /* Paper plane */
    '.imx-game-plane { position: fixed; top: 12%; right: 6%; width: 120px; height: 120px; opacity: 0.15; z-index: 0; pointer-events: none; animation: imx-fly 25s ease-in-out infinite; }' +
    'body.light-mode .imx-game-plane { opacity: 0.12; }' +
    '.imx-game-plane svg { width: 100%; height: 100%; }' +
    '@keyframes imx-fly { 0%,100% { transform: translate(0,0) rotate(0deg); } 20% { transform: translate(50px,-30px) rotate(10deg); } 40% { transform: translate(100px,20px) rotate(-6deg); } 60% { transform: translate(30px,50px) rotate(12deg); } 80% { transform: translate(-20px,15px) rotate(-4deg); } }' +

    /* Footer */
    '#imx-game-footer { margin-top: 3rem; padding: 2rem 1.25rem; border-top: 1px solid rgba(255,255,255,0.08); text-align: center; font-size: 0.8rem; color: #64748B; }' +
    'body.light-mode #imx-game-footer { border-top-color: #E2E8F0; }' +
    '.imx-gf-inner { max-width: 700px; margin: 0 auto; }' +
    '.imx-gf-inner a { color: #0EA5E9; text-decoration: none; }' +
    '.imx-gf-inner a:hover { text-decoration: underline; }' +
    '.imx-gf-links { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem 1rem; margin: 0.75rem 0; }' +
    '.imx-gf-copy { margin-top: 0.5rem; opacity: 0.6; }' +

    /* Mobile adjustments */
    '@media (max-width: 640px) {' +
      '#imx-game-header { padding: 0.4rem 0.75rem; }' +
      '.imx-gh-logo span { font-size: 0.9rem; }' +
      '.imx-gh-link { display: none; }' +
      '.imx-game-plane { width: 80px; height: 80px; top: 8%; right: 3%; }' +
    '}';
  document.head.appendChild(css);
})();
