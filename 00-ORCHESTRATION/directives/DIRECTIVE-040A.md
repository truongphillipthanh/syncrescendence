# DIRECTIVE-040A: HYGIENE COMPLETION + LEDGER SYNCHRONIZATION
## Oracle 10 Blitzkrieg 40 — Stream A

**Issued**: 2026-01-05
**Stream**: A (Claude 2)
**Priority**: CRITICAL
**Duration**: 90 minutes
**Parallel**: DIRECTIVE-040B on Claude 3

---

## PREAMBLE

DIRECTIVE-039A/B achieved 95% structural objectives but left critical residual debt:
- 6 files polluting repository root
- 1 orphan scaffolding/ directory
- All three ledgers desynchronized from execution reality

This directive closes these gaps completely.

**Critical success factors:**
- EXECUTE, don't recommend
- RUN verification commands, PASTE output
- UPDATE ledgers within this directive scope

---

## PHASE 1: ROOT POLLUTION CLEANUP (~15 minutes)

### 1.1 Inventory
```bash
cd /path/to/syncrescendence
ls *.md
```
Expected: DIRECTIVE-039A.md, DIRECTIVE-039B.md, ORACLE09_FINAL_CULMINATION.md, ORACLE10_COMPREHENSIVE_ARCHAEOLOGY.md, ORACLE10_CONTEXT.md, ORACLE10_INIT.md

### 1.2 Relocate Directives
```bash
mv DIRECTIVE-039A.md 00-ORCHESTRATION/directives/DIRECTIVE-039A.md
mv DIRECTIVE-039B.md 00-ORCHESTRATION/directives/DIRECTIVE-039B.md
```

### 1.3 Relocate Oracle Contexts
```bash
# Keep current context in oracle_contexts/
mv ORACLE10_CONTEXT.md 00-ORCHESTRATION/oracle_contexts/ORACLE10_CONTEXT.md
mv ORACLE10_COMPREHENSIVE_ARCHAEOLOGY.md 00-ORCHESTRATION/oracle_contexts/ORACLE10_COMPREHENSIVE_ARCHAEOLOGY.md

# Archive historical/initialization docs
mv ORACLE09_FINAL_CULMINATION.md 05-ARCHIVE/SCAFF-ORACLE09_FINAL_CULMINATION.md
mv ORACLE10_INIT.md 05-ARCHIVE/SCAFF-ORACLE10_INIT.md
```

### 1.4 Verification
```bash
ls *.md
# Expected: README.md only (or empty)

ls 00-ORCHESTRATION/directives/DIRECTIVE-039*.md
# Expected: DIRECTIVE-039A.md, DIRECTIVE-039B.md

ls 00-ORCHESTRATION/oracle_contexts/
# Expected: 4 files now (ORACLE_ARC.md, ORACLE10_CONTEXT.md, ORACLE10_COMPREHENSIVE_ARCHAEOLOGY.md, plus existing)
```

---

## PHASE 2: FLATTEN ORPHAN SCAFFOLDING (~5 minutes)

### 2.1 Execute
```bash
cd 00-ORCHESTRATION
mv scaffolding/COHERENCE_ABSORPTION_AUDIT.md state/ARCH-COHERENCE_ABSORPTION_AUDIT.md
rmdir scaffolding
```

### 2.2 Verification
```bash
find 00-ORCHESTRATION -type d -name "scaffolding"
# Expected: empty

ls 00-ORCHESTRATION/state/ARCH-*.md
# Expected: includes ARCH-COHERENCE_ABSORPTION_AUDIT.md
```

---

## PHASE 3: LEDGER SYNCHRONIZATION (~45 minutes)

### 3.1 Update tasks.csv

Open `00-ORCHESTRATION/state/tasks.csv` and make these changes:

**Update TASK-003:**
```
Before: TASK-003,PROJ-001,Process remaining paradigm sources,task,in_progress,P1,Claude_Code,null,20,null,2026-01-02,2026-01-02,...
After:  TASK-003,PROJ-001,Process remaining paradigm sources,task,done,P1,Claude_Code,null,20,4,2026-01-02,2026-01-05,26 sources processed via 039A/B
```

**Update TASK-004:**
```
Before: TASK-004,PROJ-001,Process strategic sources,task,not_started,P2,Claude_Code,TASK-003,15,null,2026-01-02,2026-01-02,...
After:  TASK-004,PROJ-001,Process strategic sources,task,done,P2,Claude_Code,null,15,3,2026-01-02,2026-01-05,Completed with paradigm batch
```

**Append new task rows:**
```csv
TASK-032,PROJ-001,DIRECTIVE-039A Phase 1-2 structural,structural,done,P1,Claude_Code_2,null,1.25,1.08,2026-01-05,2026-01-05,state/ flattened; oracle_contexts/ distilled 9→2
TASK-033,PROJ-001,DIRECTIVE-039A Phase 3 processing,processing,done,P1,Claude_Code_2,null,1.5,1.5,2026-01-05,2026-01-05,13 paradigm sources processed and qualified
TASK-034,PROJ-001,DIRECTIVE-039B Phase 1-2 structural,structural,done,P1,Claude_Code_3,null,0.42,0.42,2026-01-05,2026-01-05,ARCHIVE/ scaffolding/ and EXEMPLA/ flattened
TASK-035,PROJ-001,DIRECTIVE-039B Phase 3 processing,processing,done,P1,Claude_Code_3,null,1.5,1.5,2026-01-05,2026-01-05,13 sources processed; 6 CANON integrations
TASK-036,PROJ-001,DIRECTIVE-040A hygiene+ledger,hygiene,done,P1,Claude_Code_2,null,0.75,null,2026-01-05,2026-01-05,Root cleanup; all ledgers synchronized
TASK-037,PROJ-001,DIRECTIVE-040B completion gate,verification,done,P1,Claude_Code_3,null,1.0,null,2026-01-05,2026-01-05,40+ sources; PROJ-001 complete
```

### 3.2 Update projects.csv

**Update PROJ-001:**
```
Before: PROJ-001,Transcript Ingestion,initiative,in_progress,P1,Oracle9,null,9,modal1,2026-01-15,2026-01-01,2026-01-02,...
After:  PROJ-001,Transcript Ingestion,initiative,in_progress,P1,Oracle10,null,10,modal1,2026-01-15,2026-01-01,2026-01-05,40+ processed targeting completion this session
```
(Final status update to `complete` pending 040B verification)

### 3.3 Update sources.csv (CRITICAL)

For each of these 34 processed SOURCE-* files, update the corresponding row:

**Status and date updates required for:**
1. SOURCE-20250320-youtube-lecture-longnow-benjamin_bratton
2. SOURCE-20250403-youtube-interview-dwarkesh-scott_alexander_daniel_kokotajlo
3. SOURCE-20250522-youtube-interview-dwarkesh-sholto_douglas_trenton_bricken
4. SOURCE-20250528-youtube-lecture-longnow-sara_imari_walker
5. SOURCE-20250605-youtube-lecture-strangeloop-ethan_mollick
6. SOURCE-20250623-youtube-interview-brainmind-blaise_aguera_y_arcas
7. SOURCE-20250723-youtube-interview-lex_fridman-demis_hassabis
8. SOURCE-20250807-youtube-lecture-tedx-blaise_aguera_y_arcas
9. SOURCE-20250902-youtube-lecture-strangeloop-david_deutsch
10. SOURCE-20250903-youtube-interview-tow-max_tegmark
11. SOURCE-20250912-youtube-interview-dwarkesh-sergey_levine
12. SOURCE-20250926-youtube-interview-dwarkesh_patel-richard_sutton
13. SOURCE-20251001-x-thread-andrej_karpathy-sutton_response
14. SOURCE-20251013-youtube-interview-indset-matthew_kinsella
15. SOURCE-20251014-youtube-interview-duqun-donald_hoffman
16. SOURCE-20251017-youtube-interview-dwarkesh_patel-andrej_karpathy
17. SOURCE-20251020-youtube-interview-a16z-reid_hoffman
18. SOURCE-20251021-youtube-interview-mlst-chris_kempes
19. SOURCE-20251021-youtube-interview-tbpn-bryan_johnson
20. SOURCE-20251024-youtube-interview-arcprize-chollet_knoop
21. SOURCE-20251025-youtube-interview-mlst-blaise_aguera_y_arcas
22. SOURCE-20251027-youtube-interview-allin-john_martinis
23. SOURCE-20251028-youtube-lecture-nvidia-gtc_jensen_huang
24. SOURCE-20251029-youtube-interview-openai-sam_jakub_wojciech
25. SOURCE-20251030-youtube-interview-moonshots-anatoly_yakovenko
26. SOURCE-20251030-youtube-video-aiexp-end_of_ai
27. SOURCE-20251031-youtube-interview-a16z-marc_andreessen_ben_horowitz
28. SOURCE-20251031-youtube-interview-a16z-marc_ben
29. SOURCE-20251031-youtube-interview-allin-elon_musk
30. SOURCE-20251031-youtube-interview-bilawal-john_gaeta
31. SOURCE-20251031-youtube-lecture-extropic-trevor_mccourt
32. SOURCE-20251031-youtube-video-dshapiro-post_labor_enterprise
33. SOURCE-20251031-youtube-video-nopriors-best_of_2025
34. SOURCE-20251101-youtube-video-dshapiro-renaissance_2_0

For each row:
- Change `status` column: → `processed`
- Change `date_processed` column: → `2026-01-05`

### 3.4 Verification
```bash
# Task count
wc -l 00-ORCHESTRATION/state/tasks.csv
# Expected: 39 lines (header + 38 tasks)

# No in_progress for PROJ-001 critical tasks
grep "PROJ-001" 00-ORCHESTRATION/state/tasks.csv | grep "in_progress" | grep -E "TASK-00[34]"
# Expected: empty

# Processed source count in CSV
grep ",processed," 04-SOURCES/sources.csv | wc -l
# Expected: 34+
```

---

## PHASE 4: ADDITIONAL SOURCE PROCESSING (~20 minutes)

To definitively exceed 40 processed sources, process these 6:

1. `20251020-youtube_video-itrg-ben_goertzel` → Intelligence chain
2. `20251024-youtube_lecture-eit-henrik_von_scheel` → Expertise chain
3. `20251023-youtube_video-scaleai-chain_of_thought_mcp_atlas_benchmark` → Intelligence chain
4. `20251027-youtube_video-carbutt-cathie_wood` → Expertise chain
5. `20251222-youtube_video-a16z-content` → Information chain
6. `20251223-youtube_video-aidaily-mike_kreiger` → Intelligence chain

Use processing pattern from REF-PROCESSING_PATTERN.md:
- Read raw transcript
- Create qualified brief with frontmatter
- Save to 04-SOURCES/processed/ as SOURCE-YYYYMMDD-...
- Update sources.csv row

---

## PHASE 5: VERIFICATION + REPORTING

### 5.1 Final Verification Suite
```bash
# Root clean
ls *.md 2>/dev/null | wc -l
# Expected: 0 or 1

# No scaffolding
find . -type d -name "scaffolding" | wc -l
# Expected: 0

# Processed count
ls 04-SOURCES/processed/*.md | wc -l
# Expected: 40+

# Tasks complete
grep "in_progress" 00-ORCHESTRATION/state/tasks.csv | grep "PROJ-001"
# Expected: empty (only TASK-036/037 might show in_progress during execution)
```

### 5.2 Execution Log
Create `00-ORCHESTRATION/execution_logs/EXECUTION_LOG-2026-01-05-040A.md`:

```markdown
# EXECUTION LOG: DIRECTIVE-040A
## Stream A Completion Report

**Date**: 2026-01-05
**Executor**: Claude 2 (Stream A)
**Status**: COMPLETE

## Phase 1: Root Cleanup
- Files relocated: 6
- Destination verification: [paste ls output]

## Phase 2: Flatten Scaffolding
- File moved: COHERENCE_ABSORPTION_AUDIT.md → ARCH-COHERENCE_ABSORPTION_AUDIT.md
- Directory removed: scaffolding/
- Verification: [paste find output]

## Phase 3: Ledger Sync
- tasks.csv: 2 updated, 6 added (38 total)
- projects.csv: PROJ-001 owner updated
- sources.csv: 34 rows updated to processed

## Phase 4: Additional Processing
| Source | Status | Chain |
|--------|--------|-------|
| ben_goertzel | processed | Intelligence |
| [etc] | ... | ... |

## Verification Results
[paste all verification command outputs]
```

---

## SUCCESS CRITERIA

- [ ] 0 .md files at repository root (except README)
- [ ] 0 scaffolding/ directories
- [ ] tasks.csv has 38+ rows, no PROJ-001 critical tasks in_progress
- [ ] projects.csv PROJ-001 owner = Oracle10
- [ ] sources.csv has 34+ rows with status=processed
- [ ] 40+ SOURCE-* files in processed/
- [ ] Execution log with verification outputs

---

*Execute comprehensively. Synchronize ledgers completely. Verify rigorously.*
