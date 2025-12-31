# [Project Name] - Logic Audit

Complete documentation of user states, routing logic, and application flow.

---

## Table of Contents

- [User States](#user-states)
- [Page-by-Page Logic](#page-by-page-logic)
- [Database Queries](#database-queries)
- [Component Reference](#component-reference)
- [Edge Cases](#edge-cases)
- [Testing Checklist](#testing-checklist)

---

## User States

A user can be in one of these states at any time:

| State | Description | Authenticated | Has Paid | Additional Conditions |
|-------|-------------|---------------|----------|----------------------|
| `visitor` | Not logged in | No | No | - |
| `registered` | Has account, free tier | Yes | No | - |
| `subscribed` | Paid customer | Yes | Yes | - |
| `[custom]` | [Description] | [Yes/No] | [Yes/No] | [Conditions] |

---

## Page-by-Page Logic

### Homepage (`/`)

**File:** `src/app/page.tsx`

| Element | User State | Behavior |
|---------|------------|----------|
| Main CTA | visitor | Shows "Get Started" → `/signup` |
| Main CTA | registered | Shows "Upgrade" → `/pricing` |
| Main CTA | subscribed | Shows "Dashboard" → `/dashboard` |

**Status:** [ ] Not implemented / [x] Implemented

---

### Dashboard (`/dashboard`)

**File:** `src/app/dashboard/page.tsx`

| Condition | Behavior |
|-----------|----------|
| Not authenticated | Redirect → `/login` |
| Not subscribed | Redirect → `/pricing` |
| Subscribed | Show dashboard |

**Key Logic:**
```typescript
if (!user) redirect('/login')
if (!subscription) redirect('/pricing')
// Show dashboard
```

**Status:** [ ] Not implemented / [x] Implemented

---

### [Page Name] (`/route`)

**File:** `src/app/route/page.tsx`

| Condition | Behavior |
|-----------|----------|
| [Condition 1] | [What happens] |
| [Condition 2] | [What happens] |

**Status:** [ ] Not implemented / [x] Implemented

---

## Database Queries

### Check User Subscription

```typescript
// Client-side
const { data } = await supabase
  .from('subscriptions')
  .select('*')
  .eq('user_id', userId)
  .eq('status', 'active')
  .single()
```

### [Query Name]

```typescript
// Description of what this query does
const { data } = await supabase
  .from('table')
  .select('columns')
  .eq('condition', value)
```

---

## Component Reference

### [ComponentName]

**File:** `src/components/ComponentName.tsx`

**Purpose:** [What it does]

**Props:**
```typescript
interface Props {
  prop1: string
  prop2?: boolean
}
```

**Usage:**
```tsx
<ComponentName prop1="value" />
```

---

## Edge Cases

Document edge cases and how they're handled:

### [Edge Case Name]
- **Scenario:** [What can happen]
- **Handling:** [How we handle it]
- **Status:** [ ] Not handled / [x] Handled

### User refreshes during checkout
- **Scenario:** User refreshes page mid-payment
- **Handling:** [Describe recovery mechanism]
- **Status:** [ ] Not handled / [x] Handled

### Webhook arrives before redirect
- **Scenario:** Stripe webhook processes before user returns
- **Handling:** [Describe polling/retry logic]
- **Status:** [ ] Not handled / [x] Handled

---

## Testing Checklist

### Visitor Flow
- [ ] Can view homepage
- [ ] CTA shows correct state
- [ ] Can navigate to signup
- [ ] Can complete signup

### Authenticated User Flow
- [ ] Can log in
- [ ] Redirected appropriately based on subscription
- [ ] Can access authorized pages
- [ ] Cannot access unauthorized pages

### Payment Flow
- [ ] Can initiate checkout
- [ ] Payment processes correctly
- [ ] Webhook creates subscription
- [ ] User gains access after payment

### Edge Cases
- [ ] Refresh during checkout handled
- [ ] Duplicate webhooks handled
- [ ] Failed payment shows error
- [ ] Expired session handled

---

## RLS Policies

### [table_name]

```sql
-- Policy name and purpose
CREATE POLICY "policy_name"
ON table_name FOR [SELECT/INSERT/UPDATE/DELETE]
USING (condition)
WITH CHECK (condition);
```

---

*Last updated: [Date]*
