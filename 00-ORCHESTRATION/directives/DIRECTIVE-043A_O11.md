# DIRECTIVE-043A: INFRASTRUCTURE & OPERATIONS
## Oracle 11 | Blitzkrieg 043 | Stream A

**Issued**: 2026-01-09
**Oracle**: 11
**Stream**: A (Infrastructure/Operations)
**Parallel**: DIRECTIVE-043B (Content/Strategy)
**Status**: READY FOR EXECUTION

---

## EXECUTIVE SUMMARY

Stream A addresses foundational hygiene, ground truth restoration, and operational infrastructure expansion. These tasks must complete before or in parallel with Stream B's strategic work to ensure correct substrate for IIC configuration.

**Primary Objectives**:
1. **P0**: Restore system prompt ground truth (unified-prompt files)
2. **P2**: Validate Gemini CLI for multi-CLI expansion (PROJ-012)
3. **P3**: Queue cleanup and Skills conversion tracking
4. **P3**: Methodology documentation (Review/Retrospective separation)

**Estimated Duration**: 2-3 hours
**Dependencies**: synthesis-*.md files (provided in Oracle context)

---

## PHASE 1: SYSTEM PROMPT GROUND TRUTH RESTORATION [P0]

### 1.1 Problem Statement

The repository's `02-OPERATIONAL/prompts/unified/[Model]-unified-prompt.md` files are **NOT** the authoritative system prompts. Analysis confirms:

| File | Repository Version | Authoritative Version |
|------|-------------------|----------------------|
| ChatGPT-unified-prompt.md | 15KB, markdown prose | synthesis-chatgpt.md (25KB, structured) |
| Claude-unified-prompt.md | 9KB, markdown prose | synthesis-claude.md (14KB, XML structure) |
| Gemini-unified-prompt.md | 3KB, markdown | synthesis-gemini.md (2.5KB) |
| Grok-unified-prompt.md | 8KB, markdown | synthesis-grok.md (3.5KB) |

The synthesis files contain the correctly structured XML prompts with `<system_prompt>`, `<core_identity>`, `<cognitive_profile>`, and `<reasoning>` tags. The repository versions are earlier iterations or alternative syntheses.

### 1.2 Execution Steps

```bash
# Navigate to prompts directory
cd 02-OPERATIONAL/prompts/unified/

# Backup current (incorrect) files
mkdir -p ../../../05-ARCHIVE/prompt-backup-043A/
cp *-unified-prompt.md ../../../05-ARCHIVE/prompt-backup-043A/

# Copy synthesis files (from outputs or Principal drop)
# Principal will provide these files at root level
cp /path/to/synthesis-chatgpt.md ChatGPT-unified-prompt.md
cp /path/to/synthesis-claude.md Claude-unified-prompt.md
cp /path/to/synthesis-gemini.md Gemini-unified-prompt.md
cp /path/to/synthesis-grok.md Grok-unified-prompt.md

# Archive justification files (valuable documentation)
cp /path/to/justification-*.md ../../../05-ARCHIVE/

# Verify file sizes match expected
wc -c *-unified-prompt.md
# Expected: ChatGPT ~25KB, Claude ~14KB, Gemini ~2.5KB, Grok ~3.5KB

# Commit
git add -A
git commit -m "fix(prompts): restore authoritative synthesis system prompts

Replaces unified-prompt files with synthesis-[model].md versions.
- ChatGPT: 15KB → 25KB (XML structured)
- Claude: 9KB → 14KB (XML structured)
- Gemini: 3KB → 2.5KB (correct version)
- Grok: 8KB → 3.5KB (correct version)

Archives justification files for documentation.
Resolves DIRECTIVE-043A Phase 1."
```

### 1.3 Verification Checklist

- [ ] ChatGPT-unified-prompt.md starts with `<system_prompt>` tag
- [ ] Claude-unified-prompt.md contains `<cognitive_profile>` section
- [ ] Gemini-unified-prompt.md is properly formatted
- [ ] Grok-unified-prompt.md is properly formatted
- [ ] All four justification-*.md files in 05-ARCHIVE/
- [ ] Backup of previous versions preserved

### 1.4 Task Tracking

Create task entry:
```csv
TASK-055,null,Restore system prompt ground truth,task,done,P0,Claude_Code,null,0.5,{actual},2026-01-09,2026-01-09,Replaced unified-prompt files with synthesis versions per DIRECTIVE-043A
```

---

## PHASE 2: MULTI-CLI VALIDATION (PROJ-012) [P2]

### 2.1 Objective

Validate Gemini CLI operational capability and determine integration patterns for multi-CLI orchestration.

### 2.2 Gemini CLI Test Protocol

```bash
# Test 1: Basic connectivity
gemini --version
gemini auth status

# Test 2: Simple prompt execution
echo "What is 2+2?" | gemini chat

# Test 3: File processing capability
echo "Summarize this text: The quick brown fox jumps over the lazy dog." | gemini chat

# Test 4: JSON output mode
gemini chat --output-format json "List three programming languages"

# Test 5: Multi-turn capability
gemini chat --session test-session "Hello, I'm testing multi-turn."
gemini chat --session test-session "What did I just say?"
```

### 2.3 Capability Assessment Matrix

Complete this assessment:

| Capability | Claude Code | Gemini CLI | Notes |
|------------|-------------|------------|-------|
| File reading | ✓ | ? | Test with local files |
| File writing | ✓ | ? | Test output to disk |
| Multi-turn context | ✓ | ? | Test session persistence |
| JSON output | ✓ | ? | Test structured responses |
| Streaming | ✓ | ? | Test token streaming |
| Tool use | ✓ | ? | Test function calling |
| Code execution | ✓ | ? | Test code blocks |
| Max context | 200K | ? | Document limit |

### 2.4 GEMINI.md Draft

If tests pass, create initial GEMINI.md (equivalent to CLAUDE.md):

```markdown
# GEMINI.md - Constitutional Rules for Gemini CLI

## Repository Context
This is the Syncrescendence repository. Gemini CLI operates as a parallel executor.

## Core Rules

### Structural (ABSOLUTE)
1. FLAT PRINCIPLE: All directories must be flat. Use naming prefixes.
2. NUMBERED DIRECTORIES: Top-level directories are 00-06.
3. PROTECTED ZONES: 01-CANON/ requires Principal approval for changes.

### Operational (ABSOLUTE)
4. LEDGER GROUND TRUTH: tasks.csv and sources.csv are authoritative.
5. ATOMIC UPDATES: CSV updates use temp file → validate → rename.
6. COMMIT DISCIPLINE: Commit with semantic prefixes (feat:, fix:, docs:).

### Gemini-Specific
7. ZONE OWNERSHIP: Follow coordination.yaml zone assignments.
8. JSON OUTPUT: Prefer --output-format json for structured data.
9. SESSION MANAGEMENT: Use named sessions for multi-turn work.

## Default Operations

### Before Starting Work
1. Read this file
2. Check coordination.yaml for zone ownership
3. Pull latest from repository

### After Completing Work
1. Update relevant ledgers
2. Commit with semantic message
3. Push to branch per coordination.yaml

## Integration Points
- Claude Code: Primary deep reasoning, complex synthesis
- Gemini CLI: Fast structured output, data processing
- ChatGPT Codex: Code generation (if subscribed)
```

### 2.5 Decision Required: ChatGPT Plus/Codex

Document decision framework:

| Factor | Weight | Gemini CLI | Codex (if Plus) |
|--------|--------|------------|-----------------|
| Cost | High | Free | $20/month |
| Code gen quality | High | Good | Excellent |
| Speed | Medium | Fast | Very fast |
| Integration | Medium | CLI-native | CLI via API |
| Unique capability | Medium | Google integration | OpenAI ecosystem |

**Recommendation**: Complete Gemini CLI validation first. If it satisfies data processing needs, defer Codex subscription. Re-evaluate after 2 weeks of Gemini usage.

### 2.6 Task Tracking

```csv
TASK-053,PROJ-012,Test Gemini CLI basic operations,task,{status},P2,Claude_Code,null,1,{actual},2026-01-09,2026-01-09,DIRECTIVE-043A Phase 2
TASK-054,PROJ-012,Draft GEMINI.md,task,{status},P2,Claude_Code,TASK-053,0.5,{actual},2026-01-09,2026-01-09,DIRECTIVE-043A Phase 2
```

---

## PHASE 3: QUEUE CLEANUP [P3]

### 3.1 Current State

Per QUEUE_DISPOSITION.md, execution checklist incomplete:

```
03-QUEUE/
├── modal1/
│   ├── AI_ECOSYSTEM_SURVEY.md        → Move to 02-OPERATIONAL/surveys/
│   ├── CONTENT_PROCESSING_QUEUE.md   → Merge into YOUTUBE_PROCESSING_BACKLOG
│   ├── QUICK_WINS.md                 → Archive
│   └── YOUTUBE_PROCESSING_BACKLOG.md → Move to 02-OPERATIONAL/queues/
├── modal2/
│   └── [6 files - intentional deferral, DO NOT MOVE]
└── QUEUE_DISPOSITION.md              → Keep for reference
```

### 3.2 Execution Steps

```bash
# Create target directories (FLAT PRINCIPLE - no subdirectories within these)
mkdir -p 02-OPERATIONAL/surveys
mkdir -p 02-OPERATIONAL/queues

# Move operational documents
mv 03-QUEUE/modal1/AI_ECOSYSTEM_SURVEY.md 02-OPERATIONAL/surveys/
mv 03-QUEUE/modal1/YOUTUBE_PROCESSING_BACKLOG.md 02-OPERATIONAL/queues/

# Merge CONTENT_PROCESSING_QUEUE into YOUTUBE_PROCESSING_BACKLOG
# Append non-YouTube content section
cat 03-QUEUE/modal1/CONTENT_PROCESSING_QUEUE.md >> 02-OPERATIONAL/queues/YOUTUBE_PROCESSING_BACKLOG.md

# Archive QUICK_WINS
mv 03-QUEUE/modal1/QUICK_WINS.md 05-ARCHIVE/ARCHIVE-QUICK_WINS-2026-01-09.md

# Delete processed files from modal1
rm 03-QUEUE/modal1/CONTENT_PROCESSING_QUEUE.md

# Verify modal1 is empty
ls 03-QUEUE/modal1/
# Expected: empty or only .gitkeep

# Verify modal2 unchanged (6 files, intentional deferral)
ls 03-QUEUE/modal2/ | wc -l
# Expected: 6 or 7

# Commit
git add -A
git commit -m "chore(queue): complete modal1 disposition per QUEUE_DISPOSITION.md

- AI_ECOSYSTEM_SURVEY → OPERATIONAL/surveys/
- YOUTUBE_PROCESSING_BACKLOG → OPERATIONAL/queues/
- CONTENT_PROCESSING_QUEUE merged into YOUTUBE_PROCESSING_BACKLOG
- QUICK_WINS archived with timestamp
- modal2 unchanged (intentional deferral)

Resolves DIRECTIVE-043A Phase 3."
```

### 3.3 Verification Checklist

- [ ] 02-OPERATIONAL/surveys/AI_ECOSYSTEM_SURVEY.md exists
- [ ] 02-OPERATIONAL/queues/YOUTUBE_PROCESSING_BACKLOG.md exists
- [ ] 03-QUEUE/modal1/ is empty (or only .gitkeep)
- [ ] 03-QUEUE/modal2/ has 6-7 files (unchanged)
- [ ] 05-ARCHIVE/ARCHIVE-QUICK_WINS-2026-01-09.md exists

---

## PHASE 4: SKILLS CONVERSION TRACKING [P3]

### 4.1 Create PROJ-016

Skills conversion identified as valuable but deferred. Create project for tracking:

```csv
PROJ-016,Skills Conversion,initiative,not_started,P3,Oracle12+,null,12+,modal1,null,2026-01-09,2026-01-09,Convert top 5 functions to Claude Skills format (transcribe_youtube; transcribe_interview; integrate; readize; listenize)
```

### 4.2 Associated Tasks (For Future Oracle)

```csv
TASK-057,PROJ-016,Create skills/claude/ directory structure,task,not_started,P3,Claude_Code,null,0.5,null,2026-01-09,2026-01-09,Structure: skills/claude/{transcription;synthesis;transformation}/
TASK-058,PROJ-016,Convert transcribe_youtube.xml to Skill,task,not_started,P3,Claude_Code,TASK-057,1,null,2026-01-09,2026-01-09,Add YAML frontmatter; test activation accuracy
TASK-059,PROJ-016,Convert transcribe_interview.xml to Skill,task,not_started,P3,Claude_Code,TASK-057,1,null,2026-01-09,2026-01-09,Add YAML frontmatter; test activation accuracy
TASK-060,PROJ-016,Convert integrate.xml to Skill,task,not_started,P3,Claude_Code,TASK-057,1,null,2026-01-09,2026-01-09,Add YAML frontmatter; test activation accuracy
TASK-061,PROJ-016,Convert readize.xml to Skill,task,not_started,P3,Claude_Code,TASK-057,0.5,null,2026-01-09,2026-01-09,Add YAML frontmatter; test activation accuracy
TASK-062,PROJ-016,Convert listenize.xml to Skill,task,not_started,P3,Claude_Code,TASK-057,0.5,null,2026-01-09,2026-01-09,Add YAML frontmatter; test activation accuracy
```

### 4.3 No Immediate Action Required

This phase creates tracking entries only. Execution deferred to Oracle 12+.

---

## PHASE 5: METHODOLOGY DOCUMENTATION [P3]

### 5.1 Objective

Document the adopted Review/Retrospective methodology as operational protocol.

### 5.2 Create REF-METHODOLOGY.md

```bash
cat > 00-ORCHESTRATION/state/REF-METHODOLOGY.md << 'EOF'
# REF-METHODOLOGY
## Sprint-Bounded Kanban with Review/Retrospective Separation

**Version**: 1.0
**Adopted**: Oracle 11 (2026-01-09)

---

## Framework Overview

Syncrescendence adopts a hybrid methodology synthesized from Scrum, Kanban, XP, and Lean principles:

| Component | Source | Implementation |
|-----------|--------|----------------|
| Sprint boundaries | Scrum | Oracle sessions = Sprint |
| Kanban visualization | Kanban | Ledger-based flow tracking |
| Atomic feedback | XP | make verify + TDD-like ledger checks |
| Continuous improvement | Lean/Kaizen | Built into Oracle transitions |

---

## Structural Mapping

```
ORACLE SESSION = Sprint
├── BLITZKRIEG = Sprint Increment
│   └── Parallel A/B streams (XP-like pairing concept)
├── ORACLE CONTEXT VERSIONING = Continuous Documentation
├── ORACLE CULMINATION = Sprint Review (product validation)
└── ORACLE INIT (next) = Sprint Retrospective (process optimization)
```

---

## Review vs Retrospective

### Sprint Review (Oracle Culmination)
**Function**: Product validation - "Are we building the right thing?"
**Focus**: Deliverables, outcomes, CANON quality
**Participants**: Principal + Oracle
**Output**: Updated backlog, validated deliverables

### Sprint Retrospective (Oracle Init)
**Function**: Process optimization - "Are we building it right?"
**Focus**: Methodology, efficiency, bottleneck removal
**Participants**: Principal + Oracle (informed by execution logs)
**Output**: Process improvements, methodology refinements

---

## Operational Cadence

### Daily (When Active)
- Blitzkrieg execution
- Ledger updates
- make verify before commits

### Per-Blitzkrieg
- Parallel A/B execution
- Execution log creation
- Context versioning

### Per-Oracle
- Culmination (Review)
- Init (Retrospective)
- Backlog refinement

### Quarterly
- 18-lens strategic review
- Project prioritization
- Chain development assessment

---

## 18-Lens Integration

All significant decisions evaluated against 18 lenses. Key lenses for methodology:

| Lens | Methodology Implication |
|------|------------------------|
| #12 Industrial Engineering | Identifies bottleneck (Principal relay) |
| #14 Permaculture | Self-sustaining patterns via automation |
| #16 Agile | Minimum viable increments |
| #17 Lean | Waste elimination |

---

## Feedback Granularity

| Type | Frequency | Trigger |
|------|-----------|---------|
| Atomic (ledger check) | Per commit | make verify |
| Incremental (blitzkrieg) | Per directive | Execution log |
| Sprint (Oracle) | Per session | Culmination + Init |
| Strategic (18-lens) | Quarterly | Review session |

---

*Adopted Oracle 11 | Source: additions.md synthesis + 18-lens evaluation*
EOF

git add 00-ORCHESTRATION/state/REF-METHODOLOGY.md
git commit -m "docs(methodology): document Review/Retrospective framework

Sprint-bounded Kanban with explicit separation:
- Culmination = Review (product validation)
- Init = Retrospective (process optimization)
- XP atomic feedback via make verify
- Lean continuous improvement

Resolves DIRECTIVE-043A Phase 5."
```

---

## PHASE 6: LEDGER SYNCHRONIZATION

### 6.1 Update projects.csv

Add PROJ-016:

```csv
PROJ-016,Skills Conversion,initiative,not_started,P3,Oracle12+,null,12+,modal1,null,2026-01-09,2026-01-09,Convert top 5 functions to Claude Skills format
```

### 6.2 Update tasks.csv

Add all new tasks from this directive:

```csv
TASK-055,null,Restore system prompt ground truth,task,done,P0,Claude_Code,null,0.5,{actual},2026-01-09,2026-01-09,Phase 1 - system prompts restored
TASK-053,PROJ-012,Test Gemini CLI basic operations,task,{status},P2,Claude_Code,null,1,{actual},2026-01-09,2026-01-09,Phase 2
TASK-054,PROJ-012,Draft GEMINI.md,task,{status},P2,Claude_Code,TASK-053,0.5,{actual},2026-01-09,2026-01-09,Phase 2
TASK-063,null,Complete queue disposition,task,done,P3,Claude_Code,null,0.5,{actual},2026-01-09,2026-01-09,Phase 3 - modal1 cleared
TASK-064,null,Document methodology,task,done,P3,Claude_Code,null,0.5,{actual},2026-01-09,2026-01-09,Phase 5 - REF-METHODOLOGY created
TASK-057,PROJ-016,Create skills/claude/ directory structure,task,not_started,P3,Claude_Code,null,0.5,null,2026-01-09,2026-01-09,Deferred to Oracle 12+
TASK-058,PROJ-016,Convert transcribe_youtube.xml to Skill,task,not_started,P3,Claude_Code,TASK-057,1,null,2026-01-09,2026-01-09,Deferred
TASK-059,PROJ-016,Convert transcribe_interview.xml to Skill,task,not_started,P3,Claude_Code,TASK-057,1,null,2026-01-09,2026-01-09,Deferred
TASK-060,PROJ-016,Convert integrate.xml to Skill,task,not_started,P3,Claude_Code,TASK-057,1,null,2026-01-09,2026-01-09,Deferred
TASK-061,PROJ-016,Convert readize.xml to Skill,task,not_started,P3,Claude_Code,TASK-057,0.5,null,2026-01-09,2026-01-09,Deferred
TASK-062,PROJ-016,Convert listenize.xml to Skill,task,not_started,P3,Claude_Code,TASK-057,0.5,null,2026-01-09,2026-01-09,Deferred
```

### 6.3 Use Atomic Update Pattern

```bash
# Use sync_ledgers.py or manual atomic pattern
cd 00-ORCHESTRATION/state/

# Backup
cp projects.csv projects.csv.bak.$(date +%s)
cp tasks.csv tasks.csv.bak.$(date +%s)

# Update (append new rows)
# ... edits ...

# Validate
python3 -c "import csv; list(csv.DictReader(open('projects.csv')))"
python3 -c "import csv; list(csv.DictReader(open('tasks.csv')))"

# Commit
git add projects.csv tasks.csv
git commit -m "chore(ledgers): update for DIRECTIVE-043A

- Added PROJ-016 (Skills Conversion)
- Added TASK-053 through TASK-064
- Marked Phase 1,3,5 tasks as done"
```

---

## EXECUTION LOG TEMPLATE

Create execution log upon completion:

```markdown
# EXECUTION_LOG-2026-01-09-043A.md

**Directive**: DIRECTIVE-043A_INFRASTRUCTURE_OPERATIONS
**Executor**: Claude Code (Alpha)
**Date**: 2026-01-09
**Duration**: {actual_time}

## Summary
Stream A addressed infrastructure hygiene and operational expansion.

## Phase Completion

| Phase | Status | Notes |
|-------|--------|-------|
| 1. System Prompts | ✓/✗ | {notes} |
| 2. Gemini CLI | ✓/✗ | {notes} |
| 3. Queue Cleanup | ✓/✗ | {notes} |
| 4. Skills Tracking | ✓/✗ | {notes} |
| 5. Methodology | ✓/✗ | {notes} |
| 6. Ledgers | ✓/✗ | {notes} |

## Files Changed
- {list}

## Commits
- {list}

## Blockers/Issues
- {if any}

## Handoff to Stream B
Stream A complete. No blocking dependencies for Stream B (IIC Configuration).
```

---

## VERIFICATION COMMANDS

```bash
# Final verification
make verify

# Specific checks
ls 02-OPERATIONAL/prompts/unified/
wc -c 02-OPERATIONAL/prompts/unified/*-unified-prompt.md
ls 02-OPERATIONAL/surveys/
ls 02-OPERATIONAL/queues/
ls 03-QUEUE/modal1/
cat 00-ORCHESTRATION/state/REF-METHODOLOGY.md | head -20
grep "PROJ-016" 00-ORCHESTRATION/state/projects.csv
grep "TASK-05" 00-ORCHESTRATION/state/tasks.csv
```

---

## SUCCESS CRITERIA

| Criterion | Target |
|-----------|--------|
| System prompts corrected | 4 files with correct content |
| Gemini CLI validated | Test results documented |
| modal1 cleared | 0 files (or .gitkeep only) |
| PROJ-016 created | Entry in projects.csv |
| REF-METHODOLOGY exists | Document in state/ |
| All commits semantic | feat:/fix:/docs:/chore: prefixes |

---

*DIRECTIVE-043A ready for execution. Parallel with DIRECTIVE-043B.*
