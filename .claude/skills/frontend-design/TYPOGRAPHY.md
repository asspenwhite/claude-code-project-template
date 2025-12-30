# Typography Reference

## Recommended Font Pairings

### Modern Professional
```css
--font-display: 'General Sans', sans-serif;
--font-body: 'Satoshi', sans-serif;
```

### Editorial/Magazine
```css
--font-display: 'Playfair Display', serif;
--font-body: 'Source Sans Pro', sans-serif;
```

### Tech/Developer
```css
--font-display: 'Cabinet Grotesk', sans-serif;
--font-body: 'Inter', sans-serif;  /* OK for body if display is distinctive */
--font-mono: 'JetBrains Mono', monospace;
```

### Friendly/Approachable
```css
--font-display: 'Bricolage Grotesque', sans-serif;
--font-body: 'Plus Jakarta Sans', sans-serif;
```

### Bold/Impactful
```css
--font-display: 'Clash Display', sans-serif;
--font-body: 'Switzer', sans-serif;
```

## Type Scale

Use aggressive size jumps for clear hierarchy:

```css
/* Mobile */
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.25rem;    /* 20px */
--text-xl: 1.5rem;     /* 24px */
--text-2xl: 2rem;      /* 32px */
--text-3xl: 2.5rem;    /* 40px */
--text-4xl: 3.5rem;    /* 56px */

/* Desktop - more dramatic */
--text-hero: 4.5rem;   /* 72px */
--text-display: 3.5rem; /* 56px */
```

## Weight Contrast

Pair extreme weights for impact:

```css
/* Headers: Bold or Black */
h1, h2 { font-weight: 700; } /* or 800, 900 */

/* Body: Regular or Light */
p { font-weight: 400; } /* or 300 */

/* Subtle labels */
.label { font-weight: 500; letter-spacing: 0.05em; text-transform: uppercase; }
```

## Letter Spacing

```css
/* Tight for large headlines */
.headline { letter-spacing: -0.02em; }

/* Normal for body */
.body { letter-spacing: 0; }

/* Wide for small caps/labels */
.label { letter-spacing: 0.1em; }
```

## Google Fonts CDN

```html
<!-- Outfit (General Sans alternative) -->
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<!-- Playfair Display + Source Sans -->
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Source+Sans+Pro:wght@300;400;600&display=swap" rel="stylesheet">

<!-- Plus Jakarta Sans -->
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

## Tailwind Config

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        display: ['Outfit', 'sans-serif'],
        body: ['Plus Jakarta Sans', 'sans-serif'],
      },
    },
  },
}
```
