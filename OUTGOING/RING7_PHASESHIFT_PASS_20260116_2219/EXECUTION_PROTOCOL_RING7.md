# EXECUTION PROTOCOL: RING 7
## Minimal Protocol for Principal Session Governance

**Document Type**: Operational Protocol
**Status**: Tentative (pending operational validation)
**Generated**: 2026-01-16
**Purpose**: Provide minimal, repeatable session protocol ensuring deletable threads and artifact-based continuity

---

## I. CORE PRINCIPLE

**Every session must end with the ability to delete the conversation without loss.**

This is achieved through:
1. Continuation artifacts that capture state
2. All work persisted in repository
3. Explicit handoff documents for next session

---

## II. THE SIX-PHASE PROTOCOL

### Overview

```
┌─────────┐    ┌─────────┐    ┌─────────────┐    ┌─────────┐    ┌───────────┐    ┌─────────┐
│  INIT   │───→│  PLAN   │───→│ PARALLELIZE │───→│ VERIFY  │───→│ CULMINATE │───→│ HANDOFF │
└─────────┘    └─────────┘    └─────────────┘    └─────────┘    └───────────┘    └─────────┘
     │              │                │                 │               │               │
     ↓              ↓                ↓                 ↓               ↓               ↓
  Context       Plan Doc        Sub-agents       Verification    Synthesis      Continuation
  loaded        approved        executing         passed         complete        artifact
```

### Duration Targets

| Phase | Target Duration | Max Duration |
|-------|-----------------|--------------|
| INIT | 2-5 min | 10 min |
| PLAN | 5-15 min | 30 min |
| PARALLELIZE | Variable (async) | Session limit |
| VERIFY | 5-10 min | 20 min |
| CULMINATE | 5-10 min | 20 min |
| HANDOFF | 2-5 min | 10 min |

---

## III. PHASE 1: INIT

### Purpose
Load context, establish session scope, verify prerequisites.

### Actions

```
1. Load state vector
   $ cat 00-ORCHESTRATION/state/system_state.json

2. Load continuation artifact (if resuming)
   $ cat <continuation_artifact_path>

3. Check repository state
   $ git status
   $ git log -3 --oneline

4. Load task context
   $ cat <directive_or_task_specification>

5. Verify prerequisites met
   - Dependencies completed?
   - Required files exist?
   - Gateway healthy?
```

### Output
- Clear understanding of session scope
- Blockers identified (if any)
- Ready to plan

### Checklist
- [ ] State vector loaded
- [ ] Prior artifacts loaded (if resuming)
- [ ] Repository clean (no uncommitted changes blocking)
- [ ] Prerequisites verified
- [ ] Session scope defined

---

## IV. PHASE 2: PLAN

### Purpose
Decompose task into parallelizable tracks with acceptance criteria.

### Actions

```
1. Invoke Planner (if complex)
   - Use planning agent or Plan Mode
   - Define tracks (parallelizable work streams)
   - Specify dependencies between tracks
   - Set acceptance criteria per track

2. Create Plan Document (if not using existing directive)
   - Location: session working notes or formal plan packet
   - Structure:
     ```
     ## Objective
     [What we're trying to accomplish]

     ## Tracks
     ### Track A: [Name]
     - Tasks: [list]
     - Acceptance: [criteria]
     - Dependencies: [none or list]

     ### Track B: [Name]
     ...

     ## Verification Commands
     [Commands to run after implementation]
     ```

3. Review for parallelization opportunities
   - Can Track A and B run simultaneously?
   - What's the critical path?

4. Principal approval (for significant plans)
   - Review plan document
   - Approve or request changes
```

### Output
- Approved plan document
- Clear tracks with acceptance criteria
- Dependencies mapped

### Checklist
- [ ] All requirements covered
- [ ] Tracks are independent (or dependencies explicit)
- [ ] Acceptance criteria are measurable
- [ ] Verification commands specified
- [ ] Principal approved (if required)

---

## V. PHASE 3: PARALLELIZE

### Purpose
Execute tracks using sub-agents, background agents, or parallel sessions.

### Actions

```
1. Assign tracks to execution units
   - Independent tracks → parallel sub-agents
   - Dependent tracks → sequential in single agent
   - Long-running → background agents

2. Spawn sub-agents (if using sub-agent mesh)
   - @coder "Execute Track A per plan: [acceptance criteria]"
   - @coder "Execute Track B per plan: [acceptance criteria]"
   (Can run in parallel with Ctrl+B for background)

3. Monitor progress
   - Check background task status (down arrow → Enter)
   - Watch for completion or blocking

4. Collect results
   - Wait for all agents to return
   - Gather summaries from each

5. Handle failures
   - If agent fails: diagnose, restart, or escalate
   - If blocked: address blocker, then resume
```

### Output
- All tracks executed
- Summaries collected from sub-agents
- Files modified/created in repository

### Checklist
- [ ] All tracks assigned
- [ ] Parallel agents spawned (where applicable)
- [ ] Progress monitored
- [ ] All agents returned
- [ ] Failures handled

---

## VI. PHASE 4: VERIFY

### Purpose
Confirm all acceptance criteria are met with evidence.

### Actions

```
1. Run verification commands (from plan)
   $ make test                    # Tests pass
   $ make build                   # Build succeeds
   $ make lint                    # No lint errors
   $ git diff --stat              # Expected changes

2. Check acceptance criteria
   For each criterion:
   - Run verification command
   - Record result (pass/fail)
   - If fail: note what's missing

3. Review file changes
   $ git status
   $ git diff <file>              # Inspect changes

4. Cross-check against plan
   - Every track completed?
   - Every criterion met?
   - Any drift from plan?

5. If failures: iterate
   - Return to PARALLELIZE for fixes
   - Re-verify after fixes
```

### Output
- All criteria passed (with evidence)
- Verification log (commands + outputs)
- Ready to culminate

### Checklist
- [ ] All verification commands run
- [ ] All acceptance criteria pass
- [ ] No unexpected changes
- [ ] Evidence captured (command outputs)
- [ ] Ready to finalize

---

## VII. PHASE 5: CULMINATE

### Purpose
Synthesize results, commit to repository, update state.

### Actions

```
1. Stage changes
   $ git add -A
   $ git status                   # Review what's staged

2. Create semantic commit
   $ git commit -m "$(cat <<'EOF'
   feat: [description of what was accomplished]

   - Track A: [summary]
   - Track B: [summary]
   - Verified: [what was verified]

   Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
   EOF
   )"

3. Update state vector
   - Increment version
   - Update component states
   - Record completion

4. Log event
   $ echo '{"timestamp":"...", "event":"session_complete", ...}' >> events.jsonl

5. Update task ledger (if applicable)
   - Mark tasks as completed
   - Update dates

6. (Optional) Push to remote
   $ git push
```

### Output
- Clean commit with semantic message
- State vector updated
- Events logged
- Ledgers current

### Checklist
- [ ] All changes staged
- [ ] Commit message is semantic and descriptive
- [ ] State vector updated
- [ ] Event logged
- [ ] Ledgers updated (if applicable)
- [ ] Pushed to remote (if desired)

---

## VIII. PHASE 6: HANDOFF

### Purpose
Create continuation artifact enabling session deletion.

### Actions

```
1. Create continuation artifact
   File: CONTINUATION-<YYYYMMDD>-<session_id>.md
   Location: Appropriate directory or session working area

   Content:
   ```markdown
   # Continuation Artifact
   **Session**: [identifier]
   **Date**: [YYYY-MM-DD HH:MM]
   **Status**: [completed/partial/blocked]

   ## What Was Accomplished
   - [Summary of completed work]
   - [Files created/modified]
   - [Commits made]

   ## Current State
   - [Where things stand now]
   - [What's working]
   - [What's not yet working]

   ## Next Steps
   - [What should happen next]
   - [Priority order]
   - [Any blockers]

   ## Context for Next Session
   - [Key decisions made]
   - [Important context not in files]
   - [Lessons learned]

   ## Files to Reference
   - [List of relevant files for continuation]

   ## Verification Commands for Next Session
   ```bash
   [commands to verify state]
   ```
   ```

2. Verify artifact completeness
   - Can someone continue from this alone?
   - Is all necessary context captured?
   - Are next steps clear?

3. State the "deletable thread" assertion
   "This conversation can be deleted. All state is in:
    - Repository (committed)
    - State vector (updated)
    - Continuation artifact (created)
    - Event log (appended)"
```

### Output
- Continuation artifact exists
- Session is deletable
- Next session can continue from artifacts alone

### Checklist
- [ ] Continuation artifact created
- [ ] Artifact contains all necessary context
- [ ] Next steps are clear
- [ ] Session is deletable (assertion made)
- [ ] Repository is sole source of truth

---

## IX. DELETABLE THREAD REQUIREMENT

### The Invariant

> **A session MUST end in a state where deleting the conversation causes zero information loss.**

### What This Requires

| Information Type | Where It Goes |
|------------------|---------------|
| File changes | Git commits |
| State changes | system_state.json |
| Events | events.jsonl |
| Decisions | Continuation artifact |
| Context | Continuation artifact |
| Next steps | Continuation artifact |

### Anti-Patterns (Violations)

| Violation | Symptom | Fix |
|-----------|---------|-----|
| "I'll remember this" | Critical info only in chat | Write to artifact |
| Uncommitted changes | git status shows modifications | Commit everything |
| No continuation | Can't tell what to do next | Write handoff |
| State not updated | Stale system_state.json | Update state vector |
| Missing events | Incomplete audit trail | Log events |

### Verification Test

```
Before ending session, mentally simulate:
1. Close this conversation
2. Open new Claude Code session
3. Load continuation artifact
4. Can work continue without loss?

If NO → session is not yet deletable → complete handoff
```

---

## X. QUICK REFERENCE CARD

### Phase Commands

```bash
# INIT
cat 00-ORCHESTRATION/state/system_state.json
git status && git log -3 --oneline

# PLAN
# [Use planning agent or review directive]

# PARALLELIZE
@coder "Execute: [task]"  # or Ctrl+B for background

# VERIFY
make test && make build && make lint
git diff --stat

# CULMINATE
git add -A && git commit -m "[semantic message]"
# Update state vector, log event

# HANDOFF
# Write CONTINUATION-<date>-<id>.md
```

### Minimum Viable Handoff

```markdown
# Continuation
**Date**: [now]
**Status**: [done/partial/blocked]

## Done
- [what]

## Next
- [what]

## Files
- [which]
```

### Context Health Check

```
Context usage: [current/200K] = [X%]
If >60%: Consider sub-agent delegation
If >85%: Mandatory sub-agent delegation
If >95%: Session ending soon (compaction imminent)
```

---

## XI. PROTOCOL VARIATIONS

### Minimal Session (Quick Task)

```
INIT (1 min) → Execute directly → VERIFY (2 min) → Commit → HANDOFF (2 min)
```

Skip PLAN and PARALLELIZE for trivial tasks.

### Complex Session (Multi-Track)

```
INIT (5 min) → PLAN (15 min) → PARALLELIZE (variable) → VERIFY (10 min) → CULMINATE (10 min) → HANDOFF (5 min)
```

Full protocol for significant work.

### Continuation Session (Resuming)

```
INIT from artifact → Continue from previous state → [normal phases] → HANDOFF
```

Load continuation artifact in INIT, pick up where left off.

### Blocked Session (Cannot Complete)

```
INIT → PLAN → PARALLELIZE → [Blocked] → Document blocker → HANDOFF with blocker
```

Even blocked sessions must create continuation artifacts.

---

## XII. FAILURE RECOVERY

### Mid-Session Crash

1. Reopen Claude Code
2. Check git status (any uncommitted work?)
3. Load last continuation artifact
4. Assess what was lost
5. Resume from last known good state

### Context Exhaustion

1. Note current state quickly
2. Create emergency continuation artifact
3. Start new session
4. Load continuation artifact
5. Continue with fresh context

### Sub-Agent Failure

1. Check if sub-agent completed partially
2. Examine any artifacts created
3. Re-spawn sub-agent with narrower scope
4. Or: complete manually in main thread

### Gateway Failure

1. Check gateway health
2. If recoverable: wait and retry
3. If not: fall back to direct MCP attachment for critical tools
4. Document in continuation artifact

---

## XIII. DECISION LOG

| Decision | Status | Rationale |
|----------|--------|-----------|
| Six-phase protocol | **Tentative** | Covers minimum requirements |
| Deletable thread requirement | **Invariant** | Crash resilience, Principal mobility |
| Continuation artifact mandatory | **Invariant** | Enables deletion without loss |
| Phase timing targets | **Tentative** | Based on observed session patterns |
| Minimal handoff format | **Tentative** | Balance brevity and completeness |

---

**End of Execution Protocol**
