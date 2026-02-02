# 00-ORCHESTRATION

Strategic coordination infrastructure. Contains live state, operational scripts, and historical archive.

## Directory Structure

### state/ (21 files) — PROTECTED ZONE
Active ledgers, references, and architectural documents. Deletions require Sovereign approval.

**Prefix conventions**:
- `DYN-*` — Dynamic state (changes frequently, updated by automation)
- `REF-*` — Reference protocols (stable, rarely changes)
- `ARCH-*` — Architectural documents (active design/principles)

**Key files**:
- `DYN-BACKLOG.md` — Operational backlog and project status
- `DYN-TASKS.csv` — Task ledger (ground truth)
- `DYN-PROJECTS.csv` — Project tracking
- `DYN-TWIN_COORDINATION_PROTOCOL.md` — OpenClaw agent coordination
- `ARCH-INTENTION_COMPASS.md` — Destination alignment (20 intention entries)
- `ARCH-SOVEREIGNTY_STRATA.md` — σ₀–σ₇ sovereignty layers
- `REF-STANDARDS.md` — 18 evaluative lenses
- `REF-PROCESSING_PATTERN.md` — Source processing workflow
- `REF-NEO_BLITZKRIEG_BUILDOUT.md` — Current execution pipeline

### scripts/ (28 files) — Operational Tooling
Active automation scripts, hook scripts, and SN system.

**Categories**:
- **Hooks** (5): session_log, ajna_pedigree, create_execution_log, pre_compaction, intent_compass
- **SN System** (6): sn_encode/decode/expand.py, smart_convert.py, sn_symbols.yaml, SN_BLOCK_TEMPLATES.md
- **Dispatch** (3): dispatch.sh, dispatch_to_psyche.sh, watch_dispatch.sh
- **Verification** (2): verify_all.sh, ops_lint.sh
- **Utilities** (6): compact_wisdom.sh, create_directive.sh, regenerate_canon.py, sync_ledgers.py, create_gdrive_pointers.py, corpus-survey.sh
- **Config/Reference** (3): GEMINI-CORPUS-SENSING-PROMPT.md, hazel_rules.yaml, km_macros.yaml
- **Ingest** (3): ingest_chatgpt_container.sh/.py, setup-worktrees.sh

### archive/ (9 files) — Historical Record
Compacted directives, execution logs, Oracle contexts, and design decisions. Cold storage — not loaded by default.

**Key compendiums**:
- `ARCH-DIRECTIVE_COMPENDIUM.md` — 60+ directives compressed into one
- `ARCH-EXECUTION_HISTORY.md` — 60+ execution logs compressed into one
- `ARCH-ORACLE_GENEALOGY.md` — Oracle 0-13 arc, patterns, key decisions
- `ARCH-DESIGN_DECISIONS_GENESIS.md` — Three-tier structure, architectural experiments

## Audit Log

| Date | Action | Files | Details |
|------|--------|-------|---------|
| 2026-02-02 | Ultimate annealment | ~30→~26 | Scripts cleanup (4 deleted), Makefile stale targets removed, 12 broken cross-refs fixed |
| 2026-02-01 | State/archive anneal | 77→30 | state/ 24→21, archive/ 53→9 (83% compaction), 2 new compendiums created |
| 2026-02-01 | Deep audit | 142→110 | 29 deleted, 13 moved state/→archive/, stale paths fixed |
| 2026-01-26 | Phase 3 compaction | ~260→127 | Directives + logs compressed, subdirs merged |
| 2026-01-22 | Initial restructure | — | Created from wholesale restructure |
