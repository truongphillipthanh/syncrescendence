# Refactor Risk Ledger

**Date**: 2026-01-19

This document catalogs flattening risks discovered during the corpus survey.

---

## 1. Evidence That Should Remain Immutable

### 01-CANON/ (Protected Zone)

**Location**: `01-CANON/`
**Files**: 79 CANON-NNNNN documents

**Why It Matters**:
- Constitutional Rule #3 designates this a Protected Zone
- Contains verified canonical knowledge
- Modifications require explicit Principal approval

**Preservation Strategy**:
- Never auto-refactor CANON files
- Require manual review for any changes
- Maintain git history for all modifications

---

### Historical Archives in -OUTGOING/

**Location**: `-OUTGOING/*.zip`
**Files**: 7 zip archives (teleology, defrag, ring7, etc.)

**Why It Matters**:
- Contains point-in-time snapshots of system evolution
- Teleology passes document philosophical decisions
- Defrag passes document structural changes
- Bakeoff artifacts compare multi-model outputs

**Preservation Strategy**:
- Keep archives in `-OUTGOING/` or move to `05-ARCHIVE/`
- Never unzip and flatten into working tree
- Maintain as sealed capsules

---

### Execution Logs

**Location**: `00-ORCHESTRATION/execution_logs/`
**Files**: 56 EXECUTION_LOG-*.md files

**Why It Matters**:
- Provides audit trail of all directive executions
- Links directives to outcomes
- Critical for debugging and accountability

**Preservation Strategy**:
- Keep timestamped, never overwrite
- Archive old logs to `05-ARCHIVE/` if needed
- Maintain directive linkage

---

## 2. Tool-Specific Quirks

### ChatGPT Memory Synchronization

**Artifact**: `02-OPERATIONAL/prompts/chatgpt/PROMPT-CHATGPT-GLOBAL_MEMORY_REGISTRATION.md`

**Quirk**:
- ChatGPT's Saved Memory has strict formatting requirements
- Must be copy-paste friendly (no markdown fences around instructions)
- Memory updates require explicit user action in ChatGPT

**Risk if Normalized**:
- Breaking ChatGPT memory sync workflow
- Losing copy-paste-ready format

**Preservation Strategy**:
- Keep in dedicated `chatgpt/` subdirectory
- Test memory registration after any changes
- Document format requirements in file header

---

### Claude Code Command Structure

**Artifact**: `.claude/commands/project/*.md`

**Quirk**:
- Claude Code requires specific file location
- Commands must be at `.claude/commands/project/` (not configurable)
- Frontmatter format differs from ops_lint expectations

**Risk if Normalized**:
- Moving files breaks `/project:` command discovery
- Changing format breaks command parsing

**Preservation Strategy**:
- Never relocate command files
- Extend ops_lint to optionally validate command frontmatter
- Document location constraint in CLAUDE.md

---

### Ingestion Script Parsing Logic

**Artifact**: `00-ORCHESTRATION/scripts/ingest_chatgpt_container.py`

**Quirk**:
- Depends on exact marker strings (`===READABLE===`, `===DIRECTIVE_PACK===`)
- Regex patterns tuned for specific file name formats
- Currently still contains `===AUDIZABLE===` parsing (retired)

**Risk if Normalized**:
- Changing markers breaks ingestion
- Must update script before changing protocol docs

**Preservation Strategy**:
- Update script and docs atomically
- Test ingestion after any protocol changes
- Remove dead code (AUDIZABLE parsing) in cleanup pass

---

## 3. Intentional Duplication (Stratigraphy)

### Multiple Blitzkrieg Protocol Documents

**Locations**:
- `02-OPERATIONAL/BLITZKRIEG_PROTOCOL.md`
- `00-ORCHESTRATION/state/REF-BLITZKRIEG_PROTOCOL_VNEXT.md`

**Why This Duplication Exists**:
- `BLITZKRIEG_PROTOCOL.md` is the user-facing reference
- `REF-BLITZKRIEG_PROTOCOL_VNEXT.md` is the versioned spec
- Represents evolution from original to vNext

**Preservation Strategy**:
- Consolidate into single source OR
- Keep both with clear cross-references
- Document which is authoritative in COCKPIT.md

---

### IIC Config Files

**Location**: `02-OPERATIONAL/IIC-*-config.md`
**Files**: 5 files (Acumen, Coherence, Efficacy, Mastery, Transcendence)

**Why This Structure Exists**:
- Each file represents an Intelligence Information Chain stage
- Configurations are intentionally separate for stage-specific tuning
- Shared protocols in `IIC-shared-protocols.md`

**Preservation Strategy**:
- Keep as separate files (not duplication, but separation of concerns)
- Maintain shared protocols file for common elements
- Do not merge into single file

---

### Evidence Pack Copies in -OUTGOING/

**Observation**: Some reports exist in both:
- `-OUTGOING/20260118-codify_*/REF-REPO_VALIDATION_PROTOCOL.md`
- `00-ORCHESTRATION/state/REF-REPO_VALIDATION_PROTOCOL.md`

**Why This Exists**:
- `-OUTGOING/` copy is bundle artifact (export capsule)
- `00-ORCHESTRATION/state/` copy is canonical location
- Represents export vs source distinction

**Preservation Strategy**:
- Keep canonical in `00-ORCHESTRATION/state/`
- Keep bundle copies as export artifacts
- Do not deduplicate across these boundaries

---

## 4. Unknown-Unknown Notes

### .tmp.driveupload/ Contents

**Location**: `.tmp.driveupload/`
**Observation**: Contains partial file `14655.sb-6e8f0473-2l0Uk5` with audizable markers

**Risk**:
- Unknown purpose (appears to be Obsidian/Drive sync artifact)
- Contains legacy marker format
- May cause grep false positives

**Preservation Strategy**:
- Add to .gitignore if not already
- Exclude from validation scans
- Do not include in repo content

---

### Oracle Context Accumulation

**Location**: `00-ORCHESTRATION/oracle_contexts/`
**Files**: ORACLE9-12_CONTEXT.md + current ORACLE12_CONTEXT.md at parent

**Risk**:
- Oracle contexts grow over time
- May accumulate stale state
- Current ORACLE12_CONTEXT.md at parent level (not in oracle_contexts/)

**Preservation Strategy**:
- Consolidate ORACLE contexts into `oracle_contexts/`
- Archive old contexts after session ends
- Document context lifecycle

---

### Sources CSV State

**Location**: `04-SOURCES/sources.csv`
**Size**: 54K (significant ledger)

**Risk**:
- Critical ground truth for source tracking
- Partial updates could corrupt state
- Referenced by multiple processes

**Preservation Strategy**:
- Atomic updates only (temp file → validate → rename)
- Never batch-edit without validation
- Maintain backup before major operations

---

## Risk Summary Table

| Risk Category | Location | Severity | Preservation Action |
|---------------|----------|----------|---------------------|
| Immutable evidence | 01-CANON/ | High | Never auto-refactor |
| Immutable evidence | -OUTGOING/*.zip | Medium | Keep as sealed capsules |
| Immutable evidence | execution_logs/ | Medium | Never overwrite |
| Tool quirk | chatgpt/ prompts | Medium | Test after changes |
| Tool quirk | .claude/commands/ | High | Never relocate |
| Tool quirk | ingest script | Medium | Update atomically |
| Intentional stratigraphy | BLITZKRIEG docs | Low | Consolidate or cross-ref |
| Intentional stratigraphy | IIC configs | Low | Keep separate |
| Intentional stratigraphy | -OUTGOING copies | Low | Distinguish export vs source |
| Unknown-unknown | .tmp.driveupload/ | Low | Exclude from scans |
| Unknown-unknown | Oracle contexts | Medium | Consolidate locations |
| Unknown-unknown | sources.csv | High | Atomic updates only |

---

## Pre-Refactor Checklist

Before any flattening or normalization:

- [ ] Back up 01-CANON/ (even though protected)
- [ ] Verify all archives in -OUTGOING/ are sealed
- [ ] Snapshot execution_logs/ state
- [ ] Test ChatGPT memory sync workflow
- [ ] Verify .claude/commands/ discovery works
- [ ] Test ingest script with sample input
- [ ] Document current BLITZKRIEG doc relationship
- [ ] Verify IIC config separation is intentional
- [ ] Confirm .tmp.* in .gitignore
- [ ] Consolidate Oracle contexts
- [ ] Back up sources.csv
