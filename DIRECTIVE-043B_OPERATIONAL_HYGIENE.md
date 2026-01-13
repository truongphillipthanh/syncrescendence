# DIRECTIVE-043B: OPERATIONAL HYGIENE & RESEARCH INTEGRATION
## Stream B — Claude 3 (Beta)

**Issued**: 2026-01-11
**Authority**: Oracle 12 under Principal direction
**Stream**: B (Claude 3)
**Priority**: P0 — Repository Consolidation
**Estimated Duration**: 60-90 minutes
**Parallel**: DIRECTIVE-043A executing simultaneously on Claude 2

---

## DECISION CONTEXT

### Principal's Actual Words
> "somewhere along the line, we'll need to audit and anneal the corpus again, the semantic content of it for alignment/congruence, as well as lean/optimization/streamlining"

> "the reports that were attached ought to be canonized, these were key, persistent signals that required constant surveillance before"

> "completely survey for ground truth every single past Oracle conversation, especially my inputs, to in a meta way understand all of these decisions"

### Oracle's Interpretation
The research documents (frontier_models.md, platform_features.md, cognitive_profile.md) and Strategic Reconnaissance Report represent high-resolution intelligence that should be canonized. Additionally, repository hygiene is needed before ChatGPT Plus onboarding.

### 18-Lens Evaluation
- **Lens 17 (Lean)**: Eliminate waste — consolidate research into canonical form
- **Lens 14 (Permaculture)**: Research integrated = self-sustaining intelligence
- **Lens 8 (Elegance)**: Clean repository = developer happiness

---

## PHASE 1: RESEARCH CANONIZATION
**Duration**: ~30 minutes

### Task 1.1: Assess Research Documents

The following documents were produced/integrated in Oracle 11-12:
1. `frontier_models.md` (1,459 lines) — Model capabilities, benchmarks, community sentiment
2. `platform_features.md` (1,948 lines) — Surface inventory, memory, rate limits, MCP
3. `cognitive_profile.md` (84 lines) — Principal's operating requirements
4. `STRATEGIC_RECONNAISSANCE_REPORT_ENHANCED.md` (597 lines) — Synthesis document

**Disposition Decision**:
- `cognitive_profile.md` → Integrate into CANON-35120-NEURODIVERGENT (already exists) OR create satellite
- `frontier_models.md` → Create CANON-30XXX under Intelligence chain (temporal, but foundational)
- `platform_features.md` → Integrate into CANON-31142-PLATFORM_GRAMMAR or create update
- `STRATEGIC_RECONNAISSANCE_REPORT_ENHANCED.md` → Archive as ARCH-RECONNAISSANCE_2026-01

### Task 1.2: Update CANON-35120-NEURODIVERGENT

The cognitive_profile.md contains:
- Coherence-first processing
- Field-based cognition
- Language as phase transition
- Interruption cost model
- Energy economics

These concepts should be cross-referenced in CANON-35120 if not already present.

### Task 1.3: Create ARCH-RECONNAISSANCE_2026-01.md

Archive the Strategic Reconnaissance Report with proper metadata:

```markdown
---
archive_id: ARCH-RECONNAISSANCE_2026-01
title: Strategic Reconnaissance Report - Oracle 12 Campaign Phase 1
date: 2026-01-11
source: Oracle 12
type: synthesis
status: archived
superseded_by: null
cross_refs:
  - CANON-25200-CONSTELLATION_ARCH
  - CANON-31142-PLATFORM_GRAMMAR
synopsis: Integration of frontier model capabilities, platform features, and cognitive architecture research
---

[Content of STRATEGIC_RECONNAISSANCE_REPORT_ENHANCED.md]
```

### Task 1.4: Update CANON-31142-PLATFORM_GRAMMAR

The platform_features.md contains detailed feature topology that should update the existing platform grammar document. Key additions:
- Claude Trifurcation (web/desktop/CLI)
- Rate limit sharing (~45/5hr across surfaces)
- Gemini YouTube native processing (263 tok/sec video)
- ChatGPT Codex CLI details
- MCP ecosystem state

---

## PHASE 2: REPOSITORY HYGIENE
**Duration**: ~20 minutes

### Task 2.1: Audit Root Level

```bash
# Survey root-level files
ls -la *.md *.csv *.yaml *.xml *.py *.sh | wc -l

# Categorize by prefix
ls *.md | grep -E "^CANON-" | wc -l
ls *.md | grep -E "^ARCH-" | wc -l
ls *.md | grep -E "^DYN-" | wc -l
ls *.md | grep -E "^REF-" | wc -l
ls *.md | grep -E "^DIRECTIVE-" | wc -l
ls *.md | grep -E "^EXECUTION_LOG-" | wc -l
ls *.md | grep -E "^SCAFF-" | wc -l

# Identify orphans (no standard prefix)
ls *.md | grep -v -E "^(CANON-|ARCH-|DYN-|REF-|DIRECTIVE-|EXECUTION_LOG-|SCAFF-|README|CLAUDE|index)"
```

### Task 2.2: Consolidate Orphan Files

Any files without standard prefixes should be:
1. Assigned appropriate prefix (ARCH-, REF-, etc.)
2. OR integrated into existing CANON
3. OR deleted if superseded

Common patterns to address:
- `AI_*.md` files → Move to appropriate CANON or ARCH
- `*-unified-prompt.md` files → Verify still needed
- `justification-*.md` files → Archive or integrate
- `MODEL_PROFILE-*.yaml` → Verify referenced in CANON-30xxx

### Task 2.3: Verify Ledger Consistency

```bash
# Count projects
wc -l projects.csv
cat projects.csv | grep -c "complete"
cat projects.csv | grep -c "not_started"
cat projects.csv | grep -c "blocked"

# Count tasks
wc -l tasks.csv
cat tasks.csv | grep -c "done"
cat tasks.csv | grep -c "in_progress"
cat tasks.csv | grep -c "not_started"

# Verify no orphan tasks (tasks without valid project)
# [manual verification]
```

---

## PHASE 3: SCAFFOLD METABOLISM
**Duration**: ~15 minutes

### Principal's Context
> "The actual semantic content of /05-ARCHIVE needs to be digested into coherence. It cannot be a junk drawer. Each token must fight and achieve teleology."

### Task 3.1: Audit SCAFF-* Files

```bash
ls SCAFF-*.md | wc -l
```

SCAFF files are temporary scaffolding from previous Oracles. Assess each:
- **SCAFF-ALPHA_***: Oracle 5 phase work — likely superseded
- **SCAFF-BETA_***: Oracle 5 phase work — likely superseded
- **SCAFF-ORACLE***: Historical Oracle culminations — archive or delete
- **SCAFF-*_REPORT.md**: One-time reports — archive if valuable, delete if not

### Task 3.2: Apply Metabolism

For each SCAFF file:
1. **Extract** any unique value not captured elsewhere
2. **Integrate** into appropriate CANON if valuable
3. **DELETE** the SCAFF file (metabolism complete)

Document in execution log which files were metabolized and disposition.

---

## PHASE 4: EXECUTION LOG ARCHAEOLOGY
**Duration**: ~10 minutes

### Task 4.1: Audit Execution Logs

```bash
ls EXECUTION_LOG-*.md | wc -l
ls EXECUTION_LOG-*.md | head -10
ls EXECUTION_LOG-*.md | tail -10
```

### Task 4.2: Assess Execution Log Value

Execution logs serve:
1. **Audit trail**: What was attempted when
2. **Pattern detection**: What works, what fails
3. **Retrospective**: Learning from past directives

**Recommendation**: Keep but consolidate into monthly archives if count exceeds 30.

---

## PHASE 5: VERIFICATION & LOG
**Duration**: ~10 minutes

### Task 5.1: Final Repository State

```bash
# Count all markdown files
ls *.md | wc -l

# Count by category
echo "CANON:" && ls CANON-*.md | wc -l
echo "ARCH:" && ls ARCH-*.md | wc -l
echo "REF:" && ls REF-*.md | wc -l
echo "DIRECTIVE:" && ls DIRECTIVE-*.md | wc -l
echo "EXECUTION_LOG:" && ls EXECUTION_LOG-*.md | wc -l
echo "DYN:" && ls DYN-*.md | wc -l
echo "SCAFF:" && ls SCAFF-*.md | wc -l
echo "Other:" && ls *.md | grep -v -E "^(CANON-|ARCH-|DYN-|REF-|DIRECTIVE-|EXECUTION_LOG-|SCAFF-)" | wc -l

# Verify flat principle
find . -type d -mindepth 1 | grep -v ".git" | grep -v ".claude"
```

### Task 5.2: Update Ledgers

Update tasks.csv:

```csv
TASK-054,null,Canonize research documents,processing,in_progress,P0,Claude_Code_3,null,1.0,null,2026-01-11,2026-01-11,DIRECTIVE-043B Phase 1
TASK-055,null,Repository hygiene audit,hygiene,in_progress,P1,Claude_Code_3,null,0.5,null,2026-01-11,2026-01-11,DIRECTIVE-043B Phase 2
TASK-056,null,Metabolize SCAFF files,processing,in_progress,P1,Claude_Code_3,null,0.5,null,2026-01-11,2026-01-11,DIRECTIVE-043B Phase 3
TASK-057,null,Create DIRECTIVE-043B execution log,documentation,in_progress,P2,Claude_Code_3,null,0.25,null,2026-01-11,2026-01-11,DIRECTIVE-043B Phase 5
```

### Task 5.3: Create Execution Log

Create `EXECUTION_LOG-2026-01-11-043B.md`:

```markdown
# EXECUTION LOG: DIRECTIVE-043B
**Date**: 2026-01-11
**Stream**: B (Claude 3)
**Directive**: 043B - Operational Hygiene & Research Integration
**Status**: [COMPLETE/PARTIAL]

## Phase 1: Research Canonization
| Document | Disposition | Integrated Into |
|----------|-------------|-----------------|
| cognitive_profile.md | [disposition] | [target] |
| frontier_models.md | [disposition] | [target] |
| platform_features.md | [disposition] | [target] |
| STRATEGIC_RECONNAISSANCE_REPORT_ENHANCED.md | [disposition] | [target] |

## Phase 2: Repository Hygiene
| Metric | Before | After |
|--------|--------|-------|
| Total .md files | [count] | [count] |
| Orphan files | [count] | [count] |
| SCAFF files | [count] | [count] |

## Phase 3: SCAFF Metabolism
| File | Disposition | Reason |
|------|-------------|--------|
| SCAFF-*.md | [DELETE/ARCHIVE/KEEP] | [reason] |

## Phase 4: Execution Log Review
- Total logs: [count]
- Recommendation: [action]

## Verification
[paste output of verification commands]

## Duration
Start: [time]
End: [time]
Total: [minutes]
```

---

## SUCCESS CRITERIA

This directive is complete when:
- [ ] Research documents assessed and canonized/archived
- [ ] CANON-31142 updated with platform feature additions
- [ ] ARCH-RECONNAISSANCE_2026-01.md created
- [ ] Repository hygiene audit complete
- [ ] SCAFF files metabolized (extract value → delete)
- [ ] Orphan files addressed (prefixed or integrated)
- [ ] tasks.csv includes TASK-054-057 marked done
- [ ] Execution log created with verification evidence
- [ ] Flat principle verified (no new subdirectories)

---

*Stream B consolidates intelligence and prepares clean foundation for platform expansion.*
