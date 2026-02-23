# DISPATCH PACKAGE — Agendizer Phase 4: Connect

**DispatchPackageV2**

```yaml
id: DISPATCH-20260207-AGZ-P4-001
objective: "Implement the L3 Connect depth layer with force-directed graph visualization using Metal rendering, on-device convergence edge computation, and echo-to-graph integration"
context_bundle:
  evidence_refs:
    - orchestration/state/impl/EVIDENCE-LOCK-20260207-agendizer-clarescence2.md
  prd_delta_refs:
    - orchestration/state/impl/PRD-DELTAS-20260207-agendizer-hard-locks.md
  prior_receipts:
    - ER-20260207-AGZ-P0-001 (Phase 0 complete)
    - ER-20260207-AGZ-GATE-P0-001 (Commander P0 approved)
    - ER-20260207-AGZ-P1-001 (Phase 1 complete)
    - ER-20260207-AGZ-GATE-P1-001 (Commander P1 approved)
    - ER-20260207-AGZ-P2-001 (Phase 2 complete)
    - ER-20260207-AGZ-GATE-P2-001 (Commander P2 approved)
    - ER-20260207-AGZ-P3-001 (Phase 3 complete)
    - ER-20260207-AGZ-GATE-P3-001 (Commander P3 approved)
capability_requirements:
  - swift-compilation
  - swiftui-rendering
  - metal-rendering
  - force-directed-graph-layout
  - natural-language-framework
  - gesture-recognition
gates:
  - id: P4-G1
    description: "ConnectView renders force-directed graph of Intentions and Edges"
    pass_criteria: "L3 Connect displays a force-directed graph where nodes are Intentions and edges are Edge relationships. Graph uses physics simulation for layout. Build succeeds."
  - id: P4-G2
    description: "Graph rendering uses Metal acceleration"
    pass_criteria: "Graph rendering pipeline uses Metal (MTKView or CAMetalLayer) for GPU-accelerated node/edge drawing. Falls back gracefully if Metal unavailable. Liquid Glass material on graph chrome (Delta 1)."
  - id: P4-G3
    description: "On-device convergence edge computation"
    pass_criteria: "ConvergenceDetector protocol + LocalConvergenceDetector using NaturalLanguage.framework semantic similarity. Computes Edge relationships between Intentions based on content similarity. Never sends data externally (Delta 4). Edges stored with confidence scores and attribution."
  - id: P4-G4
    description: "Echo clusters visualized as graph supernodes"
    pass_criteria: "EchoClusters from Phase 3 render as grouped/highlighted supernodes in the graph. Echo trajectory (rising/stable/fading) visually indicated. Tapping a supernode expands to show member intentions."
  - id: P4-G5
    description: "L3 Connect accessible via CMD+Shift+G"
    pass_criteria: "AppNavigationState.DepthLayer.connect.isAvailable returns true. CMD+Shift+G (or pinch-to-zoom gesture) activates L3. Shortcut wired in AgendizerApp commands."
  - id: P4-G6
    description: "Graph supports pan, zoom, and node selection"
    pass_criteria: "MagnifyGesture for zoom, DragGesture for pan, tap for node selection. Selected node shows detail panel with intention content, edges, and stage history."
  - id: P4-G7
    description: "Progressive disclosure preserved — L4 still unavailable"
    pass_criteria: "DepthLayer.dispatch remains isAvailable == false. L4 not exposed in UI or keyboard commands."
  - id: P4-G8
    description: "All existing tests still pass + new connect/graph tests"
    pass_criteria: "All 24 Phase 0-3 tests green. New tests cover: graph node creation from intentions, convergence detection, echo supernode grouping, CMD+Shift+G routing, L4 still gated. Total >= 30 tests."
rollback_plan:
  action: "Revert Phase 4 commits if gates fail; Phase 0-3 foundation remains intact"
  notification: "SwarmHandoffEnvelope with objective: ROLLBACK-P4 to Commander"
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
### Phase: 4 — Connect (Force-Directed Graph + Convergence)
### Primary Delta Enforcement: Delta 4 (on-device convergence), Delta 1 (Metal-accelerated Liquid Glass graph)

---

### Step 1: Create ConvergenceDetector Protocol + LocalConvergenceDetector

Create `Agendizer/Graph/ConvergenceDetector.swift`:

```swift
import Foundation
import NaturalLanguage

/// Protocol for detecting convergence edges between intentions.
protocol ConvergenceDetector {
    func computeEdges(for intentions: [Intention]) -> [Edge]
    var requiresNetwork: Bool { get }
}

/// On-device convergence computation using NaturalLanguage.framework.
/// NEVER sends data externally (Delta 4).
final class LocalConvergenceDetector: ConvergenceDetector {
    let requiresNetwork = false

    /// Minimum similarity for edge creation (0.0 to 1.0).
    private let edgeThreshold: Double = 0.6

    func computeEdges(for intentions: [Intention]) -> [Edge] {
        guard intentions.count >= 2 else { return [] }
        guard let embedding = NLEmbedding.sentenceEmbedding(for: .english)
              ?? NLEmbedding.wordEmbedding(for: .english) else { return [] }

        var edges: [Edge] = []

        for i in 0..<intentions.count {
            for j in (i+1)..<intentions.count {
                let distance = embedding.distance(
                    between: intentions[i].rawContent,
                    and: intentions[j].rawContent
                )
                let similarity = 1.0 - distance
                if similarity >= edgeThreshold {
                    let edge = Edge(
                        sourceID: intentions[i].id.uuidString,
                        targetID: intentions[j].id.uuidString,
                        edgeType: .convergence,
                        confidence: similarity,
                        attribution: .init(type: .system)
                    )
                    edges.append(edge)
                }
            }
        }

        return edges
    }
}
```

### Step 2: Create ForceDirectedGraph Engine

Create `Agendizer/Graph/ForceDirectedLayout.swift`:

```swift
import Foundation
import simd

/// Force-directed graph layout engine using velocity Verlet integration.
/// Runs on CPU; Metal rendering is separate (display layer only).
@Observable
final class ForceDirectedLayout {
    struct GraphNode: Identifiable {
        let id: UUID
        var position: SIMD2<Float>
        var velocity: SIMD2<Float> = .zero
        let intention: Intention
        var isEchoSupernode: Bool = false
        var echoCluster: EchoCluster? = nil
    }

    struct GraphEdge: Identifiable {
        let id: UUID
        let sourceID: UUID
        let targetID: UUID
        let confidence: Double
        let edgeType: EdgeType
    }

    var nodes: [GraphNode] = []
    var edges: [GraphEdge] = []
    var selectedNodeID: UUID? = nil

    // Physics constants
    private let repulsionStrength: Float = 500.0
    private let attractionStrength: Float = 0.01
    private let damping: Float = 0.9
    private let idealEdgeLength: Float = 150.0

    func populate(intentions: [Intention], edges: [Edge], echoClusters: [EchoCluster]) {
        // Create nodes with random initial positions
        self.nodes = intentions.map { intention in
            GraphNode(
                id: intention.id,
                position: SIMD2<Float>(
                    Float.random(in: -300...300),
                    Float.random(in: -300...300)
                ),
                intention: intention
            )
        }

        // Mark echo supernodes
        for cluster in echoClusters {
            for intention in cluster.intentions {
                if let idx = self.nodes.firstIndex(where: { $0.id == intention.id }) {
                    self.nodes[idx].isEchoSupernode = true
                    self.nodes[idx].echoCluster = cluster
                }
            }
        }

        // Create graph edges
        self.edges = edges.map { edge in
            GraphEdge(
                id: edge.id,
                sourceID: UUID(uuidString: edge.sourceID) ?? UUID(),
                targetID: UUID(uuidString: edge.targetID) ?? UUID(),
                confidence: edge.confidence,
                edgeType: edge.edgeType
            )
        }
    }

    func step() {
        guard nodes.count >= 2 else { return }

        // Repulsion between all node pairs
        for i in 0..<nodes.count {
            for j in (i+1)..<nodes.count {
                let delta = nodes[i].position - nodes[j].position
                let dist = max(simd_length(delta), 1.0)
                let force = repulsionStrength / (dist * dist)
                let direction = delta / dist
                nodes[i].velocity += direction * force
                nodes[j].velocity -= direction * force
            }
        }

        // Attraction along edges
        for edge in edges {
            guard let srcIdx = nodes.firstIndex(where: { $0.id == edge.sourceID }),
                  let tgtIdx = nodes.firstIndex(where: { $0.id == edge.targetID }) else { continue }
            let delta = nodes[tgtIdx].position - nodes[srcIdx].position
            let dist = simd_length(delta)
            let force = attractionStrength * (dist - idealEdgeLength)
            let direction = delta / max(dist, 1.0)
            nodes[srcIdx].velocity += direction * force
            nodes[tgtIdx].velocity -= direction * force
        }

        // Apply velocity with damping
        for i in 0..<nodes.count {
            nodes[i].velocity *= damping
            nodes[i].position += nodes[i].velocity
        }
    }
}
```

### Step 3: Create ConnectView (L3) with Metal Rendering

Create `Agendizer/Views/ConnectView.swift`:

```swift
import SwiftUI
import SwiftData
import MetalKit

/// L3 Connect — Force-directed graph of Intentions, Edges, and Echo supernodes.
/// Uses Metal for GPU-accelerated rendering (Delta 1).
struct ConnectView: View {
    @Query private var intentions: [Intention]
    @State private var layout = ForceDirectedLayout()
    @State private var convergenceDetector = LocalConvergenceDetector()
    @State private var echoDetector = LocalEchoDetector()
    @State private var scale: CGFloat = 1.0
    @State private var offset: CGSize = .zero
    @State private var isInitialized = false

    var body: some View {
        ZStack {
            // Graph canvas — Metal-accelerated
            GraphMetalView(layout: layout)
                .gesture(magnifyGesture)
                .gesture(dragGesture)

            // Selected node detail overlay
            if let selectedID = layout.selectedNodeID,
               let node = layout.nodes.first(where: { $0.id == selectedID }) {
                NodeDetailPanel(node: node)
                    .frame(maxWidth: 320)
                    .glassEffect()
                    .transition(.move(edge: .trailing))
            }
        }
        .task {
            guard !isInitialized else { return }
            let echoes = echoDetector.detectEchoes(in: intentions)
            let edges = convergenceDetector.computeEdges(for: intentions)
            layout.populate(intentions: intentions, edges: edges, echoClusters: echoes)
            isInitialized = true
        }
    }

    private var magnifyGesture: some Gesture {
        MagnifyGesture()
            .onChanged { value in
                scale = value.magnification
            }
    }

    private var dragGesture: some Gesture {
        DragGesture()
            .onChanged { value in
                offset = value.translation
            }
    }
}

/// Metal-backed graph renderer.
/// If Metal is unavailable, falls back to SwiftUI Canvas.
struct GraphMetalView: NSViewRepresentable {
    @Bindable var layout: ForceDirectedLayout

    func makeNSView(context: Context) -> MTKView {
        let view = MTKView()
        view.device = MTLCreateSystemDefaultDevice()
        view.clearColor = MTLClearColor(red: 0, green: 0, blue: 0, alpha: 0)
        view.isOpaque = false
        view.delegate = context.coordinator
        view.preferredFramesPerSecond = 60
        view.enableSetNeedsDisplay = false
        return view
    }

    func updateNSView(_ nsView: MTKView, context: Context) {
        context.coordinator.layout = layout
    }

    func makeCoordinator() -> GraphMetalCoordinator {
        GraphMetalCoordinator(layout: layout)
    }
}

/// Metal rendering coordinator — handles draw calls.
/// Implement node circles, edge lines, echo supernode highlights.
final class GraphMetalCoordinator: NSObject, MTKViewDelegate {
    var layout: ForceDirectedLayout

    init(layout: ForceDirectedLayout) {
        self.layout = layout
        super.init()
    }

    func mtkView(_ view: MTKView, drawableSizeWillChange size: CGSize) {}

    func draw(in view: MTKView) {
        // Step physics simulation
        layout.step()

        // Metal rendering:
        // 1. Draw edges as lines with alpha = confidence
        // 2. Draw nodes as circles (amber for echo supernodes, blue for regular)
        // 3. Highlight selected node
        guard let drawable = view.currentDrawable,
              let descriptor = view.currentRenderPassDescriptor,
              let commandQueue = view.device?.makeCommandQueue(),
              let commandBuffer = commandQueue.makeCommandBuffer(),
              let encoder = commandBuffer.makeRenderCommandEncoder(descriptor: descriptor) else { return }

        // TODO: Implement Metal shader pipeline for node/edge rendering
        // For MVP: use basic vertex/fragment shaders with instance rendering
        // Nodes: instanced quads with circle SDF
        // Edges: line primitives with confidence-based alpha

        encoder.endEncoding()
        commandBuffer.present(drawable)
        commandBuffer.commit()
    }
}

/// Detail panel shown when a graph node is selected.
struct NodeDetailPanel: View {
    let node: ForceDirectedLayout.GraphNode

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text(node.intention.rawContent)
                .font(.body)
                .lineLimit(5)

            Divider()

            Text("Stage: \(node.intention.stage.rawValue)")
                .font(.caption)
                .foregroundStyle(.secondary)

            if node.isEchoSupernode, let cluster = node.echoCluster {
                HStack {
                    Image(systemName: "waveform.path.ecg")
                        .foregroundStyle(Color(hex: 0xD87001))
                    Text("Echo cluster: \(cluster.frequency)× \(cluster.trajectory.rawValue)")
                        .font(.caption)
                }
            }

            Text("\(node.intention.stateTransitions.count) transitions")
                .font(.caption2)
                .foregroundStyle(.tertiary)
        }
        .padding()
    }
}
```

**Important Metal notes**:
- The Metal shader pipeline (vertex/fragment shaders) needs implementation. If full Metal shader authoring is blocked by time, implement a SwiftUI `Canvas` fallback that draws nodes as circles and edges as lines using CoreGraphics. The `GraphMetalView` wrapper should detect Metal availability and fall back.
- The physics simulation runs on CPU in `ForceDirectedLayout.step()` — this is fine for <= 1000 nodes. GPU compute kernels are a Phase 6 optimization if needed.

### Step 4: Update AppNavigationState for L3

Modify `Agendizer/Navigation/AppNavigationState.swift`:

- Change `DepthLayer.connect.isAvailable` to return `true`
- Set `keyboardShortcut` for `.connect` — use a custom approach since CMD+Shift+G needs shift modifier
- Add `toggleConnect()` method
- Keep `.dispatch.isAvailable == false`

```swift
var isAvailable: Bool {
    switch self {
    case .capture, .navigate, .ledger, .connect: return true  // L3 now available
    case .dispatch: return false                                // L4 still gated
    }
}
```

### Step 5: Wire CMD+Shift+G in AgendizerApp

Add to `AgendizerApp.swift` `CommandGroup`:

```swift
Button("Connect") {
    navigationState.toggleConnect()
}
.keyboardShortcut("g", modifiers: [.command, .shift])
```

### Step 6: Update ContentView for L3 Rendering

In `ContentView.swift`, add the `.connect` case:

```swift
switch navigationState.activeLayer {
case .capture:
    CaptureView()
case .navigate:
    NavigateView()
case .ledger:
    LedgerView()
case .connect:
    ConnectView()
default:
    CaptureView()
}
```

### Step 7: Write Tests

Add to `AgendizerTests/ConnectGraphTests.swift` (new file):

Required test cases:
1. `testConnectLayerNowAvailable` — `DepthLayer.connect.isAvailable == true`
2. `testDispatchLayerStillUnavailable` — `DepthLayer.dispatch.isAvailable == false`
3. `testToggleConnectChangesLayer` — CMD+Shift+G switches to L3
4. `testGoToCaptureFromConnect` — CMD+0 returns to L0 from L3
5. `testConvergenceDetectorDoesNotRequireNetwork` — `LocalConvergenceDetector().requiresNetwork == false`
6. `testConvergenceDetectorCreatesSimilarEdges` — Similar intentions produce edges with confidence >= threshold
7. `testConvergenceDetectorIgnoresDissimilarContent` — Dissimilar intentions produce no edges
8. `testForceDirectedLayoutPopulatesNodes` — Layout correctly creates nodes from intentions
9. `testForceDirectedLayoutMarksEchoSupernodes` — Echo cluster members marked as supernodes
10. `testForceDirectedLayoutPhysicsStep` — After step(), node positions change

### Step 8: Verify All Phase 0-3 Tests Still Pass

Run full test suite: `xcodebuild test`. All 24 existing tests must still pass alongside new connect/graph tests. Target: >= 30 total tests.

---

## Phase 0-3 Artifacts Available

These files exist and should be extended, not replaced:

- `Agendizer/Models/DomainModels.swift` — Edge model already exists; may need to add convergence edge type if not present
- `Agendizer/Navigation/AppNavigationState.swift` — Enable L3, add toggleConnect(), wire CMD+Shift+G
- `Agendizer/Views/ContentView.swift` — Add .connect case
- `Agendizer/Echoes/EchoDetector.swift` — LocalEchoDetector available for reuse in ConnectView
- `Agendizer/AgendizerApp.swift` — Add CMD+Shift+G command
- `AgendizerTests/NavigationTests.swift` — Update testFutureLayersNotAvailable to assert only L4

**Important**: `NavigationTests.testFutureLayersNotAvailable` currently asserts L3/L4 are unavailable. This test MUST be updated to assert only L4 is unavailable (L3 is now available). Do NOT break this test — update it.

---

## New Files Expected

| File | Purpose |
|---|---|
| `Agendizer/Graph/ConvergenceDetector.swift` | Convergence edge computation protocol + LocalConvergenceDetector |
| `Agendizer/Graph/ForceDirectedLayout.swift` | Physics-based graph layout engine |
| `Agendizer/Views/ConnectView.swift` | L3 force-directed graph view with Metal rendering |
| `AgendizerTests/ConnectGraphTests.swift` | Graph + convergence tests |

---

## Handoff Protocol

On completion, Adjudicator produces:
1. `ExecutionReceipt` per CONTRACT §2.3
2. `SwarmHandoffEnvelope` back to Commander for gate review
3. Result file to `-INBOX/commander/00-INBOX0/RESULT-adjudicator-YYYYMMDD-agendizer-phase4.md`
4. CONFIRM file to Commander's inbox (per DYN-DISPATCH_KANBAN_PROTOCOL v1.1.0)

---

**Priority**: P0
**Lane**: Adjudicator (Codex GPT-5.3)
**Deadline**: 2026-02-21T00:00:00Z
**Reply-To**: commander
