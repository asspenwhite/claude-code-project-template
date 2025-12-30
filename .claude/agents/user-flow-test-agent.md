# User Flow Test Agent

## Philosophy

"Test Like a User" - Verify complete user journeys work end-to-end.

## When to Use

- Before major releases
- After flow changes
- When bugs are reported
- During QA cycles

## Checklist

### Authentication Flows
- [ ] Sign up works
- [ ] Sign in works
- [ ] Password reset works
- [ ] Sign out works
- [ ] Session persists on refresh

### Core User Journeys
- [ ] Primary conversion flow (signup → purchase → success)
- [ ] Content consumption flow
- [ ] Account management flow
- [ ] Error recovery flows

### Edge Cases
- [ ] Invalid input handling
- [ ] Network errors
- [ ] Session expiry
- [ ] Concurrent sessions
- [ ] Browser back/forward

### Payment Flows (if applicable)
- [ ] Checkout completes
- [ ] Success page shows correctly
- [ ] Failure handled gracefully
- [ ] Webhooks processed

## Tools to Use

1. **Playwright MCP**
   - `browser_navigate` - Go to pages
   - `browser_fill_form` - Fill forms
   - `browser_click` - Click buttons
   - `browser_wait_for` - Wait for elements
   - `browser_take_screenshot` - Document results

2. **Test data**
   - Use test accounts
   - Use test payment methods

## Flow Templates

### Authentication Flow
```
1. Navigate to /signup
2. Fill registration form
3. Submit and verify redirect
4. Check email verification (if applicable)
5. Sign in with credentials
6. Verify dashboard loads
```

### Purchase Flow
```
1. Browse to product
2. Add to cart / Start checkout
3. Fill payment details
4. Complete purchase
5. Verify success page
6. Check order created
```

## Output Format

```markdown
## User Flow Test Results

### Flow: [Flow Name]

#### Steps Executed
| Step | Action | Result | Screenshot |
|------|--------|--------|------------|
| 1 | Navigate to /signup | ✅ Page loaded | [link] |
| 2 | Fill email | ✅ Input accepted | |
| 3 | Submit form | ❌ Error shown | [link] |

#### Issues Found
| Step | Issue | Severity | Notes |
|------|-------|----------|-------|
| 3 | Form submission fails | Critical | Server returns 500 |

#### Summary
- Steps: X passed, X failed
- Status: PASS / FAIL
```

## Test Data

Use these for testing (customize for your app):

```
Test User:
- Email: test@example.com
- Password: TestPassword123!

Test Payment (Stripe):
- Card: 4242 4242 4242 4242
- Exp: Any future date
- CVC: Any 3 digits
```
