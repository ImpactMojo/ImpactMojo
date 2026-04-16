# Chamber Petition (AOR)

Petition page for Advocates-on-Record at the Supreme Court of India requesting
chambers instead of work-stations.

## Deployment

- **Live site**: https://chamber-petition.netlify.app/
- **Netlify site ID**: `6581a696-c2d1-4a16-bcdf-681dc517762b`
- **Backend**: Netlify Forms (migrated from Supabase on 2026-04-16)
- **No git integration** — deploys happen via Netlify API / drag-drop

## Architecture

- Single static `index.html` (no build step)
- Form submits to Netlify Forms (`name="aor-petition"`)
- Signature count displayed as baseline (67) + local session increments
- True total visible in Netlify Forms dashboard

## History

- **2025-12-27**: Original Supabase version launched
- **2026-03-31**: 67th signature collected (last before migration)
- **2026-04-16**: Migrated to Netlify Forms, Supabase `AORPetition` project deleted

## Backup

`signatures-backup-2026-04-16.json` contains all 67 signatures exported from
Supabase before the migration. Format:

```json
{
  "id": "uuid",
  "name": "...",
  "bar_id": "...",
  "aor_no": "...",
  "email": "...",
  "phone": "...",
  "signed_at": "ISO timestamp"
}
```

## Redeploy

```bash
# Via Netlify CLI (not currently configured), or via API:
curl -X POST -H "Authorization: Bearer $NETLIFY_PAT" \
  -H "Content-Type: application/zip" \
  --data-binary @chamber-petition.zip \
  "https://api.netlify.com/api/v1/sites/6581a696-c2d1-4a16-bcdf-681dc517762b/deploys"
```
