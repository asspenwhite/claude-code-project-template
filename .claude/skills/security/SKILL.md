---
name: security
description: Enforces security patterns for authentication, payments, and data protection. Use when working on auth flows, API routes, payment processing, protected resources, or handling user data. Prevents common vulnerabilities.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Security

**Core Rule**: Trust nothing client-side. Server-side validation is the source of truth.

## Critical Rules

### NEVER Do These

1. **Trust client-side auth state** - Always verify on server
2. **Create protected records from client** - Use webhooks or server actions
3. **Send sensitive data to client** - Keep secrets server-side
4. **Skip validation** - Validate all inputs on server

### ALWAYS Do These

1. **Verify auth in API routes** - Check session before processing
2. **Use server-side checks** - For protected pages and actions
3. **Validate webhook signatures** - Never trust unsigned webhooks
4. **Log security events** - Create audit trail

## Reference Files

| Need | File |
|------|------|
| Code patterns & examples | [PATTERNS.md](PATTERNS.md) |
| Pre-commit checklist | [CHECKLIST.md](CHECKLIST.md) |
| Key files to audit | [FILES.md](FILES.md) |

## Validation Script

Before committing auth/payment code, run:

```bash
python .claude/skills/security/scripts/validate.py src/
```

## Checklist Before Completing

```
- [ ] No client-side auth/payment trust
- [ ] Server verifies auth before processing
- [ ] API routes check authentication
- [ ] Sensitive data stays server-side
- [ ] Webhooks verify signatures
- [ ] Inputs validated on server
```
