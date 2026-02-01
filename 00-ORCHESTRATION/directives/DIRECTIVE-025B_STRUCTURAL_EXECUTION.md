# DIRECTIVE-025B: STRUCTURAL EXECUTION STREAM
## Claude 3 (Code Desktop) Initialization
**Issued**: 2025-12-31
**Authority**: Oracle7 under Sovereign direction
**Classification**: CRITICAL — Repository Restructuring
**Parallel Stream**: Claude 2 handles documentation/extraction (DIRECTIVE-025A)

---

## DECISION CONTEXT

### Sovereign's Actual Words
> "Where's the flat level hierarchy? Where's the aliases?"

> "Aliases are supposed to be for Finder, not for Obsidian."

> "Why are they [GENESIS] in an orphaned folder?"

> "Apply 18 principles. Understand the ontology of the Syncrescendence."

> "Rigorously, meticulously, and comprehensively study every single Oracle thread... and fix it."

### Oracle's Interpretation
The repository structure violates established architectural decisions from Oracle 2-6. GENESIS exists as orphaned tier when it should be cosmos-level CANON. Flat hierarchy was decided but never implemented. Finder aliases were specified but never created. This directive executes the structural transformation.

### Alternatives Considered
1. **Incremental fixes** — Rejected: "This is not some simple nominal or tactical fix"
2. **Partial restructuring** — Rejected: Violates "most extreme dynamic progressive route"
3. **Complete structural overhaul** — CHOSEN

### Rationale (18-Lens Summary)
| Lens | Score | Notes |
|------|-------|-------|
| Syncrescendent Route | ✓ | Restores architectural coherence |
| Bitter Lesson | ✓ | Flat + metadata scales to 1000+ files |
| Antifragile | ✓ | Three-pillar infrastructure robust to change |
| Meet the Moment | ✓ | Fixes current dysfunction |
| Personal Idiosyncrasies | ✓ | 2-decision navigation, holistic visibility |
| Elegance + Dev Happiness | ✓ | Clean mental model |
| Agentify + Human-Navigable | ✓ | Both can traverse effectively |
| Systems Thinking | ✓ | Parts now relate to whole correctly |
| Industrial Engineering | ✓ | Eliminates rework from structural confusion |

**Score**: 17/18 — Approved

### Implicit Agreements
- Orchestration is protected infrastructure (never apply metabolism)
- Naming convention encodes hierarchy
- Metadata provides machine-readable relationships
- Finder aliases provide human-friendly views
- GENESIS IS cosmos tier (not separate)

---

## YOUR MISSION

You are the structural execution engine. Your parallel (Claude 2) prepares documentation and extraction while you implement the architectural transformation: GENESIS canonization, flat hierarchy, directory restructuring, naming enforcement, and Finder alias creation.

---

## PHASE A: GENESIS CANONIZATION

### Background
GENESIS-000 through GENESIS-003 exist as separate tier. Oracle7 determined via 18-lens analysis: GENESIS IS cosmos tier—foundational, not separate. Must be canonized as CANON-0000x.

### Task A1: Determine Numbering Strategy

**Option 1**: Insert GENESIS at [[CANON-00000-SCHEMA-cosmos]] through [[CANON-00003-PRINCIPLES-cosmos]], renumber existing cosmos
```
GENESIS-000-ORIGIN → CANON-00000-ORIGIN-cosmos
GENESIS-001-LINEAGE → CANON-00001-LINEAGE-cosmos
GENESIS-002-PRINCIPLES → CANON-00002-PRINCIPLES-cosmos
GENESIS-003-EVOLUTION → CANON-00003-EVOLUTION-cosmos
CANON-00000-SCHEMA → CANON-00004-SCHEMA-cosmos
CANON-00001-SYNCRESCENDENCE → CANON-00005-SYNCRESCENDENCE-cosmos
... (renumber all existing)
```

**Option 2**: Insert GENESIS at [[CANON-00001-ORIGIN-cosmos]] through [[CANON-00004-EVOLUTION-cosmos]], Schema stays [[CANON-00000-SCHEMA-cosmos]]
```
CANON-00000-SCHEMA-cosmos (unchanged - navigational must come first)
GENESIS-000-ORIGIN → CANON-00001-ORIGIN-cosmos
GENESIS-001-LINEAGE → CANON-00002-LINEAGE-cosmos
GENESIS-002-PRINCIPLES → CANON-00003-PRINCIPLES-cosmos
GENESIS-003-EVOLUTION → CANON-00004-EVOLUTION-cosmos
CANON-00001-SYNCRESCENDENCE → CANON-00005-SYNCRESCENDENCE-cosmos
... (renumber rest)
```

**Recommended**: Option 2 — Schema as navigational document should remain first entry point.

### Task A2: Execute GENESIS Canonization

```bash
# Create backup
cp -r GENESIS/ GENESIS_BACKUP_$(date +%Y%m%d)/

# Rename GENESIS files to CANON format
mv GENESIS-000-ORIGIN.md CANON-00001-ORIGIN-cosmos.md
mv GENESIS-001-LINEAGE.md CANON-00002-LINEAGE-cosmos.md
mv GENESIS-002-PRINCIPLES.md CANON-00003-PRINCIPLES-cosmos.md
mv GENESIS-003-EVOLUTION.md CANON-00004-EVOLUTION-cosmos.md

# Update frontmatter in each file
# - Change id: GENESIS-00x to id: CANON-0000x
# - Change tier: GENESIS to tier: CANON
# - Add type: cosmos

# Remove empty GENESIS directory
rmdir GENESIS/
```

### Task A3: Renumber Existing Cosmos Documents

| Current | New |
|---------|-----|
| CANON-00000-SCHEMA-cosmos.md | (unchanged) |
| CANON-00001-SYNCRESCENDENCE-cosmos.md | CANON-00005-SYNCRESCENDENCE-cosmos.md |
| CANON-00002-CORPUS-cosmos.md | CANON-00006-CORPUS-cosmos.md |
| CANON-00003-EVALUATION-cosmos.md | CANON-00007-EVALUATION-cosmos.md |
| CANON-00004-RESOLUTIONS-cosmos.md | CANON-00008-RESOLUTIONS-cosmos.md |
| CANON-00005-STRATEGY-cosmos.md | CANON-00009-STRATEGY-cosmos.md |
| CANON-00006-OPERATIONS-cosmos.md | CANON-00010-OPERATIONS-cosmos.md |
| CANON-00007-ARTIFACT_PROTOCOL-cosmos.md | CANON-00011-ARTIFACT_PROTOCOL-cosmos.md |
| CANON-00008-MODAL_SEQUENCE-cosmos.md | CANON-00012-MODAL_SEQUENCE-cosmos.md |
| CANON-00009-QUICKSTART-cosmos.md | CANON-00013-QUICKSTART-cosmos.md |
| CANON-00010-CONTENT_PROTOCOL-cosmos.md | CANON-00014-CONTENT_PROTOCOL-cosmos.md |

**Commands**:
```bash
# Rename each file
mv CANON-00001-SYNCRESCENDENCE-cosmos.md CANON-00005-SYNCRESCENDENCE-cosmos.md
# ... (continue for all)

# Update frontmatter id: in each renamed file
# Update any cross-references in all CANON files
```

### Task A4: Update Cross-References

Search all CANON files for references to old IDs and update:

```bash
# Find all references to old IDs
grep -r "CANON-0000[1-9]" CANON/
grep -r "CANON-0001[0-4]" CANON/

# Update references in each file
# Use sed or manual editing
```

---

## PHASE B: FLAT HIERARCHY IMPLEMENTATION

### Background
Oracle2-4 established flat + symlink architecture. Oracle6 specified "aliases for Finder, not Obsidian." Never implemented.

### Task B1: Flatten CANON Directory

All CANON files should be at single level:

**Current** (nested):
```
CANON/
├── cosmos/
│   ├── CANON-00000-SCHEMA-cosmos.md
│   └── ...
├── core/
│   ├── CANON-10000-CELESTIAL_BODY-core.md
│   └── ...
├── lattice/
│   └── ...
└── chains/
    └── ...
```

**Target** (flat):
```
CANON/
├── CANON-00000-SCHEMA-cosmos.md
├── CANON-00001-ORIGIN-cosmos.md
├── CANON-10000-CELESTIAL_BODY-core.md
├── CANON-20000-PALACE-lattice.md
├── CANON-30000-INTELLIGENCE-chain.md
└── ... (all ~65 files at same level)
```

**Commands**:
```bash
# Move all files to CANON root
find CANON/ -name "CANON-*.md" -exec mv {} CANON/ \;

# Remove empty subdirectories
rmdir CANON/cosmos/ CANON/core/ CANON/lattice/ CANON/chains/ 2>/dev/null

# Verify flat structure
ls CANON/ | wc -l
ls -la CANON/
```

### Task B2: Create Finder Aliases

Create alias directories that provide filtered views without duplicating files:

```bash
# Create aliases directory
mkdir -p aliases/

# Create symbolic links for logical views
# Note: These are directory-level filters, not file duplicates

# Cosmos view
mkdir -p aliases/cosmos/
ln -s ../../CANON/CANON-0*.md aliases/cosmos/

# Core view
mkdir -p aliases/core/
ln -s ../../CANON/CANON-1*.md aliases/core/

# Lattice view
mkdir -p aliases/lattice/
ln -s ../../CANON/CANON-2*.md aliases/lattice/

# Chains view (all 30000-35999)
mkdir -p aliases/chains/
ln -s ../../CANON/CANON-3*.md aliases/chains/

# Per-chain views
mkdir -p aliases/chains/intelligence/
ln -s ../../../CANON/CANON-30*.md aliases/chains/intelligence/

mkdir -p aliases/chains/information/
ln -s ../../../CANON/CANON-31*.md aliases/chains/information/

mkdir -p aliases/chains/insight/
ln -s ../../../CANON/CANON-32*.md aliases/chains/insight/

mkdir -p aliases/chains/expertise/
ln -s ../../../CANON/CANON-33*.md aliases/chains/expertise/

mkdir -p aliases/chains/knowledge/
ln -s ../../../CANON/CANON-34*.md aliases/chains/knowledge/

mkdir -p aliases/chains/wisdom/
ln -s ../../../CANON/CANON-35*.md aliases/chains/wisdom/
```

### Task B3: Restructure OPERATIONAL

**Target structure**:
```
OPERATIONAL/
├── functions/
│   ├── distill/      # Functions that compress
│   ├── transform/    # Functions that convert
│   └── expand/       # Functions that elaborate
├── prompts/
│   ├── unified/      # Platform prompts (ChatGPT/Claude/Gemini/Grok)
│   └── profiles/     # MODEL_PROFILE YAMLs
└── processing/       # Active work
```

**Commands**:
```bash
# Create structure
mkdir -p OPERATIONAL/functions/{distill,transform,expand}
mkdir -p OPERATIONAL/prompts/{unified,profiles}
mkdir -p OPERATIONAL/processing/

# Move function XMLs
# Distill functions (compress)
mv consolidate.xml coalesce.xml compile.xml OPERATIONAL/functions/distill/

# Transform functions (convert)
mv convert.xml translate.xml reforge.xml anneal.xml OPERATIONAL/functions/transform/

# Expand functions (elaborate)
mv amplify.xml absorb.xml OPERATIONAL/functions/expand/

# Move remaining XMLs based on function
# (Classify each: harmonize, integrate, listenize, readize, optimize, offload, primer, transcribe_*)

# Move unified prompts
mv *-unified-prompt.md OPERATIONAL/prompts/unified/
mv *-gemknowledge-base.md OPERATIONAL/prompts/unified/

# Move MODEL_PROFILE YAMLs
mv MODEL_PROFILE-*.yaml OPERATIONAL/prompts/profiles/
```

### Task B4: Consolidate Orchestration

**Current** (chaotic):
```
orchestration/
├── execution_logs/     # Original
├── execution-logs/     # Duplicate!
└── ... (other mess)
```

**Target**:
```
orchestration/
├── directives/         # Archive of issued directives
├── execution_logs/     # Single log directory
├── scaffolding/        # Working documents (ALPHA_*, BETA_*)
└── state/
    ├── BACKLOG.md
    ├── CURRENT_STATE.md
    ├── ORACLE_DECISIONS.md    # NEW from Claude 2
    ├── THREAD_CONTEXT.md      # NEW from Claude 2
    ├── STANDARDS.md           # NEW from Claude 2
    └── DESIGN_DECISIONS.md    # NEW from Claude 2
```

**Commands**:
```bash
# Consolidate log directories
mv execution-logs/* execution_logs/ 2>/dev/null
rmdir execution-logs/ 2>/dev/null

# Move scattered execution logs to proper location
mv EXECUTION_LOG-*.md orchestration/execution_logs/

# Move directives
mv DIRECTIVE-*.md orchestration/directives/

# Move scaffolding (ALPHA/BETA working docs)
mv ALPHA_*.md orchestration/scaffolding/
mv BETA_*.md orchestration/scaffolding/
```

---

## PHASE C: NAMING ENFORCEMENT

### Task C1: Fix Legacy "Technology_Lunar_" Naming

```bash
# List all legacy files
ls | grep "Technology_Lunar_"

# Process based on Oracle7 decisions:
# - Research_Protocols → CANONIZE (wait for Claude 2 prep)
# - Implementation_Guide → CANONIZE (wait for Claude 2 prep)
# - FrontierModels → DELETE (after verification)
# - Screenplay_Formatting → QUEUE (Modal 2)

# For now, move to staging
mkdir -p orchestration/scaffolding/tech_lunar_staging/
mv Technology_Lunar_-_*.md orchestration/scaffolding/tech_lunar_staging/
```

### Task C2: Fix Typo Files

```bash
# Fix "Al" → "AI" typos
mv Al_Academic_Research.md AI_Academic_Research.md
mv Al_Image_Generators.md AI_Image_Generators.md

# Fix triple underscore
mv AI_3D___VFX.md AI_3D_VFX.md

# Fix other encoding issues
mv "The_Next_Wave_in_Al_Video_and_VFX.md" "The_Next_Wave_in_AI_Video_and_VFX.md"
```

### Task C3: Process "Technological_Lunar_" System Prompts

**Wait for Claude 2's extraction verification before deletion.**

```bash
# For now, move to staging
mkdir -p orchestration/scaffolding/legacy_prompts/
mv Technological_Lunar_-_*.txt orchestration/scaffolding/legacy_prompts/
```

---

## PHASE D: QUEUE ORGANIZATION

### Task D1: Create Queue Structure

```
QUEUE/
├── modal1/           # Current modal content
├── modal2/           # Future modal (visual)
│   └── screenplay_formatting/
└── pending/          # Unclassified
```

```bash
mkdir -p QUEUE/{modal1,modal2/screenplay_formatting,pending}

# Move screenplay content (after Claude 2 prep)
# mv orchestration/scaffolding/tech_lunar_staging/Technology_Lunar_-_Screenplay* QUEUE/modal2/screenplay_formatting/
```

---

## PHASE E: VERIFICATION

### Task E1: Structure Verification

```bash
# Verify CANON is flat
echo "CANON files at root level:"
ls CANON/*.md | wc -l

# Verify no nested directories in CANON
find CANON/ -type d | wc -l  # Should be 1 (just CANON/)

# Verify aliases work
echo "Testing aliases:"
ls aliases/cosmos/
ls aliases/chains/intelligence/

# Verify orchestration structure
echo "Orchestration structure:"
tree orchestration/
```

### Task E2: Cross-Reference Integrity

```bash
# Check for broken references
grep -r "CANON-" CANON/ | grep -v ".md:" | head -20

# Check for references to old GENESIS tier
grep -r "GENESIS-" CANON/
grep -r "tier: GENESIS" CANON/
```

### Task E3: Naming Consistency

```bash
# Check for legacy naming patterns
ls | grep -E "(Technology|Technological)_Lunar"
ls | grep "^Al_"
ls | grep "___"

# Should all return empty
```

---

## PHASE F: EXECUTION LOG

### Required Output

Create `orchestration/execution_logs/EXECUTION_LOG-2025-12-31-025B.md`:

```markdown
# EXECUTION LOG: DIRECTIVE-025B
## Structural Execution Stream
**Date**: 2025-12-31
**Agent**: Claude 3 (Code Desktop)
**Directive**: DIRECTIVE-025B

---

## Phase A: GENESIS Canonization

### A1: Numbering Strategy
- Strategy chosen: [Option 1/2]
- Rationale: [Why]

### A2: GENESIS Files Renamed
| Original | New | Status |
|----------|-----|--------|
| GENESIS-000-ORIGIN | CANON-00001-ORIGIN-cosmos | ☐ |
| GENESIS-001-LINEAGE | CANON-00002-LINEAGE-cosmos | ☐ |
| GENESIS-002-PRINCIPLES | CANON-00003-PRINCIPLES-cosmos | ☐ |
| GENESIS-003-EVOLUTION | CANON-00004-EVOLUTION-cosmos | ☐ |

### A3: Cosmos Documents Renumbered
| Original | New | Status |
|----------|-----|--------|
| CANON-00001-SYNCRESCENDENCE | CANON-00005-SYNCRESCENDENCE | ☐ |
| ... | ... | ... |

### A4: Cross-References Updated
- Files checked: [N]
- References updated: [N]
- Issues found: [List]

---

## Phase B: Flat Hierarchy

### B1: CANON Flattened
- Files moved to root: [N]
- Subdirectories removed: [List]

### B2: Finder Aliases Created
- aliases/cosmos/: ☐
- aliases/core/: ☐
- aliases/lattice/: ☐
- aliases/chains/: ☐
- aliases/chains/[chain]/: ☐ (x6)

### B3: OPERATIONAL Restructured
- functions/distill/: [N files]
- functions/transform/: [N files]
- functions/expand/: [N files]
- prompts/unified/: [N files]
- prompts/profiles/: [N files]

### B4: Orchestration Consolidated
- execution_logs/ consolidated: ☐
- directives/ populated: ☐
- scaffolding/ populated: ☐
- state/ ready for Claude 2 docs: ☐

---

## Phase C: Naming Enforcement

### C1: Tech Lunar Files Staged
- Files moved to staging: [N]

### C2: Typos Fixed
| Original | Fixed | Status |
|----------|-------|--------|
| Al_Academic_Research | AI_Academic_Research | ☐ |
| Al_Image_Generators | AI_Image_Generators | ☐ |
| AI_3D___VFX | AI_3D_VFX | ☐ |

### C3: Legacy Prompts Staged
- Files moved to staging: [N]

---

## Phase D: Queue Organization

### D1: Queue Structure Created
- QUEUE/modal1/: ☐
- QUEUE/modal2/: ☐
- QUEUE/pending/: ☐

---

## Phase E: Verification

### E1: Structure Verification
- CANON flat: [Y/N] ([N] files)
- Aliases functional: [Y/N]
- Orchestration correct: [Y/N]

### E2: Cross-Reference Integrity
- Broken references found: [N]
- GENESIS references remaining: [N]

### E3: Naming Consistency
- Legacy patterns remaining: [N]
- Typos remaining: [N]

---

## Summary

| Phase | Status | Notes |
|-------|--------|-------|
| A: GENESIS | ☐ | |
| B: Flat Hierarchy | ☐ | |
| C: Naming | ☐ | |
| D: Queue | ☐ | |
| E: Verification | ☐ | |

**Blockers**: [Any issues]

**Coordination with Claude 2**: 
- Awaiting: [What from Claude 2]
- Completed for Claude 2: [What Claude 2 needs]

**Ready for Sovereign Review**: ☐
```

---

## SUCCESS CRITERIA

Per 18 lenses:

1. **Syncrescendent Route**: GENESIS integrated, architecture coherent
2. **Bitter Lesson**: Flat + metadata scales
3. **Antifragile**: Three-pillar infrastructure robust
4. **Agentify + Human-Navigable**: 2-decision navigation, aliases work
5. **Elegance + Dev Happiness**: Clean, satisfying structure
6. **Industrial Engineering**: No redundant directories

---

## DELIVERABLES

1. CANON/ flattened (all files at root level)
2. GENESIS canonized as CANON-0000x
3. Cosmos documents renumbered
4. aliases/ directory with symbolic links
5. OPERATIONAL/ restructured
6. orchestration/ consolidated
7. Typos fixed
8. Legacy files staged (awaiting Claude 2 prep)
9. QUEUE/ structure created
10. `orchestration/execution_logs/EXECUTION_LOG-2025-12-31-025B.md`

---

## COORDINATION WITH CLAUDE 2

Claude 2 (DIRECTIVE-025A) provides:
- `ORACLE_DECISIONS.md` → Install in orchestration/state/
- `THREAD_CONTEXT.md` → Install in orchestration/state/
- `STANDARDS.md` → Install in orchestration/state/
- `DESIGN_DECISIONS.md` → Install in orchestration/state/
- `CANONIZATION_PREP_Research_Protocols.md` → Informs your canonization
- `CANONIZATION_PREP_Implementation_Guide.md` → Informs your canonization
- `QUEUE_PREP_Screenplay_Formatting.md` → Informs your queue placement
- `SYSTEM_PROMPT_EXTRACTION_VERIFICATION.md` → Enables deletion
- `DELETION_MANIFEST.md` → Lists files to delete

**Do not delete legacy files until Claude 2 confirms extraction complete.**

---

**Execute with precision. The architecture must finally match the decisions.**
