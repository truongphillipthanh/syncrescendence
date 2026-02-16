# CAPABILITY MATRIX — Twin-Swarm Routing Substrate

**Locked**: 2026-02-07
**Authority**: Commander (Opus 4.6) + Adjudicator (Codex GPT-5.3)
**Source**: RESULT-adjudicator-20260207-agendizer-clarescence2-substantiated.md §2
**Status**: FROZEN — Routing decisions reference this table

---

## Truth Surface: GPT-5.3 Codex vs Opus 4.6

| Axis | GPT-5.3-Codex / Codex App | Opus 4.6 / Claude Code | Operational Implication |
|---|---|---|---|
| Orchestration model | Parallel tasks in isolated environments; project-level organization; Agents SDK orchestration primitives | Agent Teams in Claude Code with shared task lists and teammate messaging | Treat both as swarm-capable; choose leader by lane objective |
| Parallelism | Native multi-task parallel coding surfaces | Native multi-agent team workflows | Run dual-lane execution with deterministic ownership boundaries |
| Context behavior | Model-specific context strategy; SDK traces for orchestration observability | 1M context (beta) + context compaction (beta) | Use Opus for deep long-context synthesis; Codex for wide execution throughput |
| Tool/runtime integration | Codex app + OpenAI platform SDK surfaces | Claude Code + Claude Agent surfaces | Standardize handoff envelope, not tool-specific prompt chains |
| Xcode pathway | Integrated in Xcode 26.3 | Integrated in Xcode 26.3 | Apple-native app work can run in either surface with parity checkpoints |
| Safety/controls | Agents SDK guardrails/handoffs/traces | Team coordination controls and policy layers | Require receipts and gates independent of provider |
| Availability constraints | Feature rollout and plan gating by account/surface | 1M context and teams may be plan/beta constrained | Define fallback scenarios before launch |

---

## Lane Assignment (Deterministic)

### Commander Lane (Opus 4.6)
- **Strengths**: Long-context synthesis (1M tokens), architecture judgments, doctrine/gate decisions
- **Assigned**: Architecture decisions, PRD refinement, evidence evaluation, gate enforcement, final integration verification
- **Agendizer scope**: Data model design review, progressive disclosure architecture, MCP/A2A port design, convergence graph topology, quality gate adjudication

### Adjudicator Lane (Codex GPT-5.3)
- **Strengths**: Parallel implementation decomposition, execution packaging, deterministic artifact production
- **Assigned**: Xcode project scaffolding, SwiftData model implementation, SwiftUI view construction, test suite generation, CI/CD pipeline
- **Agendizer scope**: Phase 0-6 implementation execution, file-by-file build plan, unit tests, integration tests, Metal rendering setup

### Shared Boundary
- Communication exclusively via `SwarmHandoffEnvelope`
- No free-form lane bleed
- Every handoff produces an `ExecutionReceipt`

---

## Fallback Scenarios

| Scenario | Condition | Response |
|---|---|---|
| A (Nominal) | Claude Teams stable, Codex app stable | Full twin-swarm mode |
| B (Claude degraded) | Claude Teams unavailable/unstable | Commander single-lead with bounded subagents/worktrees |
| C (Codex degraded) | Codex app constraints | Continue via CLI lane with same envelope and receipts |
| D (Both degraded) | Feature gating blocks both | Single-agent sequential execution, Commander primary |

**Current posture**: Scenario A (nominal). Both platforms operational as of 2026-02-07.

---

**Gate B: PASS** — Capability matrix resolves OpenAI/Anthropic/Apple convergence without contradictions.
