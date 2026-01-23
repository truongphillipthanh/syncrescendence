# ORACLE 10 INITIALIZATION

## Inheritance Summary
- **7 dirs**: 00-ORCHESTRATION → 06-EXEMPLA
- **78 CANON docs** (corpus complete)
- **184 sources**: 176 in raw/, 8 in processed/, 4 integrated (MISSION INCOMPLETE)
- **FLAT VIOLATIONS**: state/ has 4 subdirs, oracle_contexts/ has 9 files, scaffolding/ nested

## Your First 4 Actions (Execute Before Anything Else)

### 1. Flatten state/ (~15 min)
```bash
cd 00-ORCHESTRATION/state
mv archaeology/CRYSTALLINE_CHARACTERISTICS.md ARCH-CRYSTALLINE_CHARACTERISTICS.md
mv archaeology/DESIGN_DECISIONS.md ARCH-DESIGN_DECISIONS.md
mv archaeology/ORACLE_ARC_SUMMARY.md ARCH-ORACLE_ARC_SUMMARY.md
mv archaeology/ORACLE_DECISIONS.md ARCH-ORACLE_DECISIONS.md
mv dynamic/ACTUAL_TREE.md DYN-ACTUAL_TREE.md
mv dynamic/BACKLOG.md DYN-BACKLOG.md
mv dynamic/DASHBOARD.md DYN-DASHBOARD.md
mv ledgers/* ./
mv reference/* ./  # prefix with REF- if needed
rmdir archaeology dynamic ledgers reference
```

### 2. Distill oracle_contexts/ (~30 min)
- READ all 9 files
- COMPRESS Oracle 0-9 history into single ORACLE_ARC.md
- DELETE the 9 source files
- Keep: ORACLE_ARC.md + ORACLE10_CONTEXT.md (2 files only)

### 3. Flatten 05-MEMORY/scaffolding/ (~5 min)
```bash
cd 05-MEMORY && mv scaffolding/* ./ && rmdir scaffolding
```

### 4. Flatten 06-EXEMPLA/ (~5 min)
```bash
cd 06-EXEMPLA
mv case-studies/TEMPLATE.md CASE-TEMPLATE.md
mv worked-examples/TEMPLATE.md EXAMPLE-TEMPLATE.md
rmdir case-studies worked-examples
```

## Your Primary Mission: PROJ-001

**Oracle 9 FAILED this mission.** Tasks remaining:

| Task | Status | Action |
|------|--------|--------|
| TASK-003 | in_progress | Process 40+ paradigm sources |
| TASK-004 | not_started | Process strategic sources |
| TASK-008 | not_started | Review CONTENT_PROCESSING_QUEUE.md |
| TASK-009 | not_started | Review YOUTUBE_PROCESSING_BACKLOG.md |

**Success**: 40+ in processed/, 20+ integrated into CANON, PROJ-001 COMPLETE

## Anti-Patterns (DO NOT REPEAT)

| Anti-Pattern | Oracle 9 Did | You Must Do |
|--------------|--------------|-------------|
| Incremental directives | 22 directives | 1 comprehensive directive per objective |
| Organization = distillation | Created subdirs | SEMANTIC COMPRESSION (read→extract→compress→delete) |
| Documentation without execution | "RECOMMEND: Delete X" | EXECUTE and VERIFY |
| Report-based evaluation | Trusted logs | Run verification commands |
| Structural busywork | 27 structural tasks, 0 source processing | Focus on PROJ-001 |

## Verification Before Declaring Complete

```bash
# 1. state/ is flat
ls 00-ORCHESTRATION/state/ | grep -c "/"  # Should be 0

# 2. oracle_contexts/ has exactly 2 files
ls 00-ORCHESTRATION/oracle_contexts/ | wc -l  # Should be 2

# 3. No in_progress tasks
grep "in_progress" tasks.csv  # Should be empty

# 4. Sources processed
ls 04-SOURCES/processed/ | wc -l  # Should be 40+
```

## Memory Edits (7 Active)
1. 7 numbered dirs, metabolism = content not infra
2. Comprehensive directives, minimize relay, 18 lenses
3. Ontology: CSV/RDBMS, superintelligent architect framing
4. A/B stream delivery, artifacts to /outputs
5. **FLAT PRINCIPLE**: prefixes not subdirs
6. **DISTILLATION**: read→extract→compress→delete
7. **LEDGER TRUTH**: tasks.csv is ground truth

## Context Files to Reference
- ORACLE09_FINAL_CULMINATION.md (failure analysis)
- tasks.csv, projects.csv (ground truth)
- REF-PROCESSING_PATTERN.md (source processing method)
- REF-SOURCES_SCHEMA.md (8-dimensional classification)

---

*Flatten debt. Process sources. Verify against ledgers. Don't repeat Oracle 9's failure.*
