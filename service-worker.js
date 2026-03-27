// Service Worker for ImpactMojo PWA
// v5 - Offline PWA support for flagship courses, shell caching, offline fallback
const CACHE_NAME = 'impactmojo-v8';
const COURSE_CACHE_PREFIX = 'impactmojo-course-';

// App shell: core assets cached on install
// NOTE: auth.js, config.js, state-manager.js are NOT in SHELL_ASSETS
// because they use stale-while-revalidate instead — cache-first causes
// stale auth code to persist across deploys, breaking login.
const SHELL_ASSETS = [
  '/',
  '/index.html',
  '/offline.html',
  '/manifest.json',
  '/js/pwa.js',
  '/js/offline.js',
  '/js/router.js',
  '/js/search.js',
  '/js/cookie-ui.js',
  '/js/learning-tracks.js',
  '/js/faq-bank.js',
  '/js/bookmarks-compare.js',
  '/js/premium.js',
  '/js/translate.js',
  '/js/resource-launch.js',
  '/js/mobile-ui.js',
  '/js/course-progress.js',
  '/assets/images/favicon.ico',
  '/assets/images/favicon.png',
  '/assets/images/favicon-16x16.png',
  '/assets/images/favicon-32x32.png',
  '/assets/images/apple-touch-icon.png',
  '/assets/images/android-chrome-192x192.png',
  '/assets/images/android-chrome-512x512.png'
];

// Flagship course definitions
const FLAGSHIP_COURSES = [
  'gandhi', 'devecon', 'devai', 'dataviz',
  'mel', 'poa', 'media', 'law', 'SEL'
];

// Course page URLs to pre-cache
const COURSE_PAGES = FLAGSHIP_COURSES.map(id => `/courses/${id}/index.html`);

// Get all URLs that need caching for a given course (on-demand download)
function getCourseURLs(courseId) {
  const base = `/courses/${courseId}/`;
  return [
    base,
    `${base}index.html`,
    `${base}lexicon.html`
  ];
}

// Get the cache name for a specific course
function getCourseCacheName(courseId) {
  return `${COURSE_CACHE_PREFIX}${courseId}`;
}

// Install - cache app shell + flagship course pages
self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      // Cache shell assets first, then course pages (non-blocking failures)
      return cache.addAll(SHELL_ASSETS).then(() => {
        // Cache course pages individually so one failure doesn't break install
        return Promise.allSettled(
          COURSE_PAGES.map(url =>
            fetch(url).then(resp => {
              if (resp.ok) return cache.put(url, resp);
            }).catch(() => {})
          )
        );
      });
    }).catch(err => console.log('SW: install cache error', err))
  );
});

// Activate - clean up old caches (preserve individual course download caches)
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(names =>
      Promise.all(
        names
          .filter(n => n !== CACHE_NAME && !n.startsWith(COURSE_CACHE_PREFIX))
          .map(n => caches.delete(n))
      )
    ).then(() => self.clients.claim())
  );
});

// Fetch strategy:
// - Cached shell/course assets: cache-first (fast offline)
// - Other HTML pages: network-first (fresh content, fallback to cache/offline.html)
// - Other JS/CSS/images: stale-while-revalidate
// - API/Supabase calls: network-only (never cache)
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // Skip non-GET, cross-origin, and Supabase/API calls
  if (event.request.method !== 'GET' || url.origin !== self.location.origin) {
    return;
  }

  const pathname = url.pathname;
  const isHTML = event.request.headers.get('accept')?.includes('text/html') ||
                 pathname.endsWith('.html') || pathname === '/';

  // Check if this URL is part of the pre-cached shell or course pages
  const isShellAsset = SHELL_ASSETS.includes(pathname);
  const isCoursePage = COURSE_PAGES.includes(pathname) ||
                       FLAGSHIP_COURSES.some(id => pathname === `/courses/${id}/`);

  if (isShellAsset || isCoursePage) {
    // Cache-first for shell assets and pre-cached course pages
    event.respondWith(
      caches.match(event.request).then(cached => {
        if (cached) {
          // Return cache immediately, update in background
          const fetchPromise = fetch(event.request).then(response => {
            if (response.ok) {
              caches.open(CACHE_NAME).then(cache => cache.put(event.request, response));
            }
          }).catch(() => {});
          fetchPromise; // fire-and-forget
          return cached;
        }
        // Not in cache yet - fetch and cache
        return fetch(event.request).then(response => {
          if (response.ok) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
          }
          return response;
        }).catch(() => {
          if (isHTML) return caches.match('/offline.html');
          return new Response('', { status: 503 });
        });
      })
    );
  } else if (isHTML) {
    // Network-first for other HTML pages
    event.respondWith(
      fetch(event.request)
        .then(response => {
          if (response.ok) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
          }
          return response;
        })
        .catch(() => {
          notifyClients({ type: 'OFFLINE_DETECTED' });
          return caches.match(event.request)
            .then(cached => {
              if (cached) return cached;
              // Check course download caches as fallback
              return caches.keys().then(names => {
                const courseCaches = names.filter(n => n.startsWith(COURSE_CACHE_PREFIX));
                return courseCaches.reduce((promise, cacheName) =>
                  promise.then(result => result || caches.open(cacheName).then(c => c.match(event.request))),
                  Promise.resolve(null)
                );
              }).then(result => result || caches.match('/offline.html'));
            });
        })
    );
  } else {
    // Stale-while-revalidate for other assets (JS, CSS, images, fonts)
    event.respondWith(
      caches.match(event.request).then(cached => {
        const fetchPromise = fetch(event.request).then(response => {
          if (response && response.ok) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
          }
          return response;
        }).catch(() => {
          if (cached) return cached;
          // Check course caches as fallback for assets
          return caches.keys().then(names => {
            const courseCaches = names.filter(n => n.startsWith(COURSE_CACHE_PREFIX));
            return courseCaches.reduce((promise, cacheName) =>
              promise.then(result => result || caches.open(cacheName).then(c => c.match(event.request))),
              Promise.resolve(null)
            );
          });
        });

        return cached || fetchPromise;
      })
    );
  }
});

// ─── Message listener: "Download for Offline" flow ───
self.addEventListener('message', event => {
  if (event.data && event.data.type === 'CACHE_COURSE') {
    const courseId = event.data.courseId;
    if (!FLAGSHIP_COURSES.includes(courseId)) {
      notifyClients({ type: 'COURSE_CACHE_ERROR', courseId, error: 'Unknown course ID' });
      return;
    }
    event.waitUntil(cacheCourse(courseId));
  }

  if (event.data && event.data.type === 'CHECK_COURSE_CACHED') {
    const courseId = event.data.courseId;
    event.waitUntil(
      caches.has(getCourseCacheName(courseId)).then(exists => {
        notifyClients({ type: 'COURSE_CACHE_STATUS', courseId, cached: exists });
      })
    );
  }
});

// Cache all assets for a course (on-demand download)
async function cacheCourse(courseId) {
  const cacheName = getCourseCacheName(courseId);
  const urls = getCourseURLs(courseId);
  const total = urls.length;
  let completed = 0;

  try {
    const cache = await caches.open(cacheName);

    for (const url of urls) {
      try {
        const response = await fetch(url);
        if (response.ok) {
          await cache.put(url, response);
        }
      } catch (err) {
        console.warn(`SW: Failed to cache ${url}:`, err.message);
      }
      completed++;
      notifyClients({
        type: 'COURSE_CACHE_PROGRESS',
        courseId,
        progress: Math.round((completed / total) * 100),
        completed,
        total
      });
    }

    notifyClients({ type: 'COURSE_CACHE_COMPLETE', courseId });
  } catch (err) {
    console.error('SW: Course cache failed:', err);
    notifyClients({ type: 'COURSE_CACHE_ERROR', courseId, error: err.message });
  }
}

// ─── Background sync: retry queued progress data ───
self.addEventListener('sync', event => {
  if (event.tag === 'sync-progress') {
    event.waitUntil(syncProgress());
  }
});

async function syncProgress() {
  try {
    const db = await openDB();
    const tx = db.transaction('pendingSync', 'readwrite');
    const store = tx.objectStore('pendingSync');
    const request = store.getAll();

    return new Promise((resolve, reject) => {
      request.onsuccess = async () => {
        const items = request.result || [];
        for (const item of items) {
          try {
            await fetch(item.url, {
              method: item.method || 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(item.data)
            });
            store.delete(item.id);
          } catch (err) {
            console.warn('SW: Sync retry failed for', item.id);
          }
        }
        resolve();
      };
      request.onerror = () => resolve();
    });
  } catch (err) {
    console.log('SW: No pending sync data');
  }
}

function openDB() {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open('ImpactMojoOffline', 1);
    request.onupgradeneeded = () => {
      const db = request.result;
      if (!db.objectStoreNames.contains('pendingSync')) {
        db.createObjectStore('pendingSync', { keyPath: 'id', autoIncrement: true });
      }
    };
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

// ─── Notify all clients ───
function notifyClients(message) {
  self.clients.matchAll({ type: 'window', includeUncontrolled: false }).then(clients => {
    clients.forEach(client => client.postMessage(message));
  });
}
