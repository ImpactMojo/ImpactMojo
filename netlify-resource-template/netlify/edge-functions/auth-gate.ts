// netlify/edge-functions/auth-gate.ts
// Netlify Edge Function — gates access to a premium resource site.
//
// Deploy this file (and the netlify.toml) to EACH resource Netlify site.
//
// Required env vars (set in Netlify dashboard → Site settings → Environment variables):
//   RESOURCE_TOKEN_SECRET  — same HMAC secret used in the Supabase Edge Function
//   RESOURCE_ID            — unique slug for this Netlify site:
//                            "code-convert-pro" → stats-assist.netlify.app
//                            "qual-insights"    → qual-lab.netlify.app
//                            "vaniscribe"       → vaniscribe.netlify.app
//                            "rq-builder"       → researchquestions.netlify.app

import type { Context } from "https://edge.netlify.com";

// ── JWT helpers (minimal, no external deps) ─────────────────────────
function base64UrlDecode(str: string): Uint8Array {
  // Restore standard base64 padding
  let b64 = str.replace(/-/g, "+").replace(/_/g, "/");
  while (b64.length % 4 !== 0) b64 += "=";
  const binary = atob(b64);
  const bytes = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i++) bytes[i] = binary.charCodeAt(i);
  return bytes;
}

function base64UrlEncode(buf: ArrayBuffer): string {
  const bytes = new Uint8Array(buf);
  let binary = "";
  for (const b of bytes) binary += String.fromCharCode(b);
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

interface TokenPayload {
  sub: string;
  resource: string;
  iat: number;
  exp: number;
}

async function verifyJwt(token: string, secret: string): Promise<TokenPayload | null> {
  const parts = token.split(".");
  if (parts.length !== 3) return null;

  const [headerB64, payloadB64, signatureB64] = parts;

  // Import HMAC key
  const encoder = new TextEncoder();
  const key = await crypto.subtle.importKey(
    "raw",
    encoder.encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign", "verify"],
  );

  // Verify signature
  const data = encoder.encode(`${headerB64}.${payloadB64}`);
  const signature = base64UrlDecode(signatureB64);
  const valid = await crypto.subtle.verify("HMAC", key, signature, data);
  if (!valid) return null;

  // Decode payload
  const payloadJson = new TextDecoder().decode(base64UrlDecode(payloadB64));
  const payload: TokenPayload = JSON.parse(payloadJson);

  // Check expiry
  const now = Math.floor(Date.now() / 1000);
  if (payload.exp && payload.exp < now) return null;

  return payload;
}

// ── Cookie helpers ──────────────────────────────────────────────────
function getCookie(cookieHeader: string | null, name: string): string | null {
  if (!cookieHeader) return null;
  const match = cookieHeader.match(new RegExp(`(?:^|;\\s*)${name}=([^;]*)`));
  return match ? decodeURIComponent(match[1]) : null;
}

// ── Main handler ────────────────────────────────────────────────────
export default async function handler(req: Request, context: Context) {
  const secret = Deno.env.get("RESOURCE_TOKEN_SECRET");
  const resourceId = Deno.env.get("RESOURCE_ID");

  if (!secret || !resourceId) {
    console.error("auth-gate: Missing RESOURCE_TOKEN_SECRET or RESOURCE_ID env vars");
    return new Response("Server misconfigured", { status: 500 });
  }

  const LOGIN_URL = "https://www.impactmojo.in/login?reason=expired";

  // ── 1. Check for existing session cookie ──────────────────────────
  const cookieHeader = req.headers.get("cookie");
  const sessionToken = getCookie(cookieHeader, "resource_session");

  if (sessionToken) {
    const payload = await verifyJwt(sessionToken, secret);
    if (payload && payload.resource === resourceId) {
      // Valid session — pass through to the origin
      return context.next();
    }
    // Cookie is present but invalid/expired — fall through to token check
  }

  // ── 2. Check for ?token= query parameter ─────────────────────────
  const url = new URL(req.url);
  const tokenParam = url.searchParams.get("token");

  if (!tokenParam) {
    // No cookie, no token → redirect to login
    return Response.redirect(LOGIN_URL, 302);
  }

  // ── 3. Verify the token ───────────────────────────────────────────
  const payload = await verifyJwt(tokenParam, secret);

  if (!payload) {
    return Response.redirect(LOGIN_URL, 302);
  }

  // Ensure the token is scoped to this specific resource site
  if (payload.resource !== resourceId) {
    return Response.redirect(LOGIN_URL, 302);
  }

  // ── 4. Token valid — set session cookie and redirect cleanly ──────
  // Mint a longer-lived session cookie (24h) so the user doesn't need
  // to re-authenticate on every sub-page navigation.
  const encoder = new TextEncoder();
  const key = await crypto.subtle.importKey(
    "raw",
    encoder.encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );

  const now = Math.floor(Date.now() / 1000);
  const sessionPayload = {
    sub: payload.sub,
    resource: resourceId,
    iat: now,
    exp: now + 86400, // 24 hours
  };

  const headerB64 = base64UrlEncode(encoder.encode(JSON.stringify({ alg: "HS256", typ: "JWT" })));
  const payloadB64 = base64UrlEncode(encoder.encode(JSON.stringify(sessionPayload)));
  const sigData = encoder.encode(`${headerB64}.${payloadB64}`);
  const sig = await crypto.subtle.sign("HMAC", key, sigData);
  const sigB64 = base64UrlEncode(sig);
  const sessionJwt = `${headerB64}.${payloadB64}.${sigB64}`;

  // Strip the token from the URL for a clean redirect
  url.searchParams.delete("token");
  const cleanUrl = url.toString();

  return new Response(null, {
    status: 302,
    headers: {
      Location: cleanUrl,
      "Set-Cookie": [
        `resource_session=${sessionJwt}`,
        `HttpOnly`,
        `Secure`,
        `SameSite=Lax`,
        `Path=/`,
        `Max-Age=86400`, // 24 hours
      ].join("; "),
    },
  });
}

export const config = { path: "/*" };
