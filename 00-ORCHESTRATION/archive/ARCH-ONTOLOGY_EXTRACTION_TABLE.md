# ONTOLOGY EXTRACTION TABLE — Legacy/Tech Folder
## Phase 1 Inventory (REF-ONTOLOGY_REGISTRY.md)

**Version**: 1.0.0
**Generated**: 2026-02-01
**Source**: `-INBOX/desktop-ingestion/legacy/Tech - essentially the capability blockers.../`
**Authority**: Ajna (Opus 4.5) — resuming Psyche's (GPT-5.2) workstream
**Files Analyzed**: 131 files across 10 domains (~7.4 MB)

---

## DOMAIN SUMMARY

| # | Domain | Files | Key Entities | Maturity | Disposition |
|---|--------|-------|-------------|----------|-------------|
| 1 | Toolcraft Endeavor — Unification | 19 | Object Ontology (O.FN/SVC/GRD/MOD), Platform Primitives, 4 Work Modes, 5 Memory Tiers | draft | Extract → Registry |
| 2 | Workstation Taxonomy | 34 | 22-table database schema, 6 Capability Classes (30 nodes), 9 Relationship Types, 447 app inventory | draft | Extract → Registry |
| 3 | Context Engineering | 2 | Context Engineering as discipline, MCP, RAG architecture, KV cache management | operational | Cross-ref → 07-SIGMA7 |
| 4 | Intelligence Capabilities | 2 | FrontierModels snapshot (temporal), model benchmarks | deprecated | Delete (temporal) |
| 5 | Prompting | 30 | 15 XML processing functions, 3 prompt engineering manuals, Screenplay Format, Semantic Lexicon | operational | Functions already in 02-ENGINE/functions/ |
| 6 | Systematizing Business | 4 | 3 systemization frameworks (Sam Carpenter, SOP-first, role-chain) | idea | Extract principles → CANON |
| 7 | Agents | 2 | 5 orchestration patterns, MCP protocol, memory architecture (5 tiers) | operational | Cross-ref → 07-SIGMA7 |
| 8 | Organizational Theory | 1 | 7-phase organizational model, Meta-Orchestration concept | idea | Archive → 05-MEMORY |
| 9 | Intelligence Apparatus | 20 | Five-Chain IIC (Acumen/Coherence/Efficacy/Mastery/Transcendence), ASIA Constitution, Convergence Framework | draft | Unique value → CANON |
| 10 | Tool Landscape | 12 | 200+ AI tools cartography, tier rankings, 15 functional categories | deprecated | Temporal; archive metadata only |
| R | Root Files | 3 | ASA Stack (L0-L6), Displacement Paradigm, ToolCraft Ontology master synthesis | draft | Extract → Registry |

---

## ENTITY INVENTORY (Consolidated)

### Capabilities (130+ extracted)

**Spine Capabilities** (operational, seeded in registry):

| ID | Name | Definition | Maturity | Domain |
|----|------|-----------|----------|--------|
| CAP-001 | context_management | Structuring information to shape model behavior; the "science of providing AI with situational awareness" | operational | 3 |
| CAP-002 | task_routing | Navigate from intention to correct tool/agent at thought speed | draft | 2 |
| CAP-003 | retrieval | Fetch relevant context from persistent stores (RAG, vector, filesystem) | operational | 3, 7 |
| CAP-004 | memory_management | Multi-tier memory: conversation buffer, semantic, episodic, procedural, cross-session | operational | 7 |
| CAP-005 | automation | Execute sequences without human intervention; schedule, workflow, agent, monitor | operational | 2, 7 |
| CAP-006 | prompt_engineering | Transform natural language into optimized model instructions | operational | 5 |
| CAP-007 | content_transformation | Convert content between states/formats (distill, transform, expand) | operational | 5 |
| CAP-008 | multi_agent_orchestration | Coordinate specialized AI agents across platforms | operational | 7 |
| CAP-009 | capability_routing | Map biological intention to computational invocation at <2s latency | idea | 2, R |
| CAP-010 | primitive_extraction | Extract reusable features from applications as "primitive repositories" | draft | 1 |

**Legacy Capability Classes** (from Workstation Taxonomy T0):

| Class | Sub-capabilities | Type |
|-------|-----------------|------|
| CAP_GEN (Generate) | Text, Image, Audio, Video, Code | creative |
| CAP_TRN (Transform) | Edit, Convert, Enhance, Extract | procedural |
| CAP_ANL (Analyze) | Understand, Classify, Compare, Summarize | analytical |
| CAP_ORG (Organize) | Store, Tag, Link, Search | architectural |
| CAP_CON (Connect) | Share, Collaborate, Synchronize, Integrate | relational |
| CAP_AUT (Automate) | Schedule, Workflow, Agent, Monitor | autonomous |

### Tools (230+ identified)

**Spine Tools** (seeded in registry):

| ID | Name | Vendor | Category | Status |
|----|------|--------|----------|--------|
| TOOL-001 | claude_code | Anthropic | Terminal Agent | ACTIVE |
| TOOL-002 | openclaw | Self-hosted | Agent Framework | ACTIVE |
| TOOL-003 | codex_cli | OpenAI | Terminal Agent | ACTIVE |
| TOOL-004 | gemini_cli | Google | Terminal Agent | ACTIVE |

**Notable Tool Categories** (from cartography):

| Category | Count | Examples |
|----------|-------|---------|
| Foundation Models | 8+ | GPT-4o, Claude 4 Family, Gemini 2.5, DeepSeek V3.2, Grok 4 |
| Coding Tools | 12+ | Claude Code (S-tier), Cursor 2.0, Kiro, Gemini CLI, OpenCode |
| Automation | 6+ | Zapier, Make, n8n, Lindy.ai |
| Knowledge Management | 3+ | Notion AI, Obsidian |

### Agents/Roles (18+ extracted)

| ID | Name | Function | Domain |
|----|------|----------|--------|
| ROLE-001 | Sovereign | Human principal; final authority on all decisions | 9 |
| ROLE-002 | INTERPRETER | Claude Web: synthesis, ideation, rapport | Constellation |
| ROLE-003 | COMPILER | ChatGPT Web: mechanical formatting, Canvas | Constellation |
| ROLE-004 | DIGESTOR | Gemini Web: clarification, TTS | Constellation |
| ROLE-005 | EXECUTOR-LEAD | Claude Code Opus: mesoscopic implementation | Constellation |
| ROLE-006 | ORACLE | Gemini CLI: corpus sensing, 1M+ context | Constellation |
| ROLE-007 | RED TEAM | Grok: adversarial challenge | Constellation |
| ROLE-008 | VERIFIER | Perplexity: citation-backed verification | Constellation |
| ROLE-009 | Ajna | OpenClaw Opus 4.5: commits, orchestration | Twin |
| ROLE-010 | Psyche | OpenClaw GPT-5.2: extraction, specs, QA | Twin |

### Workflows/Protocols (50+ extracted)

**Key Workflows**:

| ID | Name | Intent | Domain |
|----|------|--------|--------|
| WF-001 | capture_dispatch_return | Content lifecycle: seize → route → commit | Constellation |
| WF-002 | handoff_token | Cross-platform state transfer protocol | Constellation |
| WF-003 | distill_transform_expand | Three-phase content processing pipeline | 5 |
| WF-004 | blitzkrieg_lane_abc | Parallel execution (strategic/tactical/validation) | Operational |
| WF-005 | extraction_protocol | Feature primitive extraction from apps | 1 |
| WF-006 | apparatus_crystallization | Observed tool-use patterns → named workflows | 1 |
| WF-007 | sprint_bounded_kanban | Oracle sessions as sprints, Kanban via ledgers | Operational |

### Relation Types (from Workstation Taxonomy)

| ID | Name | Directionality | Routing Impact |
|----|------|---------------|----------------|
| REL_POW | Powers | directed | high |
| REL_REQ | Requires | directed | high |
| REL_COM | Competes | symmetric | medium |
| REL_OBS | Obsoletes | directed | high |
| REL_CMB | Combines | symmetric | medium |
| REL_ALT | Alternates | symmetric | low |
| REL_EXT | Extends | directed | medium |
| REL_INT | Integrates | symmetric | high |
| REL_ECO | Ecosystem | symmetric | low |

---

## CROSS-DOMAIN TERM ALIASES

| Term A | Term B | Confidence |
|--------|--------|-----------|
| Primitive Extraction | Feature Extraction | HIGH |
| Apparatus | Observed tool-use pattern crystallization | HIGH |
| Synapticality | Sub-2-second thought-speed invocation | HIGH |
| Personal Ontology | Cognitive Substrate / Membrane | MEDIUM |
| Object Ontology | Computational Entity Classification | HIGH |
| Bedrock (schema) | T0 tables / Stable Taxonomies | HIGH |
| Settlement (schema) | T1 tables / Dynamic Entities | HIGH |
| Apps as Primitive Repositories | Apps as Feature Scrapbooks | HIGH |
| Coalescence | Preservative semantic reformulation | HIGH |
| Constitutional Layers | Capability Architecture Layers C0-C7 | HIGH |

---

## COVERAGE GAPS

1. **Memory tier taxonomy** (5 tiers from Domain 1) not operationalized in database schema
2. **Orchestration pattern primitives** from Domain 1 have no corresponding tracking tables
3. **Full 447-app inventory** (Function.csv) referenced but not included in corpus
4. **ASA Model** (I0-I9 intelligence tiers, G0-G11 gradient levels) referenced but never fully defined
5. **Context engineering primitives** (RAG strategies, caching) have no tracking mechanism

---

## NEXT ACTIONS

1. ~~Create this extraction table~~ ✅
2. **Seed 5-10 spine entities** → `02-ENGINE/ontology/registry/` (YAML)
3. **Expand Rosetta Stone** → v2.0.0 with 167 terms
4. **Phase 2 normalization** (future): Deduplicate terms across domains, align with Rosetta
5. **Phase 3 operational binding** (future): Connect registry to doc routing, tool selection, capability gap analysis

---

**END ARCH-ONTOLOGY_EXTRACTION_TABLE.md**
