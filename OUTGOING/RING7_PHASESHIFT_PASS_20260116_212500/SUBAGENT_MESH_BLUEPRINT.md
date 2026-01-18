# Sub-Agent Mesh Blueprint
**Generated**: 2026-01-17T05:30:00Z
**Purpose**: Architecture for multi-agent coordination within Ring 7

---

## Executive Summary

The sub-agent mesh enables parallel execution of specialized tasks within Claude Code's agentic loop. Rather than processing sequentially, a **Coordinator** dispatches work to **Workers** (specialized sub-agents) and synthesizes results.

**Key Insight**: Claude Code's Task tool already implements sub-agent dispatch. This blueprint formalizes the coordination patterns that maximize effectiveness.

---

## Mesh Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                     SUB-AGENT MESH                                  │
│                                                                      │
│                    ┌──────────────────┐                             │
│                    │   COORDINATOR    │                             │
│                    │   (Main Thread)  │                             │
│                    └────────┬─────────┘                             │
│                             │                                        │
│           ┌─────────────────┼─────────────────┐                     │
│           │                 │                 │                     │
│     ┌─────▼─────┐     ┌─────▼─────┐     ┌─────▼─────┐             │
│     │  PLANNER  │     │  EXPLORER │     │   CODER   │             │
│     └───────────┘     └───────────┘     └───────────┘             │
│                                                                      │
│     ┌───────────┐     ┌───────────┐     ┌───────────┐             │
│     │  REVIEWER │     │  ARCHIVIST│     │  AUDITOR  │             │
│     └───────────┘     └───────────┘     └───────────┘             │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Agent Role Specifications

### Coordinator (Main Thread)

**Purpose**: Orchestrate work, maintain coherence, synthesize results

**Responsibilities**:
1. Parse incoming directive/plan
2. Decompose into parallelizable tasks
3. Dispatch to appropriate workers
4. Monitor execution progress
5. Reconcile worker outputs
6. Produce unified result

**Anti-Patterns**:
- ✗ Doing work that should be delegated
- ✗ Waiting sequentially when parallel is possible
- ✗ Dispatching without clear acceptance criteria
- ✗ Synthesizing without verification

### Planner (Task tool: subagent_type=Plan)

**Purpose**: Design implementation strategies before execution

**Inputs**:
- User request or feature specification
- Current codebase context
- Constraints and requirements

**Outputs**:
- Step-by-step implementation plan
- Critical files identification
- Architectural trade-offs
- Risk assessment

**Best Practices**:
```yaml
Use_When:
  - New feature implementation (3+ files affected)
  - Refactoring that touches multiple modules
  - Architectural decisions with multiple valid approaches
  - Complex debugging requiring systematic analysis

Avoid_When:
  - Simple single-file edits
  - Clear, well-specified tasks
  - Pure research/exploration (use Explorer instead)
```

### Explorer (Task tool: subagent_type=Explore)

**Purpose**: Rapidly search and understand codebases

**Inputs**:
- Search query or question
- Codebase scope (path patterns)
- Thoroughness level (quick/medium/very_thorough)

**Outputs**:
- Relevant file locations
- Code structure understanding
- Pattern identification
- Answer to codebase questions

**Best Practices**:
```yaml
Use_When:
  - Finding files by patterns (e.g., "**/*.tsx")
  - Searching for keywords across codebase
  - Understanding how systems work
  - Locating where specific logic lives

Thoroughness_Levels:
  quick: Basic pattern matching, first few hits
  medium: Moderate exploration across likely locations
  very_thorough: Comprehensive search across naming conventions
```

### Coder (Implicit via Edit/Write tools)

**Purpose**: Implement code changes

**Not a separate sub-agent** but the core editing capability:
- Read → Understand → Edit pattern
- Verification before claiming done
- Commit discipline

### Reviewer (Future sub-agent type)

**Purpose**: Verify code quality and correctness

**Potential Responsibilities**:
- Run tests and report results
- Check for security vulnerabilities
- Verify acceptance criteria
- Lint and format validation

**Current Workaround**: Use Task with general-purpose agent and explicit review prompt.

### Archivist (Future sub-agent type)

**Purpose**: Manage knowledge persistence

**Potential Responsibilities**:
- Create continuation packets
- Update ledgers
- Archive processed sources
- Maintain indexes

**Current Workaround**: Coordinator handles directly or uses Bash for ledger updates.

### Auditor (Implicit via verification)

**Purpose**: Ensure Definition of Done

**Already Implemented** via:
- `make verify` commands
- Pre-commit hooks
- Schema validation
- Ledger ground truth checks

---

## Dispatch Patterns

### Pattern 1: Parallel Exploration

**When**: Need to search multiple areas simultaneously

```yaml
Pattern: Parallel_Exploration
Description: Fan-out search across different domains

Example:
  Coordinator: "Find all authentication-related code"
  Dispatch:
    - Explorer(query="authentication middleware", thoroughness=medium)
    - Explorer(query="login form components", thoroughness=medium)
    - Explorer(query="session management", thoroughness=medium)
  Synthesis: Merge results, identify patterns, report locations
```

### Pattern 2: Plan-Then-Execute

**When**: Complex implementation requiring upfront design

```yaml
Pattern: Plan_Then_Execute
Description: Strategy before action

Example:
  Coordinator: "Add user preferences feature"
  Phase_1:
    - Planner(feature_spec, codebase_context)
    - Output: Implementation plan with steps
  Phase_2:
    - For each step in plan:
        - Coder(implement step)
        - Verify(check acceptance criteria)
  Phase_3:
    - Auditor(run full test suite)
```

### Pattern 3: Explore-Plan-Execute

**When**: Unknown codebase or feature area

```yaml
Pattern: Explore_Plan_Execute
Description: Understand before designing, design before building

Example:
  Coordinator: "Refactor payment processing"
  Phase_1:
    - Explorer(query="payment processing", thoroughness=very_thorough)
    - Output: Understanding of current architecture
  Phase_2:
    - Planner(refactor_goal, current_understanding)
    - Output: Refactoring strategy
  Phase_3:
    - Execute plan with incremental verification
```

### Pattern 4: Background Processing

**When**: Long-running tasks that shouldn't block

```yaml
Pattern: Background_Processing
Description: Fire and check later

Example:
  Coordinator: "Run comprehensive test suite"
  Dispatch:
    - Task(run_tests, run_in_background=true)
  Continue: Work on other tasks
  Later:
    - TaskOutput(task_id) or Read(output_file)
```

---

## Context Propagation

### Problem: Sub-Agents Lack Coordinator Context

Each sub-agent starts fresh. The Coordinator must provide:
1. Minimal viable context
2. Clear task boundaries
3. Expected output format
4. Relevant file paths

### Solution: Context Packet Pattern

```yaml
Context_Packet:
  task_description: Clear, actionable instruction
  relevant_files:
    - path/to/file1.ts
    - path/to/file2.ts
  constraints:
    - "Do not modify protected files"
    - "Maintain backwards compatibility"
  output_expectations:
    - "Return list of affected files"
    - "Include line numbers for changes"
  background:
    - "This is part of larger refactoring effort"
    - "Other agents are working on related modules"
```

### Anti-Pattern: Context Dump

**Don't**: Pass entire conversation history to sub-agents
**Do**: Extract relevant context into focused packet

---

## Coordination Protocols

### Protocol 1: Work Assignment

```yaml
Assignment_Protocol:
  1. Coordinator identifies parallelizable tasks
  2. For each task:
     - Define acceptance criteria
     - Estimate complexity
     - Select appropriate agent type
     - Package context
  3. Dispatch simultaneously (single message, multiple Task calls)
  4. Monitor for completion
```

### Protocol 2: Result Synthesis

```yaml
Synthesis_Protocol:
  1. Collect all sub-agent outputs
  2. Check for contradictions
  3. Merge non-conflicting results
  4. Resolve conflicts via:
     - Coordinator judgment
     - Additional verification
     - Escalation to Principal if stakes high
  5. Produce unified output
```

### Protocol 3: Error Handling

```yaml
Error_Protocol:
  1. Sub-agent reports failure
  2. Coordinator assesses:
     - Recoverable? → Retry with adjusted parameters
     - Scope issue? → Reduce scope, retry
     - Blocker? → Document and escalate
  3. Don't block other parallel work on single failure
```

---

## Sub-Agent Limits and Thresholds

### Parallel Dispatch Limits

| Scenario | Max Parallel | Reason |
|----------|--------------|--------|
| Exploration | 3-5 | Diminishing returns |
| Background tasks | 2-3 | System resource constraints |
| Mixed workload | 3 | Context management |

### Complexity Thresholds

| Complexity | Approach |
|------------|----------|
| Low (single file, clear change) | Direct execution, no sub-agents |
| Medium (2-5 files, clear pattern) | Single sub-agent if needed |
| High (5+ files, unclear pattern) | Plan → parallel execution |
| Very High (architectural change) | Explore → Plan → staged execution |

---

## Integration with Ring 7 Components

### Sub-Agents and Execution Substrate

Sub-agents use the same execution substrate as Coordinator:
- Same tool access (based on permissions)
- Same context limits
- Same verification requirements

### Sub-Agents and Tooling Gateway

Each sub-agent has access to:
- **Native tools**: Read, Write, Edit, Glob, Grep, Bash
- **MCP servers**: As configured in parent session
- **Scoped tools**: Based on subagent_type

### Sub-Agents and Neo-Plugins

Currently:
- Sub-agents inherit MCP configuration
- No A2A (agent-to-agent) protocol between sub-agents

Future:
- Direct sub-agent communication via A2A
- Shared memory via MCP memory servers

---

## Mesh Failure Modes

### FM-MESH-001: Coordinator Bottleneck
**Symptom**: All work flows through slow synthesis
**Cause**: Over-centralized coordination
**Prevention**: Empower sub-agents with clear boundaries, reduce round-trips

### FM-MESH-002: Context Starvation
**Symptom**: Sub-agents ask for information Coordinator has
**Cause**: Inadequate context packets
**Prevention**: Include all necessary context upfront

### FM-MESH-003: Result Collision
**Symptom**: Sub-agents modify same files
**Cause**: Overlapping scope
**Prevention**: Explicit file/scope boundaries per sub-agent

### FM-MESH-004: Dispatch Without Return
**Symptom**: Background tasks never checked
**Cause**: Fire-and-forget without follow-up
**Prevention**: Track all dispatches, check all outputs

---

## Implementation Checklist

### Immediate (Use Today)

- [x] Use Task tool with appropriate subagent_type
- [x] Dispatch parallel searches with multiple Task calls in single message
- [x] Use run_in_background for long operations
- [x] Provide clear context in prompt parameter

### Near-Term (Configure)

- [ ] Define standard context packet templates
- [ ] Create coordination patterns in CLAUDE.md
- [ ] Add sub-agent dispatch to slash commands

### Future (When Available)

- [ ] Custom sub-agent types (Reviewer, Archivist)
- [ ] Inter-agent communication protocol
- [ ] Shared memory across sub-agents

---

## Summary

The sub-agent mesh transforms Claude Code from single-threaded execution to parallel specialist coordination. Key principles:

1. **Coordinator orchestrates, workers execute**
2. **Parallel dispatch when independent**
3. **Context packets prevent starvation**
4. **Synthesis reconciles results**
5. **Verification closes the loop**

This blueprint formalizes what's already possible with Claude Code's Task tool while identifying patterns that maximize effectiveness.

---

## Version History

**v1.0.0** (2026-01-17): Initial sub-agent mesh specification
- Agent role definitions
- Dispatch patterns
- Coordination protocols
