---
id: DEC-20260204-213941-compaction-policy
kind: DECISION_ATOM
scope: substrate
status: provisional
updated: 2026-02-04
---

Decision ID: DEC-20260204-213941-compaction-policy
Choice: Pre-compaction hook policy becomes **BLOCKING** for dirty work in critical directories: if there are uncommitted changes or untracked files under `00-ORCHESTRATION/state/`, `02-ENGINE/`, `05-SIGMA/`, compaction must fail fast (non-zero) unless an explicit override flag is set.
Why (lens 1-2): Antifragile (prevent silent loss / incoherent archives), Repo Sovereignty (archives must reflect committed state)
Falsifier: If blocking compaction measurably harms workflow (e.g., compaction is routinely needed during exploratory sessions), switch to WARN-only but require an explicit compaction receipt capturing dirty state.
Reversibility type: reversible
Touched surfaces: 00-ORCHESTRATION/scripts/pre_compaction.sh; 00-ORCHESTRATION/scripts/compact_wisdom.sh; any hook wiring
Evidence pointers: pre_compaction.sh (currently warn-only); compact_wisdom.sh (moves staging → archive)

DecisionAtom: DEC-20260204-213941-compaction-policy
IntentionLink: —
Fingerprint: 9e9b409
