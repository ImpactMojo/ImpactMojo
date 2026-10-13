// Netlify Edge Function: proxy PolicyDhara (Astro app on GitHub Pages)
// to /policydhara on impactmojo.in. Same pattern as devdiscourses.ts.
//
// PolicyDhara emits absolute asset URLs under /PolicyDhara/_astro/...
// so we also handle /PolicyDhara/* and proxy those through.
//
// Isolation, as in devdiscourses.ts: every response carries a
// Content-Security-Policy with `sandbox` and no `allow-same-origin`, so the
// page runs in an opaque origin and its scripts cannot read this site's
// storage or cookies, register a service worker here, or reach Supabase.
// connect-src is 'self' only. The newsletter form posts to Buttondown, which
// form-action allows. The injected storage script gives the page an
// in-memory localStorage, so the theme, bookmarks and "last visit" work for
// the visit and are not remembered afterwards.

import type { Context } from "https://edge.netlify.com";

const UPSTREAM = "https://varnasr.github.io/PolicyDhara";

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
    "form-action 'self' https://buttondown.com",
    "frame-ancestors 'self'",
].join("; ");

// In-memory Storage for a sandboxed page, where localStorage throws.
const STORAGE_SHIM = `<script>(function(){function m(){var d={};return{getItem:function(k){k=String(k);return Object.prototype.hasOwnProperty.call(d,k)?d[k]:null},setItem:function(k,v){d[String(k)]=String(v)},removeItem:function(k){delete d[String(k)]},clear:function(){d={}},key:function(i){var a=Object.keys(d);return i<a.length?a[i]:null},get length(){return Object.keys(d).length}}};["localStorage","sessionStorage"].forEach(function(n){try{window[n].getItem("x")}catch(e){try{Object.defineProperty(window,n,{value:m(),configurable:true})}catch(_){}}})})();</script>`;

function secure(headers: Headers) {
    headers.append("content-security-policy", CSP);
    headers.set("x-content-type-options", "nosniff");
}

export default async (request: Request, context: Context) => {
    const url = new URL(request.url);
    let path = url.pathname;

    if (path === "/policydhara" || path === "/policydhara/") {
        path = "/";
    } else if (path.startsWith("/policydhara/")) {
        path = path.slice("/policydhara".length);
    } else if (path.startsWith("/PolicyDhara/")) {
        path = path.slice("/PolicyDhara".length);
    } else {
        return context.next();
    }

    const upstreamUrl = UPSTREAM + path + url.search;
    const upstream = await fetch(upstreamUrl, {
        headers: { "User-Agent": "ImpactMojo/policydhara-proxy" },
        redirect: "follow",
    });

    const ct = upstream.headers.get("content-type") || "";
    if (!ct.includes("text/html")) {
        // Assets (CSS/JS/images) ship from Astro with content-hashed filenames,
        // so upstream's long cache is safe to pass through.
        const headers = new Headers(upstream.headers);
        secure(headers);
        return new Response(upstream.body, { status: upstream.status, headers });
    }

    // PolicyDhara already uses absolute /PolicyDhara/... paths, so a <base>
    // tag isn't strictly needed, but inject one anyway for defensiveness.
    let body = await upstream.text();
    const base = /<base\s/i.test(body) ? "" : `<base href="/policydhara/">`;
    body = body.replace(/<head([^>]*)>/i, `<head$1>${base}${STORAGE_SHIM}`);
    const headers = new Headers(upstream.headers);
    headers.set("content-type", "text/html; charset=utf-8");
    headers.delete("content-length");
    secure(headers);
    // Override upstream's max-age=600: GitHub Pages caches HTML for 10 min,
    // which means upstream PolicyDhara deploys took up to 10 min to appear here.
    // Short browser cache + stale-while-revalidate keeps TTFB fast but lets
    // edits propagate within ~60s of an upstream deploy.
    headers.set(
        "cache-control",
        "public, max-age=60, s-maxage=60, stale-while-revalidate=600",
    );
    return new Response(body, { status: upstream.status, headers });
};

export const config = {
    path: ["/policydhara", "/policydhara/*", "/PolicyDhara/*"],
};
