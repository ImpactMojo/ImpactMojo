-- Fix infinite recursion in organizations RLS policies
-- Error: 42P17 "infinite recursion detected in policy for relation organizations"
--
-- Root cause: circular policy references between organizations and
-- organization_members tables. Fix uses direct auth.uid() checks
-- instead of cross-table subqueries.

-- ============================================================
-- 1. Drop existing broken policies on organizations
-- ============================================================
DROP POLICY IF EXISTS "org_admin_select" ON public.organizations;
DROP POLICY IF EXISTS "org_admin_insert" ON public.organizations;
DROP POLICY IF EXISTS "org_admin_update" ON public.organizations;
DROP POLICY IF EXISTS "org_admin_delete" ON public.organizations;
DROP POLICY IF EXISTS "org_member_select" ON public.organizations;
DROP POLICY IF EXISTS "organizations_select" ON public.organizations;
DROP POLICY IF EXISTS "organizations_insert" ON public.organizations;
DROP POLICY IF EXISTS "organizations_update" ON public.organizations;
DROP POLICY IF EXISTS "organizations_delete" ON public.organizations;
-- Catch-all: drop any remaining policies
DO $$
DECLARE
    pol RECORD;
BEGIN
    FOR pol IN
        SELECT policyname FROM pg_policies WHERE tablename = 'organizations' AND schemaname = 'public'
    LOOP
        EXECUTE format('DROP POLICY IF EXISTS %I ON public.organizations', pol.policyname);
    END LOOP;
END $$;

-- ============================================================
-- 2. Ensure RLS is enabled
-- ============================================================
ALTER TABLE public.organizations ENABLE ROW LEVEL SECURITY;

-- ============================================================
-- 3. Create non-recursive policies using direct auth.uid() checks
-- ============================================================

-- Admins can view their own organization
CREATE POLICY "org_admin_select"
    ON public.organizations FOR SELECT
    USING (admin_id = auth.uid());

-- Admins can create an organization
CREATE POLICY "org_admin_insert"
    ON public.organizations FOR INSERT
    WITH CHECK (admin_id = auth.uid());

-- Admins can update their own organization
CREATE POLICY "org_admin_update"
    ON public.organizations FOR UPDATE
    USING (admin_id = auth.uid())
    WITH CHECK (admin_id = auth.uid());

-- Admins can delete their own organization
CREATE POLICY "org_admin_delete"
    ON public.organizations FOR DELETE
    USING (admin_id = auth.uid());

-- ============================================================
-- 4. Fix organization_members policies (avoid circular refs)
-- ============================================================
DO $$
DECLARE
    pol RECORD;
BEGIN
    FOR pol IN
        SELECT policyname FROM pg_policies WHERE tablename = 'organization_members' AND schemaname = 'public'
    LOOP
        EXECUTE format('DROP POLICY IF EXISTS %I ON public.organization_members', pol.policyname);
    END LOOP;
END $$;

-- Create organization_members table if it doesn't exist
CREATE TABLE IF NOT EXISTS public.organization_members (
    id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    org_id uuid REFERENCES public.organizations(id) ON DELETE CASCADE,
    user_id uuid REFERENCES auth.users(id) ON DELETE CASCADE,
    role text DEFAULT 'member' CHECK (role IN ('member', 'manager', 'admin')),
    invited_at timestamptz DEFAULT now(),
    joined_at timestamptz,
    UNIQUE(org_id, user_id)
);

ALTER TABLE public.organization_members ENABLE ROW LEVEL SECURITY;

-- Use a security-definer function to check org admin status
-- without triggering RLS on the organizations table
CREATE OR REPLACE FUNCTION public.is_org_admin(check_org_id uuid)
RETURNS boolean
LANGUAGE sql
SECURITY DEFINER
STABLE
SET search_path = public
AS $$
    SELECT EXISTS (
        SELECT 1 FROM public.organizations
        WHERE id = check_org_id AND admin_id = auth.uid()
    );
$$;

-- Org admins can manage members
CREATE POLICY "org_members_admin_select"
    ON public.organization_members FOR SELECT
    USING (public.is_org_admin(org_id) OR user_id = auth.uid());

CREATE POLICY "org_members_admin_insert"
    ON public.organization_members FOR INSERT
    WITH CHECK (public.is_org_admin(org_id));

CREATE POLICY "org_members_admin_update"
    ON public.organization_members FOR UPDATE
    USING (public.is_org_admin(org_id))
    WITH CHECK (public.is_org_admin(org_id));

CREATE POLICY "org_members_admin_delete"
    ON public.organization_members FOR DELETE
    USING (public.is_org_admin(org_id));
