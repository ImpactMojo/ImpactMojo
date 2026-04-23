/**
 * ImpactLex runtime configuration.
 * Shared by index.html and review.html.
 * Committed to the repo because it only contains public identifiers;
 * the admin token lives in the environment, never in client code.
 */
window.IMPACTLEX_CONFIG = {
  // Public InstantDB app ID — safe to commit, client-side SDKs need it.
  instantDbAppId: 'ad5a119b-417b-41c0-8705-4783dcea65b0',

  // Offline-first fallback. Always loaded regardless of InstantDB connectivity.
  snapshotUrl: '/impactlex/data/seed-snapshot.json',

  // Emails allowed into /impactlex/review.html. Add your own here.
  adminEmails: [],
};
