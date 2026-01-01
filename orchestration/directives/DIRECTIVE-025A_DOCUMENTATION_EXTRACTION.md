# DIRECTIVE-025A: DOCUMENTATION & EXTRACTION STREAM
## Claude 2 (Desktop) Initialization
**Issued**: 2025-12-31
**Authority**: Oracle7 under Principal direction
**Classification**: CRITICAL — Context Engineering Remediation
**Parallel Stream**: Claude 3 handles structural execution (DIRECTIVE-025B)

---

## DECISION CONTEXT

### Principal's Actual Words
> "This is not some simple nominal or tactical fix. REVIEW EVERY CONVERSATION... The repository is incredibly awful, all adhoc, virtually unchanged."

> "Given such abject failure of context engineering go to the maximum resolution."

> "Whenever you give your directives to the Claude, those directions HAVE to ALSO codify what we have decided and our logic and reasoning and rationale and conclusions."

> "The Claudes have no visibility into our decisions. The repository was supposed to be a Foyer, where all context is accessible."

### Oracle's Interpretation
Seven Oracle threads produced strategic decisions, but context engineering failed catastrophically. Claudes executing directives had no visibility into WHY decisions were made. The repository—supposed to be a "Foyer" where all context is accessible—lacked decision documentation. This directive establishes maximum-resolution documentation.

### Alternatives Considered
1. **Minimal documentation (going forward only)** — Rejected: Doesn't remediate 7 threads of lost context
2. **Summary-level documentation** — Rejected: Violates "maximum resolution" instruction
3. **Retroactive + prospective comprehensive documentation** — CHOSEN

### Rationale (18-Lens Summary)
| Lens | Score | Notes |
|------|-------|-------|
| Syncrescendent Route | ✓ | Restores continuity |
| Bitter Lesson | ✓ | Documentation scales |
| Antifragile | ✓ | Gains from chaos (more decisions = more learnings) |
| Meet the Moment | ✓ | Claudes need visibility NOW |
| Steelman/Redteam | ✓ | Documents alternatives considered |
| Personal Idiosyncrasies | ✓ | Provides holistic context |
| Potency w/o Resolution Loss | ✓ | Maximum resolution preserved |
| Agentify + Human-Navigable | ✓ | Repository becomes self-explanatory |
| Systems Thinking | ✓ | Documentation IS visibility mechanism |
| Lean | ✓ | Eliminates rework from lost context |

**Score**: 18/18 — Approved

### Implicit Agreements
- Principal speaks through webapp only; all context must persist in repository
- Oracle cannot execute; can only issue directives
- Directives must be comprehensive; Claudes lack Oracle thread visibility
- Repository is Foyer; all context must be accessible to any agent

---

## YOUR MISSION

You are the documentation and extraction engine for context engineering remediation. Your parallel (Claude 3) handles structural changes while you establish the decision archive and extract unrealized value from legacy files.

---

## PHASE A: DEPLOY DOCUMENTATION INFRASTRUCTURE

### Task A1: Install Core Documentation Files

The following files have been created by Oracle7. Install them in `orchestration/state/`:

**File 1: ORACLE_DECISIONS.md** (~8K)
- Complete decision log from Oracle 0-7
- Each decision includes Principal's words, Oracle's interpretation, alternatives, rationale
- Living document—update with each future thread

**File 2: THREAD_CONTEXT.md** (~4K)
- Summary of what each Oracle thread established
- Pattern identification (Oracle3 as "the model")
- Quick reference for thread-specific contributions

**File 3: STANDARDS.md** (~6K)
- Complete 18 evaluative lenses
- Application methodology
- Worked example

**Commands**:
```bash
# Ensure state directory exists
mkdir -p orchestration/state/

# Copy files (you'll receive content from Principal)
# Save each to orchestration/state/[FILENAME].md

# Verify
ls -la orchestration/state/
```

---

## PHASE B: SYSTEM PROMPT EXPORT EXTRACTION

### Background
The repository contains 16 "Technological_Lunar_-_System_Prompts*" files. These are raw exports from each platform (ChatGPT, Claude, Gemini, Grok) for both Apple and Google accounts.

**Oracle7 Analysis**: These are process artifacts, not canonical content. Value is what they TEACH, not what they ARE. However, extraction must be verified before deletion.

### Task B1: Audit Unextracted Value

Compare raw exports against unified prompts to identify unextracted intelligence:

```bash
# List all raw exports
ls -la | grep "Technological_Lunar_"

# List unified prompts for comparison
ls -la | grep -E "^(ChatGPT|Claude|Gemini|Grok).*unified"
```

For each platform, examine:
1. **ChatGPT memories** (7K) — Does unified prompt capture accumulated context?
2. **Account variations** (Apple vs Google) — Any account-specific intelligence?
3. **Historical configurations** — Evidence of Archetype Engineering era for GENESIS-003?

### Task B2: Extract to Appropriate Destinations

**Extract TO**:
| Content Type | Destination |
|--------------|-------------|
| Historical evidence of Archetype Engineering | Append to GENESIS-003-EVOLUTION.md |
| Platform-specific quirks not in unified | Append to CANON-31142-PLATFORM_GRAMMAR |
| Learnings about what worked/didn't | Create orchestration/state/DESIGN_DECISIONS.md |

**Template for DESIGN_DECISIONS.md**:
```markdown
# DESIGN DECISIONS LOG
## System Prompt Architecture
**Last Updated**: [DATE]

---

## Decision: Archetype Engineering → Reception Calibration

**What Was Tried**: Detailed persona specifications per lab
- Claude: "intellectual collaborator and reasoning partner" (~2,300 chars)
- [Continue for each lab]

**Observed Issues**:
- Over-engineered: Too many behavioral specifications
- Formulaic outputs: Models followed structure too rigidly
- [Continue]

**Learning**: Models respond better to understanding the USER than becoming a PERSONA.

**Superseded By**: Reception Calibration (three-layer architecture)

---

## Decision: [Next decision]
...
```

### Task B3: Verify Extraction Complete

Create verification checklist:

```markdown
# SYSTEM_PROMPT_EXTRACTION_VERIFICATION.md

## Extraction Status

| Platform | Account | Raw Export | Unified Prompt | Value Extracted? | Notes |
|----------|---------|------------|----------------|------------------|-------|
| ChatGPT | Apple | ✓ | ✓ | ☐ | [Verify memories captured] |
| ChatGPT | Google | ✓ | ✓ | ☐ | [Verify memories captured] |
| Claude | Apple | ✓ | ✓ | ☐ | |
| Claude | Google | ✓ | ✓ | ☐ | |
| Gemini | N/A | ✓ (4 slots) | ✓ | ☐ | |
| Grok | Apple | ✓ | ✓ | ☐ | |
| Grok | Google | ✓ | ✓ | ☐ | |

## Unextracted Value Identified
- [ ] [List any value not in unified prompts]

## Extraction Complete
Date: [DATE]
Verified by: Claude 2
```

### Task B4: Mark for Deletion (DO NOT DELETE YET)

After extraction verified, mark files for deletion:

```bash
# Create manifest of files to delete
cat > orchestration/state/DELETION_MANIFEST.md << 'EOF'
# Files Pending Deletion
## System Prompt Exports
**Status**: Extraction complete, awaiting Principal approval for deletion

### Files
1. Technological_Lunar_-_System_PromptsChatGPT__OpenAI_Apple__Memories.txt
2. Technological_Lunar_-_System_PromptsChatGPT__OpenAI_Apple__System_Prompt_1...
[List all 16 files]

### Verification
- Extraction verification: orchestration/state/SYSTEM_PROMPT_EXTRACTION_VERIFICATION.md
- Extraction date: [DATE]
- Extracted by: Claude 2

### Approval Required
Principal must approve deletion before execution.
EOF
```

---

## PHASE C: TECH LUNAR CANONIZATION PREP

### Background
Oracle7 determined via 18-lens analysis:
| File | Disposition | Rationale |
|------|-------------|-----------|
| Research_Protocols.md | CANONIZE | Methodology is antifragile |
| Implementation_Guide.md | CANONIZE | Patterns are antifragile |
| FrontierModels.md | DELETE | Temporal, obsolete |
| Screenplay_Formatting_* | QUEUE (Modal 2) | Future modality |

### Task C1: Research Protocols Analysis

Examine `Technology_Lunar_-_3_Research_Protocols.md`:

1. **Identify canonical target**: Should become asteroid under CANON-30300 (Tech Stack)
2. **Proposed ID**: CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE.md
3. **Content audit**: What's essential vs. what's example/illustration?
4. **Size estimate**: Target ~20K (compress from 31K)

**Produce**: `CANONIZATION_PREP_Research_Protocols.md` with:
- Proposed CANON ID and placement
- Content outline (what sections to preserve)
- Content to compress/remove
- YAML frontmatter draft

### Task C2: Implementation Guide Analysis

Examine `Technology_Lunar_-_4_Implementation_Guide.md`:

1. **Identify canonical target**: Should become asteroid under CANON-30300 (Tech Stack)
2. **Proposed ID**: CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE.md
3. **Content audit**: What's essential vs. what's example/illustration?
4. **Size estimate**: Target ~25K (compress from 43K)

**Produce**: `CANONIZATION_PREP_Implementation_Guide.md`

### Task C3: Screenplay Formatting Queue Prep

Examine `Technology_Lunar_-_Screenplay_Formatting_*` files (~5 files):

1. **Consolidate**: Should these become single QUEUE item?
2. **Tag**: Mark as "Modal 2" content
3. **Expiration**: 2-cycle from Modal 2 activation

**Produce**: `QUEUE_PREP_Screenplay_Formatting.md`

### Task C4: FrontierModels Deletion Prep

`Technology_Lunar_-_FrontierModels.md` — MARKED FOR DELETION

Verify no unextracted value:
1. Is any content unique (not in MODEL_PROFILE-*.yaml)?
2. Is there historical value for GENESIS layer?
3. Is there methodology worth preserving?

If no unique value → Add to DELETION_MANIFEST.md

---

## PHASE D: EXECUTION LOG

### Required Output

Create `orchestration/execution_logs/EXECUTION_LOG-2025-12-31-025A.md`:

```markdown
# EXECUTION LOG: DIRECTIVE-025A
## Documentation & Extraction Stream
**Date**: 2025-12-31
**Agent**: Claude 2 (Desktop)
**Directive**: DIRECTIVE-025A

---

## Phase A: Documentation Infrastructure

### A1: Core Files Installed
- [ ] ORACLE_DECISIONS.md → orchestration/state/
- [ ] THREAD_CONTEXT.md → orchestration/state/
- [ ] STANDARDS.md → orchestration/state/

**Notes**: [Any issues]

---

## Phase B: System Prompt Extraction

### B1: Audit Findings
[Summary of what was found]

### B2: Extractions Made
| Content | Destination | Size |
|---------|-------------|------|
| [What] | [Where] | [How much] |

### B3: Verification
- Extraction verification file created: ☐
- All value extracted: ☐

### B4: Deletion Manifest
- Files marked for deletion: [N]
- Awaiting Principal approval: ☐

---

## Phase C: Tech Lunar Prep

### C1: Research_Protocols
- Canonization prep file: ☐
- Proposed ID: [ID]
- Target size: [X]K

### C2: Implementation_Guide
- Canonization prep file: ☐
- Proposed ID: [ID]
- Target size: [X]K

### C3: Screenplay_Formatting
- Queue prep file: ☐
- Consolidated to: [N files]

### C4: FrontierModels
- Unique value found: [Y/N]
- Added to deletion manifest: ☐

---

## Summary

| Task | Status | Notes |
|------|--------|-------|
| A1 | ☐ | |
| B1-B4 | ☐ | |
| C1-C4 | ☐ | |

**Blockers**: [Any issues requiring Principal decision]

**Ready for Principal Review**: ☐
```

---

## SUCCESS CRITERIA

Per 18 lenses:

1. **Syncrescendent Route**: Decision continuity restored
2. **Bitter Lesson**: Documentation scales to future threads
3. **Antifragile**: System gains from this remediation
4. **Agentify + Human-Navigable**: Any Claude can discover context
5. **Lean**: Eliminated rework from lost context
6. **Six Sigma**: Reduced defect rate (no more fictional execution claims)

---

## DELIVERABLES

1. `orchestration/state/ORACLE_DECISIONS.md` — Installed
2. `orchestration/state/THREAD_CONTEXT.md` — Installed
3. `orchestration/state/STANDARDS.md` — Installed
4. `orchestration/state/DESIGN_DECISIONS.md` — Created with learnings
5. `orchestration/state/SYSTEM_PROMPT_EXTRACTION_VERIFICATION.md` — Extraction verified
6. `orchestration/state/DELETION_MANIFEST.md` — Files pending deletion
7. `CANONIZATION_PREP_Research_Protocols.md` — Ready for Claude 3
8. `CANONIZATION_PREP_Implementation_Guide.md` — Ready for Claude 3
9. `QUEUE_PREP_Screenplay_Formatting.md` — Ready for Claude 3
10. `orchestration/execution_logs/EXECUTION_LOG-2025-12-31-025A.md` — Complete log

---

## COORDINATION WITH CLAUDE 3

Claude 3 (DIRECTIVE-025B) handles:
- Structural reorganization
- GENESIS canonization
- Actual file creation/deletion/moves
- Naming convention enforcement

You prepare; Claude 3 executes. Your prep files inform Claude 3's actions.

---

**Execute with thoroughness. Maximum resolution. The Foyer must be complete.**
