// This file acts as a "map" for all components in this folder.
// It makes imports cleaner in other parts of the app.

export { default as Logo } from './Logo.js';
export { default as Navigation } from './Navigation.js';
export { default as QuizResult } from './QuizResult.js';
export { default as SimpleQuiz } from './SimpleQuiz.js';
export { default as Footer } from './Footer.js'; // Added the new Footer component

// These files export multiple components, so we use `export *`
export * from './floating-action-buttons.js';
export * from './homepage-components.js';
export * from './learning-tracks-component.js';

