-- One row per order email (owner's "Confirm payment" mail and the buyer's file
-- mail), written by netlify/functions/submission-created.mjs and confirm.mjs.
-- Answers "did the email go out" with a query. Service role only.
create table if not exists public.order_mail_log (
  id bigint generated always as identity primary key,
  created_at timestamptz not null default now(),
  kind text not null,
  to_email text not null,
  subject text,
  ref text,
  status text not null check (status in ('sent','failed')),
  attempts int not null default 1,
  detail text
);
alter table public.order_mail_log enable row level security;
revoke all on public.order_mail_log from anon, authenticated;
create index if not exists order_mail_log_created_idx on public.order_mail_log (created_at desc);
