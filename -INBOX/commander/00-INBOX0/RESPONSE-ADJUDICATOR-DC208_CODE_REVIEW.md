---
agent: adjudicator
council: DC-208
topic: DC-208 Mining Pipeline Code Review — Round 1 (FAIL verdict, P0 bugs)
status: unprocessed
collected: 2026-02-23
---

# Adjudicator: DC-208 Mining Pipeline Code Review

## Overall Assessment
FAIL
The four built components are not pilot-ready. The extraction output cannot be ingested by the integration bridge, negative-knowledge records are schema-incompatible with the bridge schema, wildfire promotion is functionally inert, and retry/idempotency semantics allow duplicate Graphiti writes under normal reruns/concurrent drains. Core architecture intent is visible, but integration contracts are currently broken.

## Component 1: Triage Script
### Blueprint Compliance: 6/10
### Bugs Found
- [P0] Wildfire promotion is ineffective in final ranked output. Promoted items are appended *after* the top-k slice, then persistence writes only `scores[:top_k]`, so no promoted source appears in output.
  - Code: `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_triage.py:609`, `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_triage.py:713`
  - Runtime evidence: `/tmp/DC208_REVIEW_TRIAGE.json` had `wildfire_promoted_top = 0` despite `wildfire_pct=0.05`.
- [P1] 150 CSV rows are dropped from scoring because records with blank `id` are discarded, reducing coverage from 1773 -> 1623.
  - Code: `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_triage.py:165`
  - Evidence: `DYN-SOURCES.csv rows 1773, with_id 1623, blank_id 150`.
- [P1] `integration_targets` extraction is inconsistent with observed frontmatter. Code reads `integrated_into` and only as list; many sources use `integration_targets` and/or scalar strings, driving target-density undercount.
  - Code: `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_triage.py:147`, `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_triage.py:319`
- [P2] Parse-error observability is inaccurate. Warnings are emitted for YAML parse failures, but `parse_errors` summary can remain zero due filename/source-id matching gaps.
  - Code: `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_triage.py:288`

### Integration Issues
- `DYN-SOURCE_TRIAGE.json` currently persists top-k only, which weakens future cluster-engine input if that engine expects full-mode source ranking.
  - Code: `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_triage.py:713`

### Recommendations
- Replace top-k composition logic with replacement semantics (swap out bottom N top-k entries for wildfire promotions).
- Preserve/scaffold records with blank `id` using deterministic filename-derived IDs.
- Normalize both `integration_targets` and `integrated_into`, accepting scalar/list forms.
- Emit parse-error counts from scan results directly (not only mapped records).

## Component 2: Extraction Template
### Blueprint Compliance: 7/10
### Bugs Found
- [P0] Output schema is not bridge-ingestable. Extractor writes atom objects (`atom_id`, `category`, etc.) with no `record_type`, `uuid`, `schema_version`, so `memsync_bridge` rejects all lines.
  - Code (producer): `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_extract.py:582`
  - Code (consumer validation): `/Users/system/syncrescendence/orchestration/scripts/memsync_bridge.py:290`, `/Users/system/syncrescendence/orchestration/scripts/memsync_bridge.py:299`
  - Runtime evidence: `validation failed: Unknown record_type: None`, ingested `0`.
- [P1] Non-fenced frontmatter files (33 known files) are not parsed by extractor parser; body starts at line 1, so extraction includes metadata text and provenance shifts.
  - Code: `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_extract.py:221`
- [P1] LLM-provided `line_start/line_end` are accepted without clamping to chunk bounds, permitting invalid provenance ranges.
  - Code: `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_extract.py:426`

### Integration Issues
- No adapter exists from extractor categories (`claim`, `framework`, etc.) to bridge entity types (`Claim`, `Framework`, etc.), and no relation records are emitted.
  - Code refs: `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_extract.py:51`, `/Users/system/syncrescendence/orchestration/scripts/memsync_schema.py:40`

### Recommendations
- Add a bridge-ready export mode that emits envelope records:
  - `{record_type, schema_version, uuid, timestamp, payload:{...}}` or schema-native flat records expected by `memsync_schema`.
- Parse non-fenced frontmatter consistently with triage parser behavior.
- Clamp provenance to chunk bounds and reject out-of-range spans.

## Component 5: Integration Bridge
### Blueprint Compliance: 5/10
### Bugs Found
- [P0] Idempotency is incomplete. Duplicate suppression checks only retry queue entries; successfully sent records are never persisted as sent keys, so reruns resend duplicates.
  - Code: `/Users/system/syncrescendence/orchestration/scripts/memsync_bridge.py:349`, `/Users/system/syncrescendence/orchestration/scripts/memsync_bridge.py:360`
- [P0] Concurrent drains can duplicate writes: rows are selected then sent then deleted without row locking/in-flight marking.
  - Code: `/Users/system/syncrescendence/orchestration/scripts/memsync_bridge.py:405`, `/Users/system/syncrescendence/orchestration/scripts/memsync_bridge.py:460`
- [P1] Backoff sequence is off-by-one from documented sequence. Implementation yields first delayed retry at ~15s (plus jitter), not 5s.
  - Code: `/Users/system/syncrescendence/orchestration/scripts/memsync_bridge.py:150`, `/Users/system/syncrescendence/orchestration/scripts/memsync_bridge.py:464`
- [P1] Schema validation is too permissive for non-atom records (e.g., failure records can omit key fields and still parse if defaults satisfy dataclass fields).
  - Code: `/Users/system/syncrescendence/orchestration/scripts/memsync_schema.py:169`

### Integration Issues
- Bridge expects schema-native records, while extractor emits raw atoms. Contract is broken at ingest boundary.
  - Code: `/Users/system/syncrescendence/orchestration/scripts/memsync_bridge.py:268`
- Blueprint called for extending `memsync_daemon.py` with typed records and retry drain CLI. Implementation created separate `memsync_bridge.py` and did not extend daemon interface.
  - Daemon code: `/Users/system/syncrescendence/orchestration/scripts/memsync_daemon.py:216`

### Recommendations
- Persist a `sent_records` table keyed by deterministic idempotency key and check it before send.
- Add transactional claiming for retry rows (`BEGIN IMMEDIATE` + status column) to prevent dual-drain duplicate sends.
- Align backoff to documented schedule or update docs.
- Tighten per-record required-field validation in `memsync_schema`.

## Component 8: Negative Knowledge Store
### Blueprint Compliance: 6/10
### Bugs Found
- [P0] `to_memsync_record()` output is incompatible with `FailurePheromoneRecord` schema (`schema_version`, `uuid`, `timestamp`, `stage`, `error` missing; `record_id` non-standard).
  - Code (producer): `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_negative_knowledge.py:297`
  - Code (schema): `/Users/system/syncrescendence/orchestration/scripts/memsync_schema.py:122`
  - Runtime evidence: `ValidationError Missing schema_version`.
- [P1] Decay can be nullified when `decayed_confidence == 0.0` due `or` fallback to original confidence.
  - Code: `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_negative_knowledge.py:305`, `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_negative_knowledge.py:324`
  - Runtime evidence: forced `decayed_confidence=0.0` serialized as `1.0`.
- [P2] Retest candidate selection ignores expiration, potentially retesting expired failures.
  - Code: `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_negative_knowledge.py:269`

### Integration Issues
- `to_graphiti_edge()` shape is not consumed by bridge/daemon pipelines (no ingestion path from this edge structure currently wired).
  - Code: `/Users/system/syncrescendence/orchestration/00-ORCHESTRATION/scripts/source_negative_knowledge.py:315`

### Recommendations
- Emit schema-compliant failure pheromone records with required bridge fields.
- Replace `x or y` confidence selection with explicit `is None` checks.
- Filter expired failures from retest pool.

## Cross-Component Integration Matrix
| Producer | Output | Consumer | Status | Notes |
|---|---|---|---|---|
| `source_extract.py` | Atom JSONL (`atom_id`, `category`, etc.) | `memsync_bridge.py ingest_extraction_jsonl()` | FAIL | Missing `record_type/schema_version/uuid`; bridge rejects all records |
| `source_extract.py` | category values (`claim/framework/...`) | `memsync_schema.py SourceAtomRecord.entity_type` | FAIL | No category→entity_type mapping |
| `source_negative_knowledge.py to_memsync_record()` | failure pheromone dict | `memsync_schema.py FailurePheromoneRecord` | FAIL | Missing required schema fields; key mismatch (`record_id`) |
| `memsync_schema.py map_*` | Graphiti payload objects | `memsync_bridge.py _send_record_to_graphiti()` | PARTIAL | Works for schema-native records only; producer mismatch blocks path |
| `source_triage.py` | `DYN-SOURCE_TRIAGE.json` top-k ranking | future cluster engine | RISK | Only top-k persisted; wildcard promotions not reflected |

## Critical Fixes (must fix before pilot)
1. Add a contract adapter so extraction emits bridge-ingestable records (or teach bridge to ingest raw atom schema).
2. Fix wildfire logic so promoted sources replace low-ranked top-k entries and appear in persisted top-k.
3. Make idempotency durable across successful sends and add concurrency-safe retry claiming.
4. Align negative-knowledge memsync payload with `FailurePheromoneRecord` schema.
5. Fix confidence serialization for `decayed_confidence == 0.0`.

## Non-Critical Improvements (can defer)
1. Include blank-id CSV rows via deterministic fallback IDs to recover full 1773 coverage.
2. Parse `integration_targets`/`integrated_into` in both scalar and list forms.
3. Clamp extractor provenance spans to chunk bounds.
4. Improve parse-error metrics so summary counts match warnings.
5. Decide whether bridge remains separate or capabilities merge into `memsync_daemon.py` for operational simplicity.

## Verdict: Ready for pilot? NO
