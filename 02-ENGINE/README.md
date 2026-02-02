# 02-ENGINE

Executable components: functions, prompts, protocols, model configurations, and platform identity. Flat structure with prefix conventions.

## Prefix Conventions (76 files)

| Prefix | Count | Purpose |
|--------|-------|---------|
| `FUNC-*` | 20 | Function metaprompts (XML/MD) — Three-phase workflow: Distill/Transform/Expand |
| `REF-*` | 11 | Reference protocols (stable operational docs) |
| `PROMPT-*` | 8 | Platform prompts — 4 canonical (v2.1) + 4 special-purpose |
| `AVATAR-*` | 6 | Platform identity configs (Pantheon v3) |
| `IIC-*` | 6 | Information Integration Constellation chain configs |
| `CAP-*` | 5 | Capability ontology definitions (YAML) |
| `DYN-*` | 5 | Dynamic operational data (CSV/JSON/YAML) |
| `TOOL-*` | 4 | Tool definitions (YAML) |
| `PROTO-*` | 2 | Platform onboarding protocols |
| `QUEUE-*` | 1 | Pending CANON candidates |
| `SURVEY-*` | 1 | Living AI ecosystem survey |
| `WF-*` | 1 | Workflow definitions |
| `MODEL-INDEX` | 1 | Model registry (pricing, capabilities, benchmarks) |
| `TEMPLATE-*` | 1 | Execution log template |
| `DEF-*` | 1 | Constellation variable definitions |
| Other | 3 | gemini-settings.json, MCP_SETUP.md, README.md |

## Key Files

- `FUNC-INDEX.md` — Function capability index (agentic-first membrane)
- `REF-ROSETTA_STONE.md` — Terminology reconciliation (living doc)
- `REF-FLEET_COMMANDERS_HANDBOOK.md` — Non-coding Claude Code operations
- `REF-STACK_TELEOLOGY.md` — Technology disposition tracker
- `MODEL-INDEX.md` — Model registry with pricing and benchmarks
- `WF-001-capture_dispatch_return.yaml` — Core workflow pattern

## Audit Log

| Date | Action | Files | Details |
|------|--------|-------|---------|
| 2026-02-01 | Deep audit | 114->76 | 32 deleted (8 stale REF-*, 8 unused FUNC-*, 8 PROMPT-UNIFIED-*, 6 MODEL-PROFILE stubs, 1 SURVEY, 1 empty dir), 6 QUEUE Modal 2 items moved to 04-SOURCES/research/, QUEUE-QUEUE double prefix fixed, FUNC-INDEX updated, stale cross-refs fixed |
| 2026-01-26 | Phase 4 flatten | ~130->114 | 15 subdirs eliminated, prefix system applied |
| 2026-01-22 | Initial restructure | -- | Created from wholesale restructure |
