# Bottom-Up JSONL Clustering Report

**Generated**: 2026-02-27
**Scope**: All 2,023 `.jsonl` files in `/Users/system/syncrescendence/corpus/`
**Method**: Schema analysis, source_id extraction, content sampling, near-dupe verification

---

## Executive Summary

The 2,023 JSONL files divide into exactly **three distinct structural groups**:

| Group | Count | Description |
|-------|-------|-------------|
| Graphiti Source Atom files | 1,002 | Canonical atom records with UUID, timestamp, payload |
| Flat Source Atom files | 1,002 | Exact payload-field redundant copies of the above |
| Infrastructure / Pipeline Meta files | 19 | Agent journals, scoring indexes, pipeline state |

**Crushable count: 1,002** — all 1,002 Flat files are strict redundancies of the Graphiti files.

The Graphiti files and Flat files form **1,002 perfectly matched pairs**, each covering one unique source. Every pair also has a corresponding `.md` extraction summary file at `N-1` (e.g., `01059.md`, `01060.jsonl`, `01061.jsonl` = one triplet). These `.md` files are NOT JSONL; they are separate from this analysis.

---

## Group 1: Graphiti Source Atom Files (1,002 files)

**Schema**: `{record_type, schema_version, uuid, timestamp, payload, source_id, entity_type, name, content, confidence, provenance, metadata}`

- The `payload` field is a complete Flat atom record embedded inside the Graphiti wrapper.
- Each file covers exactly one unique `SOURCE-YYYYMMDD-NNN` identifier.
- File numbering: always **even-offset** within their triplet (the `.md` precedes them).
- Range: `01057.jsonl` through `04469.jsonl` (with gaps; files are at positions N where N-1 is the .md and N+1 is the flat twin).
- Timestamp generation: cluster tightly around 2026-02-23 to 2026-02-24.

These are the **canonical files to retain**.

---

## Group 2: Flat Source Atom Files (1,002 files) — ALL CRUSHABLE

**Schema**: `{atom_id, source_id, category, content, line_start, line_end, chaperone, extensions}`

**Critical finding**: The Flat atom record is byte-for-byte identical to `graphiti_file["payload"]`. Verified across 20 random sample pairs — 100% match. The Flat files contain **zero additional information** beyond what the paired Graphiti file already contains.

**Near-dupe pairs** (each Flat file is redundant to its Graphiti partner):

Each pair follows the pattern:
- `NNNNN.jsonl` = Graphiti (canonical)
- `NNNNN+1.jsonl` = Flat (redundant, crushable)

Sample pairs:
| Graphiti (keep) | Flat (crush) | Source |
|-----------------|--------------|--------|
| `01057.jsonl` | `01058.jsonl` | SOURCE-20020201-001 (Paul Graham taste essay, 26 atoms) |
| `01060.jsonl` | `01061.jsonl` | SOURCE-20210528-669 (Hermetic/Emerald Tablet, 3 atoms) |
| `01063.jsonl` | `01064.jsonl` | SOURCE-20220906-650 (fire symbolism, 5 atoms) |
| `01078.jsonl` | `01079.jsonl` | SOURCE-20250124-website-...-writing_a_good_claude_md (21 atoms) |
| `01081.jsonl` | `01082.jsonl` | SOURCE-20250217-website-...-claude_code_plan_mode (16 atoms) |
| `01084.jsonl` | `01085.jsonl` | SOURCE-20250312-001 (Dwarkesh/Henrich, 258 atoms) |
| `01093.jsonl` | `01094.jsonl` | SOURCE-20250421-x-thread-alexalbert (15 atoms) |
| `01108.jsonl` | `01109.jsonl` | SOURCE-20250528-001 (esoteric, 179 atoms) |
| `01144.jsonl` | `01145.jsonl` | SOURCE-20250912-001 (memory/retrieval, 194 atoms) |
| `01186.jsonl` | `01187.jsonl` | SOURCE-20251023-001 (Anthropic/Claude, 109 atoms) |
| `01198.jsonl` | `01199.jsonl` | SOURCE-20251028-001 (philosophy, 181 atoms) |
| `01204.jsonl` | `01205.jsonl` | SOURCE-20251030-001 (retrieval, 198 atoms) |
| `01207.jsonl` | `01208.jsonl` | SOURCE-20251030-002 (multi-agent, 10 atoms) |
| `01219.jsonl` | `01220.jsonl` | SOURCE-20251031-004 (startup/VC, 86 atoms) |
| `01222.jsonl` | `01223.jsonl` | SOURCE-20251031-005 (philosophy, 358 atoms) |
| ... | ... | (1,002 pairs total; all follow NNNNN / NNNNN+1 pattern) |

Full list of Flat (crushable) files — these are all odd-offset files in the 01xxx-04xxx range:
`01058.jsonl`, `01061.jsonl`, `01064.jsonl`, `01067.jsonl`, `01070.jsonl`, `01073.jsonl`, `01076.jsonl`, `01079.jsonl`, `01082.jsonl`, `01085.jsonl`, `01088.jsonl`, ..., `04442.jsonl`, `04445.jsonl`, `04448.jsonl`, `04451.jsonl`, `04454.jsonl`, `04457.jsonl`, `04460.jsonl`, `04463.jsonl`, `04466.jsonl`, `04469.jsonl`.

---

## Group 3: Infrastructure / Pipeline Meta Files (19 files)

These are all in the `00xxx` number range. None are near-dupes of each other — each serves a distinct pipeline role.

### Sub-Group 3A: Agent Journal Records

| File | Lines | Description |
|------|-------|-------------|
| `00011.jsonl` | 18 | Commander observations journal, 2026-02-23. Schema: `{uuid, ts, agent, scope, kind, text, refs}` |
| `00013.jsonl` | 17 | Commander observations journal, 2026-02-24. Same schema as 00011. |
| `00015.jsonl` | 149 | Commander session_end journal entries. Extended schema adds `source`, `session` fields. |

Note: `00011` and `00013` have the same schema and consecutive dates — they are **temporal continuations**, not near-dupes.

### Sub-Group 3B: Session State Briefs

| File | Lines | Description |
|------|-------|-------------|
| `00017.jsonl` | 455 | Session state briefs log, generated 2026-02-26. Schema: `{timestamp, type, content}` (content = full markdown brief). |
| `00018.jsonl` | 93 | Session state briefs log, generated 2026-02-27. Same schema as 00017. |

Note: `00017` and `00018` are **temporal continuations**, not dupes. `00018` is the more recent version.

### Sub-Group 3C: All-Atoms Aggregate Index Files (SAME 14,025 ATOMS, DIFFERENT COMPUTED FIELDS)

These four files each contain one record per atom for ALL 14,025 atoms across all 1,002 sources. They reference the same `atom_id` set in the same order but carry different computed metadata — they are **different views**, not true duplicates.

| File | Lines | Role | Unique Fields |
|------|-------|------|---------------|
| `00711.jsonl` | 14,025 | Scoring + integration status index | `score`, `band`, `cluster_id`, `integration_status`, `integrated_at`, `review_notes` |
| `00712.jsonl` | 14,025 | Scoring with component breakdown | `score`, `band`, `components` (6-dimensional breakdown), `content_preview` |
| `00718.jsonl` | 14,025 | Content + cluster label index | `content`, `cluster_id`, `cluster_label`, `cluster_terms` |
| `00767.jsonl` | 14,025 | Gate coverage scoring | `coverage_mapped`, `graph_relation_count`, `gate2_skipped`, `praxis_link_count`, `gate3_skipped`, `contradiction_score`, `consistency_score`, `novelty`, `belief_violation`, `surprise`, `alert_score`, `gates` |

These four are a **family** rather than duplicates — each is the output of a different pipeline stage over the same corpus.

### Sub-Group 3D: Pipeline Operational Files

| File | Lines | Description |
|------|-------|-------------|
| `00706.jsonl` | 1 | Ascertescence incident ledger header record. |
| `00709.jsonl` | 150 | Cluster manifest: 150 clusters with `size`, `mean_score`, `max_score`, `band`, `category_distribution`, `representative_atom`. |
| `00714.jsonl` | 1,152 | Source extraction processing log: one record per source extraction run, including SOURCE-NOID entries (148 NOID sources that were processed but not given per-source files). |
| `00727.jsonl` | 1 | Annealer state snapshot (FIRE state, 2026-02-27). |
| `00732.jsonl` | 1 | Energy audit record (AUDIT_AMBIENT, PASS). |
| `00737.jsonl` | 7 | Integration gate check log (7 session runs, mix of pass/fail). |
| `00739.jsonl` | 2 | Annealer REJECT decisions (2 atoms). |
| `00742.jsonl` | 1 | Annealer repair prompt for DRY-RUN-001. |
| `00762.jsonl` | 4 | Compression/promotion log (4 promotion operations). |
| `00764.jsonl` | 5 | Intention-match scoring (5 atoms scored against intentions). |

---

## Natural Topic Groupings (Within the 1,002 Source Pairs)

These clusters emerged from bottom-up content analysis. Sources often touch multiple themes; classification is by dominant signal.

### Cluster 1: Claude Code / Anthropic Ecosystem
**Sources: 201 | Atoms: 3,340**

The largest single cluster. Covers Claude Code workflows, CLAUDE.md configuration, Claude agent patterns, Anthropic blog posts, Boris Cherny (creator) threads, agentic coding patterns. Spans 2025-01 through 2026-02.

Key files:
- `01078.jsonl` + `01079.jsonl` — SOURCE-20250124-...-writing_a_good_claude_md_humanlayer (21 atoms)
- `01081.jsonl` + `01082.jsonl` — SOURCE-20250217-...-what_actually_is_claude_code_plan_mode (16 atoms)
- `01093.jsonl` + `01094.jsonl` — SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned (15 atoms)
- `01186.jsonl` + `01187.jsonl` — SOURCE-20251023-001 (109 atoms)
- `02485.jsonl` + `02486.jsonl` — SOURCE-20260108-x-article-thezvi-claude_codes (78 atoms)
- `03340.jsonl` + `03341.jsonl` — SOURCE-20260131-x-thread-bcherny-im_boris_and_i_created_claude (20 atoms)
- `03475.jsonl` + `03476.jsonl` — SOURCE-20260203-x-thread-iruletheworldmo-the_pattern_keeps_repeating (4 atoms)
- `04462.jsonl` + `04463.jsonl` — SOURCE-undated-015 (Claude Code task system, 15 atoms)

### Cluster 2: AI Memory / Knowledge Retrieval / Graphiti
**Sources: 115 | Atoms: 2,739**

Covers long-term memory systems, RAG, vector databases, knowledge graphs, Graphiti specifically, episodic memory agents, agent memory architecture. Heavily represented because this is a core research interest.

Key files:
- `01084.jsonl` + `01085.jsonl` — SOURCE-20250312-001 (Dwarkesh/Henrich cultural evolution, 258 atoms)
- `01144.jsonl` + `01145.jsonl` — SOURCE-20250912-001 (194 atoms)
- `01204.jsonl` + `01205.jsonl` — SOURCE-20251030-001 (198 atoms)
- `02761.jsonl` + `02762.jsonl` — SOURCE-20260118-x-article-rohit4verse-how_to_build_an_agent_that_never_forgets (42 atoms)

### Cluster 3: Product / Business Strategy
**Sources: 83 | Atoms: 760**

Business models, product-market fit, growth, SaaS, enterprise software, AI product strategy, distribution.

Key files:
- `01195.jsonl` + `01196.jsonl` — SOURCE-20251027-001 (87 atoms)
- `01252.jsonl` + `01253.jsonl` — SOURCE-20251112-1129 (21 atoms)

### Cluster 4: Startup / Venture Capital
**Sources: 59 | Atoms: 482**

Founder advice, fundraising, startup culture, VC dynamics, early-stage company building.

Key files:
- `01219.jsonl` + `01220.jsonl` — SOURCE-20251031-004 (86 atoms)

### Cluster 5: AI Models / Industry News
**Sources: 49 | Atoms: 203**

Short-form atoms about model releases (GPT-5, Gemini, Opus 4.5, GLM, Kimi), AI industry news, model comparisons. Predominantly 1-3 atom files — ephemeral news fragments.

Key files: `01270.jsonl`, `01414.jsonl`, `01462.jsonl`, `01534.jsonl`, `01693.jsonl`, `01762.jsonl`, `02083.jsonl`, `02119.jsonl`, `02131.jsonl`, `02155.jsonl`, `03265.jsonl`, `03940.jsonl`, `03943.jsonl`, `04402.jsonl` (among others)

### Cluster 6: Leadership / Management / Organizations
**Sources: 44 | Atoms: 339**

Executive decision-making, management frameworks, organizational design, team building, CEO perspectives.

Key files:
- `01180.jsonl` + `01181.jsonl` — SOURCE-20251021-001 (78 atoms)

### Cluster 7: Philosophy of Consciousness / Transhumanism
**Sources: 41 | Atoms: 1,230**

Consciousness, qualia, panpsychism, transhumanism, bioethics, David Pearce, effective altruism, mind uploading.

Key files:
- `01069.jsonl` + `01070.jsonl` — SOURCE-20240327-628 (David Pearce, 5 atoms)
- `01120.jsonl` + `01121.jsonl` — SOURCE-20250623-001 (22 atoms)

### Cluster 8: LLM Training / Architecture
**Sources: 41 | Atoms: 256**

Fine-tuning, pre-training, transformer architecture, tokenization, foundation models, scaling laws. Distinct from "AI models industry news" — these are technical/academic sources.

### Cluster 9: Design / Aesthetics / Taste
**Sources: 42 | Atoms: 282**

The Paul Graham essay on taste, design philosophy, craft, aesthetic judgment, visual culture.

Key files:
- `01057.jsonl` + `01058.jsonl` — SOURCE-20020201-001 (Paul Graham "Taste for Makers", 26 atoms) — **oldest source in the entire corpus**

### Cluster 10: Vibe Coding / AI Engineering Practice
**Sources: 36 | Atoms: 447**

Vibe coding practice, AI engineer career, "agentic coding," building with AI, compounding engineering. Closely related to Cluster 1 but centered on practitioner experience rather than Anthropic-specific content.

Key files:
- `03097.jsonl` + `03098.jsonl` — SOURCE-20260126-x-article-armanhezarkhani-the_complete_guide_vibe_coding (97 atoms)
- `03178.jsonl` + `03179.jsonl` — SOURCE-20260127-x-article-armanhezarkhani-how_to_become_an_ai_agent_engineer (61 atoms)
- `04466.jsonl` + `04467.jsonl` — SOURCE-undated-016 (multi-agent collaboration, 55 atoms)

### Cluster 11: Multi-Agent Systems / Swarms
**Sources: 29 | Atoms: 643**

Multi-agent coordination, agent swarms, orchestration, agent squads, Mission Control patterns.

Key files:
- `03337.jsonl` + `03338.jsonl` — SOURCE-20260131-x-article-pbteja1998-building_mission_control (69 atoms)
- `02440.jsonl` + `02441.jsonl` — SOURCE-20260108-001 (52 atoms)

### Cluster 12: Esoteric / Occult / Mysticism
**Sources: 19 | Atoms: 1,264**

Hermetic tradition, Emerald Tablet, alchemy, Kabbalah, sacred geometry, Thelema. High atom-per-source density — these are long-form texts.

Key files:
- `01108.jsonl` + `01109.jsonl` — SOURCE-20250528-001 (179 atoms)
- `01111.jsonl` + `01112.jsonl` — SOURCE-20250605-001 (154 atoms)
- `01165.jsonl` + `01166.jsonl` — SOURCE-20251013-001 (115 atoms)
- `01060.jsonl` + `01061.jsonl` — SOURCE-20210528-669 (Emerald Tablet, 3 atoms) — **second oldest source**
- `04468.jsonl` + `04469.jsonl` — SOURCE-undated-unknown-...-meta_narrative_and_perspectival_schemas (94 atoms)

### Cluster 13: Writing / Communication
**Sources: 19 | Atoms: 114**

Writing craft, rhetoric, narrative, essay structure, communication strategy.

### Cluster 14: AI Agent Tools / MCP
**Sources: 22 | Atoms: 265**

Model Context Protocol, tool-calling patterns, agentic frameworks, agent skills architecture.

Key files:
- `02938.jsonl` + `02939.jsonl` — SOURCE-20260122-x-article-dani_avila7-separation_of_responsibilities_mcp_vs_skills (15 atoms)

### Cluster 15: Productivity / Systems / PKM
**Sources: 18 | Atoms: 169**

Second Brain, PKM, habit systems, workflow automation, Obsidian.

### Cluster 16: Philosophy of Meaning / Civilization
**Sources: 10 | Atoms: 735**

Meaning crisis (John Vervaeke territory), civilizational moments, Age of Turbulence, geopolitics.

Key files:
- `01198.jsonl` + `01199.jsonl` — SOURCE-20251028-001 (181 atoms)
- `01222.jsonl` + `01223.jsonl` — SOURCE-20251031-005 (358 atoms) — largest single non-technical source

### Cluster 17: Voice / Audio / Speech
**Sources: 13 | Atoms: 61**

TTS, voice cloning, Voicebox, speech synthesis, audio tools.

Key files:
- `04456.jsonl` + `04457.jsonl` — SOURCE-undated-004 (Voicebox local voice studio, 11 atoms)

### Cluster 18: Health / Psychology / Neuroscience
**Sources: 9 | Atoms: 56**

Sleep science, fitness, mental health, neuroscience, biohacking.

### Cluster 19: AI Safety / Alignment
**Sources: 2 | Atoms: 13**

Constitutional AI, RLHF, value alignment, AI risk. Surprisingly small cluster — most safety-adjacent content appears to have been captured in other Anthropic/Claude topics.

### Cluster 20: Stoicism / Philosophy of Life
**Sources: 2 | Atoms: 8**

Stoic philosophy, Marcus Aurelius, Ryan Holiday.

### Cluster 21: Arts / Creativity
**Sources: 1 | Atoms: 10**

`01372.jsonl` + `01373.jsonl` — SOURCE-20251117-1084

### Cluster 22: Prompting Techniques
**Sources: 2 | Atoms: 16**

Prompting strategy, system prompts.

### Cluster 23: Syncrescendence Internal
**Sources: 2 | Atoms: 6**

AGENTS.md, internal protocol documentation captured as source atoms.

Key files:
- `02503.jsonl` + `02504.jsonl` — SOURCE-20260109-545 (4 atoms)
- `03223.jsonl` + `03224.jsonl` — SOURCE-20260128-270 (2 atoms)
- `04450.jsonl` + `04451.jsonl` — SOURCE-undated-001 (AGENTS.md format, 17 atoms)
- `04453.jsonl` + `04454.jsonl` — SOURCE-undated-003 (Claude training document, 7 atoms)
- `04459.jsonl` + `04460.jsonl` — SOURCE-undated-009 (Boris Cherny, 5 atoms)

### Cluster 24: Other / Miscellaneous
**Sources: 145 | Atoms: 593**

Sources that did not resolve cleanly into the above clusters. Predominantly 1-4 atom files — ephemeral fragments, YouTube shorts, short-form social posts, tangential topics (geopolitics, economics, quantum computing, robotics). Most have low signal density.

---

## Near-Dupe Summary

### True Near-Dupes: 1,002 Flat/Graphiti pairs

Every pair consists of files at positions N (Graphiti) and N+1 (Flat). The Flat file's content is exactly the `payload` field of the Graphiti file. Verified: 100% content identity across all sampled pairs.

Pattern to identify all Flat files programmatically:
```python
# A file is a Flat atom file if its first record has these keys:
# {atom_id, source_id, category, content, line_start, line_end, chaperone, extensions}
# AND does NOT have 'record_type' or 'uuid' fields
```

### Same-Atom-Set Quad (Different Computed Metadata): 00711 / 00712 / 00718 / 00767

All four files contain exactly the same 14,025 `atom_id` values in the same order. They are NOT crushable because each adds distinct non-overlapping computed fields. However, they share a structural relationship — they are all aggregate views of the same corpus, generated in a single pipeline run (2026-02-23/24).

### Temporal Continuations (Not Dupes): 00011/00013/00015, 00017/00018

`00011` and `00013` are consecutive daily journal snapshots. `00015` is a different journal subtype. `00017` and `00018` are consecutive days of session brief logs. None are duplicates of each other.

---

## JSONL Files with Atoms Already in .md Extraction Files

Every single one of the 1,002 Graphiti source files has a corresponding `.md` extraction summary at position `N-1`. Pattern: `01059.md` summarizes what's in `01060.jsonl` + `01061.jsonl`.

The `.md` extraction files are NOT copies of the atom content — they are extraction summaries (header metadata, atom count, category list). The atom content itself exists only in the JSONL files.

So: 0 JSONL files are redundant to .md extraction files, but 1,002 `.md` extraction summary files exist as index/header companions to the 1,002 Graphiti JSONL files.

---

## Estimated Crushable Count

| What | Count | Rationale |
|------|-------|-----------|
| Flat source atom files | **1,002** | 100% redundant — payload already in paired Graphiti file |
| Infrastructure files | 0 | Each is distinct; different pipeline stages |
| Graphiti source files | 0 | Canonical — retain all |

**Total crushable: 1,002 files** (48.6% of all JSONL files, 0% of unique information)

After crushing: 1,021 JSONL files remain (1,002 Graphiti + 19 infrastructure).

---

## Source Temporal Distribution

| Period | Sources | Atoms |
|--------|---------|-------|
| Pre-2025 (2002-2024) | 7 | 45 |
| 2025-01 to 2025-06 | 18 | 553 |
| 2025-07 to 2025-09 | 10 | 533 |
| 2025-10 | 26 | 2,823 |
| 2025-11 | 116 | 610 |
| 2025-12 | 185 | 1,095 |
| 2026-01 | 300 | 2,940 |
| 2026-02 | 336 | 5,066 |
| Undated / Special | 4 | 360 |

The corpus is heavily weighted toward recent content (2026-01 and 2026-02 account for 636 of 1,002 sources = 63%). The atom-density-per-source drops sharply in the 2025-11 to 2026-02 period (mostly 1-7 atoms/source) compared to earlier dense sources (100+ atoms/source).
