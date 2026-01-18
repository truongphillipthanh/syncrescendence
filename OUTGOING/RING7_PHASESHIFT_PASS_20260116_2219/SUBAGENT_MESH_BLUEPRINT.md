# SUBAGENT MESH BLUEPRINT
## Role Taxonomy, Bounded Contexts, and Failure Modes

**Document Type**: Architectural Blueprint
**Status**: Tentative (pending operational validation)
**Generated**: 2026-01-16
**Inputs**: Sub-agents video (Leon van Zyl), platform_features.md, INTERACTION_PARADIGM.md

---

## I. EXECUTIVE SUMMARY

The sub-agent mesh is a **parallel execution architecture** that:
1. Protects the main conversation's context window
2. Enables specialized roles with distinct capabilities
3. Allows parallelization of independent tasks
4. Returns compressed summaries rather than full execution traces

**Key insight from practitioners**: "Using sub-agents isn't just about saving tokens; it's about maintaining the 'intelligence' of the main agent by preventing the fragmentation that occurs when a conversation becomes too long."

---

## II. ROLE TAXONOMY

### Overview: The Seven Roles

| Role | Purpose | Invocation Pattern |
|------|---------|-------------------|
| **Coordinator** | Orchestrate other agents, maintain coherence | Main thread (never a sub-agent) |
| **Planner** | Decompose tasks, create execution plans | `@planner` or Task tool with Plan agent |
| **Explorer** | Codebase reconnaissance, pattern finding | `@explore` or Task tool with Explore agent |
| **Coder** | Implementation, file modifications | Custom agent or direct execution |
| **Reviewer** | Code review, security audit, quality check | Custom agent (even Haiku excels here) |
| **Archivist** | Documentation, changelog, commit messages | Custom agent or direct |
| **Auditor** | Verification against specifications | Custom agent |

### The Hierarchical Principle

```
COORDINATOR (Main Thread)
    │
    ├── PLANNER (planning phase)
    │       └── returns: Plan document
    │
    ├── EXPLORER (reconnaissance phase)
    │       └── returns: Codebase summary
    │
    ├── CODER (implementation phase, parallel)
    │   ├── Coder-Track-A
    │   ├── Coder-Track-B
    │   └── Coder-Track-C
    │       └── each returns: Implementation summary
    │
    ├── REVIEWER (verification phase, parallel)
    │   ├── Reviewer-Security
    │   ├── Reviewer-Quality
    │   └── Reviewer-Completeness
    │       └── each returns: Review findings
    │
    ├── AUDITOR (acceptance phase)
    │       └── returns: Audit packet
    │
    └── ARCHIVIST (documentation phase)
            └── returns: Documentation artifacts
```

---

## III. ROLE SPECIFICATIONS

### III.A COORDINATOR

**Purpose**: Orchestrate the sub-agent mesh, maintain session coherence, make routing decisions.

**Inputs**:
- User requests
- Sub-agent summaries
- Repository state
- Plan documents

**Outputs**:
- Sub-agent invocations
- Routing decisions
- Synthesis of sub-agent results
- Final responses to user

**Allowed Tools**:
- All tools (as main thread)
- Task tool (for spawning sub-agents)
- TodoWrite (for tracking)
- Read/Edit/Write (direct intervention)

**Failure Modes**:
| Failure | Symptom | Prevention |
|---------|---------|------------|
| Context bloat | Slow responses, forgetting | Delegate to sub-agents aggressively |
| Micromanagement | Doing sub-agent work | Trust specialists |
| Lost coherence | Contradictory actions | Maintain explicit state tracking |
| Premature synthesis | Acting before sub-agents complete | Wait for all returns |

**Verification Expectations**:
- All sub-agents spawned successfully
- All returns received and incorporated
- Final state reflects sub-agent contributions

**NEVER carries implicitly**:
- Full sub-agent execution traces
- Intermediate reasoning from sub-agents
- Tool outputs from sub-agent sessions

---

### III.B PLANNER

**Purpose**: Decompose complex tasks into executable tracks, identify parallelization opportunities.

**Inputs**:
- Task description
- Codebase context (from Explorer)
- Constraints and requirements
- Prior plans (for iteration)

**Outputs**:
- Structured plan document with:
  - Tracks (parallelizable work streams)
  - Dependencies between tracks
  - Acceptance criteria per track
  - Risk assessment

**Allowed Tools**:
- Read (examine existing code/docs)
- Glob (find relevant files)
- Grep (search patterns)
- **No Write/Edit** (planning, not implementation)

**Failure Modes**:
| Failure | Symptom | Prevention |
|---------|---------|------------|
| Over-planning | Plans that exceed implementation scope | Time-box planning, bias toward action |
| Under-specification | Coders guess at requirements | Include explicit acceptance criteria |
| Missed dependencies | Tracks that block each other | Dependency analysis before parallelization |
| Scope creep | Plan expands beyond request | Anchored to original request |

**Verification Expectations**:
- Plan addresses all stated requirements
- Each track has clear acceptance criteria
- Dependencies are acyclic (DAG structure)
- Parallel tracks are actually independent

**NEVER carries implicitly**:
- Implementation details (Coder's job)
- Current file contents (reference, don't embed)
- Verification results (Auditor's job)

---

### III.C EXPLORER

**Purpose**: Fast codebase reconnaissance using lightweight model (Haiku).

**Inputs**:
- Query or exploration goal
- Scope constraints (directories, file types)
- Prior exploration results (for refinement)

**Outputs**:
- Codebase summary
- File inventory with purposes
- Architecture patterns detected
- Relevant code locations for follow-up

**Allowed Tools**:
- Glob (file discovery)
- Grep (pattern search)
- Read (file examination)
- **No Write/Edit** (reconnaissance only)

**Failure Modes**:
| Failure | Symptom | Prevention |
|---------|---------|------------|
| Shallow exploration | Missing critical files | Multiple search strategies |
| Hallucinated structures | Claiming files that don't exist | Glob before claiming |
| Irrelevant detail | Returning too much noise | Stay focused on query |
| Missed patterns | Not recognizing architecture | Use multiple heuristics |

**Verification Expectations**:
- All claimed files exist (verifiable with glob)
- Summary accurately reflects codebase
- Architecture patterns are defensible

**NEVER carries implicitly**:
- Full file contents (summarize, don't embed)
- Modification plans (Planner/Coder's job)
- Historical context (state is in repository)

**Model Selection**: Haiku strongly preferred for cost/speed. Explorer is high-volume.

---

### III.D CODER

**Purpose**: Implement changes according to plan, write code that passes review.

**Inputs**:
- Plan document or track specification
- Acceptance criteria
- Relevant codebase context
- Style guidelines (from CLAUDE.md)

**Outputs**:
- Modified/created files
- Implementation summary
- Notes for reviewer (edge cases, decisions made)

**Allowed Tools**:
- Read (examine existing code)
- Edit (modify files)
- Write (create files)
- Bash (run tests, build commands)
- Glob/Grep (find related code)

**Failure Modes**:
| Failure | Symptom | Prevention |
|---------|---------|------------|
| Over-engineering | Adding unrequested features | Strict adherence to plan |
| Under-testing | Code that fails in review | Run tests before declaring done |
| Style drift | Inconsistent with codebase | Reference existing patterns |
| Incomplete implementation | Partial features | Acceptance criteria checklist |
| Breaking changes | Existing tests fail | Run full test suite |

**Verification Expectations**:
- All acceptance criteria met
- Tests pass (new and existing)
- No linting errors
- Changes are minimal and focused

**NEVER carries implicitly**:
- Full plan document (reference by ID)
- Other tracks' implementation details
- Review feedback (receive fresh in review cycle)

---

### III.E REVIEWER

**Purpose**: Quality assurance, security audit, completeness verification.

**Inputs**:
- Implementation summary from Coder
- Acceptance criteria from plan
- Files modified
- Review type (security, quality, completeness)

**Outputs**:
- Review findings (structured)
- Pass/fail determination
- Specific improvement requests
- Severity ratings

**Allowed Tools**:
- Read (examine code)
- Grep (search for patterns)
- Bash (run security scanners, linters)
- **No Write/Edit** (review, not fix)

**Failure Modes**:
| Failure | Symptom | Prevention |
|---------|---------|------------|
| Rubber stamping | Approving without scrutiny | Structured checklist |
| Scope creep | Reviewing unrelated code | Focus on changed files |
| False positives | Flagging non-issues | Understand context |
| Missing severity | Treating critical as minor | Explicit severity framework |

**Verification Expectations**:
- All changed files examined
- Security checklist applied
- Findings are actionable
- Severity ratings are calibrated

**NEVER carries implicitly**:
- Full implementation history
- Coder's reasoning (only examine artifacts)
- Prior review cycles (fresh eyes each time)

**Model Selection**: Even Haiku performs well for reviews. Cost-effective for multiple passes.

---

### III.F ARCHIVIST

**Purpose**: Documentation, changelogs, commit messages, knowledge capture.

**Inputs**:
- Implementation summaries
- Review results
- Plan documents
- Repository conventions

**Outputs**:
- Updated documentation
- Changelog entries
- Commit messages
- CANON updates (if applicable)

**Allowed Tools**:
- Read (examine existing docs)
- Write (create docs)
- Edit (update docs)
- Bash (git operations)

**Failure Modes**:
| Failure | Symptom | Prevention |
|---------|---------|------------|
| Over-documentation | Docs longer than code | Concise, not comprehensive |
| Stale docs | Docs don't match code | Update at implementation time |
| Missing context | Future readers confused | Include "why" not just "what" |
| Commit noise | Uninformative messages | Semantic commit convention |

**Verification Expectations**:
- Docs reflect current state
- Commit messages are meaningful
- Changelog is accurate

**NEVER carries implicitly**:
- Full implementation details (summarize)
- Review discussions (capture conclusions only)
- Exploratory findings (only final architecture)

---

### III.G AUDITOR

**Purpose**: Verify execution against specifications, produce audit packets.

**Inputs**:
- Plan document with acceptance criteria
- Implementation artifacts
- Review results
- Verification commands to run

**Outputs**:
- Audit packet (structured JSON)
  - Criteria results (pass/fail per criterion)
  - Drift analysis (what deviated from plan)
  - Evidence (command outputs, test results)
  - Recommendation (accept/reject/revise)

**Allowed Tools**:
- Read (examine artifacts)
- Bash (run verification commands)
- Grep (search for patterns)
- **No Write/Edit** (audit, not fix)

**Failure Modes**:
| Failure | Symptom | Prevention |
|---------|---------|------------|
| Claims without evidence | "It works" without proof | Require command output |
| Scope mismatch | Auditing wrong criteria | Reference original plan |
| False pass | Criteria not actually met | Independent verification |
| Audit theater | Going through motions | Genuine scrutiny |

**Verification Expectations**:
- Every acceptance criterion has explicit pass/fail
- Evidence is reproducible
- Drift is documented and justified

**NEVER carries implicitly**:
- Full execution history
- Internal reasoning of other agents
- Unstated assumptions

---

## IV. BOUNDED CONTEXT RULES

### The Information Boundary Principle

**Each sub-agent operates in a bounded context.** Information crossing boundaries must be:
1. Explicitly passed as input
2. Returned as structured output
3. Stored in repository (shared state)

### What MUST NEVER Be Carried Implicitly

| Information Type | Why Prohibited | Alternative |
|------------------|----------------|-------------|
| Full execution traces | Context bloat | Return summaries |
| Other agents' reasoning | Context contamination | Return conclusions only |
| Unstated assumptions | Coordination failure | Explicit in inputs |
| Current file contents | Redundancy, staleness | Read at execution time |
| Prior session state | Context window limits | Reference repository state |
| Intermediate results | Summary suffices | Structured outputs only |

### The Repository as Shared State

```
Sub-Agent A ──→ Repository ←── Sub-Agent B
     │              │               │
     │              ↓               │
     │    [files, state, events]    │
     │              │               │
     └──── (shared state) ─────────┘
```

Agents communicate through:
1. **Files**: Modified artifacts
2. **State vector**: `system_state.json`
3. **Events**: `events.jsonl`
4. **Packets**: Structured JSON documents

NOT through:
- Shared memory
- Direct message passing
- Coordinator's context window

### Bounded Context Example

**BAD** (implicit carrying):
```
Coordinator: "The Coder made these changes: [500 lines of diff].
             Now Reviewer, check this code."
```

**GOOD** (bounded context):
```
Coordinator: "Reviewer, examine files [list] against acceptance
             criteria [list]. Return findings as structured output."

Reviewer: (reads files directly, evaluates criteria, returns summary)
```

---

## V. ORCHESTRATION PATTERNS

### Pattern 1: Serial Pipeline

```
Planner → Coder → Reviewer → Auditor → Archivist
```

Use when: Tasks are inherently sequential, each stage depends on prior.

### Pattern 2: Parallel Exploration

```
       ┌── Explorer (tech stack) ──┐
Coord ─┼── Explorer (features) ────┼─→ Synthesis
       └── Explorer (architecture) ─┘
```

Use when: Multiple independent reconnaissance goals.

### Pattern 3: Parallel Implementation

```
Planner ─→ ┌── Coder (Track A) ─→ Reviewer A ──┐
           ├── Coder (Track B) ─→ Reviewer B ──┼─→ Auditor
           └── Coder (Track C) ─→ Reviewer C ──┘
```

Use when: Plan identifies independent work streams.

### Pattern 4: Review Specialization

```
Coder ─→ ┌── Reviewer (Security) ───┐
         ├── Reviewer (Quality) ────┼─→ Synthesis
         └── Reviewer (Completeness)┘
```

Use when: Different review concerns are independent.

### Pattern 5: Iterative Refinement

```
┌─→ Coder ─→ Reviewer ─→ [Issues?] ─→ Yes ─┐
│                           │              │
│                           No             │
│                           ↓              │
└──────────────────────── Done ←───────────┘
```

Use when: Code requires multiple revision cycles.

---

## VI. SUB-AGENT CREATION PROTOCOL

### Using Claude Code's `/agents` Command

```bash
# Create project-level agent
/agents create

# Prompts:
# 1. Agent description (purpose, expertise, constraints)
# 2. Available tools (select from list)
# 3. Model (Opus/Sonnet/Haiku)
# 4. Name (e.g., "coder", "reviewer", "security-auditor")

# Result: .claude/agents/<name>.md
```

### Agent Definition Template

```markdown
# Agent: [Name]

## Role
[One sentence purpose]

## Expertise
[Domain knowledge, skills]

## Constraints
- [What this agent should NOT do]
- [Boundaries of authority]

## Output Format
[Expected structure of returns]

## Model
[Opus/Sonnet/Haiku and rationale]
```

### Tool Selection by Role

| Role | Recommended Tools |
|------|-------------------|
| Planner | Read, Glob, Grep |
| Explorer | Read, Glob, Grep |
| Coder | Read, Edit, Write, Bash |
| Reviewer | Read, Grep, Bash |
| Archivist | Read, Write, Edit, Bash |
| Auditor | Read, Bash, Grep |

### Model Selection by Role

| Role | Recommended Model | Rationale |
|------|-------------------|-----------|
| Coordinator | Opus (main) | Synthesis, judgment |
| Planner | Sonnet or Opus | Planning quality matters |
| Explorer | **Haiku** | Speed/cost, simple task |
| Coder | Sonnet | Balance of quality/cost |
| Reviewer | **Haiku** | Surprisingly effective |
| Archivist | Haiku or Sonnet | Documentation is straightforward |
| Auditor | Sonnet | Judgment required |

---

## VII. VERIFICATION EXPECTATIONS SUMMARY

### Per-Role Verification

| Role | Must Verify |
|------|-------------|
| Coordinator | All sub-agents completed, results synthesized |
| Planner | Plan covers requirements, dependencies are acyclic |
| Explorer | Claimed files exist, summary accurate |
| Coder | Tests pass, criteria met, changes minimal |
| Reviewer | All files examined, findings actionable |
| Archivist | Docs match code, commits meaningful |
| Auditor | Criteria evaluated, evidence reproducible |

### Mesh-Level Verification

1. **Coverage**: Every task in plan assigned to an agent
2. **Completion**: Every agent returned summary
3. **Consistency**: No contradictions between agent outputs
4. **Integration**: Combined output achieves original goal

---

## VIII. FAILURE RECOVERY PATTERNS

### Single Agent Failure

```
1. Identify failed agent and failure type
2. If context issue: restart agent with fresh context
3. If capability issue: route to different agent/model
4. If persistent: escalate to Coordinator for manual intervention
```

### Coordination Failure

```
1. Capture current state in repository
2. Create continuation artifact with:
   - Completed work
   - In-progress work (state)
   - Remaining work
3. Start new Coordinator session with artifact
```

### Cascading Failure Prevention

- Each agent's work is atomic (complete or not started)
- No agent depends on another agent's in-progress state
- Repository is the only shared state
- Failures are isolated to single agent scope

---

## IX. DECISION LOG

| Decision | Status | Rationale |
|----------|--------|-----------|
| 7 core roles | **Tentative** | Covers observed workflow needs |
| Haiku for Explorer/Reviewer | **Tentative** | Cost optimization, practitioner validation |
| Repository as shared state | **Invariant** | Only scalable coordination mechanism |
| Bounded context rule | **Invariant** | Context window economics |
| No implicit carrying | **Invariant** | Coordination correctness |

---

**End of Sub-Agent Mesh Blueprint**
