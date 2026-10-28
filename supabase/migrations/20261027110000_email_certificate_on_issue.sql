-- Email a learner when a certificate is issued.
--
-- Until now nothing told a learner their certificate existed. Issuing one
-- (public.auto_issue_certificate) inserts the row and stops, and every row in
-- public.notifications was a welcome message. This trigger asks the
-- send-notification Edge Function to announce the new certificate. The call is
-- queued by pg_net and returns at once, so a slow or failed email can never
-- hold up or undo the certificate. The function sends from Team ImpactMojo and
-- records the announcement as a notification of type "certificate"; the daily
-- job retries any that did not go out.
--
-- The bearer is the public anon key, the same one every page ships in
-- js/config.js. The function treats that caller as untrusted: it takes only a
-- certificate id, mails only that certificate's holder, and mails each
-- certificate once.

CREATE EXTENSION IF NOT EXISTS pg_net WITH SCHEMA extensions;

CREATE OR REPLACE FUNCTION public.email_certificate_on_issue()
RETURNS TRIGGER
LANGUAGE plpgsql SECURITY DEFINER
SET search_path TO 'public', 'extensions', 'net', 'pg_temp'
AS $$
BEGIN
  PERFORM net.http_post(
    url := 'https://ddyszmfffyedolkcugld.supabase.co/functions/v1/send-notification/certificate-email',
    headers := jsonb_build_object(
      'Content-Type', 'application/json',
      'Authorization', 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRkeXN6bWZmZnllZG9sa2N1Z2xkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ3MzMxMzEsImV4cCI6MjA4MDMwOTEzMX0.vPLlFkC3pqOBtofZ8B6_FBLbRfOKwlyv3DzLvJBS16w'
    ),
    body := jsonb_build_object('certificate_id', NEW.id)
  );
  RETURN NEW;
EXCEPTION WHEN OTHERS THEN
  RETURN NEW;
END;
$$;

REVOKE ALL ON FUNCTION public.email_certificate_on_issue() FROM PUBLIC, anon, authenticated;

DROP TRIGGER IF EXISTS certificate_email_on_issue ON public.certificates;
CREATE TRIGGER certificate_email_on_issue
  AFTER INSERT ON public.certificates
  FOR EACH ROW EXECUTE FUNCTION public.email_certificate_on_issue();
