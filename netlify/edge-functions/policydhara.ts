// Netlify Edge Function: proxy PolicyDhara (Astro app on GitHub Pages)
// to /policydhara on impactmojo.in. Same pattern as devdiscourses.ts.
//
// PolicyDhara emits absolute asset URLs under /PolicyDhara/_astro/...
// so we also handle /PolicyDhara/* and proxy those through.

import type { Context } from "https://edge.netlify.com";

const UPSTREAM = "https://varnasr.github.io/PolicyDhara";

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
        headers.delete("content-security-policy");
        headers.delete("x-frame-options");
        return new Response(upstream.body, { status: upstream.status, headers });
    }

    // PolicyDhara already uses absolute /PolicyDhara/... paths, so a <base>
    // tag isn't strictly needed — but inject one anyway for defensiveness.
    let body = await upstream.text();
    if (!/<base\s/i.test(body)) {
        body = body.replace(/<head([^>]*)>/i, `<head$1><base href="/policydhara/">`);
    }
    const headers = new Headers(upstream.headers);
    headers.set("content-type", "text/html; charset=utf-8");
    headers.delete("content-length");
    headers.delete("content-security-policy");
    headers.delete("x-frame-options");
    // Override upstream's max-age=600 — GitHub Pages caches HTML for 10 min,
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
