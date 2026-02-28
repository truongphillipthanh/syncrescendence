# Adjudicator: DC-208 Mining Pipeline Code Review — Round 2

## Fix Verification
### Fix 1: VERIFIED
- Wildfire promotion now persists into top-k output (replacement semantics, not append-only).
- Evidence from run (`mode=all`): `records=1773`, `top_k_count=50`, `wildfire_promoted_topk=2`, and promoted rows are ranked within top-k.
- Persistence coverage is fixed: all rows now include `rank` and `top_k` and are written to triage JSON (`persisted_total=1773`).

### Fix 2: VERIFIED
- Blank-ID row handling is fixed: full corpus coverage restored (`1773` rows persisted) with deterministic fallback IDs (`SOURCE-NOID-xxxx`), count `150`.
- `integration_targets`/`integrated_into` normalization is fixed for scalar and comma-list CSV values.
- Runtime normalization check:
  - `integration_targets='T1'` -> `['T1']`
  - `integrated_into='Z1,Z2'` -> `['Z1','Z2']`

### Fix 3: PARTIALLY FIXED
- Fixed and verified:
  - `write_bridge_jsonl()` emits bridge envelopes that pass `memsync_schema.validate_record()`.
  - `source_relation` records are emitted for `opposes_atom_ids` and ingest correctly via `memsync_bridge.ingest_extraction_jsonl()`.
  - Provenance clamping works (`line_start/line_end` clamp to chunk bounds).
- Remaining regression:
  - Hybrid frontmatter files that start with `has_transcript: yes` followed by fenced YAML are still misparsed by extractor frontmatter logic.
  - Repro: [source_extract.py](../../../orchestration/00-ORCHESTRATION/scripts/source_extract.py) (line 233) treats only the first bare line as frontmatter, then leaves fenced YAML in body.
  - Impacted corpus slice: 33 files (`has_transcript` + `---` on line 2).

### Fix 4: VERIFIED
- Durable idempotency is fixed:
  - `sent_records` is now persisted and checked before send.
  - Re-ingesting same `.bridge.jsonl` twice produced one HTTP send total (no duplicate write).
- Concurrency claim is fixed:
  - Process-level concurrent `--drain-retry` test resulted in one send total for one queued row.
  - `BEGIN IMMEDIATE` + `status='in_flight'` claim works to prevent dual-send.
- Backoff starts correctly at ~5s (`_backoff_seconds(1)` ~= 5.x).

### Fix 5: VERIFIED
- `to_memsync_record()` now matches `FailurePheromoneRecord` contract and validates through `memsync_schema.validate_record()`.
- `decayed_confidence == 0.0` now serializes correctly (no fallback to original confidence).
- Expired failures are excluded from retest candidate selection.
- Rehabilitation neutralization works in active queries (`query_failures(active_only=True)` excludes rehabilitated failure).

## Cross-Component Integration Matrix (Updated)
| Producer | Output | Consumer | Status | Notes |
|---|---|---|---|---|
| `source_triage.py` | `DYN-SOURCE_TRIAGE.json` (full ranked set + top_k flags) | future cluster engine | PASS | Full persistence restored; wildfire entries now appear in top-k |
| `source_extract.py` | `EXTRACT-*.bridge.jsonl` | `memsync_bridge.py ingest_extraction_jsonl()` | PASS | Schema validates; typed records parse; relations ingested |
| `source_extract.py` | category -> entity_type mapping | `memsync_schema.py` | PASS | Mapping aligns (`Claim/Framework/Prediction/Concept/PraxisHook`) |
| `memsync_schema.py` | Graphiti payload mapping | `memsync_bridge.py _send_record_to_graphiti()` | PASS | Entity/relation routes align with bridge sender |
| `source_negative_knowledge.py to_memsync_record()` | `failure_pheromone` record | `memsync_schema.validate_record()` | PASS | Contract now schema-compatible |
| retry queue (`memsync_bridge.py`) | queued failed records | `--drain-retry` workers | PASS WITH CAVEAT | No duplicate claims observed; no lease-recovery for orphaned `in_flight` rows |

## New Issues Found
- [P1] Extractor frontmatter parsing still fails for hybrid files (`has_transcript` then fenced YAML).
  - Location: [source_extract.py](../../../orchestration/00-ORCHESTRATION/scripts/source_extract.py) (line 233)
  - Effect: extraction body can include frontmatter block; provenance and atom quality can drift.
- [P2] Opposing-relation target IDs can become stale after dedup/resequencing.
  - Locations: ID resequence in [source_extract.py](../../../orchestration/00-ORCHESTRATION/scripts/source_extract.py) (line 553), relation emit in [source_extract.py](../../../orchestration/00-ORCHESTRATION/scripts/source_extract.py) (line 692)
  - Effect: relation may point to non-existent target atom UUID if original IDs changed during dedup.
- [P2] Retry rows can strand in `in_flight` on worker crash (no lease timeout/reaper).
  - Location: claim logic in [memsync_bridge.py](../../../orchestration/scripts/memsync_bridge.py) (line 439)
  - Effect: row may never re-enter `pending` without manual intervention.

## Non-Critical Improvements (Updated)
- Add `in_flight` lease timeout + reaper (`claimed_at`, stale reclaim threshold).
- In bridge CLI/docs, default ingestion pattern should explicitly target `.bridge.jsonl` to avoid noisy invalid-line warnings from raw atom JSONL.
- Add post-dedup `opposes_atom_ids` remapping table so relation targets always resolve.
- Keep bridge/daemon split for now; revisit merger only after pilot telemetry.

## Verdict: Ready for pilot? YES WITH CAVEATS
Pilot on top-5 is acceptable **if**:
1. Top-5 selection excludes the 33 hybrid-frontmatter files, or parser fix is applied first.
2. Pilot runbook includes manual recovery for any orphaned `in_flight` retry rows.
