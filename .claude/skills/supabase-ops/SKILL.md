---
name: supabase-ops
description: Supabase Management API operations — manage databases, migrations, edge functions, auth, and storage using $SUPABASE_PAT. Use when the user asks about database operations, migrations, edge function deployment, or Supabase administration.
---

# Supabase Operations Skill

Manage Supabase projects using `$SUPABASE_PAT` (Management API) and project-level keys for data operations.

## Authentication

### Management API (project admin)
```
Authorization: Bearer $SUPABASE_PAT
```
Base URL: `https://api.supabase.com/v1`

### Data API (client-side queries)
```
apikey: {SUPABASE_ANON_KEY}
Authorization: Bearer {SUPABASE_ANON_KEY}
```
Base URL: `https://{project_ref}.supabase.co`

## Management API Capabilities

### Projects
- List projects: `GET /projects`
- Get project: `GET /projects/{ref}`

### Database
- Run SQL: `POST /projects/{ref}/database/query` with `{"query": "SELECT ..."}`
- List tables: Query `information_schema.tables`
- List migrations: `GET /projects/{ref}/database/migrations`

### Edge Functions
- List functions: `GET /projects/{ref}/functions`
- Get function: `GET /projects/{ref}/functions/{slug}`
- Create function: `POST /projects/{ref}/functions`
- Update function: `PATCH /projects/{ref}/functions/{slug}`
- Delete function: `DELETE /projects/{ref}/functions/{slug}`

### Auth
- List users: `GET /projects/{ref}/auth/users`
- Auth config: `GET /projects/{ref}/config/auth`

### Storage
- List buckets: Via Data API `GET /storage/v1/bucket`
- Bucket operations: Create, update, delete buckets

### Secrets
- List secrets: `GET /projects/{ref}/secrets`
- Create secrets: `POST /projects/{ref}/secrets`
- Delete secrets: `DELETE /projects/{ref}/secrets`

## Usage Pattern

```bash
# Management API
curl -s -H "Authorization: Bearer $SUPABASE_PAT" \
  https://api.supabase.com/v1/projects/{ref}

# Data API (direct DB queries via PostgREST)
curl -s -H "apikey: {anon_key}" \
  -H "Authorization: Bearer {anon_key}" \
  "https://{ref}.supabase.co/rest/v1/table_name?select=*"
```

## Common Workflows

### Run a migration
```bash
curl -s -X POST \
  -H "Authorization: Bearer $SUPABASE_PAT" \
  -H "Content-Type: application/json" \
  -d '{"query": "ALTER TABLE ..."}' \
  https://api.supabase.com/v1/projects/{ref}/database/query
```

### Deploy edge function
Use the Supabase CLI (`supabase functions deploy {slug}`) or the Management API.

### Set edge function secrets
```bash
curl -s -X POST \
  -H "Authorization: Bearer $SUPABASE_PAT" \
  -H "Content-Type: application/json" \
  -d '[{"name": "KEY", "value": "val"}]' \
  https://api.supabase.com/v1/projects/{ref}/secrets
```

## Best Practices
- Use Management API for admin operations, Data API for CRUD
- Always test migrations on a branch/staging project first
- Never expose service_role keys in client-side code
- Use RLS (Row Level Security) policies for all public tables
