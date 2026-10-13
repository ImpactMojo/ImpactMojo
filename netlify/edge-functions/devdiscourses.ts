// Netlify Edge Function: proxy a GitHub-Pages-hosted external page so
// it appears at /devdiscourses on impactmojo.in. Injects a <base> tag
// so the page's relative asset URLs (css/, js/) resolve correctly under
// the proxied base path, fixing the "blank/unstyled page" problem you
// can't solve with _redirects alone (Netlify normalises trailing slashes
// when matching, so the no-slash form silently serves the page with
// broken relative paths).
//
// Routes (self-registered via the exported config below):
//   /devdiscourses        → varnasr.github.io/development-discourses/
//   /devdiscourses/       → varnasr.github.io/development-discourses/
//   /devdiscourses/*      → varnasr.github.io/development-discourses/<splat>
//
// Isolation. These pages come from another repository but are served on
// www.impactmojo.in, where the Supabase session sits in localStorage. Every
// response therefore carries a Content-Security-Policy with `sandbox` and no
// `allow-same-origin`: the browser gives the page an opaque origin, so its
// scripts cannot read this site's storage or cookies, register a service
// worker here, or call Supabase with a visitor's session. connect-src is
// 'self' only. The upstream's own security headers are passed through.
// Because sandboxed pages cannot use localStorage, a small script injected
// at the top of <head> gives them an in-memory one, so the theme and saved
// items work for the visit and are simply not remembered afterwards.

import type { Context } from "https://edge.netlify.com";

const UPSTREAM = "https://varnasr.github.io/development-discourses";
const BASE_PATH = "/devdiscourses/";

const CSP = [
    "sandbox allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-modals allow-downloads",
    "default-src 'self'",
    "script-src 'self' 'unsafe-inline'",
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
    "font-src 'self' data: https://fonts.gstatic.com",
    "img-src 'self' data: https:",
    "connect-src 'self'",
    "manifest-src 'self'",
    "worker-src 'none'",
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "frame-ancestors 'self'",
].join("; ");

// In-memory Storage for a sandboxed page, where localStorage throws.
const STORAGE_SHIM = `<script>(function(){function m(){var d={};return{getItem:function(k){k=String(k);return Object.prototype.hasOwnProperty.call(d,k)?d[k]:null},setItem:function(k,v){d[String(k)]=String(v)},removeItem:function(k){delete d[String(k)]},clear:function(){d={}},key:function(i){var a=Object.keys(d);return i<a.length?a[i]:null},get length(){return Object.keys(d).length}}};["localStorage","sessionStorage"].forEach(function(n){try{window[n].getItem("x")}catch(e){try{Object.defineProperty(window,n,{value:m(),configurable:true})}catch(_){}}})})();</script>`;

function secure(headers: Headers) {
    // Upstream policies are kept and ours is added beside them; a browser
    // enforces every policy it receives.
    headers.append("content-security-policy", CSP);
    headers.set("x-content-type-options", "nosniff");
}

export default async (request: Request, context: Context) => {
    const url = new URL(request.url);
    let path = url.pathname;

    // Strip our base prefix to find the upstream path.
    if (path === "/devdiscourses" || path === "/devdiscourses/") {
        path = "/";
    } else if (path.startsWith("/devdiscourses/")) {
        path = path.slice("/devdiscourses".length); // keeps leading slash
    } else {
        return context.next();
    }

    const upstreamUrl = UPSTREAM + path + url.search;
    const upstream = await fetch(upstreamUrl, {
        headers: { "User-Agent": "ImpactMojo/devdiscourses-proxy" },
        redirect: "follow",
    });

    const ct = upstream.headers.get("content-type") || "";
    // Everything except HTML passes through unchanged apart from the policy,
    // which also covers an SVG or other document opened directly.
    if (!ct.includes("text/html")) {
        const headers = new Headers(upstream.headers);
        secure(headers);
        return new Response(upstream.body, { status: upstream.status, headers });
    }

    // HTML: inject <base> so relative asset paths resolve against /devdiscourses/.
    let body = await upstream.text();
    const base = /<base\s/i.test(body) ? "" : `<base href="${BASE_PATH}">`;
    body = body.replace(/<head([^>]*)>/i, `<head$1>${base}${STORAGE_SHIM}`);
    const headers = new Headers(upstream.headers);
    headers.set("content-type", "text/html; charset=utf-8");
    headers.delete("content-length");
    secure(headers);
    return new Response(body, { status: upstream.status, headers });
};

export const config = { path: ["/devdiscourses", "/devdiscourses/*"] };
