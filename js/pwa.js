// ImpactMojo — PWA cleanup
// Unregisters any existing service worker so users get fresh files from Netlify CDN.
(function () {
  'use strict';
  if (!('serviceWorker' in navigator)) return;

  navigator.serviceWorker.getRegistrations().then(function (registrations) {
    registrations.forEach(function (reg) {
      reg.unregister().then(function () {
        console.log('ImpactMojo SW unregistered');
      });
    });
  });

  // Clear all caches left behind by old service worker
  if ('caches' in window) {
    caches.keys().then(function (keys) {
      keys.forEach(function (key) { caches.delete(key); });
    });
  }
})();
