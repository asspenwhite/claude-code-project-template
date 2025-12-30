# Security Pre-Commit Checklist

Run through this checklist before committing auth/payment code.

---

## Step 1: Verify Authentication Checks

```bash
# Look for routes without auth verification
grep -r "export async function" src/app/api/ | head -20
```

For each API route, verify:
- [ ] Calls `supabase.auth.getUser()` or equivalent
- [ ] Returns 401 if not authenticated
- [ ] Doesn't trust client-provided user data

---

## Step 2: Verify Authorization

For protected resources:
- [ ] Checks user has permission (role, subscription, ownership)
- [ ] Uses database lookup, not client state
- [ ] Returns 403 if not authorized

---

## Step 3: Verify Webhook Security

For webhook handlers:
- [ ] Verifies signature before processing
- [ ] Uses raw body for signature verification
- [ ] Handles signature failure gracefully
- [ ] Logs webhook events for audit

---

## Step 4: Check for Exposed Secrets

```bash
# Look for hardcoded secrets
grep -r "sk_live\|sk_test\|password\|secret" src/ --include="*.ts" --include="*.tsx"
```

Verify:
- [ ] No API keys in client code
- [ ] No secrets in `NEXT_PUBLIC_*` variables
- [ ] Service role keys only in server code

---

## Step 5: Verify Input Validation

For all user input:
- [ ] Validated on server (not just client)
- [ ] Uses schema validation (Zod, etc.)
- [ ] Sanitizes before database operations
- [ ] Has appropriate length/type limits

---

## Step 6: Check Database Operations

```bash
# Look for client-side inserts to sensitive tables
grep -r "\.insert\|\.update\|\.delete" src/ --include="*.tsx"
```

Verify:
- [ ] Sensitive records created server-side only
- [ ] RLS policies enforce access control
- [ ] No client-side modification of protected data

---

## Quick Validation Commands

```bash
# Run automated security check
python .claude/skills/security/scripts/validate.py src/

# Check for common anti-patterns
grep -r "user_metadata" src/ --include="*.ts" --include="*.tsx"
grep -r "NEXT_PUBLIC.*KEY\|NEXT_PUBLIC.*SECRET" src/
```

---

## Red Flags to Watch For

| Pattern | Risk | Fix |
|---------|------|-----|
| `user_metadata.isPaid` | Payment bypass | Check database table |
| Client-side `.insert()` on orders | Fake orders | Use webhook only |
| `NEXT_PUBLIC_*_SECRET` | Exposed secrets | Move to server-only |
| Missing `getUser()` in API | Auth bypass | Add auth check |
| Webhook without signature check | Fake events | Verify signature |
