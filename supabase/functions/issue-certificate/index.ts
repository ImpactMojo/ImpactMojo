// supabase/functions/issue-certificate/index.ts
// Supabase Edge Function — issues a certificate when a course is completed.
//
// Called by: database trigger on user_progress (progress_percentage = 100)
//            OR directly via POST from the client.
//
// Env (auto-provided by Supabase):
//   SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY

import { serve } from "https://deno.land/std@0.177.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.39.3";

// ── Course catalog (certificate-eligible courses) ─────────────────────
const COURSE_NAMES: Record<string, string> = {
  mel: "Monitoring, Evaluation & Learning",
  dataviz: "Data Visualization for Impact",
  devai: "AI for Development",
  devecon: "Development Economics",
  gandhi: "Gandhi & Contemporary Development",
  law: "Law & Development",
  media: "Media, Communication & Development",
  SEL: "Social & Emotional Learning",
  poa: "Philosophy of Action",
};

// ── CORS headers ──────────────────────────────────────────────────────
const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "https://www.impactmojo.in",
  "Access-Control-Allow-Headers":
    "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

// ── Generate certificate number: IM-DEVECON-2026-A3F7 ─────────────────
function generateCertificateNumber(courseId: string): string {
  const prefix = "IM";
  const courseCode = courseId.toUpperCase().slice(0, 8);
  const year = new Date().getFullYear();
  const hex = crypto.getRandomValues(new Uint8Array(4));
  const suffix = Array.from(hex)
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("")
    .toUpperCase()
    .slice(0, 6);
  return `${prefix}-${courseCode}-${year}-${suffix}`;
}

serve(async (req: Request) => {
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: CORS_HEADERS });
  }

  try {
    // ── Auth: accept either service-role (trigger) or user JWT ──────
    const authHeader = req.headers.get("Authorization");
    if (!authHeader?.startsWith("Bearer ")) {
      return new Response(
        JSON.stringify({ error: "Missing Authorization header" }),
        {
          status: 401,
          headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
        }
      );
    }
    const accessToken = authHeader.replace("Bearer ", "");

    const supabaseUrl = Deno.env.get("SUPABASE_URL")!;
    const supabaseAnonKey = Deno.env.get("SUPABASE_ANON_KEY")!;
    const serviceRoleKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;

    // Determine caller: if the token equals the service role key it's a
    // trigger / internal call; otherwise verify the user session.
    let userId: string;

    if (accessToken === serviceRoleKey) {
      // Called from DB trigger / webhook — user_id comes in the body
      const body = await req.json();
      userId = body.user_id;
      if (!userId) {
        return new Response(
          JSON.stringify({ error: "user_id required for service-role calls" }),
          {
            status: 400,
            headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
          }
        );
      }
      // course_id also comes from body for trigger calls
      const courseId = body.course_id;
      if (!courseId) {
        return new Response(
          JSON.stringify({ error: "course_id required" }),
          {
            status: 400,
            headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
          }
        );
      }

      return await issueCertificate(
        supabaseUrl,
        serviceRoleKey,
        userId,
        courseId
      );
    } else {
      // Called from client — verify session
      const userClient = createClient(supabaseUrl, supabaseAnonKey, {
        global: { headers: { Authorization: `Bearer ${accessToken}` } },
      });
      const {
        data: { user },
        error: userError,
      } = await userClient.auth.getUser();
      if (userError || !user) {
        return new Response(
          JSON.stringify({ error: "Invalid session" }),
          {
            status: 401,
            headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
          }
        );
      }
      userId = user.id;

      const { course_id: courseId } = await req.json();
      if (!courseId) {
        return new Response(
          JSON.stringify({ error: "course_id required" }),
          {
            status: 400,
            headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
          }
        );
      }

      return await issueCertificate(
        supabaseUrl,
        serviceRoleKey,
        userId,
        courseId
      );
    }
  } catch (err) {
    console.error("issue-certificate error:", err);
    return new Response(
      JSON.stringify({ error: "Internal server error" }),
      {
        status: 500,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      }
    );
  }
});

// ── Core logic ─────────────────────────────────────────────────────────
async function issueCertificate(
  supabaseUrl: string,
  serviceRoleKey: string,
  userId: string,
  courseId: string
) {
  const adminClient = createClient(supabaseUrl, serviceRoleKey);

  // 1. Verify course is valid
  const courseName = COURSE_NAMES[courseId];
  if (!courseName) {
    return new Response(
      JSON.stringify({ error: "Unknown course", course_id: courseId }),
      {
        status: 400,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      }
    );
  }

  // 2. Check progress is actually 100%
  const { data: progress } = await adminClient
    .from("user_progress")
    .select("progress_percentage")
    .eq("user_id", userId)
    .eq("course_id", courseId)
    .single();

  if (!progress || progress.progress_percentage < 100) {
    return new Response(
      JSON.stringify({
        error: "Course not yet completed",
        progress: progress?.progress_percentage ?? 0,
      }),
      {
        status: 403,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      }
    );
  }

  // 3. Check if certificate already exists (idempotent)
  const { data: existing } = await adminClient
    .from("certificates")
    .select("id, certificate_number")
    .eq("user_id", userId)
    .eq("course_id", courseId)
    .single();

  if (existing) {
    return new Response(
      JSON.stringify({
        message: "Certificate already issued",
        certificate_number: existing.certificate_number,
        certificate_id: existing.id,
      }),
      {
        status: 200,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      }
    );
  }

  // 4. Get user profile for the certificate
  const { data: profile } = await adminClient
    .from("profiles")
    .select("full_name, display_name, email")
    .eq("id", userId)
    .single();

  const recipientName =
    profile?.full_name || profile?.display_name || "Learner";

  // 5. Generate certificate number
  const certificateNumber = generateCertificateNumber(courseId);
  const verificationUrl = `https://www.impactmojo.in/verify-certificate.html?cert=${certificateNumber}`;

  // 6. Insert certificate record
  const { data: cert, error: insertError } = await adminClient
    .from("certificates")
    .insert({
      user_id: userId,
      course_id: courseId,
      course_name: courseName,
      certificate_number: certificateNumber,
      verification_url: verificationUrl,
    })
    .select()
    .single();

  if (insertError) {
    console.error("Certificate insert error:", insertError);
    return new Response(
      JSON.stringify({ error: "Failed to issue certificate" }),
      {
        status: 500,
        headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
      }
    );
  }

  // 7. Update profile's certificates_earned array
  const { data: currentProfile } = await adminClient
    .from("profiles")
    .select("certificates_earned")
    .eq("id", userId)
    .single();

  const currentCerts = currentProfile?.certificates_earned || [];
  if (!currentCerts.includes(cert.id)) {
    await adminClient
      .from("profiles")
      .update({
        certificates_earned: [...currentCerts, cert.id],
      })
      .eq("id", userId);
  }

  return new Response(
    JSON.stringify({
      message: "Certificate issued successfully",
      certificate_id: cert.id,
      certificate_number: certificateNumber,
      course_name: courseName,
      recipient_name: recipientName,
      verification_url: verificationUrl,
      issued_at: cert.issued_at,
    }),
    {
      status: 201,
      headers: { ...CORS_HEADERS, "Content-Type": "application/json" },
    }
  );
}
