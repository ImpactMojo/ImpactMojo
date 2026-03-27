// ImpactMojo — Service Worker removed.
// This file unregisters itself and clears all caches so existing
// users' browsers stop serving stale files.
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
    .then(() => self.clients.matchAll())
    .then(clients => {
      clients.forEach(client => client.postMessage({ type: 'SW_CLEARED' }));
    })
  );
  // Unregister this service worker
  self.registration.unregister();
});
