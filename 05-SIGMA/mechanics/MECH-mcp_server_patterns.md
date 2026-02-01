# MECH: MCP Server Patterns

**Scope**: Server architecture, production servers, configuration, context tax mitigation

---

## Core Concept

```
TERM MCPArchitecture:
sutra: "Server exposes, client discovers, protocol standardizes—USB-C for AI"
gloss: Model Context Protocol separates tool definition from tool execution.
       Servers expose resources (data), tools (actions), and prompts (templates).
       Clients query available capabilities, invoke as needed. Any system
       implementing protocol becomes AI-accessible.
spec:
    type: MECHANISM
    components:
        server: "Exposes capabilities via protocol"
        client: "Claude Code, other MCP-compatible agents"
        protocol: "JSON-RPC over stdio or HTTP"
    exposed_by_server:
        resources: "Data accessible to agent"
        tools: "Actions agent can take"
        prompts: "Templates for common operations"
end
```

---

## The Context Tax Problem

```
NORM ContextTax:
sutra: "7 servers = 100K tokens = 50% gone before conversation starts"
gloss: Every tool schema consumes tokens from context window. Direct connection
       to multiple MCP servers creates bloat that degrades performance even
       when tools aren't used (context rot). This is the fundamental scaling
       problem.
spec:
    measurement: "7 typical servers ≈ 100K tokens"
    impact: "50% of 200K limit consumed before work"
    degradation: "Performance drops as irrelevant tokens accumulate"
    solutions: [tool_search, cli_wrappers, mcp_launchpad]
end
```

---

## Configuration Patterns

### Project-Level (`.mcp.json`)

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/path/to/project"]
    }
  }
}
```

**Location**: Project root or `.claude/`
**Scope**: This project only
**Note**: Name `mcp.json` (no leading period) to avoid collision with Claude Code conventions

### User-Level (`~/.claude.json`)

```json
{
  "mcpServers": {
    "personal-tools": {
      "command": "node",
      "args": ["/path/to/custom-server.js"]
    }
  }
}
```

**Location**: `~/.claude/`
**Scope**: All projects for this user

### Enterprise-Level (`managed-mcp.json`)

Managed by IT, not user-configurable. Organizational tools and policies.

---

## Key Production Servers

| Server | Command | Use Case |
|--------|---------|----------|
| **github** | `npx @mcp/server-github` | PR management, issues, code review |
| **filesystem** | `npx @mcp/server-filesystem /path` | Cross-directory file access |
| **postgres** | `npx @mcp/server-postgres` | Database queries |
| **supabase** | `npx supabase-mcp` | Supabase integration |
| **slack** | `npx @mcp/server-slack` | Channel read/write |
| **notion** | `npx @mcp/server-notion` | Documentation, wikis |
| **gdrive** | `npx @mcp/server-gdrive` | Google Drive access |
| **memory** | `npx @mcp/server-memory` | Key-value persistence |
| **brave-search** | `npx @mcp/server-brave-search` | Web search |

---

## Governance Principle

```
NORM MCPGovernance:
sutra: "Configure 20-30, enable <10 per project—lazy loading beats eager"
spec:
    configured: "20-30 servers available"
    enabled: "<10 servers active per project"
    rationale: "Each enabled server adds context tax"
    pattern: "Enable by project needs, not globally"
end
```

---

## Context Tax Mitigation

### Tool Search (Built-in)

Claude Code implements progressive disclosure:
1. Startup: Load lightweight search tool (~500 tokens)
2. Reasoning: Agent identifies tool need
3. Just-in-time: Specific tool schema loaded
4. Result: ~95% context preserved for task

### CLI Wrappers

Document CLI tools in CLAUDE.md instead of connecting MCP:

```markdown
## Available Tools (via CLI)
- `gh pr list` — List pull requests
- `gh issue create` — Create GitHub issue
- `supabase db query "..."` — Run SQL
```

**Advantage**: Zero context tax until tool invoked
**Disadvantage**: Less structured than MCP schema

### MCP Launchpad

Semantic search across all configured servers:

```bash
# Install
uv tool install mcp-launchpad

# Configure in mcp.json (without leading dot)
# Search for tools
mcpl search "create issue"

# Get specific schema
mcpl inspect github create_issue
```

**Advantage**: Thousands of tools, ~500 token startup cost
**Disadvantage**: Additional installation, caching overhead

---

## Environment Variables

For secrets in MCP configuration:

```json
{
  "mcpServers": {
    "github": {
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

Define in `.env` file (same directory as `mcp.json`):

```
GITHUB_TOKEN=ghp_xxxxxxxxxxxx
```

**Security note**: Never commit `.env` files.

---

## When MCP vs CLI

| Use MCP When | Use CLI When |
|--------------|--------------|
| Structured input/output matters | Simple invocation sufficient |
| Schema discovery needed | Docs in CLAUDE.md adequate |
| Complex parameter validation | Straightforward arguments |
| Enterprise governance required | Personal tooling |

**Practitioner wisdom**: "Custom MCP servers are often worse than CLI tools with good documentation."

---

## Gemini MCP Integration

```bash
claude mcp add gemini-cli -s user -- npx -y gemini-mcp-tool
```

Enables slash commands:
- `/gemini-review` — Code review with 1M context
- `/gemini-plan` — Project-aware planning

**Pattern**: Claude orchestrates, Gemini provides massive-context analysis.

---

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| All servers always enabled | 50%+ context consumed | Enable per-project |
| MCP for simple operations | Overhead exceeds benefit | Use CLI |
| No environment variable isolation | Secrets leak | Use `${VAR}` syntax |
| Ignoring context meter | Degraded performance | Monitor, disable unused |

---

## Cross-References

- [[SYNTHESIS-agents_mcp_foundations]] → MCP architecture overview
- [[SYNTHESIS-cross_platform_patterns]] → Gemini integration patterns
- [[MECH-subagent_delegation]] → MCP in sub-agent context
