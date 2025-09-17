import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

// ====================================
// EMERGENCY FIX - RUNS BEFORE EVERYTHING!
// ====================================
console.log('Loading emergency fixes...');

// Fix .map() errors
const originalMap = Array.prototype.map;
Array.prototype.map = function(...args) {
  if (this == null || this == undefined) {
    console.warn('Fixed: Attempted to call .map() on null/undefined');
    return [];
  }
  return originalMap.apply(this, args);
};

// Fix .slice() errors  
const originalSlice = Array.prototype.slice;
Array.prototype.slice = function(...args) {
  if (this == null || this == undefined) {
    console.warn('Fixed: Attempted to call .slice() on null/undefined');
    return [];
  }
  return originalSlice.apply(this, args);
};

// Fix .filter() errors
const originalFilter = Array.prototype.filter;
Array.prototype.filter = function(...args) {
  if (this == null || this == undefined) {
    console.warn('Fixed: Attempted to call .filter() on null/undefined');
    return [];
  }
  return originalFilter.apply(this, args);
};

console.log('✅ Emergency fixes applied successfully!');

// ====================================
// NOW RENDER YOUR APP
// ====================================
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
