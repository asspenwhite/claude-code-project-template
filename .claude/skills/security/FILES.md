# Security-Critical Files

Files that require extra scrutiny during security audits.

---

## Authentication Files

| File | Purpose | What to Check |
|------|---------|---------------|
| `src/lib/auth.ts` | Client auth utilities | Never trusts user_metadata |
| `src/lib/auth-server.ts` | Server auth utilities | Checks database, not metadata |
| `src/middleware.ts` | Route protection | Covers all protected paths |
| `src/lib/supabase/server.ts` | Server Supabase client | Proper cookie handling |
| `src/lib/supabase/admin.ts` | Admin client | Only used server-side |

---

## Payment/Webhook Files

| File | Purpose | What to Check |
|------|---------|---------------|
| `src/app/api/webhook/*/route.ts` | Webhook handlers | Signature verification |
| `src/app/api/checkout/route.ts` | Checkout creation | Auth check, price validation |
| `src/app/checkout/success/page.tsx` | Post-payment | Polls for webhook-created record |

---

## Protected Routes

| File | Purpose | What to Check |
|------|---------|---------------|
| `src/app/(protected)/*/page.tsx` | Protected pages | Server-side auth check |
| `src/app/api/*/route.ts` | API routes | Auth before processing |
| `src/app/admin/*/page.tsx` | Admin pages | Role-based access |

---

## Environment Variables

### Safe to Expose (NEXT_PUBLIC_*)
```
NEXT_PUBLIC_SUPABASE_URL
NEXT_PUBLIC_SUPABASE_ANON_KEY
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY
NEXT_PUBLIC_APP_URL
```

### NEVER Expose (Server-only)
```
SUPABASE_SERVICE_ROLE_KEY
STRIPE_SECRET_KEY
STRIPE_WEBHOOK_SECRET
DATABASE_URL
JWT_SECRET
```

---

## Database Tables Requiring RLS

| Table | RLS Policy Needed |
|-------|-------------------|
| `users` | Users read/update own only |
| `orders` | Users read own only, no client insert |
| `subscriptions` | Users read own only |
| `admin_roles` | No public access (service role only) |
| `audit_logs` | Insert only, no read/update/delete |

---

## Files to Review After Changes

When you change auth:
- [ ] All protected routes still check auth
- [ ] Middleware still covers all paths
- [ ] RLS policies still applied

When you change payments:
- [ ] Webhook handlers still verify signatures
- [ ] Success page doesn't trust URL params
- [ ] Client can't create payment records

When you add API routes:
- [ ] Auth check at top of handler
- [ ] Input validation before processing
- [ ] Error responses don't leak info
