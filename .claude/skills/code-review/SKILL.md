---
name: code-review
description: Code quality patterns for TypeScript and React. Auto-activates when writing or modifying code files.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Code Review - Quality Patterns

Apply these patterns when writing or reviewing code.

## TypeScript

```
✓ Explicit types for function parameters
✓ Interfaces over type aliases for objects
✓ Zod schemas for external/user data
✓ Proper error handling with typed errors
✗ No `any` types without justification
✗ No implicit any
✗ No type assertions without validation
```

## React Patterns

```
✓ Keys on mapped elements
✓ Loading and error states handled
✓ Empty states designed
✓ Proper cleanup in useEffect
✗ No unnecessary useEffect
✗ No inline object/function definitions in props
✗ No state that can be derived
```

## Code Quality

```
✓ Error messages are user-friendly
✓ Constants instead of magic numbers
✓ DRY - extract repeated logic
✓ Single responsibility functions
✗ No console.log in production
✗ No commented-out code
✗ No overly complex functions (>50 lines)
```

## Performance

```
✓ Memoize expensive calculations
✓ Lazy load heavy components
✓ Paginate large lists
✗ No N+1 queries
✗ No unnecessary re-renders
✗ No blocking operations on main thread
```

## Security

```
✓ Validate all user input
✓ Sanitize output to prevent XSS
✓ Use parameterized queries
✗ No secrets in client code
✗ No eval() or innerHTML with user data
```

## Checklist

```
- [ ] Types are explicit and correct
- [ ] Error states handled
- [ ] No console.log left behind
- [ ] Performance considered
- [ ] Security checked
```
