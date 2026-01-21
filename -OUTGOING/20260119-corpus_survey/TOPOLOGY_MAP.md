# Topology Map

**Date**: 2026-01-19

---

## Directory Overview

### Root Level
| Item | Type | Size | Purpose |
|------|------|------|---------|
| `CLAUDE.md` | File | 5.7K | Constitutional rules for Claude Code sessions |
| `COCKPIT.md` | File | 3.2K | System navigation index |
| `Makefile` | File | 2.8K | Build/verify commands |

### Numbered Zones (00-06)

#### 00-ORCHESTRATION (182 files, 1.9M)
**Role Hypothesis**: Strategic coordination center—directives, execution logs, system state, validation scripts.

| Subdirectory | Files | Contents |
|--------------|-------|----------|
| `blackboard/` | 4 | JSON artifacts (audits, evidence, executions, plans) |
| `directives/` | 56 | DIRECTIVE-NNN.md files defining work orders |
| `execution_logs/` | 56 | EXECUTION_LOG-YYYY-MM-DD-NNN.md completion records |
| `oracle_contexts/` | 5 | ORACLE[N]_CONTEXT.md thread state capsules |
| `schemas/` | 1 | packet_protocol.json |
| `scripts/` | 13 | Shell scripts, Python utilities |
| `state/` | 45 | REF-*, DYN-*, ARCH-* state documents |
| `templates/` | 1 | Template files |

**Key Files**:
- `state/system_state.json` — Current state vector
- `state/REF-STANDARDS.md` — 18 evaluative lenses
- `state/REF-BLITZKRIEG_PROTOCOL_VNEXT.md` — Multi-lane execution protocol
- `scripts/structural_verify.sh` — Constitutional compliance checker

#### 01-CANON (79 files, 2.8M)
**Role Hypothesis**: Protected canonical knowledge—CANON-NNNNN documents forming the permanent knowledge base.

**Contents**: CANON-00000 through CANON-40xxx series covering:
- Core schema (00000-00017)
- Core entities (10000-11000)
- Lattice structures (20000-25000)
- Domain knowledge (30000-40000)

**Naming Convention**: `CANON-NNNNN-TITLE-scope.md`

#### 02-OPERATIONAL (83 files, 992K)
**Role Hypothesis**: Working configurations—prompts, functions, model profiles, coordination specs.

| Subdirectory | Files | Contents |
|--------------|-------|----------|
| `functions/` | 26 | Processing function definitions |
| `models/` | 2 | Model index and profiles |
| `prompts/` | 17 | System prompts (canonical/, chatgpt/) |
| `registries/` | 3 | REF-* registries and taxonomies |
| `scripts/` | 3 | ops_lint.sh and utilities |
| `specs/` | 2 | REF-AUDIZER_PROTOCOL.md, REF-CHATGPT_MEMORY_POLICY.md |

**Key Files**:
- `coordination.yaml` — Platform constellation config
- `BLITZKRIEG_PROTOCOL.md` — Execution protocol
- `IIC-*-config.md` — Intelligence chain configurations (5 files)

#### 03-QUEUE (7 files, 92K)
**Role Hypothesis**: Pending work items organized by modal stage.

| Subdirectory | Files | Contents |
|--------------|-------|----------|
| `modal1/` | 3 | Current-stage queue items |
| `modal2/` | 3 | Future-stage queue items |

#### 04-SOURCES (279 files, 9.9M)
**Role Hypothesis**: Source document repository—raw inputs and processed outputs.

| Subdirectory | Files | Contents |
|--------------|-------|----------|
| `raw/` | 199 | Unprocessed source documents |
| `processed/` | 46 | Processed and tagged sources |

**Key Files**:
- `sources.csv` — Source tracking ledger
- `creator_bios.md` — Creator metadata
- `filename_mapping.csv` — Name normalization

#### 05-ARCHIVE (81 files, 1.0M)
**Role Hypothesis**: Historical preservation—superseded artifacts and reference material.

**Contents**: Archived directives, old state files, superseded documentation.

#### 06-EXEMPLA (5 files, 20K)
**Role Hypothesis**: Templates and examples for artifact creation.

**Contents**: Template files for various artifact types (continuation packets, etc.)

### Exchange Directories

#### -INBOX (9 files, 48K)
**Role Hypothesis**: Incoming artifacts from external platforms (ChatGPT, etc.)

**Contents**:
- `blitzkrieg_drop/` — Directives dropped from ChatGPT
- `chatgpt_*.md` — Memory/prompt artifacts from ChatGPT
- `smoketest_result.md` — Validation outputs

#### -OUTGOING (41 files, 1.4M)
**Role Hypothesis**: Export staging—bundles for external consumption, reinit capsules.

**Structure**:
- `YYYYMMDD-<slug>/` — Dated export bundles
- `*.zip` — Archived passes (teleology, defrag, ring7)
- `TURBINE_BAKEOFF_*` — Multi-model comparison artifacts

---

## File Counts by Extension

| Extension | Count | Percentage |
|-----------|-------|------------|
| `.md` | 577 | 73.6% |
| `.txt` | 119 | 15.2% |
| `.xml` | 20 | 2.6% |
| `.sh` | 13 | 1.7% |
| `.json` | 12 | 1.5% |
| `.zip` | 7 | 0.9% |
| `.yaml` | 7 | 0.9% |
| `.csv` | 7 | 0.9% |
| `.py` | 6 | 0.8% |
| Other | 16 | 2.0% |

---

## File Counts by Top-Level Directory

| Directory | Files | Size |
|-----------|-------|------|
| 00-ORCHESTRATION | 182 | 1.9M |
| 01-CANON | 79 | 2.8M |
| 02-OPERATIONAL | 83 | 992K |
| 03-QUEUE | 7 | 92K |
| 04-SOURCES | 279 | 9.9M |
| 05-ARCHIVE | 81 | 1.0M |
| 06-EXEMPLA | 5 | 20K |
| -INBOX | 9 | 48K |
| -OUTGOING | 41 | 1.4M |
| **Total** | **784** | ~18M |

---

## Cross-Check with DYN-TREE.md

The tree listing in `00-ORCHESTRATION/state/DYN-TREE.md` matches observed topology with the following notes:
- `-INBOX/` and `-OUTGOING/` correctly shown as root exceptions
- Zone directories 00-06 all present
- File counts consistent with observed state
