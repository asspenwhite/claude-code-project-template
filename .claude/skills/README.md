# Claude Code Skills

Skills are domain knowledge that auto-activate when Claude is working on relevant tasks.

---

## How Skills Work

1. **Auto-activation**: Skills load automatically based on task relevance
2. **Progressive disclosure**: Only loads what's needed to save tokens
3. **Creation-time guidance**: Prevents mistakes before they happen

---

## Included Skills

### frontend-design

Prevents "AI slop" - the generic patterns Claude defaults to.

**Activates when:** Building UI components, pages, styling, visual work

**Prevents:**
- Inter/Roboto/Arial fonts
- Purple gradients on white
- Cookie-cutter layouts
- Default shadcn styling unchanged

### security

Enforces secure patterns for auth, payments, and data protection.

**Activates when:** Working on auth, payment, API routes, protected resources

**Prevents:**
- Client-side security checks
- Exposed secrets
- Missing auth verification
- Insecure data handling

---

## Creating Custom Skills

### File Structure

```
.claude/skills/your-skill/
├── SKILL.md           # Core rules (keep under 500 lines)
├── PATTERNS.md        # Detailed code patterns
├── CHECKLIST.md       # Pre-completion checklist
└── scripts/           # Validation scripts (optional)
    └── validate.py
```

### SKILL.md Format

```markdown
---
name: skill-name
description: When this skill should activate. Be specific.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Skill Name

Brief overview.

## Core Rules

The most important rules that ALWAYS apply.
Keep this section short and scannable.

## Reference Files

| Need | File |
|------|------|
| Patterns | [PATTERNS.md](PATTERNS.md) |
| Checklist | [CHECKLIST.md](CHECKLIST.md) |

## Checklist Before Completing

- [ ] Rule 1 followed
- [ ] Rule 2 followed
```

### Guidelines

- **SKILL.md under 500 lines** - Ideally 50-100
- **Put details in reference files** - Load on demand
- **Use tables for quick scanning** - Not prose
- **Include a checklist** - Verifiable completion criteria

---

## Progressive Disclosure

Skills load in 3 levels:

1. **Metadata** (~100 tokens) - Always loaded
2. **SKILL.md body** - When task matches
3. **Reference files** - Only when needed

This saves 50-80% of tokens compared to loading everything.
