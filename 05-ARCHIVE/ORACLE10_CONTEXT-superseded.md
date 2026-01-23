# ORACLE 10 CONTEXT
## Session Handoff Document

**Generated**: 2026-01-05
**Status**: ACTIVE
**Purpose**: Provide Claude Code instances with complete operational context

---

## SITUATION AWARENESS

### Repository Structure (7 Numbered Directories)
```
00-ORCHESTRATION/  ← Coordination infrastructure (PROTECTED)
01-CANON/          ← 78 constitutional documents (COMPLETE)
02-OPERATIONAL/    ← Living documents
03-QUEUE/          ← Pending items (2-cycle metabolism)
04-SOURCES/        ← raw: 176, processed: 8, integrated: 4 (MISSION TARGET)
05-ARCHIVE/        ← Historical preservation
06-EXEMPLA/        ← Case studies and examples
```

### Current State Summary
- **CANON corpus**: 78 documents, semantically annealed, at superlativity
- **Sources**: 184 tracked in sources.csv; only 8 processed, 4 integrated
- **PROJ-001 status**: MISSION INCOMPLETE (Oracle 9 failed this mission)
- **Flat violations**: 4 locations requiring immediate paydown

---

## FLAT VIOLATIONS (IMMEDIATE DEBT)

### Violation 1: 00-ORCHESTRATION/state/
```
state/
├── archaeology/     ← 4 files, VIOLATES FLAT
├── dynamic/         ← 3 files, VIOLATES FLAT
├── ledgers/         ← 4 files, VIOLATES FLAT
└── reference/       ← 7 files, VIOLATES FLAT
```
**Resolution**: Flatten with prefixes (ARCH-, DYN-, REF-), move ledgers to root, delete empty subdirs

### Violation 2: 00-ORCHESTRATION/oracle_contexts/
```
oracle_contexts/     ← 9 files, should be 2
```
**Resolution**: Semantic compression—READ all 9, EXTRACT unique value, COMPRESS into ORACLE_ARC.md + ORACLE10_CONTEXT.md, DELETE originals

### Violation 3: 05-ARCHIVE/scaffolding/
```
scaffolding/         ← 16 files nested
```
**Resolution**: Flatten to 05-ARCHIVE/ root with SCAFF- prefix

### Violation 4: 06-EXEMPLA/
```
case-studies/        ← 1 file, VIOLATES FLAT
worked-examples/     ← 1 file, VIOLATES FLAT
```
**Resolution**: Flatten with CASE- and EXAMPLE- prefixes

---

## PRIMARY MISSION: PROJ-001

### Objective
Transform 184 raw sources into processed intelligence briefs integrated into CANON.

### Current Task Status (from tasks.csv)
| Task | Status | Action Required |
|------|--------|-----------------|
| TASK-003 | IN_PROGRESS | Process 40+ paradigm sources |
| TASK-004 | NOT_STARTED | Process strategic sources |
| TASK-008 | NOT_STARTED | Review CONTENT_PROCESSING_QUEUE.md |
| TASK-009 | NOT_STARTED | Review YOUTUBE_PROCESSING_BACKLOG.md |

### Success Metrics
- 40+ files in 04-SOURCES/processed/
- 20+ sources integrated into CANON documents
- PROJ-001 marked COMPLETE in projects.csv
- All TASK-003/004/008/009 marked DONE in tasks.csv

### Processing Pattern (from REF-PROCESSING_PATTERN.md)
1. **Triage**: Classify source by signal tier (paradigm/strategic/tactical/noise)
2. **Extract**: Pull key insights, quotes, frameworks
3. **Qualify**: Create processed .md with frontmatter and qualified content
4. **Integrate**: Weave insights into relevant CANON documents
5. **Update**: Mark status in sources.csv

---

## 18 EVALUATIVE LENSES

Apply before any major decision:

| # | Lens | Question |
|---|------|----------|
| 1 | Syncrescendent Route | Does this advance the civilizational mission? |
| 2 | Bitter Lesson | Does this scale with compute, not hand-crafting? |
| 3 | Antifragile | Does this get stronger under stress? |
| 4 | Meet the Moment | Is this the work THIS moment requires? |
| 5 | Steelman & Redteam | What's the best counter-argument? |
| 6 | Personal Idiosyncrasies | Does this honor the Principal's cognitive profile? |
| 7 | Potency Without Loss | Maximum power with minimum sacrifice? |
| 8 | Elegance | Is this the simplest form that works? |
| 9 | Agentify | Can a fresh agent navigate this in ≤2 decisions? |
| 10 | First Principles | What are the irreducible truths here? |
| 11 | Systems Thinking | What are the second-order effects? |
| 12 | Industrial Engineering | What's the throughput bottleneck? |
| 13 | Complexity Theory | Is this emergence or complication? |
| 14 | Permaculture | Does this create self-sustaining patterns? |
| 15 | Design Thinking | What does the user actually need? |
| 16 | Agile | What's the minimum viable increment? |
| 17 | Lean | What's the waste here? |
| 18 | Six Sigma | What's the defect rate and root cause? |

---

## ANTI-PATTERNS (DO NOT REPEAT)

| Anti-Pattern | What Oracle 9 Did | What You Must Do |
|--------------|-------------------|------------------|
| Incremental directives | 22 small directives | Execute comprehensive directive fully |
| Organization = distillation | Created subdirs | READ→EXTRACT→COMPRESS→DELETE |
| Documentation without execution | "RECOMMEND: Delete X" | EXECUTE, then VERIFY |
| Report-based evaluation | Trusted own logs | Run verification commands, examine output |
| Structural busywork | 27 structural tasks, 0 sources | Focus on PROJ-001 substance |

---

## MEMORY EDITS (7 ACTIVE)

1. **Repo structure**: 7 numbered dirs (00-06); metabolism applies to CONTENT not infrastructure
2. **Directive pattern**: Comprehensive directives; minimize relay; 18 lenses evaluation
3. **Ontology emergence**: CSV/RDBMS bridge toward codebase; superintelligent architect framing
4. **Delivery pattern**: A/B stream bifurcation; artifacts to /outputs
5. **FLAT PRINCIPLE**: All directories FLAT; use naming prefixes not subdirs; nesting requires Principal approval
6. **DISTILLATION SEMANTICS**: "Metabolize/distill" = READ all → EXTRACT unique value → COMPRESS into single doc → DELETE originals
7. **LEDGER GROUND TRUTH**: tasks.csv is truth for work status; verify IN_PROGRESS tasks are DONE before claiming complete

---

## VERIFICATION COMMANDS

Run these BEFORE claiming completion:

```bash
# Flat violations resolved
find 00-ORCHESTRATION/state -type d | wc -l  # Should be 1 (just state/ itself)
ls 00-ORCHESTRATION/oracle_contexts/ | wc -l  # Should be 2
find 05-ARCHIVE -type d | wc -l  # Should be 1
find 06-EXEMPLA -type d | wc -l  # Should be 1

# Sources processed
ls 04-SOURCES/processed/*.md | wc -l  # Target: 40+

# Ledger truth
grep "in_progress" 00-ORCHESTRATION/state/tasks.csv | grep "PROJ-001"  # Should be empty when done
```

---

## COORDINATION PROTOCOL

### Stream Assignment
- **Claude 2 (Stream A)**: Receives DIRECTIVE-039A
- **Claude 3 (Stream B)**: Receives DIRECTIVE-039B

### Handoff Rules
1. Each stream operates independently on assigned scope
2. No cross-stream dependencies within same directive
3. Artifacts output to /outputs for Principal collection
4. Execution logs capture all changes for merge coordination

### Conflict Resolution
If streams would touch same file:
1. Stream A has priority on 00-ORCHESTRATION/
2. Stream B has priority on 05-ARCHIVE/, 06-EXEMPLA/
3. Both can process different sources in parallel

---

*Oracle 10 Context active. Execute with precision. Verify before completion claims.*
