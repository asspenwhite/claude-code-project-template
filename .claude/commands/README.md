# Commands

Commands are slash-invoked shortcuts that trigger Agents with predefined configurations.

## How Commands Work

```
User types: /design-review
Claude reads: .claude/commands/design-review.md
Claude loads: .claude/agents/design-review-agent.md
Claude runs: Agent checklist on current context
```

## Command Syntax

Commands use `$ARGUMENTS` for user input:

```markdown
Review the design of $ARGUMENTS using the design review agent.

Load agent: .claude/agents/design-review-agent.md
```

## Available Commands

| Command | Purpose | Agent |
|---------|---------|-------|
| `/design-review` | Review UI/UX design | design-review-agent |
| `/security-audit` | Security vulnerability check | security-audit-agent |
| `/code-review` | Code quality review | code-review-agent |
| `/accessibility` | WCAG compliance check | accessibility-agent |
| `/user-flow-test` | End-to-end flow testing | user-flow-test-agent |
| `/docs-update` | Update documentation | docs-update-agent |

## Usage Examples

Type these commands **inside Claude Code** (after running `claude` in your terminal):

```bash
# Review a specific component
/design-review src/components/Header.tsx

# Security audit the auth system
/security-audit src/lib/auth

# Full code review
/code-review

# Test the signup flow
/user-flow-test signup flow

# Update docs after changes
/docs-update
```

## Creating Custom Commands

1. Create command file: `.claude/commands/[name].md`
2. Create matching agent: `.claude/agents/[name]-agent.md`
3. Reference the agent in the command

### Command Template

```markdown
[Description of what the command does]

$ARGUMENTS

Load and follow the instructions in: .claude/agents/[name]-agent.md
```

## Best Practices

1. **One command, one purpose** - Keep commands focused
2. **Match agents** - Every command should have a corresponding agent
3. **Use $ARGUMENTS** - Allow users to specify targets
4. **Clear descriptions** - First line should explain what it does
