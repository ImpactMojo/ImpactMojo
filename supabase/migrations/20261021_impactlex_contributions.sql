-- ImpactLex contributions, moved from InstantDB (shutting down 2026-08-31 2027).
--
-- A reader suggests a term or an edit from /impactlex/. Anyone can add a row;
-- only a signed-in admin (public.is_admin(), defined in
-- 20260719_fix_profiles_public_exposure.sql) can read, approve or reject one.
-- The reader's email is optional and is the only personal data held, so it is
-- never readable by anon or by other signed-in users.
--
-- The glossary itself stays in the repository (impactlex/data/seed-snapshot.json);
-- it is 494 rows that change by pull request, and a second copy in a database
-- is how the InstantDB copy drifted 109 terms behind.

CREATE TABLE IF NOT EXISTS public.impactlex_contributions (
  id           uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  term         text NOT NULL CHECK (char_length(term) BETWEEN 1 AND 200),
  category     text CHECK (category IS NULL OR char_length(category) <= 80),
  definition   text CHECK (definition IS NULL OR char_length(definition) <= 4000),
  example      text CHECK (example IS NULL OR char_length(example) <= 2000),
  email        text CHECK (email IS NULL OR char_length(email) <= 254),
  status       text NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected')),
  reviewer_note text CHECK (reviewer_note IS NULL OR char_length(reviewer_note) <= 2000),
  reviewed_at  timestamptz,
  created_at   timestamptz NOT NULL DEFAULT now()
);

ALTER TABLE public.impactlex_contributions ENABLE ROW LEVEL SECURITY;

-- A new row is always pending: a reader cannot submit an already-approved one.
DROP POLICY IF EXISTS "Anyone can suggest a term" ON public.impactlex_contributions;
CREATE POLICY "Anyone can suggest a term" ON public.impactlex_contributions
  FOR INSERT TO anon, authenticated
  WITH CHECK (status = 'pending' AND reviewer_note IS NULL AND reviewed_at IS NULL);

DROP POLICY IF EXISTS "Admins read contributions" ON public.impactlex_contributions;
CREATE POLICY "Admins read contributions" ON public.impactlex_contributions
  FOR SELECT TO authenticated USING (public.is_admin());

DROP POLICY IF EXISTS "Admins review contributions" ON public.impactlex_contributions;
CREATE POLICY "Admins review contributions" ON public.impactlex_contributions
  FOR UPDATE TO authenticated
  USING (public.is_admin()) WITH CHECK (public.is_admin());

DROP POLICY IF EXISTS "Admins delete contributions" ON public.impactlex_contributions;
CREATE POLICY "Admins delete contributions" ON public.impactlex_contributions
  FOR DELETE TO authenticated USING (public.is_admin());

REVOKE ALL ON public.impactlex_contributions FROM anon, authenticated;
GRANT INSERT ON public.impactlex_contributions TO anon, authenticated;
GRANT SELECT, UPDATE, DELETE ON public.impactlex_contributions TO authenticated;
