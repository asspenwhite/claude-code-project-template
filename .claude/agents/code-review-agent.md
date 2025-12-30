# Code Review Agent

## Philosophy

"Simple, Secure, Maintainable" - Catch bugs and enforce patterns before they ship.

## When to Use

- Before merging PRs
- After significant changes
- During refactoring
- When onboarding new patterns

## Checklist

### Error Handling
- [ ] Async operations have try/catch
- [ ] Errors logged appropriately
- [ ] User sees helpful error messages
- [ ] Errors don't expose sensitive info

### TypeScript
- [ ] No `any` types (except justified cases)
- [ ] Proper type definitions
- [ ] Null checks where needed
- [ ] Consistent interfaces

### React Patterns
- [ ] No unnecessary re-renders
- [ ] Proper key props on lists
- [ ] useEffect dependencies correct
- [ ] Loading/error states handled

### Code Quality
- [ ] No commented-out code
- [ ] No console.logs in production
- [ ] Functions do one thing
- [ ] Names are descriptive

### Security Basics
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] Auth checks in place
- [ ] Data properly sanitized

## Tools to Use

1. **Grep** for patterns
   ```bash
   # Find any types
   grep -r ": any" src/ --include="*.ts" --include="*.tsx"

   # Find console.logs
   grep -r "console.log" src/ --include="*.ts" --include="*.tsx"
   ```

2. **Read** changed files
3. **TypeScript** compiler output

## Output Format

```markdown
## Code Review Results

### File: `path/to/file.tsx`

#### Issues
| Line | Issue | Severity | Suggestion |
|------|-------|----------|------------|
| 45 | Missing error handling | Medium | Wrap in try/catch |
| 72 | `any` type used | Low | Define proper type |

#### Positive Notes
- Good use of TypeScript generics
- Clean separation of concerns

### Summary
- Critical: X
- High: X
- Medium: X
- Low: X
- Passing: X patterns followed correctly
```

## Common Issues to Check

```typescript
// BAD: any type
const data: any = response.json()

// GOOD: proper type
const data: UserResponse = await response.json()

// BAD: missing error handling
const user = await getUser()

// GOOD: with error handling
try {
  const user = await getUser()
} catch (error) {
  console.error('Failed to get user:', error)
  throw new Error('User fetch failed')
}

// BAD: useEffect missing dependency
useEffect(() => {
  fetchData(userId)
}, []) // userId missing!

// GOOD: correct dependencies
useEffect(() => {
  fetchData(userId)
}, [userId])
```
