// ImpactMojo Offline Module
// Provides course download, cache checking, and offline/online status indicators
(function () {
  'use strict';

  const COURSE_CACHE_PREFIX = 'impactmojo-course-';

  const FLAGSHIP_COURSES = [
    'gandhi', 'devecon', 'devai', 'dataviz',
    'mel', 'poa', 'media', 'law', 'sel',
    'gender', 'pubchoice', 'pubpol', 'causal', 'livelihoods', 'powerBI',
    'intervention', 'nothing-about-us', 'nvc-rj', 'esg', 'gender-mel',
    'social-protection', 'social-movements'
  ];

  // ─── Toast notification helper ───
  function showToast(message, type) {
    type = type || 'info';
    // Remove existing toast if present
    const existing = document.getElementById('impactmojo-offline-toast');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.id = 'impactmojo-offline-toast';
    if (type !== 'progress') toast.setAttribute('role', type === 'error' ? 'alert' : 'status');
    toast.textContent = message;

    // Each clears 4.5:1 under white text (#1287).
    const colors = {
      info: '#0369A1',
      success: '#047857',
      error: '#B91C1C',
      warning: '#92400E',
      progress: '#4F46E5'
    };

    Object.assign(toast.style, {
      position: 'fixed',
      bottom: '20px',
      left: '50%',
      transform: 'translateX(-50%)',
      background: colors[type] || colors.info,
      color: '#fff',
      padding: '12px 24px',
      borderRadius: '8px',
      fontSize: '14px',
      fontWeight: '500',
      zIndex: '99999',
      boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
      transition: 'opacity 0.3s ease',
      maxWidth: '90vw',
      textAlign: 'center'
    });

    document.body.appendChild(toast);

    // Auto-dismiss after 4 seconds (except progress)
    if (type !== 'progress') {
      setTimeout(function () {
        toast.style.opacity = '0';
        setTimeout(function () { toast.remove(); }, 300);
      }, 4000);
    }
  }

  // ─── Offline/Online status indicator ───
  function createStatusIndicator() {
    const indicator = document.createElement('div');
    indicator.id = 'impactmojo-offline-indicator';
    Object.assign(indicator.style, {
      position: 'fixed',
      top: '10px',
      right: '10px',
      padding: '6px 14px',
      borderRadius: '20px',
      fontSize: '12px',
      fontWeight: '600',
      zIndex: '99998',
      transition: 'opacity 0.3s ease, transform 0.3s ease',
      pointerEvents: 'none'
    });
    document.body.appendChild(indicator);
    return indicator;
  }

  function updateStatusIndicator(online) {
    var indicator = document.getElementById('impactmojo-offline-indicator');
    if (!indicator) indicator = createStatusIndicator();

    if (online) {
      indicator.textContent = 'Online';
      indicator.style.background = '#047857';
      indicator.style.color = '#fff';
      indicator.style.opacity = '1';
      // Fade out after 2 seconds when online
      setTimeout(function () { indicator.style.opacity = '0'; }, 2000);
    } else {
      indicator.textContent = 'Offline';
      indicator.style.background = '#B91C1C';
      indicator.style.color = '#fff';
      indicator.style.opacity = '1';
    }
  }

  // ─── Initialize online/offline listeners ───
  function initStatusListeners() {
    window.addEventListener('online', function () {
      updateStatusIndicator(true);
      showToast('You are back online', 'success');
    });

    window.addEventListener('offline', function () {
      updateStatusIndicator(false);
      showToast('You are offline. Downloaded courses are still available.', 'warning');
    });

    // Listen for SW messages
    if (navigator.serviceWorker) {
      navigator.serviceWorker.addEventListener('message', function (event) {
        var data = event.data;
        if (!data) return;

        switch (data.type) {
          case 'COURSE_CACHE_PROGRESS':
            showToast('Saving for offline: ' + data.progress + '% (' + data.completed + ' of ' + data.total + ' files)', 'progress');
            break;
          case 'COURSE_CACHE_COMPLETE':
            showToast('Saved. This course now opens without a connection.', 'success');
            break;
          case 'COURSE_CACHE_ERROR':
            showToast('Download failed: ' + (data.error || 'Unknown error'), 'error');
            break;
          case 'OFFLINE_DETECTED':
            updateStatusIndicator(false);
            break;
        }
      });
    }

    // Set initial state
    if (!navigator.onLine) {
      updateStatusIndicator(false);
    }
  }

  // ─── Download a course for offline use ───
  function downloadCourse(courseId) {
    if (!FLAGSHIP_COURSES.includes(courseId)) {
      showToast('This course cannot be saved for offline yet.', 'error');
      return Promise.reject(new Error('Unknown course ID: ' + courseId));
    }

    if (!navigator.serviceWorker || !navigator.serviceWorker.controller) {
      showToast('Offline saving is not ready yet. Reload the page and try again.', 'error');
      return Promise.reject(new Error('Service worker not active'));
    }

    showToast('Saving this course for offline reading...', 'info');
    navigator.serviceWorker.controller.postMessage({
      type: 'CACHE_COURSE',
      courseId: courseId,
      urls: pageAssetUrls()
    });

    return Promise.resolve(true);
  }

  // The same-origin files this page actually loaded, as path plus query, so the
  // worker caches the stamped addresses the page will ask for offline (#1287).
  function pageAssetUrls() {
    var out = [location.pathname + location.search];
    try {
      performance.getEntriesByType('resource').forEach(function (e) {
        var u = new URL(e.name);
        if (u.origin === location.origin) out.push(u.pathname + u.search);
      });
    } catch (err) {}
    return out;
  }

  // Which flagship course this page is the entry page of, if any.
  function currentCourseId() {
    var m = /^\/courses\/([^\/]+)\/(?:index\.html|powerbi\.html)?$/i.exec(location.pathname);
    if (!m) return null;
    var dir = m[1].toLowerCase();
    for (var i = 0; i < FLAGSHIP_COURSES.length; i++) {
      if (FLAGSHIP_COURSES[i].toLowerCase() === dir) return FLAGSHIP_COURSES[i];
    }
    return null;
  }

  // A save/remove control under the course's Start button.
  function addSaveControl() {
    var id = currentCourseId();
    var start = document.querySelector('.ch-hero .ch-start');
    if (!id || !start || !('serviceWorker' in navigator) || !('caches' in window)) return;
    var css = document.createElement('style');
    css.textContent = '.im-offline{display:flex;flex-wrap:wrap;align-items:center;gap:6px 12px;margin:12px 0 0;font:500 13.5px/1.4 Inter,Helvetica,Arial,sans-serif;color:var(--ch-muted,#4B5563)}' +
      '.im-offline button{font:600 13.5px/1.2 Inter,Helvetica,Arial,sans-serif;color:var(--ch-link,#0369A1);background:none;border:1px solid var(--ch-line-strong,#C9CED6);border-radius:999px;padding:8px 14px;min-height:40px;cursor:pointer}' +
      '.im-offline button:hover{border-color:var(--ch-link,#0369A1)}' +
      '.im-offline button:focus-visible{outline:2px solid var(--ch-link,#0369A1);outline-offset:2px}';
    document.head.appendChild(css);
    var box = document.createElement('div');
    box.className = 'im-offline';
    var btn = document.createElement('button');
    btn.type = 'button';
    var note = document.createElement('span');
    box.appendChild(btn);
    box.appendChild(note);
    start.insertAdjacentElement('afterend', box);
    function show(saved) {
      btn.textContent = saved ? 'Remove offline copy' : 'Save for offline';
      btn.setAttribute('aria-pressed', saved ? 'true' : 'false');
      note.textContent = saved ? 'Saved on this device. It opens without a connection.' : 'Keep a copy on this device for areas with no signal.';
    }
    isCourseCached(id).then(show);
    btn.addEventListener('click', function () {
      isCourseCached(id).then(function (saved) {
        if (saved) { removeCourse(id).then(function () { show(false); }); return; }
        downloadCourse(id).catch(function () {});
      });
    });
    if (navigator.serviceWorker) {
      navigator.serviceWorker.addEventListener('message', function (event) {
        var d = event.data || {};
        if (d.type === 'COURSE_CACHE_COMPLETE' && d.courseId === id) show(true);
      });
    }
  }

  // ─── Check if a course is cached ───
  function isCourseCached(courseId) {
    if (!('caches' in window)) {
      return Promise.resolve(false);
    }
    var cacheName = COURSE_CACHE_PREFIX + courseId;
    return caches.has(cacheName);
  }

  // ─── Remove a cached course ───
  function removeCourse(courseId) {
    if (!('caches' in window)) {
      return Promise.resolve(false);
    }
    var cacheName = COURSE_CACHE_PREFIX + courseId;
    return caches.delete(cacheName).then(function (deleted) {
      if (deleted) {
        showToast('The offline copy of this course was removed.', 'info');
      }
      return deleted;
    });
  }

  // ─── List all cached courses ───
  function listCachedCourses() {
    if (!('caches' in window)) {
      return Promise.resolve([]);
    }
    return caches.keys().then(function (names) {
      return names
        .filter(function (n) { return n.startsWith(COURSE_CACHE_PREFIX); })
        .map(function (n) { return n.replace(COURSE_CACHE_PREFIX, ''); });
    });
  }

  // ─── Queue progress data for background sync ───
  function queueProgressSync(url, data) {
    return openDB().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction('pendingSync', 'readwrite');
        var store = tx.objectStore('pendingSync');
        store.add({ url: url, method: 'POST', data: data, timestamp: Date.now() });
        tx.oncomplete = function () {
          // Request background sync
          if (navigator.serviceWorker && navigator.serviceWorker.ready) {
            navigator.serviceWorker.ready.then(function (reg) {
              if (reg.sync) {
                return reg.sync.register('sync-progress');
              }
            }).catch(function () {
              // Background sync not supported — will retry on next load
            });
          }
          resolve(true);
        };
        tx.onerror = function () { reject(tx.error); };
      });
    });
  }

  function openDB() {
    return new Promise(function (resolve, reject) {
      var request = indexedDB.open('ImpactMojoOffline', 1);
      request.onupgradeneeded = function () {
        var db = request.result;
        if (!db.objectStoreNames.contains('pendingSync')) {
          db.createObjectStore('pendingSync', { keyPath: 'id', autoIncrement: true });
        }
      };
      request.onsuccess = function () { resolve(request.result); };
      request.onerror = function () { reject(request.error); };
    });
  }

  // ─── Initialize on DOM ready ───
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { initStatusListeners(); addSaveControl(); });
  } else {
    initStatusListeners();
    addSaveControl();
  }

  // ─── Export globally ───
  window.ImpactMojoOffline = {
    downloadCourse: downloadCourse,
    isCourseCached: isCourseCached,
    removeCourse: removeCourse,
    listCachedCourses: listCachedCourses,
    queueProgressSync: queueProgressSync,
    FLAGSHIP_COURSES: FLAGSHIP_COURSES
  };

})();
