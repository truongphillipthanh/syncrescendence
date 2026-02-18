# PRAC: Sub-Agent Delegation Guide

**Scope**: When and how to delegate to sub-agents for token efficiency
**Linear**: SYN-10 / IMPL-A-0006
**Status**: CANONICAL

---

## The Decision

Every task has a choice: execute inline (main context) or fork to a sub-agent (separate context). The wrong choice either wastes tokens or misses parallelism.

---

## Decision Tree

```
Is the task independent of current conversation?
├── NO → Execute inline (main context)
└── YES →
    Does it require writing/editing files?
    ├── NO → Use Explore agent (read-only, fast, cheap)
    └── YES →
        Is it > 5 minutes of work?
        ├── NO → Execute inline
        └── YES →
            Can multiple tasks run in parallel?
            ├── YES → Fork multiple sub-agents (Blitzkrieg)
            └── NO → Fork single general-purpose agent
```

---

## Skill Context Annotation

Skills can declare their execution context preference using a comment header:

```markdown
<!-- context: fork -->
<!-- model: haiku -->
<!-- reason: Heavy file scanning, independent of main thread -->

# Skill: Codebase Health Check
...
```

### Context Values

| Value | Meaning | Invocation |
|-------|---------|-----------|
| `inline` | Execute in main agent context | Skill tool (default) |
| `fork` | Execute in isolated sub-agent | Task tool with subagent_type |
| `parallel` | Can be batched with other fork tasks | Multiple Task tool calls |

### When to Mark `context: fork`

A skill SHOULD be marked `fork` when:
- It performs read-heavy analysis (corpus surveys, audits)
- Its output is a summary, not an ongoing conversation
- It consumes >10K tokens typically
- It doesn't need iterative human feedback during execution

A skill SHOULD remain `inline` when:
- It modifies conversation state (e.g., memory updates)
- Its output feeds directly into the next step
- It requires back-and-forth with the user
- It's under 2K tokens

---

## Model Selection for Forked Skills

| Complexity | Model | Token Cost | Use Case |
|-----------|-------|-----------|----------|
| Low | Haiku | ~$0.001/task | File search, pattern matching, quick validation |
| Medium | Sonnet | ~$0.01/task | Code review, implementation, testing |
| High | Opus | ~$0.10/task | Architecture, complex reasoning, multi-step planning |

**Default to Haiku for explore, Sonnet for execution.** Only escalate to Opus when the task genuinely requires deep reasoning.

---

## Constellation Agent Mapping

In Syncrescendence, sub-agent delegation maps to Constellation roles:

| Delegation Target | Agent | Model | When |
|-------------------|-------|-------|------|
| `explore` sub-agent | (built-in) | Haiku | Quick searches, file discovery |
| `general-purpose` sub-agent | (built-in) | Sonnet | Implementation tasks |
| Dispatch to Adjudicator | Codex CLI | Sonnet | Quality review, testing |
| Dispatch to Cartographer | Gemini CLI | Gemini 2.5 Pro | Research, 1M context analysis |
| Dispatch to Psyche | OpenClaw | GPT-5.3-codex | Automation, system cohesion |

**Rule**: Intra-session delegation uses sub-agents (Task tool). Cross-session delegation uses dispatch.sh (INBOX files).

---

## Token Savings Examples

| Scenario | Inline Cost | Forked Cost | Savings |
|----------|------------|-------------|---------|
| Audit 79 CANON files | ~80K tokens in main | ~80K in sub + 2K summary | Main context preserved |
| 3 parallel explores | ~45K sequential in main | ~15K each in parallel, 3K total returned | 80% main context saved |
| Research task (read-only) | ~30K polluting main | ~30K isolated + 1K summary | Main stays at peak intelligence |

The savings aren't in total tokens consumed — they're in **main context preservation**. A main agent at 20% usage is dramatically smarter than one at 70%.

---

## Anti-Patterns

1. **Forking trivial tasks**: Sub-agent overhead (~2K tokens for init) makes tasks under 3K tokens more expensive when forked.
2. **Not reading sub-agent output**: The summary returned IS the result. Process it, don't just acknowledge.
3. **Using Opus for explore tasks**: Haiku finds files just as well at 1/100th the cost.
4. **Forking tasks that need conversation context**: If the sub-agent needs to understand the current discussion, it can't — fork with explicit context in the prompt.

---

## Cross-References

- `04-SOURCES/research/MECH-subagent_delegation.md` — Full mechanics (built-in types, invocation methods, coordinator pattern)
- `02-ENGINE/REF-ROSETTA_STONE.md` — Gap Analysis G8
- `PRAC-blitzkrieg_worktree_isolation.md` — Parallel execution via worktrees
- `PRAC-ralph_pattern_execution.md` — Fresh context loops (extreme version of context isolation)
