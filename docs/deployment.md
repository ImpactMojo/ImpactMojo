# Deployment Guide

## Main Site (impactmojo.in)

### Netlify Setup

The main site deploys automatically from the `main` branch on GitHub.

- **Build command:** None (static site)
- **Publish directory:** `.` (root)
- **Custom domain:** `www.impactmojo.in`

### Clean URL Routing

The `_redirects` file rewrites clean URLs to `index.html`:
```
/courses    /index.html   200
/labs       /index.html   200
/about      /index.html   200
```

The `js/router.js` script reads the URL path and opens the corresponding section/modal.

### Supabase Configuration

1. Create a Supabase project
2. Enable authentication (Email, Google OAuth, Magic Links)
3. Create the `profiles` table (see README for schema)
4. Copy the **anon key** and **project URL** to `js/auth.js`
5. Deploy the `mint-resource-token` Edge Function with `supabase functions deploy`

### Supabase Edge Function

```bash
cd supabase
supabase secrets set RESOURCE_TOKEN_SECRET="your-hmac-secret-here"
supabase functions deploy mint-resource-token
```

## Premium Resource Sites

Each premium tool is a separate Netlify site with a JWT auth-gate edge function.

### Setup Steps (per site)

1. **Create site** on Netlify (manual deploy or linked repo)

2. **Set environment variables** in Netlify dashboard → Site settings → Environment variables:
   - `RESOURCE_TOKEN_SECRET` — same HMAC key used in Supabase Edge Function (set as "Secret", Production context)
   - `RESOURCE_ID` — unique slug for this site (not secret, all contexts)

3. **Deploy with edge function:**
   - Include `netlify.toml` in the site root
   - Include `netlify/edge-functions/auth-gate.ts`
   - Deploy via Netlify CLI or API

### Resource ID Mapping

| Site | RESOURCE_ID |
|------|-------------|
| *(private — see Netlify dashboard)* | `rq-builder` |
| *(private — see Netlify dashboard)* | `code-convert-pro` |
| *(private — see Netlify dashboard)* | `qual-insights` |
| *(private — see Netlify dashboard)* | `vaniscribe` |

### Generating a New HMAC Secret

```bash
openssl rand -base64 32
```

Use the same secret across all resource sites and the Supabase Edge Function.

### Verifying the Auth Gate

After deployment, visit the resource site directly. You should be redirected to:
```
https://www.impactmojo.in/login?reason=expired
```

If you see a 500 error, check that both `RESOURCE_TOKEN_SECRET` and `RESOURCE_ID` are set correctly.

## Adding a New Premium Resource Site

1. Create the tool as a static HTML/JS site
2. Deploy to Netlify
3. Add `RESOURCE_TOKEN_SECRET` and `RESOURCE_ID` env vars
4. Deploy with the auth-gate edge function (use `netlify-resource-template/`)
5. Add the resource ID to the tier ACL in `supabase/functions/mint-resource-token/index.ts`
6. Add the URL to `RESOURCE_URLS` in `js/resource-launch.js`
7. Add a card on `premium.html` with `data-resource-id="your-id"`
