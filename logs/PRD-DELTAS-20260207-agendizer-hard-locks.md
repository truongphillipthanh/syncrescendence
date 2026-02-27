# PRD DELTA INSERT — Agendizer Hard Locks

**Locked**: 2026-02-07
**Authority**: Commander (Opus 4.6)
**Source**: RESULT-adjudicator-20260207-agendizer-clarescence2-substantiated.md §3 + CLARESCENCE-2026-02-06-agendizer-prd-reinforcement.md
**Status**: FROZEN — These deltas are non-negotiable for all implementation phases

---

## Five Hard Deltas (Apply to All Agendizer Execution)

### Delta 1: Apple-Native First-Party Quality Bar

**Mandate**: macOS-first MVP with SwiftUI and Apple design language fidelity. Liquid Glass applied where appropriate, content readability remains primary.

**Implementation locks**:
- Minimum deployment target: macOS 26 (Tahoe)
- SwiftUI lifecycle (`@main App`)
- `.glassEffect()` modifier on NavigationSplitView sidebar, toolbars, and overlays
- San Francisco system font exclusively — no font picker
- System-adaptive light/dark mode via `@Environment(\.colorScheme)`
- Accent color: warm amber/orange (#d87001) for intentional items; system blue for interactive elements
- Liquid Glass material on all chrome surfaces; opaque content areas for readability
- Visual benchmark is **Apple Notes**, not Notion

**Falsifier**: If HIG review would flag the app as non-native.

---

### Delta 2: Progressive Disclosure Depth Stack (Not Tab Sprawl)

**Mandate**: L0 Capture → L1 Navigate → L2 Ledger → L3 Connect → L4 Dispatch. Depth reveal is usage-driven; no forced multi-surface cognitive load.

**Implementation locks**:
- Five views are NOT tabs — they are depth layers
- L0 (Capture): Always one tap/shortcut away. Full-bleed text editor. Apple Notes simplicity.
- L1 (Navigate): Revealed by swipe/CMD+1. Three-column `NavigationSplitView`. Default home after onboarding week.
- L2 (Ledger): Discovered via project drill-down or CMD+2. Agenda-style timeline.
- L3 (Connect): Discovered via CMD+Shift+G or pinch-to-zoom. Force-directed graph with Metal rendering.
- L4 (Dispatch): Discovered only when MCP/A2A agent connection configured. CMD+D.
- Progressive reveal prompts: system suggests deeper layers after usage thresholds (3+ days → Ledger prompt; 2+ weeks with echoes → Connect prompt)
- Users can productively use Capture + Navigate for weeks without discovering deeper layers

**Falsifier**: If a new user encounters all five views in their first session.

---

### Delta 3: API Ports as Architectural Boundary

**Mandate**: MCP/A2A are explicit ports, not hidden feature glue. Core app remains useful without live external agent connection.

**Implementation locks**:
- MCP server: embedded, local Unix socket, not network-exposed by default
- MCP resources (read-only by default): `agendizer://intentions/`, `agendizer://projects/`, `agendizer://echoes/`, `agendizer://dispatch/`
- MCP tools (require authorization): `agendizer.capture()`, `agendizer.interpret()`, `agendizer.dispatch()`, `agendizer.resolve_echo()`
- A2A Agent Card: published at `/.well-known/agent-card.json` with capabilities array
- Protocol version posture:
  - MCP compatibility floor: `2025-06-18`
  - MCP current upstream: `2025-11-25`
  - A2A target: `v0.3.0`
  - A2A compatibility: `v0.2.x` `/.well-known/agent.json` during transition
- Dispatch Console (L4) is invisible until first agent connection configured
- App is 100% functional without any agent connection

**Falsifier**: If removing all agent connections degrades any core functionality.

---

### Delta 4: On-Device-By-Default with Explicit Cloud Escalation

**Mandate**: Interpretation, echoing, and convergence default local. Dispatch outward only on explicit authorization.

**Implementation locks**:
- `IntentionInterpreter` protocol with swappable backends:
  - `LocalInterpreter`: CoreML text classification for ontology routing
  - `CloudInterpreter`: MCP tool call to Claude/GPT (user-authorized, per-invocation)
- `EchoDetector`: NaturalLanguage.framework on-device embeddings — never sends data externally
- Convergence edge computation: on-device semantic similarity
- Voice capture: Speech.framework on-device Whisper — audio never leaves device
- Cloud AI: opt-in per invocation with clear UI indication (badge/icon showing "cloud" vs "device")
- Default is ALWAYS local. No silent cloud escalation.

**Falsifier**: If any core pipeline stage sends data externally without explicit user action.

---

### Delta 5: Auditability Sacrosanctity

**Mandate**: Immutable raw capture. Append-only transitions. Receipts for every state mutation.

**Implementation locks**:
- `Intention.rawContent` is `let` (immutable in Swift) — never mutated after creation
- `Intention.stateTransitions` is append-only `[StateTransition]` — no deletions, no edits to prior entries
- Every `StateTransition` records: timestamp, fromStage, toStage, actor (human/system/agent), rationale
- `DispatchPackage` includes `receipt_contract` specifying expected receipt format
- Every agent execution returns an `ExecutionReceipt` with: proof_of_run, files_touched, bench_or_test_outcome, model_surface_used, timestamp_utc
- Compaction operates on VIEWS (display summarization), never on the transition log
- Data export includes full transition history

**Falsifier**: If any historical state transition can be modified or deleted.

---

## Application Order

These deltas apply to every implementation phase (Phase 0-6). They are not aspirational — they are constitutional. Any implementation artifact that violates a delta is rejected at gate review.

| Phase | Primary Delta Enforcement |
|---|---|
| Phase 0 (Foundation) | Delta 5 (immutable rawContent, append-only transitions in SwiftData model) |
| Phase 1 (Interpretation) | Delta 4 (local-first interpreter protocol), Delta 5 (correction as StateTransition) |
| Phase 2 (Navigation) | Delta 2 (depth stack navigation, not tabs) |
| Phase 3 (Ledger) | Delta 5 (timeline from append-only log), Delta 4 (on-device echo detection) |
| Phase 4 (Connect) | Delta 4 (on-device convergence), Delta 1 (Metal-accelerated Liquid Glass graph) |
| Phase 5 (Dispatch) | Delta 3 (MCP/A2A as ports), Delta 5 (receipts for every dispatch) |
| Phase 6 (Polish) | Delta 1 (Liquid Glass throughout), Delta 2 (progressive reveal onboarding) |

---

**Gate C: PASS** — PRD deltas explicitly encode Apple-native Liquid Glass + progressive disclosure depth stack + macOS-first ergonomics.
