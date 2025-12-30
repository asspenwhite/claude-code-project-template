---
name: frontend-design
description: Creates distinctive, production-grade frontend interfaces avoiding generic AI aesthetics. Use when building UI components, pages, styling, or any visual/frontend work. Prevents AI slop (Inter fonts, purple gradients, cookie-cutter layouts).
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(npm:*), Bash(npx:*)
---

# Frontend Design

Create distinctive interfaces that avoid "AI slop" - the generic patterns Claude defaults to without guidance.

## Quick Start

Before coding any UI, answer these questions:

1. **Purpose**: What problem does this solve?
2. **Tone**: Pick ONE theme from [THEMES.md](THEMES.md) and commit fully
3. **Differentiation**: What's the ONE thing someone will remember?

## Core Rules

### Typography - NEVER Use
- Inter, Roboto, Arial, Open Sans, Lato, system fonts as primary

### Colors - NEVER Use
- Purple gradients on white backgrounds
- Generic blue (#0066CC, #3B82F6)
- Default Tailwind colors unchanged

### Layouts - NEVER Use
- Centered content with no visual interest
- Cookie-cutter card grids
- Default shadcn/ui styling unchanged

## Reference Files

| Need | File |
|------|------|
| Font pairings & type scale | [TYPOGRAPHY.md](TYPOGRAPHY.md) |
| Color palettes & themes | [THEMES.md](THEMES.md) |
| Animation patterns | [MOTION.md](MOTION.md) |
| Before/after examples | [EXAMPLES.md](EXAMPLES.md) |

## Checklist Before Completing

```
- [ ] No Inter/Roboto/Arial fonts
- [ ] No purple-on-white gradients
- [ ] Custom color palette applied
- [ ] At least one animation/transition
- [ ] Backgrounds have depth (not plain white)
- [ ] Typography has clear hierarchy
```
