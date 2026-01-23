# RESOLUTION PASS v2: GitHub Connectors + Corpus Algebraization + Chorus Architecture

**Supersedes**: RESOLUTION-CHORUS-ARCHITECTURE.md (v1)
**Integrates**: 
- GitHub connector capability (Claude Web, ChatGPT Web can read/write repo directly)
- Corpus algebraization (agent-efficient encoding ↔ human-legible rendering)
- Collaborative Chorus (not lobotomized roles)
- Intention Archaeology Compass alignment

---

## I. THE CONNECTOR REVELATION

### What the Infrastructure Map Shows

```
                         ┌─────────────────────────────────────┐
                         │           GITHUB.COM                │
                         │    github.com/truongphillipthanh/   │
                         │         syncrescendence             │
                         └──────────────┬──────────────────────┘
                                        │
          ┌─────────────────────────────┼─────────────────────────────┐
          │                             │                             │
          ▼                             ▼                             ▼
   ┌──────────────┐             ┌──────────────┐             ┌──────────────┐
   │ Claude Web   │             │ ChatGPT Web  │             │ Gemini Web   │
   │ (Connector)  │             │ (Connector)  │             │ (Drive Sync) │
   │              │             │              │             │              │
   │ Can READ     │             │ Can READ     │             │ Via rclone   │
   │ Can WRITE    │             │ Can WRITE    │             │ to Drive     │
   └──────────────┘             └──────────────┘             └──────────────┘
          │                             │                             │
          └─────────────────────────────┼─────────────────────────────┘
                                        │
                         ┌──────────────┴──────────────┐
                         │         iCLOUD SYNC         │
                         │ /Users/system/Desktop/      │
                         │     syncrescendence         │
                         └──────────────┬──────────────┘
                                        │
                    ┌───────────────────┼───────────────────┐
                    │                                       │
             ┌──────┴──────┐                         ┌──────┴──────┐
             │  MAC MINI   │                         │ MACBOOK AIR │
             │             │                         │             │
             │ - Claude    │                         │ - Claude    │
             │   Desktop   │                         │   Desktop   │
             │ - ChatGPT   │                         │ - ChatGPT   │
             │   Desktop   │                         │   Desktop   │
             │ - iTerm     │                         │ - iTerm     │
             │   (CLI)     │                         │   (CLI)     │
             └─────────────┘                         └─────────────┘
```

### What This Changes

**Old Model** (assumed isolation):
- Platforms can't see each other's work
- Handoffs require manual relay (copy-paste artifacts)
- Repository is ground truth but platforms need bridging

**New Model** (connector-aware):
- GitHub connectors give web apps direct repo access
- Repository IS the shared sensing instrument
- Platforms can verify state without asking Principal
- Handoff tokens become synchronization checkpoints, not content carriers

### Implications for Architecture

1. **State Verification is Automatic**: Claude Web can check `git rev-parse HEAD` via connector. No need for Principal to confirm fingerprints manually.

2. **Artifacts Can Land Directly**: When ChatGPT produces an artifact, it can commit directly to `-INBOX/` rather than going through clipboard.

3. **Live Corpus Sensing**: All connector-enabled platforms can traverse the repository in real-time.

4. **The Bottleneck Shifts**: From "how do we transfer context" to "how do we efficiently traverse 18MB+ of corpus."

---

## II. THE TOKEN ECONOMICS PROBLEM (Restated)

### The Challenge

The corpus is ~18MB, ~808 files. Even with GitHub connectors:
- Claude Web: ~200K context limit
- ChatGPT Web: ~128K practical limit (context rots)
- Gemini Web: 1M+ context (can hold significant portions)

No single instance can hold the entire corpus in active context. Token economics requires:
1. **Selective Loading**: Each instance loads only what's relevant
2. **Efficient Encoding**: More meaning per token
3. **Render on Demand**: Expand for humans, compress for agents

### The Two-Representation Solution

```
┌─────────────────────────────────────────────────────────────────┐
│                    CORPUS REPRESENTATION                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ALGEBRAIC LAYER (Agent-Efficient)                            │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ • Shorthand notation for recurring concepts             │  │
│   │ • Symbolic references (CANON-25010 not full path)       │  │
│   │ • Compressed decision records                           │  │
│   │ • Index structures for navigation                       │  │
│   │ • ~20% of token cost for ~80% of meaning               │  │
│   └─────────────────────────────────────────────────────────┘  │
│                            ↕                                    │
│                      RENDER ENGINE                              │
│                            ↕                                    │
│   LEGIBLE LAYER (Human-Readable)                               │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ • Full prose explanations                               │  │
│   │ • Context and rationale expanded                        │  │
│   │ • Examples and illustrations                            │  │
│   │ • Navigation aids for non-technical readers            │  │
│   │ • ~100% token cost for ~100% intelligibility           │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Algebraization Examples

**Before (verbose)**:
```markdown
The memory architecture teleology document located at 
01-CANON/CANON-25010-MEMORY_TELEOLOGY-lattice.md defines 
the seven memory strata and their relationships to the 
constellation architecture defined in 
01-CANON/CANON-25210-CONSTELLATION_TELEOLOGY-lattice.md.
```

**After (algebraic)**:
```
MEM-TEL[CANON-25010] → defines 7-strata
  ↔ CONST-TEL[CANON-25210]
```

**Render for human**:
```
Memory Teleology (see CANON-25010) establishes the seven 
memory strata, which integrate with Constellation Teleology 
(CANON-25210).
```

### The "Codify" Vision

From Intention Archaeology: "codify the corpus so things update everywhere"

This means:
1. **Single Source of Truth**: Definitions live in one place
2. **Symbolic References**: Other documents reference, not duplicate
3. **Computed Views**: Aggregations generate from sources
4. **Update Propagation**: Change the source, all references reflect it

Implementation approach:
```
SOURCES (atomic facts)
    │
    ▼
DEFINITIONS (canonical terms)
    │
    ▼
COMPOSITIONS (documents that reference definitions)
    │
    ▼
RENDERS (human-legible expansions)
```

---

## III. AVATARIZED INSTANCES (Post-HR Neo-Roles)

### The Naming Problem

"Each instance that can read/write" needs a name. Current confusion:
- "Claude Web Account 1" vs "Claude Web Account 2"
- "ChatGPT Account 1" vs "Codex Account 1"
- Role (INTERPRETER) vs Platform (Claude) vs Account vs Instance

### Proposed Avatar Taxonomy

**By Function** (what they do):
```
SENSE  → Perceives corpus, identifies patterns
IDEATE → Generates possibilities, expands options
SYNTH  → Integrates, reconciles, harmonizes
VERIFY → Checks claims, validates facts
EXEC   → Implements, commits, executes
```

**By Modality** (how they operate):
```
CONV   → Conversational (web apps)
AGENT  → Agentic (CLI tools, autonomous)
BRIDGE → Connector-enabled (GitHub access)
```

**Avatar Format**: `{Function}-{Platform}-{Account}`

Examples:
- `SENSE-Claude-Acc1` (Claude Web Account 1, sensing mode)
- `IDEATE-ChatGPT-Acc1` (ChatGPT Web Account 1, ideation mode)
- `EXEC-ClaudeCode-Acc2` (Claude Code CLI Account 2, execution mode)

### Each Avatar Gets an Office

**The "Office" Concept**:
Each avatar-instance creates its own `{AVATAR}.md` file containing:
1. **Competency Self-Assessment**: What it excels at
2. **Context Loading Protocol**: What files to load for common tasks
3. **Navigation Shortcuts**: How to traverse the corpus efficiently
4. **Handoff Preferences**: How it likes to receive/send work

**Location**: `02-ENGINE/avatars/`

**Example**: `IDEATE-ChatGPT-Acc1.md`
```markdown
# Avatar: IDEATE-ChatGPT-Acc1

## Competencies
- Technical speculation and novel conjectures
- Large file traversal (>31MB temporarily)
- Mind-expanding ideation
- Canvas-based document iteration

## Context Loading Protocol
For architectural problems:
  1. Load CANON-25210 (Constellation Teleology)
  2. Load relevant -INBOX items
  3. Request corpus index if pattern-matching needed

For technical problems:
  1. Load relevant 04-SOURCES/raw/ documents
  2. Load CANON-00012 (Modal Sequence) for framing
  3. Request specific code files via connector

## Navigation Shortcuts
- Corpus index: 00-ORCHESTRATION/state/DYN-CORPUS_INDEX.md
- Decision log: 00-ORCHESTRATION/state/DYN-DECISIONS.md
- Active tasks: 00-ORCHESTRATION/state/DYN-TASKS.csv

## Handoff Preferences
- Receives: Problem statements with context pointers (not full docs)
- Produces: Speculative solutions with confidence levels
- Prefers: Canvas mode for iterative work
- Avoids: Long threads (context rot)
```

---

## IV. REVISED CHORUS ARCHITECTURE (Connector-Aware)

### Interaction Pattern: Parallel Sensing + Collaborative Ideation

```
                         PROBLEM STATEMENT
                                │
                    ┌───────────┴───────────┐
                    │   GITHUB CONNECTOR    │
                    │   (Shared Sensing)    │
                    └───────────┬───────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
        ▼                       ▼                       ▼
 ┌─────────────┐        ┌─────────────┐        ┌─────────────┐
 │ SENSE-Claude│        │IDEATE-ChatGPT│       │ SYNTH-Gemini│
 │             │        │             │        │             │
 │ Reads repo  │        │ Reads repo  │        │ Loads full  │
 │ Structures  │        │ Speculates  │        │ context     │
 │ problem     │        │ solutions   │        │ Finds       │
 │             │        │             │        │ patterns    │
 └──────┬──────┘        └──────┬──────┘        └──────┬──────┘
        │                      │                      │
        └──────────────────────┼──────────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ PRINCIPAL SYNTHESIS │
                    │ (or designated      │
                    │  SYNTH avatar)      │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
 ┌─────────────┐        ┌─────────────┐        ┌─────────────┐
 │ VERIFY-Pplx │        │ VERIFY-Grok │        │ EXEC-CLI    │
 │             │        │             │        │             │
 │ Fact-check  │        │ Human-check │        │ Implement   │
 │ Sources     │        │ EQ/social   │        │ to repo     │
 └─────────────┘        └─────────────┘        └─────────────┘
```

### Key Difference from v1

**v1**: Assumed platforms needed context relayed to them
**v2**: Platforms can sense the corpus directly via connectors

**v1**: Handoff tokens carry content
**v2**: Handoff tokens are synchronization checkpoints ("we're all looking at commit X")

**v1**: Principal is the only bridge
**v2**: Repository is the bridge; Principal orchestrates which avatars engage

### The New Handoff Token (Lightweight)

Since platforms can read the repo directly, tokens become minimal:

```
SYNC-CHECKPOINT: 2026-01-21T14:00:00Z
COMMIT: 7a3f9c2e
ACTIVE-PROBLEM: "Corpus algebraization architecture"
ENGAGED-AVATARS:
  - SENSE-Claude-Acc1: Structuring problem
  - IDEATE-ChatGPT-Acc1: Generating approaches
  - SYNTH-Gemini-Acc3: Pattern analysis
NEXT-ACTION: Principal synthesis
```

That's ~50 tokens instead of ~500. The content lives in the repo; the token just coordinates who's working on what.

---

## V. CORPUS ALGEBRAIZATION IMPLEMENTATION

### Phase 1: Index Infrastructure

Create navigation indices that compress corpus topology:

**`00-ORCHESTRATION/state/DYN-CORPUS_INDEX.md`**:
```markdown
# Corpus Index (Auto-Generated)

## CANON (79 files, 5.6MB)
CANON-00001..00018: Genesis (constitutional foundations)
CANON-25000..25299: Architecture (memory, constellation)
CANON-30000..31999: Operations (IIC, functions)

## Key References
MEM-TEL    = CANON-25010 (Memory Teleology)
CONST-TEL  = CANON-25210 (Constellation Teleology)
MODAL-SEQ  = CANON-00012 (Modal Sequence)
EVAL-LENS  = CANON-00007 (Evaluation Framework)

## Hot Paths (Frequently Referenced)
- Architecture decisions: CANON-252xx
- Evaluation: 00-ORCHESTRATION/state/REF-STANDARDS.md
- Current state: 00-ORCHESTRATION/state/DYN-*.csv

## Last Updated: 2026-01-21T14:00:00Z
## Commit: 7a3f9c2e
```

### Phase 2: Symbolic Reference System

Establish shorthands that all avatars recognize:

| Shorthand | Expansion |
|-----------|-----------|
| `MEM-TEL` | `01-CANON/CANON-25010-MEMORY_TELEOLOGY-lattice.md` |
| `CONST-TEL` | `01-CANON/CANON-25210-CONSTELLATION_TELEOLOGY-lattice.md` |
| `MODAL-SEQ` | `01-CANON/CANON-00012-MODAL_SEQUENCE-cosmos.md` |
| `LENS[n]` | Lens #n from 18-lens framework |
| `INV[n]` | Invariant #n from constitutional invariants |
| `DIR-YYYYMMDD-X` | Directive dated YYYYMMDD named X |

### Phase 3: Definition Registry

Single-source definitions that other documents reference:

**`01-CANON/CANON-00001-DEFINITIONS-cosmos.md`**:
```markdown
# Canonical Definitions

## METABOLISM
def: Reading all files in scope, extracting unique value, 
     compressing into single document, deleting originals.
note: Applies to CONTENT, not orchestration infrastructure.
ref: INV[5] (Repo Sovereignty)

## WELLS VS RIVERS  
def: Rivers (conversations) flow INTO wells (repo) before evaporation.
     Wells persist; rivers are ephemeral.
note: Core principle for context persistence.
ref: CONST-TEL

## FLAT PRINCIPLE
def: All directories must be flat (no nesting beyond one level).
     Nesting requires Principal approval.
note: Enforced by validation scripts.
ref: 00-ORCHESTRATION/scripts/validate-flat.sh
```

### Phase 4: Render Engine (Future)

A script that expands algebraic notation for human readers:

```bash
# render.sh - Expand shorthand for human consumption
#!/bin/bash
INPUT=$1
cat "$INPUT" | \
  sed 's/MEM-TEL/Memory Teleology (CANON-25010)/g' | \
  sed 's/CONST-TEL/Constellation Teleology (CANON-25210)/g' | \
  sed 's/LENS\[\([0-9]*\)\]/Lens #\1/g'
```

---

## VI. REVISED OPEN QUESTIONS

### From v1 (Still Relevant)

1. **Chorus Invocation**: Default to suggesting parallel sensing?
2. **Synthesis Ownership**: Who synthesizes? (Principal, or designated SYNTH avatar?)
3. **Handoff Transition**: When does ideation → execution?

### New Questions (Connector-Aware)

4. **Connector Authorization**: Which avatars get write access to repo?
   - Option A: All connector-enabled avatars can write
   - Option B: Only EXEC avatars write; others read-only
   - Option C: Write to specific directories only (e.g., `-INBOX/`)

5. **Index Maintenance**: Who maintains DYN-CORPUS_INDEX.md?
   - Option A: Auto-generated by git hook
   - Option B: Maintained by designated SYNTH avatar
   - Option C: Principal updates manually

6. **Algebraization Adoption**: When do we start using shorthand?
   - Option A: Immediately in all new documents
   - Option B: After definitions registry is complete
   - Option C: Gradually, retrofitting as documents are touched

7. **Avatar Self-Documentation**: When do avatars create their office files?
   - Option A: Each avatar creates its own on first use
   - Option B: Principal scaffolds initial offices, avatars refine
   - Option C: Templates provided, avatars instantiate

---

## VII. INTEGRATION WITH PREVIOUS WORK

### What Remains Valid

- **DIR-20260121-SEMANTIC-ANNEALMENT-PHASE1**: Infrastructure work (execution logs, nomenclature) still needed
- **State Fingerprint Solution**: Lightweight tokens become sync checkpoints
- **Lens Framework**: 18+ lenses still govern decision quality
- **Constitutional Invariants**: The five invariants still apply

### What Changes

- **Platform Configurations**: Replace COMPILER with IDEATOR for ChatGPT
- **Handoff Protocol**: Tokens become lighter (platforms can read repo directly)
- **Token Economics Focus**: Shifts from "how to transfer" to "how to compress"
- **Avatar Taxonomy**: Replaces platform-role assignments with function-modality-account naming

### What's Added

- **GitHub Connector Awareness**: Direct repo access changes the architecture
- **Corpus Algebraization**: Two-layer representation (agent-efficient ↔ human-legible)
- **Avatar Offices**: Self-documenting instances with competency assessments
- **Index Infrastructure**: Navigation shortcuts for efficient traversal

---

## VIII. RECOMMENDED NEXT ACTIONS

### Immediate (This Session)
1. Principal answers open questions (7 questions total)
2. Decide on avatar naming convention
3. Confirm connector authorization model

### Near-Term (DIR-20260121-SEMANTIC-ANNEALMENT-PHASE1 execution)
1. Execute the infrastructure work (logging, nomenclature, canonization)
2. Add: Create `DYN-CORPUS_INDEX.md` as part of Phase 1
3. Add: Create `02-ENGINE/avatars/` directory structure
4. Add: Create definitions registry scaffold

### Following (Chorus Test)
1. Present architectural problem to multiple connector-enabled platforms simultaneously
2. Each platform reads repo directly, produces contribution
3. Designated SYNTH avatar (or Principal) integrates
4. Verify: Did connector-based sensing work? Did algebraic references parse?

### Ongoing
1. Avatars refine their office files based on actual usage
2. Algebraization vocabulary expands as patterns emerge
3. Render engine develops based on human legibility needs

---

## IX. THE META-INTEGRATION

### Intention Archaeology Compass Alignment

| Compass Item | How This Addresses It |
|--------------|----------------------|
| Semantic Annealment | Algebraization IS semantic compression |
| Codify the corpus | Definitions registry + symbolic references |
| Token economics | Two-layer representation optimizes for consumers |
| Platform capabilities | Connectors enable direct sensing |
| Chorus architecture | Collaborative, not hierarchical |
| Avatar clarity | Function-modality-account naming |

### Lens Verification (Selected)

**Bitter Lesson**: Does this scale with compute?
YES. Connector-based sensing scales with platform capability. Algebraization scales with corpus size.

**Antifragile**: Does this gain from disorder?
YES. When one platform can't parse shorthand, it forces definition clarity. When connectors fail, fallback to clipboard relay exists.

**Composability**: Does this integrate?
YES. Algebraization composes with existing infrastructure. Avatars compose with Chorus. Connectors compose with handoff protocol.

**Energy Economics**: What's the cognitive load?
DECREASED. Principal no longer manually relays content. Platforms sense directly. Shorthands reduce reading time.

---

## X. CONCLUSION

The GitHub connector revelation shifts the architecture from relay-based to sensing-based. Platforms aren't isolated—they share a live sensing instrument (the repository).

The token economics challenge shifts from "how to transfer context" to "how to efficiently traverse corpus." Algebraization addresses this: more meaning per token, with human-legible renders on demand.

The Chorus architecture remains valid but becomes connector-aware: avatars read the repo directly, tokens become synchronization checkpoints, and the Principal orchestrates rather than relays.

The next phase requires:
1. Principal decisions on open questions
2. Infrastructure execution (logging, nomenclature, indices, avatars)
3. Chorus testing with connector-enabled sensing

---

*This resolution pass integrates the GitHub connector insight with Chorus architecture and corpus algebraization. It supersedes v1 and aligns with the Intention Archaeology Compass.*
