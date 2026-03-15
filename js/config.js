/**
 * ImpactMojo Configuration
 *
 * Centralised Supabase credentials and site settings.
 * All other scripts reference these values instead of hard-coding them.
 *
 * FORK NOTICE:
 *   If you forked this repository you MUST replace the values below
 *   with your own Supabase project credentials.  Using the original
 *   credentials violates the project licence and will be revoked.
 */

(function () {
  'use strict';

  var cfg = {
    SUPABASE_URL:      'https://ddyszmfffyedolkcugld.supabase.co',
    SUPABASE_ANON_KEY: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRkeXN6bWZmZnllZG9sa2N1Z2xkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ3MzMxMzEsImV4cCI6MjA4MDMwOTEzMX0.vPLlFkC3pqOBtofZ8B6_FBLbRfOKwlyv3DzLvJBS16w',

    // Allowed origins for premium resource launches
    SITE_ORIGIN: 'https://www.impactmojo.in',
  };

  // Freeze so other scripts cannot tamper with the values at runtime
  Object.freeze(cfg);

  window.ImpactMojoConfig = cfg;
})();
