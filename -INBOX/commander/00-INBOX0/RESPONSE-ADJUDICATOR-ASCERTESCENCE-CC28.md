**Repo-grounded baseline**
- `atom_cluster.py` already emits cluster/score/index artifacts, and `DYN-ATOM_INDEX.jsonl` currently has `integration_status: "pending"` for all 14,025 atoms ([atom_cluster.py](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/atom_cluster.py), [DYN-ATOM_INDEX.jsonl](/Users/system/syncrescendence/sources/04-SOURCES/_meta/DYN-ATOM_INDEX.jsonl)).
- `session_state_brief.py` already persists brief entries to Commander journal JSONL and has an Integration Metric section ([session_state_brief.py](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/session_state_brief.py)).
- Global hooks already run `session_state_brief.py` on `UserPromptSubmit` and `cc_handoff.sh` on `PreCompact` ([settings.json](/Users/system/.claude/settings.json)).
- Memory architecture is explicitly file-first with Layer-2 journals and Layer-3 optional projection ([ARCH-MEMORY_ARCHITECTURE.md](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/state/ARCH-MEMORY_ARCHITECTURE.md)).
- Config centralization exists (`config.sh`, `config.py`) and a migration script already exists (`config_migrate.sh`) but no hard assertion harness yet ([config.sh](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/config.sh), [config.py](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/config.py), [config_migrate.sh](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/config_migrate.sh)).
- `memory_compaction.py` exists, but it is weekly digest/dedup, not intent-aware "dream consolidation" ([memory_compaction.py](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/memory_compaction.py)).

## Spec 1: Protease Protocol (Destructive Atom Integration)

**Architecture (text diagram)**
```text
DYN-ATOM_SCORE_AUDIT.jsonl + DYN-ATOM_INDEX.jsonl + DYN-ATOM_CLUSTER_MANIFEST.jsonl
    + ARCH-INTENTION_COMPASS.md (active intentions)
    -> protease_queue.py
    -> DYN-PROTEASE_QUEUE.jsonl (machine)
    -> DYN-PROTEASE_QUEUE.md (Sovereign chewing queue; grouped by intention)

Sovereign rewrites selected atoms -> 50-token SN axioms (template-constrained)
    -> protease_promote.py --target praxis|canon
    -> SN artifact append (praxis or canon)
    -> DYN-ATOM_INDEX.jsonl status update: pending -> consumed -> promoted_*
    -> DYN-PROTEASE_METRICS.jsonl + DYN-PROTEASE_METRICS.md
```

**Failure modes**

| Failure mode | What breaks | Blast radius | Mitigation |
|---|---|---|---|
| Cluster-level band unusable (currently all clusters `archive_candidate`) | No queue if you only trust cluster bands | High | Queue from atom-level `sovereign_review` band first, then cluster-group for context |
| Intention matcher overfits keywords | Wrong queue routing | Medium | Hybrid score: priority keyword overlap + embedding similarity + manual override field |
| Re-promotion duplicates | Same atom promoted multiple times | Medium | Enforce state machine in `DYN-ATOM_INDEX` and reject non-`pending/queued` transitions |
| JSONL corruption during index write | Atom lifecycle state lost | High | temp file + validate + atomic rename (same pattern as CSV invariant) |
| SN output too lossy | Axiom drops rationale | High | Require `source_atom_ids` + `why_preserved` field in each SN block |

**Implementation plan**
- Create [protease_queue.py](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/protease_queue.py) (~280 LOC).
- Create [protease_promote.py](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/protease_promote.py) (~320 LOC).
- Create [DYN-PROTEASE_QUEUE.jsonl](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/state/DYN-PROTEASE_QUEUE.jsonl) and [DYN-PROTEASE_QUEUE.md](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/state/DYN-PROTEASE_QUEUE.md) writers (~120 LOC formatting logic).
- Extend [session_state_brief.py](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/session_state_brief.py) integration metric to read protease metrics, not commit-subject heuristics (~40 LOC).
- Add SN target files:
  - [PRAC-PROTEASE_AXIOMS.sn.md](/Users/system/syncrescendence/praxis/05-SIGMA/practice/PRAC-PROTEASE_AXIOMS.sn.md)
  - [CANON-PROTEASE_AXIOMS.sn.md](/Users/system/syncrescendence/canon/01-CANON/sn/CANON-PROTEASE_AXIOMS.sn.md)
- Total: ~760 LOC. Session budget: 2 sessions.

**Verification checklist**
1. Generate queue: `python3 .../protease_queue.py --max-atoms 120`.
2. Confirm queue atoms are all from `sovereign_review` band or explicit override.
3. Promote 1 test axiom; verify `DYN-ATOM_INDEX` transitions and timestamp fields.
4. Re-run promotion on same atom; must hard-fail idempotently.
5. Check metrics: atoms in/out, compression ratio, intention coverage update.

---

## Spec 2: Dream Cycle (`circadian_sync.py`)

**Architecture (text diagram)**
```text
Trigger (launchd nightly OR manual at close)
    -> circadian_sync.py
Inputs:
  - agents/commander/memory/journal/*.jsonl (session_brief + session_end + manual)
  - git log range since last sync
  - agents/commander/outbox/handoffs/HANDOFF-*.md
  - DYN-DEFERRED_COMMITMENTS.md
Process:
  normalize -> deduplicate -> retain/forget classify -> summarize rationale-preserving
Outputs:
  - MEMORY_CONSOLIDATION.md (append-only cycles)
  - FORGET_CANDIDATES.jsonl (negative selection ledger)
  - DYN-DREAM_QUALITY.jsonl (+ md summary)
  - circadian_state.json (cursor, last commit, last ts)
```

**Failure modes**

| Failure mode | What breaks | Blast radius | Mitigation |
|---|---|---|---|
| Runs while session active | Consolidates partial state | Medium | guard: exit if active CLI process or dirty protected dirs |
| Over-aggressive forgetting | Drops needed context | High | two-step forget: `candidate` then `confirmed` after N cycles |
| Low-quality compression | rationale lost | High | dream quality metric gates append; below threshold writes only draft |
| Duplicate cycles | memory spam | Low | state cursor (`last_ts`,`last_commit`) + content hash dedupe |
| Handoff parser drift | misses key decisions | Medium | strict fallback: include raw "unparsed excerpts" section |

**Implementation plan**
- Create [circadian_sync.py](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/circadian_sync.py) (~380 LOC).
- Create [com.syncrescendence.circadian-sync.plist](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/launchd/com.syncrescendence.circadian-sync.plist) (~70 LOC).
- Create output/state files:
  - [MEMORY_CONSOLIDATION.md](/Users/system/syncrescendence/agents/commander/memory/MEMORY_CONSOLIDATION.md)
  - [FORGET_CANDIDATES.jsonl](/Users/system/syncrescendence/agents/commander/memory/sync/FORGET_CANDIDATES.jsonl)
  - [circadian_state.json](/Users/system/syncrescendence/agents/commander/memory/sync/circadian_state.json)
  - [DYN-DREAM_QUALITY.jsonl](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/state/DYN-DREAM_QUALITY.jsonl)
- Optional hook: add manual close trigger in [cc_handoff.sh](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/cc_handoff.sh) (~15 LOC).
- Total: ~500 LOC. Session budget: 2 sessions.

**Verification checklist**
1. `--dry-run` shows retain/forget decisions without writes.
2. First real run appends one cycle with source commit range.
3. Second run (no changes) produces zero-op cycle.
4. Inject known decision IDs; verify rationale coverage in dream-quality report.
5. Simulate active session guard; script exits cleanly without write.

---

## Spec 3: Proprioceptive Config Harness

**Architecture (text diagram)**
```text
Every script start:
  source config.sh
  -> sync_config_preflight --context <script>
  -> assert dirs/files/env assumptions
  -> fail closed with explicit assumption + repair hint

Standalone:
  config_health.sh --json|--md --strict
  -> used by scaffold_validate.sh
  -> used by cockpit_startup.sh

Migration:
  config_migrate.sh --dry-run|--apply --verify
  -> rewrites scripts to config imports/sourcing
  -> runs scaffold_validate gate
```

**Failure modes**

| Failure mode | What breaks | Blast radius | Mitigation |
|---|---|---|---|
| False failures on optional components | noisy failures reduce trust | Medium | required vs optional assertions split |
| Path drift across machines | scripts fail on MBA/mini mismatch | High | configurable root via env override + resolved repo-root proof |
| Migration script rewrites comments/examples incorrectly | doc/code mismatch | Low | code-only rewrite guards + syntax checks |
| Health check not integrated in validators | drift undetected | Medium | scaffold_validate hard-calls config health and returns violation code |
| Silent pass with stale fallback paths | proprioception lost | High | remove hardcoded fallback roots in execution scripts |

**Implementation plan**
- Extend [config.sh](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/config.sh): `sync_assert_dir`, `sync_assert_file`, `sync_config_preflight` (~120 LOC).
- Extend [config.py](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/config.py): `validate_config(strict)` + `ConfigError` (~90 LOC).
- Create [config_health.sh](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/config_health.sh) (~140 LOC).
- Integrate in [scaffold_validate.sh](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/scaffold_validate.sh) and optionally [cockpit_startup.sh](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/cockpit_startup.sh) (~50 LOC).
- Extend existing [config_migrate.sh](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/config_migrate.sh) for dynamic inventory + verify-only (~120 LOC).
- Total: ~520 LOC. Session budget: 1.5 sessions.

**Verification checklist**
1. `bash .../config_health.sh --strict --json` passes in healthy repo.
2. Temporarily break one required path; confirm explicit failed assumption text.
3. Run `scaffold_validate.sh`; ensure config failures appear as first-class violations.
4. `config_migrate.sh --dry-run` then `--apply`; run `bash -n` and `python3 -m py_compile` on touched files.
5. Confirm removed hardcoded `/Users/system/syncrescendence` runtime fallbacks in active scripts.

---

## Spec 4: State Vector (Tier 1 + Tier 2)

**Architecture (text diagram)**
```text
PreCompact/SessionClose
    -> state_vector.py --tier both
Collectors:
  phase/dependencies: DYN-DEFERRED_COMMITMENTS.md
  intentions: ARCH-INTENTION_COMPASS.md (active, ranked)
  inhibitions: AGENTS anti-patterns + current phase-gate blocks
  output contract: latest active directive/task artifacts
Writers:
  Tier 1 -> DYN-STATE_VECTOR.md (~300 tokens)
  Tier 2 -> DYN-PORTAL_EXPANDED.md (~2,000 tokens)
  optional machine form -> DYN-STATE_VECTOR.json
cc_handoff embeds links to both
```

**Failure modes**

| Failure mode | What breaks | Blast radius | Mitigation |
|---|---|---|---|
| Token budgets exceeded | portal becomes textbook again | Medium | hard token cap + priority truncation |
| Intention parser drift on markdown tables | wrong top 3 intentions | High | parser tests on current compass snapshots |
| Inhibitions too generic | agents ignore constraints | Medium | generate from concrete anti-pattern lines and current blockers |
| Hook timing race with handoff | stale vector in handoff | Low | call vector generation before final handoff write |
| Tier divergence | Tier 1 contradicts Tier 2 | Medium | both generated from same structured intermediate JSON |

**Implementation plan**
- Create [state_vector.py](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/state_vector.py) (~320 LOC).
- Create outputs:
  - [DYN-STATE_VECTOR.md](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/state/DYN-STATE_VECTOR.md)
  - [DYN-PORTAL_EXPANDED.md](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/state/DYN-PORTAL_EXPANDED.md)
  - [DYN-STATE_VECTOR.json](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/state/DYN-STATE_VECTOR.json)
- Modify [cc_handoff.sh](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/cc_handoff.sh) to call vector generation pre-write (~25 LOC).
- Total: ~345 LOC. Session budget: 1 session.

**Verification checklist**
1. Generate both tiers manually; confirm token targets.
2. Validate required fields present: phase, top 3 intentions, inhibitions, output format.
3. Trigger precompact path; handoff references freshly generated vector files.
4. Regression test parser against current `ARCH-INTENTION_COMPASS.md` table variants.
5. Compare Tier 1 to Tier 2 source IDs for consistency.

---

## Meta-question: Engineering Assessment

### 1) Integration-First Gate enforceability
Yes, implementable, but with **dual enforcement**:
1. `session-close gate` (primary): checks whether at least one value artifact was produced and atom lifecycle advanced.
2. `commit-time gate` (secondary): validates commit trailers point to real value artifacts.

Technical enforcement:
- New gate script checks diffs since baseline commit from [DYN-SESSION_BASELINE.json](/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/state/DYN-SESSION_BASELINE.json).
- Pass condition:
  - at least one new/changed file under `praxis/05-SIGMA` or `canon/01-CANON/sn`, and
  - at least one `DYN-ATOM_INDEX` transition to `consumed/promoted_*`.
- Controlled bypass: `INTEGRATION_GATE_BYPASS=1` + required reason file in `-SOVEREIGN/`.

### 2) "Make it breathe or die" viability
Viable only with rails. Without rails, yes, it can poison subsequent sessions.

Required rails:
1. Quarantine lane: new consolidations land in consolidation file, not canonical memory directly.
2. TTL probation: promoted summaries expire unless referenced within N cycles.
3. Rollback pointer: every consolidation cycle stores source range and reversible patch.
4. Contradiction preservation: never overwrite prior rationale; append supersession markers.
5. Health budget: if dream quality drops below threshold, stop promotion and alert.

### 3) Minimum set to trigger building -> inhabiting transition
Minimum effective set:
1. **Spec 1 core** (Protease queue + promote + consumed marking + metrics).
2. **Spec 4 Tier 1** (300-token state vector generated at close).
3. **Spec 2 lite** (filesystem-only consolidation append + forget candidates).

`Spec 3` is high-value hardening but not the minimum catalyst for phase transition.

### Risk matrix

| Item | Likelihood | Impact | Risk | Control |
|---|---|---|---|---|
| Gate too strict blocks legitimate infra sessions | Medium | Medium | Medium | scoped bypass with explicit reason |
| Autocatalytic bad summary contaminates memory | Medium | High | High | quarantine + TTL + rollback |
| Protease queue becomes another backlog | Medium | High | High | hard WIP limit per intention, consumed-state enforcement |
| State vector drift from real repo state | Low | High | Medium | generated only from filesystem state, no manual edits |

**Recommended sequence**
1. Implement Spec 1 core + strict consumed-state transitions.
2. Wire Integration-First Gate to Spec 1 metrics.
3. Implement Spec 4 Tier 1 close-hook generation.
4. Implement Spec 2 lite nightly/close consolidation.
5. Implement Spec 3 harness and full migration sweep as stability pass.