# Claude Code Agents

Agents are specialized reviewers you invoke manually via slash commands.

---

## How Agents Work

1. **Manual invocation**: Run via `/command-name`
2. **Focused review**: Each agent has a specific purpose
3. **Checklist-driven**: Structured verification steps
4. **Actionable output**: Clear findings with file:line references

---

## Included Agents

| Agent | Command | Purpose |
|-------|---------|---------|
| design-review | `/design-review` | Visual UI review with screenshots |
| security-audit | `/security-audit` | Auth, payment, data security |
| code-review | `/code-review` | General code quality |
| accessibility | `/accessibility` | WCAG 2.1 AA compliance |
| user-flow-test | `/user-flow-test` | E2E journey testing |
| docs-update | `/docs-update` | Documentation sync |

---

## Using Agents

### Quick Check (Changed Files Only)
```bash
claude /code-review
# Reviews only recently changed files
```

### Full Audit (Entire Codebase)
```bash
claude /security-audit full
# Reviews all security-critical files
```

---

## Agent Output Format

Agents report findings using this structure:

```
## [Category]

### [Issue Title]
- **File:** `path/to/file.tsx:123`
- **Severity:** Critical/High/Medium/Low
- **Finding:** Description of the issue
- **Recommendation:** How to fix it
```

---

## Creating Custom Agents

### File Structure
```
.claude/agents/my-agent.md
.claude/commands/my-command.md
```

### Agent Template
```markdown
# Agent Name

## Philosophy

One-line guiding principle for this agent.

## When to Use

- Scenario 1
- Scenario 2

## Checklist

### Category 1
- [ ] Check item 1
- [ ] Check item 2

### Category 2
- [ ] Check item 3

## Tools to Use

- Tool 1 for purpose 1
- Tool 2 for purpose 2

## Output Format

How to structure findings.
```

### Command Template
```markdown
# /command-name

Brief description.

## Instructions

1. Read the agent config at `.claude/agents/agent-name.md`
2. Follow the checklist
3. Report findings

## Scope

- **Quick:** Changed files only
- **Full:** Entire codebase
```

---

## Best Practices

1. **Run after significant changes** - Not every small edit
2. **Use appropriate scope** - Quick for PRs, full for releases
3. **Act on findings** - Don't ignore issues
4. **Customize for your project** - Update file paths and checks
