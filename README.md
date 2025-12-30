# Claude Code Project Template

A production-grade template for configuring Claude Code with Skills, Agents, and Commands based on [Anthropic's research](https://www.anthropic.com/engineering/claude-code-best-practices).

## Why This Template?

Most Claude Code setups are basic. This template implements the **Skills + Agents + Commands** architecture that Anthropic's research shows produces better results:

- **Skills** auto-activate during code **creation** to prevent mistakes
- **Agents** are invoked manually for **review** to catch issues
- **Commands** provide human-readable ways to run agents

The result: Claude writes better code the first time and catches more issues during review.

---

## Quick Start

### Option A: Tell Claude What You're Building (Recommended)

Just describe your project and Claude customizes everything:

```
I'm starting a new project using the Claude Code project template.

**Project Name:** My App
**Description:** [What it does]
**Tech Stack:** [Your stack]
**Key Features:**
1. Feature 1
2. Feature 2

Please customize the template for my project.
```

See [QUICKSTART.md](QUICKSTART.md) for detailed prompts and examples.

### Option B: Manual Setup

#### 1. Copy the `.claude/` folder to your project

```bash
cp -r .claude/ your-project/.claude/
```

#### 2. Copy and customize `CLAUDE.md`

```bash
cp docs/CLAUDE.md.example your-project/CLAUDE.md
```

Edit it to match your project's specifics.

#### 3. Install MCP servers (optional but recommended)

```bash
# Browser automation for visual testing
claude mcp add playwright -- npx @anthropic/mcp-playwright

# UI component library
claude mcp add shadcn -- npx -y @anthropic-ai/shadcn-mcp@latest

# Up-to-date library docs
claude mcp add context7 -- npx -y @anthropic-ai/context7-mcp@latest
```

### 4. Start using

```bash
# Skills auto-activate when relevant
# Just start coding - frontend-design skill activates for UI work

# Run agents via commands
claude /security-audit
claude /code-review
claude /design-review
```

---

## What's Included

```
.claude/
├── skills/                    # Auto-activate during creation
│   ├── frontend-design/       # Prevents "AI slop" (generic fonts, purple gradients)
│   └── security/              # Enforces secure patterns
│
├── agents/                    # Manual review workflows
│   ├── design-review-agent.md
│   ├── security-audit-agent.md
│   ├── code-review-agent.md
│   ├── accessibility-agent.md
│   ├── user-flow-test-agent.md
│   └── docs-update-agent.md
│
└── commands/                  # Human-readable agent triggers
    └── [matching .md files]

docs/
├── CLAUDE.md.example          # Template for main instructions
├── MCP.md                     # MCP server setup guide
└── ARCHITECTURE.md            # How Skills/Agents/Commands work
```

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                        CLAUDE.md                             │
│                   (Project-specific rules)                   │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│    Skills    │      │    Agents    │      │   Commands   │
│ (Auto-load)  │      │   (Manual)   │      │   (Manual)   │
│              │      │              │      │              │
│ Prevents     │      │ Catches      │      │ /security    │
│ mistakes     │      │ issues       │      │ /code-review │
│ during       │      │ during       │      │ /design      │
│ creation     │      │ review       │      │              │
└──────────────┘      └──────────────┘      └──────────────┘
```

### Progressive Disclosure

Skills use 3-level loading to save tokens:

1. **Level 1:** Metadata only (~100 tokens) - loaded at startup
2. **Level 2:** SKILL.md body (<500 lines) - when task is relevant
3. **Level 3:** Reference files - only when specifically needed

---

## Customizing for Your Project

### Skills

Edit the skills to match your domain:

- `frontend-design/` - Already universal, customize color palettes in THEMES.md
- `security/` - Adapt patterns for your auth/payment system

### Agents

Modify agents for your workflows:

- Update file paths to match your project structure
- Add project-specific checks to checklists
- Remove irrelevant sections

### CLAUDE.md

This is your main configuration. Include:

- Project overview and tech stack
- Key directories and file locations
- Critical rules (security, patterns to follow)
- Links to detailed docs

---

## Documentation Workflow

This template includes a complete docs-as-code workflow:

- **CHANGELOG.md** - Auto-updated with every change
- **DECISIONS.md** - Log architectural decisions as they happen
- **TODO.md** - Track tasks with clear status
- **LOGIC_AUDIT.md** - Document user flows and edge cases

Run `/docs-update` after any session to sync documentation with code.

See [docs/WORKFLOW.md](docs/WORKFLOW.md) for details.

---

## Research Background

This template is based on:

- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)

Key insight: **Skills prevent mistakes during creation**, while **Agents catch issues during review**. Using both together produces the best results.

---

## License

MIT - Use this however you want.

---

## Contributing

Found something that could be better? PRs welcome!
