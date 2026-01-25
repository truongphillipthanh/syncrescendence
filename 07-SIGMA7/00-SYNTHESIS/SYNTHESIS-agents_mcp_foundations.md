# Agent and MCP Foundations: Canonical Reference

**Version**: 1.0.0 | **Stream**: C | **Purpose**: Expand underdeveloped agent/MCP layer

---

## Executive Frame

The paradigm shift from "assistant" to "agent" is definitional. Assistants suggest actions for human execution; agents execute actions autonomously. This distinction governs architecture: agents need perception (how they see world state), decision logic (how they choose actions), and action interfaces (how they affect state). The agent loop—observe, decide, act, observe result, repeat—runs until goal achieved or stopping condition met.

Claude Code, Codex CLI, and Cowork are agents. ChatGPT web is an assistant. Cursor is a copilot (HITL with limited action space). The shift from Human-in-the-Loop (HITL) to Human-on-the-Loop (HOTL) enables tasks spanning hours with thousands of steps where humans monitor rather than perform.

MCP (Model Context Protocol) extends agent capability by providing standardized tool interfaces. Like USB-C for AI—any system implementing the protocol becomes available to any MCP-compatible agent. The context tax of tool definitions (50K+ tokens for 7 servers) creates the primary constraint, solved through progressive disclosure and tool search.

---

## TERM Blocks: Core Concepts

```
TERM AgentParadigm:
sutra: "Agents act on world state—assistants merely suggest actions"
gloss: The defining feature of an agent is tool execution, not recommendation.
       When you tell an assistant "send this email," it drafts text for you to
       paste. When you tell an agent, it invokes the email tool and sends.
       This capability/responsibility shift changes everything about architecture.
spec:
    type: TERM
    defining_feature: tool_execution (vs recommendation)
    agent_examples: [Claude Code, Codex CLI, Cowork, MCP servers]
    assistant_examples: [ChatGPT web, base Claude web]
    copilot_examples: [Cursor, Windsurf]
    key_difference: "Agents handle exceptions; automations break on them"
end
```

```
TERM AgentLoop:
sutra: "Observe-decide-act-observe result-repeat until goal or stopping condition"
gloss: Every agent follows this recursive pattern. Perception reads current state
       (APIs, databases, files). Decision logic chooses next action. Action interface
       executes (and logs for audit). Result observation feeds next decision.
       Stopping conditions prevent infinite loops.
spec:
    type: TERM
    phases: [perception, decision, action, observation, iteration]
    perception_sources: [APIs, databases, filesystems, web]
    decision_approaches:
        routine: structured decision trees
        ambiguous: LLM invocation
    action_requirements: [logged, reversible, permission-gated]
    stopping_conditions: [goal_achieved, max_iterations, human_interrupt, error_threshold]
end
```

```
TERM ThreeComponents:
sutra: "Perception sees, decision chooses, action affects—skip any and agent fails"
gloss: Every production agent has exactly three components. Perception: how agent
       sees world (APIs, databases, document stores). Decision logic: how agent
       chooses (structured trees for routine, LLM for ambiguous). Action interface:
       how agent affects world (logged, reversible, permission-gated).
spec:
    type: TERM
    perception:
        purpose: "How agent sees world state"
        implementations: [API calls, database queries, file reads, web scraping]
    decision_logic:
        purpose: "How agent chooses actions"
        routine: "Structured decision trees"
        ambiguous: "LLM invocation"
        principle: "Use LLM only when needed"
    action_interface:
        purpose: "How agent affects world"
        requirements: [logged, reversible, permission_gated]
        principle: "Never silent failures"
end
```

```
TERM ModelContextProtocol:
sutra: "USB-C for AI—standardized tool interface across any system"
gloss: MCP provides protocol for exposing tools to AI models. Servers expose
       resources (data), tools (actions), and prompts (templates). Clients
       (Claude Code) discover and invoke them. Any system implementing MCP
       becomes accessible to any MCP-compatible agent.
spec:
    type: TERM
    architecture: server-client (servers expose, clients invoke)
    components:
        resources: "Data accessible to agent"
        tools: "Actions agent can take"
        prompts: "Templates for common operations"
    configuration: [".mcp.json (project)", "~/.claude.json (user)"]
    discovery: "Client queries server for available tools"
    invocation: "Client sends structured request, server executes"
end
```

```
TERM ContextTax:
sutra: "Seven MCP servers = 50% context consumed before conversation starts"
gloss: Every tool definition consumes tokens. With 7 typical MCP servers,
       ~100K of 200K tokens gone before work begins. This is the fundamental
       scaling problem with direct MCP connection. Solution: progressive
       disclosure via Tool Search or CLI wrappers.
spec:
    type: TERM
    problem: "Tool schemas consume context budget"
    typical_impact: "7 servers = 100K tokens = 50% of 200K limit"
    degradation: "Context rot—performance degrades as irrelevant tokens accumulate"
    solutions:
        tool_search: "Lazy load only needed tool definitions"
        cli_wrappers: "Reference CLI tools in CLAUDE.md, load definitions on demand"
        mcp_launchpad: "Semantic search across all configured servers"
end
```

```
TERM ProgressiveDisclosure:
sutra: "Metadata at startup, full definitions only when tool actually needed"
gloss: Instead of loading all tool schemas upfront, agent starts with lightweight
       search capability (~500 tokens). When reasoning indicates need for specific
       tool, system retrieves and loads that schema. Preserves ~95% of context
       for actual task data.
spec:
    type: TERM
    startup_load: "Search tool only (~500 tokens)"
    activation_trigger: "Agent reasoning indicates tool need"
    just_in_time: "Specific tool definition loaded when needed"
    context_savings: "~95% preserved for task data"
    implementations: [Claude Code Tool Search, MCP Launchpad, Skills system]
end
```

```
TERM SubagentDelegation:
sutra: "Spawn isolated workers, return artifacts—parallelism without pollution"
gloss: Sub-agents operate in separate context windows, preventing cross-contamination.
       Main agent delegates specific tasks, receives structured artifacts, maintains
       clean context. The Task tool in Claude Code implements this. 50K tokens
       used by sub-agent don't affect main agent's 200K limit.
spec:
    type: TERM
    isolation: "Separate context per sub-agent"
    communication: "Artifact return (not shared state)"
    context_benefit: "Sub-agent tokens don't count against main agent"
    pattern: "orchestrator → specialist → artifact → orchestrator"
    invocation:
        direct: "@agent-name or Ctrl+B for background"
        implicit: "Agent spawns when appropriate"
    subagent_types:
        bash: "Terminal operations, git, commands"
        explore: "Fast Haiku for code search"
        plan: "Investigation and requirements"
        general_purpose: "Multi-step execution"
end
```

```
TERM ToolSurface:
sutra: "Filesystem, bash, MCP, desktop, subagent—five classes of capability"
gloss: Agent capability defined by available tools. Filesystem operations (read,
       write, edit) form base layer. Bash extends to any CLI tool. MCP provides
       external integrations. Desktop adds GUI control. Subagents enable
       parallelism and specialization.
spec:
    type: TERM
    tool_classes:
        filesystem: [Read, Write, Edit, Glob, Grep]
        bash: "Any CLI tool inheriting user environment"
        mcp: "External service integrations"
        desktop: "Mouse, keyboard, screen control"
        subagent: "Delegated parallel execution"
    capability_expansion:
        mcp_servers: "Add without code changes"
        skills: "Add procedural knowledge"
        cli_tools: "Document in CLAUDE.md"
end
```

---

## Orchestration Patterns

### Supervisor Pattern (Centralized Control)

Supervisor agent coordinates all work: receives task, decomposes, routes to workers, validates, synthesizes.

```
User Request
    ↓
[Supervisor Agent]
    ↓
Decompose → Route → Monitor → Validate → Synthesize
    ↓         ↓         ↓
[Worker 1] [Worker 2] [Worker 3]
```

**When to use**:
- Tasks with clear decomposition
- Need auditability and reasoning transparency
- Quality control matters more than speed
- 3-8 worker agents maximum

**Problem**: Supervisors become bottlenecks. Every decision flows through one agent, creating serial processing even when work is parallel. Token costs scale with coordination layers.

### Swarm Pattern (Peer-to-Peer)

No central controller. Agents communicate directly, self-organize around task.

```
[Agent A] ←→ [Agent B]
    ↕  ↘     ↙  ↕
[Agent C] ←→ [Agent D]
```

**When to use**:
- Multiple perspectives needed
- No clear task decomposition
- Real-time responsiveness critical
- Agents can self-organize

**Problem**: Emergent behavior hard to predict. Agents may duplicate work, create loops, or converge on suboptimal solutions. Debugging requires tracing mesh, not tree.

### Hierarchical Pattern (Multi-Level)

Supervisor pattern, recursive. Top level manages mid-levels, which manage workers.

```
[Top-Level Supervisor]
          ↓
    ┌─────┴─────┐
    ↓           ↓
[Mid-Level A] [Mid-Level B]
    ↓           ↓
[Workers 1-3] [Workers 4-6]
```

**When to use**:
- 10+ agents
- Multiple abstraction layers needed
- Both strategic and tactical control required

**Problem**: Token costs explode. Three-layer hierarchy with 5 agents per layer can burn 50K+ tokens on coordination alone.

---

## Communication Strategies

### Shared State (Default)

All agents read/write common state object.

**Advantages**: Simple, easy to debug (inspect state)
**Disadvantages**: Race conditions, no isolation, unbounded growth
**When to use**: Start here. Use until specific problems emerge.

### Message Passing (Event-Driven)

Agents publish/subscribe to events. No direct state sharing.

**Advantages**: Loose coupling, natural for async, easy to add agents
**Disadvantages**: Harder debugging, potential loops, needs infrastructure
**When to use**: Truly independent agents, async processing across services.

### Handoff Mechanism

Explicit control transfer with context passing.

**Advantages**: Clear control flow, auditable, context preservation
**Disadvantages**: Tight coupling, serial by default, handoff overhead
**When to use**: Specific order required, context must flow through chain.

---

## Memory Architecture

### Session-Based Memory

Each interaction is session with isolated state. Merge back on completion.

**Use case**: Parallel agents needing shared context but isolated changes.

### Window Memory

Sliding window of recent exchanges. Oldest compressed or dropped.

**Use case**: Long-running conversations where context matters but can't keep all.

### Episodic Memory

Store interaction history between specific agents. Enables cross-agent learning.

**Use case**: Frequently collaborating agents that improve from past coordination.

---

## MCP Server Patterns

### Key Production Servers

| Server | Capability | Use Case |
|--------|------------|----------|
| **github** | PR management, issues, code review | Development workflow |
| **filesystem** | Cross-directory file access | Large codebase navigation |
| **slack** | Channel read/write, notifications | Team communication |
| **notion** | Documentation, wikis | Knowledge management |
| **postgres/supabase** | Database queries | Data operations |
| **gdrive** | Google Drive access | Document management |
| **memory/sqlite** | Structured key-value persistence | Agent long-term memory |

### Configuration Patterns

**Project-level** (`.mcp.json`):
```json
{
  "servers": {
    "github": { "command": "npx", "args": ["github-mcp"] }
  }
}
```

**User-level** (`~/.claude.json`):
Available across all projects. Good for personal tooling.

**Governance principle**: Have 20-30 configured, keep <10 enabled per project.

### MCP Launchpad Pattern

CLI wrapper providing semantic search across all configured servers:
- `mcpl list` — Browse available tools
- `mcpl search issues` — Semantic search across servers
- `mcpl inspect server tool` — Get full schema on demand

**Benefit**: ~500 tokens at startup instead of 100K. Tools loaded just-in-time.

---

## Production Considerations

### Token Economics

Multi-agent systems burn tokens fast:
- Supervisor decomposition: ~1K tokens
- 4 worker agents: ~12K tokens (3K each)
- Supervisor synthesis: ~2K tokens
- **Total**: ~15K tokens vs ~4K for single agent

**Optimizations**:
- Cache supervisor instructions
- Compress worker outputs (structured data, not prose)
- Parallelize independent work
- Lazy agent activation

### Error Propagation

**Failure modes**:
- Poison pills: Garbage output breaks downstream
- Deadlocks: Circular wait dependencies
- Resource exhaustion: All agents hit same rate limit
- Cascading failures: Supervisor dies, orphans workers

**Defenses**:
- Timeouts at every layer
- Circuit breakers after N failures
- Graceful degradation (work with subset)
- State isolation (worker failures don't corrupt shared state)

---

## Anti-Patterns

- **Over-coordination**: Don't coordinate independent tasks
- **Kitchen sink agents**: Specialization is the point
- **Synchronous everything**: Default to async
- **Ignoring costs**: Track token usage or get surprise bills
- **No fallbacks**: Build degraded modes
- **Direct MCP over CLI**: CLI tools with good docs often more reliable

---

## When to Use What

| Scenario | Pattern |
|----------|---------|
| Need auditability, 3-8 agents | Supervisor |
| Multiple perspectives, no decomposition | Swarm |
| 10+ agents, layered abstraction | Hierarchical |
| Task simple enough | Single agent |
| Not sure | Single agent, iterate |

**Golden rule**: Build one agent that works reliably before building ten.

---

## Cross-References

- [[SYNTHESIS-cross_platform_patterns]] → Oracle-Executor, Chorus Protocol
- [[MECH-subagent_delegation]] → Task tool mechanics
- [[MECH-mcp_server_patterns]] → Server configuration details
- [[PRAC-oracle_to_executor_handoff]] → File-based coordination
