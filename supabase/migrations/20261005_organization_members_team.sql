-- Team labels for the org dashboard. Additive and nullable: existing rows are unchanged,
-- and the dashboard checks whether the column exists, so it works before and after this runs.
-- Access is already covered by the org_members_admin_* policies (is_org_admin(org_id)).
alter table public.organization_members
  add column if not exists team text check (team is null or char_length(team) <= 60);

comment on column public.organization_members.team is
  'Free-text team or project label set by the organisation admin, used to filter the dashboard.';
