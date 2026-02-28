# NUCLEOSYNTHESIS MAP — Corpus Classification Authority

**Updated**: 2026-02-28 (CC58)
**Corpus**: 22 semantic topic folders, 5,954 files (49.3% reduction from 11,733 originals)
**Subcategory Indexes**: 5 largest folders indexed (3,238 files across 30 sub-themes)
**Constitutional Law**: Classification by SEMANTIC TOPIC only. Type-based clustering FORBIDDEN.

---

## Folder Census

| Folder | Files | Description | Subcategories |
|--------|------:|-------------|:---:|
| ai-biotech | 10 | Biotechnology, synthetic biology, AI in life sciences | — |
| ai-capability-futures | 448 | Frontier AI capabilities, scaling laws, AGI timelines, capability predictions | **6** |
| ai-memory-retrieval | 393 | Long-term memory, RAG, vector databases, knowledge graphs, Graphiti, agent memory architecture | — |
| ai-models | 880 | Model releases, benchmarks, LLM architecture, training, fine-tuning, tokenization | **6** |
| ai-safety | 101 | Constitutional AI, RLHF, alignment, governance, existential risk | — |
| ai-video-vfx | 126 | AI image/video generation, VFX workflows, creative AI tooling | — |
| claude-code | 577 | Claude Code CLI: architecture, hooks, Plan Mode, MCP, skills, worktrees, permissions | **6** |
| design-taste | 193 | Design philosophy, aesthetics, craft, UI/UX, "Taste for Makers" | — |
| geopolitics-grand-strategy | 163 | US-China, grand strategy, civilizational analysis, defense, international relations | — |
| health-psychology | 181 | Sleep, fitness, mental health, neuroscience, biohacking, psychology | — |
| infrastructure | 90 | DevOps, cloud, servers, networking, compute economics | — |
| leadership-management | 52 | Executive decision-making, org design, management frameworks | — |
| meaning-civilization | 190 | Meaning crisis (Vervaeke), civilizational inflection, cultural criticism | — |
| multi-agent-systems | 761 | Multi-agent coordination, swarms, orchestration, MCP patterns, harness engineering, Syncrescendence operational files | **6** |
| openclaw | 572 | OpenClaw/ClawdBot/Moltbot: installation, security, memory, SOUL.md, phone, fleets | **6** |
| philosophy-esoterica | 234 | Consciousness, transhumanism, qualia, panpsychism, Hermetic tradition, alchemy, Kabbalah | — |
| product-business | 242 | Business models, PMF, SaaS, AI product strategy, distribution | — |
| productivity-pkm | 184 | Second Brain, PKM, Obsidian, habits, workflow automation, focus | — |
| prompt-engineering | 41 | Prompt design, templates, optimization, few-shot patterns | — |
| startup-vc | 81 | Founders, fundraising, startup culture, VC dynamics | — |
| vibe-coding | 207 | AI-assisted coding practice, prompt-to-product, Karpathy guidelines | — |
| writing-creation | 221 | Writing craft, rhetoric, content creation, voice/TTS | — |

**Total**: 5,954 files across 22 folders. 49.3% reduction from 11,733 originals. 5 folders subcategorized (3,238 files, 30 sub-themes).

---

## Classification Patterns (Wisdom)

### What Works
- **Semantic topic as sole classifier.** A file about consciousness goes in philosophy-esoterica whether it's .jsonl, .md, .py, or .log. This principle resolved every ambiguity once enforced.
- **Agent-independent convergence.** When Oracle, Cartographer, and Adjudicator independently agree a file is misplaced, it is misplaced. Triangulation eliminates individual bias.
- **Content-reading over filename-matching.** Files with numeric IDs (00001.jsonl) carry no semantic signal in their names. Only reading content determines placement.

### Anti-Patterns (SEARED)
- **Type-based routing** — the single most common error. Routing all .jsonl to ai-memory-retrieval, all .py to infrastructure, all .log to multi-agent-systems. CONSTITUTIONALLY FORBIDDEN. The content determines the folder, never the extension.
- **Source-based routing** — clustering by content creator or platform instead of topic. Alex Hormozi content about business goes in product-business; his content about health goes in health-psychology. Creator is not a category.
- **Keyword inflation** — "claw" or "molt" in a filename doesn't mean openclaw. "Agent" doesn't mean multi-agent-systems. Read the content.
- **News-roundup scatter** — AI news digests covering multiple topics were scattered across folders based on which topic was mentioned first. These belong in ai-capability-futures (their primary semantic weight is AI trajectory).
- **Operational-vs-about conflation** — a config file FOR a multi-agent system is ABOUT multi-agent systems. A task file about memory architecture is ABOUT ai-memory-retrieval. The "about" test always wins.

### Boundary Rulings (Sovereign-Ratified)
- **philosophy-esoterica vs meaning-civilization**: SEPARATE. Natural joint confirmed — consciousness/mysticism IS different from meaning/civilization.
- **claude-code vs vibe-coding**: SEPARATE. Claude Code = the specific tool/platform. Vibe coding = the general practice regardless of tool.
- **ai-memory-retrieval vs productivity-pkm**: SEPARATE. Different audiences, different problems. AI memory = technical architecture. PKM = human knowledge workflows.
- **multi-agent-systems**: Coherent despite size. Internal Syncrescendence operational files belong here when they ARE about multi-agent coordination.

---

## Repetitions — Nature, Causes, and Resolution (CC57)

The corpus contained ~895 redundant files. Forensic analysis revealed six distinct mechanisms — each a different species of repetition with different root causes and different implications.

### Mechanism 1: Pipeline Handshake Artifacts (773 pairs — dominant)

The atom extraction pipeline ran in two stages: a Flat extractor produced `EXTRACT-SOURCE-*.jsonl` (bare atoms), then `memsync_bridge.py` wrapped each into a Graphiti bridge format (adding uuid, schema_version, provenance, timestamp, confidence). Both outputs were committed together. The Flat file was the input; the bridge file was the output. Neither stage deleted the other.

**Nature**: Not an error — a pipeline that never cleaned up its intermediates. The Flat JSONL was the precursor; the Graphiti JSONL was the cleaned version. Both surviving is the artifact of a batch process that committed everything.

**Resolution**: 773 Flat JSONL removed. 146 Flat JSONL with no matching bridge pair retained (unique content). Graphiti variants preserve all data plus metadata.

### Mechanism 2: Multi-Stage Ingestion Copies (bulk of 122 near-dupes)

The same web/X article was captured, renamed, and re-committed at each pipeline stage: `feed/` (raw drop) → `04-SOURCES/` (research notebook) → `corpus/` (numeric ID). Each stage produced a file. When corpus was flattened to numeric IDs, multiple stages' outputs coexisted as separate numbered files.

**Nature**: Not sync errors — pipeline archaeology. Each copy is a fossilized stage of a linear process. The later copy is typically fuller (canonicalized SOURCE format with richer metadata). The earlier copy is often truncated or missing the `.md` extension.

### Mechanism 3: Double-Capture from Scraping (subset of 122)

The same article was scraped at different times, producing slightly different title renderings or truncation points. Example: "OpenClaw + MiniMax = The $14/Month AI Agent" captured as two files — one 464 lines, one 243 lines — with subtly different filenames (`minimax_the_14_month` vs `minimax_equals_the_$14_month`).

**Nature**: A pain signal. The ingestion pipeline had no deduplication gate — no URL-level or content-hash check to prevent re-ingestion of already-captured articles. The corpus absorbed whatever was dropped into `feed/`, including re-scrapes.

### Mechanism 4: Agent Task Broadcast Copies (small count)

The orchestrator broadcast identical task templates to multiple agents (e.g., health check sent to all 5 agents). Each agent's copy differed only in the `To:` and `Reply-To:` fields. All copies landed in corpus when operational artifacts were aggregated.

**Nature**: Not errors — the broadcast protocol working as designed. The repetition is structural: N agents × 1 broadcast = N near-identical files. The semantic content is identical; only the addressing differs.

### Mechanism 5: Race Condition Double-Claims (rare)

Two instances of the same agent (Mac mini + MacBook Air) both claimed an unclaimed task within seconds, each producing a `.complete` file. No distributed lock prevented concurrent claims.

**Nature**: An alarm bell. The auto-ingest system lacked mutex on task claiming. Both instances read the task as unclaimed and wrote competing completion records. Low frequency but a real concurrency bug.

### Mechanism 6: Sequential Compaction Snapshots (rare)

The `cc_handoff.sh` PreCompact hook fired twice within one minute during rapid-fire commits near the context limit, producing two handoff files timestamped one minute apart with slightly different git HEADs.

**Nature**: Not an error — legitimate versioned snapshots of a continuously evolving state. The later snapshot supersedes the earlier one. Both are valid; only the later one is needed.

### Summary

| Mechanism | Count | Nature | Signal |
|-----------|------:|--------|--------|
| Pipeline intermediates (Flat→Graphiti) | 773 | Precursor/cleaned pair, no cleanup step | Pipeline hygiene |
| Multi-stage ingestion copies | ~80 | Fossilized pipeline stages | Pipeline needs single-output |
| Double-capture scraping | ~20 | Same URL scraped twice | Missing dedup gate |
| Agent broadcast copies | ~15 | N agents × 1 broadcast | Structural, not a bug |
| Race condition claims | ~5 | Concurrency bug | Alarm bell — needs mutex |
| Sequential compaction | ~2 | Versioned snapshots | Expected behavior |

**Total removed (CC57)**: 889 files (773 JSONL + 116 near-dupes). Corpus: 11,733 → 5,954 (49.3% reduction).

---

## Subcategory Indexes (CC58)

Subcategories are implemented as **Ranganathan faceted indexes** — semantic routing tables overlaid on flat space. Files do not move. Filenames do not change. Each indexed folder contains a `SUBCATEGORY-INDEX.md` that maps numeric file IDs to sub-themes. A file can be cross-referenced from multiple indexes.

| Folder | Sub-themes |
|--------|-----------|
| **ai-models** (880) | Mathematical Foundations, Frontier Model Releases, Training & Scaling, Benchmarks & Evaluation, Architecture & Efficiency, Fine-Tuning & Adaptation |
| **multi-agent-systems** (762) | External MAS Research, Syncrescendence Operations, Orchestration Patterns, MCP & Protocol Engineering, Sub-Agent Delegation, Architecture & Frameworks |
| **claude-code** (576) | Core Architecture, Extended Thinking & Reasoning, MCP & Sub-Agent Integration, Customization & Skills, Community & Usage Patterns, Security & Isolation |
| **openclaw** (572) | Installation & Configuration, Memory & Personality, Phone & Multi-Device Fleets, Security & Cost Optimization, Operational Tooling, Ecosystem & Comparative Analysis |
| **ai-capability-futures** (448) | AGI Timelines & Predictions, Scaling Laws & Trajectories, Agent Evals & Capability Benchmarks, Market & Investment Analysis, Democratization & Open Models, Human-AI Symbiosis |

**Architecture**: Ranganathan faceted classification. Physical files are immutable numeric IDs. Subcategories exist only as index entries. Reclassification = editing one line in an index file, zero file I/O. Poly-hierarchical: liminal files can appear in multiple indexes.

**Formation principles**: Threshold of Distinction (sub-theme justified only if semantic distance from peers > internal variance), Asymmetric Density (follow Zipf's law, not forced equal distribution), no type-based sub-themes at any granularity level.

---

## Constitutional Constraints

1. **CLUSTERING BY TYPE IS FORBIDDEN.** Classification is by semantic topic of contents, always and only.
2. **No "other" / "general" / "uncategorized" buckets.** Every file earns its folder by topic.
3. **Nothing gets deleted** without Sovereign approval. Merge policy for near-dupes.
4. **philosophy-esoterica and meaning-civilization remain SEPARATE** (Sovereign ruling CC56).

## Teleology (Sovereign Directive CC56 — SEARED)

The corpus is becoming a textbook — a compendium to build the Syncrescendence.

We cluster progressively. Subcategories will form within folders. Metacategories will form across folders. We semantically tighten for maximal coherence. Every misclassification is a flaw in the canon. Every reclassification illuminates.

The end state is a navigable knowledge architecture where any reader can find any piece of the Syncrescendence vision by semantic topic, drill into subcategories for depth, and zoom out to metacategories for breadth.

---

*This document is the single classification authority for the corpus.*
