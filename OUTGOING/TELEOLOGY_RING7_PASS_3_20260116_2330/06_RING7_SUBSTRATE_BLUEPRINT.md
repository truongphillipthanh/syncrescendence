# RING 7 SUBSTRATE BLUEPRINT
## Concrete Patterns for Execution Infrastructure

**Purpose**: Actionable blueprint for sub-agents, tool gateways, artifact handoffs, and repo-as-spine
**Generated**: 2026-01-16
**Builds On**: RING7_PHASESHIFT_PASS_20260116_2219/

---

## I. RING 7 RECAP

**Ring 7** = Execution Substrate = The only ring that touches reality

Components:
1. **Execution Engines**: Claude Code, Jules, Codex
2. **Sub-Agent Architecture**: Coordinator → specialized agents
3. **Tool Gateway**: Progressive disclosure of MCP servers
4. **Artifact Handoffs**: Structured packets between agents/sessions
5. **Repo-as-Spine**: Repository as ground truth and coordination backbone

---

## II. SUB-AGENT ARCHITECTURE

### The Seven Roles

```
                    COORDINATOR (Main Thread)
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ↓                  ↓                  ↓
   ┌─────────┐       ┌─────────┐       ┌─────────┐
   │ PLANNER │       │ EXPLORER│       │ CODER   │
   │ (plan)  │       │ (recon) │       │ (impl)  │
   └─────────┘       └─────────┘       └─────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
   ┌─────────┐       ┌─────────┐       ┌─────────┐
   │ REVIEWER│       │ARCHIVIST│       │ AUDITOR │
   │ (verify)│       │ (docs)  │       │ (audit) │
   └─────────┘       └─────────┘       └─────────┘
```

### Role Specifications

| Role | Model | Tools Allowed | Returns |
|------|-------|---------------|---------|
| **Coordinator** | Opus | All | Final synthesis |
| **Planner** | Sonnet/Opus | Read, Glob, Grep | Plan document |
| **Explorer** | Haiku | Read, Glob, Grep | Codebase summary |
| **Coder** | Sonnet | Read, Edit, Write, Bash | Impl summary |
| **Reviewer** | Haiku | Read, Grep, Bash | Review findings |
| **Archivist** | Haiku/Sonnet | Read, Write, Edit, Bash | Docs/commits |
| **Auditor** | Sonnet | Read, Bash, Grep | Audit packet |

### Invocation Patterns

**Direct invocation**:
```
@explore "Describe the codebase structure"
@coder "Implement the feature per this plan: [acceptance criteria]"
```

**Background invocation** (Ctrl+B):
```
# Frees main thread while agent works
@explore "Analyze tech stack" [Ctrl+B]
# Check status with down arrow → Enter
```

**Parallel agents**:
```
Coordinator: "I need to understand both the frontend and backend.
              Launch two explore agents in parallel."
# Both run simultaneously, each returns summary
```

### Bounded Context Rules

**NEVER carry implicitly across agent boundary**:
- Full execution traces
- Intermediate reasoning
- Other agents' context
- Tool output details

**ALWAYS carry explicitly**:
- Task specification
- Acceptance criteria
- File references
- Summary of prior work

---

## III. TOOL GATEWAY PATTERN

### The Problem

Direct MCP attachment consumes ~15K tokens per server:
- 7 servers = 100K tokens (50% of context)
- 13+ servers = unusable

### The Solution: Progressive Disclosure

```
┌─────────────────────────────────────────────────────────┐
│                     Claude Code                          │
│   ┌─────────────────────────────────────────────────┐   │
│   │         Context Window (200K tokens)             │   │
│   │  ┌──────────────────┐  ┌───────────────────┐   │   │
│   │  │ Gateway (~2K)    │  │ Actual Work       │   │   │
│   │  └──────────────────┘  │ (remaining 198K)  │   │   │
│   │                        └───────────────────┘   │   │
│   └─────────────────────────────────────────────────┘   │
└───────────────────────────────────────────────────────────┘
                            │
                            ↓
┌─────────────────────────────────────────────────────────┐
│                  Tool Gateway CLI                        │
│   Commands: list, search, inspect, call                  │
│   Cache: Tool schemas stored locally                     │
│   Search: Semantic (BM25) tool discovery                 │
└───────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ↓               ↓               ↓
       [Server 1]      [Server 2]      [Server N]
        (dormant)       (dormant)       (dormant)
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

### Hybrid Configuration

**Direct attachment** (always connected, ~30K tokens):
- filesystem (always needed)
- github (frequent for code work)

**Gateway access** (on-demand, ~2K base):
- sentry, linear, supabase, notion, slack, jira, ...
- Hundreds of tools possible without context cost

### CLAUDE.md Gateway Block

```markdown
## Tool Gateway

You have access to the MCP Launchpad CLI (`mcpl`) for tool discovery.

Available servers: sentry, linear, supabase, github, notion, slack

Workflow:
1. `mcpl search <intent>` - Find tools by what you want to do
2. `mcpl inspect <server> <tool>` - Get tool schema
3. `mcpl call <server> <tool> --args '<json>'` - Invoke tool

NEVER assume tool schemas. ALWAYS inspect before calling.
```

---

## IV. ARTIFACT HANDOFFS

### The Principle

**Conversations are ephemeral. Artifacts are persistent.**

Every agent-to-agent or session-to-session transition uses structured artifacts:
- Plan → Execution via Plan Packet
- Execution → Audit via Execution Packet
- Session → Session via Continuation Packet

### Handoff Locations

```
00-ORCHESTRATION/
├── blackboard/
│   ├── evidence/    # Gemini sensing outputs
│   ├── plans/       # ChatGPT planning outputs
│   ├── executions/  # Claude Code execution outputs
│   └── audits/      # ChatGPT audit outputs
├── state/
│   ├── system_state.json    # Current state vector
│   └── events.jsonl         # Append-only event log
└── oracle_contexts/
    └── ORACLE[N]_CONTEXT.md  # Session continuity
```

### Handoff Protocol

**Agent A finishing → Agent B starting**:

1. Agent A creates packet in appropriate blackboard directory
2. Agent A updates `events.jsonl` with handoff event
3. Agent B loads packet at start
4. Agent B acknowledges receipt before proceeding

**Session ending**:

1. Create Continuation Packet
2. Update state vector
3. Log event
4. Commit changes
5. State "safe to delete"

---

## V. REPO-AS-SPINE

### The Architecture

```
                    ┌─────────────────────┐
                    │     REPOSITORY      │
                    │   (Ground Truth)    │
                    └─────────┬───────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ↓                     ↓                     ↓
   ┌─────────┐          ┌─────────┐          ┌─────────┐
   │ Claude  │          │ ChatGPT │          │ Gemini  │
   │  Code   │          │         │          │         │
   └─────────┘          └─────────┘          └─────────┘

   All write to repo     Packets via repo     Reads from repo
   State changes here    Coordination here    Sensing here
```

### Repo Responsibilities

| Function | Repo Component |
|----------|----------------|
| State persistence | `system_state.json`, `events.jsonl` |
| Task tracking | `tasks.csv` |
| Coordination | `blackboard/` packets |
| Constitution | `CLAUDE.md`, CANON |
| Context | `oracle_contexts/` |
| Work products | CANON, SOURCES, OPERATIONAL |

### Multi-Platform Coordination via Repo

1. **Gemini** reads repo via Drive connector, produces Evidence Packet
2. **ChatGPT** receives Evidence Packet, produces Plan Packet
3. **Claude Code** executes Plan Packet, produces Execution Packet
4. **ChatGPT** audits Execution Packet, produces Audit Packet
5. **Repo** stores all, enables continuation from any platform

---

## VI. NTH-ORDER EFFECTS

### 1st Order Effects (Immediate)

| Effect | Type | Mechanism |
|--------|------|-----------|
| Main context preserved | Benefit | Sub-agent tokens isolated |
| Parallel execution enabled | Benefit | Independent agents |
| Token cost reduced | Benefit | Progressive disclosure |
| Coordination overhead | Cost | Must manage agents |
| Additional latency | Cost | Gateway indirection |

### 2nd Order Effects (Secondary)

| Effect | Type | Mechanism |
|--------|------|-----------|
| Complex tasks feasible | Benefit | More context available |
| Quality differentiation | Benefit | Specialized agents outperform generalist |
| Larger tool ecosystems | Benefit | No hard ceiling on tools |
| Information loss at boundaries | Risk | Summaries compress too much |
| Debugging complexity | Cost | Which agent caused issue? |

### 3rd Order Effects (Tertiary)

| Effect | Type | Mechanism |
|--------|------|-----------|
| Principal role shifts | Benefit | Governor not relay |
| Tool selection becomes intentional | Benefit | Search-based, not ambient |
| New failure modes emerge | Risk | Coordination failures, orphaned agents |
| Platform resilience increases | Benefit | Continuation artifacts survive crashes |

### 4th Order Effects (Quaternary)

| Effect | Type | Mechanism |
|--------|------|-----------|
| Institutional scalability | Benefit | System can grow beyond Principal bandwidth |
| Platform agnosticism | Benefit | Can span Claude/Gemini/ChatGPT |
| Composable execution | Benefit | Any combination of agents/tools/handoffs |
| Dependency on orchestration | Risk | Orchestration failure = system failure |

---

## VII. RISKS AND MITIGATIONS

### Risk Matrix

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Context collapse** | Medium | High | Sub-agent delegation, compaction discipline |
| **Coordination deadlock** | Low | High | Dependency DAGs, atomic agent work |
| **Gateway unavailable** | Low | Medium | Fallback to direct attachment for critical tools |
| **Artifact omission** | Medium | High | Forced export rule, session-end checklist |
| **Summary info loss** | Medium | Medium | Structured packets with required fields |
| **Cost explosion** | Low | Medium | Agent count limits, model tiering |
| **Tool sprawl** | Medium | Low | Periodic tool audit, disable unused |

### Mitigation Patterns

**For Context Issues**:
```bash
# Check context usage
claude status

# Delegate to sub-agent if >60%
@explore "Handle this reconnaissance task"

# Force compaction if approaching limit
/compact Focus on state changes, ignore verbose logs
```

**For Coordination Issues**:
```bash
# Check running agents
# (down arrow → Enter in Claude Code)

# Kill stuck agent
# (if supported)
```

**For Gateway Issues**:
```bash
# Check gateway health
mcpl list

# Fall back to direct if needed
# (manually connect critical server)
```

---

## VIII. IMPLEMENTATION CHECKLIST

### Phase 1: Foundation (Do First)

- [ ] Set up CLAUDE.md with gateway block
- [ ] Configure 2-3 direct MCP servers (filesystem, github)
- [ ] Create blackboard directory structure
- [ ] Establish continuation packet template

### Phase 2: Sub-Agents (Do Second)

- [ ] Create custom agents via `/agents`
- [ ] Test Explorer agent (Haiku) on codebase
- [ ] Test Coder agent (Sonnet) on simple task
- [ ] Test Reviewer agent (Haiku) on code review
- [ ] Establish parallel invocation pattern

### Phase 3: Gateway (Do Third)

- [ ] Install gateway CLI (if using MCP Launchpad or similar)
- [ ] Configure `mcp.json` with available servers
- [ ] Cache tool schemas
- [ ] Test search → inspect → call workflow
- [ ] Document available servers in CLAUDE.md

### Phase 4: Full Integration (Do Last)

- [ ] Run end-to-end: Evidence → Plan → Execute → Audit
- [ ] Verify all packets written to blackboard
- [ ] Test continuation: delete session, resume from artifact
- [ ] Document any customizations needed

---

## IX. VERIFICATION COMMANDS

```bash
# Verify sub-agents work
claude "Use the explore agent to describe this codebase briefly"

# Verify gateway works (if using)
mcpl list && mcpl search "test"

# Verify blackboard exists
ls -la 00-ORCHESTRATION/blackboard/

# Verify state vector
cat 00-ORCHESTRATION/state/system_state.json | head -20

# Verify continuation works
# 1. Create continuation artifact
# 2. Start new session
# 3. Load artifact
# 4. Verify context restored
```

---

**Ring 7 is the enabling membrane. Master this, and the inner rings manifest.**
