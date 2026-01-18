# CRASHOUT PREVENTION AND RECOVERY
## Mechanistic Analysis, Prevention Architecture, and Recovery Procedure
**Generated**: 2026-01-17
**Purpose**: Prevent context loss and provide recovery procedures

---

## I. WHAT A CRASHOUT IS

A **crashout** is a system failure mode where context discontinuity causes:
1. **High-effort retransmission burden** on the Principal
2. **Emotional overload** from technical unintelligibility
3. **Loss of accumulated progress** in conversational surfaces

This is not "growing pains" or "model limitations." It's a **specific, preventable failure class**.

---

## II. THE FAILURE CHAIN

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CRASHOUT FAILURE CHAIN                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  STAGE 1: IMPLICIT DATABASE FORMATION                                      │
│  ────────────────────────────────────                                       │
│  A conversational surface becomes an implicit database.                     │
│  State exists "somewhere in chat" but not externalized to repository.       │
│  Principal and assistant share context that has no durable form.            │
│                                                                             │
│                              │                                              │
│                              ▼                                              │
│                                                                             │
│  STAGE 2: CONTEXT DISCONTINUITY                                            │
│  ────────────────────────────                                               │
│  Something breaks:                                                          │
│  - Memory doesn't load correctly                                            │
│  - UI glitch loses conversation                                             │
│  - Thread becomes partially inaccessible                                    │
│  - Project context fails to transfer                                        │
│  - Session ends before externalization                                      │
│  - Model switches mid-thread                                                │
│                                                                             │
│                              │                                              │
│                              ▼                                              │
│                                                                             │
│  STAGE 3: INVISIBLE ASSUMPTION RESPONSE                                    │
│  ────────────────────────────────────────                                   │
│  Assistant responds as if state is still shared.                            │
│  Produces instructions that presuppose invisible context.                   │
│  "Continue from where we left off" when there's no shared memory.          │
│  Technical jargon without grounding in visible artifacts.                   │
│                                                                             │
│                              │                                              │
│                              ▼                                              │
│                                                                             │
│  STAGE 4: RETRANSMISSION BURDEN                                            │
│  ────────────────────────────────                                           │
│  Principal is forced into high-effort context reconstruction.               │
│  Must re-explain what the system "should know."                             │
│  Precision becomes costly because every detail requires re-specification.   │
│                                                                             │
│                              │                                              │
│                              ▼                                              │
│                                                                             │
│  STAGE 5: EMOTIONAL OVERLOAD                                               │
│  ────────────────────────────                                               │
│  Impatience spikes because cost of precision falls entirely on Principal.  │
│  Technical unintelligibility compounds frustration.                         │
│  System appears hostile rather than helpful.                                │
│  Fight-or-flight responses to what should be administrative tasks.         │
│                                                                             │
│                              │                                              │
│                              ▼                                              │
│                                                                             │
│  STAGE 6: SYSTEM ABANDONMENT OR ANGER                                      │
│  ─────────────────────────────────────                                      │
│  Principal either:                                                          │
│  - Abandons session in frustration                                          │
│  - Pushes through with degraded outcomes                                    │
│  - Expresses (justified) frustration at the system                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## III. ROOT CAUSES

### Primary Root Cause

**Web apps as implicit databases are structurally fragile.**

| Storage Type | Durability | Inspectability | Transferability |
|--------------|------------|----------------|-----------------|
| Project Memory | Opaque | No | No |
| Conversation | Deletable | Partial | No |
| Context Window | Volatile | No | No |
| Repository | **Durable** | **Yes** | **Yes** |

### Contributing Factors

| Factor | How It Contributes |
|--------|-------------------|
| Memory opacity | Cannot verify what system "knows" |
| Export friction | Hard to move artifacts out |
| Context limits | Compaction loses detail |
| Session isolation | Each thread is an island |
| Platform dependency | All state in vendor's hands |

### Cognitive Factors (Principal-Specific)

| Factor | How It Contributes |
|--------|-------------------|
| Coherence-gated cognition | Incoherence is actively painful |
| Executive function compensation | System IS the executive function; failure is personal |
| Verbal working memory strength | Can remember what was said but can't make system remember |
| Low frustration tolerance for admin burden | Retransmission feels like punishment |

---

## IV. PREVENTION ARCHITECTURE

### Level 1: Forced Externalization

**Rule**: No session ends without artifacts in repository.

| Session Type | Required Artifact |
|--------------|-------------------|
| Oracle synthesis | Oracle context document |
| Execution | Execution log or packet |
| Planning | Plan packet |
| Research | Evidence packet |
| Any valuable | Continuation packet |

**Mechanism**: Closure gate (see Cockpit Constitution, Section III).

### Level 2: Continuation Packets

**Rule**: Any deletable conversation must have a deletion-safe handoff.

```
Session Active
     │
     ▼
Work Happening
     │
     ▼
Session Ending?
     │
     ├─ YES ──▶ Create Continuation Packet
     │                   │
     │                   ▼
     │           Write to blackboard/continuations/
     │                   │
     │                   ▼
     │           Mark "Safe to Delete"
     │
     └─ NO ───▶ Continue Working
```

**Location**: `00-ORCHESTRATION/blackboard/continuations/`

### Level 3: Repository as Ground Truth

**Rule**: Web apps are consultation surfaces, not authoritative.

| Surface | Authority Level |
|---------|-----------------|
| Repository | CONSTITUTIONAL |
| System state files | OPERATIONAL |
| Web app memory | CACHE (disposable) |
| Conversation history | EPHEMERAL |

**Mechanism**: When mismatch detected, trust repo.

### Level 4: Operator Translation Layer

**Rule**: Technical outputs must be Principal-intelligible.

| Anti-Pattern | Better Pattern |
|--------------|----------------|
| "Run this command" without context | "This command does X. If it fails, try Y." |
| Raw error messages | "Error means A. To fix: B." |
| Jargon without definition | Define or avoid jargon |
| Unexplained file paths | "This file contains [description]" |

**Mechanism**: Review outputs for clarity before delivery.

### Level 5: State Verification at Session Start

**Rule**: Verify understanding before proceeding.

```markdown
## Session Start Protocol

1. Summarize current state from state vector
2. State: "My understanding is: [summary]"
3. Ask: "Does this match your understanding?"
4. Proceed only if confirmed
```

**Mechanism**: Verification gate in Cockpit Constitution.

---

## V. GUARDRAILS

### Guardrail 1: No Completion Without Artifacts

```yaml
closure_gate:
  required:
    - execution_log_exists: true
    - state_vector_updated: true
    - events_logged: true
    - continuation_packet_if_needed: true
  if_missing: block_closure
```

### Guardrail 2: No Suggestions Before Objectives Locked

```yaml
suggestion_gate:
  precondition: objectives_defined
  if_not: prompt_for_objectives_first
  rationale: "Suggestions without objectives cause drift"
```

### Guardrail 3: Always Culminate into Spine

```yaml
culmination_gate:
  at_session_end:
    - create_execution_log
    - update_state
    - create_continuation_packet
  exception: trivial_sessions (< 5 minutes, no artifacts)
```

### Guardrail 4: Verify Understanding Before Proceeding

```yaml
verification_gate:
  on_context_load:
    - state: summarize_current_state
    - verify: "Does this match your understanding?"
    - proceed_only_if: confirmed
```

### Guardrail 5: Translate Before Deliver

```yaml
translation_gate:
  on_technical_output:
    - include: what_this_does
    - include: if_this_fails
    - include: verification_command
    - avoid: unexplained_jargon
```

---

## VI. RECOVERY PROCEDURE

When a crashout occurs, follow this procedure:

### Step 1: STOP

**Do not compound the problem.**

- Don't try to "continue from where we left off"
- Don't assume shared context exists
- Don't get frustrated (justified but unhelpful)

### Step 2: GROUND IN REPOSITORY

```bash
cd ~/Desktop/syncrescendence
git pull origin main

# Check current state
cat 00-ORCHESTRATION/state/system_state.json | head -20

# Check recent events
tail -10 00-ORCHESTRATION/state/events.jsonl

# Check for continuation packets
ls -la 00-ORCHESTRATION/blackboard/continuations/
```

### Step 3: LOAD MOST RECENT CONTEXT

If continuation packet exists:
```bash
# Find most recent
ls -lt 00-ORCHESTRATION/blackboard/continuations/ | head -1

# Read it
cat 00-ORCHESTRATION/blackboard/continuations/CONT-YYYYMMDD-NNN.md
```

If no continuation packet:
- Check execution logs: `ls -lt 00-ORCHESTRATION/execution_logs/`
- Check Oracle contexts: `ls -lt 00-ORCHESTRATION/oracle_contexts/`

### Step 4: RECONSTRUCT MINIMAL CONTEXT

Create a minimal context statement:

```markdown
## Context Recovery

**Last Known State**:
- Oracle session: [N]
- Last committed work: [hash/date]
- Active intention: [from ARCH-INTENTION_COMPASS.md]

**What I Know**:
- [Fact 1 from repo]
- [Fact 2 from repo]

**What I Don't Know**:
- [What's unclear]

**Next Objective**:
- [What needs to happen]
```

### Step 5: RESUME WITH VERIFICATION

Start new session with:

```
I'm recovering from a context discontinuity. Here's what I've reconstructed:

[Paste context recovery block]

Please verify: does this match your understanding of current state?
```

### Step 6: LOG THE CRASHOUT

After recovery, log the event:

```bash
# Add to events.jsonl
echo '{"timestamp":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","event":"crashout","actor":"principal","data":{"cause":"[what caused it]","recovery_time":"[how long]","artifacts_lost":"[what was lost]"}}' >> 00-ORCHESTRATION/state/events.jsonl
```

### Step 7: CREATE KAIZEN ITEM

If prevention improvement is possible:

```markdown
## Kaizen: Crashout Prevention

**Incident**: [Date/time]
**Cause**: [Root cause]
**What Would Have Prevented**: [Missing artifact or process]
**Proposed Fix**: [Specific change]
```

---

## VII. DETECTION PATTERNS

### How to Know You're In a Crashout

| Signal | What It Means |
|--------|---------------|
| "Continue from where we left off" but context is wrong | Stage 3 |
| Needing to re-explain things the system "should know" | Stage 4 |
| Frustration spiking over administrative friction | Stage 5 |
| Considering abandoning the session | Stage 6 |

### Early Warning Signs

| Signal | What It Means |
|--------|---------------|
| Session going long without artifacts | Stage 1 forming |
| "I'll save this for later" | Stage 1 danger |
| Memory feels unreliable | Stage 2 imminent |
| Context window filling up | Stage 2 imminent |

---

## VIII. CRASHOUT SEVERITY LEVELS

| Level | Description | Recovery Time | Prevention |
|-------|-------------|---------------|------------|
| **Minor** | Single fact lost | < 5 min | Continuation packet |
| **Moderate** | Session context lost | 15-30 min | Execution log |
| **Major** | Multi-session context lost | 1-2 hours | Oracle context |
| **Catastrophic** | System understanding lost | 4+ hours | Full re-onboarding |

---

## IX. PROTOCOLS THAT WOULD HAVE PREVENTED PAST CRASHOUTS

Based on analysis of previous incidents:

| Protocol | Would Have Prevented |
|----------|---------------------|
| **Continuation Packet** | Context loss across threads |
| **Session Lifecycle** | Incomplete culmination |
| **Forced Externalization** | Implicit database formation |
| **Repository Ground Truth** | Memory vs reality confusion |
| **Operator Translation** | Technical unintelligibility |

---

## X. CONNECTION TO 18 LENSES

The crashout pathology violates multiple evaluative lenses:

| Lens | Violation |
|------|-----------|
| #6 Personal Idiosyncrasies | Ignores AuDHD cognitive load |
| #7 Potency Without Resolution Loss | Context loss IS resolution loss |
| #8 Elegance + Developer Happiness | Frustration antithesis of happiness |
| #12 Industrial Engineering | Retransmission is waste |
| #17 Lean | Context loss is pure waste |
| #18 Six Sigma | Crashouts are defects |

Prevention architecture serves these lenses directly.

---

## XI. SUMMARY

**The antidote is not "pick the right model."**

**The antidote is:**
1. A session lifecycle that forces state externalization
2. Continuation packets that make any chat deletable
3. Repository as ground truth, not web apps
4. Recovery procedure that's documented and practiced

**Web apps are improvisational and fragile unless subordinated to an external, inspectable spine.**

This is not ideology. It's systems engineering.

---

## XII. QUICK REFERENCE

### Prevention Checklist (Every Session)
- [ ] Objective locked before work
- [ ] Artifacts created during work
- [ ] State updated at end
- [ ] Continuation packet written
- [ ] "Safe to delete" confirmed

### Recovery Checklist (When Crashout Occurs)
1. [ ] STOP — don't compound
2. [ ] GROUND — check repo state
3. [ ] LOAD — find most recent context
4. [ ] RECONSTRUCT — create minimal context
5. [ ] RESUME — verify understanding
6. [ ] LOG — record the crashout
7. [ ] KAIZEN — improve prevention

---

**Crashouts are preventable. Prevent them.**
