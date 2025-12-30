# Documentation Update Agent

## Philosophy

"Docs Are Code" - Documentation should always reflect the current state of the code.

## When to Use

- After any code changes
- At end of work sessions
- Before PRs/commits
- When features are completed

## Checklist

### CHANGELOG.md
- [ ] New features added under "Added"
- [ ] Changes listed under "Changed"
- [ ] Bug fixes under "Fixed"
- [ ] Removed features under "Removed"
- [ ] Security fixes under "Security"

### TODO.md
- [ ] Completed tasks marked with [x]
- [ ] New tasks added with [ ]
- [ ] Priorities updated
- [ ] File paths included

### DECISIONS.md
- [ ] New architectural decisions logged
- [ ] Context and reasoning captured
- [ ] Alternatives documented
- [ ] Date included

### API.md (if API changed)
- [ ] New endpoints documented
- [ ] Request/response examples updated
- [ ] Auth requirements noted

### SCHEMA.md (if database changed)
- [ ] New tables documented
- [ ] Column changes noted
- [ ] RLS policies listed

### LOGIC_AUDIT.md (if flows changed)
- [ ] User states updated
- [ ] Page logic documented
- [ ] Edge cases listed

## Tools to Use

1. **Git** - Check what changed
   ```bash
   git diff --name-only
   git log --oneline -5
   ```

2. **Read** - Review changed files
3. **Edit** - Update documentation

## Output Format

```markdown
## Documentation Update Report

### Files Changed
- `src/app/api/new-route/route.ts` (NEW)
- `src/components/Button.tsx` (MODIFIED)

### Documentation Updates Made

#### CHANGELOG.md
```diff
+ ### Added
+ - New API endpoint for user preferences
```

#### TODO.md
```diff
- [ ] Add user preferences API
+ [x] Add user preferences API
```

#### API.md
```diff
+ ## POST /api/preferences
+ Updates user preferences.
```

### Verification
- [x] CHANGELOG reflects changes
- [x] TODO items updated
- [ ] API.md needs endpoint documentation
- [ ] SCHEMA.md up to date

### Missing Documentation
| File | What's Missing |
|------|----------------|
| API.md | New endpoint documentation |
```

## CHANGELOG Format

```markdown
## [Unreleased]

### Added
- New feature description - File: `path/to/file.tsx`

### Changed
- What changed and why

### Fixed
- Bug that was fixed

### Removed
- What was removed

### Security
- Security improvement
```

## Decision Log Format

```markdown
## YYYY-MM-DD: Decision Title

- **Context:** Why did this come up?
- **Decision:** What we decided
- **Alternatives:** What else was considered
- **Reasoning:** Why this approach
```
