# PRAC: Agentic Development Mastery Framework

**Scope**: Mental models, competence progression, failure taxonomy, practitioner philosophy
**Source**: Fleet Commander's Handbook (community synthesis, distilled 2026-02-01)
**Compression**: 13,200 words → ~2,500 words

---

## The Paradigm Shift

```
PROC AgenticParadigm:
sutra: "You program flight computers, not fly the plane—control outcomes, not keystrokes"
gloss: Claude Code is not a copilot (suggesting as you type) but an autonomous execution
       engine. The spaceship metaphor: set destinations, program flight plans, monitor
       instruments, intervene at decision points, ensure safe arrival.
spec:
    type: PRACTICE
    shift: "from writing code → directing an autonomous engine that writes code"
    cognitive_effort: "architecture and verification, not implementation"
    analogy: "spaceship commander, not manual pilot"
end
```

### Three Foundational Laws

1. **State Must Be Externalized** — Agent memory is temporary. Everything critical must live in files that persist across sessions, survive crashes, and enable multi-agent coordination. If it's only in the context window, it's one compaction away from gone.

2. **Verification Must Be Automated** — Tests, linters, and type-checkers are primary quality gates, not human code review. Claude should be constrained within systems where bad code cannot pass silently.

3. **Intelligence Emerges from Constraints** — Paradoxically, Claude performs better with precise constraints than vague instructions. More rules ≠ worse output (up to the ~100-150 rule ceiling). Clear boundaries focus reasoning.

---

## Five Competence Stages

```
PROC CompetenceProgression:
sutra: "Supervised → Verified → Planned → Task-Based → Fleet Command"
gloss: Progressive trust-building from manual verification to multi-instance orchestration.
       Most practitioners spend initial time at Stage 2. Stage 5 is pure architecture.
spec:
    type: PRACTICE
    stages:
      - name: "Supervised Execution"
        mode: "Simple tasks, manual verification of every change"
        review: "every line"
        temporary: true
      - name: "Verified Autonomy"
        mode: "Larger tasks, automated verification (tests, linters)"
        review: "test results, not code"
        note: "Where most initial time should be spent"
      - name: "Planned Execution"
        mode: "Plan Mode → execute. Two-phase workflow"
        review: "plans, not individual lines"
      - name: "Task-Based Direction"
        mode: "Feature-level direction with success criteria"
        review: "completed work, not in-progress"
      - name: "Fleet Command"
        mode: "Multiple parallel instances on different tasks/branches"
        review: "architecture and integration only"
    growth_timeline:
      week_1: "Foundation — setup CLAUDE.md, conservative settings, single-file tasks"
      week_2_3: "Expansion — Plan Mode, multi-file tasks, build rules from mistakes"
      month_1_2: "Integration — task lists, session rhythms, autonomous confidence"
      month_2_plus: "Mastery — parallel instances, feature-level, CLAUDE.md as asset"
end
```

---

## Five Mental Models

### Model 1: The Brilliant Intern
Claude has read every programming book ever written but has zero context about your specific project, forgets everything between sessions, does exactly what asked (including mistakes), and won't push back on misguided requests. You wouldn't hand a brilliant intern critical production code and walk away.

### Model 2: The Stochastic Coworker
Outputs are probabilistic, not deterministic. Same input may produce slightly different outputs. "Usually works" ≠ "always works." Verification is non-negotiable. "It worked once" proves nothing.

### Model 3: Context as Working Memory
Like human working memory: limited capacity, degrades with overload, benefits from external aids (notes, files), works best when focused on one thing. Don't expect Claude to remember a complex plan across sessions without writing it down.

### Model 4: The Constitutional Monarchy
CLAUDE.md defines the laws. Claude is the monarch — powerful but constitutionally bound. A constitution that tries to specify everything becomes impossible to follow. A constitution that specifies nothing provides no guidance. State principles, not exhaustive rules.

### Model 5: The Feedback Loop
The fundamental unit of agentic development:
```
Intent → Action → Verification → Learning → (repeat)
```
A weak link anywhere breaks the entire loop. Intent must be clear. Action must be scoped. Verification must be automated. Learning must persist (CLAUDE.md updates).

---

## Five Transition Traps

| Trap | Symptom | Fix |
|------|---------|-----|
| **Micromanagement** | Hovering over every line | Trust verification systems, not eyes |
| **Abdication** | "Claude handles everything" | Maintain oversight; automation ≠ abdication |
| **Infinite Context Illusion** | Treating 200K as unlimited | Performance degrades at 70%; danger at 80%+ |
| **Perfect CLAUDE.md** | Over-engineering before first use | Build from actual mistakes, not theory |
| **Tool Confusion** | Treating as chat or copilot | It's an execution engine—direct, don't converse |

---

## Failure Taxonomy

| Category | Symptoms | Root Cause | Fix |
|----------|----------|------------|-----|
| **Context** | Forgets instructions, contradicts itself | Context exhaustion/compaction | Reset session, externalize state |
| **Instruction** | Wrong thing done confidently | Ambiguous instructions | Clarify, provide examples, update rules |
| **Verification** | Bugs reach production | Inadequate test coverage | Test-first, never skip verification |
| **Scope** | Task balloons beyond intent | Unclear boundaries | Explicit decomposition and limits |
| **Environmental** | Works locally, fails elsewhere | Missing dependencies | Document env, containers, CI verify |

### The Postmortem Practice

Every failure is a learning opportunity. Structured capture:
1. **Timeline**: Task → Action → Detection → Impact
2. **Root Cause**: Why? What would have prevented it?
3. **Prevention**: Rule for CLAUDE.md? Permission change? Test to add?
4. **Learning**: What does this teach about agentic work?

### The Escalation Pattern

When Claude is stuck, escalate through five levels:
1. Clarify the instruction
2. Provide more context (files, examples)
3. Decompose into smaller tasks
4. Do the hard part yourself, let Claude handle the rest
5. Accept this task isn't suitable for automation

---

## Operational Rhythms

### Daily Rhythm
- **Morning**: Orient — review task board, check for failures, set priorities
- **Work Sessions**: Execute — one task per session, plan complex work, commit frequently
- **End of Day**: Persist — ensure commits, write handoff notes, capture learnings, update CLAUDE.md

### Session Pattern
```
Set context → State task → Plan (if non-trivial) → Review plan →
Execute with verification → Commit → Update state → Reset or continue
```

### Recovery Pattern
```
Stop immediately (Escape) → Assess (git status/diff) → Recover (git checkout/reset) →
Understand why → Prevent (add rule/permission) → Continue
```

Git is the safety net. Frequent commits = always recoverable.

---

## The Philosophy

**On Trust**: Earned, not assumed. Start with tight constraints, expand as reliability is demonstrated. Never fully trust. Always verify. Automation ≠ abdication.

**On Control**: Control outcomes, not keystrokes. Define success; let Claude determine approach. Leverage comes from architectural thinking, not implementation details.

**On Learning**: Mistakes are normal for both human and agent. Convert failures into CLAUDE.md rules. Systematic improvement, not perfection.

**On Collaboration**: Complementary partnership — humans bring judgment, context, creativity; Claude brings execution, consistency, tirelessness. Neither complete alone.

**On the Compounding Asset**: CLAUDE.md is a compounding investment. Every rule, pattern, and anti-pattern transforms Claude from generic AI into a specialist in your codebase. Over months, accumulated institutional knowledge makes every future task faster. This is the real leverage — not any single task, but the accumulated wisdom.

---

## Key Numerical Insights

- **Rule capacity**: ~100-150 rules in CLAUDE.md before crowding effects degrade compliance
- **Context degradation**: Quality drops noticeably at 70% utilization; danger zone at 80%+
- **System prompt overhead**: ~10% of context consumed by system prompt
- **Optimal parallel instances**: 3-7 concurrent workers; beyond 10, coordination overhead dominates

---

## Cross-References

- `SYNTHESIS-claude_code_architecture.md` — Technical architecture deep-dive
- `MECH-context_compaction_strategies.md` — Compaction mechanics
- `MECH-hooks_lifecycle_automation.md` — Automation hooks
- `MECH-task_orchestration.md` — Task management patterns
- `PRAC-parallel_claude_orchestration.md` — Multi-instance execution
- `[[CANON-25000-MEMORY_ARCH-lattice]]` — Memory architecture (CLAUDE.md hierarchy rationale)
