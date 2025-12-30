# Security Patterns

Copy-paste secure patterns for common scenarios.

---

## Protected Page (Server Component)

```typescript
// src/app/protected/page.tsx
import { redirect } from 'next/navigation'
import { createClient } from '@/lib/supabase/server'

export default async function ProtectedPage() {
  const supabase = await createClient()
  const { data: { user } } = await supabase.auth.getUser()

  if (!user) {
    redirect('/login')
  }

  // Additional authorization check if needed
  const { data: subscription } = await supabase
    .from('subscriptions')
    .select('status')
    .eq('user_id', user.id)
    .eq('status', 'active')
    .single()

  if (!subscription) {
    redirect('/pricing')
  }

  return <ProtectedContent />
}
```

---

## Protected API Route

```typescript
// src/app/api/protected/route.ts
import { NextResponse } from 'next/server'
import { createClient } from '@/lib/supabase/server'

export async function POST(request: Request) {
  // 1. Verify authentication
  const supabase = await createClient()
  const { data: { user } } = await supabase.auth.getUser()

  if (!user) {
    return NextResponse.json(
      { error: 'Unauthorized' },
      { status: 401 }
    )
  }

  // 2. Verify authorization (if needed)
  const { data: permission } = await supabase
    .from('permissions')
    .select('role')
    .eq('user_id', user.id)
    .single()

  if (!permission || permission.role !== 'admin') {
    return NextResponse.json(
      { error: 'Forbidden' },
      { status: 403 }
    )
  }

  // 3. Process request
  const body = await request.json()

  // 4. Validate input
  if (!body.requiredField) {
    return NextResponse.json(
      { error: 'Missing required field' },
      { status: 400 }
    )
  }

  // 5. Perform action
  const { data, error } = await supabase
    .from('records')
    .insert({ ...body, user_id: user.id })

  if (error) {
    return NextResponse.json(
      { error: 'Failed to create record' },
      { status: 500 }
    )
  }

  return NextResponse.json({ success: true, data })
}
```

---

## Stripe Webhook Handler

```typescript
// src/app/api/webhook/stripe/route.ts
import Stripe from 'stripe'
import { headers } from 'next/headers'
import { createAdminClient } from '@/lib/supabase/admin'

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!)

export async function POST(request: Request) {
  const body = await request.text()
  const headersList = await headers()
  const signature = headersList.get('stripe-signature')!

  // 1. ALWAYS verify webhook signature
  let event: Stripe.Event
  try {
    event = stripe.webhooks.constructEvent(
      body,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET!
    )
  } catch (err) {
    console.error('Webhook signature verification failed')
    return new Response('Invalid signature', { status: 400 })
  }

  // 2. Use admin client for database operations
  const supabase = createAdminClient()

  // 3. Handle events
  switch (event.type) {
    case 'checkout.session.completed': {
      const session = event.data.object as Stripe.Checkout.Session

      // Create record only via webhook (never client-side)
      await supabase.from('orders').insert({
        stripe_session_id: session.id,
        customer_email: session.customer_email,
        status: 'completed',
        amount: session.amount_total,
      })
      break
    }

    case 'customer.subscription.deleted': {
      const subscription = event.data.object as Stripe.Subscription

      // Revoke access
      await supabase
        .from('subscriptions')
        .update({ status: 'cancelled' })
        .eq('stripe_subscription_id', subscription.id)
      break
    }
  }

  return new Response('OK', { status: 200 })
}
```

---

## Admin Route Check

```typescript
// src/app/api/admin/check/route.ts
import { NextResponse } from 'next/server'
import { createClient } from '@/lib/supabase/server'

export async function GET() {
  const supabase = await createClient()
  const { data: { user } } = await supabase.auth.getUser()

  if (!user) {
    return NextResponse.json({ isAdmin: false })
  }

  // Check against server-side admin list (not client-side)
  const { data: adminRole } = await supabase
    .from('admin_roles')
    .select('role')
    .eq('user_id', user.id)
    .single()

  return NextResponse.json({
    isAdmin: !!adminRole,
    role: adminRole?.role || null
  })
}
```

---

## Input Validation

```typescript
// Using Zod for validation
import { z } from 'zod'

const CreateOrderSchema = z.object({
  productId: z.string().uuid(),
  quantity: z.number().int().positive().max(100),
  email: z.string().email(),
})

export async function POST(request: Request) {
  const body = await request.json()

  // Validate input
  const result = CreateOrderSchema.safeParse(body)

  if (!result.success) {
    return NextResponse.json(
      { error: 'Invalid input', details: result.error.issues },
      { status: 400 }
    )
  }

  // Use validated data
  const { productId, quantity, email } = result.data
  // ...
}
```

---

## Anti-Patterns (NEVER DO THIS)

### Wrong: Trusting Client State

```typescript
// WRONG - NEVER DO THIS
const { data: { user } } = await supabase.auth.getUser()
if (user?.user_metadata?.isPaid) {
  // User could fake this in client
  return <PaidContent />
}
```

### Wrong: Client-Side Record Creation

```typescript
// WRONG - NEVER DO THIS
// Client can call this directly and create fake records
await supabase.from('orders').insert({
  user_id: user.id,
  status: 'completed',  // User sets their own status!
})
```

### Wrong: Exposing Secrets

```typescript
// WRONG - NEVER DO THIS
const response = await fetch('/api/data', {
  headers: {
    'Authorization': process.env.STRIPE_SECRET_KEY  // Exposed to client!
  }
})
```

### Wrong: Missing Signature Verification

```typescript
// WRONG - NEVER DO THIS
export async function POST(request: Request) {
  const body = await request.json()
  // Anyone can send fake webhooks!
  await processPayment(body)
}
```
