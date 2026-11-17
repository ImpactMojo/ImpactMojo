-- The two course_content backups taken on 2026-10-27 sat in the public schema,
-- which is the schema the REST API serves. Every row in both still exists in
-- course_content (checked by id on 2026-11-15), so they are only the earlier
-- text of rows that were edited that day. They are moved, not dropped: the
-- archive schema is not exposed by the API, so they stop appearing in the
-- security and performance advisors, and the earlier text can still be read
-- by an administrator if the October edit ever needs undoing.
create schema if not exists archive;
revoke all on schema archive from anon, authenticated;
alter table if exists public.course_content_backup_20261027 set schema archive;
alter table if exists public.course_content_backup_20261027b set schema archive;
