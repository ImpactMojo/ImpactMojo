-- lookup_profile_id_by_email(p_email) is SECURITY DEFINER and executable by signed-in
-- users. It allowed any "organisation admin", but the organizations INSERT policy lets
-- any signed-in user create an organisation naming themselves admin, so any account
-- holder could test whether an email has an ImpactMojo account and get that person's
-- internal id.
--
-- The caller must now be an organisation admin who is on the Organization tier (the same
-- rule org-dashboard.html applies in the browser) or a site admin. Checked on
-- 2026-10-26 against the live data: all three organisation admins pass. Applied to
-- production the same day.

CREATE OR REPLACE FUNCTION public.lookup_profile_id_by_email(p_email text)
 RETURNS uuid
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'public'
AS $function$
  select p.id
  from public.profiles p
  where lower(p.email) = lower(p_email)
    and (
      -- an organisation admin who is on the Organization tier, as org-dashboard.html requires
      (
        exists (select 1 from public.organizations o where o.admin_id = auth.uid())
        and exists (select 1 from public.profiles me
                    where me.id = auth.uid() and me.subscription_tier = 'organization')
      )
      or exists (select 1 from public.profiles me where me.id = auth.uid() and me.role = 'admin')
    )
  limit 1;
$function$;
