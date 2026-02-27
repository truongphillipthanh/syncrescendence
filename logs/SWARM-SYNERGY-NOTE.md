# Swarm Synergy Note (Platform-native swarms as first-class)

Context: Phillip notes imminent **Sonnet 5** + **Kimi K2.5** with built-in agentic swarm capabilities; expects swarm paradigm to proliferate. This shifts emphasis from "pick one orchestrator" to "wield each platform’s native swarms synergistically".

Generated: 2026-02-04

---

## Problem
Our current orchestration posture implicitly assumes:
- one primary executor agent per platform, and/or
- swarm = something we implement externally (MCP + scripts + worktrees).

If platforms ship robust native swarm/agentic runtimes, external orchestration must become:
- **inter-swarm coordination**, not intra-swarm implementation.

---

## Proposed reframe (normalization + mererologization)

### Normalization goal
Define a minimal, platform-agnostic set of normalized concepts:
- **Swarm**: a coordinated set of agents within one platform runtime.
- **Swarm capability profile**: what the native swarm can do (planning depth, tool reach, memory, parallelism, cost).
- **Handoff packet**: normalized request/response envelope crossing swarm boundaries.
- **Ledger event**: normalized lifecycle event (dispatch/claim/complete/fail/decision/compact).

### Mererologization goal
Define part–whole relationships:
- Platform
  - Swarm runtime (native)
    - Agents/roles
      - Tools/connectors
- Constellation
  - Multi-swarm choreography
    - Cross-swarm routing rules
    - Trust/approval gradients

---

## Immediate implications (interdependencies)

1) **CANON-31150 / platform catalog** must grow fields for:
   - native swarm support (yes/no + notes)
   - swarm limits (max agents, parallel tool calls, memory scope)

2) **DecisionAtom templates** should include “Swarm leverage” checks:
   - What is better done inside a platform-native swarm vs cross-swarm orchestration?

3) **Routing matrix** (model_db or successor) needs an additional axis:
   - task type → (platform swarm) rather than task type → (single model)

4) **Progressive trust** becomes critical:
   - some native swarms will be high-autonomy; require explicit guardrails for external side effects.

---

## Next step (decision)
Create a DecisionAtom:
- DECISION: "Native Swarms as First-Class Execution Substrate"
- Outcome: define the normalized swarm interface + required metadata in dispatch packets + routing policies.

