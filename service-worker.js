// Service Worker for ImpactMojo PWA
// v4 - Offline course support, background sync, offline indicator
const CACHE_NAME = 'impactmojo-v4';
const COURSE_CACHE_PREFIX = 'impactmojo-course-';
const STATIC_ASSETS = [
  '/manifest.json',
  '/assets/images/favicon.ico',
  '/assets/images/favicon-16x16.png',
  '/assets/images/favicon-32x32.png',
  '/assets/images/apple-touch-icon.png',
  '/assets/images/varna-photo.jpg'
];

// Flagship course definitions
const FLAGSHIP_COURSES = [
  'gandhi', 'devecon', 'devai', 'dataviz',
  'mel', 'poa', 'media', 'law', 'SEL'
];

// Get all URLs that need caching for a given course
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

// Install - cache only static assets (fonts, icons)
self.addEventListener('install', event => {
  self.skipWaiting(); // Activate immediately on update
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(STATIC_ASSETS))
      .catch(err => console.log('SW: cache error', err))
  );
});

// Activate - clean up old caches (preserve course caches)
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(names =>
      Promise.all(
        names
          .filter(n => n !== CACHE_NAME && !n.startsWith(COURSE_CACHE_PREFIX))
          .map(n => caches.delete(n))
      )
    ).then(() => self.clients.claim()) // Take control of all pages
  );
});

// Fetch strategy:
// - HTML pages: network-first (fall back to cache only when offline)
// - JS/CSS/images: stale-while-revalidate (fast + stays fresh)
// - API/Supabase calls: network-only (never cache)
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // Skip non-GET, cross-origin, and Supabase/API calls
  if (event.request.method !== 'GET' || url.origin !== self.location.origin) {
    return;
  }

  const isHTML = event.request.headers.get('accept')?.includes('text/html') ||
                 url.pathname.endsWith('.html') || url.pathname === '/';

  if (isHTML) {
    // Network-first for HTML — always get fresh content, fall back to course cache
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
              // Check course caches as fallback
              return caches.keys().then(names => {
                const courseCaches = names.filter(n => n.startsWith(COURSE_CACHE_PREFIX));
                return courseCaches.reduce((promise, cacheName) =>
                  promise.then(result => result || caches.open(cacheName).then(c => c.match(event.request))),
                  Promise.resolve(null)
                );
              }).then(result => result || caches.match('/index.html'));
            });
        })
    );
  } else {
    // Stale-while-revalidate for assets (JS, CSS, images, fonts)
    // Also check course caches for offline asset serving
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

// Cache all assets for a course
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
    // Open IndexedDB to check for queued progress data
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
      request.onerror = () => resolve(); // Don't block on DB errors
    });
  } catch (err) {
    // IndexedDB not available or no pending data — that's fine
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

// ─── Offline indicator: notify clients of connectivity changes ───
function notifyClients(message) {
  self.clients.matchAll({ type: 'window', includeUncontrolled: false }).then(clients => {
    clients.forEach(client => client.postMessage(message));
  });
}

// Periodic offline check — notify clients when a navigation fetch fails
// (Integrated into the main fetch handler's .catch paths above rather than
//  duplicating requests. Client-side navigator.onLine events handle the rest.)
