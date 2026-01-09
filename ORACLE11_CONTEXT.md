# ORACLE 11 CONTEXT
## Blitzkrieg 043 Deployment Package

**Oracle**: 11
**Date**: 2026-01-09
**Blitzkrieg**: 043
**Status**: READY FOR DEPLOYMENT

---

## DEPLOYMENT INSTRUCTIONS

### For Principal

1. **Download all files** from this package
2. **Drop into repository root**:
   - `synthesis-*.md` files
   - `justification-*.md` files  
   - `DIRECTIVE-043A_INFRASTRUCTURE_OPERATIONS.md`
   - `DIRECTIVE-043B_CONTENT_STRATEGY.md`
   - `ORACLE11_CONTEXT.md` (this file)

3. **Deploy to Claude Code instances**:
   - **Stream A** (Alpha instance): DIRECTIVE-043A
   - **Stream B** (Beta instance): DIRECTIVE-043B

4. **Monitor execution**:
   - Check execution logs as they appear
   - Resolve any blockers flagged

### For Claude Code (Alpha - Stream A)

```bash
# Read directive
cat DIRECTIVE-043A_INFRASTRUCTURE_OPERATIONS.md

# Execute phases 1-6
# Phase 1: System prompt correction (P0)
# Phase 2: Gemini CLI validation (P2)
# Phase 3: Queue cleanup (P3)
# Phase 4: Skills tracking (P3)
# Phase 5: Methodology documentation (P3)
# Phase 6: Ledger synchronization

# Create execution log
# Commit with semantic messages
```

### For Claude Code (Beta - Stream B)

```bash
# Read directive
cat DIRECTIVE-043B_CONTENT_STRATEGY.md

# Execute phases 1-6
# Phase 1: CANON reconnaissance (P1)
# Phase 2: Memory architecture decisions (P1)
# Phase 3: Acumen IIC configuration (P1)
# Phase 4: Multi-account sync patterns (P2)
# Phase 5: Ledger updates (P1)
# Phase 6: Reconnaissance deliverable

# Create execution log
# Commit with semantic messages
```

---

## CONTEXT SUMMARY

### What Oracle 11 Inherits

| Component | Status | Location |
|-----------|--------|----------|
| CLAUDE.md | ✓ | Root |
| Makefile | ✓ | Root |
| coordination.yaml | ✓ | config/ |
| Ledgers | ✓ | 00-ORCHESTRATION/state/ |
| 6 automation scripts | ✓ | 00-ORCHESTRATION/scripts/ |

### What Oracle 11 Addresses

| Priority | Focus | Directive |
|----------|-------|-----------|
| **P0** | System prompt ground truth | 043A Phase 1 |
| **P1** | PROJ-002 IIC Configuration | 043B Phases 1-3 |
| **P2** | PROJ-012 Multi-CLI | 043A Phase 2 |
| **P2** | PROJ-014 Multi-Account | 043B Phase 4 |
| **P3** | Queue cleanup | 043A Phase 3 |
| **P3** | Skills tracking | 043A Phase 4 |
| **P3** | Methodology documentation | 043A Phase 5 |

### Methodology Adopted

**Sprint-Bounded Kanban with Review/Retrospective Separation**

- Oracle Culmination = Sprint Review (product validation)
- Oracle Init = Sprint Retrospective (process optimization)
- Blitzkrieg = Sprint Increment
- make verify = XP-like atomic validation

---

## CRITICAL CORRECTIONS

### System Prompts

The repository's `02-OPERATIONAL/prompts/unified/[Model]-unified-prompt.md` files are **NOT** authoritative.

**Correct files** (included in this package):
- `synthesis-chatgpt.md` → replaces `ChatGPT-unified-prompt.md`
- `synthesis-claude.md` → replaces `Claude-unified-prompt.md`
- `synthesis-gemini.md` → replaces `Gemini-unified-prompt.md`
- `synthesis-grok.md` → replaces `Grok-unified-prompt.md`

**Justification files** (archive to 05-ARCHIVE/):
- `justification-chatgpt.md`
- `justification-claude.md`
- `justification-gemini.md`
- `justification-grok.md`

---

## KEY REFERENCES

### PROJ-002 (IIC Configuration)

| Document | ID | Purpose |
|----------|----|----|
| IIC Constellation | CANON-31140 | Core framework |
| Five-Account | CANON-31141 | Account specs |
| Platform Grammar | CANON-31142 | Platform rules |
| Feed Curation | CANON-31143 | Content streams |
| Memory Architecture | CANON-25000 | Memory layers |
| Context Transfer | CANON-25100 | Continuity |

### PROJ-012 (Multi-CLI)

| Platform | Status | Decision |
|----------|--------|----------|
| Claude Code | Operational | Primary |
| Gemini CLI | To validate | Test in 043A |
| ChatGPT Codex | Pending | Defer until Gemini validated |

### PROJ-014 (Multi-Account)

| Account | Role | Zone |
|---------|------|------|
| Claude 1 | Primary | Alpha + General |
| Claude 2 | Overflow | Beta |
| Claude 3 | Overflow/Verify | Gamma |

---

## SUCCESS METRICS (Blitzkrieg 043)

| Metric | Target | Stream |
|--------|--------|--------|
| System prompts corrected | 4 files | A |
| Gemini CLI validated | Decision made | A |
| modal1 cleared | 0 files | A |
| REF-METHODOLOGY created | Yes | A |
| CANON reviewed | 8 documents | B |
| SCAFF-IIC_RECONNAISSANCE | Complete | B |
| Acumen memory config | Created | B |
| REF-MULTI_ACCOUNT_SYNC | Created | B |
| PROJ-002 status | IN_PROGRESS | B |

---

## LEDGER DELTAS

### projects.csv Additions

```csv
PROJ-016,Skills Conversion,initiative,not_started,P3,Oracle12+,null,12+,modal1,null,2026-01-09,2026-01-09,Convert top 5 functions to Claude Skills
```

### projects.csv Updates

```csv
# Update PROJ-002 status:
PROJ-002,IIC Configuration,initiative,in_progress,P1,Oracle11,null,11,modal1,2026-02-01,2025-12-29,2026-01-09,Phase 1 reconnaissance complete
```

### tasks.csv Additions (043A)

```csv
TASK-055,null,Restore system prompt ground truth,task,{status},P0,Claude_Code,null,0.5,{actual},2026-01-09,2026-01-09,Phase 1
TASK-053,PROJ-012,Test Gemini CLI basic operations,task,{status},P2,Claude_Code,null,1,{actual},2026-01-09,2026-01-09,Phase 2
TASK-054,PROJ-012,Draft GEMINI.md,task,{status},P2,Claude_Code,TASK-053,0.5,{actual},2026-01-09,2026-01-09,Phase 2
TASK-063,null,Complete queue disposition,task,{status},P3,Claude_Code,null,0.5,{actual},2026-01-09,2026-01-09,Phase 3
TASK-064,null,Document methodology,task,{status},P3,Claude_Code,null,0.5,{actual},2026-01-09,2026-01-09,Phase 5
TASK-057,PROJ-016,Create skills/claude/ directory,task,not_started,P3,Claude_Code,null,0.5,null,2026-01-09,2026-01-09,Deferred
TASK-058,PROJ-016,Convert transcribe_youtube.xml,task,not_started,P3,Claude_Code,TASK-057,1,null,2026-01-09,2026-01-09,Deferred
TASK-059,PROJ-016,Convert transcribe_interview.xml,task,not_started,P3,Claude_Code,TASK-057,1,null,2026-01-09,2026-01-09,Deferred
TASK-060,PROJ-016,Convert integrate.xml,task,not_started,P3,Claude_Code,TASK-057,1,null,2026-01-09,2026-01-09,Deferred
TASK-061,PROJ-016,Convert readize.xml,task,not_started,P3,Claude_Code,TASK-057,0.5,null,2026-01-09,2026-01-09,Deferred
TASK-062,PROJ-016,Convert listenize.xml,task,not_started,P3,Claude_Code,TASK-057,0.5,null,2026-01-09,2026-01-09,Deferred
```

### tasks.csv Additions (043B)

```csv
TASK-050,PROJ-002,Review IIC-related CANON documents,task,{status},P1,Oracle11,null,2,{actual},2026-01-09,2026-01-09,Phase 1
TASK-051,PROJ-002,Map memory layer hierarchy,task,{status},P1,Oracle11,null,1,{actual},2026-01-09,2026-01-09,Phase 2
TASK-052,PROJ-002,Configure Acumen IIC,task,{status},P1,Claude_Code,TASK-051,2,{actual},2026-01-09,2026-01-09,Phase 3
TASK-065,PROJ-002,Configure Coherence IIC,task,not_started,P1,Claude_Code,TASK-052,2,null,2026-01-09,2026-01-09,Future
TASK-066,PROJ-002,Configure Efficacy IIC,task,not_started,P2,Claude_Code,TASK-065,2,null,2026-01-09,2026-01-09,Future
TASK-067,PROJ-002,Configure Mastery IIC,task,not_started,P2,Claude_Code,TASK-066,2,null,2026-01-09,2026-01-09,Future
TASK-068,PROJ-002,Configure Transcendence IIC,task,not_started,P3,Claude_Code,TASK-067,2,null,2026-01-09,2026-01-09,Future
TASK-069,PROJ-014,Document multi-account sync protocol,task,{status},P2,Oracle11,null,1,{actual},2026-01-09,2026-01-09,Phase 4
TASK-070,PROJ-014,Test cross-account context resumption,task,not_started,P2,Claude_Code,TASK-069,1,null,2026-01-09,2026-01-09,Future
TASK-071,PROJ-014,Create utilization schedule,task,not_started,P3,Claude_Code,TASK-070,0.5,null,2026-01-09,2026-01-09,Future
```

---

## POST-BLITZKRIEG CHECKLIST

After both streams complete:

- [ ] Verify system prompts corrected (043A)
- [ ] Verify Gemini CLI decision documented (043A)
- [ ] Verify modal1 cleared (043A)
- [ ] Verify REF-METHODOLOGY exists (043A)
- [ ] Verify SCAFF-IIC_RECONNAISSANCE complete (043B)
- [ ] Verify acumen-memory-config.md created (043B)
- [ ] Verify REF-MULTI_ACCOUNT_SYNC created (043B)
- [ ] Verify PROJ-002 status is IN_PROGRESS (043B)
- [ ] Verify all ledgers updated
- [ ] Run `make verify` for clean state
- [ ] Create Oracle 11 versioned context (v2)

---

*Oracle 11 Context | Blitzkrieg 043 | Ready for deployment*
