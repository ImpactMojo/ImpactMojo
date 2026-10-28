-- update_streak(p_user_id) is SECURITY DEFINER and executable by signed-in users,
-- and it took the user id from the caller. Any signed-in user could therefore
-- change another user's streak and last_active_at, which also feeds the public
-- "active learners" figure in get_public_stats().
--
-- A signed-in caller may now update only their own row. Calls with no JWT subject
-- (service role, database owner) are unaffected. js/auth.js, the only caller,
-- passes the signed-in user's own id.
--
-- Applied to production on 2026-10-26. The 14-digit version avoids the duplicate
-- date prefixes several older files share.

CREATE OR REPLACE FUNCTION public.update_streak(p_user_id uuid)
 RETURNS void
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'public', 'pg_temp'
AS $function$
DECLARE
  last_active DATE;
  today DATE := CURRENT_DATE;
BEGIN
  -- A signed-in caller may only update their own streak. Calls with no JWT
  -- subject (service role, database owner) are unaffected.
  IF auth.uid() IS NOT NULL AND p_user_id IS DISTINCT FROM auth.uid() THEN
    RETURN;
  END IF;

  SELECT last_active_at::date INTO last_active FROM profiles WHERE id = p_user_id;
  IF last_active IS NULL OR last_active < today - 1 THEN
    UPDATE profiles SET streak_days = 1, last_active_at = NOW() WHERE id = p_user_id;
  ELSIF last_active = today - 1 THEN
    UPDATE profiles SET streak_days = streak_days + 1, last_active_at = NOW() WHERE id = p_user_id;
  ELSIF last_active = today THEN
    UPDATE profiles SET last_active_at = NOW() WHERE id = p_user_id;
  END IF;
END;
$function$;
