# MECH: Context Compaction Strategies

**Scope**: 75% rule, manual vs auto compaction, focus instructions, surviving compaction

---

## Core Problem

```
TERM ContextScarcity:
sutra: "200K ceiling is lie—quality degrades at 150K, collapses at 190K"
gloss: LLM context windows are finite attention, not infinite storage. As tokens
       accumulate, recall accuracy decreases ("context rot"). Auto-compaction at
       95% is emergency measure—lossy summarization often drops critical constraints.
spec:
    type: MECHANISM
    context_limit: 200K tokens (Sonnet 4.5)
    quality_sweet_spot: 75% (~150K)
    danger_zone: ">80% (~160K)"
    auto_compact_trigger: "~95% (~190K)"
    degradation_symptoms: [forgetting_instructions, looping_answers, slower_responses, increased_errors]
end
```

---

## The 75% Rule

```
NORM SeventyFivePercent:
sutra: "Free space enables reasoning quality that makes utilized tokens valuable"
gloss: "Sometimes the path to better performance is artificial constraints. Stopping
       at 75% utilization feels wasteful... But that free space enables the reasoning
       quality that makes the utilized tokens valuable."
spec:
    threshold: 75% maximum utilization
    rationale: "Performance degrades BEFORE hard limit"
    action: "Manual compaction when approaching 70%"
    anti_pattern: "Running until auto-compact at 95%"
end
```

---

## Compaction Mechanics

### Auto-Compaction
- **Trigger**: ~95% context capacity (~190K tokens)
- **Process**: System summarizes conversation history
- **Problem**: "Opaque, error-prone, not well-optimized"—squishes down history, may miss nuances

### Manual Compaction
- **Command**: `/compact`
- **Control**: User-initiated at sensible breakpoints
- **Enhancement**: Focus instructions guide preservation

```bash
/compact Focus on code changes and test results
```

---

## Focus Instructions Pattern

```
PROC FocusedCompaction:
sutra: "Tell Claude what to preserve—don't let it guess"
gloss: Default compaction guesses importance. Focus instructions force model
       to prioritize specific state over conversational fluff.
spec:
    syntax: '/compact "Preserve list of 5 architectural constraints and path to plan.md"'
    examples:
        - '/compact "Keep the API contract decisions and current file paths"'
        - '/compact "Retain all test names and their pass/fail status"'
        - '/compact "Preserve the migration checklist and completed steps"'
    anti_pattern: "Generic /compact without guidance"
end
```

---

## The Plan Mode Anchor

Most robust pattern for surviving compaction:

```
PROC PlanFileAnchor:
    1: "Agent explores code"
    2: "Agent writes PLAN.md (checklist of steps)"
    3: "User approves"
    4: "Agent executes Step 1"
    5: "Agent updates PLAN.md to mark Step 1 complete"

    compaction_event:
        "Even if context wiped or compacted poorly,
         agent reads PLAN.md to re-orient"

    benefit: "Physical file acts as External Working Memory
             immune to context decay"
end
```

**Key insight**: State in files > state in context. Files survive; context doesn't.

---

## Compaction Timing

| Trigger | Action | Quality |
|---------|--------|---------|
| 70% utilized | Manual `/compact` with focus | High—controlled preservation |
| Task phase complete | Manual `/compact` | High—natural breakpoint |
| Switching context | `/compact` or new session | High—prevents pollution |
| 95% (auto-compact) | Emergency summary | Low—lossy, unpredictable |

---

## Session Strategies

### Strategy A: Proactive Manual Compaction
```bash
# At logical breakpoints
/compact "Preserve planning discussion, architectural constraints, and plan.md path"
```
Better than waiting for auto-compact.

### Strategy B: Session Forking
Instead of fighting compaction in single long session:
1. Complete sub-task
2. Terminate session
3. Start new session with result as input

**Benefit**: Fresh context window, no accumulated noise.

### Strategy C: Externalize State Continuously
```
NORM ExternalizeState:
sutra: "State in files, not context—Claude can re-read, can't re-remember"
spec:
    patterns:
        - "Write plans to PLAN.md"
        - "Write decisions to DECISIONS.md"
        - "Update progress in PROGRESS.md"
        - "Maintain checklist in TODO.md"
    trigger: "Before any significant state change, persist to file"
    recovery: "After compaction, read state files to re-orient"
end
```

---

## What Persists Through Compaction

| Element | Survives Compaction? |
|---------|---------------------|
| CLAUDE.md instructions | Yes—reloaded fresh |
| Files on disk | Yes—can be re-read |
| Task list (new system) | Yes—stored in ~/.claude/tasks/ |
| Conversation nuances | No—summarized away |
| Specific constraints | Maybe—depends on focus instructions |
| Error context | Often lost |

---

## Degradation Symptoms

Watch for these signs that context is degrading:

1. **Forgetting earlier instructions**: Repeating behaviors you corrected
2. **Looping on answers**: Same response patterns
3. **Slower responses**: More processing with less coherence
4. **Increased errors**: Mistakes in previously-working patterns
5. **Contradicting itself**: Inconsistent with earlier statements

**Action**: Don't push through—compact or restart.

---

## Claude Code v2.1.3+ Improvements

```
NORM ImprovedCompaction:
sutra: "Plans and Todos persist across compaction—start with Plan Mode"
gloss: Post v2.1.3, auto-compaction works much better IF you start with Plan Mode
       and explicitly request comprehensive todo list. Plans and Todos persist.
spec:
    version: "2.1.3+"
    improvement: "Better preservation of structured state"
    pattern: "Start session in Plan Mode → Create comprehensive todo → Execute"
    caveat: "Still externalize critical state to files as backup"
end
```

---

## Anti-Patterns

### Running Until Exhaustion
Hardest lesson to learn. "Sometimes the path to better performance is artificial constraints."

### Over-relying on Auto-Compaction
> "Auto-compact leads to corruption, inconsistent behavior"

Better: Proactive manual compaction with explicit preservation.

### Infinite Compaction Loop
Claude reads same files → attempts compaction → restarts looping.

**Recovery**: Press Esc to interrupt → `/clear` → Start fresh session.

### Context Confusion After Compaction
Claude becomes "dumber," forgets what it built.

**Recovery**:
- `/clear` more frequently
- Break into smaller tasks
- Use `/compact` manually with focus instructions
- Size tasks to complete within 75% context

---

## Configuration

```json
// settings.json
{
  "compaction": {
    "auto_compact_threshold": 0.75,  // Lower than default
    "preserve_fields": ["plan", "todos", "decisions"]
  }
}
```

Some practitioners disable auto-compaction entirely, preferring to restart sessions.

---

## The Ralph Pattern: Fresh Context Alternative

```
TERM RalphPattern:
sutra: "Wipe the whiteboard after every task—AI operates in smartest mode with fresh context"
gloss: Ralph works because it keeps AI operating at peak capability by wiping context
       completely after each task. No compaction, no growing memory files, no accumulated noise.
spec:
    type: PRACTICE
    creator: "Jeff Huntley"
    key_insight: "LLMs get worse as context grows—fresh start every time"
    anti_pattern: "Compaction defeats the purpose"
end
```

### Canonical Implementation

```bash
#!/bin/bash
# ralph.sh
while true; do
    claude -p "$(cat prompt.md)" --max-turns 50
    if grep -q "passes: true" prd.md && ! grep -q "passes: false" prd.md; then
        echo "All tasks complete!"
        break
    fi
    sleep 5
done
```

### Required Files
- **prompt.md** — Static instructions (NEVER changes). Reads prd.md, finds highest priority incomplete task, implements, validates, exits.
- **prd.md** — Task list with `passes: true/false` flags per task. Each task has category, description, validation steps.
- **activity.md** — Log file. Each loop appends what happened. Visibility without bloating context.
- **settings.json** — Sandbox permissions to constrain damage radius.

### Common Mistakes
1. **Using compaction** instead of fresh context wipe — AI loses critical information.
2. **Growing memory files** — Models are verbose; 10 iterations stuffs context before task starts. Keep prompt static.
3. **Max iterations cap** — Cuts off discovery. Let it run until all tasks pass.

### Variations
- **Parallel Ralphs**: Multiple instances with `TASK_FILTER` for different categories.
- **Browser validation**: AI opens app and clicks through flows instead of just running tests.
- **GitHub Issues as tasks**: Ralph picks most important open issue, implements, closes.

### Cost Math
| Setup | Cost | Outcome |
|-------|------|---------|
| Correct (fresh context) | ~$30-50 | Working proof of concept |
| Wrong (compaction/growing files) | ~$300 | Broken mess, rebuild manually |

### When to Use Ralph
**Good for**: Proof of concepts, validating architecture, overnight builds, exploratory implementation.
**Not for**: Production engineering (needs human review), edge cases requiring judgment, architectural decisions requiring context.

---

## Cross-References

- [[SYNTHESIS-claude_code_architecture]] → ContextManagement TERM block
- [[MECH-task_orchestration]] → Task persistence across compaction

---

## Consolidated From

- `praxis/05-SIGMA/practice/PRAC-ralph_pattern_execution.md` — Ralph pattern (fresh context loops, canonical implementation, required files, common mistakes, variations, cost math, when-to-use guidance)
