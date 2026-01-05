# Claude Code Skills

Skills are domain knowledge that auto-activate when Claude is working on relevant tasks.

## Skills vs Agents

| Aspect | Skills | Agents |
|--------|--------|--------|
| **Activation** | Automatic (task detection) | Manual (`/command`) |
| **Purpose** | Prevention during work | Review after work |
| **Scope** | Rules that always apply | Comprehensive audits |
| **Use when** | Building/coding | Ready for review |

**Use skills for ongoing protection, agents for thorough reviews.**

---

## Core Skills (Always Active)

These skills provide guardrails that apply during everyday work.

### docs-safety
**Activates when:** Modifying TODO.md, CHANGELOG.md, or docs/ files

Prevents documentation mistakes:
- Never delete completed items (mark as [x])
- Add to existing sections (no parallel structures)
- Ask before flagging real data as placeholder

### code-review
**Activates when:** Writing or modifying code files

Enforces code quality patterns:
- TypeScript types and error handling
- React best practices
- Performance and security basics

### design-review
**Activates when:** Building UI components, styling, visual work

Ensures UI quality:
- Consistency with design system
- Accessibility requirements
- Responsive design patterns

### security-audit
**Activates when:** Auth, API routes, database queries, user data

Enforces security patterns:
- Server-side validation
- Input sanitization
- Secrets management

---

## Feature Skills

These skills provide domain-specific knowledge.

### frontend-design

Prevents "AI slop" - the generic patterns Claude defaults to.

**Activates when:** Building UI components, pages, styling

**Prevents:**
- Generic fonts (Inter/Roboto)
- Default color schemes
- Cookie-cutter layouts

### security

Deep security patterns for auth, payments, and data protection.

**Activates when:** Working on auth, payment, API routes

**Reference Files:**
- `PATTERNS.md` - Code patterns
- `CHECKLIST.md` - Pre-commit checklist
- `FILES.md` - Critical files

---

## How Skills Work

1. **Auto-activation**: Skills load automatically based on task relevance
2. **Progressive disclosure**: Only loads what's needed to save tokens
3. **Creation-time guidance**: Prevents mistakes before they happen

Skills load in 3 levels:
1. **Metadata** (~100 tokens) - Always loaded
2. **SKILL.md body** - When task matches
3. **Reference files** - Only when needed

---

## Creating Custom Skills

### File Structure

```
.claude/skills/your-skill/
├── SKILL.md           # Core rules (keep under 500 lines)
├── PATTERNS.md        # Detailed code patterns
├── CHECKLIST.md       # Pre-completion checklist
└── scripts/           # Validation scripts (optional)
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

## Checklist Before Completing

- [ ] Rule 1 followed
- [ ] Rule 2 followed
```

### Guidelines

- **SKILL.md under 500 lines** - Ideally 50-100
- **Put details in reference files** - Load on demand
- **Use tables for quick scanning** - Not prose
- **Include a checklist** - Verifiable completion criteria
