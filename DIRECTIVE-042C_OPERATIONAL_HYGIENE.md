# DIRECTIVE-042C: OPERATIONAL HYGIENE
## Stream C Execution for Claude Code Instance 3
**Date**: 2026-01-09
**Priority**: P2
**Projects**: Queue Triage, Ledger Maintenance, PROJ-016 Creation
**Estimated Duration**: 1.5-2 hours

---

## MISSION

1. Execute queue disposition per documented rules
2. Create PROJ-016 (Skills Conversion) for tracking
3. Update all ledgers with new tasks and project
4. Refresh DYN-BACKLOG.md with current state

---

## CONTEXT

Read the attached ORACLE11_CONTEXT_BLITZKRIEG.md for full strategic context.

**Queue Disposition Rules** (from QUEUE_DISPOSITION.md):
- modal1/: Text-based processing inbox → move to OPERATIONAL or merge
- modal2/: Visual capability deferral queue → keep until Modal 2 activated
- Living documents → 02-OPERATIONAL/
- Point-in-time documents → 05-ARCHIVE/
- Overlapping documents → MERGE into single authoritative source

---

## DELIVERABLES

### 1. Queue Disposition Execution

Execute the following file movements:

**03-QUEUE/modal1/ Disposition**:

| File | Disposition | Destination | Rationale |
|------|-------------|-------------|-----------|
| AI_ECOSYSTEM_SURVEY.md | MOVE | 02-OPERATIONAL/surveys/ | Living document, regularly updated |
| CONTENT_PROCESSING_QUEUE.md | MERGE | Into YOUTUBE_PROCESSING_BACKLOG.md | Overlapping scope |
| QUICK_WINS.md | MOVE | 05-ARCHIVE/ | Point-in-time, historical value only |
| YOUTUBE_PROCESSING_BACKLOG.md | MOVE | 02-OPERATIONAL/queues/ | Active workflow document |

**03-QUEUE/modal2/ Disposition**:

| File | Disposition | Rationale |
|------|-------------|-----------|
| AI_3D_VFX.md | KEEP | Awaiting Modal 2 visual capabilities |
| AI_Academic_Research.md | RECLASSIFY → modal1 | Text-based, no visual requirement |
| AI_Image_Generators.md | KEEP | Awaiting Modal 2 visual capabilities |
| AI_Workflows_in_Video_and_VFX.md | KEEP | Awaiting Modal 2 visual capabilities |
| Physical_AI.md | KEEP | Awaiting Modal 2 visual capabilities |
| QUEUE-36200-SCREENPLAY_ORCHESTRATION.md | KEEP | Awaiting Modal 2 visual capabilities |
| The_Next_Wave_in_AI_Video_and_VFX.md | KEEP | Awaiting Modal 2 visual capabilities |

**Result**: 03-QUEUE/ should be clean with only modal2/ containing deferred visual content.

### 2. PROJ-016 Creation (Skills Conversion)

Create new project entry:

```csv
PROJ-016,Skills Conversion,initiative,not_started,P3,Oracle12+,null,12+,modal1,null,2026-01-09,2026-01-09,Convert top XML functions to Claude Skills format per README specifications
```

**Project Scope** (from README and Oracle context):
- Convert 5 priority functions from XML to Claude Skills format
- Functions: transcribe_youtube, transcribe_interview, integrate, readize, listenize
- Requires Claude Projects deployment testing
- Requires activation accuracy validation

### 3. Updated tasks.csv

Add new tasks created across all Blitzkrieg streams:

```csv
# Stream A tasks (PROJ-002)
TASK-050,PROJ-002,Create Acumen IIC configuration,task,not_started,P1,Claude_Code_1,null,1.5,null,2026-01-09,2026-01-09,Full account specification
TASK-051,PROJ-002,Create Coherence IIC configuration,task,not_started,P1,Claude_Code_1,null,1.5,null,2026-01-09,2026-01-09,Full account specification
TASK-052,PROJ-002,Create IIC shared protocols,task,not_started,P1,Claude_Code_1,null,0.5,null,2026-01-09,2026-01-09,Communication standards

# Stream B tasks (PROJ-012 + hygiene)
TASK-053,PROJ-012,Create GEMINI.md context file,task,not_started,P1,Claude_Code_2,null,0.5,null,2026-01-09,2026-01-09,Syncrescendence-adapted for Gemini CLI
TASK-054,PROJ-012,Create gemini-settings.json template,task,not_started,P2,Claude_Code_2,null,0.25,null,2026-01-09,2026-01-09,MCP and model configuration
TASK-055,PROJ-012,Create multi-CLI coordination protocol,task,not_started,P1,Claude_Code_2,null,0.5,null,2026-01-09,2026-01-09,Parallel execution framework
TASK-056,null,Correct unified-prompt files,task,not_started,P0,Claude_Code_2,null,0.75,null,2026-01-09,2026-01-09,4 files replaced from authoritative sources

# Stream C tasks (Queue + PROJ-016)
TASK-057,null,Execute queue disposition,task,not_started,P2,Claude_Code_3,null,0.5,null,2026-01-09,2026-01-09,Move/merge modal1 files
TASK-058,PROJ-016,Create Skills Conversion project,task,not_started,P3,Claude_Code_3,null,0.25,null,2026-01-09,2026-01-09,Project scaffolding only
TASK-059,null,Update DYN-BACKLOG.md,task,not_started,P2,Claude_Code_3,null,0.5,null,2026-01-09,2026-01-09,Refresh with current state

# Stream D task (Gemini validation)
TASK-060,PROJ-012,Validate Gemini CLI operations,task,not_started,P2,Gemini_CLI,null,0.5,null,2026-01-09,2026-01-09,Test directive execution

# Future tasks (for tracking)
TASK-061,PROJ-002,Create Efficacy IIC configuration,task,not_started,P2,TBD,TASK-051,1.5,null,2026-01-09,2026-01-09,Operations chain account
TASK-062,PROJ-002,Create Mastery IIC configuration,task,not_started,P2,TBD,TASK-061,1.5,null,2026-01-09,2026-01-09,Teaching chain account
TASK-063,PROJ-002,Create Transcendence IIC configuration,task,not_started,P2,TBD,TASK-062,1.5,null,2026-01-09,2026-01-09,Wisdom chain account
TASK-064,PROJ-016,Convert transcribe_youtube to Skill,task,not_started,P3,TBD,null,2.0,null,2026-01-09,2026-01-09,First skill conversion
TASK-065,PROJ-016,Convert integrate to Skill,task,not_started,P3,TBD,TASK-064,2.0,null,2026-01-09,2026-01-09,Second skill conversion
```

### 4. Updated DYN-BACKLOG.md

Refresh the backlog document with current state:

```markdown
# SYNCRESCENDENCE OPERATIONAL BACKLOG
## Persistent State for Oracle-Claude Coordination
**Last Updated**: 2026-01-09T[TIME]

---

## ACTIVE SPRINT: ORACLE 11 BLITZKRIEG

### Currently Executing (Parallel Streams)
- [x] Stream A (DIRECTIVE-042A): IIC Foundation (Acumen + Coherence)
- [x] Stream B (DIRECTIVE-042B): Multi-CLI Integration + System Prompt Correction
- [x] Stream C (DIRECTIVE-042C): Operational Hygiene + Ledger Updates
- [ ] Stream D (DIRECTIVE-042D): Gemini CLI Validation

### Projects Status
| Project | Status | Priority | Notes |
|---------|--------|----------|-------|
| PROJ-001 | COMPLETE | P1 | Transcript Ingestion (43 sources) |
| PROJ-002 | IN_PROGRESS | P1 | IIC Configuration (Oracle 11) |
| PROJ-011 | COMPLETE | P0 | Automation Infrastructure |
| PROJ-012 | IN_PROGRESS | P2 | Multi-CLI Integration |
| PROJ-016 | NOT_STARTED | P3 | Skills Conversion (new) |

---

## NEAR-TERM BACKLOG

### IIC Configuration (PROJ-002)
- [x] Acumen IIC specification
- [x] Coherence IIC specification
- [ ] Efficacy IIC specification
- [ ] Mastery IIC specification
- [ ] Transcendence IIC specification
- [ ] Cross-IIC communication testing

### Multi-CLI Integration (PROJ-012)
- [x] GEMINI.md created
- [x] gemini-settings.json template
- [x] Multi-CLI coordination protocol
- [ ] Gemini CLI validation (test directive)
- [ ] ChatGPT Codex evaluation (if available)

### Skills Conversion (PROJ-016)
- [ ] transcribe_youtube.xml → Claude Skill
- [ ] transcribe_interview.xml → Claude Skill
- [ ] integrate.xml → Claude Skill
- [ ] readize.xml → Claude Skill
- [ ] listenize.xml → Claude Skill

### System Maintenance
- [x] System prompt files corrected
- [x] Queue disposition complete
- [ ] Phase 3 content annealment (deferred)

---

## BLOCKED / DEFERRED

### Modal 2 Queue (Awaiting Visual Capabilities)
- AI_3D_VFX.md
- AI_Image_Generators.md
- AI_Workflows_in_Video_and_VFX.md
- Physical_AI.md
- QUEUE-36200-SCREENPLAY_ORCHESTRATION.md
- The_Next_Wave_in_AI_Video_and_VFX.md

### Blocked Projects
- PROJ-004 (Automation): Blocked by PROJ-003
- PROJ-005 (Branding): Blocked by PROJ-002
- PROJ-006 (Ontology): Blocked by PROJ-003
- PROJ-007 (Curriculum): Blocked by PROJ-006

---

## COMPLETED (Oracle 10-11)

### Oracle 10
- [x] PROJ-001: Transcript Ingestion (43 sources, pattern proven)
- [x] PROJ-011: Automation Infrastructure (CLAUDE.md, Makefile, etc.)

### Oracle 11 (In Progress)
- [x] Methodology integration (Review/Retro separation)
- [x] System prompt verification (discrepancy identified)
- [x] 02-OPERATIONAL triage
- [x] 03-QUEUE disposition analysis
- [x] Blitzkrieg directive package issued

---

## METRICS

### Execution Capacity
| Instance | Status | Zone |
|----------|--------|------|
| Claude Code 1 (Alpha) | Active | Stream A |
| Claude Code 2 (Beta) | Active | Stream B |
| Claude Code 3 (Gamma) | Active | Stream C |
| Gemini CLI (Delta) | Validating | Stream D |

### Project Health
| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Active projects | 3-5 | 3 | HEALTHY |
| Blocked projects | <3 | 4 | ACCEPTABLE |
| Complete projects | Increasing | 2 | HEALTHY |

### Ledger Integrity
| Ledger | Records | Last Verified |
|--------|---------|---------------|
| tasks.csv | 65+ | 2026-01-09 |
| projects.csv | 12 | 2026-01-09 |
| sources.csv | 184 | 2026-01-08 |

---

*Backlog updated after Oracle 11 Blitzkrieg issuance. Parallel execution in progress across 4 streams.*
```

---

## EXECUTION STEPS

### Phase 1: Queue Disposition (30 min)

1. Create 02-OPERATIONAL/surveys/ if not exists
2. Create 02-OPERATIONAL/queues/ if not exists
3. Move AI_ECOSYSTEM_SURVEY.md to 02-OPERATIONAL/surveys/
4. Merge CONTENT_PROCESSING_QUEUE.md into YOUTUBE_PROCESSING_BACKLOG.md
5. Move merged file to 02-OPERATIONAL/queues/
6. Move QUICK_WINS.md to 05-ARCHIVE/
7. Move AI_Academic_Research.md from modal2/ to modal1/
8. Delete empty modal1/ after moves complete
9. Verify final state

### Phase 2: Project Creation (15 min)

1. Add PROJ-016 to projects.csv
2. Verify CSV format and validation
3. Document scope in notes field

### Phase 3: Task Updates (30 min)

1. Add all TASK-050 through TASK-065 to tasks.csv
2. Follow atomic update protocol (temp → validate → rename)
3. Verify no duplicate IDs
4. Verify project_id references valid

### Phase 4: Backlog Refresh (30 min)

1. Update DYN-BACKLOG.md with complete current state
2. Mark completed items from Oracle 10-11
3. Add new projects and tasks
4. Update metrics section
5. Timestamp the update

### Phase 5: Verification and Output (15 min)

1. Verify all file movements complete
2. Verify CSVs validate
3. Copy updated files to /mnt/user-data/outputs/
4. Create execution log

---

## OUTPUT REQUIREMENTS

All files to: `/mnt/user-data/outputs/`

Files to produce:
1. `tasks.csv` (updated)
2. `projects.csv` (updated)
3. `DYN-BACKLOG.md` (updated)
4. `EXECUTION_LOG-2026-01-09-042C.md`

---

## SUCCESS CRITERIA

| Criterion | Verification |
|-----------|--------------|
| modal1/ files moved | ls -la 02-OPERATIONAL/surveys/, queues/ |
| QUICK_WINS.md archived | ls -la 05-ARCHIVE/ |
| PROJ-016 created | grep PROJ-016 projects.csv |
| New tasks added | wc -l tasks.csv shows increase |
| DYN-BACKLOG refreshed | Last Updated timestamp current |
| CSVs validate | No parse errors |

---

## LEDGER UPDATES

This directive IS the ledger update directive. Ensure all tasks from all streams are captured.

Final task count should be approximately 65 tasks (47 existing + 18 new).
Final project count should be 12 projects (11 existing + 1 new).

---

*Execute with precision. Ledger integrity enables coordination across all execution instances.*
