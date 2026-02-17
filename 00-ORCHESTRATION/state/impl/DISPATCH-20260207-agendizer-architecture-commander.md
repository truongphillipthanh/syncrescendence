# DISPATCH PACKAGE — Agendizer Architecture Review & Gate Enforcement

**DispatchPackageV2**

```yaml
id: DISPATCH-20260207-AGZ-ARCH-001
objective: "Maintain architectural oversight, enforce gates, and prepare Phase 1+ handoff envelopes as Adjudicator completes Phase 0"
context_bundle:
  evidence_refs:
    - 00-ORCHESTRATION/state/impl/EVIDENCE-LOCK-20260207-agendizer-clarescence2.md
    - 00-ORCHESTRATION/state/impl/CAPABILITY-MATRIX-20260207-twin-swarm-routing.md
  clarescence_ref: /Users/home/Desktop/Agendizer/CLARESCENCE-2026-02-06-agendizer-prd-reinforcement.md
  prd_delta_refs:
    - 00-ORCHESTRATION/state/impl/PRD-DELTAS-20260207-agendizer-hard-locks.md
  prior_receipts: []
capability_requirements:
  - long-context-synthesis
  - architecture-review
  - gate-enforcement
  - dispatch-packaging
gates:
  - id: ARCH-G1
    description: "Phase 0 artifacts pass Delta 1-5 compliance check"
    pass_criteria: "Every SwiftData model, every view, every test aligns with PRD deltas"
  - id: ARCH-G2
    description: "Phase 1 dispatch package ready before Phase 0 deadline"
    pass_criteria: "DISPATCH-*-agendizer-phase1-adjudicator.md published"
  - id: ARCH-G3
    description: "MCP/A2A port architecture design document published"
    pass_criteria: "Detailed MCP server spec + A2A Agent Card spec committed"
rollback_plan:
  action: "Reject Phase 0 artifacts and issue correction envelope to Adjudicator"
  notification: "SwarmHandoffEnvelope with objective: CORRECTION"
receipt_contract:
  required_fields:
    - proof_of_run
    - files_touched
    - gate_results
  deadline_utc: "2026-02-14T00:00:00Z"
```

---

## Commander Responsibilities (Ongoing)

### 1. Gate Enforcement
- Review every Adjudicator `ExecutionReceipt`
- Verify gate pass/fail claims against actual artifacts
- Reject non-compliant work with specific correction directives

### 2. Phase Pipeline Management
- Prepare dispatch packages for Phase 1-6 as Phase 0 nears completion
- Each phase dispatch references the previous phase's receipt as `prior_receipts`
- Maintain wave-gated sequencing: no Phase N+1 dispatch until Phase N gates pass

### 3. Architecture Design Documents
Prepare before Phase 5 (Dispatch):
- MCP Server specification (local Unix socket, JSON-RPC 2.0)
- MCP resource URI scheme (`agendizer://`)
- MCP tool definitions with authorization model
- A2A Agent Card structure per v0.3.0 spec
- Agent connection configuration UI wireframe

### 4. Integration Verification
- After each phase: verify the app builds, tests pass, and Liquid Glass rendering is correct
- After Phase 4 (Connect): verify Metal-accelerated graph rendering performance
- After Phase 5 (Dispatch): end-to-end test with actual MCP client connection

### 5. Doctrine Maintenance
- Keep evidence lock current if new information surfaces
- Update capability matrix if platform behavior changes
- Ensure PRD deltas are never softened or bypassed

---

## Phase Pipeline (Wave-Gated)

| Phase | Adjudicator Dispatch | Commander Gate | Target |
|---|---|---|---|
| 0: Foundation | DISPATCH-20260207-AGZ-P0-001 | Delta 5 compliance, build success | Week 1 |
| 1: Interpretation | (prepared after P0 gates) | Delta 4 compliance, local-first interpreter | Week 2 |
| 2: Navigation | (prepared after P1 gates) | Delta 2 compliance, depth stack (not tabs) | Week 3 |
| 3: Ledger | (prepared after P2 gates) | Delta 5 timeline, Delta 4 echo detection | Week 4 |
| 4: Connect | (prepared after P3 gates) | Delta 1 Metal rendering, Delta 4 on-device | Week 5 |
| 5: Dispatch | (prepared after P4 gates) | Delta 3 MCP/A2A ports, Delta 5 receipts | Week 6 |
| 6: Polish | (prepared after P5 gates) | Delta 1+2 full Liquid Glass + onboarding | Week 7-8 |

---

**Priority**: P0
**Lane**: Commander (Opus 4.6)
**Mode**: Continuous oversight
