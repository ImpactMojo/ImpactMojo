# API Reference

## Supabase Schema

### Tables

#### `profiles`

Stores user profile and subscription data. Auto-created on signup via database trigger.

| Column | Type | Description |
|--------|------|-------------|
| `id` | uuid (PK, FK → auth.users) | User ID |
| `email` | text | User email |
| `full_name` | text | Display name |
| `subscription_tier` | text | `explorer`, `practitioner`, `professional`, `organization` |
| `subscription_status` | text | `active`, `expired`, `cancelled` |
| `organization_id` | uuid (nullable) | FK to organizations table |
| `created_at` | timestamptz | Account creation |
| `updated_at` | timestamptz | Last profile update |

#### `organizations`

| Column | Type | Description |
|--------|------|-------------|
| `id` | uuid (PK) | Organization ID |
| `name` | text | Organization name |
| `admin_id` | uuid (FK → profiles) | Org admin user |
| `max_seats` | integer | License seat count |
| `created_at` | timestamptz | Creation date |

### Row Level Security (RLS)

```sql
-- Users can read their own profile
CREATE POLICY "Users can view own profile"
  ON profiles FOR SELECT
  USING (auth.uid() = id);

-- Users can update their own profile
CREATE POLICY "Users can update own profile"
  ON profiles FOR UPDATE
  USING (auth.uid() = id);
```

## Edge Functions

### `mint-resource-token`

Mints a short-lived JWT for accessing premium resource sites.

**Request:**
```
POST /functions/v1/mint-resource-token
Authorization: Bearer <supabase_access_token>
Content-Type: application/json

{
  "resource_id": "rq-builder"
}
```

**Response (200):**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "url": "https://<resource-site>/?token=eyJhbGciOiJIUzI1NiIs..."
}
```

**Response (403):**
```json
{
  "error": "Your subscription tier does not include this resource"
}
```

**JWT Claims:**
```json
{
  "sub": "user-uuid",
  "resource": "rq-builder",
  "tier": "professional",
  "iat": 1710000000,
  "exp": 1710000300
}
```

### `auth-gate.ts` (Netlify Edge Function)

Deployed on each premium resource site. Validates JWT tokens and manages session cookies.

**Flow:**
1. Check for `resource_session` cookie → if valid, allow request
2. Check for `?token=` query parameter → verify JWT signature
3. Verify `resource` claim matches site's `RESOURCE_ID`
4. Set 24-hour `resource_session` cookie
5. Redirect to clean URL (strip token parameter)
6. No cookie + no token → redirect to login page

## Tier Access Matrix

| Resource | Explorer | Practitioner | Professional | Organization |
|----------|----------|--------------|--------------|--------------|
| Free courses & content | Yes | Yes | Yes | Yes |
| RQ Builder | No | Yes | Yes | Yes |
| Code Convert Pro | No | No | Yes | Yes |
| Qual Insights | No | No | Yes | Yes |
| VaniScribe | No | No | Yes | Yes |
| DevData Practice | No | No | Yes | Yes |
| Viz Cookbook | No | No | Yes | Yes |
| DevEcon Toolkit | No | No | Yes | Yes |

## Authentication Flow

```
User clicks "Login" → Supabase Auth (Google OAuth / Magic Link)
                     → Profile auto-created via DB trigger
                     → JWT issued by Supabase
                     → Client stores session in localStorage

User clicks premium tool → js/resource-launch.js
                         → POST mint-resource-token with Supabase JWT
                         → Receives resource JWT
                         → window.open(resourceUrl + '?token=...')
                         → Resource site auth-gate validates token
                         → Sets session cookie, serves tool
```
