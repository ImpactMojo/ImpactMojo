/**
 * ImpactLex runtime configuration.
 * Shared by index.html and review.html.
 * Committed to the repo because it only contains public identifiers: the
 * Supabase anon key is the same one every page of the site already ships, and
 * row-level security on impactlex_contributions decides what it can do.
 */
window.IMPACTLEX_CONFIG = {
  supabaseUrl: 'https://ddyszmfffyedolkcugld.supabase.co',
  supabaseAnonKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRkeXN6bWZmZnllZG9sa2N1Z2xkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ3MzMxMzEsImV4cCI6MjA4MDMwOTEzMX0.vPLlFkC3pqOBtofZ8B6_FBLbRfOKwlyv3DzLvJBS16w',

  // The glossary. Edited by pull request; see CLAUDE.md.
  snapshotUrl: '/impactlex/data/seed-snapshot.json',
};
