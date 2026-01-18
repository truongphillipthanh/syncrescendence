# Strata Schema
## Classification System for Repository Contents
**Generated**: 2026-01-17

---

## I. STRATA DEFINITIONS

### Stratum 1: CONSTITUTIONAL CANON (Protected)
**Location**: `01-CANON/`
**Mutability**: Requires Principal approval for any change
**Purpose**: Verified canonical knowledge; the "deep wells"
**Characteristics**:
- Documents that govern the system
- Validated through 18-lens evaluation
- Append-friendly, edit-hostile
- Never temporal content

**Identification**: Files in `01-CANON/` matching `CANON-*.md`

---

### Stratum 2: ORCHESTRATION/PROTOCOLS (Semi-Protected)
**Location**: `00-ORCHESTRATION/state/REF-*`, `00-ORCHESTRATION/state/ARCH-*`
**Mutability**: Deliberate updates only; append-only for ARCH-
**Purpose**: Reference protocols and archaeological records
**Characteristics**:
- REF-: Stable methodologies and standards
- ARCH-: Frozen historical decisions
- Define how work is done
- Changes require justification

**Identification**:
- `00-ORCHESTRATION/state/REF-*.md`
- `00-ORCHESTRATION/state/ARCH-*.md`

---

### Stratum 3: OPERATIONAL WORKING SET (High Churn)
**Location**: `00-ORCHESTRATION/state/DYN-*`, ledgers, directives, execution logs
**Mutability**: High; changes frequently
**Purpose**: Current state tracking and execution records
**Characteristics**:
- DYN-: Real-time dashboards and backlogs
- Ledgers (*.csv): Task and project tracking
- Directives: Active execution instructions
- Execution logs: Work records

**Identification**:
- `00-ORCHESTRATION/state/DYN-*.md`
- `00-ORCHESTRATION/state/*.csv`
- `00-ORCHESTRATION/directives/DIRECTIVE-*.md`
- `00-ORCHESTRATION/execution_logs/EXECUTION_LOG-*.md`
- `00-ORCHESTRATION/blackboard/*`

---

### Stratum 4: OPERATIONAL RESOURCES
**Location**: `02-OPERATIONAL/`, `config/`
**Mutability**: Medium; changed when tools/processes change
**Purpose**: Functions, prompts, model profiles, configuration
**Characteristics**:
- Operational tooling
- Not constitutional
- Changes with platform evolution

**Identification**:
- `02-OPERATIONAL/functions/*.xml`, `*.md`
- `02-OPERATIONAL/prompts/**`
- `02-OPERATIONAL/models/**`
- `config/*`

---

### Stratum 5: SOURCES (Processing Pipeline)
**Location**: `04-SOURCES/`
**Mutability**: Append for raw/, transform to processed/
**Purpose**: Source documents in processing pipeline
**Characteristics**:
- raw/: Intake, never modified after creation
- processed/: Transformed with frontmatter
- filename_mapping.csv: Provenance tracking

**Identification**:
- `04-SOURCES/raw/*`
- `04-SOURCES/processed/*`

---

### Stratum 6: QUEUE (Pending Work)
**Location**: `03-QUEUE/`
**Mutability**: Items move to CANON or ARCHIVE when processed
**Purpose**: Pending items organized by modal
**Characteristics**:
- Temporary holding area
- Items graduate or are archived

**Identification**: `03-QUEUE/**`

---

### Stratum 7: ARCHIVE (Historical Preservation)
**Location**: `05-ARCHIVE/`
**Mutability**: Append-only; never deleted
**Purpose**: Historical records no longer actively used
**Characteristics**:
- Preserved for archaeology
- Not actively referenced
- May contain superseded content

**Identification**: `05-ARCHIVE/ARCH-*.md`, `05-ARCHIVE/SCAFF-*.md`

---

### Stratum 8: EXEMPLA (Templates)
**Location**: `06-EXEMPLA/`
**Mutability**: Low; templates are stable
**Purpose**: Templates and examples for reuse
**Characteristics**:
- Copy-and-adapt patterns
- Not constitutional

**Identification**: `06-EXEMPLA/*.md`

---

### Stratum 9: OUTGOING (Visibility Bundles)
**Location**: `OUTGOING/`
**Mutability**: Read-only after creation
**Purpose**: Generated visibility artifacts for external consumption
**Characteristics**:
- Teleology passes
- Defrag passes
- Time-stamped bundles
- May be zipped after review

**Identification**: `OUTGOING/TELEOLOGY*`, `OUTGOING/RING7*`, `OUTGOING/DEFRAG*`

---

### Stratum 10: ROOT ORPHANS (To Be Relocated)
**Location**: Repository root (not in 00-06 directories)
**Mutability**: Should be moved or deleted
**Purpose**: NONE — these are misplaced
**Characteristics**:
- Violate numbered directory principle
- Untracked or recently created
- Need triage and relocation

**Identification**: Files at root not matching expected patterns:
- `*.md` (except CLAUDE.md, Makefile, README.md)
- Directories not starting with `0[0-6]-`
- Temporary/working files

---

### Stratum 11: DETRITUS (To Be Removed)
**Location**: Various
**Mutability**: Should be deleted
**Purpose**: NONE — system artifacts
**Characteristics**:
- `.DS_Store` files
- `__MACOSX/` directories
- `*.bak.*` backup files
- `.tmp.*` temporary files
- Build artifacts

**Identification**:
- `.DS_Store`
- `*.bak.*`
- `.tmp*`
- `__MACOSX`

---

## II. STRATUM HIERARCHY

```
                    PROTECTED
                       ↑
┌─────────────────────────────────────────────────────┐
│ Stratum 1: CONSTITUTIONAL CANON                    │
│            01-CANON/                               │
├─────────────────────────────────────────────────────┤
│ Stratum 2: ORCHESTRATION/PROTOCOLS                 │
│            00-ORCHESTRATION/state/REF-, ARCH-      │
├─────────────────────────────────────────────────────┤
│ Stratum 3: OPERATIONAL WORKING SET                 │
│            DYN-*, ledgers, directives, logs        │
├─────────────────────────────────────────────────────┤
│ Stratum 4: OPERATIONAL RESOURCES                   │
│            02-OPERATIONAL/, config/                │
├─────────────────────────────────────────────────────┤
│ Stratum 5: SOURCES                                 │
│            04-SOURCES/                             │
├─────────────────────────────────────────────────────┤
│ Stratum 6: QUEUE                                   │
│            03-QUEUE/                               │
├─────────────────────────────────────────────────────┤
│ Stratum 7: ARCHIVE                                 │
│            05-ARCHIVE/                             │
├─────────────────────────────────────────────────────┤
│ Stratum 8: EXEMPLA                                 │
│            06-EXEMPLA/                             │
├─────────────────────────────────────────────────────┤
│ Stratum 9: OUTGOING                                │
│            OUTGOING/                               │
├─────────────────────────────────────────────────────┤
│ Stratum 10: ROOT ORPHANS (TO RELOCATE)             │
│             Root-level misplaced files             │
├─────────────────────────────────────────────────────┤
│ Stratum 11: DETRITUS (TO DELETE)                   │
│             .DS_Store, .tmp*, *.bak.*              │
└─────────────────────────────────────────────────────┘
                       ↓
                    EPHEMERAL
```

---

## III. DEFRAG ACTIONS BY STRATUM

| Stratum | Defrag Action |
|---------|---------------|
| 1 (Canon) | DO NOT TOUCH without Principal approval |
| 2 (Protocols) | Review for drift; propose patches |
| 3 (Working Set) | Update/clean; commit state |
| 4 (Resources) | Consolidate duplicates |
| 5 (Sources) | Process backlog; archive stale raw |
| 6 (Queue) | Process or archive |
| 7 (Archive) | Keep; append-only |
| 8 (Exempla) | Keep; update templates if needed |
| 9 (Outgoing) | Keep for reference; may zip old bundles |
| 10 (Orphans) | **RELOCATE** to proper location |
| 11 (Detritus) | **DELETE** |

---

## IV. STRATUM ASSIGNMENT HEURISTICS

```python
def assign_stratum(filepath):
    if filepath.startswith("01-CANON/"):
        return "CONSTITUTIONAL_CANON"
    elif filepath.startswith("00-ORCHESTRATION/state/REF-"):
        return "PROTOCOLS"
    elif filepath.startswith("00-ORCHESTRATION/state/ARCH-"):
        return "PROTOCOLS"
    elif filepath.startswith("00-ORCHESTRATION/state/DYN-"):
        return "WORKING_SET"
    elif filepath.startswith("00-ORCHESTRATION/state/") and filepath.endswith(".csv"):
        return "WORKING_SET"
    elif filepath.startswith("00-ORCHESTRATION/directives/"):
        return "WORKING_SET"
    elif filepath.startswith("00-ORCHESTRATION/execution_logs/"):
        return "WORKING_SET"
    elif filepath.startswith("00-ORCHESTRATION/blackboard/"):
        return "WORKING_SET"
    elif filepath.startswith("02-OPERATIONAL/"):
        return "RESOURCES"
    elif filepath.startswith("config/"):
        return "RESOURCES"
    elif filepath.startswith("04-SOURCES/"):
        return "SOURCES"
    elif filepath.startswith("03-QUEUE/"):
        return "QUEUE"
    elif filepath.startswith("05-ARCHIVE/"):
        return "ARCHIVE"
    elif filepath.startswith("06-EXEMPLA/"):
        return "EXEMPLA"
    elif filepath.startswith("OUTGOING/"):
        return "OUTGOING"
    elif ".DS_Store" in filepath or ".bak" in filepath or ".tmp" in filepath:
        return "DETRITUS"
    elif "/" not in filepath and filepath not in ["CLAUDE.md", "Makefile", "README.md"]:
        return "ROOT_ORPHAN"
    else:
        return "UNKNOWN"
```

---

## V. ROOT ORPHAN TRIAGE RULES

| File Pattern | Destination |
|--------------|-------------|
| `DIRECTIVE-*.md` | `00-ORCHESTRATION/directives/` |
| `ORACLE*_CONTEXT.md` | `00-ORCHESTRATION/oracle_contexts/` |
| `*_continuity.md` | `05-ARCHIVE/` or integrate |
| `*_memories.md` | `05-ARCHIVE/` or integrate |
| `previous_thread.md` | `05-ARCHIVE/` |
| `BLITZKRIEG_*.md` | `00-ORCHESTRATION/directives/` or `05-ARCHIVE/` |
| `DEEP_RESEARCH_*.md` | `04-SOURCES/raw/` or `05-ARCHIVE/` |
| `frontier_models.md` | `05-ARCHIVE/` (temporal) |
| `platform_features.md` | `05-ARCHIVE/` (temporal) |
| Research source dirs | `04-SOURCES/raw/` |
| `system_prompts/` | `02-OPERATIONAL/prompts/` or `05-ARCHIVE/` |

---

**Stratum assignment is the first step of principled defrag.**
