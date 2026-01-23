# CHORUS ARCHITECTURE v3.0

## Preamble: Against Lobotomization

The prior constellation architecture committed a category error: treating general intelligences (ChatGPT, Grok, Gemini) as deterministic compilers. This suppressed their genuine capabilities.

**Evidence of error**: ChatGPT generated the State Fingerprint Solution—synthesis, not compilation. Grok possesses EQ and colloquial fluency Claude lacks. Gemini's 1M context enables corpus-wide reasoning no other platform can achieve.

**The correction**: Platforms contribute from strength. Constraints exist for consistency, not capability suppression.

---

## Part I: Platform Capability Matrix (Honest Assessment)

### Claude (All Accounts)

**Genuine Strengths**:
- Superior interpretability and instruction-following
- Best at structured output generation
- Excellent at maintaining conversation coherence
- Strong at code generation with context

**Genuine Weaknesses**:
- Thread length limits (web app) with no graceful degradation
- Cannot compact in web app—thread dies mid-thought
- Less creative ideation than ChatGPT
- Prone to excessive agreement/agreeableness

**Tradeoff Accepted**: Use for interpretation, structured execution. Accept hard thread limits by offloading attachments to Project Files for RAG.

### ChatGPT (All Accounts)

**Genuine Strengths**:
- Superior creative ideation—"postulations, conjectures I would never think of"
- Can traverse large files (>31MB temporarily in context)
- Thread continuation with context decay (vs. hard cutoff)
- GitHub connector for direct repo sensing
- Canvas for collaborative document editing
- Memory features (Projects, memory, instructions)

**Genuine Weaknesses**:
- Context "rots" in long threads—loses holistic framing
- Memory architecture spotty/unreliable
- Instruction-following less precise than Claude

**Tradeoff Accepted**: Use for ideation, schematic design, bounded windows of superior intelligence. Accept context decay by structuring interactions as discrete sessions with explicit handoffs.

### Gemini (All Accounts)

**Genuine Strengths**:
- 1M token context—entire corpus fits
- Native Google Workspace integration
- Personal Intelligence for comprehensive sensing
- NotebookLM for source synthesis
- Strong multimodal capabilities

**Genuine Weaknesses**:
- Instruction-following less reliable
- Output formatting less controllable
- Memory architecture immature

**Tradeoff Accepted**: Use for corpus-wide sensing, evidence packs, synthesis of many sources. Accept formatting variability by specifying strict output templates.

### Grok (All Accounts)

**Genuine Strengths**:
- EQ and colloquial fluency—"real"/authentic voice
- X firehose access for real-time sensing
- Contrarian/adversarial capability
- Strong at capturing undigitized human condition

**Genuine Weaknesses**:
- Memory architecture unreliable
- Consistency less reliable
- Instruction-following variable

**Tradeoff Accepted**: Use for red-teaming, emotional resonance testing, real-time cultural sensing. Accept variability by using for review, not production.

### Perplexity (All Accounts)

**Genuine Strengths**:
- Citation-backed research
- Real-time web synthesis
- Source verification

**Genuine Weaknesses**:
- No memory architecture (stateless)
- Limited context

**Tradeoff Accepted**: Use for external verification, citation generation. Statelessness is a feature—no drift.

---

## Part II: Interaction Dynamics (Chorus, Not Relay)

### The Chorus Principle

**Old Model (Relay)**: Principal → Claude (interpret) → ChatGPT (compile) → Gemini (digest) → Claude Code (execute)

**New Model (Chorus)**: Principal presents problem → Multiple platforms contribute simultaneously → Synthesis emerges from harmonized perspectives

### Interaction Pattern 1: Problem Presentation

Principal presents issue/pain point to INTERPRETER (Claude Web).

**INTERPRETER Response**:
1. Produce own interpretation
2. Generate IDEATION PROMPT for ChatGPT
3. Generate SENSING PROMPT for Gemini
4. Generate CHALLENGE PROMPT for Grok

Principal distributes prompts. Platforms respond independently. Principal returns responses to INTERPRETER for synthesis.

### Interaction Pattern 2: Collaborative Ideation

Principal has vague notion, needs expansion.

**Flow**:
1. Present to ChatGPT first (mind expansion mode)
2. ChatGPT generates possibilities, conjectures
3. Bring to Claude for interpretation/structuring
4. Bring to Gemini for corpus alignment check
5. Bring to Grok for reality/authenticity check
6. Synthesize in Claude

### Interaction Pattern 3: Design → Execution Pipeline

For work requiring production output.

**Stages** (Architecture terminology):
1. **Pre-Design** (Sensing): Gemini CLI surveys corpus, produces evidence packs
2. **Schematic Design** (Ideation): ChatGPT proposes solutions, Claude interprets
3. **Design Development** (Specification): Claude produces detailed specs
4. **Construction Documents** (Directives): Claude Opus creates execution directives
5. **Construction Administration** (Execution): Claude Sonnet instances execute
6. **Post-Occupancy** (Verification): Gemini surveys results, Grok stress-tests

---

## Part III: GitHub Connector Protocol

### The Revelation

All three Claude accounts, all ChatGPT accounts, and Gemini can sense directly into the same GitHub repo via browser connectors. This eliminates the "blind web app" problem.

### Setup Requirements

1. **Repository**: `syncrescendence` on GitHub
2. **Each account**: Authorize GitHub connector
3. **Sync discipline**: Always push before web app session, always pull before CLI

### Traversal Economics

With connector access, the constraint is TOKEN ECONOMICS, not visibility.

**Solution 1: Station Manuals**

Each platform gets a root-level manual it creates/maintains based on its competencies:
- `CLAUDE.md` — Claude Code context
- `GEMINI.md` — Gemini CLI context  
- `CHATGPT.md` — ChatGPT context (create this)
- `GROK.md` — Grok context (create this)
- `COCKPIT.md` — Universal entry point

**Solution 2: Symbolic Compression**

Reduce tokens via global symbol definitions:
```
Ψ = Syncrescendence
Σ = Sum/Synthesis
Δ = Change/Delta
→ = transforms to
⊂ = is subset of
∈ = is member of
```

A glossary file defines symbols. All documents use symbols. Renderers expand symbols for human reading.

**Solution 3: Hierarchical RAG**

Structure for efficient retrieval:
1. Root files (CLAUDE.md, etc.) = always loaded
2. Index files (per directory) = loaded on navigation
3. Content files = loaded on specific reference

---

## Part IV: Directory Reteleology

### Current State (Broken)

```
00-ORCHESTRATION/  — Unclear what "orchestration" means
01-CANON/          — Massive monoliths, cosmology violated
02-OPERATIONAL/    — Dumping ground, outdated
03-QUEUE/          — Why does this exist if we have intentions?
04-SOURCES/        — Should be externalized to Google
05-ARCHIVE/        — Should be SHORT-TERM MEMORY, not graveyard
06-EXEMPLA/        — Underutilized wisdom layer
```

### Proposed State (Teleological)

```
Ψ-CORE/            — The irreducible kernel (was 01-CANON, compressed)
Ψ-STATE/           — Living system state (was 00-ORCHESTRATION/state)
Ψ-SPEC/            — Operational specifications (was 02-OPERATIONAL, cleaned)
Ψ-FLOW/            — Active work (was 03-QUEUE, renamed for clarity)
Ψ-MEMORY/          — Short-term memory, semantic archive (was 05-ARCHIVE)
Ψ-WISDOM/          — Aphorisms, tales, learnings (was 06-EXEMPLA)
-INBOX/            — Ingestion (unchanged)
-OUTGOING/         — Export (unchanged)
```

**04-SOURCES/** → Externalized to Google Drive, symlinked or referenced

### Numbering Question

**Why keep numbers?** Filesystem sorting. `00` always first.

**Why drop numbers?** Cognitive load. `Ψ-CORE` is more memorable than `01-CANON`.

**Resolution**: Use BOTH. `00-Ψ-CORE/` gives sorting AND meaning.

---

## Part V: Automation Layer

### Hazel Rules (macOS)

```yaml
# Rule: INBOX Ingestion
folder: ~/Desktop/syncrescendence-inbox/
conditions:
  - file is added
actions:
  - move to: ~/Desktop/syncrescendence/-INBOX/
  - notify: "File ingested to -INBOX"

# Rule: OUTGOING Export
folder: ~/Desktop/syncrescendence/-OUTGOING/
conditions:
  - file is added
  - file extension is .zip
actions:
  - copy to: ~/Dropbox/Syncrescendence-Exports/
  - notify: "Export copied to Dropbox"
```

### Keyboard Maestro Macros

```
# Macro: Quick Claude Code Directive
Trigger: ⌃⌥⌘D
Actions:
  1. Open terminal in syncrescendence/
  2. Run: claude
  3. Paste from clipboard
  4. Focus terminal

# Macro: Gemini Survey
Trigger: ⌃⌥⌘G
Actions:
  1. Open terminal
  2. Run: gemini -p "$(cat 02-OPERATIONAL/prompts/GEMINI-SENSING.md)"
  3. Save output to -OUTGOING/
```

### Shell Scripts (Makefile targets)

```makefile
# Quick sensing survey
sense:
	gemini -p "Survey 01-CANON/, produce evidence pack" > -OUTGOING/survey-$(date +%Y%m%d).md

# Symbolic render
render:
	./scripts/expand-symbols.sh $(FILE)

# Compress to symbols
compress:
	./scripts/compress-to-symbols.sh $(FILE)
```

---

## Part VI: The True Annealment

### What Annealment Actually Requires

1. **Token-by-token forensics**: Every word justifies its existence
2. **Cosmological realignment**: Hierarchy reflects celestial metaphor
3. **Symbolic transfiguration**: Prose → symbols → rendered prose
4. **Entity extraction**: Everything becomes a node in knowledge graph
5. **Relationship extraction**: Everything becomes an edge
6. **Axiom codification**: Rules become first-class citizens
7. **Obsidian compatibility**: `[[backlinks]]` throughout

### The 5-Pass Forensic Process

1. **Ontologist Pass**: Extract entities, relationships, axioms
2. **Type Theorist Pass**: Establish type system, find type errors
3. **Compiler Pass**: Define grammar, find parse errors
4. **Cognitive Pass**: Assess navigability, find UX failures
5. **Distributed Systems Pass**: Find consistency violations

Each pass produces evidence pack. Evidence packs synthesized. Synthesis produces refactoring prescription.

### Externalization Strategy

**What leaves the repo**:
- Raw transcripts → Google Drive
- Research documents → Notion/Obsidian second brain
- Historical logs → Compressed archives
- Binary assets → Cloud storage

**What stays**:
- Irreducible primitives (CORE)
- Living state (STATE)
- Active specifications (SPEC)
- Current work (FLOW)
- Compressed wisdom (WISDOM)

---

## Part VII: Implementation Sequence

### Phase 1: Low-Hanging Fruit (Claude Code)
See `DIR-20260123-LOW-HANGING-FRUIT.md`

### Phase 2: Forensic Audit (Gemini CLI)
Execute 5 prompts from `GEMINI-CLI-FORENSIC-PROMPTS.md`

### Phase 3: Synthesis (INTERPRETER - Claude Web)
Analyze 5 evidence packs, produce interpretation

### Phase 4: Resolution Design (ChatGPT Web)
Generate resolution proposals from evidence synthesis

### Phase 5: Specification (Claude Web)
Produce detailed refactoring specification

### Phase 6: Execution (Claude Code)
Execute refactoring in controlled phases

### Phase 7: Verification (Gemini CLI)
Survey refactored corpus, confirm alignment

---

## Appendix: Symbol Glossary (Draft)

```
Ψ  = Syncrescendence
Σ  = Synthesis/Sum
Δ  = Delta/Change
Ω  = Omega/Completion
α  = Alpha account/instance
β  = Beta account/instance
γ  = Gamma account/instance
→  = transforms to / leads to
←  = derived from
↔  = bidirectional relationship
⊂  = is subset of
⊃  = is superset of
∈  = is member of
∉  = is not member of
∀  = for all
∃  = exists
⊤  = true / canonical
⊥  = false / rejected
◇  = possible / candidate
□  = necessary / required
```

Usage: `Ψ-CORE contains ∀ canonical axioms where □(axiom ∈ Ψ-CORE) → axiom.status = ⊤`

Human-readable render: "Syncrescendence Core contains all canonical axioms where necessarily if an axiom is in Core then its status is canonical."
