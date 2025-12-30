# MCP Server Configuration

Model Context Protocol (MCP) servers extend Claude's capabilities with real-time access to external tools and services.

---

## Recommended MCP Servers

### Playwright (Visual Testing)

Browser automation for testing UI changes.

```bash
claude mcp add playwright -- npx @anthropic/mcp-playwright
```

**Tools:**
| Tool | Purpose |
|------|---------|
| `browser_navigate` | Navigate to URL |
| `browser_click` | Click elements |
| `browser_type` | Type into inputs |
| `browser_snapshot` | Get accessibility tree |
| `browser_take_screenshot` | Capture visual evidence |
| `browser_resize` | Test responsive layouts |

**Usage:**
```
Claude: Let me check the homepage layout
[Uses browser_navigate to open site]
[Uses browser_snapshot to see structure]
[Uses browser_take_screenshot for visual evidence]
```

---

### shadcn/ui (Component Library)

Access shadcn/ui component source code and demos.

```bash
claude mcp add shadcn -- npx -y @anthropic-ai/shadcn-mcp@latest
```

**Tools:**
| Tool | Purpose |
|------|---------|
| `get_component` | Get component source code |
| `list_components` | See available components |

**Usage:**
```
Claude: I need to add a dropdown menu
[Uses get_component to see shadcn dropdown implementation]
[Adapts for your project]
```

---

### Context7 (Library Documentation)

Get up-to-date documentation for any library.

```bash
claude mcp add context7 -- npx -y @anthropic-ai/context7-mcp@latest
```

**Tools:**
| Tool | Purpose |
|------|---------|
| `get-library-docs` | Fetch current docs for a library |

**Usage:**
```
Claude: How do I use the new Next.js 15 features?
[Uses get-library-docs to fetch latest Next.js docs]
[Provides accurate, current information]
```

---

### Supabase (Database)

Direct database access for queries and migrations.

```bash
claude mcp add supabase -- npx -y @anthropic-ai/supabase-mcp@latest
```

**Setup:**
1. Run `claude /mcp` to authenticate
2. Select your Supabase project

**Tools:**
| Tool | Purpose |
|------|---------|
| `execute_sql` | Run SQL queries |
| `apply_migration` | Apply schema changes |
| `list_tables` | View database structure |
| `get_logs` | View service logs |

---

### Stripe (Payments)

Payment management and webhook monitoring.

```bash
claude mcp add --transport http stripe https://mcp.stripe.com/
```

**Setup:**
1. Run `claude /mcp` to authenticate with Stripe

**Tools:**
| Tool | Purpose |
|------|---------|
| `list_payment_intents` | View payments |
| `search_stripe_documentation` | Search Stripe docs |
| `list_webhooks` | View webhook endpoints |

---

## Configuration

MCP servers are configured in `~/.claude.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@anthropic/mcp-playwright"]
    },
    "shadcn": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/shadcn-mcp@latest"]
    }
  }
}
```

---

## Managing MCP Servers

```bash
# List installed servers
claude /mcp

# Add a server
claude mcp add <name> -- <command>

# Remove a server
claude mcp remove <name>

# Re-authenticate
claude mcp auth <name>
```

---

## Permissions

Control MCP access in `.claude/settings.local.json`:

```json
{
  "permissions": {
    "allow": [
      "mcp__playwright__*",
      "mcp__shadcn__*",
      "mcp__context7__*"
    ]
  }
}
```

---

## Best Practices

1. **Use MCP instead of guessing** - Don't ask user to check things manually
2. **Playwright for visual verification** - Take screenshots to confirm UI changes
3. **Context7 for docs** - Always get current library documentation
4. **Supabase for database** - Run queries directly instead of asking user
