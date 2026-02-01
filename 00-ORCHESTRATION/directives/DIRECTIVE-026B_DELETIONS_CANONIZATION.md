# DIRECTIVE-026B: DELETIONS + CANONIZATION EXECUTION
## Claude 3 (Code Desktop) Initialization
**Issued**: 2025-12-31
**Authority**: Oracle7 under Sovereign direction
**Classification**: CRITICAL — Repository Finalization
**Parallel Stream**: Claude 2 handles scripture verification (DIRECTIVE-026A)

---

## DECISION CONTEXT

### Sovereign's Actual Words
> "Yes proceed."
(Approving deletion manifest, canonization, queue consolidation, and scripture verification)

From Oracle7 18-lens analysis:
> "Research_Protocols → CANONIZE (CANON-303xx). Implementation_Guide → CANONIZE (CANON-303xx). FrontierModels → DELETE (temporal, obsolete). Screenplay → QUEUE (Modal 2)."

> "EXTRACT any unextracted value → DELETE. Process artifacts, not canonical content."

### Oracle's Interpretation
Claude 2 (DIRECTIVE-025A) completed:
- Extraction verification for system prompt exports
- Canonization prep for Research_Protocols and Implementation_Guide
- Queue prep for Screenplay files
- Deletion manifest preparation

Claude 3 (DIRECTIVE-025B) completed:
- Staged legacy files to scaffolding/
- Did NOT delete (awaiting approval)

Sovereign has now approved. This directive executes the approved deletions and canonizations.

### Alternatives Considered
1. **Keep legacy files as archive** — Rejected: Violates metabolism model ("canonize or delete")
2. **Partial canonization** — Rejected: All-or-nothing per 18-lens analysis
3. **Full execution per manifest** — CHOSEN

### Rationale (18-Lens Summary)
| Lens | Score | Notes |
|------|-------|-------|
| Syncrescendent Route | ✓ | Removes discontinuities |
| Bitter Lesson | ✓ | Temporal content doesn't scale |
| Antifragile | ✓ | Cleaner repository more robust |
| Meet the Moment | ✓ | Current methodology canonized |
| Lean | ✓ | Eliminates waste |
| Six Sigma | ✓ | Reduces defect sources |

**Score**: 18/18 — Approved

### Implicit Agreements
- Extraction verified complete (SYSTEM_PROMPT_EXTRACTION_VERIFICATION.md)
- Value captured in DESIGN_DECISIONS.md
- Canonization prep files specify target structure
- Deletions are from orchestration/scaffolding/ (staged location)

---

## YOUR MISSION

Execute the approved deletions and canonizations. Transform staged content into canonical form. Remove legacy artifacts.

---

## PHASE A: EXECUTE APPROVED DELETIONS

### A1: Delete Legacy System Prompt Exports

**Location**: `orchestration/scaffolding/legacy_prompts/`

**Files to Delete** (14 total):
```
Technological Lunar - System PromptsChatGPT [OpenAI@Apple] Memories.txt
Technological Lunar - System PromptsChatGPT [OpenAI@Apple] System Prompt 1 - What traits should ChatGPT have?.txt
Technological Lunar - System PromptsChatGPT [OpenAI@Apple] System Prompt 2 - Anything else ChatGPT should know about you?.txt
Technological Lunar - System PromptsChatGPT [OpenAI@Google] Memories.txt
Technological Lunar - System PromptsChatGPT [OpenAI@Google] System Prompt 1 - What traits should ChatGPT have?.txt
Technological Lunar - System PromptsChatGPT [OpenAI@Google] System Prompt 2 - Anything else ChatGPT should know about you?.txt
Technological Lunar - System PromptsClaude [Anthropic@Apple] System Prompt - What personal preferences should Claude consider in responses?.txt
Technological Lunar - System PromptsClaude [Anthropic@Google] System Prompt - What personal preferences should Claude consider in responses?.txt
Technological Lunar - System PromptsGemini Saved Info - What do you want Gemini to remember? 1.txt
Technological Lunar - System PromptsGemini Saved Info - What do you want Gemini to remember? 2.txt
Technological Lunar - System PromptsGemini Saved Info - What do you want Gemini to remember? 3.txt
Technological Lunar - System PromptsGemini Saved Info - What do you want Gemini to remember? 4.txt
Technological Lunar - System PromptsGrok [xAI@Apple] System Prompt - Custom Instructions.txt
Technological Lunar - System PromptsGrok [xAI@Google] System Prompt - Custom Instructions.txt
```

**Rationale**: Extraction complete per SYSTEM_PROMPT_EXTRACTION_VERIFICATION.md. Value captured in DESIGN_DECISIONS.md.

**Commands**:
```bash
# Delete legacy prompt exports
rm -rf orchestration/scaffolding/legacy_prompts/

# Verify deletion
ls orchestration/scaffolding/ | grep -i legacy
# Should return nothing
```

### A2: Delete Temporal Content

**Location**: `orchestration/scaffolding/tech_lunar_staging/`

**File to Delete**:
```
Technology Lunar - FrontierModels.md
```

**Rationale**: October 2025 AI model landscape analysis. Fails 15/18 lenses. Temporal content with no enduring methodology. MODEL_PROFILE-*.yaml files serve this function better (structured, updatable).

**Commands**:
```bash
# Delete FrontierModels
rm "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - FrontierModels.md"

# Verify
ls "orchestration/scaffolding/tech_lunar_staging/" | grep -i frontier
# Should return nothing
```

---

## PHASE B: EXECUTE CANONIZATION

### B1: Create [[CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE]] (Research Protocols)

**Source**: `orchestration/scaffolding/tech_lunar_staging/Technology Lunar - 3 Research_Protocols.md`

**Target**: `CANON/CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE.md`

**Prep File**: `orchestration/state/CANONIZATION_PREP_Research_Protocols.md`

**Compression Target**: 31K → ~20K (35% reduction)

**Key Sections to Preserve** (from prep file):
1. Source Triad Method (Pass 1/2/3)
2. Decision-Bearing Questions First
3. Verdicting Process (5 components)
4. Anti-patterns to avoid
5. Infrastructure evaluation patterns
6. Tool evaluation patterns

**Sections to Remove/Compress**:
- Redundant examples
- Overly detailed illustrations
- Content duplicated elsewhere in CANON

**Frontmatter**:
```yaml
---
id: [[CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE]]
name: Research Protocols
identity: RESEARCH_PROTOCOLS
tier: CANON
type: asteroid
parent: [[CANON-30300-TECH_STACK-comet-INTELLIGENCE]]
chain: INTELLIGENCE
comet: TECH_STACK
version: 2.0.0
status: canonical
created: 2025-12-31
updated: 2025-12-31
change_velocity: quarterly
dependencies:
  - [[CANON-30300-TECH_STACK-comet-INTELLIGENCE]]
  - [[CANON-30000-INTELLIGENCE-chain]]
synopsis: >
  Methodologies and quality standards for AI-augmented research,
  including the Source Triad Method, verdicting process, and
  decision-bearing question prioritization.
---
```

**Commands**:
```bash
# Read source file
cat "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - 3 Research_Protocols.md"

# Create canonical version with frontmatter and compressed content
# [Create file with proper frontmatter + compressed content]

# Verify creation
ls CANON/ | grep 30330

# Delete source after successful creation
rm "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - 3 Research_Protocols.md"
```

### B2: Create [[CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE]] (Implementation Patterns)

**Source**: `orchestration/scaffolding/tech_lunar_staging/Technology Lunar - 4 Implementation_Guide.md`

**Target**: `CANON/CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE.md`

**Prep File**: `orchestration/state/CANONIZATION_PREP_Implementation_Guide.md`

**Compression Target**: 43K → ~25K (42% reduction)

**Key Sections to Preserve** (from prep file):
1. Architectural Wisdom (over-engineering lessons)
2. Memory System Bootstrapping (5 phases)
3. Orchestration Patterns (decision tree + 5 patterns)
4. Context Engineering Economics
5. Security and Governance
6. Bootstrap Roadmap (12-month timeline)

**Sections to Remove/Compress**:
- Code examples that duplicate documentation elsewhere
- Overly detailed implementation specifics
- Content superseded by evolved understanding

**Frontmatter**:
```yaml
---
id: [[CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE]]
name: Implementation Patterns
identity: IMPLEMENTATION_PATTERNS
tier: CANON
type: asteroid
parent: [[CANON-30300-TECH_STACK-comet-INTELLIGENCE]]
chain: INTELLIGENCE
comet: TECH_STACK
version: 2.0.0
status: canonical
created: 2025-12-31
updated: 2025-12-31
change_velocity: quarterly
dependencies:
  - [[CANON-30300-TECH_STACK-comet-INTELLIGENCE]]
  - [[CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE]]
  - [[CANON-30000-INTELLIGENCE-chain]]
synopsis: >
  Practical patterns for AI system implementation, including
  memory bootstrapping phases, orchestration patterns, context
  engineering economics, and anti-over-engineering wisdom.
---
```

**Commands**:
```bash
# Read source file
cat "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - 4 Implementation_Guide.md"

# Create canonical version with frontmatter and compressed content
# [Create file with proper frontmatter + compressed content]

# Verify creation
ls CANON/ | grep 30340

# Delete source after successful creation
rm "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - 4 Implementation_Guide.md"
```

---

## PHASE C: EXECUTE QUEUE CONSOLIDATION

### C1: Create QUEUE-36200 (Screenplay Orchestration)

**Source Files** (5 total in `orchestration/scaffolding/tech_lunar_staging/`):
```
Technology Lunar - Agentic ScreenplayFormatting.md (36K)
Technology Lunar - Screenplay Formatting - agentic_screenplay_format.md (11K)
Technology Lunar - Screenplay Formatting - culmination.md (7K)
Technology Lunar - Screenplay Formatting - screenplay_manual.md (18K)
Technology Lunar - Screenplay Formatting - validation.md (4.5K)
```

**Total Source Size**: ~76K

**Target**: `QUEUE/modal2/screenplay_formatting/QUEUE-36200-SCREENPLAY_ORCHESTRATION-Modal2.md`

**Prep File**: `orchestration/state/QUEUE_PREP_Screenplay_Formatting.md`

**Consolidation Target**: 76K → ~30K (60% reduction)

**Content Structure**:
```markdown
# QUEUE-36200: Screenplay Orchestration for Modal 2
## AI-Assisted Visual Production Workflows

---

## Metadata
- **Queue ID**: QUEUE-36200
- **Modal**: 2 (Visual Simulation)
- **Status**: Pending Modal 2 activation
- **Expiration**: 2 cycles from Modal 2 activation
- **Source Files**: 5 (consolidated)
- **Original Size**: ~76K
- **Consolidated Size**: ~30K

---

## I. Core Screenplay Format
[Consolidated from screenplay_manual.md]

## II. Agentic Workflows
[Consolidated from Agentic ScreenplayFormatting.md + agentic_screenplay_format.md]

## III. Validation Protocols
[Consolidated from validation.md]

## IV. Implementation Notes
[Consolidated from culmination.md]

---

## Activation Criteria
This content becomes actionable when:
1. Modal 2 capabilities mature (visual simulation)
2. Video generation tools reach production quality
3. Sovereign initiates visual production workflow

---
```

**Commands**:
```bash
# Read all source files
cat "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - Agentic ScreenplayFormatting.md"
cat "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - Screenplay Formatting - agentic_screenplay_format.md"
cat "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - Screenplay Formatting - culmination.md"
cat "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - Screenplay Formatting - screenplay_manual.md"
cat "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - Screenplay Formatting - validation.md"

# Create consolidated queue item
# [Create file with consolidated content]

# Verify creation
ls QUEUE/modal2/screenplay_formatting/

# Delete source files after successful consolidation
rm "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - Agentic ScreenplayFormatting.md"
rm "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - Screenplay Formatting - agentic_screenplay_format.md"
rm "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - Screenplay Formatting - culmination.md"
rm "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - Screenplay Formatting - screenplay_manual.md"
rm "orchestration/scaffolding/tech_lunar_staging/Technology Lunar - Screenplay Formatting - validation.md"
```

---

## PHASE D: UPDATE ALIASES

### D1: Add New Canonical Files to Aliases

After creating [[CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE]] and [[CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE]]:

```bash
# Add to chains alias
ln -s ../../CANON/CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE.md aliases/chains/
ln -s ../../CANON/CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE.md aliases/chains/

# Add to intelligence chain alias
ln -s ../../../CANON/CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE.md aliases/chains/intelligence/
ln -s ../../../CANON/CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE.md aliases/chains/intelligence/
```

---

## PHASE E: CLEANUP STAGING

### E1: Remove Empty Staging Directory

After all files processed:

```bash
# Verify staging is empty
ls orchestration/scaffolding/tech_lunar_staging/
# Should be empty or contain only unprocessed files

# If empty, remove directory
rmdir orchestration/scaffolding/tech_lunar_staging/
```

---

## PHASE F: VERIFICATION

### F1: Deletion Verification

```bash
# Verify legacy_prompts deleted
ls orchestration/scaffolding/ | grep legacy
# Should return nothing

# Verify FrontierModels deleted
find . -name "*FrontierModels*" 2>/dev/null
# Should return nothing
```

### F2: Canonization Verification

```bash
# Verify new CANON files exist
ls CANON/CANON-3033*.md
ls CANON/CANON-3034*.md

# Verify frontmatter correct
head -20 CANON/CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE.md
head -20 CANON/CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE.md

# Verify file sizes (should be compressed)
ls -la CANON/CANON-3033*.md
ls -la CANON/CANON-3034*.md
```

### F3: Queue Verification

```bash
# Verify queue item exists
ls QUEUE/modal2/screenplay_formatting/

# Verify content consolidated
head -50 QUEUE/modal2/screenplay_formatting/QUEUE-36200-SCREENPLAY_ORCHESTRATION-Modal2.md
```

### F4: Alias Verification

```bash
# Verify new aliases work
ls -la aliases/chains/intelligence/ | grep 3033
ls -la aliases/chains/intelligence/ | grep 3034
```

---

## PHASE G: EXECUTION LOG

### Required Output

Create `orchestration/execution_logs/EXECUTION_LOG-2025-12-31-026B.md`:

```markdown
# EXECUTION LOG: DIRECTIVE-026B
## Deletions + Canonization Execution
**Date**: 2025-12-31
**Agent**: Claude 3 (Code Desktop)
**Directive**: DIRECTIVE-026B

---

## Phase A: Deletions

### A1: Legacy System Prompt Exports
- Files deleted: 14
- Location: orchestration/scaffolding/legacy_prompts/
- Status: ✓ COMPLETE

### A2: Temporal Content
- Files deleted: 1 (FrontierModels.md)
- Status: ✓ COMPLETE

**Total Deletions**: 15 files

---

## Phase B: Canonization

### B1: [[CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE]] (Research Protocols)
- Source: Technology Lunar - 3 Research_Protocols.md
- Target: CANON/CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE.md
- Original size: 31K
- Final size: [X]K
- Compression: [Y]%
- Status: ✓ COMPLETE

### B2: [[CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE]] (Implementation Patterns)
- Source: Technology Lunar - 4 Implementation_Guide.md
- Target: CANON/CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE.md
- Original size: 43K
- Final size: [X]K
- Compression: [Y]%
- Status: ✓ COMPLETE

---

## Phase C: Queue Consolidation

### C1: QUEUE-36200 (Screenplay Orchestration)
- Source files: 5
- Original total size: 76K
- Consolidated size: [X]K
- Compression: [Y]%
- Status: ✓ COMPLETE

---

## Phase D: Aliases

- [[CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE]] added to aliases/chains/ and aliases/chains/intelligence/
- [[CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE]] added to aliases/chains/ and aliases/chains/intelligence/
- Status: ✓ COMPLETE

---

## Phase E: Cleanup

- tech_lunar_staging/ directory: [removed/retained]
- Status: ✓ COMPLETE

---

## Phase F: Verification

| Check | Status |
|-------|--------|
| Legacy prompts deleted | ✓ |
| FrontierModels deleted | ✓ |
| [[CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE]] created | ✓ |
| [[CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE]] created | ✓ |
| QUEUE-36200 created | ✓ |
| Aliases updated | ✓ |
| Staging cleaned | ✓ |

---

## Summary

| Action | Count | Status |
|--------|-------|--------|
| Files deleted | 15 | ✓ |
| Files canonized | 2 | ✓ |
| Files consolidated | 5 → 1 | ✓ |
| Aliases added | 4 | ✓ |

**Net file change**: -19 files (15 deleted + 5 consolidated - 1 queue item)

---

## Repository Statistics (Post-Execution)

- CANON files: 71 (was 69, +2 canonized)
- QUEUE files: [count]
- Orchestration files: [count]
- Total files: [count]

---

## Blockers

None

---

## Ready for Sovereign Review: ✓
```

---

## SUCCESS CRITERIA

Per 18 lenses:

1. **Syncrescendent Route**: Legacy removed, methodology canonized
2. **Bitter Lesson**: Temporal content eliminated, patterns preserved
3. **Antifragile**: Cleaner, more robust repository
4. **Meet the Moment**: Current methodology accessible
5. **Lean**: 19 files eliminated/consolidated
6. **Six Sigma**: Fewer error sources

---

## DELIVERABLES

1. **15 files deleted** (14 legacy prompts + 1 FrontierModels)
2. **CANON-30330-RESEARCH_PROTOCOLS** created (~20K)
3. **CANON-30340-IMPLEMENTATION_PATTERNS** created (~25K)
4. **QUEUE-36200-SCREENPLAY_ORCHESTRATION** created (~30K)
5. **Aliases updated** for new CANON files
6. **Staging cleaned**
7. `orchestration/execution_logs/EXECUTION_LOG-2025-12-31-026B.md`

---

## COORDINATION WITH CLAUDE 2

Claude 2 (DIRECTIVE-026A) performs scripture verification in parallel.

After you complete this directive, [[CANON-00006-CORPUS-cosmos]] (Corpus) will need updates to reflect:
- [[CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE]] and [[CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE]] added
- QUEUE-36200 created
- 15 files deleted

Inform Claude 2 via execution log.

---

**Execute with precision. Canonize the worthy. Delete the obsolete.**
