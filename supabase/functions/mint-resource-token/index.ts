// supabase/functions/mint-resource-token/index.ts
// Supabase Edge Function — mints a short-lived JWT for premium resource access.
//
// Env secrets (set via `supabase secrets set`):
//   RESOURCE_TOKEN_SECRET  — HMAC-SHA256 signing key (same value in each Netlify resource site)
//   SUPABASE_URL           — auto-provided by Supabase
//   SUPABASE_ANON_KEY      — auto-provided by Supabase
//   SUPABASE_SERVICE_ROLE_KEY — auto-provided; used to read profiles bypassing RLS

import { serve } from "https://deno.land/std@0.177.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.39.3";
import { create, getNumericDate } from "https://deno.land/x/djwt@v3.0.2/mod.ts";

// ── Tier → resource ACL ──────────────────────────────────────────────
// Matches existing tiers in profiles.subscription_tier.
// Resource IDs correspond to premium-only tools (NOT flagship courses,
// which are free for everyone).
const TIER_RESOURCES: Record<string, string[]> = {
  explorer: [],
  practitioner: [
    "field-notes",      // Field Notes (marginmuse.space)
    "rq-builder",       // RQ Builder Pro (researchquestions.netlify.app)
  ],
  professional: [
    "field-notes",
    "rq-builder",
    "code-convert-pro", // Code Converter Pro (stats-assist.netlify.app)
    "qual-insights",    // Qual Insights Lab Pro (qual-lab.netlify.app)
    "vaniscribe",       // VaniScribe AI (vaniscribe.netlify.app)
    "devdata-practice", // DevData Practice (varnasr.github.io)
    "viz-cookbook",      // Visualization Cookbook (varnasr.github.io)
    "devecon-toolkit",  // DevEcon Toolkit (varnasr.github.io)
  ],
  organization: [
    "field-notes",
    "rq-builder",
    "code-convert-pro",
    "qual-insights",
    "vaniscribe",
    "devdata-practice",
    "viz-cookbook",
    "devecon-toolkit",
  ],
};

// ── CORS headers (allow the main site) ───────────────────────────────
const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "https://www.impactmojo.in",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

serve(async (req: Request) => {
  // Pre-flight
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: CORS_HEADERS });
  }

  try {
    // 1. Extract the user's Supabase access token from the Authorization header
    const authHeader = req.headers.get("Authorization");
    if (!authHeader?.startsWith("Bearer ")) {
      return new Response(
        JSON.stringify({ error: "Missing or malformed Authorization header" }),
        { status: 401, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } },
      );
    }
    const accessToken = authHeader.replace("Bearer ", "");

    // 2. Parse the requested resource ID from the body
    const { resource } = await req.json();
    if (!resource || typeof resource !== "string") {
      return new Response(
        JSON.stringify({ error: "Missing resource id in request body" }),
        { status: 400, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } },
      );
    }

    // 3. Verify the caller's session using the anon client + their JWT
    const supabaseUrl = Deno.env.get("SUPABASE_URL")!;
    const supabaseAnonKey = Deno.env.get("SUPABASE_ANON_KEY")!;
    const userClient = createClient(supabaseUrl, supabaseAnonKey, {
      global: { headers: { Authorization: `Bearer ${accessToken}` } },
    });
    const { data: { user }, error: userError } = await userClient.auth.getUser();
    if (userError || !user) {
      return new Response(
        JSON.stringify({ error: "Invalid session" }),
        { status: 401, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } },
      );
    }

    // 4. Fetch the user's subscription tier (use service role to bypass RLS)
    const serviceRoleKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
    const adminClient = createClient(supabaseUrl, serviceRoleKey);
    const { data: profile, error: profileError } = await adminClient
      .from("profiles")
      .select("subscription_tier, subscription_status")
      .eq("id", user.id)
      .single();

    if (profileError || !profile) {
      return new Response(
        JSON.stringify({ error: "Profile not found" }),
        { status: 404, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } },
      );
    }

    // 5. Check subscription is active
    if (profile.subscription_status !== "active") {
      return new Response(
        JSON.stringify({ error: "Subscription inactive", code: "INACTIVE" }),
        { status: 403, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } },
      );
    }

    // 6. Check tier permits the requested resource
    const tier = (profile.subscription_tier || "explorer").toLowerCase();
    const allowed = TIER_RESOURCES[tier] ?? [];
    if (!allowed.includes(resource)) {
      return new Response(
        JSON.stringify({ error: "Your plan does not include this resource", code: "TIER" }),
        { status: 403, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } },
      );
    }

    // 7. Mint a short-lived JWT (5 min TTL)
    const secret = Deno.env.get("RESOURCE_TOKEN_SECRET");
    if (!secret) {
      console.error("RESOURCE_TOKEN_SECRET is not set");
      return new Response(
        JSON.stringify({ error: "Server configuration error" }),
        { status: 500, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } },
      );
    }

    // Import the HMAC key for djwt v3
    const encoder = new TextEncoder();
    const keyData = encoder.encode(secret);
    const cryptoKey = await crypto.subtle.importKey(
      "raw",
      keyData,
      { name: "HMAC", hash: "SHA-256" },
      false,
      ["sign", "verify"],
    );

    const now = Math.floor(Date.now() / 1000);
    const token = await create(
      { alg: "HS256", typ: "JWT" },
      {
        sub: user.id,
        resource,
        iat: now,
        exp: getNumericDate(5 * 60), // 5 minutes from now
      },
      cryptoKey,
    );

    return new Response(
      JSON.stringify({ token }),
      { status: 200, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } },
    );
  } catch (err) {
    console.error("mint-resource-token error:", err);
    return new Response(
      JSON.stringify({ error: "Internal server error" }),
      { status: 500, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } },
    );
  }
});
