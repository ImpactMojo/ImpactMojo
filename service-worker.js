// Service Worker for ImpactMojo PWA
const CACHE_NAME = 'impactmojo-v2';
const urlsToCache = [
  '/',
  '/index.html',
  '/manifest.json',
  '/js/auth.js',
  '/js/premium.js',
  '/js/router.js',
  '/js/resource-launch.js',
  '/js/bookmarks-compare.js',
  '/js/faq-bank.js',
  '/js/mobile-ui.js',
  '/js/learning-tracks.js',
  '/js/cookie-ui.js',
  '/assets/images/favicon.ico',
  '/assets/images/favicon-16x16.png',
  '/assets/images/favicon-32x32.png',
  '/assets/images/apple-touch-icon.png',
  '/assets/images/varna-photo.jpg'
];

// Install Service Worker
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
      .catch(err => console.log('Error caching files:', err))
  );
});

// Fetch event - stale-while-revalidate for own assets, network-first for API
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // Skip non-GET and cross-origin API calls
  if (event.request.method !== 'GET' || url.origin !== self.location.origin) {
    return;
  }

  event.respondWith(
    caches.match(event.request).then(cached => {
      // Fetch fresh copy in background
      const fetchPromise = fetch(event.request).then(response => {
        if (response && response.status === 200 && response.type === 'basic') {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
        }
        return response;
      }).catch(() => cached || caches.match('/index.html'));

      // Return cached immediately if available, otherwise wait for network
      return cached || fetchPromise;
    })
  );
});

// Activate Service Worker - Clean up old caches
self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];

  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
