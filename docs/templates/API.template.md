# [Project Name] - API Documentation

Complete reference for all API routes.

---

## Table of Contents

- [Authentication](#authentication)
- [Routes Overview](#routes-overview)
- [Route Details](#route-details)
- [Error Handling](#error-handling)

---

## Authentication

Most routes require authentication via [your auth method].

```typescript
// Server-side: Get current user
import { createClient } from '@/lib/supabase/server'
const supabase = await createClient()
const { data: { user } } = await supabase.auth.getUser()
```

Webhook routes use signature verification instead.

---

## Routes Overview

| Route | Method | Purpose | Auth Required |
|-------|--------|---------|---------------|
| `/api/[route]` | POST | [Description] | Yes |
| `/api/[route]` | GET | [Description] | No |
| `/api/webhook/[service]` | POST | Handle [service] events | Signature |

### Planned Routes

| Route | Method | Purpose | Notes |
|-------|--------|---------|-------|
| `/api/[future-route]` | POST | [Description] | Not yet implemented |

---

## Route Details

### POST `/api/[route-name]`

[Description of what this route does]

**Request:**
```json
{
  "field1": "value",
  "field2": 123
}
```

**Success Response (200):**
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "field": "value"
  }
}
```

**Error Response (400):**
```json
{
  "error": "Missing required field: field1"
}
```

---

### GET `/api/[route-name]`

[Description]

**Query Parameters:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | Resource ID |
| `limit` | number | No | Max results (default: 10) |

**Success Response (200):**
```json
{
  "data": [],
  "total": 0
}
```

---

### POST `/api/webhook/[service]`

Handles [service] webhook events. Protected by signature verification.

**Handled Events:**
- `event.type.one` - [What it does]
- `event.type.two` - [What it does]

**Security:**
- Requires `[SERVICE]_WEBHOOK_SECRET` environment variable
- Verifies signature header
- Returns 200 for handled events, 400 for unhandled

---

## Error Handling

All routes return consistent error format:

```json
{
  "error": "Human-readable error message"
}
```

**HTTP Status Codes:**

| Code | Meaning | When Used |
|------|---------|-----------|
| `200` | Success | Request completed |
| `201` | Created | Resource created |
| `400` | Bad Request | Missing/invalid params |
| `401` | Unauthorized | Not authenticated |
| `403` | Forbidden | Wrong permissions |
| `404` | Not Found | Resource doesn't exist |
| `409` | Conflict | Duplicate resource |
| `500` | Server Error | Unexpected error |

---

## Design Principles

1. **Server-side validation** - Never trust client data
2. **Auth required** - All user actions need authentication
3. **Rate limiting** - Protect against abuse
4. **Audit logging** - Log sensitive operations
5. **Idempotency** - Webhooks can be safely retried

---

## Environment Variables

| Variable | Purpose | Required |
|----------|---------|----------|
| `[SERVICE]_SECRET_KEY` | API authentication | Yes |
| `[SERVICE]_WEBHOOK_SECRET` | Webhook verification | Yes |

---

*Last updated: [Date]*
