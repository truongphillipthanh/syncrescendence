# Crashout Postmortem
**Generated**: 2026-01-17T05:05:00Z
**Purpose**: Mechanistic analysis of the "crashout" failure pattern and prevention architecture

---

## Definition

A **crashout** is a system failure mode where context discontinuity leads to:
1. High-effort retransmission burden on the Principal
2. Emotional overload from technical unintelligibility
3. Loss of accumulated progress in conversational surfaces

This is not a moral failure or "growing pains." It's a specific class of systems failure with identifiable causes and preventable mechanics.

---

## The Failure Chain (Mechanistic)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CRASHOUT FAILURE CHAIN                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  STAGE 1: IMPLICIT DATABASE FORMATION                                      │
│  ────────────────────────────────────────                                   │
│  A conversational surface becomes an implicit database.                     │
│  State exists "somewhere in chat" but is not externalized to repository.   │
│  The Principal and assistant share context that has no durable form.       │
│                                                                             │
│                              │                                              │
│                              ▼                                              │
│                                                                             │
│  STAGE 2: CONTEXT DISCONTINUITY                                            │
│  ────────────────────────────────                                           │
│  A discontinuity event occurs:                                              │
│  - Memory doesn't load correctly                                            │
│  - UI glitch loses conversation                                             │
│  - Thread becomes partially inaccessible                                    │
│  - Project context fails to transfer                                        │
│  - Session ends before externalization                                      │
│                                                                             │
│                              │                                              │
│                              ▼                                              │
│                                                                             │
│  STAGE 3: INVISIBLE ASSUMPTION RESPONSE                                    │
│  ────────────────────────────────────────                                   │
│  The assistant responds as if state is still shared.                        │
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
│  Must re-explain what the system is supposed to "know."                     │
│  Emotional labor of managing the absurdity of re-explaining.               │
│  Precision becomes costly because every detail requires re-specification.  │
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
│  Principal either abandons session in frustration,                          │
│  or pushes through with degraded outcomes,                                  │
│  or expresses (justified) frustration at the system.                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Root Cause Analysis

### Primary Root Cause

**Web apps as implicit databases are structurally fragile.**

Conversational interfaces store state in:
- Project memories (opaque, non-exportable)
- Conversation history (deletable, session-bound)
- Context windows (volatile, size-limited)

None of these are durable, inspectable, or transferable.

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
| Low frustration tolerance for administrative burden | Retransmission is experienced as punishment |

---

## Prevention Architecture

### Level 1: Forced Externalization

**Rule**: No session ends without artifacts in repository.

| Session Type | Required Artifact |
|--------------|-------------------|
| Oracle synthesis | Oracle context document |
| Execution | Execution log |
| Planning | Plan packet |
| Any valuable | Continuation packet |

**Enforcement**: Session lifecycle protocol requires culmination.

### Level 2: Continuation Packets

**Rule**: Any deletable conversation must have a deletable-safe handoff.

```json
{
  "id": "CONT-20260116-001",
  "state_snapshot": {...},
  "context_files": ["CLAUDE.md", "..."],
  "next_objectives": ["..."]
}
```

**Enforcement**: Store in `00-ORCHESTRATION/continuations/`

### Level 3: Repository as Ground Truth

**Rule**: Web apps are consultation surfaces, not authoritative.

| Surface | Authority Level |
|---------|-----------------|
| Repository | CONSTITUTIONAL |
| System state files | OPERATIONAL |
| Web app memory | CACHE (disposable) |
| Conversation history | EPHEMERAL |

**Enforcement**: When mismatch, trust repo.

### Level 4: Recovery Protocol

**Rule**: When crashout occurs, follow documented recovery.

1. STOP - do not compound
2. Ground in repository
3. Reconstruct minimal context
4. Resume with verification

**Enforcement**: Document exists, is practiced, is internalized.

### Level 5: Operator Translation Layer

**Rule**: Technical outputs must be Principal-intelligible.

| Anti-Pattern | Better Pattern |
|--------------|----------------|
| "Run this command" without context | "This command does X. If it fails, try Y." |
| Raw error messages | "Error means A. To fix: B." |
| Jargon without definition | Define or avoid jargon |

**Enforcement**: Review outputs for clarity before delivery.

---

## Which Protocols Would Have Prevented This?

Based on analysis of `previous_thread.md` and related context:

| Protocol | Would Have Prevented |
|----------|---------------------|
| **Continuation Packet** | Context loss across threads |
| **Session Lifecycle** | Incomplete culmination |
| **Forced Externalization** | Implicit database formation |
| **Repository Ground Truth** | Memory vs reality confusion |
| **Operator Translation** | Technical unintelligibility |

### Specific Missing Pieces

1. **No continuation packet schema** existed to formalize handoff
2. **No crashout recovery protocol** existed to guide recovery
3. **No session lifecycle** unified the start→operate→culminate→handoff flow
4. **No operator translation guidelines** for Principal-friendly output

---

## New Guardrails

Based on this analysis, implement these guardrails:

### Guardrail 1: No Completion Without Artifacts

```yaml
closure_gate:
  required:
    - execution_log_exists: true
    - state_vector_updated: true
    - events_logged: true
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

## Metrics

Track crashout frequency and severity:

| Metric | Target | Current Estimate |
|--------|--------|------------------|
| Sessions with crashout | <5% | Unknown (pre-measurement) |
| Crashouts requiring >30m recovery | 0 | Several recent |
| Sessions with proper culmination | >90% | ~50% |
| Continuation packets created | 1 per session | ~0.3 per session |

---

## Post-Incident Actions

When a crashout occurs:

1. **Log the event** to events.jsonl
```json
{"timestamp":"...","event":"crashout","actor":"principal","data":{"cause":"...","recovery_time":"..."}}
```

2. **Create kaizen item** for prevention
```csv
K-NNN,crashout,YYYY-MM-DD,"[Specific improvement]",high,pending,,
```

3. **Identify missing artifact** that would have helped
4. **Update protocols** if gap discovered
5. **Practice recovery** to reduce future recovery time

---

## Connection to 18 Lenses

The crashout pathology violates multiple lenses:

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

## Summary

**The antidote is not "pick the right model."**

**The antidote is: a session lifecycle that forces state externalization, plus continuation packets that make any single chat deletable without losing continuity.**

Web apps are improvisational and fragile unless subordinated to an external, inspectable spine. That's not ideology; it's systems engineering.
