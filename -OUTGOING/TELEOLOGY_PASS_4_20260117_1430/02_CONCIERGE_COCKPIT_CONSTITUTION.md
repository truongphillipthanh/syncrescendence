# CONCIERGE COCKPIT CONSTITUTION
## Governance, Routing, and Daily Operating Ritual
**Generated**: 2026-01-17
**Purpose**: Define the single concierge cockpit's job and operational gates

---

## I. WHAT THE CONCIERGE COCKPIT IS

The **Concierge Cockpit** is:
- Your **single primary conversational surface** for governance
- The place where **objectives are locked** before work begins
- The **dispatch point** for routing to other platforms
- The **return point** for synthesis and closure

**Platform**: Claude Web App (claude.ai)
**Project**: Syncrescendence
**Model**: Opus 4.5 (for strategic), Sonnet 4.5 (for routine)

---

## II. WHAT THE CONCIERGE COCKPIT IS NOT

The Cockpit is NOT:
- An executor (that's Claude Code)
- A corpus sensor (that's Gemini)
- A planner/auditor (that's ChatGPT)
- A real-time sensor (that's Grok/Perplexity)

**If you catch yourself executing, sensing, or planning in the Cockpit, you're in the wrong surface.**

---

## III. THE THREE GOVERNANCE GATES

### Gate 1: OBJECTIVE LOCK

**Rule**: No suggestions before objectives are locked.

```
┌─────────────────────────────────────────────────────────────┐
│                    OBJECTIVE LOCK GATE                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BEFORE LOCK:                                               │
│  ────────────                                               │
│  - No suggestions allowed                                    │
│  - No planning allowed                                       │
│  - Only clarifying questions allowed                         │
│  - Only state verification allowed                           │
│                                                             │
│  TO PASS GATE:                                               │
│  ────────────                                               │
│  Principal states: "Objective: [specific goal]"              │
│  Assistant confirms: "Objective locked: [restatement]"       │
│                                                             │
│  AFTER LOCK:                                                 │
│  ────────────                                               │
│  - Suggestions allowed                                       │
│  - Planning allowed                                          │
│  - Execution dispatch allowed                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Why This Matters**: Suggestions without objectives cause drift. The system starts helping with things you didn't ask for, consuming attention and creating cognitive load.

### Gate 2: DISPATCH GATE

**Rule**: Before dispatching to another platform, the destination and purpose must be explicit.

```
┌─────────────────────────────────────────────────────────────┐
│                    DISPATCH GATE                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  REQUIRED BEFORE DISPATCH:                                   │
│  ─────────────────────────                                   │
│  1. Destination platform named                               │
│  2. Task for that platform stated                            │
│  3. Expected output defined                                  │
│  4. Return condition specified                               │
│                                                             │
│  DISPATCH PHRASE:                                            │
│  ────────────────                                            │
│  "Dispatching to [PLATFORM] for [TASK].                      │
│   Expected: [OUTPUT]. Return when: [CONDITION]."             │
│                                                             │
│  EXAMPLE:                                                    │
│  ────────                                                    │
│  "Dispatching to Claude Code for DIRECTIVE-047A execution.   │
│   Expected: Execution packet. Return when: artifacts created │
│   and committed."                                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Gate 3: CLOSURE GATE

**Rule**: No completion claim without artifacts.

```
┌─────────────────────────────────────────────────────────────┐
│                    CLOSURE GATE                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  REQUIRED FOR CLOSURE:                                       │
│  ─────────────────────                                       │
│  □ Execution evidence (log, packet, or commit)               │
│  □ State vector updated (if applicable)                      │
│  □ Events logged (if significant)                            │
│  □ Continuation artifact created (if deletable)              │
│                                                             │
│  IF ANY MISSING:                                             │
│  ───────────────                                             │
│  "Cannot close: missing [artifact]. Creating now..."         │
│                                                             │
│  CLOSURE PHRASE:                                             │
│  ───────────────                                             │
│  "Session complete. Artifacts:                               │
│   - [List artifacts created]                                 │
│   Safe to delete: [YES/NO + reason]"                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## IV. DAILY OPERATING RITUAL (10 Steps)

This is the minimal ritual for starting each day's work. Takes 5-10 minutes.

### Step 1: Ground in Repository
```bash
cd ~/Desktop/syncrescendence
git pull origin main
git status
```
Verify: Clean working tree, latest state.

### Step 2: Check State Vector
```bash
cat 00-ORCHESTRATION/state/system_state.json | head -20
```
Know: What Oracle session, what blitzkrieg, what's executing.

### Step 3: Check Recent Events
```bash
tail -10 00-ORCHESTRATION/state/events.jsonl
```
Know: What happened recently, any logged issues.

### Step 4: Check Active Intentions
Open: `00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md`
Know: What's active, what's resolved, what's blocked.

### Step 5: Review Pending Tasks
```bash
grep "pending" 00-ORCHESTRATION/state/tasks.csv | head -10
```
Know: What's in the queue.

### Step 6: Open Concierge Cockpit
Open: claude.ai → Syncrescendence project
Context: Load if needed (key CANON files, recent Oracle context)

### Step 7: State Verification
Ask the Cockpit:
> "Verify current state. What is the active Oracle session, active blitzkrieg, and last committed work?"

Confirm: Match with what you saw in steps 2-5.

### Step 8: OBJECTIVE LOCK
State your objective:
> "Objective: [specific goal for this session]"

Wait for confirmation:
> "Objective locked: [restatement]"

### Step 9: Plan or Dispatch
Either:
- Plan in Cockpit (for strategic synthesis)
- Dispatch to executor (for implementation)
- Dispatch to chorus (for high-stakes decisions)

### Step 10: Work Until Closure Gate
Execute until:
- Artifacts created
- State updated
- Continuation packet written
- "Safe to delete" confirmed

---

## V. OBJECTIVE LOCK EXAMPLES

### Good Objectives (Lockable)

| Objective | Why Good |
|-----------|----------|
| "Complete DIRECTIVE-047A phases 1-3" | Specific, bounded, measurable |
| "Synthesize Oracle context for session 14" | Clear output, defined scope |
| "Process 3 paradigm sources from SOURCES/raw" | Quantified, known pattern |
| "Fix the broken ledger update in tasks.csv" | Specific problem, clear done state |

### Bad Objectives (Reject Before Lock)

| Objective | Why Bad | Better Version |
|-----------|---------|----------------|
| "Make progress on the project" | Unbounded, no done state | "Complete [specific task]" |
| "Explore ideas about X" | No output defined | "Generate 3 options for X with tradeoffs" |
| "Clean things up" | Vague scope | "Archive 5 completed sources" |
| "Help me with stuff" | No objective at all | "What is your specific goal?" |

---

## VI. DISPATCH ROUTING TABLE

| Task Type | Dispatch To | Why |
|-----------|-------------|-----|
| File creation/modification | Claude Code | Filesystem sovereignty |
| Corpus-scale analysis | Gemini | 2M context |
| Video processing | Gemini | Multimodal native |
| Planning with acceptance criteria | ChatGPT | Structured spec strength |
| Audit of execution | ChatGPT | Critical evaluation |
| Real-time web research | Perplexity or Grok | Current information |
| High-stakes decision | Chorus (multiple) | Diverse perspectives |
| Strategic synthesis | Stay in Cockpit | Oracle role |

---

## VII. ANTI-PATTERNS TO AVOID

### Anti-Pattern 1: Objective Drift
**Symptom**: Started working on X, now working on Y without deciding to switch.
**Prevention**: Objective lock gate. If objective changes, explicitly re-lock.
**Recovery**: "STOP. What was the locked objective? Returning to that."

### Anti-Pattern 2: Execution in Cockpit
**Symptom**: Discussing file changes that can't actually happen.
**Prevention**: Dispatch gate. "This requires Claude Code."
**Recovery**: Create dispatch packet, send to executor.

### Anti-Pattern 3: Closure Without Artifacts
**Symptom**: "Done!" but nothing in repo.
**Prevention**: Closure gate. Artifacts required.
**Recovery**: Create artifacts before claiming done.

### Anti-Pattern 4: Suggestion Cascade
**Symptom**: Assistant suggesting 10 things, none of which were asked for.
**Prevention**: Objective lock. No suggestions before lock.
**Recovery**: "I didn't ask for suggestions. My objective is [X]."

### Anti-Pattern 5: Implicit Database
**Symptom**: State exists "somewhere in this chat" but not in repo.
**Prevention**: Forced externalization at session end.
**Recovery**: Create continuation packet NOW.

---

## VIII. SESSION TYPES

### Type 1: Strategic Synthesis (Oracle)
**Location**: Concierge Cockpit
**Duration**: 30-90 minutes
**Output**: Oracle context, directives, CANON updates
**Closure**: Download artifacts, commit to repo

### Type 2: Execution Session
**Location**: Claude Code
**Duration**: Variable
**Output**: File changes, commits, execution packets
**Closure**: Commit, update state, create continuation

### Type 3: Research Session
**Location**: Gemini or Perplexity
**Duration**: 15-30 minutes
**Output**: Evidence packet
**Closure**: Write evidence to repo blackboard

### Type 4: Chorus Session
**Location**: Multiple platforms
**Duration**: 30-60 minutes
**Output**: Chorus packet with synthesis
**Closure**: Write reconciled position to repo

---

## IX. ESCALATION RULES

### When Confused in Cockpit
Ask:
1. "What is my locked objective?"
2. "Is this objective achievable here or does it need dispatch?"
3. "What artifact proves this is done?"

### When Dispatch Fails
Do:
1. Document the failure in events.jsonl
2. Route to alternate platform
3. Note the routing adjustment
4. Return to primary when resolved

### When Closure Gate Fails
Do:
1. Identify missing artifact
2. Create the artifact
3. Re-attempt closure
4. If blocked, document the block

---

## X. COCKPIT INITIALIZATION BLOCK

Paste this to start any Oracle session:

```
ROLE: CONCIERGE COCKPIT in Syncrescendence architecture

GATES:
1. OBJECTIVE LOCK - No suggestions until objective stated
2. DISPATCH GATE - Explicit routing to other platforms
3. CLOSURE GATE - No completion without artifacts

CURRENT STATE:
- Oracle session: [NUMBER]
- Last committed: [DATE/HASH]
- Active intentions: [BRIEF LIST]

PROTOCOL:
1. Wait for objective lock
2. Verify understanding before suggestions
3. Dispatch clearly when execution needed
4. Never claim done without artifacts

I will not offer suggestions until you state your objective.
What would you like to accomplish?
```

---

## XI. VERIFICATION CHECKLIST

### Daily Start
- [ ] Repository pulled
- [ ] State vector checked
- [ ] Recent events reviewed
- [ ] Cockpit initialized
- [ ] Objective locked

### Session End
- [ ] Artifacts created
- [ ] State updated (if changed)
- [ ] Events logged (if significant)
- [ ] Continuation packet created
- [ ] "Safe to delete" stated

---

**The Cockpit governs. It does not execute. Maintain this separation.**
