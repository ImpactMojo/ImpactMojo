/* ============================================================
   ImpactMojo 101 Series — Shared Slide Deck Engine
   Handles navigation, scaling, themes, fullscreen, and chart
   initialisation. Each deck calls initDeck(config) with its
   own slide IDs and chart definitions.
   ============================================================ */

let cur = 0;
let SLIDE_IDS = [];
let TOTAL = 0;
const chartsInit = {};

// Chart.js shared defaults
const CHART_DEFAULTS = {
  responsive: true, maintainAspectRatio: false,
  plugins: { legend: { labels: { font: { family: 'JetBrains Mono', size: 10 }, color: '#78716C' } } },
  scales: {
    x: { ticks: { font: { family: 'JetBrains Mono', size: 9 }, color: '#78716C' }, grid: { color: 'rgba(0,0,0,0.05)' } },
    y: { ticks: { font: { family: 'JetBrains Mono', size: 9 }, color: '#78716C' }, grid: { color: 'rgba(0,0,0,0.05)' } }
  }
};

/** Helper: create a Chart.js chart on a canvas element */
function mkChart(canvasId, type, data, opts) {
  const el = document.getElementById(canvasId);
  if (!el) return null;
  return new Chart(el, { type, data, options: { ...CHART_DEFAULTS, ...opts } });
}

/** Show slide at index n */
function showSlide(n) {
  document.getElementById(SLIDE_IDS[cur])?.classList.remove('active');
  cur = Math.max(0, Math.min(n, TOTAL - 1));
  document.getElementById(SLIDE_IDS[cur])?.classList.add('active');
  document.getElementById('prog-text').textContent = (cur + 1) + ' / ' + TOTAL;
  document.getElementById('prevBtn').disabled = cur === 0;
  document.getElementById('nextBtn').disabled = cur === TOTAL - 1;
  document.getElementById('progress-bar').style.width = ((cur + 1) / TOTAL * 100) + '%';
  // Lazy-init charts
  if (!chartsInit[cur] && typeof initChart === 'function') {
    initChart(cur);
    chartsInit[cur] = true;
  }
}

/** Navigate by delta (+1 or -1) */
function changeSlide(d) { showSlide(cur + d); }

/** Keyboard navigation */
document.addEventListener('keydown', function(e) {
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') { e.preventDefault(); changeSlide(1); }
  if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') { e.preventDefault(); changeSlide(-1); }
  if (e.key === 'Home') { e.preventDefault(); showSlide(0); }
  if (e.key === 'End') { e.preventDefault(); showSlide(TOTAL - 1); }
});

/** Touch/swipe navigation */
let touchStartX = 0;
document.addEventListener('touchstart', function(e) { touchStartX = e.touches[0].clientX; });
document.addEventListener('touchend', function(e) {
  var d = touchStartX - e.changedTouches[0].clientX;
  if (Math.abs(d) > 50) changeSlide(d > 0 ? 1 : -1);
});

/** Fullscreen toggle */
function toggleFS() {
  if (!document.fullscreenElement) document.documentElement.requestFullscreen();
  else document.exitFullscreen();
}
document.addEventListener('fullscreenchange', function() {
  document.getElementById('fs-hint').textContent = document.fullscreenElement ? 'exit fullscreen' : 'fullscreen';
});

/** Viewport scaling — fit 1280x720 to any screen */
function scaleViewport() {
  var vp = document.getElementById('viewport');
  if (!vp) return;
  var s = Math.min(window.innerWidth / 1280, window.innerHeight / 720);
  vp.style.transform = 'scale(' + s + ')';
}
window.addEventListener('resize', scaleViewport);

/** Theme switcher */
function setTheme(t) {
  document.body.classList.remove('light', 'dark');
  if (t === 'light') document.body.classList.add('light');
  else if (t === 'dark') document.body.classList.add('dark');
  document.querySelectorAll('.theme-btn').forEach(function(b) {
    b.classList.toggle('active', b.textContent.trim().toLowerCase() === t);
  });
  try { localStorage.setItem('im-theme', t); } catch(e) {}
}

/** Initialise deck — called by each deck's inline script */
function initDeck(config) {
  SLIDE_IDS = config.slideIds;
  TOTAL = SLIDE_IDS.length;

  // Restore theme
  var saved = 'light';
  try { saved = localStorage.getItem('im-theme') || 'light'; } catch(e) {}
  setTheme(saved);

  // Scale and show first slide
  scaleViewport();
  showSlide(0);
}