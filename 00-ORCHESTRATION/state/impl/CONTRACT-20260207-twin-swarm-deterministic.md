# TWIN-SWARM DETERMINISTIC CONTRACT

**Published**: 2026-02-07
**Authority**: Commander (Opus 4.6) + Adjudicator (Codex GPT-5.3)
**Source**: RESULT-adjudicator-20260207-agendizer-clarescence2-substantiated.md §4
**Status**: ACTIVE — All inter-lane communication must use these schemas

---

## 1. Protocol Version Posture

| Protocol | Floor | Current | Target |
|---|---|---|---|
| MCP | `2025-06-18` | `2025-11-25` | Current upstream validated |
| A2A | `v0.2.6` (`/.well-known/agent.json`) | `v0.3.0` (`/.well-known/agent-card.json`) | v0.3.0 with v0.2.x compat |

**Dual-version posture**: Pin to current for production, accept floor for backward compatibility. Reject anything below floor.

---

## 2. Schema Definitions

### 2.1 DispatchPackageV2

The unit of work dispatched from Commander to any execution lane.

```yaml
DispatchPackageV2:
  id: string                    # ULID, unique across all dispatches
  objective: string             # Human-readable goal statement
  context_bundle:               # All context needed for execution
    evidence_refs: string[]     # Paths to locked evidence documents
    clarescence_ref: string     # Path to source clarescence
    prd_delta_refs: string[]    # Applicable delta locks
    prior_receipts: string[]    # Receipts from prerequisite work
  capability_requirements:      # What the executing agent needs
    - string                    # e.g. "swift-compilation", "swiftui-rendering", "metal-compute"
  gates: Gate[]                 # Hard acceptance criteria
  rollback_plan: RollbackPlan   # What to do if execution fails
  receipt_contract:             # Expected receipt format
    required_fields: string[]
    deadline_utc: string        # ISO 8601
```

### 2.2 SwarmHandoffEnvelope

The protocol for inter-lane communication. This is the ONLY permitted communication format between Commander and Adjudicator lanes.

```yaml
SwarmHandoffEnvelope:
  id: string                    # ULID
  from_lane: string             # "commander" | "adjudicator"
  to_lane: string               # "commander" | "adjudicator"
  objective: string             # What the receiving lane must accomplish
  context_bundle:               # Serialized context
    files: string[]             # Paths to relevant files
    state_snapshot: object      # Current state of the work
    constraints: string[]       # Non-negotiable boundaries
  artifact_inputs: string[]     # Input artifacts (committed files)
  artifact_outputs_expected: string[]  # What the receiver should produce
  validation_suite:             # How to verify completion
    - test_name: string
      test_type: string         # "unit" | "integration" | "gate" | "manual"
      pass_criteria: string
  expected_receipt: ExecutionReceiptSpec
  deadline_utc: string          # ISO 8601
  priority: string              # "P0" | "P1" | "P2" | "P3"
```

### 2.3 ExecutionReceipt

Produced by every state-changing action. No completion claim is valid without one.

```yaml
ExecutionReceipt:
  id: string                    # ULID
  dispatch_id: string           # References the DispatchPackageV2 that spawned this
  agent: string                 # "commander-opus-4.6" | "adjudicator-codex-gpt-5.3" | etc.
  model_surface_used: string    # "claude-code" | "codex-app" | "codex-cli" | etc.
  proof_of_run: string          # Commit hash, test output, or artifact path
  files_touched: string[]       # All files created/modified
  bench_or_test_outcome: string # "PASS" | "FAIL" | "PARTIAL" with details
  gate_results:                 # Per-gate pass/fail
    - gate_id: string
      result: string            # "PASS" | "FAIL"
      evidence: string
  timestamp_utc: string         # ISO 8601
  duration_seconds: number      # Wall-clock execution time
  rollback_executed: boolean    # Whether rollback was triggered
  notes: string                 # Free-form execution notes
```

---

## 3. Ownership Boundaries

### Commander Lane (Opus 4.6 / Claude Code)
- Long-context synthesis and architecture judgments
- Final doctrine and gate decisions
- Evidence lock maintenance
- PRD delta enforcement
- Integration verification across lanes

### Adjudicator Lane (Codex GPT-5.3 / Codex CLI)
- Parallel implementation decomposition
- Execution packaging and file-by-file build plans
- Deterministic artifact production (code, tests, configs)
- Implementation clarescence authoring

### Boundary Rules
1. **No free-form lane bleed**: All inter-lane communication via `SwarmHandoffEnvelope`
2. **Single source of truth**: Evidence locks and delta locks live in Commander lane (this repo)
3. **Implementation artifacts**: Produced by Adjudicator, reviewed by Commander before merge
4. **Gate decisions**: Commander has final authority; Adjudicator can flag but not override
5. **Receipt requirement**: Every envelope produces a receipt; no exceptions

---

## 4. Gate Enforcement Protocol

| Gate | Check | Enforcer | Timing |
|---|---|---|---|
| Gate A | Every claim has primary-source citation | Commander | Before any execution wave |
| Gate B | Capability matrix has no contradictions | Commander | Before lane assignment |
| Gate C | PRD deltas encoded in implementation | Commander | After each phase completion |
| Gate D | Ownership boundaries, handoff schema, rollback fully specified | Commander | Before twin-swarm launch |
| Gate E | Every state-changing action has ExecutionReceipt | Both | Continuous |

---

## 5. Rollback Protocol

For each execution wave, rollback means:
1. `git revert` the wave's commits
2. Notify the other lane via `SwarmHandoffEnvelope` with `objective: "ROLLBACK"`
3. Produce a rollback `ExecutionReceipt` documenting what was reverted and why
4. Return to the last known-good state (previous wave's final receipt)

---

**Gate D: PASS** — Twin-Swarm ownership boundaries, handoff schema, quality gates, and rollback are fully specified.
