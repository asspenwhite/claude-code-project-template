---
name: design-review
description: UI quality and consistency patterns. Auto-activates when building UI components, styling, or visual work.
allowed-tools: Read, Write, Edit, Glob, Grep, mcp__playwright__browser_snapshot, mcp__playwright__browser_navigate
---

# Design Review - UI Quality Patterns

Apply these patterns when building or reviewing UI.

## Consistency

```
✓ Follow established color palette
✓ Use design tokens/CSS variables
✓ Match existing component patterns
✓ Consistent spacing (use spacing scale)
✗ Don't introduce new colors without reason
✗ Don't use magic pixel values
✗ Don't deviate from established patterns
```

## Accessibility

```
✓ Sufficient color contrast (4.5:1 for text)
✓ Focus states visible
✓ Alt text on images
✓ Semantic HTML elements
✓ Keyboard navigable
✗ No color-only indicators
✗ No images of text
```

## Responsive Design

```
✓ Mobile-first approach
✓ Test at common breakpoints
✓ Touch targets 44x44px minimum
✓ Readable text at all sizes
✗ No horizontal scroll on mobile
✗ No fixed widths that break small screens
```

## Component Patterns

```
✓ Clear visual hierarchy
✓ Consistent border radius
✓ Meaningful hover/active states
✓ Loading skeletons match content shape
✗ No orphaned elements
✗ No inconsistent button styles
```

## Playwright Verification

When building UI, verify with Playwright:
```
1. browser_navigate to page
2. browser_snapshot for accessibility tree
3. Check visual consistency
4. Verify responsive behavior
5. Test interactive states
```

## Checklist

```
- [ ] Matches design system
- [ ] Accessible (contrast, focus, alt text)
- [ ] Responsive at all breakpoints
- [ ] Interactions work correctly
- [ ] Loading states present
```
