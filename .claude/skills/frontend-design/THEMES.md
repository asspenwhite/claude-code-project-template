# Themes & Color Palettes

Pick ONE theme and commit fully. Bold maximalism and refined minimalism both work - the key is intentionality.

## Theme Options

### Warm Professional
Trustworthy, approachable, evokes quality.

```css
:root {
  --primary: #E07A5F;      /* Terracotta */
  --secondary: #3D405B;    /* Deep navy */
  --accent: #F2CC8F;       /* Golden hour */
  --background: #FEFAE0;   /* Warm cream */
  --foreground: #1A1A1A;   /* Rich black */
  --muted: #81B29A;        /* Sage green */
}
```

### Pacific Professional
Clean, modern, trustworthy.

```css
:root {
  --primary: #0F4C5C;      /* Deep teal */
  --secondary: #1A1A2E;    /* Navy black */
  --accent: #E36414;       /* Warm orange */
  --background: #FAFAFA;   /* Off-white */
  --foreground: #1A1A1A;
  --muted: #5F9EA0;        /* Cadet blue */
}
```

### Minimal Dark
Sophisticated, high-contrast, modern.

```css
:root {
  --primary: #FFFFFF;
  --secondary: #A1A1A1;
  --accent: #FFD700;       /* Gold */
  --background: #0A0A0A;
  --foreground: #FFFFFF;
  --muted: #2A2A2A;
}
```

### Soft Pastel
Friendly, approachable, calming.

```css
:root {
  --primary: #6366F1;      /* Indigo */
  --secondary: #818CF8;    /* Light indigo */
  --accent: #F472B6;       /* Pink */
  --background: #FDF4FF;   /* Soft lavender */
  --foreground: #1F2937;
  --muted: #E0E7FF;
}
```

### Editorial Monochrome
Magazine-style, sophisticated.

```css
:root {
  --primary: #1A1A1A;
  --secondary: #4A4A4A;
  --accent: #C41E3A;       /* Crimson accent */
  --background: #FFFEF9;   /* Warm white */
  --foreground: #1A1A1A;
  --muted: #F5F5F5;
}
```

### Dark Slate (Modern SaaS)
Tech-forward, professional.

```css
:root {
  --primary: #F97316;      /* Orange */
  --secondary: #64748B;    /* Slate */
  --accent: #FBBF24;       /* Amber */
  --background: #0F172A;   /* Slate 900 */
  --foreground: #F8FAFC;   /* Slate 50 */
  --muted: #1E293B;        /* Slate 800 */
}
```

## Applying in Tailwind

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: 'var(--primary)',
        secondary: 'var(--secondary)',
        accent: 'var(--accent)',
        background: 'var(--background)',
        foreground: 'var(--foreground)',
        muted: 'var(--muted)',
      },
    },
  },
}
```

## Applying in globals.css

```css
@layer base {
  :root {
    /* Paste your chosen palette here */
  }

  .dark {
    /* Dark mode variant if needed */
  }
}
```

## Color Usage Guidelines

| Element | Use |
|---------|-----|
| CTAs, buttons | `primary` |
| Backgrounds, cards | `background`, `muted` |
| Body text | `foreground` |
| Secondary text | `secondary` |
| Highlights, badges | `accent` |

## Anti-Patterns

NEVER use these combinations:
- Purple (#8B5CF6) on white - screams "AI generated"
- Blue (#3B82F6) buttons everywhere - generic
- Gray (#6B7280) as only accent - boring
- Default Tailwind colors with no customization
