---
name: netlify-ops
description: Netlify API operations — manage deploys, sites, DNS, environment variables, and build hooks using $NETLIFY_PAT. Use when the user asks about deployments, site configuration, domain management, or Netlify operations.
---

# Netlify Operations Skill

Manage Netlify sites, deploys, and configuration using `$NETLIFY_PAT`.

## Authentication

All API calls use:
```
Authorization: Bearer $NETLIFY_PAT
```

Base URL: `https://api.netlify.com/api/v1`

## Capabilities

### Sites
- List sites: `GET /sites`
- Get site: `GET /sites/{site_id}`
- Update site settings: `PATCH /sites/{site_id}`

### Deploys
- List deploys: `GET /sites/{site_id}/deploys`
- Get deploy: `GET /deploys/{deploy_id}`
- Lock/unlock deploy: `POST /deploys/{deploy_id}/lock` / `POST /deploys/{deploy_id}/unlock`
- Rollback: Lock a previous deploy to roll back

### Environment Variables
- List env vars: `GET /accounts/{account_slug}/env`
- Create env var: `POST /accounts/{account_slug}/env`
- Update env var: `PATCH /accounts/{account_slug}/env/{key}`
- Delete env var: `DELETE /accounts/{account_slug}/env/{key}`

### DNS
- List DNS zones: `GET /dns_zones`
- List DNS records: `GET /dns_zones/{zone_id}/dns_records`
- Create DNS record: `POST /dns_zones/{zone_id}/dns_records`

### Build Hooks
- List build hooks: `GET /sites/{site_id}/build_hooks`
- Create build hook: `POST /sites/{site_id}/build_hooks`
- Trigger build: `POST {build_hook_url}`

### Forms & Submissions
- List forms: `GET /sites/{site_id}/forms`
- List submissions: `GET /forms/{form_id}/submissions`

## Usage Pattern

```bash
curl -s -H "Authorization: Bearer $NETLIFY_PAT" \
  https://api.netlify.com/api/v1/sites
```

## Common Workflows

### Check deploy status
```bash
curl -s -H "Authorization: Bearer $NETLIFY_PAT" \
  "https://api.netlify.com/api/v1/sites/{site_id}/deploys?per_page=5"
```

### Trigger a new build
```bash
curl -s -X POST "https://api.netlify.com/build_hooks/{hook_id}"
```

## Best Practices
- Always verify deploy status after triggering builds
- Use deploy locks for production rollbacks instead of redeploying
- Set environment variables via API, never commit secrets
