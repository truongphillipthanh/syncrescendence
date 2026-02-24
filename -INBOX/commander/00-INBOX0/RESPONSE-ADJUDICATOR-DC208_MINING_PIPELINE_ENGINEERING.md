---
agent: adjudicator
council: DC-208
topic: DC-208 Mining Pipeline Engineering — full component blueprint (triage, extract, bridge, promote)
status: unprocessed
collected: 2026-02-23
---

# Adjudicator: DC-208 Mining Pipeline Engineering

## Baseline Context
- Corpus observed in repo: `1773` `SOURCE-*.md` files, `233,213` total lines.
- Existing infra already present: `orchestration/scripts/memsync_daemon.py`, `orchestration/scripts/journal_append.sh`, `orchestration/00-ORCHESTRATION/scripts/dispatch.sh`.
- Source metadata reality to design for:
- `33` source files do not start with YAML frontmatter (they begin with `has_transcript: yes`), so parser cannot assume frontmatter starts at byte 0.
- `DYN-SOURCES.csv` has `150` rows with blank `signal_tier` and other blank fields, so triage must include null-safe defaults.

## Component 1: Triage Script — BUILD
### Feasibility: 9/10
### Blueprint
- Decision:
- Use Python, not bash. Reason: YAML parsing, embedding batches, DAG generation, and null-safe scoring are stateful and error-prone in shell.
- Embedding model:
- Primary local: `all-MiniLM-L6-v2` (already used in `orchestration/00-ORCHESTRATION/scripts/chroma_server.py`).
- Fallback API: `text-embedding-3-small` only when local model unavailable.
- New files:
- `orchestration/00-ORCHESTRATION/scripts/source_triage.py`
- `orchestration/00-ORCHESTRATION/scripts/source_triage_config.yaml`
- `sources/04-SOURCES/_meta/DYN-SOURCE_TRIAGE.json`
- `sources/04-SOURCES/_meta/DYN-SOURCE_DEPENDENCY_DAG.json`
- `sources/04-SOURCES/_meta/DYN-SOURCE_DEPENDENCY_DAG.mmd`
- Functions:
- `load_dyn_sources_csv(path) -> list[SourceRow]`
- `scan_source_frontmatter(paths) -> dict[source_id, Frontmatter]`
- `compute_embedding_centrality(records, model) -> dict[source_id, float]`
- `compute_lineage_potential(records) -> dict[source_id, float]`
- `score_source(record, weights) -> ScoreBreakdown`
- `build_dependency_dag(records) -> Dag`
- `persist_triage_outputs(scores, dag) -> None`
- Data structures:
- `SourceRecord`: `{source_id, filename, signal_tier, status, topics, integration_targets, key_insights, published_date, transcript_chars}`
- `ScoreBreakdown`: `{source_id, total, target_density, centrality, lineage, domain_priority, wildfire_promoted}`
- `DagEdge`: `{from_source_id, to_source_id, edge_type, confidence}`
- CLI:
- `python3 orchestration/00-ORCHESTRATION/scripts/source_triage.py --csv sources/04-SOURCES/_meta/DYN-SOURCES.csv --sources-dir sources/04-SOURCES --mode paradigm --top-k 50 --wildfire-pct 0.05 --out-prefix sources/04-SOURCES/_meta/DYN-SOURCE`
- Parsing strategy for 1,773 frontmatter files:
- Single-process parse is already tractable, but implement `ThreadPoolExecutor` (8 workers).
- Parse first YAML block found in first 4KB, not only at file start.
- Cache parsed metadata in `DYN-SOURCE_TRIAGE.json` with file mtime hash.
- DAG format:
- Canonical machine output: JSON adjacency list (`nodes`, `edges`, attributes).
- Human visualization output: Mermaid (`flowchart LR`) sidecar.

### Failure Modes
- YAML inconsistencies break parse.
- Detect: parse exceptions with filename counters.
- Recover: soft-fail record, mark `parse_error=true`, continue.
- Centrality distortion from noisy transcript chunks.
- Detect: high leverage rank with empty `key_insights`.
- Recover: centrality uses weighted mix of `title + key_insights + synopsis` only.
- Overfitting to existing canon.
- Detect: top-N too homogeneous by topic.
- Recover: keep 5% wildfire promotion and topic-diversity constraint.

### Dependencies
- Python 3.10+
- `PyYAML`, `sentence-transformers`, `numpy`, `networkx` (optional for DAG checks)

### Estimate
- 520-680 LOC
- Complexity: M

---

## Component 2: Extraction Template — BUILD
### Feasibility: 8/10
### Blueprint
- Decision on schema scope:
- The 6 categories are sufficient as first-class fields.
- Do not add more top-level categories now; add `extensions` object for future fields.
- Chaperone metadata implementation:
- Add to every atom:
- `chaperone.context_type`: `hypothesis|rebuttal|consensus|speculation|anecdote|method`
- `chaperone.argument_role`: `claim|evidence|counterevidence|limitation`
- `chaperone.tension_vector`: fixed 6-dim float vector in `[0,1]`
- `novelty`, `consensus_pressure`, `contradiction_load`, `speculation_risk`, `actionability`, `epistemic_stability`
- `chaperone.opposes_atom_ids`: list of conflicting atom IDs
- New files:
- `engine/02-ENGINE/PROMPT-SOURCE_EXTRACTION_ATOMIC.md`
- `orchestration/00-ORCHESTRATION/scripts/source_extract.py`
- `orchestration/00-ORCHESTRATION/scripts/source_extract_validate.py`
- Output convention per source:
- `sources/04-SOURCES/_meta/EXTRACT-<SOURCE_ID>.jsonl`
- `sources/04-SOURCES/_meta/EXTRACT-<SOURCE_ID>.md`
- Functions:
- `chunk_source_with_overlap(text, max_tokens, overlap_tokens) -> list[Chunk]`
- `extract_atoms_from_chunk(chunk, prompt) -> list[Atom]`
- `merge_and_dedup_atoms(atoms) -> list[Atom]`
- `attach_chaperone_metadata(atom, local_context) -> Atom`
- `validate_atom_schema(atom) -> ValidationResult`
- CLI:
- `python3 orchestration/00-ORCHESTRATION/scripts/source_extract.py --source sources/04-SOURCES/SOURCE-...md --max-chunk-tokens 1800 --overlap 220 --target-compression 0.1 --out-dir sources/04-SOURCES/_meta`
- Large-source (>5000 lines) handling:
- Two-pass map-reduce extraction.
- Pass 1: chunk-level atoms with strict provenance spans (`line_start`, `line_end`).
- Pass 2: consolidation model merges duplicates/conflicts and preserves provenance lineage.

### Failure Modes
- Denaturation/context loss.
- Detect: atom has claim but no `argument_role` and no counterpoint.
- Recover: reject atom in validator.
- Overspecified schema slows throughput.
- Detect: extraction latency > threshold; atom reject rate >15%.
- Recover: keep required fields minimal, move optionals to `extensions`.
- Context-window overflow on long transcripts.
- Detect: token overflow errors.
- Recover: deterministic chunking and resumable extraction by chunk index.

### Dependencies
- Python 3.10+
- `jsonschema`, tokenizer package (`tiktoken` or equivalent), optional LLM client

### Estimate
- 430-590 LOC
- Complexity: M

---

## Component 3: Cluster Engine — REDESIGN
### Feasibility: 7/10
### Blueprint
- Decision on algorithm:
- Pure K-means `k=18` is operationally convenient but not semantically robust.
- Recommended hybrid:
- Stage A: HDBSCAN to find natural dense regions + outliers.
- Stage B: constrained K-means to produce exactly 18 operational clusters for batch orchestration.
- Embedding model at 26MB corpus:
- Local inference is sufficient.
- Use `all-MiniLM-L6-v2` for continuity, or `bge-small-en-v1.5` if better separation is observed in pilot.
- New files:
- `orchestration/00-ORCHESTRATION/scripts/source_cluster.py`
- `orchestration/00-ORCHESTRATION/scripts/source_cluster_eval.py`
- `sources/04-SOURCES/_meta/DYN-SOURCE_CLUSTERS.json`
- `sources/04-SOURCES/_meta/DYN-SOURCE_CLUSTERS.mmd`
- Functions:
- `build_cluster_corpus(records) -> list[Doc]`
- `embed_docs(docs, model) -> np.ndarray`
- `fit_hdbscan(embeddings) -> ClusterLabels`
- `fit_operational_kmeans(embeddings, k=18, seed_labels=...) -> ClusterLabels`
- `detect_azeotropy(records, embeddings, labels) -> list[AzeotropePair]`
- Azeotropy handling:
- Keep a second assignment table (`secondary_cluster_id`) for high-ambiguity documents.
- Emit `azeotrope_edges` where two concepts remain inseparable under multiple parameter sweeps.
- CLI:
- `python3 orchestration/00-ORCHESTRATION/scripts/source_cluster.py --triage-json sources/04-SOURCES/_meta/DYN-SOURCE_TRIAGE.json --mode paradigm --k 18 --out sources/04-SOURCES/_meta/DYN-SOURCE_CLUSTERS.json`

### Failure Modes
- Forced `k=18` merges distinct concepts.
- Detect: low silhouette + high intra-cluster contradiction.
- Recover: hybrid plus secondary assignment.
- Sparse clusters starve batches.
- Detect: many clusters with <3 sources.
- Recover: pressure-swing rebalance window + merge tiny clusters.
- Over-clustering by recency events.
- Detect: cluster dominated by single week source dates.
- Recover: temporal regularization term.

### Dependencies
- `numpy`, `scikit-learn`, `hdbscan`, optional `umap-learn`

### Estimate
- 560-760 LOC
- Complexity: M/L

---

## Component 4: Batch Orchestrator — BUILD
### Feasibility: 8/10
### Blueprint
- New files:
- `orchestration/00-ORCHESTRATION/scripts/source_batch_orchestrator.py`
- `sources/04-SOURCES/_meta/DYN-BATCH_PLAN.json`
- `sources/04-SOURCES/_meta/DYN-BATCH_CHECKPOINTS.jsonl`
- Integration point:
- Calls existing `orchestration/00-ORCHESTRATION/scripts/dispatch.sh` to create task packets per batch.
- Functions:
- `materialize_batches(cluster_map, min_size=4, max_size=6) -> list[Batch]`
- `enqueue_batch_tasks(batches, target_agent) -> list[DispatchReceipt]`
- `checkpoint_batch_progress(batch_id, status, artifacts) -> None`
- CLI:
- `python3 orchestration/00-ORCHESTRATION/scripts/source_batch_orchestrator.py --clusters sources/04-SOURCES/_meta/DYN-SOURCE_CLUSTERS.json --batch-size 4:6 --max-concurrency 4 --agent adjudicator`

### Failure Modes
- Batch starvation when one cluster has too many long files.
- Recover with workload-aware split by estimated token budget.
- Dispatch flood overwhelms shared quota.
- Recover with token-budgeted scheduler and concurrency cap.

### Dependencies
- Components 1-3 outputs
- Existing dispatch + auto_ingest loop

### Estimate
- 300-420 LOC
- Complexity: M

---

## Component 5: Integration Bridge — BUILD
### Feasibility: 8/10
### Blueprint
- Current anchor:
- Extend existing `orchestration/scripts/memsync_daemon.py` (already posting journal JSONL to Graphiti).
- JSONL schema extension (backward-compatible):
- Keep current memory records unchanged.
- Add `record_type` and `payload` for source atoms:
- `record_type`: `memory_event|source_atom|source_relation|quality_gate|failure_pheromone|lineage_event`
- `payload`: typed object depending on `record_type`
- New/updated files:
- `orchestration/scripts/memsync_daemon.py` (extend parser/router/retry)
- `orchestration/scripts/memsync_schema.py` (record validators)
- `orchestration/state/memsync_retry.sqlite` (durable retry queue)
- `orchestration/state/DYN-MEMSYNC_DLQ.jsonl` (dead-letter)
- Mapping atomic extraction to Graphiti entities/relations:
- Entity nodes: `Source`, `Claim`, `Framework`, `Prediction`, `Concept`, `PraxisHook`
- Edges: `ASSERTS`, `SUPPORTS`, `CONTRADICTS`, `DERIVED_FROM`, `MENTIONS`, `TESTED_BY`
- Every edge stores `provenance:{source_id,line_start,line_end,atom_id}`
- Retry queue design when Graphiti is down:
- Durable queue with fields `{idempotency_key, payload, attempts, next_attempt_at, last_error, created_at}`
- Backoff: exponential with jitter (e.g., 5s, 15s, 45s, 135s… max 30m)
- Dead-letter after `N=10` failures, surfaced in health report.
- CLI:
- `python3 orchestration/scripts/memsync_daemon.py --once --graphiti-base http://localhost:8001 --repo-root .`
- `python3 orchestration/scripts/memsync_daemon.py --drain-retry --max-attempts 200`

### Failure Modes
- Graphiti outage causes silent loss.
- Fix: durable queue + DLQ + metrics.
- Duplicate writes from retries.
- Fix: deterministic `idempotency_key = sha256(record_uuid + relation_type + target_id)`.
- Schema drift between extractor and memsync.
- Fix: strict schema version field (`schema_version`).

### Dependencies
- Component 2 extraction outputs
- Graphiti API availability
- SQLite

### Estimate
- 380-540 LOC
- Complexity: M

---

## Component 6: Quality Gate — BUILD
### Feasibility: 7/10
### Blueprint
- New files:
- `orchestration/00-ORCHESTRATION/scripts/source_quality_gate.py`
- `orchestration/00-ORCHESTRATION/scripts/source_quality_metrics.py`
- `sources/04-SOURCES/_meta/DYN-QUALITY_GATE_RESULTS.jsonl`
- `sources/04-SOURCES/_meta/DYN-QUALITY_ALERTS.md`
- 4+1 gate automation:
- Gate 1 Coverage: key insights mapped to at least one extracted atom.
- Gate 2 Graph density: >=8 bidirectional relations from source atoms.
- Gate 3 Praxis: >=2 successful test artifacts linked.
- Gate 4 Logical consistency: contradiction score <=0.12 (equiv. >=0.88 consistency).
- Gate 5 Surprise x Precision score.
- Surprise x Precision concrete formula:
- `surprise = 0.6 * novelty + 0.4 * belief_violation`
- `novelty = 1 - max_cosine(atom_embedding, canon_neighbor_embeddings)`
- `belief_violation = contradiction_probability_against_local_subgraph`
- `precision = 0.35 * evidence_coverage + 0.25 * source_reliability + 0.25 * cross_source_support + 0.15 * falsifiability_score`
- `alert_score = surprise * precision`
- Alert bands:
- `>=0.55`: CRITICAL
- `0.35-0.55`: REVIEW
- `<0.35`: IGNORE
- Is 0.88 calibratable:
- Yes. Treat as initial prior. Calibrate on first 50 mined sources against adjudicator labels; recompute threshold from ROC/F1 target.
- CLI:
- `python3 orchestration/00-ORCHESTRATION/scripts/source_quality_gate.py --source-id SOURCE-20251031-005 --extract-jsonl sources/04-SOURCES/_meta/EXTRACT-SOURCE-20251031-005.jsonl --graph-state orchestration/state/DYN-KNOWLEDGE_GRAPH.json`

### Failure Modes
- Precision metrics become circular/self-referential.
- Recover: require explicit external evidence spans.
- Fixed 0.88 threshold over-rejects new domains.
- Recover: per-domain calibrated thresholds with floor/ceiling.
- Surprise spikes from low-quality fringe claims.
- Recover: precision weighting suppresses low-evidence surprises.

### Dependencies
- Components 2 and 5
- Embedding model + NLI/contradiction classifier

### Estimate
- 460-640 LOC
- Complexity: M

---

## Component 7: Lineage Engine — DEFER (Build after >=50 mined sources)
### Feasibility: 6/10
### Blueprint
- Tractability analysis:
- Full pairwise comparisons at 1,773 sources: `1,570,878` pairs. This is computationally feasible locally with ANN indexing and batched vector ops.
- Citation-edge-only deltas are much cheaper and should be phase-1 lineage mode.
- New files:
- `orchestration/00-ORCHESTRATION/scripts/source_lineage.py`
- `orchestration/00-ORCHESTRATION/scripts/source_convergence_detector.py`
- `sources/04-SOURCES/_meta/DYN-LINEAGE_TREE.json`
- `sources/04-SOURCES/_meta/DYN-CONVERGENT_EVOLUTION.json`
- Functions:
- `compute_innovation_delta(parent_vec, child_vec) -> {norm, angle}`
- `label_carrier_vs_mutator(delta) -> Label`
- `find_convergent_pairs(index, temporal_window_days, ancestor_depth) -> list[ConvergenceEvent]`
- Phylogenetic storage in Graphiti:
- Nodes: `SourceMeme`, `ConceptVariant`
- Edges: `MUTATES_FROM`, `HOMOLOGY_LINK`, `HOMOPLASY_LINK`
- Edge metadata: `{delta_norm, delta_angle, discovered_at, evidence}`
- Temporal window for independent discovery:
- Default: `120` days minimum separation.
- Independence constraints: zero shared ancestors within 2 hops and Jaccard overlap of ancestry sets <0.05.
- CLI:
- `python3 orchestration/00-ORCHESTRATION/scripts/source_lineage.py --source-index sources/04-SOURCES/_meta/DYN-SOURCE_TRIAGE.json --mined-only true --window-days 120`

### Failure Modes
- False convergent evolution from sparse citation metadata.
- Recover: require semantic similarity + ancestry disjointness + temporal separation simultaneously.
- Noise explosion from pairwise matrix.
- Recover: ANN candidate pruning before exact scoring.

### Dependencies
- Stable embeddings and mined atoms from >=50 sources
- Component 5 graph relations

### Estimate
- 760-1080 LOC
- Complexity: L

---

## Component 8: Negative Knowledge Store — BUILD
### Feasibility: 8/10
### Blueprint
- Data structure:
- Graph edge type: `FAILED_PATH` from `(Hypothesis|Method|QueryPattern)` to `(FailureReason|Counterevidence)`.
- Mandatory edge metadata:
- `failure_class`: `contradiction|low_evidence|non_reproducible|scope_mismatch|obsolete`
- `confidence`
- `context_scope` (domain/task type)
- `expires_at` (optional decay)
- `retest_after`
- New files:
- `orchestration/00-ORCHESTRATION/scripts/source_negative_knowledge.py`
- `sources/04-SOURCES/_meta/DYN-NEGATIVE_KNOWLEDGE.jsonl`
- Integrate with memsync record type:
- `record_type="failure_pheromone"`
- Prevent bias against valid-but-different paths:
- Never hard-block. Treat as ranking penalty only.
- Add decay half-life and mandatory re-probe (e.g., 5% scheduled retest).
- Require `context_scope`; no global blanket failures.
- Allow explicit counter-edge `REHABILITATED_PATH`.
- CLI:
- `python3 orchestration/00-ORCHESTRATION/scripts/source_negative_knowledge.py --source-id SOURCE-... --hypothesis-id HYP-... --failure-class low_evidence --confidence 0.72 --context-scope 'ai-agents/benchmarking'`

### Failure Modes
- Poisoning by premature failure tagging.
- Recover: require adjudicator confirmation for high-impact failures.
- Path lock-in due to stale negative priors.
- Recover: decay + periodic retest + rehabilitation edges.

### Dependencies
- Component 5 integration path

### Estimate
- 220-320 LOC
- Complexity: S/M

---

## Component 9: Cyclical Relevance Model — DEFER (Integrate with DC-147)
### Feasibility: 5/10
### Blueprint
- Decision:
- Do not build as standalone now.
- Implement as a policy plugin to DC-147 model router once mining pipeline emits stable usage telemetry.
- Gear detection approach:
- Inputs from recent prompts/tasks:
- lexical signals (`build/ship/fix` vs `explore/survey/synthesize`)
- task artifact types (patch/test vs analysis/brief)
- session time blocks and task durations
- classifier output:
- `gear = execution | exploration | mixed`
- confidence score
- New files (future phase):
- `orchestration/00-ORCHESTRATION/scripts/gear_detector.py`
- `orchestration/00-ORCHESTRATION/state/DYN-GEAR_STATE.json`
- `engine/02-ENGINE/FUNC-MODEL_ROUTER.md` (extend with `gear_policy` section)
- Is this premature optimization:
- Yes if built before components 1-6 are producing consistent throughput.
- Minimal viable version after pipeline stabilization:
- Rule-based classifier first, no ML training required.
- CLI (future):
- `python3 orchestration/00-ORCHESTRATION/scripts/gear_detector.py --window 14d --out orchestration/00-ORCHESTRATION/state/DYN-GEAR_STATE.json`

### Failure Modes
- Misclassification causes wrong source surfacing.
- Recover: confidence threshold + fallback to mixed gear.
- Overfitting to time-of-day heuristics.
- Recover: feature weighting favors explicit task language over clock-time.

### Dependencies
- DC-147 router baseline
- At least 2-4 weeks of task telemetry

### Estimate
- 260-420 LOC
- Complexity: M

---

## Summary Verdict Table
| Component | Feasibility | Verdict | Why |
|---|---:|---|---|
| 1. Triage Script | 9/10 | BUILD | High leverage, straightforward, unblocks all downstream components |
| 2. Extraction Template | 8/10 | BUILD | Schema is viable with chaperone/tension additions and validator |
| 3. Cluster Engine | 7/10 | REDESIGN | Pure k-means is brittle; hybrid clustering needed |
| 4. Batch Orchestrator | 8/10 | BUILD | Existing dispatch infra can be reused with thin scheduling layer |
| 5. Integration Bridge | 8/10 | BUILD | memsync exists; extend schema + durable retry queue |
| 6. Quality Gate | 7/10 | BUILD | Formula and gates are implementable; thresholds need calibration pass |
| 7. Lineage Engine | 6/10 | DEFER | Computationally tractable but data-hungry; wait for mined graph signal |
| 8. Negative Knowledge | 8/10 | BUILD | Small extension with strong payoff in avoiding repeated dead ends |
| 9. Cyclical Relevance | 5/10 | DEFER | Should be DC-147 plugin after pipeline and telemetry stabilize |

## Recommended Build Order
1. Component 1 (Triage Script)
2. Component 2 (Extraction Template)
3. Component 5 (Integration Bridge)
4. Component 6 (Quality Gate)
5. Component 3 (Cluster Engine redesign)
6. Component 4 (Batch Orchestrator)
7. Component 8 (Negative Knowledge)
8. Component 7 (Lineage Engine after >=50 mined sources)
9. Component 9 (Cyclical Relevance integrated into DC-147 after telemetry)

## Critical Path Analysis
- Critical path sequence:
- `1 -> 2 -> 5 -> 6 -> 3 -> 4`
- Rationale:
- No valid clustering or batching without triage and extraction outputs.
- No production mining without integration bridge and quality gating.
- Cluster/batch scaling should occur only after pilot quality pass.
- Parallelizable branches:
- Component 8 can start after component 5.
- Component 7 can start after first 50 mined sources and stable Graphiti relations.
- Component 9 should not gate mining throughput and remains post-stabilization.

