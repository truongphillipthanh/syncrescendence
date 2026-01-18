# RING7 SUBSTRATE IMPLEMENTATION PLAN
## Sub-Agents, Tool Gateways, and Concrete Patterns
**Generated**: 2026-01-17
**Purpose**: How to exploit Claude Code sub-agents, avoid MCP bloat, and keep the coordinator clean

---

## I. WHAT RING 7 IS

**Ring 7** = The Execution Substrate = The only ring that touches reality

```
                 OUTER (Interface)
                      │
    ┌─────────────────┼─────────────────┐
    │                 │                 │
    │   A0: Concierge │                 │
    │   A1: Chorus    │                 │
    │   A2: Surfaces  │                 │
    │   A3: Sensors   │                 │
    │   A4: Organs    │                 │
    │                 │                 │
    │        ┌────────┴────────┐        │
    │        │   RING 7        │        │
    │        │   SUBSTRATE     │        │
    │        │   (You are here)│        │
    │        └────────┬────────┘        │
    │                 │                 │
    │   B0: Reality   │                 │
    │   B1-B7: Repo   │                 │
    │                 │                 │
    └─────────────────┼─────────────────┘
                      │
                 INNER (Metabolism)
```

Ring 7 contains:
1. **Execution Engines**: Claude Code CLI
2. **Sub-Agent Architecture**: Coordinator → specialized agents
3. **Tool Gateway**: Progressive disclosure of MCP servers
4. **Artifact Handoffs**: Packets between agents
5. **Repo-as-Spine**: Repository as coordination backbone

---

## II. THE SUB-AGENT ROSTER

### Recommended Agent Configuration

| Agent | Model | Invocation | Tools | Returns |
|-------|-------|------------|-------|---------|
| **Coordinator** | Opus | (main thread) | All | Final synthesis |
| **Planner** | Sonnet | `Task` tool | Read, Glob, Grep | Plan document |
| **Explorer** | Haiku | `Task` tool (Explore) | Read, Glob, Grep | Codebase summary |
| **Coder** | Sonnet | `Task` tool | Read, Edit, Write, Bash | Implementation summary |
| **Reviewer** | Haiku | `Task` tool | Read, Grep, Bash | Review findings |
| **Archivist** | Haiku | `Task` tool | Read, Write, Edit, Bash | Docs, commits |
| **Auditor** | Sonnet | `Task` tool | Read, Bash, Grep | Audit packet |

### The Pattern

```
                    COORDINATOR (Opus)
                    Keeps main context clean
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ↓                  ↓                  ↓
   ┌─────────┐       ┌─────────┐       ┌─────────┐
   │ PLANNER │       │ EXPLORER│       │ CODER   │
   │ (Sonnet)│       │ (Haiku) │       │ (Sonnet)│
   └─────────┘       └─────────┘       └─────────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                           ↓
                    ┌─────────────┐
                    │  REVIEWER   │
                    │  (Haiku)    │
                    └─────────────┘
                           │
                           ↓
                    ┌─────────────┐
                    │  ARCHIVIST  │
                    │  (Haiku)    │
                    └─────────────┘
```

---

## III. DISPATCH PATTERNS

### Pattern 1: Parallel Exploration

**When**: Need to understand multiple areas simultaneously.

```
Coordinator:
  "I need to understand both the orchestration system and the canon structure.
   Launch two explore agents in parallel."

Dispatch:
  Agent 1 (Explore): "Analyze 00-ORCHESTRATION/ structure and key files"
  Agent 2 (Explore): "Analyze 01-CANON/ structure and key documents"

Both run simultaneously.
Coordinator receives two summaries.
```

**Implementation**:
```
<Task subagent_type="Explore" description="Explore orchestration">
  Analyze the 00-ORCHESTRATION/ directory. Report structure, key files, patterns.
</Task>

<Task subagent_type="Explore" description="Explore canon">
  Analyze the 01-CANON/ directory. Report structure, key documents, hierarchy.
</Task>
```

### Pattern 2: Plan-Then-Execute

**When**: Clear objective, need to plan before implementing.

```
Coordinator:
  "We need to add a new packet type. First plan, then implement."

Dispatch:
  Phase 1: Planner
    "Review existing packet schemas. Propose new packet structure."

  Phase 2 (after plan approved): Coder
    "Implement the packet schema per this plan: [plan]"

  Phase 3: Reviewer
    "Review the implementation against the plan."
```

**Implementation**:
```
# Phase 1
<Task subagent_type="Plan" description="Plan new packet">
  Review 00-ORCHESTRATION/blackboard/schemas/packet_protocol.json.
  Propose a new packet type for [purpose].
</Task>

# Phase 2 (after approval)
<Task subagent_type="general-purpose" description="Implement packet">
  Implement the packet schema. Update packet_protocol.json.
  Acceptance criteria: [from plan]
</Task>

# Phase 3
<Task subagent_type="general-purpose" description="Review implementation">
  Review the changes to packet_protocol.json.
  Verify against the plan.
</Task>
```

### Pattern 3: Explore-Plan-Execute

**When**: Unclear scope, need reconnaissance first.

```
Coordinator:
  "Something's wrong with the ledger updates. Fix it."

Dispatch:
  Phase 1: Explorer
    "Find all ledger-related code. What's the current state?"

  Phase 2: Planner
    "Given these findings, what's the fix?"

  Phase 3: Coder
    "Implement the fix."

  Phase 4: Reviewer
    "Verify the fix."
```

### Pattern 4: Background Processing

**When**: Long-running task, don't want to block coordinator.

```
Coordinator:
  "Verify all 50 source files have correct frontmatter.
   Run this in background."

Dispatch:
  <Task run_in_background="true" description="Verify sources">
    Check all files in 04-SOURCES/processed/ for frontmatter compliance.
    Report any issues.
  </Task>

Coordinator continues other work.
Later: Check background task status.
```

---

## IV. CONTEXT BOUNDARIES

### NEVER Carry Across Agent Boundary (Implicit)

| Content | Why Not |
|---------|---------|
| Full execution traces | Bloats context |
| Intermediate reasoning | Not needed by next agent |
| Other agents' context | Creates confusion |
| Tool output details | Summarize instead |

### ALWAYS Carry Across Agent Boundary (Explicit)

| Content | Why |
|---------|-----|
| Task specification | What to do |
| Acceptance criteria | How to know it's done |
| File references | Where to work |
| Summary of prior work | Context for decisions |

### Context Packet Pattern

When delegating to sub-agent, provide:

```markdown
## CONTEXT PACKET

**Task**: [What to do]

**Scope**: [Which files/directories]

**Prior Work**: [What's already been done]

**Acceptance Criteria**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]

**Return**: [What to report back]
```

---

## V. TOOL GATEWAY STRATEGY

### The Problem

Direct MCP attachment consumes ~15K tokens per server:
- 7 servers = 100K tokens (50% of context)
- 13+ servers = unusable

### The Solution: Progressive Disclosure

**Directly attached** (always available):
- filesystem
- github

**Gateway access** (on-demand):
- All other MCP servers
- Loaded only when needed

### Gateway Configuration

Add to CLAUDE.md:

```markdown
## Tool Gateway

You have access to the MCP Launchpad CLI (`mcpl`) for tool discovery.

Available servers (via gateway):
- sentry, linear, supabase, notion, slack, jira, confluence

Workflow:
1. `mcpl search <intent>` - Find tools by what you want to do
2. `mcpl inspect <server> <tool>` - Get tool schema
3. `mcpl call <server> <tool> --args '<json>'` - Invoke tool

NEVER assume tool schemas. ALWAYS inspect before calling.
```

### Gateway Workflow

```bash
# 1. Search for relevant tools
mcpl search "database queries"
# Returns: supabase.execute_sql, postgres.query, ...

# 2. Inspect the best match
mcpl inspect supabase execute_sql
# Returns: Full JSON schema for this tool

# 3. Call with parameters
mcpl call supabase execute_sql --args '{"sql": "SELECT * FROM users"}'
# Returns: Query result
```

### Token Budget

| Configuration | Token Cost | Available Tools |
|---------------|------------|-----------------|
| Direct (all servers) | ~100K | 7-8 servers |
| Hybrid (2 direct + gateway) | ~35K | Unlimited |
| Gateway only | ~5K | Unlimited |

**Recommendation**: Hybrid configuration. Direct attach filesystem + github, gateway for everything else.

---

## VI. KEEPING THE COORDINATOR CLEAN

### Rule 1: Delegate Exploration

**Don't**: Read 50 files in main thread.
**Do**: Spawn Explorer agent to summarize.

### Rule 2: Delegate Heavy Computation

**Don't**: Process large batches in main thread.
**Do**: Spawn Coder agent with batch, receive summary.

### Rule 3: Summarize Returns

Sub-agents should return **summaries**, not full outputs.

**Don't**: Return 500 lines of grep output.
**Do**: Return "Found 12 matches in 4 files. Key findings: [list]"

### Rule 4: Use Background for Long Tasks

If task might take > 2 minutes:
- Run in background
- Continue coordinator work
- Check status periodically

### Rule 5: Compact Aggressively

When main context approaches 60% full:
- Spawn sub-agent for heavy work
- Use `/compact` to summarize history
- Archive detailed logs to repo

---

## VII. PLANNER → IMPLEMENTERS → REVIEWER → RECEIPTS

This is the canonical execution flow.

```
┌─────────────────────────────────────────────────────────────┐
│                         PLANNER                              │
│                                                             │
│  Input: Directive or objective                               │
│  Process: Explore, analyze, propose                          │
│  Output: Plan with acceptance criteria                       │
│                                                             │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                      IMPLEMENTERS                            │
│                                                             │
│  Input: Plan with acceptance criteria                        │
│  Process: Write code, modify files, run commands             │
│  Output: Implementation summary                              │
│                                                             │
│  (May be multiple Coders in parallel for different tracks)   │
│                                                             │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                        REVIEWER                              │
│                                                             │
│  Input: Implementation + acceptance criteria                 │
│  Process: Verify each criterion, run tests                   │
│  Output: Review findings (pass/fail per criterion)           │
│                                                             │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                        RECEIPTS                              │
│                                                             │
│  Archivist creates:                                          │
│  - Execution packet                                          │
│  - State update                                              │
│  - Event log entry                                           │
│  - Git commit                                                │
│  - Continuation packet (if session ending)                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## VIII. IMPLEMENTATION CHECKLIST

### Phase 1: Foundation (Do First)

- [ ] **CLAUDE.md has gateway block**: Add tool gateway section
- [ ] **Direct MCP servers configured**: filesystem, github
- [ ] **Blackboard directory exists**: 00-ORCHESTRATION/blackboard/
- [ ] **Continuation packet template ready**: Copy from 05_PACKET_TEMPLATES

### Phase 2: Sub-Agent Testing (Do Second)

- [ ] **Test Explorer agent**:
  ```
  Use the Task tool with subagent_type=Explore to describe 00-ORCHESTRATION/
  ```

- [ ] **Test Planner agent**:
  ```
  Use the Task tool with subagent_type=Plan to plan a small change
  ```

- [ ] **Test parallel dispatch**:
  ```
  Launch two Explore agents in one message
  ```

- [ ] **Test background processing**:
  ```
  Launch an agent with run_in_background=true
  ```

### Phase 3: Gateway Testing (Do Third)

- [ ] **Install gateway CLI** (if using MCP Launchpad or similar)
- [ ] **Configure available servers** in mcp.json
- [ ] **Test search → inspect → call workflow**:
  ```bash
  mcpl search "test"
  mcpl inspect <server> <tool>
  mcpl call <server> <tool> --args '{}'
  ```

### Phase 4: Full Integration (Do Last)

- [ ] **Run full flow**: Planner → Coder → Reviewer → Archivist
- [ ] **Verify packets written**: Check blackboard/
- [ ] **Test continuation**: End session, start new, load artifact
- [ ] **Document any customizations**

---

## IX. VERIFICATION COMMANDS

```bash
# Verify CLAUDE.md has gateway block
grep -q "Tool Gateway" CLAUDE.md && echo "Gateway block present"

# Verify blackboard structure
ls -la 00-ORCHESTRATION/blackboard/

# Verify state vector
cat 00-ORCHESTRATION/state/system_state.json | head -20

# Test Explorer agent in Claude Code
# (run this as a Claude Code command)
claude "Use the Task tool with subagent_type=Explore to briefly describe this repo"

# Check sub-agent availability
# (Task tool should be available; check claude --help or docs)
```

---

## X. ANTI-PATTERNS

### Anti-Pattern 1: Everything in Main Thread

**Symptom**: Context fills up mid-task.
**Fix**: Delegate to sub-agents earlier.

### Anti-Pattern 2: Full Outputs Returned

**Symptom**: Sub-agent returns 1000 lines.
**Fix**: Instruct sub-agent to summarize.

### Anti-Pattern 3: Tool Schema Guessing

**Symptom**: MCP tool calls fail.
**Fix**: Always inspect schema before calling.

### Anti-Pattern 4: No Receipts

**Symptom**: Work done but no artifacts.
**Fix**: Always end with Archivist creating receipts.

### Anti-Pattern 5: Orphaned Background Tasks

**Symptom**: Background task forgotten.
**Fix**: Check task status, retrieve outputs.

---

## XI. COSTS AND TRADEOFFS

| Approach | Context Cost | Latency | Coordination |
|----------|--------------|---------|--------------|
| All in main thread | High | Low | None |
| Sub-agents | Low | Medium | Medium |
| Background tasks | Low | High | High |
| Tool gateway | Very low | Medium | Low |

**Sweet Spot**: Use sub-agents for exploration and heavy work, keep main thread for coordination and synthesis.

---

## XII. QUICK REFERENCE

### Invoking Sub-Agents

```
# Explore agent (fast, read-only)
<Task subagent_type="Explore" description="description">prompt</Task>

# Plan agent (strategic, read-only)
<Task subagent_type="Plan" description="description">prompt</Task>

# General-purpose agent (can write)
<Task subagent_type="general-purpose" description="description">prompt</Task>

# Background execution
<Task subagent_type="general-purpose" run_in_background="true">prompt</Task>

# Model selection
<Task subagent_type="Explore" model="haiku">prompt</Task>  # Fast, cheap
<Task subagent_type="Plan" model="sonnet">prompt</Task>    # Balanced
<Task subagent_type="general-purpose" model="opus">prompt</Task>  # Deep
```

### Tool Gateway Commands

```bash
mcpl search "intent"              # Find tools
mcpl inspect <server> <tool>      # Get schema
mcpl call <server> <tool> --args  # Invoke
mcpl list                         # Available servers
```

### Context Health

```
> 60% context used → Delegate to sub-agent
> 80% context used → Use /compact
> 90% context used → Create continuation, start new session
```

---

**Ring 7 is the enabling membrane. Master sub-agents and gateways, and the rest flows.**
