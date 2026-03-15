// ImpactMojo PWA - Service Worker Registration
// Registers the service worker and handles update notifications
(function () {
  'use strict';

  if (!('serviceWorker' in navigator)) return;

  window.addEventListener('load', function () {
    navigator.serviceWorker.register('/service-worker.js', { scope: '/' })
      .then(function (registration) {
        console.log('ImpactMojo SW registered, scope:', registration.scope);

        // Check for updates every 30 minutes
        setInterval(function () {
          registration.update();
        }, 30 * 60 * 1000);

        // Notify user when a new version is available
        registration.addEventListener('updatefound', function () {
          var newWorker = registration.installing;
          if (!newWorker) return;

          newWorker.addEventListener('statechange', function () {
            if (newWorker.state === 'activated' && navigator.serviceWorker.controller) {
              // New SW activated - optionally show a refresh prompt
              console.log('ImpactMojo SW updated. Refresh for latest version.');
            }
          });
        });
      })
      .catch(function (err) {
        console.log('ImpactMojo SW registration failed:', err);
      });
  });
})();
