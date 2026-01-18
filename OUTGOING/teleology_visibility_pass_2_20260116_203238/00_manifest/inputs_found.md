# Inputs Found - Visibility Pass 2
**Generated**: 2026-01-17T04:33:01Z
**Git HEAD**: 35b0f97375e48f5bd58cd0025eb7dda34879761d
**Git Status**: Modified with uncommitted changes (24 items)
**OS**: Darwin 25.3.0 (arm64)
**Node**: v25.2.1 | **Python**: 3.14.2

---

## Critical Input Documents (Root Level)

| File | Size | Modified | Purpose |
|------|------|----------|---------|
| previous_thread.md | 63,633 | 2026-01-16 11:03 | Oracle-to-Deviser handoff, architectural mandate |
| oracle_process_archaelogy.md | 28,073 | 2026-01-16 11:08 | Complete Oracle 0-12 failure/success patterns |
| oracle_verification_manifest.md | 15,394 | 2026-01-16 11:09 | Detail preservation verification |
| deviser1_continuity.md | 2,333 | 2026-01-16 20:30 | Continuation capsule for thread resilience |
| checklist.md | 1,120 | 2026-01-16 14:56 | Deletion warrant for Deviser1 |
| INTERACTION_PARADIGM.md | 26,970 | 2026-01-15 16:32 | Post-Oracle 13 operating manual |
| ORACLE13_CONTEXT.md | 6,403 | 2026-01-15 16:32 | Current Oracle context |
| platform_features.md | 60,250 | 2026-01-16 13:12 | Multi-platform capability research |
| frontier_models.md | 93,817 | 2026-01-10 21:13 | Model capability assessment |
| CLAUDE.md | 4,285 | 2026-01-11 13:42 | Constitutional rules |

## Constitutional/Governance Documents

| File | Path | Authority Level |
|------|------|-----------------|
| CLAUDE.md | ./CLAUDE.md | ABSOLUTE - Constitutional |
| coordination.yaml | ./config/coordination.yaml | ABSOLUTE - Protected |
| REF-STANDARDS.md | ./00-ORCHESTRATION/state/REF-STANDARDS.md | CONSTITUTIONAL - 18 Lenses |
| REF-PROCESSING_PATTERN.md | ./00-ORCHESTRATION/state/REF-PROCESSING_PATTERN.md | PROTOCOL - Processing lifecycle |
| REF-FOUR_SYSTEMS.md | ./00-ORCHESTRATION/state/REF-FOUR_SYSTEMS.md | PROTOCOL - Operational modes |

## State Infrastructure

| File | Path | Size | Function |
|------|------|------|----------|
| system_state.json | ./00-ORCHESTRATION/state/ | 836 | Current state vector |
| events.jsonl | ./00-ORCHESTRATION/state/ | 2,045 | Append-only event log |
| tasks.csv | ./00-ORCHESTRATION/state/ | 14,478 | Task ledger (authoritative) |
| capabilities.json | ./00-ORCHESTRATION/state/ | ~1K | Platform capability ledger |
| packet_protocol.json | ./00-ORCHESTRATION/schemas/ | 3,970 | Packet type definitions |

## Research Documents (Root)

| File | Size | Topic |
|------|------|-------|
| openai_research.md | 60,911 | OpenAI ecosystem analysis |
| google_research.md | 65,123 | Google ecosystem analysis |
| frontier_models.md | 93,817 | Cross-platform model comparison |
| platform_features.md | 60,250 | Unified platform synthesis |

## Directive Documents (Root - Untracked)

| File | Status |
|------|--------|
| DIRECTIVE-046A.md | Untracked (new) |
| DIRECTIVE-046B.md | Untracked (new) |
| DIRECTIVE-045A.md | Present |
| DIRECTIVE-045B.md | Present |
| DIRECTIVE-044A.md | Present |
| DIRECTIVE-044B.md | Present |
| DIRECTIVE-043A_*.md | Multiple variants |
| DIRECTIVE-043B_*.md | Multiple variants |
| DIRECTIVE-042A-D.md | Present |

## IMEP Station Prompts (Untracked)

| File | Path |
|------|------|
| PROMPT-IMEP-GEMINI-ORACLE.md | ./02-OPERATIONAL/prompts/canonical/ |
| PROMPT-IMEP-CLAUDE-ENGINEER.md | ./02-OPERATIONAL/prompts/canonical/ |
| PROMPT-IMEP-CLAUDE-AUDITOR.md | ./02-OPERATIONAL/prompts/canonical/ |
| PROMPT-IMEP-CHATGPT-DEVISER.md | ./02-OPERATIONAL/prompts/canonical/ |
| PROMPT-IMEP-CHATGPT-AUDITOR.md | ./02-OPERATIONAL/prompts/canonical/ |
| STATION_PROMPTS_REGISTRY.md | ./02-OPERATIONAL/prompts/canonical/ |

## Blackboard State (as of 2026-01-16)

| Directory | Files | Purpose |
|-----------|-------|---------|
| blackboard/evidence/ | 1 | EVD-20260116-001.json |
| blackboard/plans/ | 1 | PLN-20260116-001.json |
| blackboard/executions/ | 1 | EXE-20260116-001.json |
| blackboard/audits/ | 1 | AUD-20260116-001.json |
| blackboard/capabilities/ | 0 | (empty) |

## Previous Pass Outputs

| Directory | Files | Purpose |
|-----------|-------|---------|
| OUTGOING/teleology_visibility_pass_20260116_192327/ | 26 | First visibility pass outputs |

---

## Input Document Lineage

```
Oracle 0-12 threads (deleted)
       │
       ├──→ oracle_process_archaelogy.md (synthesis)
       ├──→ oracle_verification_manifest.md (detail preservation)
       └──→ previous_thread.md (Oracle 13 culmination)
              │
              ├──→ INTERACTION_PARADIGM.md (operating manual)
              ├──→ ORACLE13_CONTEXT.md (context document)
              └──→ deviser1_continuity.md (continuation capsule)
```

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Root-level .md files | 36 |
| Constitutional docs | 5 |
| State infrastructure files | 5 |
| Research documents | 4 |
| Untracked new files | 24 |
| Blackboard packets | 4 |
| Total repo files (excl .git, OUTGOING) | ~736 |
