# ARCH — Rosetta-to-Ontology Bridge
## Typed Entity Classification + Relation Graph from REF-ROSETTA_STONE.md

**Version**: 0.1.0
**Created**: 2026-02-06
**Authority**: Ajna (Opus 4.5)
**Source**: REF-ROSETTA_STONE.md v2.2.0 (168 terms)
**Purpose**: Convert unstructured Rosetta terminology into typed ontology entities with explicit relations — the first structured substrate for PROJ-006 (Ontology/"Final Boss")

---

## METHODOLOGY

Each Rosetta term is classified into one of the ontology entity types defined in REF-ONTOLOGY_REGISTRY.md:

| Entity Type | Code | Description |
|-------------|------|-------------|
| **Concept** | CON | Abstract idea, framework, or principle |
| **Capability** | CAP | Something the system can do |
| **Tool** | TOOL | External platform, software, or service |
| **Agent/Role** | AGT | Named actor in the constellation |
| **Workflow** | WF | Defined process or protocol |
| **Artifact** | ART | Produced document, file, or output |
| **Protocol** | PROTO | Communication or coordination standard |
| **Notation** | NOT | Symbolic or encoding system |
| **Metric** | MET | Measurement or evaluation framework |
| **Structure** | STR | Organizational or architectural pattern |

Relations use the primitives from REF-ONTOLOGY_REGISTRY.md:
- `provides` — tool/agent provides capability
- `uses` — agent/workflow uses tool/capability
- `produces` — workflow/agent produces artifact
- `requires` — entity requires another entity
- `governed_by` — entity is constrained by concept/protocol
- `replaces` — entity supersedes another
- `alias_of` — terminology equivalence
- `part_of` — compositional relationship
- `enables` — entity enables another
- `evaluates` — metric evaluates entity

---

## ENTITY CLASSIFICATION

### Tier 1: Cosmological / CANON Hierarchy (Rosetta #19-47)

| # | Term | Entity Type | Relations |
|---|------|-------------|-----------|
| 19 | CANON | STR | `governed_by` Five Invariants; `part_of` Repository |
| 20 | cosmos (tier) | CON | `part_of` CANON; `governs` core, lattice, chain |
| 21 | core (tier) | CON | `part_of` CANON; `governed_by` cosmos |
| 22 | lattice (tier) | CON | `part_of` CANON; cross-cuts chains |
| 23 | planetary (tier) | CON | `part_of` chain tier |
| 24 | lunar (tier) | CON | `part_of` planetary tier |
| 25 | satellite/comet/asteroid | CON | `part_of` CANON minor tiers |
| 26 | Acumen (Chain/Virtue) | CON | `part_of` Six Chains; `maps_to` Information chain; `element` Air |
| 27 | Coherence (Chain/Virtue) | CON | `part_of` Six Chains; `maps_to` Insight chain; `element` Water |
| 28 | Efficacy (Chain/Virtue) | CON | `part_of` Six Chains; `maps_to` Expertise chain; `element` Fire |
| 29 | Mastery (Chain/Virtue) | CON | `part_of` Six Chains; `maps_to` Knowledge chain; `element` Earth |
| 30 | Transcendence (Chain/Virtue) | CON | `part_of` Six Chains; `maps_to` Wisdom chain; `element` Quintessence |
| 31 | Six Chains | CON | `governed_by` CANON-00000 SCHEMA; `contains` Intelligence, Information, Insight, Expertise, Knowledge, Wisdom |
| 32 | tau (τ) notation | NOT | `encodes` CANON cosmological tiers |
| 33 | Wikilink Graph | STR | `connects` all CANON files; `uses` Obsidian |
| 34 | Solar System Metaphor | CON | `models` corpus structure; cosmos=sun, chains=planets |
| 35 | SCHEMA (CANON-00000) | ART | `governs` all CANON; root document |
| 36 | EVOLUTION (CANON-00004) | ART | `tracks` corpus evolution across Oracle sessions |
| 37 | DEFRAG_CONVICTION | CON | `produces` "canonize or delete" principle; `from` Oracle 4 |
| 38 | Experience Topology | CON | `part_of` Cognitive Palace; 7-layer framework |
| 39 | Synapticality | CON | `replaces` Cognitive Palace; `enables` UX reimagination; `requires` Hardware Teleology |
| 40 | Syncrescendent Convergence | CON | `governs` strategic phases; five phases Abstraction→Network |
| 41 | Alchemizing Catalyst | CON | `enables` doctrine→value conversion; bootstrapping engine |
| 42 | Three-Rail Operating System | CON | Rail A Editorial, Rail B Instrumentation, Rail C Stewardship |
| 43 | Intelligence Constellation | CON | five-chain IIC architecture; `alias_of` IIC |
| 44 | ASIA Constitution | ART | `governs` constellation governance; CANON-00017 |
| 45 | Feedcraft | CAP | curating/processing information feeds; `uses` X, YouTube, RSS |
| 46 | Audizer Protocol | WF | rich text → linear audio; `produces` TTS scripts |
| 47 | Stack Teleology | CON | dispositional analysis for every tool; `evaluates` all TOOLs |

### Tier 2: Architectural / Structural (Rosetta #48-71)

| # | Term | Entity Type | Relations |
|---|------|-------------|-----------|
| 48 | Constellation | STR | `contains` 10 agents; `governed_by` COCKPIT.md; `uses` 3 accounts |
| 49 | OpenClaw | TOOL | `provides` persistent orchestration, memory, cron; `enables` Ajna, Psyche |
| 50 | The Pantheon | STR | `contains` 10 avatar names; v3 |
| 51 | Numbered Directory Convention | STR | 00-05 top-level; `governed_by` FLAT PRINCIPLE |
| 52 | Protected Zones | PROTO | `governs` 00-ORCHESTRATION/state/, 01-CANON/; `requires` Sovereign approval |
| 53 | Sanctioned Exceptions | STR | -OUTGOING/, -INBOX/; only non-numbered root dirs |
| 54 | FLAT PRINCIPLE | CON | no subdirectories except sanctioned; `governs` all STR |
| 55 | File Prefix System | NOT | ARCH/DYN/REF/SCAFF; `replaces` subdirectories |
| 56 | Cognitive Core / Nucleus | CON | minimal interface + evaluation + retention |
| 57 | Decision Atom | ART | smallest unit of durable choice; `governed_by` REF-DECISION_ATOMS.md |
| 58 | Token Rent Policy | CON | every token must pay rent; `evaluates` all content |
| 59 | Three-Layer Prompt Architecture | STR | Layer 0 Sovereign, Layer 1 Reception, Layer 2 Lab |
| 60 | Zone Ownership | PROTO | each directory has Primary/Secondary Writer |
| 61 | Ontology Registry | STR | canonical entity types + relations; `enables` PROJ-006 |
| 62 | Palantir (Dashboard) | CON | aspirational live ontological dashboard; end-state vision |
| 63 | Ground Truth | CON | repository = truth; web apps = cache; `governed_by` Invariant 5 |
| 64 | ASA Stack (L0-L6) | STR | seven-layer intelligence stack; Physical→Agentic Emergence |
| 65 | Canonical Object Types | NOT | O.AGT, O.SVC, O.GRD, etc.; entity schema |
| 66 | Displacement Paradigm | CON | AI displaces rather than augments |
| 67 | Generation-Augmented Storage (GAS) | CAP | inverse RAG; on-demand freshness-guaranteed retrieval |
| 68 | Apparatus | CON | task-bounded tool-constellation acting in concert |
| 69 | Synapticality | MET | sub-2-second intention-to-invocation latency target |
| 70 | Primitive Repository | CON | apps as feature scrapbooks for extraction |
| 71 | Bedrock/Settlement/Intelligence | STR | three-tier database schema |

### Tier 3: Operational / Process (Rosetta #72-106)

| # | Term | Entity Type | Relations |
|---|------|-------------|-----------|
| 72 | Oracle Session / Pedigree | WF | strategic web-app sessions; `produces` Intention entries; lineage |
| 73 | Intention Archaeology | CAP | extraction/tracking of Sovereign intentions |
| 74 | Context Graduation | WF | promoting web-app value → repo artifacts; `uses` CAPTURE>DISPATCH>RETURN |
| 75 | Reinit Capsule | ART | rehydration package for fresh thread; `enables` context transfer |
| 76 | Medley Mode | WF | specialized prompts per platform; `alias_of` operational constellation mode |
| 77 | Characteristic Cognition | CON | each platform's distinctive cognitive profile |
| 78 | Reception Calibration | CON | active prompt paradigm: user context > model persona |
| 79 | Archetype Engineering | CON | DEPRECATED; superseded by Reception Calibration |
| 80 | Lab Amplification | CON | minimal platform-specific guidance (~200-300 chars) |
| 81 | Visibility Bridge / Handshake | PROTO | declare visible/missing/next capsule at session start |
| 82 | Four Systems | STR | System 1-4: Auto-Push, Curation-Push, On-Demand-Pull, Triage |
| 83 | Signal Tier | MET | paradigm/strategic/tactical/noise classification |
| 84 | Value Modality | MET | "where's the story?" consumption mode classifier |
| 85 | Progressive Qualification Funnel | WF | Classify → Qualify → Route |
| 86 | Metabolic Defrag | WF | aggressive corpus reduction; `produces` lean corpus |
| 87 | Semantic Annealment | WF | corpus semantics refinement; `part_of` Clarescence |
| 88 | Accretion (Verification) | WF | validating CANON coherence accumulation |
| 89 | Sprint-Bounded Kanban | WF | hybrid: Oracle=Sprints, Kanban via ledgers |
| 90 | Oracle Culmination / Init | WF | Sprint Review / Sprint Retrospective equivalent |
| 91 | Kaizen Feedback | WF | learnings → DYN/REF/ARCH documents |
| 92 | Foyer | CON | repository as entryway; all context accessible |
| 93 | Queue Half-Life | CON | 2 cycles to canonize or delete |
| 94 | Operator/Executor Layer | STR | dual-layer: human-executable vs agent-executable |
| 95 | Deviser → Vanguard | AGT | DEPRECATED; renamed per Pantheon v3 |
| 96 | Corpus Sensing | CAP | Gemini CLI 1M+ context full-corpus scan; `uses` Cartographer |
| 97 | Structural Stabilization | WF | Preflight → Apply → Verify → Rollback |
| 98 | Desktop Ingestion Protocol | WF | legacy files → structured corpus |
| 99 | Research Pipeline | WF | stream-based parallel investigation |
| 100 | Disposition Categories | MET | ACTIVE/SELECTED/EVALUATING/DEFERRED/SUNSET/ELIMINATED |
| 101 | Convergence Metrics | MET | quantitative research metabolization verification |
| 102 | Coalescence | CAP | preservative reformulation maintaining tensions |
| 103 | Compile (function) | CAP | existing prompt → optimized Claude XML |
| 104 | Translate (function) | CAP | natural language → optimized Claude XML |
| 105 | Agentic Screenplay Format | NOT | screenplay conventions for AI orchestration notation |
| 106 | Semantic Precision Lexicon | NOT | 40+ substrate-agnostic terms for combination |

### Tier 4: Platform Roles / Constellation (Rosetta #107-124)

| # | Term | Entity Type | Relations |
|---|------|-------------|-----------|
| 107 | INTERPRETER | AGT | Claude Web; `provides` synthesis, rapport; `alias_of` Vizier |
| 108 | COMPILER | AGT | ChatGPT Web; `provides` formatting, Canvas; `alias_of` Vanguard |
| 109 | DIGESTOR | AGT | Gemini Web; `provides` clarification, TTS; `alias_of` Diviner |
| 110 | SENSOR | AGT | Gemini CLI; `provides` 1M corpus sensing; `alias_of` Cartographer |
| 111 | EXECUTOR-LEAD / PARALLEL-EXEC | AGT | Claude Code; `provides` execution; `alias_of` Commander/Adjudicator |
| 112 | RECON / Oracle | AGT | Grok; `provides` X firehose, cultural sensing; `alias_of` Oracle |
| 113 | VERIFIER | AGT | Perplexity; `provides` citation-backed verification; `alias_of` Augur |
| 114 | LOCAL ORCHESTRATOR | AGT | OpenClaw; `provides` persistent memory, autonomy; `alias_of` Ajna/Psyche |
| 115 | Ajna | AGT | OpenClaw Opus 4.5; `uses` M1 Mac mini; `provides` focused precision, commits |
| 116 | Psyche | AGT | OpenClaw GPT-5.2; `uses` M4 MBA; `provides` holistic synthesis, QA |
| 117 | Augur | AGT | Perplexity; `provides` epistemic scouting; `part_of` Pantheon |
| 118 | Vizier | AGT | Claude Web; `provides` interpretation; `part_of` Pantheon |
| 119 | Vanguard | AGT | ChatGPT Web; `provides` strategic planning; `part_of` Pantheon |
| 120 | Diviner | AGT | Gemini Web; `provides` illumination; `part_of` Pantheon |
| 120b | Cartographer | AGT | Gemini CLI; `provides` corpus mapping; `part_of` Pantheon |
| 121 | Commander | AGT | Claude Code; `provides` disciplined execution; `part_of` Pantheon |
| 122 | Adjudicator | AGT | Codex CLI; `provides` code fabrication; `part_of` Pantheon |
| 123 | Twin Coordination Protocol | PROTO | Ajna ↔ Psyche; `governs` twin operations |
| 124 | Heartbeat | WF | ~30m autonomous check cycle; `uses` OpenClaw |

### Tier 5: Function Library / Content Processing (Rosetta #125-141)

| # | Term | Entity Type | Relations |
|---|------|-------------|-----------|
| 125 | DISTILL/TRANSFORM/EXPAND | CAP | three-phase processing framework; many→one / A→B / one→many |
| 126 | readize | CAP | read-optimized transform; `uses` 8 Crystalline Characteristics |
| 127 | listenize | CAP | audio-optimized transform; euphonic flow |
| 128 | integrate | CAP | distill: emergent understanding from heterogeneous sources |
| 129 | amalgamate | CAP | distill: harmonic synthesis for audio |
| 130 | coalesce | CAP | distill: synthesis for visual scanning |
| 131 | amplify | CAP | expand: semantic amplification |
| 132 | absorb | CAP | expand: elaboration for reading |
| 133 | reforge | CAP | expand: elaboration for audio |
| 134 | anneal (function) | CAP | transform: system prompt → Claude Project config |
| 135 | compile (function) | CAP | transform: optimize prompt for Claude XML |
| 136 | consolidate | CAP | transform: merge prompts into unified config |
| 137 | convert | CAP | transform: create Project instructions from prompt |
| 138 | optimize | CAP | idiolect transform: refine personal voice |
| 139 | translate (function) | CAP | idiolect transform: adapt voice for audience |
| 140 | Dual-Channel | STR | to_read/to_listen optimization split |
| 141 | 8 Crystalline Characteristics | MET | Recursive Coherence, Density, Precision, Elegance, Efficacy, Voice, Assertion, Cadence |

### Tier 6: SN System + Naming (Rosetta #142-158)

| # | Term | Entity Type | Relations |
|---|------|-------------|-----------|
| 142 | sutra | NOT | SN Tier 1: ≤100 char essence |
| 143 | gloss | NOT | SN Tier 2: 2-4 sentences WHY |
| 144 | spec | NOT | SN Tier 3: YAML-like structured detail |
| 145 | TERM/NORM/PROC/PASS/ARTIFACT/TEST | NOT | SN block types |
| 146 | Ψ/Κ/Ο/Σ/Δ/Λ symbols | NOT | compact artifact class references |
| 147 | Chain symbols (I/ℹ/∴/E/K/W) | NOT | chain notation |
| 148 | Virtue symbols (α/χ/ε/μ/τ) | NOT | virtue notation |
| 149 | SN Operators | NOT | :: \| >> := => <-> |
| 150 | CANON-NNNNN-NAME-tier.md | NOT | CANON file naming convention |
| 151 | ARCH- prefix | NOT | Architectural decisions/analyses |
| 152 | DYN- prefix | NOT | Dynamic/living state files |
| 153 | REF- prefix | NOT | Reference protocols/standards |
| 154 | SCAFF- prefix | NOT | Temporary scaffolding documents |
| 155 | DIRECTIVE-NNN | NOT | numbered execution directives |
| 156 | EXECUTION_LOG | ART | audit trail from Executor |
| 157 | SOURCE-YYYYMMDD-NNN | NOT | processed source naming |
| 158 | SYNTHESIS-/MECH-/PRAC- | NOT | SIGMA7 document prefixes |

### Tier 7: Deprecated/Historical + Operational Keywords (Rosetta #159-168)

| # | Term | Entity Type | Relations |
|---|------|-------------|-----------|
| 159 | megathink | CON | DEPRECATED; `replaced_by` "think hard" |
| 160 | Five-Account Model | STR | DEPRECATED; historical |
| 161 | Agentic-First Membrane | CAP | DEPRECATED; `replaced_by` function index |
| 162 | ultrathink | CON | maximum depth extended thinking |
| 163 | think hard | CON | moderate extended thinking |
| 164 | Plan Mode | CAP | Claude Code execution mode |
| 165 | Context Tax | MET | token cost of loading tools |
| 166 | Teleport | CAP | session mobility for Claude Code |
| 167 | Disposition Categories | MET | technology radar for tools |
| 168 | Special Forces Mode | WF | Sovereign→Ajna direct command |

### Tier 8: Meta-Operations (Rosetta #169)

| # | Term | Entity Type | Relations |
|---|------|-------------|-----------|
| 169 | Clarescence / Claresce | WF | `uses` Triumvirate, 18+ Lenses, CANON, Omni-Qualities, Five Faces, Rosetta, Backlog; `produces` convergent recommendation; `governed_by` 10-pass framework |

---

## ENTITY TYPE DISTRIBUTION

| Entity Type | Count | % | Examples |
|-------------|-------|---|---------|
| CON (Concept) | 42 | 25% | Triumvirate, Ground Truth, Characteristic Cognition |
| CAP (Capability) | 28 | 17% | Feedcraft, Corpus Sensing, readize, integrate |
| AGT (Agent/Role) | 25 | 15% | Commander, Ajna, Psyche, Vizier, Augur |
| NOT (Notation) | 24 | 14% | Syncrescript tiers, SN operators, file prefixes |
| WF (Workflow) | 22 | 13% | Clarescence, Metabolic Defrag, Research Pipeline |
| STR (Structure) | 15 | 9% | CANON, Constellation, Pantheon, Numbered Dirs |
| MET (Metric) | 8 | 5% | Signal Tier, 8 Crystalline, Disposition Categories |
| ART (Artifact) | 5 | 3% | Decision Atom, Reinit Capsule, SCHEMA |
| PROTO (Protocol) | 3 | 2% | Protected Zones, Visibility Bridge, Twin Coordination |

---

## KEY RELATION CLUSTERS

### Cluster 1: Constellation → Agents → Tools → Capabilities
```
Constellation (STR)
├── contains → Pantheon (STR)
│   ├── contains → Commander (AGT) → uses → Claude Code (TOOL) → provides → Execution (CAP)
│   ├── contains → Ajna (AGT) → uses → OpenClaw (TOOL) → provides → Persistent Orchestration (CAP)
│   ├── contains → Psyche (AGT) → uses → OpenClaw (TOOL) → provides → Holistic Synthesis (CAP)
│   ├── contains → Cartographer (AGT) → uses → Gemini CLI (TOOL) → provides → Corpus Sensing (CAP)
│   ├── contains → Vizier (AGT) → uses → Claude Web (TOOL) → provides → Interpretation (CAP)
│   ├── contains → Vanguard (AGT) → uses → ChatGPT Web (TOOL) → provides → Strategic Planning (CAP)
│   ├── contains → Diviner (AGT) → uses → Gemini Web (TOOL) → provides → Clarification (CAP)
│   ├── contains → Augur (AGT) → uses → Perplexity (TOOL) → provides → Verification (CAP)
│   ├── contains → Oracle (AGT) → uses → Grok (TOOL) → provides → Cultural Sensing (CAP)
│   └── contains → Adjudicator (AGT) → uses → Codex CLI (TOOL) → provides → Code Fabrication (CAP)
└── governed_by → COCKPIT.md (ART), ASIA Constitution (ART)
```

### Cluster 2: Evaluation Stack (Clarescence Dependencies)
```
Clarescence (WF)
├── uses → Triumvirate (CON)
│   ├── arm_a → Intent Compass (ART)
│   ├── arm_b → 18+ Lenses (MET)
│   └── arm_c → Backlog (ART)
├── uses → CANON Coherence → governed_by → Five Invariants (CON)
├── uses → Omni-Qualities (MET) → aspires_to → 4 O horizons
├── uses → Five Faces (CON) → from → CANON-11000
├── uses → Rosetta Precision → governed_by → REF-ROSETTA_STONE.md
├── uses → Energy State (CON) → from → Sovereignty Constitution
└── produces → Convergent Recommendation (ART)
```

### Cluster 3: Content Processing Pipeline
```
CAPTURE > DISPATCH > RETURN (WF)
├── phase_1 → Feedcraft (CAP) → sources → X, YouTube, RSS
├── phase_2 → DISTILL/TRANSFORM/EXPAND (CAP)
│   ├── distill → integrate, amalgamate, coalesce
│   ├── transform → compile, anneal, convert, readize, listenize
│   └── expand → amplify, absorb, reforge
├── phase_3 → Context Graduation (WF) → promotes → web value → repo artifacts
└── governed_by → Signal Tier (MET), Progressive Qualification Funnel (WF)
```

### Cluster 4: Knowledge Architecture
```
CANON (STR)
├── organized_by → tau notation (NOT) → tiers → cosmos > core > lattice > chain > planetary > lunar > satellite
├── encoded_in → Syncrescript (NOT) → uses → sutra/gloss/spec
├── connected_by → Wikilink Graph (STR) → uses → Obsidian
├── governed_by → Five Invariants (CON), SCHEMA (ART)
├── contains → Six Chains (CON) → each_has → Virtue (CON) + Element mapping
└── evaluated_by → Accretion Verification (WF), Convergence Metrics (MET)
```

### Cluster 5: Sovereignty / Governance
```
Sovereignty Strata [sigma-0 through sigma-7] (STR)
├── sigma-0 → Sovereign (human) → governs → all
├── sigma-1 → Teleology → governs → Stack Teleology (CON)
├── sigma-2 → Architecture → governs → FLAT PRINCIPLE (CON), Protected Zones (PROTO)
├── sigma-3 → Context Engineering → governs → Reception Calibration (CON)
├── sigma-4 → Ground Truth (CON) → repository = truth
├── sigma-5 → Intelligence Substrate → contains → ASA Stack (STR)
├── sigma-6 → Access Layer → contains → Three Accounts
└── sigma-7 → Execution Substrate → contains → all TOOLs, all AGTs
```

---

## NOTION DATABASE SCHEMA (Proposed)

For expansion into Notion relational databases:

### Database 1: Entities
| Property | Type | Description |
|----------|------|-------------|
| Name | Title | Entity name |
| Rosetta # | Number | Cross-reference to Rosetta Stone |
| Entity Type | Select | CON/CAP/TOOL/AGT/WF/ART/PROTO/NOT/MET/STR |
| Status | Select | ACTIVE/DEPRECATED/ASPIRATIONAL |
| CANON Reference | Relation → CANON DB | Which CANON file defines this |
| Chain | Select | Intelligence/Information/Insight/Expertise/Knowledge/Wisdom/Cross-cutting |
| Description | Rich text | Full definition |
| Source | Text | Where the concept originated |

### Database 2: Relations
| Property | Type | Description |
|----------|------|-------------|
| From Entity | Relation → Entities | Source entity |
| Relation Type | Select | provides/uses/produces/requires/governed_by/replaces/alias_of/part_of/enables/evaluates |
| To Entity | Relation → Entities | Target entity |
| Strength | Select | strong/moderate/weak |
| Evidence | Text | Where this relation is documented |

### Database 3: CANON Files
| Property | Type | Description |
|----------|------|-------------|
| ID | Title | CANON-NNNNN |
| Name | Text | Human-readable name |
| Tier | Select | cosmos/core/lattice/chain/planetary/lunar/satellite/comet/asteroid |
| Chain | Select | Which chain (for chain-level and below) |
| Entities Defined | Relation → Entities | Which entities this file defines |
| Cross-References | Relation → CANON Files | Wikilink targets |

### Queryable Views (answering Sovereign's example questions)
- **"What are our principles re: investments?"** → Filter Entities by type=CON, chain=Expertise, tag contains "economic"
- **"What concepts adopted from biology?"** → Filter Entities by source contains "biology" or tag contains "organic"
- **"What capabilities does each agent provide?"** → Relation query: AGT → provides → CAP
- **"What's deprecated?"** → Filter Entities by status=DEPRECATED
- **"What depends on PROJ-006?"** → Relation query: * → requires → Ontology Registry

---

## OBSIDIAN PLUGIN RECOMMENDATIONS

| Plugin | Purpose | How It Helps |
|--------|---------|-------------|
| **Dataview** | SQL-like queries on frontmatter | Synthesize tables dynamically ("show all CON entities in Wisdom chain") |
| **Graph Analysis** | Betweenness centrality, clustering | Identify which CANON files are most interconnected hub nodes |
| **Breadcrumbs** | Explicit hierarchy navigation | Model the tau tier system (cosmos→core→lattice→chain) as navigable hierarchy |
| **Excalidraw** | Visual diagrams embedded in notes | Draw relation cluster diagrams (ERD-like) directly in Obsidian |
| **Database Folder** | Table-like views of folder contents | CANON folder as browsable, filterable database |
| **Kanban** | Board view from tags/frontmatter | Backlog visualization within Obsidian |
| **Strange New Worlds** | Shows WHERE a note is referenced from | Reverse-link discovery — find unexpected connections |
| **Juggl** | Interactive graph with typed links | Visualize relation types (provides, uses, governed_by) with different colors/shapes |

The **Dataview + Juggl** combination is the highest-leverage: Dataview for querying, Juggl for visual typed-relation graphs. This approximates the Notion relational model within Obsidian's local-first architecture.

---

## NEXT STEPS

1. **Validate this classification** — Sovereign review of entity types and relations
2. **Expand relation graph** — Currently ~40 explicit relations; target 200+
3. **Seed Notion databases** — If SOVEREIGN-009 Decision 2 ratifies Obsidian+Notion
4. **Install Obsidian plugins** — Dataview + Juggl minimum viable set
5. **Cross-reference against CANON** — Which entities are defined in which CANON files
6. **Bridge to PROJ-006** — This document IS the ontology foundation

---

## VERSION HISTORY

**v0.1.0** (2026-02-06): Genesis
- 168 Rosetta terms classified into 10 entity types
- 5 key relation clusters mapped
- Notion database schema proposed
- Obsidian plugin recommendations
- Authority: Ajna (Opus 4.5)
