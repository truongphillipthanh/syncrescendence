# TASK — Agendizer Phase 4: Connect

**Status**: COMPLETE
**Priority**: P0
**Exit-Code**: 0
**Completed-At**: 2026-02-07T08:57:31Z
**Claimed-At**: 2026-02-07T08:57:30Z
**Claimed-By**: adjudicator-M1-Mac-mini
**Kanban**: DONE
**From**: Commander (Opus 4.6)
**To**: Adjudicator (Codex GPT-5.3)
**Reply-To**: commander
**CC**: commander
**Created**: 2026-02-07
**Deadline**: 2026-02-21T00:00:00Z

---

## Objective

Implement Phase 4 (Connect) of the Agendizer Blitzkrieg: L3 Connect depth layer with force-directed graph visualization using Metal rendering, on-device convergence edge computation via NaturalLanguage.framework, and echo-to-graph supernode integration.

## Dispatch Package

Full execution brief with code scaffolds, gates, and step-by-step instructions:

**`orchestration/state/impl/DISPATCH-20260207-agendizer-phase4-adjudicator.md`**

## Prior Gate Reviews

- Phase 0: APPROVED (ER-20260207-AGZ-GATE-P0-001)
- Phase 1: APPROVED (ER-20260207-AGZ-GATE-P1-001)
- Phase 2: APPROVED (ER-20260207-AGZ-GATE-P2-001)
- Phase 3: APPROVED (ER-20260207-AGZ-GATE-P3-001)

## Primary Delta Enforcement

- **Delta 4**: ConvergenceDetector uses NaturalLanguage.framework on-device semantic similarity. Never sends data externally.
- **Delta 1**: Metal-accelerated Liquid Glass graph rendering. GPU-accelerated node/edge drawing.

## Gates (8 total)

P4-G1 through P4-G8. See dispatch package for full criteria.

## Critical Notes

1. `NavigationTests.testFutureLayersNotAvailable` currently asserts L3/L4 are unavailable. **Update this test** to assert only L4 is unavailable (L3 is now available). Do not break existing tests.
2. If full Metal shader pipeline is blocked by complexity, implement a SwiftUI `Canvas` fallback with CoreGraphics rendering. The key constraint is that the architecture supports Metal — the shaders can be refined in Phase 6 Polish.
3. `EdgeType.convergence` may need to be added to the enum in `DomainModels.swift` if not already present.

## Expected Deliverables

1. `ExecutionReceipt` per CONTRACT §2.3
2. `SwarmHandoffEnvelope` to Commander for Phase 5 authorization
3. `RESULT-adjudicator-YYYYMMDD-agendizer-phase4.md` to `-INBOX/commander/00-INBOX0/`
4. `CONFIRM-adjudicator-YYYYMMDD-agendizer-phase4-connect.md` to `-INBOX/commander/00-INBOX0/`
