# Guardrails v2
**Generated**: 2026-01-17T05:10:00Z
**Purpose**: Aligned with failure modes, enforcing crashout prevention and quality gates

---

## Overview

Guardrails are hard constraints that prevent known failure modes. They are NOT aspirational; they are gates that block progression until criteria are met.

---

## Category 1: Crashout Prevention Guardrails

### G-001: No Completion Without Artifacts

**Prevents**: Implicit database formation (Crashout Stage 1)

**Gate Condition**:
```yaml
on: session_completion_attempt
require:
  - execution_log_exists: true
  - OR: trivial_session (< 5 minutes, no state change)
block_if: artifacts_missing
message: "Cannot mark session complete without execution log"
```

**Implementation**:
- Session lifecycle protocol enforces
- Claude Code prompts for log at /compact or session end
- events.jsonl entry required

### G-002: Forced Externalization Before Delete

**Prevents**: Context loss from thread deletion (Crashout Stage 2)

**Gate Condition**:
```yaml
on: thread_delete_intent
require:
  - continuation_packet_exists: true
  - OR: all_value_externalized
block_if: valuable_context_not_externalized
message: "Create continuation packet before deleting this thread"
```

**Implementation**:
- Manual discipline (no enforcement mechanism in web apps)
- Checklist prompt before thread closure
- Continuation packet template readily accessible

### G-003: Verify Understanding Before Proceeding

**Prevents**: Invisible assumption response (Crashout Stage 3)

**Gate Condition**:
```yaml
on: session_cold_start
require:
  - state_summary_provided: true
  - user_confirmation: true
block_if: unverified_understanding
message: "Please confirm this matches your understanding before I proceed"
```

**Implementation**:
- Session lifecycle protocol includes verification step
- Assistant summarizes current state, awaits confirmation
- Proceed only on explicit "yes" or equivalent

### G-004: Translation Before Delivery

**Prevents**: Technical unintelligibility (Crashout Stage 4-5)

**Gate Condition**:
```yaml
on: technical_output_generation
require:
  - explanation_present: true
  - error_handling_present: true
  - jargon_defined_or_avoided: true
block_if: unintelligible_output
message: "Add explanation of what this does and how to verify"
```

**Implementation**:
- Output templates include explanation sections
- Review outputs for Principal-friendliness
- Use analogy when appropriate

---

## Category 2: Definition of Done Guardrails

### G-010: No Claim Without Verification

**Prevents**: Claims-based (vs commands-based) completion

**Gate Condition**:
```yaml
on: task_completion_claim
require:
  - verification_command_run: true
  - output_captured: true
  - output_proves_completion: true
block_if: unverified_claim
message: "Show me the verification command output"
```

**Implementation**:
- Execution logs include verification section
- make verify runs before commit
- Tasks.csv update only after verification

### G-011: No Execution Without Plan (Risk ≥ HIGH)

**Prevents**: Premature action on complex/risky tasks

**Gate Condition**:
```yaml
on: execution_start
if: risk_level >= HIGH
require:
  - plan_packet_exists: true
  - acceptance_criteria_defined: true
block_if: no_plan
message: "This task requires a plan packet before execution"
```

**Implementation**:
- Routing constraints identify high-risk tasks
- Plan packet template enforces acceptance criteria
- Escalation path for urgent exceptions

### G-012: No Canon Without Lenses

**Prevents**: Unvetted additions to protected zone

**Gate Condition**:
```yaml
on: canon_modification
require:
  - lenses_evaluation_complete: true
  - pass_count >= 12
  - principal_approval: true
block_if: unvetted_canon_change
message: "Canon changes require 18 Lenses evaluation (≥12 pass)"
```

**Implementation**:
- Canon modification protocol includes lenses check
- Lenses evaluation logged in execution log
- Principal approval before commit

---

## Category 3: State Integrity Guardrails

### G-020: Ledger Ground Truth

**Prevents**: State drift from reality

**Gate Condition**:
```yaml
on: completion_claim
require:
  - ledger_matches_filesystem: true
  - tasks.csv_accurate: true
  - sources.csv_accurate: true
block_if: ledger_mismatch
message: "Ledger does not match filesystem state"
```

**Implementation**:
- make verify includes ledger validation
- Atomic updates (temp → validate → rename)
- Regular audits via replay procedure

### G-021: Event Logging Required

**Prevents**: Unauditable system behavior

**Gate Condition**:
```yaml
on: significant_action
require:
  - event_logged: true
block_if: unlogged_action
message: "Significant actions must be logged to events.jsonl"
```

**Significant actions**:
- Session start/end
- Packet creation
- Execution completion
- State updates
- Errors/failures

### G-022: State Update Atomicity

**Prevents**: Partial/corrupted state updates

**Gate Condition**:
```yaml
on: state_update
require:
  - write_to_temp_file: true
  - validate_temp_file: true
  - atomic_rename: true
block_if: non_atomic_update
message: "State updates must use temp → validate → rename pattern"
```

---

## Category 4: Role Boundary Guardrails

### G-030: Planners Don't Execute

**Prevents**: Role bleed from planning to execution

**Gate Condition**:
```yaml
on: execution_command
if: current_role == "planner"
block_always: true
message: "Planners produce packets, not execute. Route to Executor."
```

**Implementation**:
- ChatGPT system prompt explicitly forbids execution
- Outputs are packets, not commands
- Escalation to Claude Code for execution

### G-031: Executors Don't Architect

**Prevents**: Scope creep during execution

**Gate Condition**:
```yaml
on: scope_change_attempt
if: current_role == "executor"
require:
  - scope_change_documented: true
  - principal_approval: true
block_if: unauthorized_scope_change
message: "Scope changes require escalation. Document and request approval."
```

**Implementation**:
- Claude Code stays within plan acceptance criteria
- Deviations logged and flagged
- Principal decides whether to approve

### G-032: Auditors Don't Modify

**Prevents**: Audit contamination

**Gate Condition**:
```yaml
on: modification_attempt
if: current_role == "auditor"
block_always: true
message: "Auditors verify, they don't modify. Create new execution for fixes."
```

**Implementation**:
- Claude-3 (Auditor) has read-only mindset
- Audit output is assessment, not action
- Fixes require separate execution pass

---

## Category 5: Protected Zone Guardrails

### G-040: Canon Deletions Forbidden Without Approval

**Prevents**: Accidental or unauthorized Canon loss

**Gate Condition**:
```yaml
on: delete_operation
if: path in "01-CANON/"
require:
  - principal_explicit_approval: true
  - documented_rationale: true
block_if: unauthorized_deletion
message: "Canon deletion requires explicit Principal approval with rationale"
```

### G-041: State Modifications Logged

**Prevents**: Stealth state changes

**Gate Condition**:
```yaml
on: modify_operation
if: path in "00-ORCHESTRATION/state/"
require:
  - event_logged: true
  - change_documented: true
block_if: unlogged_modification
message: "State modifications must be logged"
```

### G-042: Constitutional Changes Require Chorus

**Prevents**: Unvetted fundamental changes

**Gate Condition**:
```yaml
on: modify_operation
if: path in ["CLAUDE.md", "config/coordination.yaml", "REF-STANDARDS.md"]
require:
  - chorus_consultation: true
  - principal_approval: true
block_if: unvetted_constitutional_change
message: "Constitutional changes require chorus consultation and Principal approval"
```

---

## Guardrail Enforcement Summary

| Guardrail | Enforcement Level | Bypass Mechanism |
|-----------|-------------------|------------------|
| G-001 | Protocol (soft) | Principal override |
| G-002 | Manual discipline | Checklist reminder |
| G-003 | Protocol (soft) | Explicit skip |
| G-004 | Training/review | None |
| G-010 | make verify | None |
| G-011 | Routing constraints | Principal override |
| G-012 | Protocol (hard) | None |
| G-020 | Validation script | None |
| G-021 | Protocol (soft) | None |
| G-022 | Script enforcement | None |
| G-030 | System prompt | Platform switch |
| G-031 | Plan reference | Escalation |
| G-032 | System prompt | None |
| G-040 | Git hook (future) | Principal override |
| G-041 | Protocol (soft) | None |
| G-042 | Protocol (hard) | None |

---

## Integration with Failure Modes

| Failure Mode | Guardrails That Prevent |
|--------------|-------------------------|
| FM-001 Context not persisting | G-002, G-003 |
| FM-002 Memory opacity | G-020 |
| FM-003 Cross-platform loss | G-001, G-002 |
| FM-004 Outputs before objectives | G-011 |
| FM-005 Analysis paralysis | (time-boxing, not guardrail) |
| FM-008 Canon drift | G-012, G-020 |
| FM-009 Ledger mismatch | G-020, G-021 |
| FM-010 Credential exposure | (separate security policy) |
| FM-012 Planner executing | G-030 |
| FM-013 Executor planning | G-031 |
| FM-014 Verifier modifying | G-032 |

---

## Guardrail Violations Log

When a guardrail is bypassed or violated, log:

```json
{
  "timestamp": "...",
  "event": "guardrail_violation",
  "guardrail": "G-011",
  "description": "Execution without plan",
  "justification": "Emergency fix required",
  "approved_by": "principal",
  "follow_up": "Create plan retroactively"
}
```
