# Adjudicator: DC-204 Engineering Review

Repo baseline used for adjudication:
- Canonical orchestration path exists at `orchestration/00-ORCHESTRATION/*`.
- Active dispatch currently writes `agents/<agent>/inbox/{pending,active,done,failed}`.
- Legacy automation still references `-INBOX/<agent>/{00-INBOX0,10-IN_PROGRESS,...}` in multiple scripts.
- No active Git hooks are installed in `.git/hooks` (sample hooks only).
- Current repo scale is non-trivial (`~9,125` files total, `~3,674` markdown files), so design must treat query/index cost as first-order.

## Spec A: Model Router — BUILD
### Feasibility: 9/10
A shell heuristic is sufficient for v1 because inputs are structured (`topic`, `description`, `kind`, `agent`) and required outputs are small and deterministic. Python is only required once you introduce adaptive thresholding from historical outcomes.

Direct answers:
- Bash vs Python: Bash is sufficient for v1 routing and salience suppression. Use Python only for v2 calibration.
- Salience threshold: Start static (config file), then add adaptive EWMA/quantile tuner from router logs.
- `dispatch.sh` contract: strict JSON stdout + semantic exit codes (detailed below).

### Blueprint
1. Files
- Add `orchestration/00-ORCHESTRATION/scripts/route_model.sh`.
- Add `orchestration/00-ORCHESTRATION/state/DYN-MODEL_ROUTER_RULES.json`.
- Add `orchestration/00-ORCHESTRATION/state/DYN-MODEL_ROUTER_DECISIONS.ndjson`.
- Add `engine/02-ENGINE/FUNC-MODEL_ROUTER.md`.
- Modify `orchestration/00-ORCHESTRATION/scripts/dispatch.sh`.

2. Functions and contract
- `route_model.sh --topic <str> --description <str> --kind <str> --target-agent <str> --from-agent <str> --json`.
- Output JSON keys: `decision`, `model`, `input_budget`, `output_budget`, `salience_score`, `reason_codes`, `router_version`.
- Exit code `0`: dispatch allowed.
- Exit code `10`: suppress (telemetry/noise).
- Exit code `20`: invalid input/config.
- Exit code `30`: runtime router failure.

3. `dispatch.sh` integration
- Call router immediately after argument parsing and agent validation, before task file creation.
- If exit `10`, do not create `TASK-*`; append a `SUPPRESS` event to global ledger and write NDJSON decision record.
- If router fails (`20/30`), fail-open by default (`dispatch` continues with safe default model/budget), fail-closed only when `SYNCRESCENDENCE_ROUTER_STRICT=1`.

4. Data structures
- `DYN-MODEL_ROUTER_RULES.json`: per-kind/per-agent thresholds and default model map.
- `DYN-MODEL_ROUTER_DECISIONS.ndjson`: append-only audit log for future adaptive calibration.

5. Error paths
- Missing rules file: fallback to hardcoded defaults + warning.
- Malformed JSON: router exit `20`, dispatch fail-open unless strict mode.
- Unknown model alias: substitute fallback (`claude-sonnet-5` or configured default) and log degradation reason.

### Failure Modes
1. Over-suppression of legitimate work.
- Condition: threshold too high or keyword misclassification.
- Detect: spike in suppressed records plus repeated manual re-dispatch of similar tasks.
- Recover: lower threshold in rules JSON and replay suppressed candidates from log.

2. Under-suppression (cost leak).
- Condition: threshold too low.
- Detect: high volume low-value dispatches with small outputs.
- Recover: raise threshold and blacklist low-salience topic patterns.

3. Router blocks dispatch due config drift.
- Condition: rules file corruption.
- Detect: router non-zero exit burst.
- Recover: fail-open mode and restore last known-good rules from git.

### Dependencies
- DC-100/101/102 phase-gate still applies for production activation.
- Stable location for model registry (`engine/02-ENGINE/MODEL-INDEX.md`).
- `jq` availability for JSON parsing in shell.

### Estimate
- Size: S
- LOC: 220-320
- Breakdown:
- `route_model.sh`: 130-180
- `dispatch.sh` integration: 40-70
- config + docs: 50-70

## Spec B: Knowledge Graph — REDESIGN
### Feasibility: 7/10
Feasible, but the pure bash/jq constraint should be redesigned. Bash/jq can parse links at this scale, but fuzzy suggestions, cycle detection, stale-ref analysis, and transport recommendations are much more reliable and maintainable in Python.

Direct answers:
- Bash/jq at 825+ files: workable for extraction, weak for graph analytics and fuzzy recovery. Python is the right implementation language.
- Output format: JSON as canonical artifact; generate Mermaid/DOT as derived views.
- Circular references: do not treat as hard errors. Compute SCCs, flag large/degenerate cycles for review.

### Blueprint
1. Files
- Add `orchestration/00-ORCHESTRATION/scripts/knowledge_graph.py` (core).
- Add `orchestration/00-ORCHESTRATION/scripts/knowledge_graph.sh` (wrapper for cron/manual).
- Add `orchestration/00-ORCHESTRATION/state/DYN-KNOWLEDGE_GRAPH.json`.
- Add `orchestration/00-ORCHESTRATION/state/DYN-KNOWLEDGE_GRAPH_DELTA.json`.
- Add `agents/commander/outbox/REPORT-KNOWLEDGE_GRAPH_HEALTH.md`.

2. Functions
- `scan_nodes(repo_root, scopes=[canon,praxis]) -> dict[path,node]`.
- `extract_links(markdown) -> list[edge]` for wikilinks/path refs/prefix refs.
- `resolve_targets(edges, nodes) -> (resolved, broken)`.
- `detect_cycles(adjacency) -> list[scc]`.
- `suggest_repair(broken, nodes) -> candidates` (difflib/Levenshtein).
- `compute_transport_gaps()` to detect canon concepts referenced in praxis without explicit link.

3. Data structures
- `nodes`: `{id,path,prefix,mtime,hash}`.
- `edges`: `{source,target_raw,target_id,status,kind,last_seen}`.
- `issues`: `{broken,orphans,stale,transport_gaps,cycles}`.
- `metrics`: counts + trend deltas.

4. Error paths
- Parser failure on malformed markdown: record file-level parse error, continue.
- Memory pressure: stream parsing and chunked serialization.
- Missing scope dir: mark degraded run and keep previous graph with `partial=true` flag.

### Failure Modes
1. False-positive broken links from path normalization bugs.
- Detect: broken-rate spikes after script changes.
- Recover: keep alias map (`old_path -> new_path`) and rerun resolver.

2. Fuzzy matcher suggests wrong file.
- Detect: low similarity confidence or repeated reject patterns.
- Recover: threshold floor + top-3 candidate output only.

3. Graph report becomes stale and trusted anyway.
- Detect: compare run timestamp vs SLA (7 days).
- Recover: integrity gate warns when graph age exceeds SLA.

### Dependencies
- Python 3 runtime (present).
- Agreement on canonical path roots (`canon/`, `praxis/05-SIGMA/`).
- Optional: git metadata access for accurate stale reference timestamps.

### Estimate
- Size: M
- LOC: 420-620
- Breakdown:
- Python core: 300-420
- shell wrapper + scheduling hooks: 40-70
- health report generator: 80-130

## Spec C: AgentFS Hybrid — DEFER
### Feasibility: 6/10
Strategically correct but operationally risky right now due ongoing path duality (`agents/*/inbox/*` vs `-INBOX/*`) and no active hook infrastructure. Build after Git-native task tracking hardens identity and event flow.

Direct answers:
- SQLite vs DuckDB vs JSON: SQLite is correct for transactional state, single-file portability, and rebuildability. DuckDB is better for analytics than mutable operational state. JSON index is insufficient for consistency guarantees.
- Migration path: incremental shadow mode, never big-bang.
- Randomized patrol invariant: enforce mechanically via scheduled audits + breaker escalation on missed patrol SLA.

### Blueprint
1. Files
- Add `orchestration/00-ORCHESTRATION/scripts/rebuild_agentfs.sh`.
- Add `orchestration/00-ORCHESTRATION/scripts/agentfs_sync.py`.
- Add `orchestration/00-ORCHESTRATION/scripts/agentfs_patrol.sh`.
- Add `orchestration/00-ORCHESTRATION/state/agentfs.db`.
- Add `orchestration/00-ORCHESTRATION/state/DYN-AGENTFS_PATROL_REPORT.md`.

2. Schema (minimum)
- `files(path PRIMARY KEY, prefix, kind, content, file_hash, mtime_unix, git_commit, updated_at)`.
- `links(src_path, dst_path, link_type, raw_ref)`.
- `tasks(task_id PRIMARY KEY, agent, state, reply_to, created_at, updated_at)`.
- `fts_content` virtual table for full-text lookup on markdown content.

3. Read/write flow
- Source of truth remains filesystem.
- `rebuild_agentfs.sh` performs full rebuild from repo state.
- `agentfs_sync.py --changed <filelist>` updates only touched files.
- Readers query SQLite first, then verify file hash on cache hit; mismatch triggers file fallback and async repair.

4. Patrol invariant
- Weekly deterministic random sample: `seed = ISO_WEEK + git_head_short`.
- Compare DB hash vs current file hash for sampled files.
- If drift exceeds threshold, auto-open breaker or incident and trigger full rebuild.

5. Error paths
- DB corruption: `PRAGMA integrity_check` failure triggers rebuild.
- Hook missed update: detected by patrol mismatch and repaired by changed-file resync/full rebuild.
- Lock contention: use WAL mode + bounded retry; if exhausted, degrade to filesystem reads.

### Failure Modes
1. Delamination (DB/file divergence).
- Detect: patrol mismatch ratio and hash drift.
- Recover: staged repair then full rebuild.

2. Agents stop reading filesystem ("Robert Moses" risk).
- Detect: no raw-file reads in telemetry for patrol period.
- Recover: policy guard requiring minimum raw-read quota per agent/week.

3. Cross-machine divergence.
- Detect: same path has different hash on two hosts.
- Recover: rebase/pull resolution and rebuild from merged HEAD.

### Dependencies
- Complete DC-150 identity/tracking conventions first.
- Hook bootstrap mechanism (none currently installed in `.git/hooks`).
- Stable directory canonicalization decision (`-INBOX` vs `agents/*/inbox`).
- Phase-gate: DC-100/101/102 unresolved infrastructure must be green before rollout.

### Estimate
- Size: L
- LOC: 750-1050
- Breakdown:
- sync + parser logic: 350-500
- rebuild + patrol scripts: 180-260
- schema/migrations + query helpers: 150-220
- docs/runbooks/tests: 70-120

## Spec D: Git-Native Tracking (Beads) — BUILD
### Feasibility: 8/10
This is achievable with current stack and should precede AgentFS rollout to stabilize task identity/state semantics.

Direct answers:
- Gap from current inbox to Beads: moderate. You already have task artifacts and lifecycle states, but identity is file-path-centric, not commit-centric.
- Trailer convention: use deterministic `Task-ID` + `Task-State` + `Task-Agent` trailers, enforced by hook/script.
- Query at 1700+ files: use Git plumbing + incremental cache index; avoid full markdown scans for every query.

### Blueprint
1. Files
- Add `orchestration/00-ORCHESTRATION/scripts/beads_commit.sh`.
- Add `orchestration/00-ORCHESTRATION/scripts/beads_query.py`.
- Add `orchestration/00-ORCHESTRATION/scripts/beads_backfill.py`.
- Add `orchestration/00-ORCHESTRATION/state/beads_index.db` (derived cache).
- Add `engine/02-ENGINE/REF-BEADS_CONVENTION.md`.

2. Trailer convention
- `Task-ID: TASK-YYYYMMDD-<slug>`.
- `Task-State: pending|active|done|blocked|failed|archived`.
- `Task-Agent: commander|adjudicator|cartographer|psyche|ajna`.
- `Task-Reply-To: <agent>`.
- Optional: `Task-Parent: DC-###`.

3. Workflow
- `dispatch.sh` generates/normalizes `Task-ID`.
- `beads_commit.sh` wraps `git commit` using `git interpret-trailers` to append required trailers.
- `beads_query.py` builds incremental index from last processed commit for fast cross-history queries.

4. Gap closure (current vs target)
- Normalize dual inbox paths via compatibility map before strict enforcement.
- Ensure receipts/results also carry `Task-ID` to preserve DAG linkage.
- Add migration/backfill script to assign IDs to historical tasks.

5. Error paths
- Missing trailers in commit touching task artifacts: fail commit in strict mode, warn in soft mode.
- Duplicate `Task-ID`: reject and regenerate using deterministic + collision suffix.
- Rewritten history: detect index invalidation and rebuild `beads_index.db` from scratch.

### Failure Modes
1. Split-brain state between legacy `-INBOX` and new `agents/*/inbox`.
- Detect: same `Task-ID` observed in both roots with divergent state.
- Recover: canonical resolver script + single-source declaration in reference doc.

2. Commit hygiene drift.
- Detect: percentage of task commits missing required trailers.
- Recover: enforce via commit-msg hook or mandatory wrapper script.

3. Query slowness on large history.
- Detect: query latency SLA breach.
- Recover: use incremental SQLite cache keyed by commit hash.

### Dependencies
- Team agreement on canonical task identity and state machine.
- Git hook or commit wrapper adoption.
- One-time historical backfill/migration pass.

### Estimate
- Size: M
- LOC: 480-720
- Breakdown:
- commit wrapper + validation: 120-180
- query/index engine: 220-340
- backfill/migration + docs: 140-200

## Spec E: Constitutional Evolution — DEFER
### Feasibility: 3/10
Not production-feasible yet without a dedicated simulation harness and stable metrics from Specs A/D/C. A minimal offline prototype is feasible.

Direct answers:
- Feasible without dedicated simulation env: only as MVP research mode, not autonomous production governance.
- Minimum viable version: offline replay over historical tasks with single-rule mutations and strict human approval.
- Destabilization prevention: shadow mode, canary branch, one-rule-at-a-time, mandatory rollback gates.

### Blueprint
1. Files
- Add `orchestration/00-ORCHESTRATION/scripts/constitution_replay.py`.
- Add `orchestration/00-ORCHESTRATION/scripts/constitution_mutate.py`.
- Add `orchestration/00-ORCHESTRATION/state/DYN-CONSTITUTION_FITNESS.json`.
- Add `orchestration/00-ORCHESTRATION/state/DYN-CONSTITUTION_CANDIDATES.md`.
- Add `engine/02-ENGINE/FUNC-SUPREME_COURT.md` (repeal-only role spec).

2. MVP loop
- Build replay corpus from historical TASK/RESULT pairs and commit outcomes.
- Apply one mutation per trial to AGENTS rule set representation.
- Score with fixed metrics: completion rate, conflict incidence, rollback incidence, policy violations.
- Surface top candidates as proposals only; no auto-merge.

3. Safety rails
- Run only on isolated branch/worktree.
- Require Sovereign approval for any promotion.
- Hard rollback threshold: regressions on any P0 metric abort trial.

4. Error paths
- Overfit to historical artifacts.
- Metric gaming by mutation strategy.
- Rule interactions causing contradictory constraints.

### Failure Modes
1. Governance autoimmunity (agents freeze).
- Detect: thinking/output ratio inflation + dispatch throughput collapse.
- Recover: revert candidate constitution and run repeal pass.

2. Silent constitution drift.
- Detect: candidate differs from baseline without explicit approval artifact.
- Recover: enforce signed approval marker before merge.

3. Simulation-reality mismatch.
- Detect: canary trials regress while replay scores improve.
- Recover: weight live canary metrics higher than replay metrics.

### Dependencies
- Stable telemetry and identity from Specs A and D.
- Reliable task-state substrate (preferably after C shadow deployment).
- Isolated evaluation environment and explicit approval protocol.

### Estimate
- Size: L
- LOC: 900-1400
- Breakdown:
- replay/mutation engine: 500-750
- scoring/metrics pipeline: 220-340
- safety/approval plumbing + docs: 180-310

## Summary Verdict Table

| Spec | Feasibility | Complexity | Verdict | Primary Reason |
|---|---:|---|---|---|
| A: Model Router | 9/10 | S | BUILD | High value, low integration risk, immediate dispatch quality gains |
| B: Knowledge Graph | 7/10 | M | REDESIGN | Pure bash/jq constraint should be relaxed to Python core for reliability |
| C: AgentFS Hybrid | 6/10 | L | DEFER | Correct direction but high delamination risk before task identity/path normalization |
| D: Git-Native Tracking | 8/10 | M | BUILD | Strong fit to current artifacts, closes identity/audit gaps needed by C/E |
| E: Constitutional Evolution | 3/10 | L | DEFER | Needs simulation harness + stable telemetry substrate first |

## Recommended Build Order

1. Spec A (DC-147) in fail-open mode with audit logging.
2. Spec D (DC-150) to establish task identity, trailer discipline, and fast history queries.
3. Spec B (DC-148) with redesigned Python core and JSON-first outputs.
4. Spec C (DC-149) in shadow mode only, then progressive read-path adoption.
5. Spec E (DC-151) as offline research track after A/D/C metrics stabilize.

Phase-gate note: per `DYN-DEFERRED_COMMITMENTS.md`, production rollout should not violate unresolved DC-100/101/102 constraints.
