-- Applied to production on 19 August 2026 as version 20260819110149 and not
-- committed until 21 November 2026 (#1417). Until then the repository created
-- notify_user as SECURITY DEFINER with no revoke, so a database built from
-- these files left it callable by anyone through /rest/v1/rpc/notify_user.
--
-- Postgres grants EXECUTE on a new function to PUBLIC, and anon and
-- authenticated inherit it. Revoking from anon or authenticated alone does
-- nothing, because neither holds a grant of its own; PUBLIC is what has to go.
--
-- Each function that still needs a caller holds an explicit grant, which a
-- PUBLIC revoke does not touch:
--   notify_user    service_role (the send-notification and issue-certificate
--                  edge functions)
--   update_streak  authenticated (js/auth.js, own id only) and service_role
--   triggers       the trigger mechanism does not consult EXECUTE
--
-- get_public_stats and verify_certificate are public on purpose and are not
-- listed. The statements are the ones applied, wrapped so that a function a
-- later file creates (update_streak) does not stop a fresh build here.

DO $$
DECLARE
    sig text;
BEGIN
    FOREACH sig IN ARRAY ARRAY[
        'public.notify_user(uuid, text, text, text, text, jsonb)',
        'public.update_streak(uuid)',
        'public.auto_issue_certificate()',
        'public.create_notification_prefs()',
        'public.handle_new_user()',
        'public.protect_admin_tier()',
        'public.prevent_self_peer_review()',
        'public.touch_impact_outcomes_updated_at()',
        'public.update_course_content_timestamp()'
    ] LOOP
        IF to_regprocedure(sig) IS NOT NULL THEN
            EXECUTE format('REVOKE EXECUTE ON FUNCTION %s FROM PUBLIC, anon, authenticated', sig);
        END IF;
    END LOOP;

    IF to_regprocedure('public.notify_user(uuid, text, text, text, text, jsonb)') IS NOT NULL THEN
        GRANT EXECUTE ON FUNCTION public.notify_user(uuid, text, text, text, text, jsonb) TO service_role;
    END IF;
    IF to_regprocedure('public.update_streak(uuid)') IS NOT NULL THEN
        GRANT EXECUTE ON FUNCTION public.update_streak(uuid) TO authenticated, service_role;
    END IF;
END $$;
