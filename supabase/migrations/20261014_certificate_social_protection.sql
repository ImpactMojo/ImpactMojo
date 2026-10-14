-- Add the Social Protection flagship to automatic certificate issue.
-- Applied to production on 2026-10-14 by replacing public.auto_issue_certificate
-- with the same definition plus one CASE line:
--   WHEN 'social-protection' THEN 'Social Protection and Welfare Delivery in India'
-- The full function is in 20260820100000_fix_auto_issue_certificate.sql; this file
-- records the one change rather than repeating the body.
DO $$
DECLARE d text;
BEGIN
  SELECT pg_get_functiondef(p.oid) INTO d
  FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace
  WHERE n.nspname = 'public' AND p.proname = 'auto_issue_certificate';
  IF position('social-protection' IN d) = 0 THEN
    d := replace(d,
      E'WHEN ''gender-mel''       THEN ''Gender-Sensitive Monitoring, Evaluation & Learning''\n',
      E'WHEN ''gender-mel''       THEN ''Gender-Sensitive Monitoring, Evaluation & Learning''\n    WHEN ''social-protection'' THEN ''Social Protection and Welfare Delivery in India''\n');
    EXECUTE d;
  END IF;
END $$;
