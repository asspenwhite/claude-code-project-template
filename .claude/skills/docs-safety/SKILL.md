---
name: docs-safety
description: Critical rules for documentation updates. Auto-activates when modifying TODO.md, CHANGELOG.md, or any docs/ files. Prevents history deletion and organization mistakes.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Docs Safety - Critical Rules

These rules apply EVERY TIME you touch documentation files.

## NEVER Do These

```
✗ Delete completed items from TODO.md
✗ Remove project history
✗ Create parallel structures (no "Phase 2:" when "Priority 1:" exists)
✗ Scatter related items across sections
✗ Assume something is test data without asking
✗ Rewrite entire files (make targeted edits)
```

## ALWAYS Do These

```
✓ Mark completed items as [x]
✓ Add to EXISTING sections
✓ Follow existing priority/organization structure
✓ Keep related items grouped
✓ Ask if unsure whether data is real
✓ Update "Last updated" dates
```

## Recovery

```bash
# If you mess up any doc
git checkout docs/TODO.md
git checkout docs/CHANGELOG.md
# Then make targeted edits only
```

## TODO.md Pattern

```markdown
# CORRECT - Add to existing section
### Priority 1: Current Work
- [x] Existing completed item     ← Keep this
- [ ] New item you're adding      ← Add here

# WRONG - Creating parallel structure
### Phase 2: New Work              ← Don't create this
- [ ] Item that belongs above
```

## Verification Before Flagging

Before flagging as "test data to remove":

| Item | Action |
|------|--------|
| Sponsors/Partners | ASK - may be real |
| Revenue numbers | ASK - could be real |
| User accounts | Check if seed data |
| Placeholder text | Safe to flag |

## Checklist

```
- [ ] No completed items deleted
- [ ] Added to existing sections
- [ ] Related items grouped
- [ ] Dates updated
- [ ] No parallel structures created
```
