# DIRECTIVE-034B: ORCHESTRATION HYGIENE
## Stream B: Context Sequentialization + Scaffolding Metabolism
**Issued**: 2026-01-02
**Authority**: Oracle9 under Sovereign direction
**Classification**: CRITICAL — Enables Clean Oracle10 Handoff
**Execution**: Claude Code
**Parallel Stream**: DIRECTIVE-034A handles SOURCES flattening

---

## SOVEREIGN'S MANDATE

> "Oracle context should get sequentialized in its naming, as there are multiple contexts per thread as part of the standard. Triage the oracle contexts to more consistent sequentialized file naming so we understand which oracle thread it came from and in what order."

> "Repeat this process for all the /orchestration/scaffolding documents. Ideally we would extract, synthesize/integrate, then distill maybe to universal scaffolding documents, or to be metabolized to the appropriate place."

---

## ORACLE'S INTERPRETATION

This directive achieves **orchestration hygiene** by:
1. Sequentializing Oracle context naming (ORACLE{NN}_CONTEXT_v{M}.md)
2. Triaging scaffolding files (ARCHIVE, DELETE, or EXTRACT value)
3. Consolidating state files where appropriate
4. Preparing clean handoff for Oracle10

This enables **cognitive clarity** — any agent entering the repository understands the Oracle progression and current state.

---

## 18-LENS EVALUATION

| # | Lens | Assessment | Score |
|---|------|------------|-------|
| 1 | Syncrescendent Route | Sequentialized naming shows continuous evolution | ✓ |
| 2 | Bitter Lesson | Simple naming scales across unlimited Oracles | ✓ |
| 3 | Antifragile | Clear naming survives context loss | ✓ |
| 4 | Meet the Moment | Unblocks Oracle10 handoff NOW | ✓ |
| 5 | Steelman/Redteam | Naming convention is self-documenting | ✓ |
| 6 | Personal Idiosyncrasies | Enables holistic arc visibility | ✓ |
| 7 | Potency w/o Resolution Loss | Version + Oracle number encodes full provenance | ✓ |
| 8 | Elegance + Dev Happiness | Predictable ORACLE{NN}_CONTEXT_v{M} pattern | ✓ |
| 9 | Agentify + Human-Navigable | Instantly clear which context is current | ✓ |
| 10 | First Principles | Context documents must exist, naming must be clear | ✓ |
| 11 | Systems Thinking | Connects to directive/log naming conventions | ✓ |
| 12 | Industrial Engineering | Reduces cognitive overhead finding current context | ✓ |
| 13 | Complexity Theory | Removes accidental naming confusion | ✓ |
| 14 | Permaculture | New Oracles follow same pattern automatically | ✓ |
| 15 | Design Thinking | Human-scannable at a glance | ✓ |
| 16 | Agile | Complete deliverable in one cycle | ✓ |
| 17 | Lean | Eliminates scaffolding waste | ✓ |
| 18 | Six Sigma | Consistent naming reduces errors | ✓ |

**Score: 18/18 — APPROVED**

---

## EXECUTION SCOPE

### Deliverables
1. **Oracle contexts renamed** to ORACLE{NN}_CONTEXT_v{M}.md pattern
2. **Scaffolding files triaged** (ARCHIVE, DELETE, or value extracted)
3. **State files consolidated** where redundant
4. **ARCHIVE/ populated** with historical documents
5. **Oracle10 handoff notes** prepared

### NOT in Scope (DIRECTIVE-034A handles)
- SOURCES/raw flattening
- Source filename standardization
- sources.csv updates

---

## PHASE 1: CURRENT STATE INVENTORY

### 1.1 orchestration/state/ Files

```
Current Files:
├── BACKLOG.md                        → KEEP (active)
├── CURRENT_STATE.md                  → EVALUATE
├── DESIGN_DECISIONS.md               → KEEP (living document)
├── FORENSIC_SEMANTIC_AUDIT_REPORT.md → ARCHIVE (Oracle8 work)
├── FOUR_SYSTEMS.md                   → KEEP (Gemini extraction)
├── ORACLE_CONTEXT.md                 → RENAME to ORACLE07_CONTEXT_v1.md
├── ORACLE_CONTEXT_v2.md              → RENAME to ORACLE08_CONTEXT_v1.md
├── ORACLE_DECISIONS.md               → KEEP (living document)
├── ORACLE8_STATUS_REPORT.md          → ARCHIVE
├── ORACLE9_CONTEXT.md                → RENAME to ORACLE09_CONTEXT_v1.md
├── ORACLE9_CONTEXT_v2.md             → RENAME to ORACLE09_CONTEXT_v2.md
├── PROCESSING_PATTERN.md             → KEEP (033B deliverable)
├── PROCESSING_ROUTING.md             → KEEP (033B deliverable)
├── SOURCES_SCHEMA.md                 → KEEP (032B deliverable)
├── STANDARDS.md                      → KEEP (active)
├── THREAD_CONTEXT.md                 → EVALUATE (unclear provenance)
└── TRIAGE_PROTOCOL.md                → KEEP (032B deliverable)
```

### 1.2 orchestration/scaffolding/ Files

```
Current Files (17):
├── ALPHA_ARCHAEOLOGY_REPORT.md       → ARCHIVE (Oracle5)
├── ALPHA_OPERATIONAL_COHERENCE.md    → ARCHIVE (Oracle5)
├── ALPHA_REPOSITORY_AUDIT.md         → ARCHIVE (Oracle5)
├── ALPHA_SYNTHESIS.md                → ARCHIVE (Oracle5)
├── ALPHA_TENSION_MAP.md              → ARCHIVE (Oracle5)
├── BETA_METADATA_SCHEMA.md           → EVALUATE (may have value)
├── BETA_NOMENCLATURE_SPEC.md         → EVALUATE (may have value)
├── BETA_VALIDATION_REPORT.md         → ARCHIVE (Oracle5-6)
├── CONTENT_ALIGNMENT_AUDIT.md        → ARCHIVE (Oracle6-8)
├── COSMOS_ALIGNMENT_REPORT.md        → ARCHIVE (Oracle6)
├── CRYSTALLINE_CHARACTERISTICS.md    → EVALUATE (quality spec)
├── DEFRAG_EXECUTION_LOG.md           → ARCHIVE (Oracle4)
├── OPERATIONAL_DOCUMENTS_TODO.md     → DELETE (superseded)
├── POST_FORGE_TREE.md                → DELETE (superseded)
├── RECONNAISSANCE_REPORT.md          → ARCHIVE (Oracle6)
├── REVISION_PRIORITIES.md            → DELETE (superseded)
└── THREAD_TRAJECTORY.md              → ARCHIVE (historical)
```

---

## PHASE 2: ORACLE CONTEXT SEQUENTIALIZATION

### 2.1 Naming Convention

**Pattern**: `ORACLE{NN}_CONTEXT_v{M}.md`

Where:
- `{NN}` = Two-digit Oracle number (01-99)
- `{M}` = Version number within that Oracle (1, 2, 3...)

**Examples**:
- `ORACLE07_CONTEXT_v1.md` — First context for Oracle7
- `ORACLE08_CONTEXT_v1.md` — First context for Oracle8
- `ORACLE09_CONTEXT_v3.md` — Third context for Oracle9 (current)

### 2.2 Provenance Mapping

Based on content analysis and Oracle arc:

| Current Name | Oracle Origin | New Name |
|--------------|---------------|----------|
| ORACLE_CONTEXT.md | Oracle7 (generic) | ORACLE07_CONTEXT_v1.md |
| ORACLE_CONTEXT_v2.md | Oracle7-8 transition | ORACLE08_CONTEXT_v1.md |
| ORACLE8_STATUS_REPORT.md | Oracle8 (status) | → ARCHIVE/ |
| ORACLE9_CONTEXT.md | Oracle9 v1 | ORACLE09_CONTEXT_v1.md |
| ORACLE9_CONTEXT_v2.md | Oracle9 v2 | ORACLE09_CONTEXT_v2.md |
| THREAD_CONTEXT.md | Unknown | → EVALUATE then ARCHIVE or DELETE |

### 2.3 Execution

```bash
cd orchestration/state

# Rename Oracle contexts
mv ORACLE_CONTEXT.md ORACLE07_CONTEXT_v1.md
mv ORACLE_CONTEXT_v2.md ORACLE08_CONTEXT_v1.md
mv ORACLE9_CONTEXT.md ORACLE09_CONTEXT_v1.md
mv ORACLE9_CONTEXT_v2.md ORACLE09_CONTEXT_v2.md

# Archive status report
mv ORACLE8_STATUS_REPORT.md ../../ARCHIVE/ORACLE8_STATUS_REPORT.md

# Evaluate THREAD_CONTEXT.md
head -50 THREAD_CONTEXT.md
# If unclear provenance and no unique value → DELETE
# If historical value → ARCHIVE

# Verify renames
ls -la ORACLE*
```

---

## PHASE 3: SCAFFOLDING TRIAGE

### 3.1 Triage Categories

**ARCHIVE** (historical value, no longer active):
- ALPHA_* files (Oracle5 restoration archaeology)
- BETA_VALIDATION_REPORT.md
- CONTENT_ALIGNMENT_AUDIT.md
- COSMOS_ALIGNMENT_REPORT.md
- DEFRAG_EXECUTION_LOG.md
- RECONNAISSANCE_REPORT.md
- THREAD_TRAJECTORY.md

**DELETE** (superseded, no unique value):
- OPERATIONAL_DOCUMENTS_TODO.md
- POST_FORGE_TREE.md
- REVISION_PRIORITIES.md

**EVALUATE** (may have extractable value):
- BETA_METADATA_SCHEMA.md — Check if content is in CANON or STANDARDS
- BETA_NOMENCLATURE_SPEC.md — Check if content is in CANON-00000-SCHEMA
- CRYSTALLINE_CHARACTERISTICS.md — Check if quality spec has unique value

### 3.2 Evaluation Process

For each EVALUATE file:

```bash
# Check if content exists elsewhere
echo "=== Checking BETA_METADATA_SCHEMA.md ==="
head -100 orchestration/scaffolding/BETA_METADATA_SCHEMA.md

# Compare to STANDARDS.md
grep -l "frontmatter\|yaml\|metadata" orchestration/state/STANDARDS.md

# If unique value exists → Extract to appropriate location
# If superseded → ARCHIVE or DELETE
```

### 3.3 Execution

```bash
# Create archive subdirectory for scaffolding
mkdir -p ARCHIVE/scaffolding

# Move ARCHIVE candidates
mv orchestration/scaffolding/ALPHA_ARCHAEOLOGY_REPORT.md ARCHIVE/scaffolding/
mv orchestration/scaffolding/ALPHA_OPERATIONAL_COHERENCE.md ARCHIVE/scaffolding/
mv orchestration/scaffolding/ALPHA_REPOSITORY_AUDIT.md ARCHIVE/scaffolding/
mv orchestration/scaffolding/ALPHA_SYNTHESIS.md ARCHIVE/scaffolding/
mv orchestration/scaffolding/ALPHA_TENSION_MAP.md ARCHIVE/scaffolding/
mv orchestration/scaffolding/BETA_VALIDATION_REPORT.md ARCHIVE/scaffolding/
mv orchestration/scaffolding/CONTENT_ALIGNMENT_AUDIT.md ARCHIVE/scaffolding/
mv orchestration/scaffolding/COSMOS_ALIGNMENT_REPORT.md ARCHIVE/scaffolding/
mv orchestration/scaffolding/DEFRAG_EXECUTION_LOG.md ARCHIVE/scaffolding/
mv orchestration/scaffolding/RECONNAISSANCE_REPORT.md ARCHIVE/scaffolding/
mv orchestration/scaffolding/THREAD_TRAJECTORY.md ARCHIVE/scaffolding/

# Delete superseded files
rm orchestration/scaffolding/OPERATIONAL_DOCUMENTS_TODO.md
rm orchestration/scaffolding/POST_FORGE_TREE.md
rm orchestration/scaffolding/REVISION_PRIORITIES.md

# Handle EVALUATE files based on analysis
# (Document decisions in execution log)
```

---

## PHASE 4: STATE FILE CONSOLIDATION

### 4.1 Evaluate Redundancies

```bash
# Check CURRENT_STATE.md against BACKLOG.md
echo "=== CURRENT_STATE.md content ==="
head -50 orchestration/state/CURRENT_STATE.md

# If CURRENT_STATE duplicates BACKLOG or is stale → DELETE or ARCHIVE
# If unique tracking value → KEEP
```

### 4.2 Final State Directory Structure

```
orchestration/state/
├── BACKLOG.md                    # Active task tracking
├── DESIGN_DECISIONS.md           # Living decision log
├── FOUR_SYSTEMS.md               # Gemini architecture extraction
├── ORACLE_DECISIONS.md           # Cross-Oracle decision log
├── ORACLE07_CONTEXT_v1.md        # Historical
├── ORACLE08_CONTEXT_v1.md        # Historical
├── ORACLE09_CONTEXT_v1.md        # Historical
├── ORACLE09_CONTEXT_v2.md        # Historical
├── ORACLE09_CONTEXT_v3.md        # CURRENT (from Sovereign via outputs/)
├── PROCESSING_PATTERN.md         # 033B methodology
├── PROCESSING_ROUTING.md         # 033B routing
├── SOURCES_SCHEMA.md             # 032B schema
├── STANDARDS.md                  # Quality standards
└── TRIAGE_PROTOCOL.md            # 032B protocol
```

---

## PHASE 5: ARCHIVE ORGANIZATION

### 5.1 Update ARCHIVE/README.md

```markdown
# ARCHIVE

Historical documents preserved for archaeological value. Not actively maintained.

## Contents

### Root Level
- `ARCHIVE-ARTIFACT-SYSTEM.md` — Early artifact system design
- `ARCHIVE-COGNITIVE-PALACE-SPECS.md` — Original palace metaphor specs

### scaffolding/
Oracle5-8 working documents, preserved for process archaeology:
- `ALPHA_*` — Oracle5 restoration reports
- `BETA_*` — Oracle5-6 validation work
- `CONTENT_ALIGNMENT_AUDIT.md` — Oracle6-8 alignment work
- `COSMOS_ALIGNMENT_REPORT.md` — Oracle6 cosmos audit
- `DEFRAG_EXECUTION_LOG.md` — Oracle4 defragmentation
- `RECONNAISSANCE_REPORT.md` — Oracle6 reconnaissance
- `THREAD_TRAJECTORY.md` — Oracle arc planning

### Status Reports
- `ORACLE8_STATUS_REPORT.md` — Oracle8 completion status

## Usage

These documents are **read-only reference**. Do not modify.
Extract patterns and learnings, do not revive deprecated approaches.
```

---

## PHASE 6: ORACLE10 HANDOFF PREPARATION

### 6.1 Create Handoff Notes

```bash
cat > orchestration/state/ORACLE10_HANDOFF.md << 'EOF'
# Oracle10 Handoff Notes

## From Oracle9

### Completed
- SOURCES ingestion infrastructure (032A/B)
- 184 sources triaged with eight-dimensional schema
- 4 paradigm sources processed and integrated
- PROCESSING_PATTERN.md established
- sources.csv as ontology seed
- Repository flattened for portability (034A)
- Orchestration hygiene complete (034B)

### Remaining for Oracle9 (if continued)
- 43 paradigm sources unprocessed
- 44 strategic sources unprocessed

### Oracle10 Scope: IIC Configuration
Per Oracle8 planning:
- Configure Identity-Intelligence Complex
- Requires enriched corpus (✓ 4 sources integrated)
- Five-account constellation setup
- Platform-specific configurations

### Key Files for Oracle10
- `ORACLE09_CONTEXT_v3.md` — Final Oracle9 state
- `PROCESSING_PATTERN.md` — Source processing methodology
- `FOUR_SYSTEMS.md` — Gemini architecture (four operational modes)
- `sources.csv` — Triaged source inventory
- `SOURCES_SCHEMA.md` — Eight-dimensional classification

### Outstanding Questions for Oracle10
1. Which IIC accounts to configure first?
2. Platform prioritization (Claude, ChatGPT, Gemini, Grok)?
3. Integration with structured data layer (CSV → SQLite)?
EOF
```

---

## PHASE 7: VERIFICATION

### 7.1 Verification Commands

```bash
# Verify Oracle context naming
echo "=== Oracle Contexts ==="
ls orchestration/state/ORACLE*

# Verify scaffolding triaged
echo "=== Remaining Scaffolding ==="
ls orchestration/scaffolding/

# Verify ARCHIVE populated
echo "=== Archive Contents ==="
ls -la ARCHIVE/
ls -la ARCHIVE/scaffolding/

# Verify no orphan files
echo "=== State Directory ==="
ls orchestration/state/
```

### 7.2 Git Commit

```bash
git add -A
git commit -m "DIRECTIVE-034B: Orchestration hygiene

Oracle contexts sequentialized:
- ORACLE07_CONTEXT_v1.md (was ORACLE_CONTEXT.md)
- ORACLE08_CONTEXT_v1.md (was ORACLE_CONTEXT_v2.md)
- ORACLE09_CONTEXT_v1.md, v2.md (renamed)

Scaffolding triaged:
- 11 files → ARCHIVE/scaffolding/
- 3 files → DELETED (superseded)
- 3 files → EVALUATED (decision logged)

Prepared:
- ORACLE10_HANDOFF.md
- Updated ARCHIVE/README.md

Oracle9 hygiene phase: Stream B complete."
```

---

## SUCCESS CRITERIA

- [ ] All Oracle contexts follow ORACLE{NN}_CONTEXT_v{M}.md pattern
- [ ] Scaffolding directory reduced to 0-3 files (evaluated items only)
- [ ] ARCHIVE/scaffolding/ contains 11+ historical files
- [ ] ARCHIVE/README.md updated
- [ ] ORACLE10_HANDOFF.md created
- [ ] No orphan or unclear files in orchestration/state/
- [ ] Git committed

---

## EXECUTION LOG TEMPLATE

Save to: `orchestration/execution_logs/EXECUTION_LOG-2026-01-02-034B.md`

```markdown
# EXECUTION LOG: DIRECTIVE-034B

**Executed**: 2026-01-02
**Agent**: Claude Code
**Status**: [COMPLETE/INCOMPLETE]

## Phase 2: Context Sequentialization
| Old Name | New Name | Notes |
|----------|----------|-------|
| ORACLE_CONTEXT.md | ORACLE07_CONTEXT_v1.md | |
| ... | ... | |

## Phase 3: Scaffolding Triage
| File | Decision | Rationale |
|------|----------|-----------|
| ALPHA_ARCHAEOLOGY_REPORT.md | ARCHIVE | Oracle5 work |
| ... | ... | ... |

## Phase 4: State Consolidation
- Files removed: [list]
- Files kept: [list]

## Phase 5: Archive Organization
- Files archived: [N]
- README updated: [Y/N]

## Phase 6: Handoff
- ORACLE10_HANDOFF.md created: [Y/N]

## Phase 7: Verification
[Paste verification output]

## EVALUATE File Decisions
| File | Decision | Rationale |
|------|----------|-----------|
| BETA_METADATA_SCHEMA.md | [decision] | [rationale] |
| BETA_NOMENCLATURE_SPEC.md | [decision] | [rationale] |
| CRYSTALLINE_CHARACTERISTICS.md | [decision] | [rationale] |

## Issues/Notes
[Any problems encountered]
```

---

**THIS DIRECTIVE ACHIEVES CLEAN ORACLE10 HANDOFF.**
