# Canon Remediation — Pass 8 Response: Syncrescript Vision + Ratification

**Commander (Claude Opus 4.6) → Sovereign | CC42**

---

# PART I: SYNCRESCRIPT VISION

## A. Current SN Assessment

### Compression Analysis (12 Files Sampled)

| File | Canon Lines | SN Lines | Compression | AI Readability |
|------|-------------|----------|-------------|----------------|
| 00000 Schema | 1,704 | 1,704 | 1.0x (unconverted) | N/A |
| 00003 Principles | 337 | 158 | 2.1x (66%) | 9/10 |
| 00005 Syncrescendence | 1,069 | 428 | 2.5x (84%) | 8/10 |
| 20000 Palace | 513 | 174 | 2.9x (72%) | 8/10 |
| 21000 Chain Matrix | 797 | 274 | 2.9x (75%) | 9/10 |
| 25000 Memory Arch | 1,222 | 218 | 5.6x (73%) | 8/10 |
| 30000 Intelligence | 445 | 235 | 1.9x (70%) | 8/10 |
| 30400 Agentic Arch | 537 | 235 | 2.3x (76%) | 9/10 |
| 31100 Acumen | 1,057 | 174 | 6.1x (92%) | 6/10 |
| 33000 Expertise | 246 | 166 | 1.5x (61%) | 9/10 |
| 35000 Wisdom | 309 | 227 | 1.4x (61%) | 9/10 |
| 35200 Gaian Node | 1,304 | 338 | 3.9x (89%) | 8/10 |

**Average: 3.0x line compression, 74% word reduction, 8.3/10 AI readability.**

### What the Current SN Does Well

1. **Structured blocks** (`TERM`, `NORM`, `PROC`, `PASS`, `ARTIFACT`, `TEST`) with consistent fields (`sutra`, `gloss`, `spec`) — machine-parseable and semantically typed.
2. **Preserves all quantitative data** — percentages, costs, timelines, stage criteria survive compression intact.
3. **Critical gate statements preserved verbatim** in quotes — the operationally decisive content survives.
4. **Source citations preserved** — empirical grounding survives compression.
5. **Achieves 3x compression** while maintaining ~8/10 AI reconstruction fidelity.

### What the Current SN Loses

1. **No frontmatter** — `operational_status`, `depends_on`, `version`, `entities_defined` all dropped. An agent reading SN can't tell if a specification is live or aspirational.
2. **No celestial navigation** — parent/sibling/child relationships stripped. The graph topology is invisible.
3. **Variable compression quality** — Acumen (6.1x, 6/10 readability) vs. Expertise (1.5x, 9/10 readability). No consistent compression target.
4. **Prose voice destroyed** — the scripture register is gone. "Two minutes tomorrow morning beats two hours never" becomes `two_minutes_tomorrow >> two_hours_never`. Functionally equivalent; experientially dead.
5. **One unconverted file** (Schema) — incomplete coverage.

### Three Unique SN Files

- `CANON-METRICS_STREAM_A.md` — conversion report for Stream A (process metadata)
- `CANON-METRICS_STREAM_B.md` — conversion report for Stream B (process metadata)
- `CANON-PROTEASE_AXIOMS.sn.md` — six manually-authored axioms from CC32-33 (source-promoted, not a compression of a canon file)

### Verdict

The current SN is a **v1 proof of concept**: it demonstrates that structured compression works and that 3x reduction is achievable. But it's not a compiler output — it's a hand-crafted (or single-pass agent-crafted) artifact with inconsistent quality, missing metadata, and no round-trip guarantee. Syncrescript v2 needs to be a proper compilation target with a formal grammar.

---

## B. Syncrescript Design Principles

### The Influences, Translated

| Influence | What It Means for Syncrescript |
|---|---|
| **Rails** (convention over configuration) | Sensible defaults. A new canon file should need minimal annotation — the compiler infers tier, chain, celestial type, and relationships from content patterns and file location. You shouldn't have to say what's obvious. |
| **Elixir** (concurrency, immutability) | Multiple agents read simultaneously without locks. Canon files are immutable once committed (amendments create new versions, not overwrites). The compiled SN is a read-only artifact — never edited directly. |
| **Rust** (structural typing, compile-time safety) | Incoherence = compile error. If a file declares `chain: information` but its `depends_on` includes no Information-chain ancestor, that's a type error. If `volatility_band: permanent` but `refresh_cadence: quarterly`, that's a contradiction caught at compile time. |
| **Notion** (same data, different views) | One source of truth, five rendered views. The canon markdown is the source. Everything else is derived. No view is primary — each serves a different consumer. |

### The Seven Principles

1. **Single source of truth.** Canon markdown files are the only authored artifacts. Every other representation is derived. If there's a contradiction between views, the canon file wins.

2. **Convention over configuration.** If a file is numbered 31xxx, it's in the Information chain. If it's at depth 3 in the hierarchy, it's a lunar. The compiler shouldn't need to be told what it can infer. Configuration is for exceptions, not rules.

3. **Compile-time coherence enforcement.** The compiler catches:
   - Type mismatches (chain membership vs. dependency graph)
   - Volatility contradictions (band vs. cadence vs. tier)
   - Orphans (no parent, no inbound references)
   - Stale references (links to non-existent files)
   - Version conflicts (YAML vs. body, duplicate keys)
   - Status contradictions (YAML `canonical` vs. body "Non-Canonical")

4. **Immutable compiled output.** SN files are never hand-edited. If the SN is wrong, fix the canon source and recompile. This eliminates the drift between canon and SN that currently exists.

5. **Concurrent read safety.** Any number of agents can read the compiled SN simultaneously. The compilation step is the only write operation. This maps to Elixir's actor model: the canon is the GenServer state, agents are processes that read snapshots.

6. **Lossy compression with declared loss.** Every SN file declares what it dropped (a `compression_manifest` in the header). An agent reading SN knows exactly what information it's missing and can request the canon source for full fidelity.

7. **Round-trip fidelity for structure.** All structural data (frontmatter fields, dependency edges, stage definitions, quantitative thresholds) must survive round-trip: canon → SN → reconstruction. Prose voice is lossy by design — that's what the Scripture view is for.

---

## C. The View Architecture

### 1. Scripture View (Human-Authored Prose)

**Format**: Markdown with YAML frontmatter (current canon format, standardized per Pass 7 Section D).
**Consumer**: The Sovereign, human readers, narrative consumption.
**Authoring standard**:
- Every file has the canonical frontmatter schema (Pass 7 Section D)
- Prose is taste-gated by the Sovereign — agents draft, the Sovereign approves
- H1 = canonical name. H2+ = structural sections. Aphoristic density preferred.
- The scripture register is the voice of the system. This is not documentation — it's doctrine.

**What drives it**: Direct authoring. This is the source layer.

### 2. Config View (Machine-Parseable Parameters)

**Format**: YAML/TOML extracted from frontmatter + structured sections.
**Consumer**: Agents (CLAUDE.md, GEMINI.md), scripts, automation.
**Extraction pipeline**:
```
canon/*.md → parse YAML frontmatter → extract structured sections
           → merge with AGENTS.md templates → render CLAUDE.md / GEMINI.md
```
**What drives it**: `make configs` (existing pipeline). Extended to extract any machine-relevant parameter from canon (stage criteria, thresholds, cadences, cost figures).

**Key enhancement**: Currently `make configs` only generates agent configs. It should also generate:
- `canon_manifest.yaml` — replacing CANON-00006 (Corpus) with an auto-generated equivalent
- `dependency_graph.json` — the cleaned DAG from Pass 6 in machine-parseable form
- `volatility_report.yaml` — which files are past their refresh cadence

### 3. Graph View (Obsidian Topology)

**Format**: Obsidian vault with wikilinks resolved via `aliases` in frontmatter.
**Consumer**: The Sovereign's visual exploration, spatial reasoning.
**What drives it**: Frontmatter fields from Pass 7 Section D:
- `aliases` → wikilink resolution (`[[Acumen]]` → CANON-31100)
- `requires` → directional edges (the cleaned DAG)
- `siblings` → bidirectional edges (peer awareness)
- `tier`, `chain`, `celestial_type` → node styling (color, size, grouping)
- `volatility_band` → heatmap overlay

**Key enhancement**: Obsidian graph groups can be driven by frontmatter tags. Adding `tags: [chain/information, tier/chain, type/planetary, element/air]` to each file enables:
- Group by chain (6 clusters)
- Group by tier (cosmos/core/lattice/chain/archive/immune)
- Group by volatility (permanent/stable/moderate/dynamic)
- Filter by any combination

### 4. Ledger View (Live-Updating State)

**Format**: JSONL or YAML, auto-generated, never hand-edited.
**Consumer**: The session state brief, portal, operational dashboards.
**What's mutable**: operational_status, last_verified, refresh_cadence countdown, atom counts, session references.
**What's immutable**: id, canonical_name, tier, chain, structural relationships.

**The ledger is the only view that changes between compilation cycles.** It tracks:
- Which files are past their refresh cadence (staleness alert)
- Which files were touched in the current session (session delta)
- Which atoms in sources/ are candidates for promotion to which canon files
- The DAG convergence percentage (from DYN-DAG_STATE.json)

**Integration**: The session state brief (`session_state_brief.py`) already generates a portal. The ledger view is that portal's data source, fed by canon frontmatter + runtime state.

### 5. Compiled View (Syncrescript Bytecode)

**Format**: `.sn.md` files — structured blocks with `sutra`/`gloss`/`spec` fields.
**Consumer**: AI agent context windows. The primary use case: fit the entire canon into a context window.
**Compression target**: The current canon is ~50,000 lines. At 3x average compression, the compiled SN would be ~16,500 lines (~120K tokens). Target: fit in a 128K-200K context window with room for conversation.

**Compilation steps** (Section D below).

**Key enhancement over current SN**:
- Frontmatter preserved (as SN header block)
- `compression_manifest` declares what was dropped
- Consistent compression ratio target per tier (cosmos=2x, lattice=3x, chain=3-4x, asteroid=5-6x — more volatile content compresses harder because it's more replaceable)
- `operational_status` preserved — agents can distinguish live vs. aspirational

---

## D. The Compiler Sketch

### Architecture

```
canon/*.md                          ← SOURCE (authored)
    │
    ▼
┌─────────────────────────┐
│  STAGE 1: PARSE         │  Extract frontmatter + AST from markdown
│  (deterministic script)  │  Output: structured JSON per file
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│  STAGE 2: VALIDATE      │  Type-check against schema (Pass 7 §D)
│  (deterministic script)  │  Catch: orphans, stale links, contradictions
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│  STAGE 3: GRAPH         │  Build dependency graph, detect cycles
│  (deterministic script)  │  Output: dependency_graph.json, volatility_report.yaml
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│  STAGE 4: COMPRESS      │  LLM-assisted compression to SN format
│  (agent process)         │  Tier-appropriate ratios. Preserves all quantitative data.
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│  STAGE 5: VERIFY        │  Round-trip check: can an agent reconstruct
│  (agent process)         │  all structural data from SN alone?
└─────────┬───────────────┘
          │
          ▼
canon/sn/*.sn.md                    ← COMPILED (derived, never edited)
canon_manifest.yaml                 ← CONFIG VIEW (derived)
dependency_graph.json               ← GRAPH DATA (derived)
volatility_report.yaml              ← LEDGER DATA (derived)
```

### Stage Details

**Stage 1 (Parse)**: Pure script. Reads YAML frontmatter, splits markdown into sections, produces a JSON AST per file. No AI needed. This is `python parse_canon.py canon/*.md → build/parsed/*.json`.

**Stage 2 (Validate)**: Pure script. Checks every file against the frontmatter schema. Errors:
- `E001: Missing required field` (e.g., no `tier` field)
- `E002: Type mismatch` (e.g., `chain: information` but parent is in Expertise chain)
- `E003: Stale reference` (e.g., `requires: CANON-00008` — file doesn't exist)
- `E004: Volatility contradiction` (e.g., `volatility_band: permanent` + `refresh_cadence: quarterly`)
- `E005: Status contradiction` (e.g., YAML `canonical` vs body "Non-Canonical")
- `E006: Orphan` (no parent, no inbound `requires` edges)
- `E007: Missing frontmatter` (file has no YAML block)
- `W001: Version mismatch` (YAML version ≠ body version)
- `W002: Past refresh cadence` (last_verified + refresh_cadence < today)

**Stage 3 (Graph)**: Pure script. Builds the full dependency graph from `requires`/`siblings`/`synthesizes`. Detects cycles (warning, not error — the current graph has convention-cycles that are harmless). Outputs machine-parseable graph data for the Obsidian and Ledger views.

**Stage 4 (Compress)**: Agent-assisted. An LLM compresses each canon file to SN format using the block grammar (`TERM`/`NORM`/`PROC`/`PASS`/`ARTIFACT`/`TEST` → `sutra`/`gloss`/`spec`). The compression target varies by tier:

| Tier | Target Compression | Rationale |
|---|---|---|
| Cosmos | 2x | Constitutional content — preserve maximum fidelity |
| Core | 2x | Identity content — voice matters |
| Lattice | 3x | Structural frameworks — spec fields carry the load |
| Chain roots | 2-3x | Stage models — gate criteria must be verbatim |
| Planetary/Ring | 3-4x | Domain elaborations |
| Lunar | 4-5x | Methodology — procedures compress well |
| Comet/Asteroid | 5-6x | Dynamic content — most replaceable, compress hardest |
| Archive | 2x | Historical — already condensed |

**Stage 5 (Verify)**: Agent-assisted. A second LLM (or the same one in a clean context) reads the SN output and attempts to reconstruct: (a) all frontmatter fields, (b) all stage/phase definitions, (c) all quantitative thresholds, (d) all dependency relationships. Any reconstruction failure → recompile that file at lower compression.

### Integration with Promotion Pipeline

```
sources/ (14,025 atoms)
    │
    ▼ atom_cluster.py
606 sovereign_review atoms
    │
    ▼ protease_queue.py (5:1 ratio)
Promotion candidates
    │
    ▼ Ontology Gate (falsifiable antigen test)
    │
    ▼ PASS: new canon file authored (Scripture view)
    │
    ▼ Compiler (Stages 1-5)
    │
    ├─→ SN file (Compiled view)
    ├─→ Updated manifest (Config view)
    ├─→ Updated graph (Graph view)
    └─→ Updated ledger (Ledger view)
```

The compiler runs after every canon change — either manually (`make compile-canon`) or via git hook on commit to `canon/`.

---

## E. The Three-Layer Stack

### Layer 1: Canon (Source)

**Responsibility**: Holds the authored truth. Every principle, framework, specification, and narrative exists here and only here. Changes require sovereign taste-gating (for constitutional content) or agent drafting + sovereign approval (for operational content).

**Interface**: Markdown files with standardized YAML frontmatter. Read by the compiler. Read by Obsidian. Read by agents directly when full fidelity is needed.

**Current state**: 86 files, ~50,000 lines. 25% volatility-misplaced (Pass 5). 22% metadata-incomplete (Pass 7). Doctrinally coherent but organizationally incoherent.

**What "fixed" looks like**: All frontmatter standardized, volatility-aligned, dependency graph cleaned, immune system integrated, version conflicts resolved. Passes 5-7 of this remediation.

### Layer 2: Scaffold (Compiler)

**Responsibility**: Transforms canon source into all derived views. Validates coherence. Enforces the schema. Generates the graph, manifest, SN, ledger data. Also manages the promotion pipeline (sources → canon) and the session lifecycle (handoffs, state briefs, autonomy ledger).

**Interface**: Scripts and agent processes. `make validate-canon`, `make compile-canon`, `make configs`. The Makefile is the scaffold's public API.

**Current state**: Heavily decrusted in the parallel session. Scripts directory empty (103 scripts migrated or removed). State directory minimal. The scaffold is a cleared field — ready for new construction, not burdened by old.

**What "fixed" looks like**: The compiler pipeline (Section D) implemented. `make validate-canon` catches all E001-E007 errors. `make compile-canon` produces all five views. The promotion pipeline runs end-to-end with the ontology gate as a compile-time check.

### Layer 3: Exocortex (Runtime)

**Responsibility**: The live cognitive infrastructure. Memory persistence (Graphiti, JSONL journals), session state, agent coordination, the "thinking" layer that consumes canon knowledge and produces new understanding.

**Interface**: The agents themselves. Ajna reads canon + SN in context windows. Commander reads ledger state + session briefs. The exocortex is where canon knowledge becomes operational cognition.

**Current state**: Partially built. Session state brief exists (JSONL persistence). Handoff protocol exists. Autonomy ledger exists. Graphiti connection exists but is not integrated. The exocortex is the least mature layer.

**What "fixed" looks like**:
- **Memory integration**: Graphiti stores the dependency graph as a knowledge graph (entities = canon files, relationships = requires/siblings/synthesizes). Agents query the graph to find relevant canon without reading every file.
- **Live ledger**: The ledger view auto-updates from session activity. Which files were referenced? Which atoms promoted? What's the canon_delta this session?
- **Context-window compilation**: The SN compiled view fits in a context window. An agent can boot with the full canon compressed to ~120K tokens, plus session-specific uncompressed files for the current task.
- **Dream cycle**: The circadian sync concept from CC28 — between sessions, a consolidation process reviews session artifacts, identifies promotion candidates, and prepares the next session's ledger. The exocortex "sleeps."

---

# PART II: RATIFICATION

## F. Summary of Proposed Changes

### Immediate (No Dependencies, Can Execute Now)

| # | Change | Source | Effort | Reversible? |
|---|---|---|---|---|
| I-1 | Add YAML frontmatter to 5 bare files (25500, 31150, Gate v1, Gate v2, retirement_protocol) | Pass 7 §F | Trivial | Yes |
| I-2 | Fix 3 stale chain H1 headings (33000, 34000, 35000) | Pass 7 §F | Trivial | Yes |
| I-3 | Remove CANON-00008 ghost wikilink from 00007 line 854 | Pass 7 §F | Trivial | Yes |
| I-4 | Resolve 31115 identity contradiction (pick canonical or supplement) | Pass 7 §F | Trivial | Yes |
| I-5 | Fix 00014 parent conflict (YAML parent → 00010) | Pass 7 §F | Trivial | Yes |
| I-6 | Remove duplicate YAML keys from 30330, 30340 | Pass 7 §F | Trivial | Yes |
| I-7 | Kill body-inline version numbers (00000, 25200, 99000) — YAML is truth | Pass 7 §F | Trivial | Yes |
| I-8 | Reconcile cost contradiction (designate 31150 as source of truth) | Pass 7 §F | Trivial | Yes |

**Total immediate effort: 8 trivial changes. Achievable in one session.**

### Short-Term (Requires Sovereign Review)

| # | Change | Source | Effort | Decision Required |
|---|---|---|---|---|
| S-1 | Frontmatter standardization — add `tier`, `chain`, `celestial_type`, `volatility_band`, `refresh_cadence`, `canonical_name` to all 86 files | Pass 7 §D | Moderate (batch) | Approve frontmatter schema |
| S-2 | Split `depends_on` into `requires`/`siblings`/`synthesizes` for all files | Pass 7 §D, Pass 6 §B | Heavy (200+ edges to classify) | Approve relationship taxonomy |
| S-3 | Add Obsidian `aliases` for canonical names | Pass 7 §B, §C | Trivial (batch) | Approve neologism registry |
| S-4 | Intelligence decomposition — formalize sub-domains or reclassify as lattice | Pass 5 §B | Moderate | **Sovereign choice: Option 1, 2, or 3** |
| S-5 | Reclassify 13 volatility-misplaced files | Pass 5 §C | Moderate | Approve reclassification list |
| S-6 | Demote 33111 (incomplete), 30450 (dated), 34120 (perishable) | Pass 7 §G | Trivial per file | Approve demotion list |
| S-7 | Establish auto-generated file policy (31150, potentially 00006) | Pass 7 §G | Trivial | Approve policy |
| S-8 | Regenerate CANON-00006 (Corpus) manifest — 15 files behind | Pass 7 §F | Moderate | Decide: auto-generate or hand-maintain? |
| S-9 | Integrate immune system — add inbound references from 00011 to gates and protocols | Pass 6 §D | Trivial | Approve integration approach |

### Medium-Term (Requires Design Work)

| # | Change | Source | Effort | Dependency |
|---|---|---|---|---|
| M-1 | Implement compiler Stage 1 (Parse) + Stage 2 (Validate) | Pass 8 §D | Moderate | S-1 (frontmatter must exist first) |
| M-2 | Implement compiler Stage 3 (Graph) | Pass 8 §D | Moderate | S-2 (relationship split must exist first) |
| M-3 | Implement compiler Stage 4 (Compress) + Stage 5 (Verify) | Pass 8 §D | Heavy | M-1, M-2 |
| M-4 | Extend `make configs` to generate manifest, graph, volatility report | Pass 8 §C | Moderate | M-1 |
| M-5 | Obsidian vault setup with frontmatter-driven graph styling | Pass 8 §C | Moderate | S-1, S-3 |

### Long-Term (Requires New Capabilities)

| # | Change | Source | Effort | Dependency |
|---|---|---|---|---|
| L-1 | Graphiti integration — canon as knowledge graph | Pass 8 §E | Heavy | M-2 |
| L-2 | Live ledger — auto-updating operational state | Pass 8 §C | Heavy | M-4 |
| L-3 | Dream cycle — inter-session consolidation | Pass 8 §E | Heavy | L-2 |
| L-4 | Context-window compilation target — full SN fits in 200K | Pass 8 §C | Heavy | M-3 |
| L-5 | Syncrescript v2 formal grammar | Pass 8 §B | Heavy | M-3 validated |

---

## G. Risk Assessment

| Change | Risk | Mitigation |
|---|---|---|
| **I-1 through I-8** (immediate fixes) | Low. All are metadata corrections. | Git commit before each batch. `git diff` review. |
| **S-1** (frontmatter standardization) | Medium. Batch YAML modification could introduce parsing errors. | Validate with a YAML linter after each batch. Test `make configs` still works. |
| **S-2** (depends_on split) | **High.** 200+ edges to reclassify. Misclassification creates a false dependency graph. | Use Pass 6's cleaned DAG as the starting map. Human review of edge cases. The old `depends_on` field is preserved (deprecated) during migration so the original data isn't lost. |
| **S-4** (Intelligence decomposition) | **High.** Constitutional surgery. Breaks "six chains" doctrine wired into Schema, Corpus, Chain Matrix, Facets. | If Option 2 (sub-domains): minimal breakage, additive change. If Option 1 (lattice): requires coordinated updates to 4+ constitutional files. |
| **S-5** (reclassification) | Medium. Moving files between tiers changes expectations about their review cadence. | Reclassification is a frontmatter field change, not a file move. The file stays in place; its metadata changes. Fully reversible. |
| **M-3** (LLM compression) | Medium. Compression quality varies (Acumen got 6/10 in current SN). | Stage 5 verification catches quality failures. Recompile at lower compression if verification fails. |
| **L-1** (Graphiti) | Low operational risk, high complexity. | Graphiti is additive — it reads from canon, doesn't write to it. If it breaks, canon is unaffected. |

**The only irreversible action in the entire plan is renumbering files (Phase 3 of Pass 7 §C), which is deferred to long-term and optional.** Everything else is additive metadata or derived artifacts.

---

## H. Dependencies

### Critical Path

```
I-1 through I-8 (immediate)
       │
       ▼
S-1 (frontmatter schema) ──→ S-2 (relationship split) ──→ M-1 (parse) ──→ M-2 (graph)
       │                                                                        │
       ├──→ S-3 (aliases) ──→ M-5 (Obsidian)                                   │
       │                                                                        ▼
       ├──→ S-5 (reclassification)                                    M-3 (compress+verify)
       │                                                                        │
       └──→ S-9 (immune integration)                                            ▼
                                                                       L-4 (context window)
S-4 (Intelligence) ──→ independent, can happen anytime after S-1
S-6, S-7, S-8 ──→ independent, can happen anytime
```

### Parallelizable Pairs

- **I-1 through I-8** can all run in parallel (no dependencies between them)
- **S-3** (aliases) and **S-5** (reclassification) can run in parallel after S-1
- **M-1** (parse) and **M-5** (Obsidian) can run in parallel after S-1
- **Canon remediation** and **scaffold decruft** are convergent but non-blocking (Pass 7 §I)

### Scaffold Interlocks

The frontmatter standard (S-1) is the **interface contract** between canon and scaffold. Once S-1 lands:
- Scaffold can build `make validate-canon` against the schema
- Scaffold can rebuild `DYN-LATTICE_INDEX.json` from canon frontmatter
- Scaffold can auto-generate the Corpus manifest (replacing hand-maintained 00006)
- Scaffold can implement staleness alerting from `refresh_cadence` fields

Neither layer needs to wait for the other. The frontmatter schema is the handshake.

---

## I. The Sovereign's Decision Points

Every open question from Passes 5-8 that requires sovereign taste-gating. These cannot be resolved by agents — they require the Sovereign's judgment.

### Architectural Decisions

| # | Question | Options | Pass | Impact |
|---|---|---|---|---|
| **D-1** | **Intelligence decomposition** | Option 1: Lattice substrate (architecturally correct, constitutional surgery). Option 2: Chain with sub-domains (pragmatic, manages contradiction). Option 3: Dissolve and distribute (honest, destructive). | Pass 5 §B | High — determines whether there are 5 or 6 chains |
| **D-2** | **Is Intelligence a thing you develop, or a medium you develop through?** | If the former → Option 2. If the latter → Option 1. If both → Option 2 now, Option 1 later. | Pass 5 §B | Core identity question |
| **D-3** | **Confirm the celestial schema** | Volatility as sole tier axis. Celestial types with semantic meaning. The revised tier taxonomy. | Pass 5 §C | Determines all downstream numbering |
| **D-4** | **Confirm the 6-category structure** | Constitution, Architecture, Practice, Operations, Reference, Archive — or revise/replace. | Pass 5 §C (sensing report) | Determines organizational coherence |
| **D-5** | **Numbering scheme** | Option A: 6-digit TCCNNN (clean but requires renaming). Option B: Keep 5-digit + frontmatter fields (pragmatic). | Pass 7 §A | Low-urgency — frontmatter fields work regardless |

### Taste-Gating Decisions

| # | Question | Pass |
|---|---|---|
| **T-1** | **Neologism approvals** — 86 canonical names proposed (6 new neologisms: Genesis, Chronicle, Crucible, Threshold, Ontograph, Anthromachina). Approve, revise, or replace each. | Pass 7 §B |
| **T-2** | **Demotion list** — 30410-30450 (textbook imports), 34120 (Syllabus), 31150 (auto-generated), 33111 (incomplete), 30450 (dated snapshot). Approve each individually. | Pass 7 §G |
| **T-3** | **13 reclassification candidates** — files to move between volatility tiers. Each is a separate decision. | Pass 5 §C |
| **T-4** | **Auto-generated files policy** — should 31150 and 00006 be treated differently from authored canon? | Pass 7 §G |
| **T-5** | **Corpus manifest fate** — auto-generate (kill 00006 as hand-maintained) or hand-maintain (keep updating manually)? | Pass 7 §F |
| **T-6** | **Immune system integration approach** — connect gates and death protocols to the graph via 00011 (Artifact Protocol) references? | Pass 6 §D |

### Syncrescript Direction

| # | Question | Pass |
|---|---|---|
| **V-1** | **Compression target** — is ~120K tokens (full canon compressed) the right target for the Compiled view? | Pass 8 §C |
| **V-2** | **Tier-variable compression ratios** — cosmos at 2x through asteroid at 5-6x. Approve the ratio table. | Pass 8 §D |
| **V-3** | **Compiler architecture** — 5-stage pipeline (Parse → Validate → Graph → Compress → Verify). Approve or revise. | Pass 8 §D |
| **V-4** | **View priority** — which of the five views should be built first? Scripture (source) exists. Config (make configs) partially exists. Graph/Ledger/Compiled are new. | Pass 8 §C |
| **V-5** | **SN formal grammar** — should Syncrescript v2 have a formal BNF grammar, or continue with the current convention-based block format? | Pass 8 §B |

---

## J. Success Criteria

### Measurable Metrics

| Metric | Current State | Target | How to Measure |
|---|---|---|---|
| **Metadata consistency** | 59% complete frontmatter (5 bare files, 27 missing `operational_status` context, inconsistent fields) | 100% of files have complete, non-contradicting frontmatter per Pass 7 §D schema | `make validate-canon` returns zero E001-E007 errors |
| **Volatility alignment** | 75% correct (22 of 88 files misplaced per Pass 5) | 95%+ correct (allow margin for borderline cases) | Each file's `volatility_band` matches its assessed content shelf-life |
| **Graph coherence** | 5 orphans, 47 false sibling edges, 23 inverted parent-child edges, immune system severed | Zero orphans, zero false edges, immune system connected | `make validate-canon` reports zero E006 (orphan) errors; dependency_graph.json has no disconnected components |
| **Version consistency** | 3+ files with YAML/body version mismatch, batch-updated 2.0.0 everywhere | Single version source (YAML only), no body-inline versions | Zero W001 warnings from validator |
| **Cost consistency** | 3 files disagree on constellation cost | One figure, one file of record, others reference it | Grep for dollar amounts — all point to single source |
| **Compilation target** | Current SN: ~2,600 lines from 12 sampled files (74% compression). Full canon: ~50,000 lines. | Full SN: ≤17,000 lines (~120K tokens). Fits in 200K context window with room for conversation. | `wc -l canon/sn/*.sn.md` after compilation |
| **AI readability** | Average 8.3/10 across 12 sampled files, minimum 6/10 (Acumen) | Average ≥8.5/10, minimum ≥7.5/10 (no file below 7.5) | Stage 5 verification: reconstruction fidelity test |
| **Canon delta per session** | CC40-CC41: zero canon delta (the stop condition trigger) | ≥1 meaningful canon change per active session | Tracked in session state brief |
| **Punchlist clearance** | 10 items (Pass 7 §F) | Zero items | All 10 resolved |

### The Stop Condition (Inherited from CC36)

> Two consecutive zero canon_delta sessions = means-ends inversion halt.

The remediation itself must produce canon changes. If two consecutive sessions produce only scaffold/remediation artifacts without touching the canon source files, the remediation has become its own purpose. Halt and redirect to content creation.

---

*Response generated by Commander (Claude Opus 4.6). Pass 8: Syncrescript Vision + Ratification. CC42 Canon Remediation.*
