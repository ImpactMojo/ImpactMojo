// supabase/functions/send-notification/index.ts
// Supabase Edge Function — sends email notifications and creates in-app notifications.
//
// Endpoints:
//   POST /send-notification
//     Body: { type, user_id?, user_ids?, title, body, link?, metadata? }
//
//   POST /send-notification/streak-reminders
//     No body — finds users inactive for 2+ days with streak_days > 0 and sends reminders
//
//   POST /send-notification/cohort-deadlines
//     No body — finds cohorts ending within 3 days and notifies enrolled members
//
// Env: SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY
//      RESEND_API_KEY (optional — for email delivery via Resend.com)

import { serve } from "https://deno.land/std@0.177.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.39.3";

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "https://www.impactmojo.in",
  "Access-Control-Allow-Headers":
    "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

const FROM_EMAIL = "ImpactMojo <notifications@impactmojo.in>";

// ── Email via Resend (free 3K emails/month) ──────────────────────────
async function sendEmail(
  to: string,
  subject: string,
  html: string
): Promise<boolean> {
  const resendKey = Deno.env.get("RESEND_API_KEY");
  if (!resendKey) {
    console.log("RESEND_API_KEY not set — skipping email delivery");
    return false;
  }
  try {
    const resp = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${resendKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        from: FROM_EMAIL,
        to: [to],
        subject,
        html,
      }),
    });
    if (!resp.ok) {
      console.error("Resend error:", resp.status, await resp.text());
      return false;
    }
    return true;
  } catch (err) {
    console.error("Email send failed:", err);
    return false;
  }
}

// ── Email templates ──────────────────────────────────────────────────
function wrapEmail(title: string, body: string, link?: string): string {
  const cta = link
    ? `<p style="margin:24px 0"><a href="https://www.impactmojo.in${link}" style="background:#F59E0B;color:#fff;text-decoration:none;padding:12px 24px;border-radius:8px;font-weight:600;display:inline-block">View on ImpactMojo</a></p>`
    : "";
  return `<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"></head>
<body style="font-family:'Amaranth',Helvetica,Arial,sans-serif;background:#F8FAFC;margin:0;padding:0">
<div style="max-width:560px;margin:0 auto;padding:32px 24px">
<div style="text-align:center;margin-bottom:24px">
<img src="https://www.impactmojo.in/assets/images/favicon.png" width="40" height="40" alt="ImpactMojo" style="border-radius:8px">
<h2 style="font-family:Inter,Helvetica,sans-serif;color:#0F172A;margin:12px 0 0">${title}</h2>
</div>
<div style="background:#fff;border:1px solid #E2E8F0;border-radius:12px;padding:24px;color:#334155;line-height:1.6;font-size:15px">
${body}
${cta}
</div>
<p style="text-align:center;color:#94A3B8;font-size:12px;margin-top:24px">
ImpactMojo &middot; Free Development Education for South Asia<br>
<a href="https://www.impactmojo.in/account.html#notifications" style="color:#94A3B8">Manage notification preferences</a>
</p>
</div></body></html>`;
}

function streakReminderEmail(name: string, streakDays: number): string {
  return wrapEmail(
    "Keep Your Streak Alive!",
    `<p>Hi ${name},</p>
<p>You've built a <strong>${streakDays}-day learning streak</strong> on ImpactMojo — don't let it slip!</p>
<p>Even 10 minutes of learning today will keep your momentum going. Pick up where you left off or try something new.</p>`,
    "/account.html"
  );
}

function cohortDeadlineEmail(
  name: string,
  cohortName: string,
  daysLeft: number,
  progress: number
): string {
  const urgency =
    daysLeft <= 1
      ? "ends <strong>tomorrow</strong>"
      : `ends in <strong>${daysLeft} days</strong>`;
  return wrapEmail(
    `Cohort Deadline Approaching`,
    `<p>Hi ${name},</p>
<p>Your cohort <strong>${cohortName}</strong> ${urgency}.</p>
<p>Your current progress: <strong>${progress}%</strong></p>
${progress < 100 ? "<p>Complete your remaining modules to earn your certificate before the deadline.</p>" : "<p>Great work — you've completed the cohort! Your certificate will be issued shortly.</p>"}`,
    "/org-dashboard.html"
  );
}

function cohortDiscussionEmail(
  name: string,
  authorName: string,
  cohortName: string,
  preview: string
): string {
  return wrapEmail(
    `New Discussion in ${cohortName}`,
    `<p>Hi ${name},</p>
<p><strong>${authorName}</strong> posted in your cohort:</p>
<blockquote style="border-left:3px solid #F59E0B;padding:8px 16px;margin:12px 0;color:#475569;background:#FFFBEB;border-radius:0 6px 6px 0">${preview}</blockquote>`,
    "/org-dashboard.html"
  );
}

// ── Main handler ─────────────────────────────────────────────────────
serve(async (req: Request) => {
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: CORS_HEADERS });
  }

  const supabaseUrl = Deno.env.get("SUPABASE_URL")!;
  const serviceRoleKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
  const admin = createClient(supabaseUrl, serviceRoleKey);

  const url = new URL(req.url);
  const path = url.pathname.split("/").pop();

  try {
    // ── Automated: Streak Reminders ──────────────────────────────────
    if (path === "streak-reminders") {
      // Find users inactive for 2+ days who have an active streak
      const twoDaysAgo = new Date(
        Date.now() - 2 * 24 * 60 * 60 * 1000
      ).toISOString();

      const { data: users } = await admin
        .from("profiles")
        .select("id, email, full_name, display_name, streak_days")
        .gt("streak_days", 0)
        .lt("last_active_at", twoDaysAgo)
        .not("email", "is", null);

      if (!users || users.length === 0) {
        return json({ message: "No streak reminders needed", count: 0 });
      }

      let sent = 0;
      for (const user of users) {
        // Check preferences
        const { data: prefs } = await admin
          .from("notification_preferences")
          .select("email_streak_reminders, in_app_enabled")
          .eq("user_id", user.id)
          .single();

        const name = user.full_name || user.display_name || "Learner";

        // In-app notification
        if (!prefs || prefs.in_app_enabled !== false) {
          await admin.rpc("notify_user", {
            p_user_id: user.id,
            p_type: "streak_reminder",
            p_title: "Keep your streak alive!",
            p_body: `You have a ${user.streak_days}-day streak. Log in today to keep it going!`,
            p_link: "/account.html",
          });
        }

        // Email
        if (!prefs || prefs.email_streak_reminders !== false) {
          const emailSent = await sendEmail(
            user.email,
            `Keep your ${user.streak_days}-day streak alive! — ImpactMojo`,
            streakReminderEmail(name, user.streak_days)
          );
          if (emailSent) sent++;
        }
      }

      return json({
        message: "Streak reminders sent",
        users: users.length,
        emails_sent: sent,
      });
    }

    // ── Automated: Cohort Deadline Reminders ─────────────────────────
    if (path === "cohort-deadlines") {
      const threeDaysFromNow = new Date(
        Date.now() + 3 * 24 * 60 * 60 * 1000
      );
      const today = new Date();

      const { data: cohorts } = await admin
        .from("cohorts")
        .select(
          "id, name, end_date, org_id, cohort_members(user_id, progress_percentage, status)"
        )
        .eq("status", "active")
        .lte("end_date", threeDaysFromNow.toISOString().slice(0, 10))
        .gte("end_date", today.toISOString().slice(0, 10));

      if (!cohorts || cohorts.length === 0) {
        return json({
          message: "No cohort deadline reminders needed",
          count: 0,
        });
      }

      let sent = 0;
      for (const cohort of cohorts) {
        const endDate = new Date(cohort.end_date);
        const daysLeft = Math.ceil(
          (endDate.getTime() - today.getTime()) / (24 * 60 * 60 * 1000)
        );

        for (const member of cohort.cohort_members || []) {
          if (member.status === "dropped") continue;

          const { data: profile } = await admin
            .from("profiles")
            .select("email, full_name, display_name")
            .eq("id", member.user_id)
            .single();

          if (!profile?.email) continue;

          const { data: prefs } = await admin
            .from("notification_preferences")
            .select("email_cohort_deadlines, in_app_enabled")
            .eq("user_id", member.user_id)
            .single();

          const name =
            profile.full_name || profile.display_name || "Learner";

          // In-app
          if (!prefs || prefs.in_app_enabled !== false) {
            await admin.rpc("notify_user", {
              p_user_id: member.user_id,
              p_type: "cohort_deadline",
              p_title: `${cohort.name} ends in ${daysLeft} day${daysLeft === 1 ? "" : "s"}`,
              p_body: `Your progress: ${member.progress_percentage}%. Complete remaining modules before the deadline.`,
              p_link: "/org-dashboard.html",
            });
          }

          // Email
          if (!prefs || prefs.email_cohort_deadlines !== false) {
            const emailSent = await sendEmail(
              profile.email,
              `${cohort.name} ends in ${daysLeft} day${daysLeft === 1 ? "" : "s"} — ImpactMojo`,
              cohortDeadlineEmail(
                name,
                cohort.name,
                daysLeft,
                member.progress_percentage
              )
            );
            if (emailSent) sent++;
          }
        }
      }

      return json({
        message: "Cohort deadline reminders sent",
        cohorts: cohorts.length,
        emails_sent: sent,
      });
    }

    // ── Manual: Send notification to specific user(s) ────────────────
    const authHeader = req.headers.get("Authorization");
    if (!authHeader?.startsWith("Bearer ")) {
      return json({ error: "Missing Authorization header" }, 401);
    }
    const token = authHeader.replace("Bearer ", "");

    // Only service role or admin can send manual notifications
    if (token !== serviceRoleKey) {
      const userClient = createClient(
        supabaseUrl,
        Deno.env.get("SUPABASE_ANON_KEY")!,
        {
          global: { headers: { Authorization: `Bearer ${token}` } },
        }
      );
      const {
        data: { user },
      } = await userClient.auth.getUser();
      if (!user) return json({ error: "Invalid session" }, 401);

      // Check admin role
      const { data: profile } = await admin
        .from("profiles")
        .select("role")
        .eq("id", user.id)
        .single();
      if (profile?.role !== "admin" && profile?.role !== "organization_admin") {
        return json({ error: "Admin access required" }, 403);
      }
    }

    const body = await req.json();
    const { type, user_id, user_ids, title, body: notifBody, link, metadata } =
      body;

    if (!type || !title) {
      return json({ error: "type and title required" }, 400);
    }

    const targets: string[] = user_ids || (user_id ? [user_id] : []);
    if (targets.length === 0) {
      return json({ error: "user_id or user_ids required" }, 400);
    }

    let created = 0;
    for (const uid of targets) {
      await admin.rpc("notify_user", {
        p_user_id: uid,
        p_type: type,
        p_title: title,
        p_body: notifBody || null,
        p_link: link || null,
        p_metadata: metadata || {},
      });
      created++;
    }

    return json({ message: "Notifications created", count: created });
  } catch (err) {
    console.error("send-notification error:", err);
    return json({ error: "Internal server error" }, 500);
  }
});

function json(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
  });
}
