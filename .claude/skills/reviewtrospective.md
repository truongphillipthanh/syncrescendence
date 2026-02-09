# REVIEWTROSPECTIVE SKILL
## Post-Task Review — Analyze, Capture, and Improve

**Version**: 1.0.0
**Last Updated**: 2026-02-08
**Authority**: Oracle 13

---

## PURPOSE

Triggered after any completed task to analyze what worked, what did not, and what was surprising. Captures method improvements and technique kaizen. Updates `DYN-REVIEWTROSPECTIVE_LOG.md` and feeds into the method_kaizen skill.

---

## WHEN TO USE

Trigger this skill when:
- A non-trivial task or directive completes (SUCCESS, PARTIAL, or FAILED)
- A Blitzkrieg concludes (all lanes converged)
- A session ends with significant work completed
- Sovereign requests a retrospective on a specific effort
- A task fails and root cause analysis is needed

**Note**: Trivial tasks (single-file edits, ledger updates) do not need reviewtrospectives. Use judgment: if you learned something or something went wrong, write the review.

---

## PROCESS

### 1. Gather Evidence

Before analyzing, collect:

1. **Execution log**: Read relevant entry from `DYN-EXECUTION_STAGING.md`
2. **Git history**: `git log --oneline -10` for recent commits from the task
3. **Plan vs reality**: Compare the original plan (if any) to actual execution
4. **Time spent**: Estimate from session timestamps
5. **Artifacts produced**: List files created/modified
6. **Verification results**: Did all checks pass? Which failed?

### 2. Analyze

Answer these questions honestly:

**What worked well?**
- Techniques that accelerated progress
- Decisions that proved correct
- Tools or scripts that saved time
- Patterns worth repeating

**What did not work?**
- Approaches that wasted time or produced errors
- Assumptions that proved wrong
- Tools or processes that created friction
- Communication failures between agents

**What was surprising?**
- Unexpected complexity or simplicity
- Discoveries about the codebase or system
- Emergent patterns not anticipated in the plan
- Performance or quality observations

**What would you do differently?**
- Specific alternative approaches
- Better tooling or scripting
- Different agent assignment
- Changed scope or ordering

### 3. Capture

Write the reviewtrospective to `00-ORCHESTRATION/state/DYN-REVIEWTROSPECTIVE_LOG.md`:

```markdown
### REVIEW-<task-id> | YYYY-MM-DD HH:MM

**Task**: <task identifier or description>
**Outcome**: SUCCESS | PARTIAL | FAILED
**Duration**: <estimated time>
**Agent**: <executing agent>
**Plan Mode**: BLITZKRIEG | SURGICAL | SURVEY | FORTIFY | ADHOC

#### What Worked
- <observation 1>
- <observation 2>

#### What Did Not Work
- <observation 1>
- <observation 2>

#### Surprises
- <observation 1>

#### Improvements Identified
- **METHOD**: <repeatable improvement> — Candidate for: <skill/hook/script>
- **TECHNIQUE**: <specific technique> — Apply to: <domain>
- **AUTOMATION**: <automation opportunity> — Script: <proposed script name>

#### Kaizen Score
- Velocity: <faster/same/slower than expected>
- Quality: <higher/same/lower than expected>
- Learning: <high/medium/low new insight>

---
```

### 4. Create State File (First Time Only)

If `DYN-REVIEWTROSPECTIVE_LOG.md` does not exist, create it with this header:

```markdown
# DYN-REVIEWTROSPECTIVE_LOG.md
## Post-Task Review Log — Method and Technique Improvement Capture

**Created**: 2026-02-08
**Protocol**: Append only. Never edit existing entries. One entry per completed task review.
**Skill**: `.claude/skills/reviewtrospective.md`

---

## Schema

Each entry contains:
- **Task reference**: Links to execution log and plan
- **Outcome assessment**: What happened vs what was expected
- **Improvement candidates**: Methods, techniques, and automation opportunities
- **Kaizen score**: Velocity, quality, and learning metrics

Entries compact into `ARCH-REVIEWTROSPECTIVE_HISTORY.md` at 10-entry threshold.

---

## Log

```

### 5. Feed Forward

After writing the review:

1. **Count improvement candidates**: If 3+ improvements of the same type accumulate across reviews, flag for method_kaizen skill
2. **Update execution staging**: Add review link to the task's execution log entry
3. **Log to ledger**: `bash append_ledger.sh COMPLETE commander sovereign "REVIEW-<task-id>"`
4. **Compact if needed**: If log exceeds 10 entries, run `compact_wisdom.sh`

---

## ANTI-PATTERNS

1. **Skipping reviews on failures**: Failed tasks are the MOST valuable to review. Never skip.

2. **Vague observations**: "It was hard" is not useful. "The CSV validation step took 15 minutes because the backup pattern required manual verification" is useful.

3. **Blame without solutions**: Do not just note what went wrong. Always include what would be different next time.

4. **Over-reviewing trivials**: A single `fix: typo` commit does not need a reviewtrospective. Reserve for substantive work.

5. **Orphan improvements**: Every improvement candidate must specify where it applies and whether it is a method, technique, or automation opportunity.

---

## CROSS-REFERENCES

- `00-ORCHESTRATION/state/DYN-REVIEWTROSPECTIVE_LOG.md` — Review log (created by this skill)
- `00-ORCHESTRATION/state/DYN-EXECUTION_STAGING.md` — Execution tracking (input)
- `.claude/skills/execute.md` — Execution (upstream trigger)
- `.claude/skills/method_kaizen.md` — Improvement crystallization (downstream)
- `00-ORCHESTRATION/scripts/compact_wisdom.sh` — Log compaction

---

*Reviewtrospective Skill v1.0.0 | Syncrescendence*
