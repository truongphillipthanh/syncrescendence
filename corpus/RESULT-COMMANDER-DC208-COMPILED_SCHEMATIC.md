# DC-208: Compiled Source Mining Schematic — Oracle + Diviner → Adjudicator

**Compiled by**: Commander (Claude Opus 4.6)
**Date**: 2026-02-23
**Authority**: Sovereign directive — Phase 2C source mining
**Intel Sources**: Oracle DC-208 (thesis + industry consensus), Diviner DC-208 (scientific overlay + predictions)
**Purpose**: Unified engineering spec for Adjudicator to build the mining pipeline

---

## 1. Architecture Overview

**Oracle's frame**: Hierarchical agentic processing — triage, extract, batch, integrate, gate, assign.
**Diviner's reframe**: Not mining but **terraforming** — introducing intent (atmosphere) to raw corpus (sterile planet) to see what survives. Success metric is **metabolic rate** (how fast insight → action), not retrieval accuracy.

**Commander's synthesis**: Both are correct at different scales. The engineering is mining (mechanical, repeatable, measurable). The outcome is terraforming (emergent, living, metabolic). Build the mine; expect an ecosystem.

---

## 2. Convergence Matrix

| Component | Oracle (Engineering) | Diviner (Biology) | Convergence | Enhancement |
|---|---|---|---|---|
| **Triage** | Composite leverage score (targets 45%, centrality 25%, lineage 20%, domain 10%) | r/K selection — PARADIGM=K-selected (quality), long tail=r-selected (disruptive) | HIGH | **Stochastic wildfire**: randomly elevate 5% of lowest-ranked sources to prevent ecological trap (over-indexing on consensus) |
| **Extraction** | Atomic JSONL: claims, frameworks, predictions, concepts, analogies, praxis_hooks. 1:10 ratio | Enzymatic hydrolysis — risk of denaturation (stripping context kills the idea) | HIGH | **Chaperone metadata**: attach "tension vector" to every atom — not just where, but the hostile environment it was born in (rebuttal? hypothesis? consensus?) |
| **Batching** | K-means k=18, 4-6 sources/batch, 3-4 agents parallel, 8-10 inter-cluster waves | Fractional distillation — risk of azeotropy (concepts that can't be separated by clustering alone) | MEDIUM | **Pressure swing**: vary context window dynamically — shrink to fracture dense clusters, expand to find bridges in sparse ones |
| **Integration** | Engine→JSONL→memsync→Graphiti→praxis-first→canon. Dedup cosine <0.78, degree ≥3 | Long-term potentiation — risk of excitotoxicity (hallucinated connections, conspiracy-theory graph) | HIGH | **Synaptic pruning**: degrade untraversed connections after 30 days. Active forgetting is intelligence |
| **Quality Gate** | 4 gates: coverage, graph density ≥8, praxis validation ≥2 tests, Adjudicator rubric >0.88 | FEP: minimize surprise. Gate should weight surprise × precision | HIGH | **Surprise-weighted alerting**: High surprise + high precision = CRITICAL ALERT. High surprise + low precision = IGNORE |
| **Agent Assignment** | Oracle(triage+synthesis), Diviner(analogies+lineage), Adjudicator(gates), Scribe swarm(extraction) | Holobiont: Host(Sovereign) + Symbiont(Corpus). Metabolic rate as KPI | MEDIUM | **Negative knowledge logging**: agents must mark dead ends (Diviner's "pheromone of failure") |

---

## 3. Critical Enhancements from Diviner (for Adjudicator to engineer)

### 3A. Memetic Cladistics (Lineage Architecture)

Oracle proposes embedding-based lineage. Diviner proposes something deeper:

- **Vector subtraction for mutation detection**: If B cites A, compute `delta = embed(B) - embed(A)`. Low magnitude = carrier (replication). High + orthogonal = mutator (innovation).
- **Convergent evolution detector**: Find clusters that are semantically identical but temporally distinct with zero common ancestors = "universal truths" or attractors in latent space.
- **Homology vs homoplasy**: Distinguish shared ancestry (genuine influence) from convergent evolution (independent discovery).

**Adjudicator question**: Is this computationally tractable at 1,773 sources with all-MiniLM-L6-v2? What's the pairwise comparison cost?

### 3B. Cyclical Relevance Model (Antikythera Gearing)

Diviner proposes the corpus has cyclical relevance — the Sovereign oscillates between exploration mode (novelty-seeking) and execution mode (utility-seeking). The system should:
- Detect which gear the Sovereign is in (from recent prompt patterns, task types, time of day)
- Rotate the corpus presentation accordingly
- This is a model router concept applied to knowledge retrieval

**Adjudicator question**: Should this be a separate system or integrated into the model router (DC-147)?

### 3C. Retraction Mining (Negative Knowledge)

When an agent explores a path that fails, it leaves a "pheromone of failure" — a permanent negative marker that future agents can see. This prevents repeated exploration of dead ends.

**Adjudicator question**: What's the data structure for negative knowledge? A separate edge type in Graphiti? A metadata flag on nodes?

---

## 4. Diviner's Predictions (for Adjudicator validation design)

| # | Prediction | Implication | Validation Method |
|---|---|---|---|
| 1 | **Structural hole**: graph will reveal void between technical implementation and abstract philosophy — Sovereign is building a bridge between engineering and metaphysics | The unmined middle layer (systems theory applied to practice) is the Sovereign's original contribution | After first 50 sources mined, visualize graph — measure betweenness centrality of bridge nodes |
| 2 | **Semantic drift**: "Agent" means 3 different things across corpus (2023: wrapper, 2024: loop, 2025: multi-modal entity) — graph will collapse them | Need temporal-semantic axis to prevent logical contradictions | Build time-tagged concept disambiguation during extraction |
| 3 | **Hidden obsession**: 80% of "productivity" interest is actually control theory / cybernetics | Reclassify sources after mining — does the distribution confirm? | Post-mining tag analysis: compare declared vs. emergent categories |

---

## 5. Engineering Spec Summary (for Adjudicator)

### Pipeline Components to Build

| # | Component | Input | Output | Agent | Complexity |
|---|---|---|---|---|---|
| 1 | **Triage script** | DYN-SOURCES.csv + frontmatter YAML | Ranked list with leverage scores + dependency DAG | Commander | S |
| 2 | **Extraction template** | Single SOURCE-*.md | Atomic JSONL + companion MD (6 categories + chaperone metadata + tension vector) | Scribe swarm | M |
| 3 | **Cluster engine** | Embeddings of 319 PARADIGM sources | K-means clusters + intra-cluster assignments | Commander/Adjudicator | M |
| 4 | **Batch orchestrator** | Cluster assignments | Parallel agent dispatch (4-6 sources/batch) with memsync checkpoints | Commander | M |
| 5 | **Integration bridge** | Atomic JSONL | Graphiti nodes/edges with provenance, confidence, praxis_hooks | memsync daemon | S |
| 6 | **Quality gate** | Mined source + graph state | Pass/fail on 4 gates + surprise-weighted alert | Adjudicator | M |
| 7 | **Lineage engine** | All embeddings + citation graph | Innovation deltas, convergent evolution flags, phylogenetic tree | Diviner/Adjudicator | L |
| 8 | **Negative knowledge store** | Failed exploration paths | Pheromone-of-failure edges in Graphiti | All agents | S |
| 9 | **Cyclical relevance model** | Sovereign prompt patterns + task history | Gear detection (exploration/execution) + corpus rotation | Commander | M |

### Key Parameters

| Parameter | Oracle Value | Diviner Enhancement | Final Spec |
|---|---|---|---|
| Compression ratio | 1:10 | + tension vectors → ~1:8 effective | 1:8 to 1:10 (Adjudicator to calibrate) |
| Batch size | 4-6 sources | Pressure swing: adaptive 3-8 | 4-6 default, adaptive on dense/sparse clusters |
| Cluster count | k=18 | — | 18 (recalibrate after first wave) |
| Throughput target | 80-120/week | — | 80-120/week post-ramp |
| Canon dedup threshold | cosine <0.78 | — | 0.78 |
| Connection pruning | — | 30-day decay | 30-day half-life on untraversed edges |
| Wildfire percentage | — | 5% random elevation | 5% per batch |
| Quality gates | 4 (coverage, density, praxis, rubric) | + surprise weighting | 5 gates (add surprise × precision) |

---

## 6. Recommended Execution Order

1. **Triage script** (S) — immediate, unblocks everything
2. **Extraction template** (M) — defines the atomic format all agents use
3. **Integration bridge** (S) — memsync already exists, extend for new JSONL format
4. **Pilot: top 5 sources** — JRE Musk, Hoffman, Diamandis, Henrich, Walker
5. **Quality gate** (M) — validate pilot results before scaling
6. **Cluster engine + batch orchestrator** (M+M) — scale after pilot validates
7. **Lineage engine** (L) — build after first 50 sources provide enough graph data
8. **Negative knowledge + cyclical relevance** (S+M) — can be built in parallel with 6/7

All components feed into Graphiti via memsync. All gated by Phase 0 infrastructure (DONE).

---

*Compiled from Oracle DC-208 + Diviner DC-208. Next: dispatch to Adjudicator for hyper-technical engineering of the mining pipeline.*
