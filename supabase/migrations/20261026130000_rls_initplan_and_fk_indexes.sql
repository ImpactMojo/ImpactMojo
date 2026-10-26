-- Two performance fixes from the Supabase advisor, applied on 2026-10-26. Neither changes who
-- can see or change which rows.
--
-- 1. Row-level security rules that call auth.uid(), auth.role() or auth.jwt() directly make
--    Postgres repeat the call for every row it examines. Wrapping the call as
--    (select auth.uid()) lets it run once per query. Each rule below is its existing
--    definition with only that wrapping added, read from pg_policies on the live project.
--
-- 2. Foreign keys with no covering index, so a lookup or delete on the linked table had to
--    scan the whole table.
--
-- Left alone on purpose: merging overlapping rules, which can change access and so needs a
-- case by case check, and the unused indexes, which cost little.

ALTER POLICY "Users can manage own bookmarks" ON public.bookmarks
  USING (((select auth.uid()) = user_id));
ALTER POLICY "Org peers and admins can view certificates" ON public.certificates
  USING ((((select auth.uid()) = user_id) OR shares_org_with(user_id) OR is_admin()));
ALTER POLICY "Users can view own certificates" ON public.certificates
  USING (((select auth.uid()) = user_id));
ALTER POLICY challenge_req_insert ON public.challenge_requests
  WITH CHECK ((EXISTS ( SELECT 1
   FROM organizations
  WHERE ((organizations.id = challenge_requests.org_id) AND (organizations.admin_id = (select auth.uid()))))));
ALTER POLICY challenge_req_org_admin ON public.challenge_requests
  USING ((EXISTS ( SELECT 1
   FROM organizations
  WHERE ((organizations.id = challenge_requests.org_id) AND (organizations.admin_id = (select auth.uid()))))));
ALTER POLICY "Learners can view peers' submissions for review" ON public.challenge_submissions
  USING ((((select auth.uid()) IS NOT NULL) AND ((select auth.uid()) <> user_id)));
ALTER POLICY "Users can insert own submissions" ON public.challenge_submissions
  WITH CHECK (((select auth.uid()) = user_id));
ALTER POLICY "Users can update own submissions" ON public.challenge_submissions
  USING (((select auth.uid()) = user_id));
ALTER POLICY "Users can view own submissions" ON public.challenge_submissions
  USING (((select auth.uid()) = user_id));
ALTER POLICY "Users can manage own bookings" ON public.coaching_bookings
  USING (((select auth.uid()) = user_id));
ALTER POLICY "Service role can manage course_content" ON public.course_content
  USING (((select auth.role()) = 'service_role'::text))
  WITH CHECK (((select auth.role()) = 'service_role'::text));
ALTER POLICY "Users can delete own outcomes" ON public.impact_outcomes
  USING (((select auth.uid()) = user_id));
ALTER POLICY "Users can insert own outcomes" ON public.impact_outcomes
  WITH CHECK (((select auth.uid()) = user_id));
ALTER POLICY "Users can update own outcomes" ON public.impact_outcomes
  USING (((select auth.uid()) = user_id))
  WITH CHECK (((select auth.uid()) = user_id));
ALTER POLICY "Users can view own outcomes" ON public.impact_outcomes
  USING (((select auth.uid()) = user_id));
ALTER POLICY "Admins can manage assignments" ON public.learning_path_assignments
  USING ((EXISTS ( SELECT 1
   FROM (learning_paths lp
     JOIN organizations o ON ((o.id = lp.org_id)))
  WHERE ((lp.id = learning_path_assignments.path_id) AND (o.admin_id = (select auth.uid()))))));
ALTER POLICY "Users can view own assignments" ON public.learning_path_assignments
  USING (((select auth.uid()) = user_id));
ALTER POLICY "Org admins can manage learning paths" ON public.learning_paths
  USING ((EXISTS ( SELECT 1
   FROM organizations
  WHERE ((organizations.id = learning_paths.org_id) AND (organizations.admin_id = (select auth.uid()))))));
ALTER POLICY "Org members can view learning paths" ON public.learning_paths
  USING ((EXISTS ( SELECT 1
   FROM organization_members
  WHERE ((organization_members.org_id = learning_paths.org_id) AND (organization_members.user_id = (select auth.uid())) AND (organization_members.status = 'active'::text)))));
ALTER POLICY users_manage_own_prefs ON public.notification_preferences
  USING (((select auth.uid()) = user_id));
ALTER POLICY users_update_own_notifs ON public.notifications
  USING (((select auth.uid()) = user_id));
ALTER POLICY users_view_own_notifs ON public.notifications
  USING (((select auth.uid()) = user_id));
ALTER POLICY org_members_admin_select ON public.organization_members
  USING ((is_org_admin(org_id) OR (user_id = (select auth.uid()))));
ALTER POLICY org_members_self_update ON public.organization_members
  USING ((user_id = (select auth.uid())))
  WITH CHECK ((user_id = (select auth.uid())));
ALTER POLICY org_admin_delete ON public.organizations
  USING ((admin_id = (select auth.uid())));
ALTER POLICY org_admin_insert ON public.organizations
  WITH CHECK ((admin_id = (select auth.uid())));
ALTER POLICY org_admin_select ON public.organizations
  USING ((admin_id = (select auth.uid())));
ALTER POLICY org_admin_update ON public.organizations
  USING ((admin_id = (select auth.uid())))
  WITH CHECK ((admin_id = (select auth.uid())));
ALTER POLICY "Users can view own payments" ON public.payments
  USING (((select auth.uid()) = user_id));
ALTER POLICY "Owners can view reviews of their submissions" ON public.peer_reviews
  USING ((EXISTS ( SELECT 1
   FROM challenge_submissions s
  WHERE ((s.id = peer_reviews.submission_id) AND (s.user_id = (select auth.uid()))))));
ALTER POLICY "Reviewers can insert own reviews" ON public.peer_reviews
  WITH CHECK (((select auth.uid()) = reviewer_id));
ALTER POLICY "Reviewers can update own reviews" ON public.peer_reviews
  USING (((select auth.uid()) = reviewer_id))
  WITH CHECK (((select auth.uid()) = reviewer_id));
ALTER POLICY "Reviewers can view own reviews" ON public.peer_reviews
  USING (((select auth.uid()) = reviewer_id));
ALTER POLICY "Users can manage own portfolio" ON public.portfolio_items
  USING (((select auth.uid()) = user_id));
ALTER POLICY "Org peers can view member profiles" ON public.profiles
  USING ((((select auth.uid()) = id) OR shares_org_with(id)));
ALTER POLICY "Users can insert own profile" ON public.profiles
  WITH CHECK (((select auth.uid()) = id));
ALTER POLICY "Users can update own profile" ON public.profiles
  USING (((select auth.uid()) = id));
ALTER POLICY "Users can view own profile" ON public.profiles
  USING (((select auth.uid()) = id));
ALTER POLICY "Users can manage own push subscriptions" ON public.push_subscriptions
  USING (((select auth.uid()) = user_id))
  WITH CHECK (((select auth.uid()) = user_id));
ALTER POLICY "Admin write" ON public.site_content
  USING ((EXISTS ( SELECT 1
   FROM profiles
  WHERE ((profiles.id = (select auth.uid())) AND (profiles.role = 'admin'::text)))));
ALTER POLICY "Users can manage own notes" ON public.user_notes
  USING (((select auth.uid()) = user_id));
ALTER POLICY "Users can manage own progress" ON public.user_progress
  USING (((select auth.uid()) = user_id));

CREATE INDEX IF NOT EXISTS idx_challenge_requests_org_id ON public.challenge_requests (org_id);
CREATE INDEX IF NOT EXISTS idx_challenge_requests_requested_by ON public.challenge_requests (requested_by);
CREATE INDEX IF NOT EXISTS idx_learning_path_assignments_assigned_by ON public.learning_path_assignments (assigned_by);
CREATE INDEX IF NOT EXISTS idx_learning_path_assignments_user_id ON public.learning_path_assignments (user_id);
CREATE INDEX IF NOT EXISTS idx_learning_paths_created_by ON public.learning_paths (created_by);
CREATE INDEX IF NOT EXISTS idx_learning_paths_org_id ON public.learning_paths (org_id);
CREATE INDEX IF NOT EXISTS idx_organization_members_invited_by ON public.organization_members (invited_by);
CREATE INDEX IF NOT EXISTS idx_organization_members_user_id ON public.organization_members (user_id);
CREATE INDEX IF NOT EXISTS idx_organizations_admin_id ON public.organizations (admin_id);
CREATE INDEX IF NOT EXISTS idx_site_content_updated_by ON public.site_content (updated_by);
CREATE INDEX IF NOT EXISTS idx_subscription_payments_subscription_id ON public.subscription_payments (subscription_id);
