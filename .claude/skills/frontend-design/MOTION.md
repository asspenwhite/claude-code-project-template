# Motion & Animation Patterns

Focus on HIGH-IMPACT moments. One orchestrated page load beats scattered micro-interactions.

## Page Load Orchestration

Stagger elements with `animation-delay`:

```css
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeIn 0.6s ease forwards;
}

.fade-in:nth-child(1) { animation-delay: 0ms; }
.fade-in:nth-child(2) { animation-delay: 100ms; }
.fade-in:nth-child(3) { animation-delay: 200ms; }
.fade-in:nth-child(4) { animation-delay: 300ms; }

@keyframes fadeIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

## Framer Motion (React)

### Staggered Container

```tsx
import { motion } from 'framer-motion'

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.1 }
  }
}

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 }
}

<motion.div variants={container} initial="hidden" animate="show">
  <motion.div variants={item}>Item 1</motion.div>
  <motion.div variants={item}>Item 2</motion.div>
  <motion.div variants={item}>Item 3</motion.div>
</motion.div>
```

### Scroll-Triggered

```tsx
import { motion, useInView } from 'framer-motion'
import { useRef } from 'react'

function Section() {
  const ref = useRef(null)
  const isInView = useInView(ref, { once: true })

  return (
    <motion.section
      ref={ref}
      initial={{ opacity: 0, y: 50 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.6 }}
    >
      Content appears on scroll
    </motion.section>
  )
}
```

### Button Hover

```tsx
<motion.button
  whileHover={{ scale: 1.02, y: -2 }}
  whileTap={{ scale: 0.98 }}
  transition={{ type: "spring", stiffness: 400 }}
>
  Click me
</motion.button>
```

## CSS-Only Hover States

```css
.card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
}

.button {
  transition: all 0.15s ease;
}

.button:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.button:active {
  transform: translateY(0);
}
```

## Timing Guidelines

| Animation Type | Duration |
|----------------|----------|
| Hover states | 150-200ms |
| Button press | 100ms |
| Page transitions | 300-500ms |
| Stagger delay | 50-100ms |
| Scroll reveals | 400-600ms |

## Easing

```css
/* Smooth deceleration (entering) */
transition-timing-function: cubic-bezier(0, 0, 0.2, 1);

/* Smooth acceleration (exiting) */
transition-timing-function: cubic-bezier(0.4, 0, 1, 1);

/* Bounce effect */
transition-timing-function: cubic-bezier(0.68, -0.55, 0.265, 1.55);
```

## Accessibility

Always respect user preferences:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Anti-Patterns

AVOID:
- Animations longer than 500ms (feels sluggish)
- Bouncing/pulsing elements (distracting)
- Animations that block interaction
- Motion for motion's sake
