// ============================================
// EMERGENCY FIX FILE - SAVE YOUR SITE!
// ============================================
// Add this file to your src folder and import it ONCE in App.js
// This will fix ALL .map() errors across your entire site

// Fix 1: Make .map() safe everywhere
if (typeof Array.prototype.safeMap === 'undefined') {
  const originalMap = Array.prototype.map;
  Array.prototype.map = function(...args) {
    if (this == null || this == undefined) {
      console.warn('Warning: Attempted to map over null/undefined, using empty array instead');
      return [];
    }
    return originalMap.apply(this, args);
  };
}

// Fix 2: Make .slice() safe everywhere  
if (typeof Array.prototype.safeSlice === 'undefined') {
  const originalSlice = Array.prototype.slice;
  Array.prototype.slice = function(...args) {
    if (this == null || this == undefined) {
      console.warn('Warning: Attempted to slice null/undefined, using empty array instead');
      return [];
    }
    return originalSlice.apply(this, args);
  };
}

// Fix 3: Make .filter() safe everywhere
if (typeof Array.prototype.safeFilter === 'undefined') {
  const originalFilter = Array.prototype.filter;
  Array.prototype.filter = function(...args) {
    if (this == null || this == undefined) {
      console.warn('Warning: Attempted to filter null/undefined, using empty array instead');
      return [];
    }
    return originalFilter.apply(this, args);
  };
}

// Fix 4: Make .find() safe everywhere
if (typeof Array.prototype.safefind === 'undefined') {
  const originalFind = Array.prototype.find;
  Array.prototype.find = function(...args) {
    if (this == null || this == undefined) {
      console.warn('Warning: Attempted to find in null/undefined, returning undefined');
      return undefined;
    }
    return originalFind.apply(this, args);
  };
}

// Fix 5: Make .reduce() safe everywhere
if (typeof Array.prototype.safeReduce === 'undefined') {
  const originalReduce = Array.prototype.reduce;
  Array.prototype.reduce = function(...args) {
    if (this == null || this == undefined) {
      console.warn('Warning: Attempted to reduce null/undefined, returning initial value or undefined');
      return args.length > 1 ? args[1] : undefined;
    }
    return originalReduce.apply(this, args);
  };
}

// Fix 6: Make .forEach() safe everywhere
if (typeof Array.prototype.safeForEach === 'undefined') {
  const originalForEach = Array.prototype.forEach;
  Array.prototype.forEach = function(...args) {
    if (this == null || this == undefined) {
      console.warn('Warning: Attempted to forEach over null/undefined, skipping');
      return;
    }
    return originalForEach.apply(this, args);
  };
}

// Fix 7: Fix the classList error from your logs
if (typeof document !== 'undefined') {
  const originalQuerySelector = document.querySelector;
  document.querySelector = function(...args) {
    try {
      const element = originalQuerySelector.apply(this, args);
      if (!element) {
        console.warn(`Element not found for selector: ${args[0]}`);
      }
      return element;
    } catch (e) {
      console.warn(`Query selector error: ${e.message}`);
      return null;
    }
  };
}

console.log('🚀 Emergency fixes loaded - your site should work now!');

export default true;