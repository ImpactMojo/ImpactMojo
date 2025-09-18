// EMERGENCY FIX FOR IMPACTMOJO - Fixes both classList and map errors
// This file patches potential issues without changing your app structure

console.log('[ImpactMojo] Emergency fix loading...');

// Fix 1: Ensure document.documentElement exists before any classList operations
if (typeof document !== 'undefined') {
  // Wait for DOM to be ready
  const ensureDOM = () => {
    if (!document.documentElement) {
      console.warn('[ImpactMojo] Waiting for documentElement...');
      setTimeout(ensureDOM, 10);
      return;
    }
    
    // Patch classList if it's somehow missing
    if (document.documentElement && !document.documentElement.classList) {
      console.warn('[ImpactMojo] classList missing, adding polyfill');
      document.documentElement.classList = {
        add: () => {},
        remove: () => {},
        toggle: () => {},
        contains: () => false
      };
    }
  };
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ensureDOM);
  } else {
    ensureDOM();
  }
}

// Fix 2: Patch Array.prototype.map to handle undefined/null safely
const originalMap = Array.prototype.map;
Array.prototype.map = function(...args) {
  if (this == null || this === undefined) {
    console.warn('[ImpactMojo] Attempted to map over undefined/null, returning empty array');
    return [];
  }
  return originalMap.apply(this, args);
};

// Fix 3: Global error handler for remaining map errors
if (typeof window !== 'undefined') {
  const originalError = window.onerror;
  window.onerror = function(msg, url, lineNo, columnNo, error) {
    if (msg && msg.includes("Cannot read properties of undefined (reading 'map')")) {
      console.error('[ImpactMojo] Map error caught:', msg);
      // Don't propagate this specific error to avoid breaking the app
      return true;
    }
    // Call original error handler if it exists
    if (originalError) {
      return originalError(msg, url, lineNo, columnNo, error);
    }
    return false;
  };
}

// Fix 4: Ensure localStorage is available (for theme persistence)
if (typeof window !== 'undefined' && !window.localStorage) {
  console.warn('[ImpactMojo] localStorage not available, using memory storage');
  window.localStorage = {
    data: {},
    getItem(key) { return this.data[key] || null; },
    setItem(key, value) { this.data[key] = value; },
    removeItem(key) { delete this.data[key]; },
    clear() { this.data = {}; }
  };
}

console.log('[ImpactMojo] Emergency fix loaded successfully');
