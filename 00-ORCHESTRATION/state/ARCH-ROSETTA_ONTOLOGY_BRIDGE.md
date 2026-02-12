# ARCH — Rosetta-to-Ontology Bridge
## Typed Entity Classification + Relation Graph from REF-ROSETTA_STONE.md

**Version**: 1.0.0
**Created**: 2026-02-06
**Updated**: 2026-02-05
**Authority**: Ajna (Opus 4.5) → Commander (Claude Code Opus) v1.0 expansion
**Source**: REF-ROSETTA_STONE.md v2.2.0 (168 terms) + 9 new terms from Task Architecture session
**Purpose**: Convert unstructured Rosetta terminology into typed ontology entities with explicit relations — the first structured substrate for PROJ-006 (Ontology/"Final Boss")
**Relation Count**: 200+ (expanded from ~40 in v0.1.0)
**CANON Coverage**: 79 files cross-referenced

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

### Tier 9: Task Architecture + Ontology (Rosetta #170-177, added v1.0)

| # | Term | Entity Type | Relations |
|---|------|-------------|-----------|
| 170 | T1a (Linear) | TOOL | `provides` repo-facing project management; `governed_by` Five-Tier Task Architecture; `uses` GraphQL API |
| 171 | T1b (ClickUp) | TOOL | `provides` life-facing project management; `governed_by` Five-Tier Task Architecture |
| 172 | Five-Tier Task Architecture | STR | `contains` T0, T1a, T1b, T2, T3; `governed_by` ARCH-TASK_TIER_ARCHITECTURE.md; `enables` project tracking |
| 173 | operational_status | MET | `evaluates` CANON files; values: theoretical/partial/operational; `part_of` CANON Frontmatter Schema |
| 174 | CANON Frontmatter Schema | STR | `contains` operational_status, entities_defined, depends_on, last_verified; `enables` Dataview queries; `part_of` Ontology |
| 175 | Ontology Bridge | ART | `connects` Rosetta → typed entities; `enables` PROJ-006; `governed_by` REF-ONTOLOGY_REGISTRY.md |
| 176 | Dataview Query | CAP | `uses` Obsidian Dataview plugin; `queries` CANON Frontmatter; `enables` "Palantir" dashboard |
| 177 | CLI Orchestration Config | STR | `contains` CLAUDE.md, AGENTS.md, GEMINI.md; `governed_by` T1a (Linear); `enables` config parity |

---

## ENTITY TYPE DISTRIBUTION (v1.0)

| Entity Type | Count | % | Examples |
|-------------|-------|---|---------|
| CON (Concept) | 44 | 25% | Triumvirate, Ground Truth, Gaian Field Node, Five-Tier Architecture |
| CAP (Capability) | 30 | 17% | Feedcraft, Corpus Sensing, Dataview Query, readize, integrate |
| AGT (Agent/Role) | 25 | 14% | Commander, Ajna, Psyche, Vizier, Augur |
| NOT (Notation) | 24 | 14% | Syncrescript tiers, SN operators, file prefixes |
| WF (Workflow) | 23 | 13% | Clarescence, Metabolic Defrag, Research Pipeline, Heartbeat |
| STR (Structure) | 17 | 10% | CANON, Constellation, Five-Tier Architecture, CLI Config |
| MET (Metric) | 10 | 6% | Signal Tier, 8 Crystalline, operational_status, Disposition |
| ART (Artifact) | 7 | 4% | Decision Atom, Ontology Bridge, SCHEMA, Reinit Capsule |
| PROTO (Protocol) | 3 | 2% | Protected Zones, Visibility Bridge, Twin Coordination |
| **Total** | **183** | | **177 Rosetta + 6 implicit from CANON cross-ref** |

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

## CANON FILE CROSS-REFERENCE INDEX

Maps each CANON file to the entities it defines and its primary relations. This enables "which CANON file defines X?" queries.

### Cosmos Tier (00xxx)
| CANON ID | Name | Entities Defined | Key Relations |
|----------|------|-----------------|---------------|
| CANON-00000 | SCHEMA | CANON (STR), Six Chains (CON), tau notation (NOT) | `governs` all CANON files |
| CANON-00001 | ORIGIN | Origin Story (CON) | `provides` founding context |
| CANON-00002 | LINEAGE | Oracle Sessions (WF), Pedigree (ART) | `tracks` system evolution |
| CANON-00003 | PRINCIPLES | Five Invariants (CON), DEFRAG_CONVICTION (CON) | `governs` all operations |
| CANON-00004 | EVOLUTION | Corpus Evolution (WF) | `tracks` version history across Oracles |
| CANON-00005 | SYNCRESCENDENCE | Syncrescendent Convergence (CON), Five Phases (CON) | `governs` strategic trajectory |
| CANON-00006 | CORPUS | Corpus Management (WF), Token Rent Policy (CON) | `governs` content lifecycle |
| CANON-00007 | EVALUATION | Evaluation Framework (MET), 8 Crystalline Chars (MET) | `evaluates` all content |
| CANON-00009 | STRATEGY | Three-Rail OS (CON), Alchemizing Catalyst (CON) | `governs` strategic operations |
| CANON-00010 | OPERATIONS | Operational Protocols (PROTO), Zone Ownership (PROTO) | `governs` daily operations |
| CANON-00011 | ARTIFACT_PROTOCOL | Artifact Standards (PROTO), File Prefix System (NOT) | `governs` artifact production |
| CANON-00012 | MODAL_SEQUENCE | Four Modals (CON), Modal Progression (WF) | `governs` 15-year timeline |
| CANON-00013 | QUICKSTART | Onboarding (WF) | `enables` new session initialization |
| CANON-00014 | CONTENT_PROTOCOL | Content Processing (WF), DISTILL/TRANSFORM/EXPAND (CAP) | `governs` content pipeline |
| CANON-00015 | MACROSCOPIC_NARRATIVES | Strategic Narratives (CON) | `provides` framing context |
| CANON-00016 | ONTOLOGICAL_FRAMEWORK | Ontology Framework (CON), 14 Meaning Dimensions (CON) | `enables` PROJ-006 |
| CANON-00017 | AGENTIC_CONSTITUTION | ASIA Constitution (ART), Constellation Governance (PROTO) | `governs` all agents |

### Core Tier (1xxxx)
| CANON ID | Name | Entities Defined | Key Relations |
|----------|------|-----------------|---------------|
| CANON-10000 | CELESTIAL_BODY | Celestial Body (CON), Core Identity (CON) | `defines` central identity |
| CANON-11000 | FACETS | Five Faces (CON): Sensing/Meaning/Intention/Embodiment/Harmony | `evaluates` alignment |

### Lattice Tier (2xxxx)
| CANON ID | Name | Entities Defined | Key Relations |
|----------|------|-----------------|---------------|
| CANON-20000 | PALACE | Cognitive Palace (CON), Experience Topology (CON) | `models` cognitive architecture |
| CANON-20010 | DIM_COORDINATORS | Dimension Coordinators (AGT) | `part_of` Cognitive Palace |
| CANON-20020 | META_SYSTEMS | Meta-Systems (STR) | `part_of` Cognitive Palace |
| CANON-21000 | CHAIN_MATRIX | Chain Matrix (STR), Chain Progression (WF) | `governs` all 6 chains |
| CANON-21100 | TRI_HELIX | Tri-Helix (STR), Three Capacities (CON) | `cross-cuts` chains |
| CANON-22000 | INTERFERENCE | Interference Patterns (CON), Cross-chain Effects (CON) | `modulates` chain interactions |
| CANON-23000 | LUNAR_NAV | Lunar Navigation (WF), Depth Framework (CON) | `governs` lunar-tier work |
| CANON-24000 | OMNI_QUALITY | Omni-Qualities (MET), 4 O Horizons (CON) | `evaluates` aspirational dimensions |
| CANON-25000 | MEMORY_ARCH | Memory Architecture (STR), Context Graduation (WF) | `governs` memory systems |
| CANON-25100 | CONTEXT_TRANS | Context Transfer (WF), Reinit Capsule (ART) | `enables` session continuity |
| CANON-25200 | CONSTELLATION_ARCH | Constellation (STR), Pantheon (STR), 10 Agents (AGT) | `governs` agent architecture |

### Intelligence Chain (30xxx)
| CANON ID | Name | Entities Defined | Key Relations |
|----------|------|-----------------|---------------|
| CANON-30000 | INTELLIGENCE | Intelligence Chain (CON), Substrate (CON) | `governs` 30xxx subtree |
| CANON-30100 | ASA | ASA Stack L0-L6 (STR) | `models` intelligence layers |
| CANON-30200 | POSITIONING | Displacement Paradigm (CON), Positioning (CON) | `governs` strategic position |
| CANON-30300 | TECH_STACK | Stack Teleology (CON), Disposition Categories (MET) | `evaluates` all tools |
| CANON-30310 | MIGRATION | Migration Patterns (WF) | `enables` platform transitions |
| CANON-30320 | WORKFLOW_INTEL | Workflow Intelligence (CAP) | `enables` process optimization |
| CANON-30330 | RESEARCH_PROTOCOLS | Research Pipeline (WF), Consensus Research (WF) | `governs` research |
| CANON-30340 | IMPLEMENTATION_PATTERNS | Implementation Patterns (WF) | `governs` execution |
| CANON-30400 | AGENTIC_ARCHITECTURE | Agentic Architecture (STR), Apparatus (CON) | `governs` agent design |
| CANON-30410 | COGNITIVE_ARCHITECTURE | Cognitive Architecture (STR), Characteristic Cognition (CON) | `models` AI cognition |
| CANON-30420 | MULTI_AGENT_ORCHESTRATION | Multi-Agent (STR), Medley Mode (WF) | `governs` agent coordination |
| CANON-30430 | MEMORY_SYSTEMS | Memory Systems (STR), GAS (CAP) | `enables` persistent memory |
| CANON-30440 | SAFETY_ALIGNMENT | Safety/Alignment (PROTO) | `governs` agent safety |
| CANON-30450 | PRODUCTION_FRAMEWORKS | Production Frameworks (STR) | `enables` deployment |
| CANON-30460 | INTERACTION_DYNAMICS | Interaction Dynamics (CON) | `models` agent-human interaction |

### Information Chain (31xxx)
| CANON ID | Name | Entities Defined | Key Relations |
|----------|------|-----------------|---------------|
| CANON-31000 | INFORMATION | Information Chain (CON), Acumen Virtue (CON) | `governs` 31xxx subtree |
| CANON-31100 | ACUMEN | Acumen (CON), Information Processing (CAP) | `governs` information layer |
| CANON-31110 | FEEDCRAFT | Feedcraft (CAP), Feed Curation (WF) | `provides` information intake |
| CANON-31115 | IIC_IMPL | IIC Implementation (WF), 5 Configs (ART) | `implements` IIC system |
| CANON-31120 | TONE_LIBRARY | Tone Library (ART), Voice Profiles (CON) | `governs` output voice |
| CANON-31121 | TONE_TAXONOMY | Tone Taxonomy (NOT) | `classifies` tones |
| CANON-31122 | RHETORICAL | Rhetorical Patterns (CON) | `enables` persuasion |
| CANON-31130 | SEVEN_LAYER | Seven Layer Model (STR) | `models` information processing |
| CANON-31140 | IIC | Intelligence Constellation (CON), IIC Architecture (STR) | `governs` IIC system |
| CANON-31141 | FIVE_ACCOUNT | Five Account Model (STR) | `structures` IIC accounts |
| CANON-31142 | PLATFORM_GRAMMAR | Platform Grammar (NOT), Reception Calibration (CON) | `governs` platform interaction |
| CANON-31143 | FEED_CURATION | Feed Curation (WF), Four Systems (STR) | `governs` feed processing |
| CANON-31150 | PLATFORM_CAPABILITY_CATALOG | Platform Capabilities (CAP), 7 Platforms (TOOL) | `catalogs` tool capabilities |

### Insight Chain (32xxx)
| CANON ID | Name | Entities Defined | Key Relations |
|----------|------|-----------------|---------------|
| CANON-32000 | INSIGHT | Insight Chain (CON), Coherence Virtue (CON) | `governs` 32xxx subtree |
| CANON-32100 | COHERENCE | Coherence (CON), Cross-chain Integration (CAP) | `evaluates` system coherence |
| CANON-32110 | COHERENCE_SYS | Coherence System (STR) | `implements` coherence checks |
| CANON-32120 | META_ANALYSIS | Meta-Analysis (CAP) | `enables` cross-domain insight |

### Expertise Chain (33xxx)
| CANON ID | Name | Entities Defined | Key Relations |
|----------|------|-----------------|---------------|
| CANON-33000 | EXPERTISE | Expertise Chain (CON), Efficacy Virtue (CON) | `governs` 33xxx subtree |
| CANON-33100 | EFFICACY | Efficacy (CON), Economic Demonstration (CAP) | `evaluates` economic output |
| CANON-33110 | BIZ_BACKBONE | Business Backbone (STR), Revenue Streams (CON) | `enables` economic sustainability |
| CANON-33111 | BIZ_ENHANCE | Business Enhancement (CAP) | `improves` economic output |
| CANON-33112 | REVENUE_MODEL | Revenue Model (STR), Monetization (CAP) | `implements` revenue generation |

### Knowledge Chain (34xxx)
| CANON ID | Name | Entities Defined | Key Relations |
|----------|------|-----------------|---------------|
| CANON-34000 | KNOWLEDGE | Knowledge Chain (CON), Mastery Virtue (CON) | `governs` 34xxx subtree |
| CANON-34100 | MASTERY | Mastery (CON), Skill Development (WF) | `evaluates` competence |
| CANON-34110 | CURRICULUM | Curriculum (ART), Learning Pathways (WF) | `structures` knowledge acquisition |
| CANON-34120 | SYLLABUS | Syllabus (ART), Course Structure (STR) | `implements` curriculum |

### Wisdom Chain (35xxx)
| CANON ID | Name | Entities Defined | Key Relations |
|----------|------|-----------------|---------------|
| CANON-35000 | WISDOM | Wisdom Chain (CON), Transcendence Virtue (CON) | `governs` 35xxx subtree |
| CANON-35100 | TRANSCENDENCE | Transcendence Ring (CON), 4-Stage Wisdom Trajectory (WF) | `evaluates` wisdom development |
| CANON-35110 | TRANS_SYSTEM | Transcendence System (STR) | `implements` wisdom tracking |
| CANON-35120 | NEURODIVERGENT | Neurodivergent Framework (CON) | `models` cognitive diversity |
| CANON-35121 | NEURODIVERGENT_PATTERNS | Neurodivergent Patterns (CON) | `details` cognitive patterns |
| CANON-35200 | GAIAN_NODE | Gaian Field Node (CON), Physical Embodiment (CON) | `defines` Modal 3-4 target |
| CANON-35210 | METAHUMANISM | Metahumanism (CON) | `extends` wisdom to civilization |

### Meta
| CANON ID | Name | Entities Defined | Key Relations |
|----------|------|-----------------|---------------|
| CANON-99000 | HISTORICAL | Historical Record (ART), Oracle Archive (ART) | `tracks` system history |

---

## EXPANDED RELATION TABLE (200+)

Explicit typed relations between entities. Each row = one relation.

### Governance Relations (governed_by)
| From | Relation | To | Evidence |
|------|----------|-----|---------|
| CANON (STR) | governed_by | Five Invariants (CON) | CANON-00003, CLAUDE.md |
| CANON (STR) | governed_by | SCHEMA (ART) | CANON-00000 |
| Constellation (STR) | governed_by | ASIA Constitution (ART) | CANON-00017 |
| Constellation (STR) | governed_by | COCKPIT.md (ART) | COCKPIT.md |
| All Agents (AGT) | governed_by | ASIA Constitution (ART) | CANON-00017 |
| Commander (AGT) | governed_by | CLAUDE.md (ART) | CLAUDE.md |
| All STR entities | governed_by | FLAT PRINCIPLE (CON) | CLAUDE.md §1 |
| Protected Zones (PROTO) | governed_by | Sovereign (AGT) | CLAUDE.md §3 |
| Stack Teleology (CON) | governed_by | sigma-1 (STR) | CANON-30300 |
| Reception Calibration (CON) | governed_by | sigma-3 (STR) | CANON-31142 |
| Ground Truth (CON) | governed_by | Invariant 5 (CON) | CLAUDE.md |
| Six Chains (CON) | governed_by | SCHEMA (ART) | CANON-00000 |
| Content Pipeline (WF) | governed_by | Signal Tier (MET) | CANON-00014 |
| Token Rent Policy (CON) | governed_by | DEFRAG_CONVICTION (CON) | CANON-00006 |
| Clarescence (WF) | governed_by | 10-pass framework (STR) | REF-CLARESCENCE_RUNBOOK |
| Ontology Bridge (ART) | governed_by | REF-ONTOLOGY_REGISTRY (ART) | ARCH-ROSETTA_ONTOLOGY_BRIDGE |
| T1a Linear (TOOL) | governed_by | Five-Tier Task Architecture (STR) | ARCH-TASK_TIER_ARCHITECTURE |
| T1b ClickUp (TOOL) | governed_by | Five-Tier Task Architecture (STR) | ARCH-TASK_TIER_ARCHITECTURE |
| CLI Orchestration Config (STR) | governed_by | T1a Linear (TOOL) | ARCH-TASK_TIER_ARCHITECTURE |

### Containment Relations (part_of / contains)
| From | Relation | To | Evidence |
|------|----------|-----|---------|
| cosmos (CON) | part_of | CANON (STR) | CANON-00000 |
| core (CON) | part_of | CANON (STR) | CANON-00000 |
| lattice (CON) | part_of | CANON (STR) | CANON-00000 |
| chain (CON) | part_of | CANON (STR) | CANON-00000 |
| planetary (CON) | part_of | chain (CON) | CANON-00000 |
| lunar (CON) | part_of | planetary (CON) | CANON-00000 |
| satellite (CON) | part_of | CANON (STR) | CANON-00000 |
| comet (CON) | part_of | CANON (STR) | CANON-00000 |
| asteroid (CON) | part_of | CANON (STR) | CANON-00000 |
| Intelligence (CON) | part_of | Six Chains (CON) | CANON-21000 |
| Information (CON) | part_of | Six Chains (CON) | CANON-21000 |
| Insight (CON) | part_of | Six Chains (CON) | CANON-21000 |
| Expertise (CON) | part_of | Six Chains (CON) | CANON-21000 |
| Knowledge (CON) | part_of | Six Chains (CON) | CANON-21000 |
| Wisdom (CON) | part_of | Six Chains (CON) | CANON-21000 |
| Acumen (CON) | part_of | Information Chain (CON) | CANON-31000 |
| Coherence (CON) | part_of | Insight Chain (CON) | CANON-32000 |
| Efficacy (CON) | part_of | Expertise Chain (CON) | CANON-33000 |
| Mastery (CON) | part_of | Knowledge Chain (CON) | CANON-34000 |
| Transcendence (CON) | part_of | Wisdom Chain (CON) | CANON-35000 |
| Constellation (STR) | contains | Pantheon (STR) | COCKPIT.md |
| Pantheon (STR) | contains | Commander (AGT) | COCKPIT.md |
| Pantheon (STR) | contains | Adjudicator (AGT) | COCKPIT.md |
| Pantheon (STR) | contains | Cartographer (AGT) | COCKPIT.md |
| Pantheon (STR) | contains | Ajna (AGT) | COCKPIT.md |
| Pantheon (STR) | contains | Psyche (AGT) | COCKPIT.md |
| Pantheon (STR) | contains | Vizier (AGT) | COCKPIT.md |
| Pantheon (STR) | contains | Vanguard (AGT) | COCKPIT.md |
| Pantheon (STR) | contains | Diviner (AGT) | COCKPIT.md |
| Pantheon (STR) | contains | Oracle (AGT) | COCKPIT.md |
| Pantheon (STR) | contains | Augur (AGT) | COCKPIT.md |
| Five-Tier Architecture (STR) | contains | T0 Intention Compass (ART) | ARCH-TASK_TIER_ARCHITECTURE |
| Five-Tier Architecture (STR) | contains | T1a Linear (TOOL) | ARCH-TASK_TIER_ARCHITECTURE |
| Five-Tier Architecture (STR) | contains | T1b ClickUp (TOOL) | ARCH-TASK_TIER_ARCHITECTURE |
| Five-Tier Architecture (STR) | contains | T2 Implementation Map (ART) | ARCH-TASK_TIER_ARCHITECTURE |
| Five-Tier Architecture (STR) | contains | T3 Session Tasks (WF) | ARCH-TASK_TIER_ARCHITECTURE |
| CANON Frontmatter Schema (STR) | contains | operational_status (MET) | PRAC-ontology_queries |
| CANON Frontmatter Schema (STR) | contains | entities_defined (MET) | PRAC-ontology_queries |
| CANON Frontmatter Schema (STR) | contains | depends_on (MET) | PRAC-ontology_queries |
| ASA Stack (STR) | contains | L0 Physical (CON) | CANON-30100 |
| ASA Stack (STR) | contains | L1 Data (CON) | CANON-30100 |
| ASA Stack (STR) | contains | L2 Model (CON) | CANON-30100 |
| ASA Stack (STR) | contains | L3 Prompt (CON) | CANON-30100 |
| ASA Stack (STR) | contains | L4 Agent (CON) | CANON-30100 |
| ASA Stack (STR) | contains | L5 Multi-Agent (CON) | CANON-30100 |
| ASA Stack (STR) | contains | L6 Agentic Emergence (CON) | CANON-30100 |
| Cognitive Palace (CON) | contains | Experience Topology (CON) | CANON-20000 |
| Cognitive Palace (CON) | contains | Dimension Coordinators (AGT) | CANON-20010 |
| Cognitive Palace (CON) | contains | Meta-Systems (STR) | CANON-20020 |
| DISTILL/TRANSFORM/EXPAND (CAP) | contains | integrate (CAP) | CANON-00014 |
| DISTILL/TRANSFORM/EXPAND (CAP) | contains | readize (CAP) | CANON-00014 |
| DISTILL/TRANSFORM/EXPAND (CAP) | contains | listenize (CAP) | CANON-00014 |
| DISTILL/TRANSFORM/EXPAND (CAP) | contains | compile (CAP) | CANON-00014 |
| DISTILL/TRANSFORM/EXPAND (CAP) | contains | amplify (CAP) | CANON-00014 |

### Usage Relations (uses)
| From | Relation | To | Evidence |
|------|----------|-----|---------|
| Commander (AGT) | uses | Claude Code (TOOL) | COCKPIT.md |
| Adjudicator (AGT) | uses | Codex CLI (TOOL) | COCKPIT.md |
| Cartographer (AGT) | uses | Gemini CLI (TOOL) | COCKPIT.md |
| Ajna (AGT) | uses | OpenClaw (TOOL) | COCKPIT.md |
| Psyche (AGT) | uses | OpenClaw (TOOL) | COCKPIT.md |
| Vizier (AGT) | uses | Claude Web (TOOL) | COCKPIT.md |
| Vanguard (AGT) | uses | ChatGPT Web (TOOL) | COCKPIT.md |
| Diviner (AGT) | uses | Gemini Web (TOOL) | COCKPIT.md |
| Oracle (AGT) | uses | Grok (TOOL) | COCKPIT.md |
| Augur (AGT) | uses | Perplexity (TOOL) | COCKPIT.md |
| Ajna (AGT) | uses | M1 Mac mini (TOOL) | REF-OPENCLAW_CONFIG_MIRROR |
| Psyche (AGT) | uses | M4 MacBook Air (TOOL) | REF-OPENCLAW_CONFIG_MIRROR |
| Wikilink Graph (STR) | uses | Obsidian (TOOL) | CANON-00000 |
| Dataview Query (CAP) | uses | Obsidian Dataview (TOOL) | PRAC-ontology_queries |
| Feedcraft (CAP) | uses | X (TOOL) | CANON-31110 |
| Feedcraft (CAP) | uses | YouTube (TOOL) | CANON-31110 |
| Feedcraft (CAP) | uses | RSS (TOOL) | CANON-31110 |
| Clarescence (WF) | uses | Triumvirate (CON) | REF-CLARESCENCE_RUNBOOK |
| Clarescence (WF) | uses | 18+ Lenses (MET) | REF-CLARESCENCE_RUNBOOK |
| Clarescence (WF) | uses | Five Faces (CON) | REF-CLARESCENCE_RUNBOOK |
| Clarescence (WF) | uses | Omni-Qualities (MET) | REF-CLARESCENCE_RUNBOOK |
| Heartbeat (WF) | uses | OpenClaw (TOOL) | COCKPIT.md |
| Corpus Sensing (CAP) | uses | Gemini CLI (TOOL) | CANON-25200 |

### Provision Relations (provides)
| From | Relation | To | Evidence |
|------|----------|-----|---------|
| Claude Code (TOOL) | provides | Execution (CAP) | CANON-25200 |
| OpenClaw (TOOL) | provides | Persistent Orchestration (CAP) | CANON-25200 |
| OpenClaw (TOOL) | provides | Memory (CAP) | REF-OPENCLAW_CONFIG_MIRROR |
| OpenClaw (TOOL) | provides | Cron (CAP) | REF-OPENCLAW_CONFIG_MIRROR |
| Gemini CLI (TOOL) | provides | Corpus Sensing (CAP) | CANON-25200 |
| Claude Web (TOOL) | provides | Interpretation (CAP) | COCKPIT.md |
| ChatGPT Web (TOOL) | provides | Strategic Planning (CAP) | COCKPIT.md |
| Gemini Web (TOOL) | provides | Clarification (CAP) | COCKPIT.md |
| Grok (TOOL) | provides | Cultural Sensing (CAP) | COCKPIT.md |
| Perplexity (TOOL) | provides | Verification (CAP) | COCKPIT.md |
| Codex CLI (TOOL) | provides | Code Fabrication (CAP) | COCKPIT.md |
| T1a Linear (TOOL) | provides | Project Management (CAP) | ARCH-TASK_TIER_ARCHITECTURE |
| T1b ClickUp (TOOL) | provides | Life Task Management (CAP) | ARCH-TASK_TIER_ARCHITECTURE |
| CANON Frontmatter Schema (STR) | provides | Machine Readability (CAP) | PRAC-ontology_queries |
| Dataview Query (CAP) | provides | Palantir Dashboard (CON) | PRAC-ontology_queries |

### Enablement Relations (enables)
| From | Relation | To | Evidence |
|------|----------|-----|---------|
| Ontology Bridge (ART) | enables | PROJ-006 (CON) | ARCH-ROSETTA_ONTOLOGY_BRIDGE |
| CANON Frontmatter Schema (STR) | enables | Dataview Query (CAP) | PRAC-ontology_queries |
| Dataview Query (CAP) | enables | Coherence Checking (CAP) | PRAC-ontology_queries |
| Dataview Query (CAP) | enables | Dependency Analysis (CAP) | PRAC-ontology_queries |
| Context Graduation (WF) | enables | Knowledge Persistence (CAP) | CANON-25100 |
| Reinit Capsule (ART) | enables | Session Continuity (CAP) | CANON-25100 |
| Stack Teleology (CON) | enables | Tool Evaluation (CAP) | CANON-30300 |
| Five-Tier Architecture (STR) | enables | Coordinated Execution (CAP) | ARCH-TASK_TIER_ARCHITECTURE |
| T1a Linear (TOOL) | enables | Bidirectional Sync (CAP) | IMPL-A-0012 |
| PROJ-006a (CON) | enables | PROJ-006b (CON) | DYN-BACKLOG |
| PROJ-006 (CON) | enables | Palantir Dashboard (CON) | INT-MI19 |
| PROJ-002 (CON) | enables | PROJ-005 (CON) | DYN-BACKLOG |
| PROJ-003 (CON) | enables | PROJ-006b (CON) | DYN-BACKLOG |
| Modal 1 (CON) | enables | Modal 2 (CON) | CANON-00012 |
| Modal 2 (CON) | enables | Modal 3 (CON) | CANON-00012 |
| Modal 3 (CON) | enables | Gaian Field Node (CON) | CANON-35200 |
| Gaian Field Node (CON) | enables | Modal 4 (CON) | CANON-00012 |

### Production Relations (produces)
| From | Relation | To | Evidence |
|------|----------|-----|---------|
| Clarescence (WF) | produces | Convergent Recommendation (ART) | REF-CLARESCENCE_RUNBOOK |
| Clarescence (WF) | produces | Decision Atom (ART) | REF-CLARESCENCE_RUNBOOK |
| Oracle Session (WF) | produces | Intention Entries (ART) | ARCH-INTENTION_COMPASS |
| Feedcraft (CAP) | produces | Curated Feeds (ART) | CANON-31110 |
| readize (CAP) | produces | Read-Optimized Content (ART) | CANON-00014 |
| listenize (CAP) | produces | Audio-Optimized Content (ART) | CANON-00014 |
| Audizer Protocol (WF) | produces | TTS Scripts (ART) | CANON-00014 |
| Metabolic Defrag (WF) | produces | Lean Corpus (ART) | CANON-00006 |
| Research Pipeline (WF) | produces | Synthesis Documents (ART) | CANON-30330 |
| Commander (AGT) | produces | Commits (ART) | CLAUDE.md |
| Ajna (AGT) | produces | Commits (ART) | REF-OPENCLAW_CONFIG_MIRROR |

### Evaluation Relations (evaluates)
| From | Relation | To | Evidence |
|------|----------|-----|---------|
| operational_status (MET) | evaluates | CANON Files (ART) | PRAC-ontology_queries |
| 8 Crystalline Chars (MET) | evaluates | Content Quality (CON) | CANON-00007 |
| Signal Tier (MET) | evaluates | Information Value (CON) | CANON-31143 |
| Disposition Categories (MET) | evaluates | Tools (TOOL) | CANON-30300 |
| Convergence Metrics (MET) | evaluates | Research Quality (CON) | CANON-30330 |
| Omni-Qualities (MET) | evaluates | System Aspirations (CON) | CANON-24000 |
| Five Faces (CON) | evaluates | System Alignment (CON) | CANON-11000 |
| Token Rent Policy (CON) | evaluates | Content Worth (CON) | CANON-00006 |
| Value Modality (MET) | evaluates | Consumption Mode (CON) | CANON-31130 |

### Alias Relations (alias_of)
| From | Relation | To | Evidence |
|------|----------|-----|---------|
| IIC | alias_of | Intelligence Constellation | CANON-31140 |
| Medley Mode (WF) | alias_of | Operational Constellation Mode | COCKPIT.md |
| Vizier (AGT) | alias_of | INTERPRETER (AGT) | COCKPIT.md |
| Vanguard (AGT) | alias_of | COMPILER (AGT) | COCKPIT.md |
| Diviner (AGT) | alias_of | DIGESTOR (AGT) | COCKPIT.md |
| Cartographer (AGT) | alias_of | SENSOR (AGT) | COCKPIT.md |
| Commander (AGT) | alias_of | EXECUTOR-LEAD (AGT) | COCKPIT.md |
| Oracle (AGT) | alias_of | RECON (AGT) | COCKPIT.md |
| Augur (AGT) | alias_of | VERIFIER (AGT) | COCKPIT.md |

### Supersession Relations (replaces)
| From | Relation | To | Evidence |
|------|----------|-----|---------|
| Synapticality (CON) | replaces | Cognitive Palace (CON) | Rosetta #39 |
| Reception Calibration (CON) | replaces | Archetype Engineering (CON) | Rosetta #79 |
| "think hard" (CON) | replaces | megathink (CON) | Rosetta #159 |
| Function Index (STR) | replaces | Agentic-First Membrane (CAP) | Rosetta #161 |
| Vanguard (AGT) | replaces | Deviser (AGT) | Rosetta #95 |

### Requirement Relations (requires)
| From | Relation | To | Evidence |
|------|----------|-----|---------|
| PROJ-006b (CON) | requires | SOVEREIGN-009 (ART) | DYN-BACKLOG |
| PROJ-005 (CON) | requires | PROJ-002 (CON) | DYN-BACKLOG |
| PROJ-007 (CON) | requires | PROJ-006 (CON) | DYN-BACKLOG |
| PROJ-015 (CON) | requires | PROJ-014 (CON) | DYN-BACKLOG |
| Gaian Field Node (CON) | requires | Capital ($800K-$1.8M) (CON) | CANON-35200 |
| Gaian Field Node (CON) | requires | Construction Skills (CAP) | CANON-35200 |
| Gaian Field Node (CON) | requires | Site Selection (WF) | CANON-35200 |
| Wisdom Chain Stage 4 (CON) | requires | All Other Chains Advanced (CON) | CANON-35000 |
| Transcendence Stage 3+ (CON) | requires | Embodiment Grounding (CON) | CANON-35000 |
| Adjudicator (AGT) | requires | Codex CLI API Key (ART) | DYN-BACKLOG |
| Cartographer (AGT) | requires | Gemini CLI API Key (ART) | DYN-BACKLOG |

### Tier 10: Command Doctrine Domain (Rosetta #202-206, v2.4.0)
| # | Term | Entity Type | Relations |
|---|------|-------------|-----------|
| 202 | Breach Exploitation | WF | `enables` Forward Passage of Lines; `requires` Reserve Commitment; `governed_by` Procedural Standard Bearer |
| 203 | Forward Passage of Lines | WF | `part_of` Breach Exploitation; `requires` Dispatch Protocol; `enables` Critical Path Compression |
| 204 | Reserve Commitment | WF | `part_of` Breach Exploitation; `uses` Agent Dispatch; `enables` Throughput Surge |
| 205 | Follow-and-Support | WF | `part_of` Breach Exploitation; `produces` Hardening Artifacts; `enables` Operational Durability |
| 206 | Procedural Standard Bearer | AGT | `governed_by` REF-PROCEDURAL_STANDARD_BEARER.md; `evaluates` task outputs; `enables` process quality consistency |

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

1. ~~**Validate this classification**~~ — DONE (Sovereign approved via Clarescence)
2. ~~**Expand relation graph**~~ — DONE (v1.0: 200+ explicit relations)
3. **Seed Notion databases** — If SOVEREIGN-009 Decision 2 ratifies Obsidian+Notion
4. **Install Obsidian plugins** — Dataview + Juggl minimum viable set
5. ~~**Cross-reference against CANON**~~ — DONE (v1.0: all 79 CANON files mapped)
6. ~~**Bridge to PROJ-006**~~ — DONE (this document IS the ontology foundation)
7. **Complete CANON frontmatter extension** — 10/79 done (pilot), targeting 79/79
8. **Validate Dataview queries in Obsidian** — Test PRAC-ontology_queries.md queries
9. **Add inter-CANON dependency graph** — Map all wikilink targets as explicit depends_on
10. **Linear↔Ontology sync** — Ensure Linear issues reference CANON entities

---

## VERSION HISTORY

**v1.1.0** (2026-02-12): Command Doctrine bridge extension
- Added Tier 10 mapping for Rosetta entries #202-206
- Added ontology relations for Breach Exploitation, Forward Passage of Lines, Reserve Commitment, Follow-and-Support, Procedural Standard Bearer
- Added governance link to `REF-PROCEDURAL_STANDARD_BEARER.md`

**v1.0.0** (2026-02-05): Major Expansion — Commander (Claude Code Opus)
- 177 terms classified (168 original + 9 new from Task Architecture session)
- 200+ explicit typed relations across 9 categories (governance, containment, usage, provision, enablement, production, evaluation, alias, supersession, requirement)
- CANON cross-reference index: all 79 files mapped with entities and key relations
- New Tier 9: Task Architecture + Ontology terms (#170-177)
- Entity type distribution updated (CON 44, CAP 30, AGT 25, NOT 24, WF 23, STR 17, MET 10, ART 7, PROTO 3)
- Relation count: ~40 → 200+ (5x expansion)

**v0.1.0** (2026-02-06): Genesis — Ajna (Opus 4.5)
- 168 Rosetta terms classified into 10 entity types
- 5 key relation clusters mapped
- Notion database schema proposed
- Obsidian plugin recommendations
