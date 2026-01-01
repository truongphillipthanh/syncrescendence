# DIRECTIVE-024: Ruthless Forge
## Phase 4 — Naming Architecture & Duplicate Elimination

**Issued**: 2025-12-31
**Issued By**: Oracle6
**To**: Claude Code Desktop (Claude 2 and Claude 3 parallel/sequential)
**Priority**: CRITICAL
**Type**: Execution (destructive operations)

---

## PREAMBLE: THE EIGHTEEN LENSES

This directive has been evaluated against all accumulated critical lenses:

### Original Nine (Oracle4)
1. **Syncrescendent Route** — Continuous, cyclic, recursive
2. **Bitter Lesson Scaling** — General methods, large-context-ready
3. **Antifragile** — Stronger from disorder
4. **Meet the Moment / Crest** — Timely + runway for what's coming
5. **Steelman & Redteam** — Survives strongest attack
6. **Personal Idiosyncrasies** — Macroscopic-first, hub-and-spoke cognition
7. **Potency Without Resolution Loss** — Maximum compression, full fidelity
8. **Elegance + Developer Happiness** — Minimal surface, predictable patterns
9. **Agentify + Human-Navigable** — 2 decisions to any file, Obsidian-comprehensible

### Extended Nine (Oracle6)
10. **First Principles** — Does this need to exist? Why?
11. **Systems Thinking** — How do parts relate to whole?
12. **Industrial Engineering** — Throughput, efficiency, process optimization
13. **Complexity Theory** — Essential vs accidental complexity
14. **Permaculture (generalized)** — Self-sustaining, regenerative design
15. **Design Thinking** — Human-centered, empathy-driven
16. **Agile** — Shippable increment, iterative improvement
17. **Lean** — Eliminate waste, value stream focus
18. **Six Sigma (generalized)** — Defect elimination, variation reduction

---

## CONTEXT: THE ACTUAL STATE

### Quantified Problems

| Problem | Scope | Impact |
|---------|-------|--------|
| Duplicate CANON files (old + new naming) | ~65 file pairs | ~2.5M wasted bytes |
| Backup files (.backup, _md.backup) | ~19 files | ~500K wasted bytes |
| Legacy naming ("Technology Lunar", "Technological_Lunar_") | ~20 files | Confusion, non-portable |
| `.txt.txt` double extensions | ~2 files | Obvious defect |
| Directory names with spaces/dashes (`- Apple/`) | ~4 directories | Non-portable, breaks scripts |
| Prompts duplication (multiple naming conventions) | ~30 files | Retrieval confusion |
| No enforced naming convention | 100% | Agent and human confusion |

**Estimated waste**: 40-50% of repository content is redundant or legacy.

### Why This Matters

1. **Context Window Waste**: Duplicates consume tokens when loaded
2. **Retrieval Ambiguity**: Which file is authoritative?
3. **Onboarding Impossible**: No one can learn this structure
4. **Platform Non-Portability**: Cannot upload cleanly to any frontier lab
5. **Agent Confusion**: Pattern matching fails with inconsistent naming
6. **Human Confusion**: Synaptic navigation impossible

---

## PART 1: NAMING ARCHITECTURE SPECIFICATION

### 1.1 Design Principles

**Human Requirements** (synaptic, subconscious, automatic):
- Light-switch ease — reach and find
- Gestalt recognition — shape tells function
- Consistent rhythm — predictable patterns
- Visual scanning — differentiation at glance

**Agent Requirements** (parseable, predictable, unambiguous):
- Regex-friendly patterns
- Metadata extractable from filename
- No special characters requiring escaping
- Hierarchical information encoded in name

**Bifurcation Strategy**:
- **Filesystem**: Agent-optimized, strict convention
- **Obsidian**: Human-optimized via aliases and display names
- **Same content, different interfaces**

### 1.2 Case Convention Standard

| Case Type | Usage | Example |
|-----------|-------|---------|
| SCREAMING_SNAKE | Tier prefixes, constants | `CANON`, `GENESIS`, `QUEUE` |
| kebab-case | Directory names, human paths | `prompts/`, `execution-logs/` |
| PascalCase | Canonical identities | `SYNCRESCENDENCE`, `PALACE` |
| snake_case | Multi-word components within segment | `execution_log`, `tech_stack` |

**Connector Convention**:
- Hyphen `-` separates semantic segments (tier-number-identity)
- Underscore `_` joins words within a segment (MULTI_WORD)
- Period `.` only for extension

### 1.3 File Type Teleology

| Extension | Teleological Function | Processing Expectation |
|-----------|----------------------|------------------------|
| `.md` | Prose, documentation, narrative | Human reading, LLM context |
| `.yaml` | Configuration, profiles, schemas | Machine parsing, structured data |
| `.xml` | Functions, prompts, templates | Invocation, transformation |
| `.sh` | Automation, scripts | Execution |
| `.txt` | Raw input, legacy, unprocessed | Pending transformation or deletion |
| `.json` | Data interchange, state | Machine parsing |

**Teleological Implication**: `.txt` files are temporary — they await processing into `.md` or deletion.

### 1.4 CANON Naming Convention (ENFORCED)

**Pattern**:
```
CANON-{NNNNN}-{IDENTITY}-{tier}.md
```

**Components**:
- `CANON` — Tier prefix (SCREAMING_SNAKE)
- `{NNNNN}` — 5-digit hierarchical number (00000-99999)
- `{IDENTITY}` — Canonical identity (SCREAMING_SNAKE with underscores)
- `{tier}` — Body type (lowercase: cosmos, core, lattice, chain, meta)

**Examples**:
```
CANON-00001-SYNCRESCENDENCE-cosmos.md
CANON-31141-FIVE_ACCOUNT-satellite.md
CANON-35200-GAIAN_NODE-lunar.md
```

**Hierarchy Encoding in Number**:
```
00xxx — cosmos tier (meta-systemic)
1xxxx — core tier (foundational)
2xxxx — lattice tier (architectural)
30xxx — Intelligence chain
31xxx — Information chain
32xxx — Insight chain
33xxx — Expertise chain
34xxx — Knowledge chain
35xxx — Wisdom chain
99xxx — meta tier (historical)
```

**Body Type in Tier Segment** (for orbital disambiguation):
- `cosmos` — meta-systemic documents
- `core` — foundational definitions
- `lattice` — architectural specifications
- `chain` — chain root documents
- `planetary` — planetary body documents
- `lunar` — lunar documents
- `satellite` — satellite documents
- `comet` — comet documents
- `asteroid` — asteroid documents
- `ring` — ring documents
- `meta` — historical/archival

### 1.5 GENESIS Naming Convention

**Pattern**:
```
GENESIS-{NNN}-{IDENTITY}.md
```

**Examples**:
```
GENESIS-000-ORIGIN.md
GENESIS-001-LINEAGE.md
GENESIS-002-PRINCIPLES.md
```

### 1.6 OPERATIONAL Naming Convention

**Directory Structure** (flattened from current):
```
OPERATIONAL/
├── functions/           # XML function definitions
│   ├── distill/
│   ├── transform/
│   └── expand/
├── prompts/             # System prompt configurations
│   ├── profiles/        # MODEL_PROFILE-*.yaml files
│   └── accounts/        # Account-specific prompts by platform
├── processing/          # Processing documentation
└── claude/              # Claude-specific operational docs
```

**File Naming**:
- Functions: `{verb}.xml` (e.g., `amalgamate.xml`, `transcribe_youtube.xml`)
- Profiles: `MODEL_PROFILE-{Model}-{Version}.yaml`
- Accounts: `{platform}-{account}-{type}.md`

### 1.7 QUEUE Naming Convention

**Pattern**:
```
QUEUE-{source}-{topic}.md
```

Or directory-based:
```
QUEUE/
├── youtube/
├── literature/
├── modal2/
└── pending/
```

### 1.8 orchestration/ Naming Convention

**Already reasonably structured. Minor adjustments**:
```
orchestration/
├── directives/          # DIRECTIVE-{NNN}_{IDENTITY}.md
├── execution-logs/      # EXECUTION_LOG-{YYYY-MM-DD}-{NNN}.md
├── scaffolding/         # Working documents (ALPHA_*, BETA_*)
└── state/               # CURRENT_STATE.md, BACKLOG.md
```

---

## PART 2: DUPLICATE ELIMINATION PROTOCOL

### 2.1 Identification Rules

**A file is DUPLICATE if**:
1. It matches the content of another file with different naming
2. It uses OLD naming convention when NEW exists
3. It is a `.backup` file of an existing current file
4. It has double extension (`.txt.txt`)

**OLD naming patterns to eliminate**:
```
CANON-{NNNNN}-{tier}-{LONG_LEGACY_NAME}*.md
CANON-{NNNNN}-chain-{CHAIN}-{hierarchy}*.md
Technology Lunar - *.md
Technological Lunar - *.md
Technological_Lunar_*.txt
*.backup
*_md.backup
```

**NEW naming pattern to KEEP**:
```
CANON-{NNNNN}-{IDENTITY}-{tier}.md
```

### 2.2 Deletion Checklist

**Before deleting ANY file**:
- [ ] Verify NEW naming version exists
- [ ] Verify content is identical or NEW is more recent
- [ ] Record deletion in execution log
- [ ] Confirm file is not the ONLY copy

**Files to DELETE** (after verification):

| Pattern | Expected Count | Action |
|---------|----------------|--------|
| `CANON-*-{tier}-{LONG_NAME}*.md` (old) | ~65 | DELETE after verifying new exists |
| `*.backup` | ~19 | DELETE (git preserves history) |
| `*_md.backup` | ~19 | DELETE |
| `Technological_Lunar_*.txt` | ~12 | DELETE or CONSOLIDATE |
| `Technology Lunar - *.md` in QUEUE | ~6 | KEEP (queue items, not duplicates) |
| `.txt.txt` files | ~2 | FIX extension |

### 2.3 Directory Cleanup

**Rename**:
```
OPERATIONAL/prompts/- Apple/  →  OPERATIONAL/prompts/accounts/apple/
OPERATIONAL/prompts/- Google/ →  OPERATIONAL/prompts/accounts/google/
```

**Consolidate prompt files**:
- Multiple versions of same prompt → Keep most recent
- `ChatGPT1.md`, `ChatGPT2.md` → Rename to semantic names or consolidate
- `Claude1.md`, `Claude2.md` → Same

---

## PART 3: EXECUTION SEQUENCE

### Phase A: Safe Backup (Claude 2)

**MUST complete before any deletions**:

```bash
# Create timestamped backup of entire repo
cd /path/to/syncrescendence
git add -A
git commit -m "pre-DIRECTIVE-024: backup before ruthless forge"
git tag DIRECTIVE-024-PRE
```

**Deliverable**: `EXECUTION_LOG-2025-12-31-024A.md`

### Phase B: Duplicate Identification (Claude 2)

**Task**: Generate complete list of duplicate files with verification.

```bash
# Find all files matching old naming pattern
find . -name "CANON-*-cosmos-*.md" -o -name "CANON-*-chain-*.md" \
       -o -name "CANON-*-lattice-*.md" -o -name "CANON-*-core-*.md"

# Find all backup files
find . -name "*.backup" -o -name "*_md.backup"

# Find legacy naming
find . -name "Technological_Lunar_*" -o -name "Technology Lunar*"

# Find double extensions
find . -name "*.txt.txt"
```

**Produce**: `DUPLICATE_MANIFEST.md` listing every file to delete with:
- File path
- Corresponding authoritative file (if applicable)
- Verification status
- Recommended action

**Deliverable**: `EXECUTION_LOG-2025-12-31-024B.md`

### Phase C: Deletion Execution (Claude 3)

**AFTER Phase B verification**:

```bash
# Delete old naming convention files
# (only after verifying each has new naming equivalent)

# Delete backup files
find . -name "*.backup" -delete
find . -name "*_md.backup" -delete

# Fix double extensions
# (manual review required)
```

**Produce**: Deletion confirmation with file counts.

**Deliverable**: `EXECUTION_LOG-2025-12-31-024C.md`

### Phase D: Directory Restructure (Claude 3)

**Rename problematic directories**:

```bash
# Fix spaces and special characters
mv "OPERATIONAL/prompts/- Apple" "OPERATIONAL/prompts/accounts/apple"
mv "OPERATIONAL/prompts/- Google" "OPERATIONAL/prompts/accounts/google"
```

**Consolidate prompt files** into structured accounts/ directory.

**Deliverable**: `EXECUTION_LOG-2025-12-31-024D.md`

### Phase E: Verification & Commit (Claude 2 or 3)

```bash
# Verify no broken references
# Run tree to confirm structure
tree -L 3 > POST_FORGE_TREE.md

# Commit
git add -A
git commit -m "DIRECTIVE-024: ruthless forge complete - duplicates eliminated, naming enforced"
git tag DIRECTIVE-024-POST
```

**Produce**: `POST_FORGE_TREE.md` and final state summary.

**Deliverable**: `EXECUTION_LOG-2025-12-31-024E.md`

---

## PART 4: OBSIDIAN CONFIGURATION

After filesystem cleanup, configure Obsidian for human navigation:

### 4.1 Aliases

In frontmatter of each CANON file, add human-friendly alias:
```yaml
aliases:
  - "Syncrescendence Core"
  - "The North Star"
```

### 4.2 Graph Configuration

- Enable local graph for hub-and-spoke navigation
- Color nodes by tier (cosmos = gold, chain = blue, etc.)
- Size nodes by link count

### 4.3 Display Names

Obsidian can show aliases in graph and links while filesystem uses agent-optimized names.

---

## PART 5: VALIDATION CRITERIA

### Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Duplicate files | 0 | `find . -name "*.backup"` returns empty |
| Old naming files | 0 | No `CANON-*-{tier}-{LONG}*.md` patterns |
| Double extensions | 0 | No `.txt.txt` files |
| Problematic directories | 0 | No spaces or special chars in paths |
| Total file count reduction | 30-40% | Compare pre/post counts |
| Repository size reduction | 25-35% | Compare pre/post sizes |

### Portability Test

After cleanup, verify repository can be:
- [ ] Uploaded to fresh Claude Project (no errors)
- [ ] Cloned via git (no path issues)
- [ ] Rendered in Obsidian (graph coherent)
- [ ] Listed with `tree` (no escaping issues)

---

## PART 6: EIGHTEEN-LENS EVALUATION

| Lens | How This Directive Addresses It |
|------|--------------------------------|
| Syncrescendent Route | Establishes continuous naming convention for future cycles |
| Bitter Lesson Scaling | Flat naming scales with context window growth |
| Antifragile | Single convention prevents future drift |
| Meet the Moment | Enables platform portability NOW |
| Steelman & Redteam | Convention survives "what if new file type?" attack |
| Personal Idiosyncrasies | Hub-and-spoke via Obsidian graph preserved |
| Potency Without Resolution Loss | Naming encodes hierarchy without deep nesting |
| Elegance + Developer Happiness | Predictable patterns, no special cases |
| Agentify + Human-Navigable | Filesystem for agents, Obsidian aliases for humans |
| First Principles | Every file must justify existence |
| Systems Thinking | Naming convention is coherent system |
| Industrial Engineering | Eliminates waste, improves throughput |
| Complexity Theory | Removes accidental complexity (duplicates) |
| Permaculture | Self-sustaining convention, regenerative |
| Design Thinking | Human-centered via Obsidian layer |
| Agile | Shippable after each phase |
| Lean | 40% waste elimination |
| Six Sigma | Defect elimination (duplicates, naming variance) |

---

## PART 7: SATELLITE SIZE NOTE

**Large satellites (100K+) are not automatically bloat.**

Technical and tactical documents (CANON-31141, 31142, 31143) may legitimately require extensive specification. The question is not "is it large?" but:

1. **First Principles**: Does each section justify its existence?
2. **Potency**: Is every paragraph earning its tokens?
3. **Gravity**: Should this satellite be promoted to lunar or planetary status?

**Content compression is a SEPARATE directive** (DIRECTIVE-025) after structural cleanup.

---

## DELIVERABLES SUMMARY

| Phase | Deliverable | Owner |
|-------|-------------|-------|
| A | `EXECUTION_LOG-2025-12-31-024A.md` (backup confirmation) | Claude 2 |
| B | `EXECUTION_LOG-2025-12-31-024B.md` + `DUPLICATE_MANIFEST.md` | Claude 2 |
| C | `EXECUTION_LOG-2025-12-31-024C.md` (deletion confirmation) | Claude 3 |
| D | `EXECUTION_LOG-2025-12-31-024D.md` (restructure confirmation) | Claude 3 |
| E | `EXECUTION_LOG-2025-12-31-024E.md` + `POST_FORGE_TREE.md` | Claude 2/3 |

**All deliverables saved to**: `orchestration/execution-logs/`

---

## EXECUTION AUTHORIZATION

**This directive authorizes DESTRUCTIVE OPERATIONS** (file deletion, directory restructuring).

**Safeguards**:
1. Git backup with tag before any changes
2. Manifest review before deletion
3. Phased execution with verification gates
4. Execution logs for each phase

**Proceed when ready. The ruthless forge begins.**

---

*Every token fights for its place. This is how superlativity is achieved.*
