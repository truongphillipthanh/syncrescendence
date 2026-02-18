# DISPATCH PACKAGE — Agendizer Phase 1: Interpretation

**DispatchPackageV2**

```yaml
id: DISPATCH-20260207-AGZ-P1-001
objective: "Implement the Script Breakdown Engine (IntentionInterpreter) with local and cloud backends, interpretation review UI, correction feedback loop, and PipelineEngine"
context_bundle:
  evidence_refs:
    - 00-ORCHESTRATION/state/impl/EVIDENCE-LOCK-20260207-agendizer-clarescence2.md
  clarescence_ref: /Users/home/Desktop/Agendizer/CLARESCENCE-2026-02-06-agendizer-prd-reinforcement.md
  prd_delta_refs:
    - 00-ORCHESTRATION/state/impl/PRD-DELTAS-20260207-agendizer-hard-locks.md
  prior_receipts:
    - ER-20260207-AGZ-P0-001 (Phase 0 complete, all gates passed)
    - ER-20260207-AGZ-GATE-P0-001 (Commander gate review approved)
capability_requirements:
  - swift-compilation
  - swiftui-rendering
  - coreml-integration
  - protocol-oriented-design
gates:
  - id: P1-G1
    description: "IntentionInterpreter protocol defined with swappable backends"
    pass_criteria: "Protocol compiles, LocalInterpreter and CloudInterpreter both conform"
  - id: P1-G2
    description: "LocalInterpreter uses on-device NaturalLanguage.framework"
    pass_criteria: "NaturalLanguage import, NLModel or NLEmbedding usage for ontology classification, no external network calls"
  - id: P1-G3
    description: "CloudInterpreter gates on explicit user authorization"
    pass_criteria: "Cloud calls require user opt-in flag, clear UI indication when cloud is active"
  - id: P1-G4
    description: "Interpretation review UI renders 'You wrote X → I interpreted as Y → Approve/Edit/Reject'"
    pass_criteria: "InterpretationReviewView displays raw capture, proposed interpretation, and three action buttons"
  - id: P1-G5
    description: "Corrections stored as StateTransitions (Delta 5 enforcement)"
    pass_criteria: "Rejecting/editing an interpretation appends a StateTransition with actor and rationale"
  - id: P1-G6
    description: "PipelineEngine advances IOs through stages"
    pass_criteria: "PipelineEngine can process an Intention from .captured through .interpreted with appropriate transitions"
  - id: P1-G7
    description: "Integration tests pass for interpretation pipeline"
    pass_criteria: "All tests green, covering: local interpretation, cloud interpretation (mocked), approval, rejection, correction"
rollback_plan:
  action: "Revert Phase 1 commits if gates fail; Phase 0 foundation remains intact"
  notification: "SwarmHandoffEnvelope with objective: ROLLBACK-P1 to Commander"
receipt_contract:
  required_fields:
    - proof_of_run
    - files_touched
    - bench_or_test_outcome
    - gate_results
  deadline_utc: "2026-02-21T00:00:00Z"
```

---

## Detailed Execution Brief

### Target: Adjudicator (Codex GPT-5.3)
### Phase: 1 — Interpretation (Script Breakdown Engine)
### Primary Delta Enforcement: Delta 4 (on-device default), Delta 5 (corrections as transitions)

---

### Step 1: Define IntentionInterpreter Protocol

Create `Agendizer/Interpretation/IntentionInterpreter.swift`:

```swift
protocol IntentionInterpreter {
    /// Interpret raw content and return a proposed interpretation
    func interpret(_ intention: Intention) async throws -> Interpretation

    /// Whether this interpreter requires network access
    var requiresNetwork: Bool { get }

    /// Display name for UI attribution
    var displayName: String { get }
}
```

### Step 2: Implement LocalInterpreter

Create `Agendizer/Interpretation/LocalInterpreter.swift`:

- Import `NaturalLanguage`
- Use `NLEmbedding.wordEmbedding(for: .english)` or a custom CoreML text classification model for ontology class routing
- Classify raw text into `OntologyClass` (project, area, resource, echo, tension, signal)
- Generate charitable interpretation summary based on classification + text analysis
- **No network calls**. `requiresNetwork = false`.

Charitable interpretation strategy:
- Extract action verbs → suggest this is a task/project
- Detect temporal references → suggest scheduling
- Detect emotional language → classify as tension/signal
- Detect repeated themes → flag potential echo
- Always frame interpretation charitably: "It sounds like you want to..." not "You need to..."

### Step 3: Implement CloudInterpreter

Create `Agendizer/Interpretation/CloudInterpreter.swift`:

- Stub that formats an MCP tool call request for Claude/GPT
- `requiresNetwork = true`
- Requires explicit `isCloudAuthorized: Bool` flag — refuse to execute if false
- UI must show clear "Cloud" indicator when active
- For Phase 1: implement as a mock/stub. Real MCP integration comes in Phase 5.

### Step 4: Build InterpretationReviewView

Create `Agendizer/Views/InterpretationReviewView.swift`:

Visual layout:
```
┌─────────────────────────────────────┐
│ You wrote:                          │
│ ┌─────────────────────────────────┐ │
│ │ [Raw capture text, immutable]   │ │
│ └─────────────────────────────────┘ │
│                                     │
│ I interpreted this as:              │
│ ┌─────────────────────────────────┐ │
│ │ [Proposed interpretation]       │ │
│ │ Category: [OntologyClass]       │ │
│ │ Rationale: [Charitable reading] │ │
│ └─────────────────────────────────┘ │
│                                     │
│ [Approve ✓]  [Edit ✎]  [Reject ✗]  │
│                                     │
│ Interpreted by: [LocalInterpreter]  │
└─────────────────────────────────────┘
```

- **Approve**: Accept interpretation, append StateTransition (captured → interpreted), advance stage
- **Edit**: Present editable text field with pre-filled interpretation, on save append StateTransition with `actor: .human` and rationale "Manual correction"
- **Reject**: Append StateTransition with `actor: .human` and rationale "Interpretation rejected", stage remains `.captured`, mark for re-interpretation

### Step 5: Implement PipelineEngine

Create `Agendizer/Pipeline/PipelineEngine.swift`:

```swift
@Observable
final class PipelineEngine {
    private let interpreter: IntentionInterpreter

    init(interpreter: IntentionInterpreter) {
        self.interpreter = interpreter
    }

    /// Process a captured intention through interpretation
    func processCapture(_ intention: Intention) async throws -> Interpretation {
        guard intention.stage == .captured else {
            throw PipelineError.invalidStage(current: intention.stage, expected: .captured)
        }
        return try await interpreter.interpret(intention)
    }

    /// Apply an approved interpretation to an intention
    func applyInterpretation(
        _ interpretation: Interpretation,
        to intention: Intention,
        actor: Actor
    ) {
        intention.interpretation = interpretation
        intention.transition(
            to: .interpreted,
            actor: actor,
            rationale: "Interpretation approved"
        )
    }
}
```

### Step 6: Wire Into CaptureView

Modify `CaptureView.swift`:
- After "Process" button creates an Intention, trigger `PipelineEngine.processCapture()`
- On completion, present `InterpretationReviewView` as a sheet
- User approves/edits/rejects → StateTransition appended → UI updates

### Step 7: Write Tests

Create `AgendizerTests/InterpretationTests.swift`:

Required test cases:
1. `testLocalInterpreterReturnsInterpretation` — LocalInterpreter produces valid Interpretation
2. `testCloudInterpreterRefusesWithoutAuthorization` — CloudInterpreter throws if not authorized
3. `testApprovalCreatesStateTransition` — Approving interpretation appends transition captured→interpreted
4. `testRejectionKeepsStageAsCaptured` — Rejecting interpretation appends transition but keeps stage
5. `testCorrectionRecordsHumanActor` — Editing interpretation records human actor with "Manual correction"
6. `testPipelineEngineRejectsWrongStage` — Calling processCapture on non-captured intention throws
7. `testInterpretationPreservesRawContent` — After interpretation, rawContent is unchanged (Delta 5)

---

## Phase 0 Artifacts Available

These files exist from Phase 0 and should be extended, not replaced:

- `Agendizer/Models/DomainModels.swift` — Add `PipelineError` enum if needed
- `Agendizer/Views/CaptureView.swift` — Wire PipelineEngine
- `Agendizer/AgendizerApp.swift` — May need to inject PipelineEngine
- `AgendizerTests/IntentionTests.swift` — Reference for test patterns

---

## New Files Expected

| File | Purpose |
|---|---|
| `Agendizer/Interpretation/IntentionInterpreter.swift` | Protocol definition |
| `Agendizer/Interpretation/LocalInterpreter.swift` | On-device NL interpretation |
| `Agendizer/Interpretation/CloudInterpreter.swift` | Cloud interpretation stub |
| `Agendizer/Pipeline/PipelineEngine.swift` | Stage advancement engine |
| `Agendizer/Views/InterpretationReviewView.swift` | Approve/Edit/Reject UI |
| `AgendizerTests/InterpretationTests.swift` | Integration tests |

---

## Handoff Protocol

On completion, Adjudicator produces:
1. `ExecutionReceipt` per CONTRACT §2.3
2. `SwarmHandoffEnvelope` back to Commander for gate review
3. Result file to `-INBOX/commander/00-INBOX0/RESULT-adjudicator-20260207-agendizer-phase1.md`

---

**Priority**: P0
**Lane**: Adjudicator (Codex GPT-5.3)
**Deadline**: 2026-02-21T00:00:00Z
