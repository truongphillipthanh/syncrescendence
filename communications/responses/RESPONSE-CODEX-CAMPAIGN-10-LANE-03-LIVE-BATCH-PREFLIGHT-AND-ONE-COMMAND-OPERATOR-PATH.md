# Response

## Scope

Created the narrowest repo-native path from the current fixture-safe Acumen harness to a first true live batch.

Primary surfaces:

1. `/Users/system/syncrescendence/Makefile`
2. `/Users/system/syncrescendence/operators/acumen/README.md`
3. `/Users/system/syncrescendence/runtime/acumen/README.md`
4. `/Users/system/syncrescendence/orchestration/state/ACUMEN-PIPELINE-STATUS.json`

Supporting runtime hardening:

1. `/Users/system/syncrescendence/operators/acumen/pipeline_flow.py`
2. `/Users/system/syncrescendence/operators/acumen/run_triage.py`

## Delivered

1. Added `acumen-live-batch` at `/Users/system/syncrescendence/Makefile:185`.
   - Blocks immediately if `ACUMEN_YOUTUBE_API_KEY` or `GEMINI_API_KEY` is unset.
   - Validates the existing registry.
   - Enforces strict identity before any live call.
   - Runs the existing sequential wrapper in `POLL_MODE=live` and `TRIAGE_MODE=gemini`.
   - Keeps the fixture-safe `acumen-sample-run` path intact at `/Users/system/syncrescendence/Makefile:178`.

2. Tightened the live failure boundary in `/Users/system/syncrescendence/operators/acumen/pipeline_flow.py`.
   - Added top-level `failure_domain`, `failure_code`, `failure_message`, and `failed_stage`.
   - Embedded the nested poll and triage status snapshots into pipeline status.
   - Classified strict identity as `identity`, missing credential surfaces as `credential`, and provider / transport failures as `external_service`.

3. Added triage failure summarization in `/Users/system/syncrescendence/operators/acumen/run_triage.py`.
   - Status now emits a normalized failure summary when batch triage fails.
   - Restored the missing local `append_jsonl` helper needed by the current file so the fixture-safe path still completes.

4. Updated the operator and runtime runbooks.
   - `/Users/system/syncrescendence/operators/acumen/README.md:95` now documents the one-command live batch path and its bounded failure classes.
   - `/Users/system/syncrescendence/runtime/acumen/README.md:103` now points operators to `ACUMEN_YOUTUBE_API_KEY=... GEMINI_API_KEY=... make acumen-live-batch`.

5. Refreshed `/Users/system/syncrescendence/orchestration/state/ACUMEN-PIPELINE-STATUS.json:1`.
   - Current committed status remains fixture-safe and green.
   - It now includes `execution_profile`, `ok`, and the nested poll / triage snapshots that the live path will also populate.

## Verification

Executed:

1. `python3 -m py_compile /Users/system/syncrescendence/operators/acumen/run_triage.py /Users/system/syncrescendence/operators/acumen/pipeline_flow.py`
2. `make -C /Users/system/syncrescendence -n acumen-live-batch`
3. `env -u ACUMEN_YOUTUBE_API_KEY -u GEMINI_API_KEY make -C /Users/system/syncrescendence acumen-live-batch`
4. `make -C /Users/system/syncrescendence acumen-sample-run`

Observed:

1. The new live target expands to the strict identity + live poll + gemini triage path.
2. Missing credentials stop the live target immediately with `blocked: missing ACUMEN_YOUTUBE_API_KEY in environment`.
3. The fixture-safe sample run still succeeds and regenerated `/Users/system/syncrescendence/orchestration/state/ACUMEN-PIPELINE-STATUS.json` with `ok: true`.

## Boundary Notes

1. No live YouTube or Gemini batch was executed in this packet because no credentials were injected into repo execution.
2. No secrets were written, echoed, or committed. Only env-var names are referenced.
3. `run_triage.py` already contained broader evidence-family work; this packet did not unwind that work and only added the smallest compatibility fix needed to keep the sample path passing.
