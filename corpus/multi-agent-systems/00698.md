# DISPATCH PACKAGE — Agendizer Phase 0: Foundation

**DispatchPackageV2**

```yaml
id: DISPATCH-20260207-AGZ-P0-001
objective: "Scaffold Agendizer Xcode project and implement SwiftData model with full Intention Object data architecture"
context_bundle:
  evidence_refs:
    - orchestration/state/impl/EVIDENCE-LOCK-20260207-agendizer-clarescence2.md
  clarescence_ref: /Users/home/Desktop/Agendizer/CLARESCENCE-2026-02-06-agendizer-prd-reinforcement.md
  prd_delta_refs:
    - orchestration/state/impl/PRD-DELTAS-20260207-agendizer-hard-locks.md
  prior_receipts: []
capability_requirements:
  - swift-compilation
  - swiftui-rendering
  - swiftdata-modeling
  - xcode-project-creation
gates:
  - id: P0-G1
    description: "Xcode project builds cleanly with macOS 26 target"
    pass_criteria: "xcodebuild succeeds with zero errors"
  - id: P0-G2
    description: "SwiftData models match CLARESCENCE data model exactly"
    pass_criteria: "Intention, Project, Edge, EchoCluster, StateTransition models compile and conform to Codable + Identifiable"
  - id: P0-G3
    description: "CaptureView renders full-bleed text editor with Liquid Glass toolbar"
    pass_criteria: "Preview renders, text input works, amber Process button visible"
  - id: P0-G4
    description: "Unit tests for data model pass"
    pass_criteria: "All tests green, covering: IO creation, stage transitions, append-only enforcement"
  - id: P0-G5
    description: "Delta 5 enforcement: rawContent is immutable, stateTransitions are append-only"
    pass_criteria: "Attempting to mutate rawContent produces compile error; transitions array only supports append"
rollback_plan:
  action: "Delete Xcode project directory if Phase 0 gates fail"
  notification: "SwarmHandoffEnvelope with objective: ROLLBACK to Commander"
receipt_contract:
  required_fields:
    - proof_of_run (xcodebuild output or commit hash)
    - files_touched
    - bench_or_test_outcome
    - gate_results
  deadline_utc: "2026-02-14T00:00:00Z"
```

---

## Detailed Execution Brief

### Target: Adjudicator (Codex GPT-5.3)

### Step 1: Create Xcode Project
- App name: `Agendizer`
- Platform: macOS
- Lifecycle: SwiftUI (`@main App`)
- Minimum deployment: macOS 26 (Tahoe)
- Swift language version: 6.0
- Frameworks: SwiftUI, SwiftData, NaturalLanguage

### Step 2: Implement SwiftData Models

Per CLARESCENCE §4.3, implement these models exactly:

```swift
@Model final class Intention {
    @Attribute(.unique) let id: String  // ULID
    let createdAt: Date
    let rawContent: RawContent          // IMMUTABLE (Delta 5)
    var interpretation: Interpretation?
    var stage: PipelineStage
    var ontologyClass: OntologyClass
    var temporalBinding: TemporalBinding?
    var projectBindings: [Project]
    var echoCluster: EchoCluster?
    var edges: [Edge]
    var stateTransitions: [StateTransition]  // APPEND-ONLY (Delta 5)
    var dispatchPackage: DispatchPackage?
}
```

Plus: `Project`, `Edge`, `EchoCluster`, `StateTransition` (all per CLARESCENCE §4.3)
Plus: enums `PipelineStage`, `OntologyClass`, `CaptureSource`, `EdgeType`, `Actor`

### Step 3: Build CaptureView
- Full-bleed text editor filling the content area
- Liquid Glass toolbar at top with single amber "Process" button
- Previous entries scroll below with translucency
- Voice capture button (Speech.framework stub)
- Auto-save on text change
- CMD+N hotkey for new capture

### Step 4: Write Unit Tests
- `IntentionTests`: creation, rawContent immutability, stage transition append
- `ProjectTests`: creation, intention binding
- `EdgeTests`: creation, type assignment
- `PipelineStageTests`: valid transitions, invalid transitions rejected
- `StateTransitionTests`: append-only enforcement

### Step 5: Verify Gates
- Run `xcodebuild` — zero errors
- Run test suite — all green
- Screenshot CaptureView preview

---

## Handoff Protocol

On completion, Adjudicator produces:
1. `ExecutionReceipt` per CONTRACT §2.3
2. `SwarmHandoffEnvelope` back to Commander with artifacts for Gate C review
3. Commit all implementation to Agendizer repo/branch

---

**Priority**: P0
**Lane**: Adjudicator (Codex GPT-5.3)
**Deadline**: 2026-02-14T00:00:00Z
