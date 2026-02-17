---
id: DEC-20260204-213941-native-swarms-substrate
kind: DECISION_ATOM
scope: substrate
status: provisional
updated: 2026-02-04
---

Decision ID: DEC-20260204-213941-native-swarms-substrate
Choice: Treat **platform-native swarms** as first-class execution substrate. Shift routing from “task → single model” toward “task → platform swarm profile,” with a normalized cross-swarm **handoff packet** and explicit **trust/approval gradients** for side effects.
Why (lens 1-2): Meet the Moment (native swarms proliferating across platforms), Potency Without Resolution Loss (use native power without locking in; normalize interface)
Falsifier: If native swarms remain inconsistent/unreliable across platforms, or cannot be constrained safely for external side effects, revert to external orchestration as primary and treat native swarms as optional accelerators.
Reversibility type: costly-reversible
Touched surfaces: CANON-31150 (platform capability catalog); routing matrices (model_db successor); dispatch packet schema; progressive trust policy
Evidence pointers: 00-ORCHESTRATION/state/impl/tooling/SWARM-SYNERGY-NOTE.md; D-026 backlog entry; Phillip directive re Sonnet 5 / Kimi K2.5

DecisionAtom: DEC-20260204-213941-native-swarms-substrate
IntentionLink: —
Fingerprint: 9e9b409
