/**
 * ImpactLex service worker.
 *
 * Strategy:
 *   - App shell (html/css/js) → stale-while-revalidate
 *   - Seed snapshot JSON → stale-while-revalidate (so the app opens fast offline
 *     but refreshes when network is available)
 *   - Everything else → network-first with cache fallback
 */

const VERSION = 'impactlex-v2';
const SHELL_CACHE = `${VERSION}-shell`;
const DATA_CACHE = `${VERSION}-data`;

const SHELL_URLS = [
  '/impactlex/',
  '/impactlex/index.html',
  '/impactlex/app.js',
  '/impactlex/config.js',
  '/impactlex/styles.css',
  '/impactlex/manifest.webmanifest',
  '/impactlex/data/seed-snapshot.json',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(SHELL_CACHE).then((cache) => cache.addAll(SHELL_URLS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => !k.startsWith(VERSION)).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  if (!url.pathname.startsWith('/impactlex/') && url.pathname !== '/assets/images/ImpactMojo%20Logo.png' && !url.pathname.startsWith('/assets/images/favicon') && !url.pathname.startsWith('/assets/images/apple-touch-icon')) return;

  const cacheName = url.pathname.endsWith('.json') ? DATA_CACHE : SHELL_CACHE;

  event.respondWith(
    caches.open(cacheName).then((cache) =>
      cache.match(req).then((cached) => {
        const networkPromise = fetch(req).then((res) => {
          if (res && res.status === 200 && res.type === 'basic') cache.put(req, res.clone());
          return res;
        }).catch(() => cached);
        return cached || networkPromise;
      })
    )
  );
});
