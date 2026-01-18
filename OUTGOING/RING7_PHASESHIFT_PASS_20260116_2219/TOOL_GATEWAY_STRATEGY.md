# TOOL GATEWAY STRATEGY
## Progressive Disclosure vs Direct MCP Attachment

**Document Type**: Strategic Analysis + Pattern Proposal
**Status**: Tentative (pending operational validation)
**Generated**: 2026-01-16
**Inputs**: MCP video (Kenny Liao), platform_features.md, context economics analysis

---

## I. THE PROBLEM STATEMENT

### Context Window Economics

Claude Code's 200K token context window is finite. Every capability added consumes tokens:

| Context Consumer | Token Cost | Persistence |
|------------------|------------|-------------|
| System prompt (CLAUDE.md) | ~2-5K | Per session |
| Conversation history | Grows with use | Until compaction |
| Tool definitions (MCP) | **~10-15K per server** | Per connected server |
| Active file contents | Variable | While relevant |

### The MCP Token Tax

**Empirical finding** (from practitioner video):
> "With seven MCP servers connected, the MCP tools alone consume around 100,000 tokens, or 50% of the total capacity."

At ~15K tokens per MCP server:
- 7 servers = ~100K tokens (50% of context)
- 14 servers = ~200K tokens (100% of context = unusable)
- **Hard ceiling**: ~13 MCP servers before system becomes non-functional

### Context Rot Amplification

Beyond token consumption, irrelevant context degrades performance:

> "As discussed in a paper published by Chroma, the performance of agents degrades as you fill up more of the context window. If the context is filled with irrelevant information, it distracts the agent and further degrades performance."

**The compound problem**: More tools → more token consumption → less space for actual work → worse performance even on remaining space.

---

## II. COMPARISON: DIRECT ATTACHMENT VS PROGRESSIVE DISCLOSURE

### Approach A: Direct MCP Attachment

**Pattern**:
```
Claude Code ←──connected──→ MCP Server 1
            ←──connected──→ MCP Server 2
            ←──connected──→ MCP Server 3
            ...
            ←──connected──→ MCP Server N
```

**Characteristics**:
| Aspect | Direct Attachment |
|--------|-------------------|
| Token cost | O(N × server_definition_size) |
| Tool availability | Immediate (all tools in context) |
| Discovery | N/A (pre-loaded) |
| Scaling | **Does not scale** (hard ceiling ~13 servers) |
| Performance | Degrades as servers increase |
| Simplicity | High (native integration) |

**When Appropriate**:
- Small number of frequently-used servers (≤3)
- Session dedicated to specific toolset
- Short sessions where context won't fill

**When Inappropriate**:
- Large tool ecosystems
- General-purpose sessions
- Long-running work

### Approach B: Progressive Disclosure Gateway

**Pattern**:
```
Claude Code ←──connected──→ Gateway (single MCP)
                              │
                              ├── search() → returns tool schemas on demand
                              ├── list() → shows available servers
                              ├── inspect() → shows specific tool schema
                              └── call() → invokes tool
                              │
            ┌─────────────────┼─────────────────┐
            ↓                 ↓                 ↓
      MCP Server 1      MCP Server 2      MCP Server N
         (dormant)        (dormant)         (dormant)
```

**Characteristics**:
| Aspect | Progressive Disclosure |
|--------|----------------------|
| Token cost | O(1) base + O(k) per tool used |
| Tool availability | On-demand (discovered then loaded) |
| Discovery | Search-based (semantic or keyword) |
| Scaling | **Scales to thousands** of tools |
| Performance | Stable (only relevant tools in context) |
| Simplicity | Lower (requires gateway setup) |

**When Appropriate**:
- Large tool ecosystems (>5 servers)
- Variable task types requiring different tools
- Long-running sessions
- Cost/context optimization required

**When Inappropriate**:
- Single-server workflows
- Rapid tool switching without search
- Minimal infrastructure tolerance

### Head-to-Head Comparison

| Factor | Direct Attachment | Progressive Disclosure |
|--------|-------------------|----------------------|
| **Setup complexity** | Low | Medium |
| **Token efficiency** | Poor | Excellent |
| **Scaling** | Hard ceiling | Linear with usage |
| **Tool discovery** | Pre-known | Search-based |
| **Latency per call** | Lower | Higher (gateway overhead) |
| **Infrastructure** | Native MCP | Gateway + cache |
| **Performance stability** | Degrades | Stable |

---

## III. THE CLI-GATEWAY PATTERN (Launchpad Model)

### Principle: Tool Access Without Context Pollution

The gateway provides:
1. **Single entry point** (one tool definition in context)
2. **Cached discovery** (search without live connections)
3. **On-demand schema loading** (only what's needed)
4. **Semantic search** (find tools by intent, not name)

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Claude Code                          │
│   ┌─────────────────────────────────────────────────┐   │
│   │              Context Window (200K)               │   │
│   │  ┌──────────────────┐  ┌───────────────────┐   │   │
│   │  │ Gateway Tool Def │  │ Current Work      │   │   │
│   │  │ (~2K tokens)     │  │ (remaining space) │   │   │
│   │  └──────────────────┘  └───────────────────┘   │   │
│   └─────────────────────────────────────────────────┘   │
└───────────────────────────┬─────────────────────────────┘
                            │ CLI calls
                            ↓
┌─────────────────────────────────────────────────────────┐
│                 Gateway CLI (mcpl)                       │
│   ┌─────────────┐  ┌─────────────┐  ┌──────────────┐   │
│   │   Cache     │  │   Search    │  │   Router     │   │
│   │ (tool defs) │  │   (BM25)    │  │ (to servers) │   │
│   └─────────────┘  └─────────────┘  └──────────────┘   │
└───────────────────────────┬─────────────────────────────┘
                            │ spawns as needed
                            ↓
┌─────────────────────────────────────────────────────────┐
│                  MCP Server Pool                         │
│   ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐    │
│   │Sentry│  │Linear│  │Supabase│ │GitHub│  │ ...  │    │
│   └──────┘  └──────┘  └──────┘  └──────┘  └──────┘    │
└─────────────────────────────────────────────────────────┘
```

### Gateway Operations

**1. List Servers**
```bash
mcpl list
# Returns: Available servers and their enabled/disabled status
```

**2. Refresh Cache**
```bash
mcpl list --refresh
# Connects to all servers, caches tool definitions locally
# Only needed when servers change
```

**3. Search Tools (Semantic)**
```bash
mcpl search "database queries"
# Returns: Ranked list of tools matching intent
# Uses BM25 semantic search, not just keywords
```

**4. Inspect Tool**
```bash
mcpl inspect supabase execute_sql
# Returns: Full JSON schema for specific tool
# Claude loads this on-demand when needed
```

**5. Call Tool**
```bash
mcpl call sentry get_issue --args '{"issue_id": "123"}'
# Invokes tool through gateway
# Returns result to Claude
```

### Workflow Example

**Without Gateway** (direct attachment):
```
Claude: [has 100K tokens of MCP definitions in context]
Claude: "I need to check a Sentry issue"
Claude: [knows sentry.get_issue is available, calls it]
# Cost: 100K tokens always present
```

**With Gateway**:
```
Claude: [has 2K tokens of gateway definition]
Claude: "I need to check a Sentry issue"
Claude: mcpl search "error tracking issues"
# Returns: sentry.get_issue, sentry.list_issues, linear.get_issue
Claude: mcpl inspect sentry get_issue
# Returns: JSON schema (~500 tokens)
Claude: mcpl call sentry get_issue --args '{"issue_id": "123"}'
# Returns: Issue data
# Cost: 2K base + 500 per tool used
```

---

## IV. IMPLEMENTATION REQUIREMENTS

### Minimal Viable Gateway

**Components**:
1. CLI tool (Python/Node) installed globally
2. Configuration file (`mcp.json`) listing available servers
3. Local cache for tool schemas
4. Search index (BM25 or simpler keyword)

**Configuration Example** (`~/.claude/mcp.json`):
```json
{
  "servers": {
    "sentry": {
      "command": "npx",
      "args": ["-y", "@sentry/mcp-server"],
      "env": {"SENTRY_API_TOKEN": "${SENTRY_TOKEN}"},
      "enabled": true
    },
    "linear": {
      "command": "npx",
      "args": ["-y", "@linear/mcp-server"],
      "env": {"LINEAR_API_KEY": "${LINEAR_KEY}"},
      "enabled": true
    },
    "supabase": {
      "command": "npx",
      "args": ["-y", "@supabase/mcp-server"],
      "env": {"SUPABASE_URL": "${SUPABASE_URL}"},
      "enabled": false
    }
  }
}
```

### Claude Code Integration

**CLAUDE.md addition**:
```markdown
## Tool Gateway

You have access to the MCP Launchpad CLI (`mcpl`) for discovering and using tools.

Available servers: sentry, linear, supabase, github, notion

Commands:
- `mcpl list` - Show available servers
- `mcpl search <query>` - Find tools by intent
- `mcpl inspect <server> <tool>` - Get tool schema
- `mcpl call <server> <tool> --args '<json>'` - Invoke tool

Workflow: search → inspect → call
Do NOT assume tool schemas; always inspect before calling.
```

### Caching Strategy

**Cache Layers**:
1. **Server list**: Long-lived (changes rarely)
2. **Tool schemas**: Medium-lived (rebuild on `--refresh`)
3. **Search index**: Rebuilt with tool schemas
4. **Call results**: Not cached (dynamic data)

**Cache Location**: `~/.mcpl/cache/`
```
~/.mcpl/
├── cache/
│   ├── servers.json       # Available servers
│   ├── tools/             # Tool schemas per server
│   │   ├── sentry.json
│   │   ├── linear.json
│   │   └── ...
│   └── search_index.json  # BM25 index
└── mcp.json              # Configuration
```

---

## V. COORDINATOR TOOL REQUEST PROTOCOL

### How the Coordinator Should Request Tools

**Step 1: Identify Intent**
```
"I need to [action] related to [domain]"
Example: "I need to find issues related to authentication errors"
```

**Step 2: Search for Tools**
```bash
mcpl search "authentication errors issues"
# Returns ranked options
```

**Step 3: Inspect Best Match**
```bash
mcpl inspect sentry search_issues
# Returns schema with parameters
```

**Step 4: Invoke with Parameters**
```bash
mcpl call sentry search_issues --args '{"query": "authentication"}'
```

**Step 5: Process Result**
```
# Handle response, integrate into workflow
```

### Coordinator Decision Tree

```
Need external tool?
    │
    ├── No → Use native Claude Code tools
    │
    └── Yes → Which domain?
              │
              ├── Known domain (e.g., "github")
              │   └── mcpl inspect github <likely_tool>
              │
              └── Unknown domain
                  └── mcpl search "<intent description>"
                      └── mcpl inspect <best_match>
```

### Anti-Patterns

**DON'T**: Assume tool schemas
```
# BAD
mcpl call github create_issue --args '{"title": "Bug"}'
# May fail if schema is different
```

**DO**: Always inspect first
```
# GOOD
mcpl inspect github create_issue
# Learn: needs "title", "body", "repo", "labels"
mcpl call github create_issue --args '{"title": "Bug", "body": "...", "repo": "..."}'
```

**DON'T**: Connect all servers directly
```
# BAD - context bloat
mcp_servers: [sentry, linear, supabase, github, notion, slack, ...]
```

**DO**: Use gateway for large tool sets
```
# GOOD - single entry point
Use mcpl for tool discovery and invocation
```

---

## VI. RISKS AND MITIGATIONS

### Risk 1: Context Bloat

**Description**: Tool definitions consume excessive context.

**Symptoms**:
- Slow response times
- Forgetting earlier conversation
- Degraded reasoning quality

**Mitigations**:
| Mitigation | Mechanism |
|------------|-----------|
| Progressive disclosure gateway | Load tools on-demand |
| Server pruning | Disable unused servers |
| Session scoping | Connect only session-relevant servers |
| Sub-agent delegation | Tool-heavy work in isolated context |

### Risk 2: Context Rot

**Description**: Irrelevant information degrades performance.

**Symptoms**:
- Model distracted by irrelevant tools
- Wrong tool selection
- Increased latency

**Mitigations**:
| Mitigation | Mechanism |
|------------|-----------|
| Semantic search | Surface only relevant tools |
| Tool pruning | Remove unused tools from consideration |
| Session hygiene | Clear irrelevant context |
| Bounded context | Keep tool knowledge minimal |

### Risk 3: Tool Sprawl

**Description**: Accumulation of tools without governance.

**Symptoms**:
- Duplicate capabilities across servers
- Unclear which tool for which task
- Maintenance burden

**Mitigations**:
| Mitigation | Mechanism |
|------------|-----------|
| Tool inventory | Maintain capability ledger |
| Canonical tools | Designate preferred tool per task |
| Periodic audit | Review and prune tool set |
| Usage tracking | Identify unused tools |

### Risk 4: Gateway Complexity

**Description**: Gateway adds operational overhead.

**Symptoms**:
- Gateway failures block tool access
- Configuration drift
- Cache staleness

**Mitigations**:
| Mitigation | Mechanism |
|------------|-----------|
| Fallback to direct | Allow direct attachment for critical servers |
| Health checks | Verify gateway operation |
| Cache refresh protocol | Regular refresh schedule |
| Documentation | Clear setup and troubleshooting |

### Risk 5: Latency Overhead

**Description**: Gateway adds latency to tool calls.

**Symptoms**:
- Slower tool invocations
- Perceived sluggishness

**Mitigations**:
| Mitigation | Mechanism |
|------------|-----------|
| Local caching | Tool schemas cached locally |
| Parallel discovery | Search index pre-built |
| Connection pooling | Keep server connections warm |
| Accept tradeoff | Latency < context exhaustion |

---

## VII. HYBRID STRATEGY RECOMMENDATION

### The Recommended Configuration

**Direct attachment** (always connected):
- 1-3 highest-frequency servers
- Session-critical tools
- Low token-cost servers

**Progressive disclosure** (via gateway):
- All other servers
- Infrequently-used tools
- Large tool-surface servers

### Example Configuration

```yaml
# Direct attachment (native MCP)
direct_servers:
  - filesystem  # Always needed
  - github      # Frequent for code work
  # Total: ~30K tokens

# Gateway access (mcpl)
gateway_servers:
  - sentry      # Occasional
  - linear      # Occasional
  - supabase    # Occasional
  - notion      # Rare
  - slack       # Rare
  - jira        # Rare
  # Dozens more possible without context cost
```

### Decision Criteria for Direct vs Gateway

| Factor | Direct | Gateway |
|--------|--------|---------|
| Usage frequency | >10x/session | <10x/session |
| Token cost | <10K | >10K |
| Session criticality | Always needed | Conditionally needed |
| Latency sensitivity | High | Acceptable |

---

## VIII. DECISION LOG

| Decision | Status | Rationale |
|----------|--------|-----------|
| Progressive disclosure for scale | **Tentative** | Based on token economics |
| Hybrid direct+gateway | **Tentative** | Balance convenience and scale |
| Semantic search for discovery | **Tentative** | Superior to keyword for intent |
| Local caching | **Invariant** | Reduce latency, offline capability |
| Inspect-before-call rule | **Invariant** | Schema correctness |

---

**End of Tool Gateway Strategy**
