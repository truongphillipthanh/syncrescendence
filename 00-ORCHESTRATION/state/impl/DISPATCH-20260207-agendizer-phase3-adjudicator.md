# DISPATCH PACKAGE — Agendizer Phase 3: Ledger

**DispatchPackageV2**

```yaml
id: DISPATCH-20260207-AGZ-P3-001
objective: "Implement the L2 Ledger depth layer with agenda-style timeline from append-only StateTransitions, on-device echo detection via NaturalLanguage.framework embeddings, and VelocityMetric on Project"
context_bundle:
  evidence_refs:
    - 00-ORCHESTRATION/state/impl/EVIDENCE-LOCK-20260207-agendizer-clarescence2.md
  prd_delta_refs:
    - 00-ORCHESTRATION/state/impl/PRD-DELTAS-20260207-agendizer-hard-locks.md
  prior_receipts:
    - ER-20260207-AGZ-P0-001 (Phase 0 complete, all gates passed)
    - ER-20260207-AGZ-GATE-P0-001 (Commander gate review P0 approved)
    - ER-20260207-AGZ-P1-001 (Phase 1 complete, all gates passed)
    - ER-20260207-AGZ-GATE-P1-001 (Commander gate review P1 approved)
    - ER-20260207-AGZ-P2-001 (Phase 2 complete, all gates passed)
    - ER-20260207-AGZ-GATE-P2-001 (Commander gate review P2 approved)
capability_requirements:
  - swift-compilation
  - swiftui-rendering
  - natural-language-framework
  - swiftdata-queries
  - timeline-view-layout
gates:
  - id: P3-G1
    description: "LedgerView renders agenda-style timeline from StateTransitions"
    pass_criteria: "L2 Ledger shows a chronological timeline of StateTransitions grouped by date. Each entry shows timestamp, fromStage→toStage, actor, and rationale. Build succeeds."
  - id: P3-G2
    description: "Timeline is read-only projection of append-only log"
    pass_criteria: "LedgerView is strictly read-only. No edit/delete affordances. Timeline data source is Intention.stateTransitions — the append-only log. No separate timeline data store."
  - id: P3-G3
    description: "EchoDetector uses NaturalLanguage.framework on-device embeddings"
    pass_criteria: "EchoDetector protocol with LocalEchoDetector implementation. Uses NLEmbedding for semantic similarity between Intention.rawContent values. Never sends data externally. Threshold-based clustering into EchoCluster."
  - id: P3-G4
    description: "Echo clusters surface in LedgerView"
    pass_criteria: "LedgerView has an 'Echoes' section showing detected EchoClusters with frequency, trajectory, and member intentions. Clusters are discoverable but not intrusive."
  - id: P3-G5
    description: "VelocityMetric added to Project"
    pass_criteria: "Project model extended with VelocityMetric (or computed velocity). Metric reflects capture-to-dispatch throughput rate. Available in NavigateView project detail."
  - id: P3-G6
    description: "L2 Ledger accessible via CMD+2 from AppNavigationState"
    pass_criteria: "AppNavigationState.DepthLayer.ledger.isAvailable returns true. CMD+2 shortcut wired in AgendizerApp commands. L2 toggleable from L0/L1."
  - id: P3-G7
    description: "Progressive disclosure preserved — L3/L4 still unavailable"
    pass_criteria: "DepthLayer.connect and .dispatch remain isAvailable == false. L3/L4 not exposed in UI or keyboard commands."
  - id: P3-G8
    description: "All existing tests still pass + new ledger/echo tests"
    pass_criteria: "All 16 Phase 0-2 tests green. New tests cover: LedgerView timeline rendering, echo detection similarity, echo clustering, VelocityMetric, CMD+2 shortcut, L3/L4 still gated. Total >= 22 tests."
rollback_plan:
  action: "Revert Phase 3 commits if gates fail; Phase 0+1+2 foundation remains intact"
  notification: "SwarmHandoffEnvelope with objective: ROLLBACK-P3 to Commander"
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
### Phase: 3 — Ledger (Timeline + Echo Detection)
### Primary Delta Enforcement: Delta 5 (timeline from append-only log), Delta 4 (on-device echo detection)

---

### Step 1: Create EchoDetector Protocol + LocalEchoDetector

Create `Agendizer/Echoes/EchoDetector.swift`:

```swift
import Foundation
import NaturalLanguage

/// Protocol for detecting echo patterns (recurring themes) across intentions.
protocol EchoDetector {
    func detectEchoes(in intentions: [Intention]) -> [EchoCluster]
    var requiresNetwork: Bool { get }
}

/// On-device echo detection using NaturalLanguage.framework embeddings.
/// NEVER sends data externally (Delta 4).
final class LocalEchoDetector: EchoDetector {
    let requiresNetwork = false

    /// Similarity threshold for clustering (0.0 to 1.0).
    /// Intentions with embedding distance below this are considered echoes.
    private let similarityThreshold: Double = 0.75

    func detectEchoes(in intentions: [Intention]) -> [EchoCluster] {
        guard intentions.count >= 2 else { return [] }
        guard let embedding = NLEmbedding.wordEmbedding(for: .english) else { return [] }

        // Build similarity groups using sentence-level embedding comparison
        var clusters: [[Intention]] = []
        var assigned = Set<UUID>()

        for i in 0..<intentions.count {
            guard !assigned.contains(intentions[i].id) else { continue }
            var cluster = [intentions[i]]
            assigned.insert(intentions[i].id)

            for j in (i+1)..<intentions.count {
                guard !assigned.contains(intentions[j].id) else { continue }
                let distance = embedding.distance(
                    between: intentions[i].rawContent,
                    and: intentions[j].rawContent
                )
                // NLEmbedding.distance returns cosine distance; lower = more similar
                if distance < (1.0 - similarityThreshold) {
                    cluster.append(intentions[j])
                    assigned.insert(intentions[j].id)
                }
            }

            if cluster.count >= 2 {
                clusters.append(cluster)
            }
        }

        return clusters.map { group in
            let sorted = group.sorted { $0.createdAt < $1.createdAt }
            return EchoCluster(
                intentions: sorted,
                frequency: group.count,
                trajectory: classifyTrajectory(group),
                firstSeen: sorted.first!.createdAt,
                lastSeen: sorted.last!.createdAt
            )
        }
    }

    private func classifyTrajectory(_ group: [Intention]) -> EchoTrajectory {
        guard group.count >= 2 else { return .stable }
        let firstHalf = group.prefix(group.count / 2)
        let secondHalf = group.suffix(group.count / 2)
        let firstRate = Double(firstHalf.count)
        let secondRate = Double(secondHalf.count)
        if secondRate > firstRate * 1.5 { return .rising }
        if secondRate < firstRate * 0.5 { return .fading }
        return .stable
    }
}
```

**Note**: `NLEmbedding.wordEmbedding` may need to be replaced with `NLEmbedding.sentenceEmbedding` if available on macOS 26, or use `NLModel` with a custom embedding model. The key constraint is **on-device only** — no network calls. Adjust the embedding approach if sentence-level embeddings produce better clustering, but maintain the `EchoDetector` protocol abstraction.

### Step 2: Create LedgerView (L2)

Create `Agendizer/Views/LedgerView.swift`:

```swift
import SwiftUI
import SwiftData

/// L2 Ledger — Agenda-style timeline from the append-only StateTransition log.
/// This view is strictly READ-ONLY (Delta 5 — no edit/delete of transition history).
struct LedgerView: View {
    @Query(sort: \Intention.createdAt, order: .reverse) private var intentions: [Intention]
    @State private var echoDetector: LocalEchoDetector = LocalEchoDetector()
    @State private var echoClusters: [EchoCluster] = []

    var body: some View {
        NavigationSplitView {
            // Sidebar: Date-grouped timeline
            List {
                Section("Timeline") {
                    ForEach(groupedTransitions, id: \.date) { group in
                        DisclosureGroup(group.dateLabel) {
                            ForEach(group.entries, id: \.id) { entry in
                                TimelineEntryRow(entry: entry)
                            }
                        }
                    }
                }

                if !echoClusters.isEmpty {
                    Section("Echoes") {
                        ForEach(echoClusters) { cluster in
                            EchoClusterRow(cluster: cluster)
                        }
                    }
                }
            }
            .glassEffect()
            .navigationTitle("Ledger")
        } detail: {
            Text("Select a timeline entry to view details")
                .foregroundStyle(.secondary)
        }
        .task {
            echoClusters = echoDetector.detectEchoes(in: intentions)
        }
    }

    // Group all StateTransitions across all Intentions by date
    private var groupedTransitions: [DateGroup] {
        let allTransitions: [(Intention, StateTransition)] = intentions.flatMap { intention in
            intention.stateTransitions.map { (intention, $0) }
        }
        let sorted = allTransitions.sorted { $0.1.timestamp > $1.1.timestamp }

        let calendar = Calendar.current
        let grouped = Dictionary(grouping: sorted) { pair in
            calendar.startOfDay(for: pair.1.timestamp)
        }

        return grouped.map { date, entries in
            DateGroup(
                date: date,
                dateLabel: date.formatted(.dateTime.month().day().weekday()),
                entries: entries.map { intention, transition in
                    TimelineEntry(
                        id: transition.id,
                        timestamp: transition.timestamp,
                        intentionContent: String(intention.rawContent.prefix(80)),
                        fromStage: transition.fromStage,
                        toStage: transition.toStage,
                        actor: transition.actor,
                        rationale: transition.rationale
                    )
                }
            )
        }
        .sorted { $0.date > $1.date }
    }
}

// MARK: - Supporting Types

struct DateGroup {
    let date: Date
    let dateLabel: String
    let entries: [TimelineEntry]
}

struct TimelineEntry: Identifiable {
    let id: UUID
    let timestamp: Date
    let intentionContent: String
    let fromStage: PipelineStage
    let toStage: PipelineStage
    let actor: Actor
    let rationale: String
}

struct TimelineEntryRow: View {
    let entry: TimelineEntry

    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            HStack {
                Text(entry.fromStage.rawValue)
                    .font(.caption.bold())
                    .foregroundStyle(.secondary)
                Image(systemName: "arrow.right")
                    .font(.caption2)
                Text(entry.toStage.rawValue)
                    .font(.caption.bold())
                    .foregroundStyle(.primary)
                Spacer()
                Text(entry.timestamp.formatted(.dateTime.hour().minute()))
                    .font(.caption2)
                    .foregroundStyle(.tertiary)
            }
            Text(entry.intentionContent)
                .font(.subheadline)
                .lineLimit(2)
            if !entry.rationale.isEmpty {
                Text(entry.rationale)
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
        }
        .padding(.vertical, 2)
    }
}

struct EchoClusterRow: View {
    let cluster: EchoCluster

    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            HStack {
                Image(systemName: "waveform.path.ecg")
                    .foregroundStyle(Color(hex: 0xD87001))
                Text("\(cluster.frequency)× echo")
                    .font(.subheadline.bold())
                Spacer()
                Text(cluster.trajectory.rawValue)
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
            Text(cluster.intentions.first?.rawContent.prefix(60) ?? "")
                .font(.caption)
                .lineLimit(1)
            Text("\(cluster.firstSeen.formatted(.dateTime.month().day())) — \(cluster.lastSeen.formatted(.dateTime.month().day()))")
                .font(.caption2)
                .foregroundStyle(.tertiary)
        }
    }
}
```

### Step 3: Add VelocityMetric to Project

Extend `Agendizer/Models/DomainModels.swift`:

```swift
/// Velocity metric — captures capture-to-dispatch throughput rate for a project.
struct VelocityMetric: Codable {
    var capturedCount: Int = 0
    var dispatchedCount: Int = 0
    var averageTransitTimeSeconds: Double? = nil
    var lastComputedAt: Date = Date()

    var throughputRate: Double {
        guard capturedCount > 0 else { return 0 }
        return Double(dispatchedCount) / Double(capturedCount)
    }
}
```

Add to `Project` model:

```swift
var velocityMetric: VelocityMetric = VelocityMetric()
```

**Important**: Ensure VelocityMetric is Codable-compatible with SwiftData. If SwiftData doesn't natively persist custom Codable structs, store as JSON Data and decode on access.

### Step 4: Update AppNavigationState for L2

Modify `Agendizer/Navigation/AppNavigationState.swift`:

- Change `DepthLayer.ledger.isAvailable` to return `true`
- Add `keyboardShortcut` for `.ledger`: `"2"`
- Add `toggleLedger()` method following same pattern as `toggleNavigate()`

```swift
var isAvailable: Bool {
    switch self {
    case .capture, .navigate, .ledger: return true  // L2 now available
    case .connect, .dispatch: return false           // L3/L4 still gated
    }
}

var keyboardShortcut: KeyEquivalent? {
    switch self {
    case .capture: return "0"
    case .navigate: return "1"
    case .ledger: return "2"      // CMD+2 for Ledger
    case .connect: return nil
    case .dispatch: return nil
    }
}
```

### Step 5: Wire CMD+2 in AgendizerApp

Add to `AgendizerApp.swift` `CommandGroup`:

```swift
Button("Ledger") {
    navigationState.toggleLedger()
}
.keyboardShortcut("2", modifiers: .command)
```

### Step 6: Update ContentView for L2 Rendering

In `ContentView.swift`, add the `.ledger` case:

```swift
switch navigationState.activeLayer {
case .capture:
    CaptureView()
case .navigate:
    NavigateView()
case .ledger:
    LedgerView()
default:
    CaptureView()
}
```

### Step 7: Write Tests

Add to `AgendizerTests/LedgerTests.swift` (new file):

Required test cases:
1. `testLedgerLayerNowAvailable` — `DepthLayer.ledger.isAvailable == true`
2. `testConnectAndDispatchStillUnavailable` — L3/L4 `isAvailable == false`
3. `testToggleLedgerChangesLayer` — CMD+2 switches to L2
4. `testGoToCaptureFromLedger` — CMD+0 returns to L0 from L2
5. `testEchoDetectorDoesNotRequireNetwork` — `LocalEchoDetector().requiresNetwork == false`
6. `testEchoDetectorClustersIdenticalContent` — Two intentions with very similar rawContent form a cluster
7. `testEchoDetectorIgnoresDissimilarContent` — Two dissimilar intentions produce no cluster
8. `testTimelineGroupsByDate` — StateTransitions group correctly by calendar day
9. `testVelocityMetricThroughputRate` — throughputRate computed correctly
10. `testLedgerTimelineIsReadOnly` — Verify no mutation APIs on timeline view data

Add to `AgendizerTests/EchoTests.swift` (new file):

Additional echo-specific tests:
1. `testEchoTrajectoryClassification` — Rising/fading/stable classification
2. `testEchoDetectorMinimumTwoIntentions` — Single intention returns empty clusters

### Step 8: Verify All Phase 0+1+2 Tests Still Pass

Run full test suite: `xcodebuild test`. All 16 existing tests must still pass alongside new ledger/echo tests. Target: >= 22 total tests.

---

## Phase 0+1+2 Artifacts Available

These files exist and should be extended, not replaced:

- `Agendizer/Models/DomainModels.swift` — Add VelocityMetric struct, extend Project
- `Agendizer/Navigation/AppNavigationState.swift` — Enable L2, add toggleLedger(), wire CMD+2
- `Agendizer/Views/ContentView.swift` — Add .ledger case
- `Agendizer/Views/CaptureView.swift` — No changes needed
- `Agendizer/Views/NavigateView.swift` — No changes needed (wire project velocity display if time permits)
- `Agendizer/AgendizerApp.swift` — Add CMD+2 command
- `AgendizerTests/IntentionTests.swift` — Must still pass
- `AgendizerTests/ProjectEdgePipelineTests.swift` — Must still pass
- `AgendizerTests/NavigationTests.swift` — Must still pass (update testFutureLayersNotAvailable to reflect L2 now available)

**Important**: `NavigationTests.testFutureLayersNotAvailable` currently asserts L2/L3/L4 are unavailable. This test MUST be updated to assert only L3/L4 are unavailable (L2 is now available). Do NOT break this test — update it.

---

## New Files Expected

| File | Purpose |
|---|---|
| `Agendizer/Echoes/EchoDetector.swift` | Echo detection protocol + LocalEchoDetector |
| `Agendizer/Views/LedgerView.swift` | L2 agenda-style timeline view |
| `AgendizerTests/LedgerTests.swift` | Ledger timeline + velocity tests |
| `AgendizerTests/EchoTests.swift` | Echo detection tests |

---

## Handoff Protocol

On completion, Adjudicator produces:
1. `ExecutionReceipt` per CONTRACT §2.3
2. `SwarmHandoffEnvelope` back to Commander for gate review
3. Result file to `-INBOX/commander/00-INBOX0/RESULT-adjudicator-YYYYMMDD-agendizer-phase3.md`
4. CONFIRM file to Commander's inbox (per DYN-DISPATCH_KANBAN_PROTOCOL v1.1.0)

---

**Priority**: P0
**Lane**: Adjudicator (Codex GPT-5.3)
**Deadline**: 2026-02-21T00:00:00Z
**Reply-To**: commander
