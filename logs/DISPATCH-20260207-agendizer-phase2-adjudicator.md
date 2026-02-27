# DISPATCH PACKAGE — Agendizer Phase 2: Navigation

**DispatchPackageV2**

```yaml
id: DISPATCH-20260207-AGZ-P2-001
objective: "Implement the L1 Navigate depth layer with three-column NavigationSplitView, progressive disclosure architecture, and keyboard-driven depth traversal"
context_bundle:
  evidence_refs:
    - orchestration/state/impl/EVIDENCE-LOCK-20260207-agendizer-clarescence2.md
  prd_delta_refs:
    - orchestration/state/impl/PRD-DELTAS-20260207-agendizer-hard-locks.md
  prior_receipts:
    - ER-20260207-AGZ-P0-001 (Phase 0 complete, all gates passed)
    - ER-20260207-AGZ-GATE-P0-001 (Commander gate review P0 approved)
    - ER-20260207-AGZ-P1-001 (Phase 1 complete, all gates passed)
    - ER-20260207-AGZ-GATE-P1-001 (Commander gate review P1 approved)
capability_requirements:
  - swift-compilation
  - swiftui-rendering
  - navigation-architecture
  - keyboard-shortcut-integration
gates:
  - id: P2-G1
    description: "NavigationSplitView with three-column layout renders correctly"
    pass_criteria: "L1 Navigate uses NavigationSplitView with sidebar, list, and detail columns. Build succeeds."
  - id: P2-G2
    description: "L0 Capture remains accessible via one tap or CMD+0"
    pass_criteria: "From any depth layer, CMD+0 (or equivalent shortcut) returns to L0 CaptureView. Capture is never more than one action away."
  - id: P2-G3
    description: "L1 Navigate revealed by swipe or CMD+1"
    pass_criteria: "CMD+1 toggles NavigationSplitView. L1 is not visible on first launch — user must discover it."
  - id: P2-G4
    description: "Sidebar uses Liquid Glass material"
    pass_criteria: "NavigationSplitView sidebar has .glassEffect() modifier applied. Visually consistent with Delta 1."
  - id: P2-G5
    description: "Navigation state is depth-based, not tab-based"
    pass_criteria: "No TabView anywhere in the app. Navigation is hierarchical depth (L0→L1→L2→...), not lateral tabs."
  - id: P2-G6
    description: "Progressive disclosure architecture in place"
    pass_criteria: "L2/L3/L4 views are stub placeholders or not yet visible. System does not expose deeper layers until future phases. A new user sees only L0 and can discover L1."
  - id: P2-G7
    description: "All existing tests still pass + new navigation tests"
    pass_criteria: "All 10 Phase 1 tests green. New tests cover: L1 visibility toggle, CMD shortcuts, navigation state management. Total >= 13 tests."
rollback_plan:
  action: "Revert Phase 2 commits if gates fail; Phase 0+1 foundation remains intact"
  notification: "SwarmHandoffEnvelope with objective: ROLLBACK-P2 to Commander"
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
### Phase: 2 — Navigation (Progressive Disclosure Depth Stack)
### Primary Delta Enforcement: Delta 2 (depth stack, not tabs), Delta 1 (Liquid Glass)

---

### Step 1: Create AppNavigationState

Create `Agendizer/Navigation/AppNavigationState.swift`:

```swift
import SwiftUI

/// Manages the app's depth-layer navigation state.
/// L0 = Capture, L1 = Navigate, L2 = Ledger (future), L3 = Connect (future), L4 = Dispatch (future)
@Observable
final class AppNavigationState {
    enum DepthLayer: Int, CaseIterable, Identifiable {
        case capture = 0    // L0 — always available
        case navigate = 1   // L1 — discovered via CMD+1
        case ledger = 2     // L2 — Phase 3
        case connect = 3    // L3 — Phase 4
        case dispatch = 4   // L4 — Phase 5

        var id: Int { rawValue }

        var keyboardShortcut: KeyEquivalent? {
            switch self {
            case .capture: return "0"
            case .navigate: return "1"
            case .ledger: return "2"
            case .connect: return nil  // CMD+Shift+G in Phase 4
            case .dispatch: return nil // CMD+D in Phase 5
            }
        }

        var isAvailable: Bool {
            switch self {
            case .capture, .navigate: return true
            case .ledger, .connect, .dispatch: return false // unlocked in future phases
            }
        }
    }

    var activeLayer: DepthLayer = .capture
    var isNavigateRevealed: Bool = false

    func goToCapture() {
        activeLayer = .capture
    }

    func toggleNavigate() {
        if activeLayer == .navigate {
            activeLayer = .capture
        } else {
            activeLayer = .navigate
            isNavigateRevealed = true
        }
    }
}
```

### Step 2: Create NavigateView (L1)

Create `Agendizer/Views/NavigateView.swift`:

```swift
import SwiftUI
import SwiftData

struct NavigateView: View {
    @Query private var intentions: [Intention]
    @Query private var projects: [Project]

    var body: some View {
        NavigationSplitView {
            // Sidebar: Projects + categories
            List {
                Section("Projects") {
                    ForEach(projects) { project in
                        NavigationLink(value: project) {
                            Label(project.name, systemImage: "folder")
                        }
                    }
                }
                Section("Recent Captures") {
                    ForEach(intentions.prefix(20)) { intention in
                        NavigationLink(value: intention) {
                            Text(intention.rawContent.prefix(60) + "...")
                                .lineLimit(2)
                        }
                    }
                }
            }
            .glassEffect()
        } content: {
            // List: Intentions within selected project/category
            Text("Select a project or capture")
                .foregroundStyle(.secondary)
        } detail: {
            // Detail: Full intention view
            Text("Select an item to view details")
                .foregroundStyle(.secondary)
        }
    }
}
```

### Step 3: Update ContentView for Depth Navigation

Modify `Agendizer/Views/ContentView.swift`:

```swift
import SwiftUI

struct ContentView: View {
    @State private var navigationState = AppNavigationState()

    var body: some View {
        Group {
            switch navigationState.activeLayer {
            case .capture:
                CaptureView()
            case .navigate:
                NavigateView()
            default:
                // Future phases — should never render yet
                CaptureView()
            }
        }
        .keyboardShortcut("0", modifiers: .command) // CMD+0 → Capture
        .keyboardShortcut("1", modifiers: .command) // CMD+1 → Navigate
        .environment(navigationState)
    }
}
```

**Important**: Use `.commands {}` modifier on the `WindowGroup` in `AgendizerApp.swift` for proper keyboard shortcut handling. The shortcuts should be menu commands, not view-level shortcuts.

### Step 4: Wire Keyboard Shortcuts in AgendizerApp

Modify `Agendizer/AgendizerApp.swift`:

Add a `CommandGroup` for navigation:

```swift
.commands {
    CommandGroup(after: .sidebar) {
        Button("Capture") {
            navigationState.goToCapture()
        }
        .keyboardShortcut("0", modifiers: .command)

        Button("Navigate") {
            navigationState.toggleNavigate()
        }
        .keyboardShortcut("1", modifiers: .command)
    }
}
```

### Step 5: Ensure No Tabs

**Critical constraint**: There must be NO `TabView` anywhere in the codebase. Navigation is depth-based. Verify with a project-wide search for `TabView` — must return zero results.

### Step 6: Write Tests

Add to `AgendizerTests/NavigationTests.swift`:

Required test cases:
1. `testDefaultLayerIsCapture` — App starts on L0
2. `testToggleNavigateChangesLayer` — CMD+1 switches to L1
3. `testGoToCaptureFromAnyLayer` — CMD+0 always returns to L0
4. `testNavigateRevealedFlagSetsOnFirstVisit` — `isNavigateRevealed` becomes true
5. `testNoTabViewInApp` — Static assertion: no TabView usage (compile-time or runtime)
6. `testFutureLayersNotAvailable` — L2/L3/L4 `isAvailable == false`

### Step 7: Verify All Phase 0+1 Tests Still Pass

Run full test suite: `xcodebuild test`. All 10 existing tests must still pass alongside new navigation tests.

---

## Phase 0+1 Artifacts Available

These files exist and should be extended, not replaced:

- `Agendizer/Models/DomainModels.swift` — Add navigation-related types if needed
- `Agendizer/Views/CaptureView.swift` — Remains L0, no changes needed
- `Agendizer/Views/ContentView.swift` — Major changes: wrap in depth navigation
- `Agendizer/AgendizerApp.swift` — Add keyboard commands + navigation state
- `AgendizerTests/IntentionTests.swift` — Must still pass
- `AgendizerTests/ProjectEdgePipelineTests.swift` — Must still pass

---

## New Files Expected

| File | Purpose |
|---|---|
| `Agendizer/Navigation/AppNavigationState.swift` | Depth-layer state machine |
| `Agendizer/Views/NavigateView.swift` | L1 three-column NavigationSplitView |
| `AgendizerTests/NavigationTests.swift` | Navigation depth tests |

---

## Handoff Protocol

On completion, Adjudicator produces:
1. `ExecutionReceipt` per CONTRACT §2.3
2. `SwarmHandoffEnvelope` back to Commander for gate review
3. Result file to `-INBOX/commander/00-INBOX0/RESULT-adjudicator-YYYYMMDD-agendizer-phase2.md`
4. CONFIRM file to Commander's inbox (per DYN-DISPATCH_KANBAN_PROTOCOL v1.1.0)

---

**Priority**: P0
**Lane**: Adjudicator (Codex GPT-5.3)
**Deadline**: 2026-02-21T00:00:00Z
**Reply-To**: commander
