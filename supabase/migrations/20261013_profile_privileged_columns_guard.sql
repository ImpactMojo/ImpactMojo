-- Snapshot of the live guard that stops a user giving themselves a paid tier,
-- an admin role, payment ids or resource grants by updating their own profile.
-- It existed in the database and nowhere in this repository, so a rebuild from
-- the repository would have dropped it. Captured from production on 2026-10-13.

CREATE OR REPLACE FUNCTION public.guard_profile_privileged_columns()
 RETURNS trigger
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'public', 'pg_temp'
AS $function$
begin
  if coalesce(auth.role(), '') in ('authenticated', 'anon') and not public.is_admin() then
    if tg_op = 'UPDATE' then
      if new.role is distinct from old.role
         or new.subscription_tier is distinct from old.subscription_tier
         or new.subscription_status is distinct from old.subscription_status
         or new.subscription_start is distinct from old.subscription_start
         or new.subscription_end is distinct from old.subscription_end
         or new.razorpay_customer_id is distinct from old.razorpay_customer_id
         or new.razorpay_subscription_id is distinct from old.razorpay_subscription_id
         or new.resource_grants is distinct from old.resource_grants then
        raise warning 'profiles: privileged columns cannot be changed by the account holder; change ignored';
      end if;
      new.role := old.role;
      new.subscription_tier := old.subscription_tier;
      new.subscription_status := old.subscription_status;
      new.subscription_start := old.subscription_start;
      new.subscription_end := old.subscription_end;
      new.razorpay_customer_id := old.razorpay_customer_id;
      new.razorpay_subscription_id := old.razorpay_subscription_id;
      new.resource_grants := old.resource_grants;
    elsif tg_op = 'INSERT' and auth.uid() is not null and auth.uid() = new.id then
      new.role := 'learner';
      new.subscription_tier := 'explorer';
      new.subscription_status := 'active';
      new.subscription_start := null;
      new.subscription_end := null;
      new.razorpay_customer_id := null;
      new.razorpay_subscription_id := null;
      new.resource_grants := null;
    end if;
  end if;
  return new;
end;
$function$

;

DROP TRIGGER IF EXISTS a_guard_profile_privileged_columns ON public.profiles;
CREATE TRIGGER a_guard_profile_privileged_columns BEFORE INSERT OR UPDATE ON public.profiles FOR EACH ROW EXECUTE FUNCTION guard_profile_privileged_columns();
