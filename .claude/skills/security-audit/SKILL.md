---
name: security-audit
description: Security patterns for auth, API routes, and data protection. Auto-activates when working on authentication, API endpoints, database queries, or handling user data.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Security Audit - Protection Patterns

Apply these patterns when working on auth, APIs, or user data.

## Core Rule

**Trust nothing client-side. Server-side validation is the source of truth.**

## Authentication

```
✓ Verify session/token on every protected route
✓ Check user roles/permissions server-side
✓ Use secure session management
✓ Implement proper logout (invalidate tokens)
✗ Never trust client-side auth state alone
✗ Never skip auth checks for "internal" routes
✗ Never store sensitive data in localStorage
```

## API Security

```
✓ Validate all input parameters
✓ Use parameterized queries (prevent SQL injection)
✓ Rate limit public endpoints
✓ Return generic errors to clients
✗ Never expose stack traces to users
✗ Never trust request headers blindly
✗ Never log sensitive data
```

## Data Protection

```
✓ Encrypt sensitive data at rest
✓ Use HTTPS everywhere
✓ Implement proper CORS policies
✓ Sanitize user input before display (prevent XSS)
✗ Never store passwords in plain text
✗ Never expose internal IDs unnecessarily
✗ Never return more data than needed
```

## Secrets Management

```
✓ Use environment variables for secrets
✓ Different secrets per environment
✓ Rotate secrets regularly
✗ Never commit secrets to git
✗ Never log API keys or tokens
✗ Never expose secrets in client bundles
```

## Common Vulnerabilities

| Vulnerability | Prevention |
|---------------|------------|
| SQL Injection | Parameterized queries |
| XSS | Sanitize output, CSP headers |
| CSRF | CSRF tokens on mutations |
| Auth Bypass | Server-side checks always |
| Data Exposure | Minimal data in responses |

## Checklist

```
- [ ] Auth verified server-side
- [ ] Input validated
- [ ] Output sanitized
- [ ] Secrets not exposed
- [ ] Errors don't leak info
- [ ] Rate limiting in place
```
