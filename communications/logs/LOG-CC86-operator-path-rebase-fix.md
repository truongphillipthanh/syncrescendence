# LOG-CC86 operator path rebase fix

## Intent

Repair operator scripts that still assumed pre-migration file topology and therefore resolved repo paths incorrectly after shell restructuring.

## Problem

Several bridge/runtime operators set `REPO_ROOT = Path(__file__).resolve().parent` even when the script lived under `operators/*`. That made path lookups resolve to `operators/...` instead of repo root and silently broke:

1. policy loads
2. runtime collector imports
3. reconciler imports
4. event normalization/sanitization output paths

## Patched operators

1. exocortex bridges:
   - [exocortex_event_bridge.py](/Users/system/syncrescendence/operators/exocortex/exocortex_event_bridge.py)
   - [channel_surface_bridge.py](/Users/system/syncrescendence/operators/exocortex/channel_surface_bridge.py)
   - [cloudflare_domain_bridge.py](/Users/system/syncrescendence/operators/exocortex/cloudflare_domain_bridge.py)
   - [github_issue_bridge.py](/Users/system/syncrescendence/operators/exocortex/github_issue_bridge.py)
   - [google_model_bridge.py](/Users/system/syncrescendence/operators/exocortex/google_model_bridge.py)
   - [manus_checkpoint_bridge.py](/Users/system/syncrescendence/operators/exocortex/manus_checkpoint_bridge.py)
   - [obsidian_repo_bridge.py](/Users/system/syncrescendence/operators/exocortex/obsidian_repo_bridge.py)
   - [xai_model_bridge.py](/Users/system/syncrescendence/operators/exocortex/xai_model_bridge.py)
   - [youtube_feed_bridge.py](/Users/system/syncrescendence/operators/exocortex/youtube_feed_bridge.py)
2. runtime operators:
   - [reconcile-ajna-events.py](/Users/system/syncrescendence/operators/runtime/reconcile-ajna-events.py)
   - [sync-openclaw.py](/Users/system/syncrescendence/operators/runtime/sync-openclaw.py)
   - [sanitize-openclaw-events.py](/Users/system/syncrescendence/operators/runtime/sanitize-openclaw-events.py)
   - [normalize_event_ledger.py](/Users/system/syncrescendence/operators/runtime/normalize_event_ledger.py)

## Verification

1. compiled all patched scripts via `python3 -m py_compile ...` (pass)
2. emitted and reconciled exocortex smoke event via:
   - `python3 operators/exocortex/exocortex_event_bridge.py ...` (pass)
   - `python3 operators/runtime/reconcile-ajna-events.py` (pass)
3. exercised representative bridges:
   - `cloudflare_domain_bridge.py` (pass)
   - `channel_surface_bridge.py --channel slack` (pass)

## Outcome

Operator pathing is now aligned with the current shell topology, reducing hidden breakage across exocortex ingestion and runtime reconciliation.
