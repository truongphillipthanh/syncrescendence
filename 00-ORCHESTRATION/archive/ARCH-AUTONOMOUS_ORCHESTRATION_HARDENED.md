# Hardened Autonomous Orchestration Architecture

## Objective
Eliminate split-brain and silent breakage by making repository integrity a mandatory control-plane gate, then enforcing bounded autonomy with explicit breaker and budget semantics.

## Layered Control Plane
1. Layer 0: Integrity Plane
- Script: `00-ORCHESTRATION/scripts/repo_integrity_gate.sh`
- Checks:
  - `.git/index.lock` absence
  - invalid ref artifacts under `.git/refs*` (`.DS_Store`, spaced ref names)
  - required tracked roots in `HEAD` (`-INBOX`, `-OUTGOING`, `00-ORCHESTRATION`)
  - optional strict `git fsck --full` mode
- Behavior: fail-closed, emit `-SOVEREIGN/INCIDENT-INTEGRITY-*`.

2. Layer 1: Execution Plane (Ingest)
- Script: `00-ORCHESTRATION/scripts/auto_ingest_loop.sh`
- Hardening:
  - integrity + breaker gating before autonomous writes
  - structured failure envelope:
    - `Failure-Code`
    - `Failure-Class`
    - `Failure-Retryable`
    - `Failure-Reason`
  - monotonic attempts (`Retry-Count`, `Attempt`)
  - lease IDs (`Lease-ID`) in state + confirm receipts
  - per-agent heartbeat files under `00-ORCHESTRATION/state/heartbeat/`
  - hourly retry budget caps

3. Layer 2: Recovery Plane (Watchdog)
- Script: `00-ORCHESTRATION/scripts/constellation_watchdog.sh`
- Liveness model is multi-signal:
  - pane output signal
  - heartbeat age
  - artifact movement age
- Recovery policy:
  - heartbeat nudge only when heartbeat + movement are both stale
  - interrupt only when both are stale past interrupt thresholds

4. Layer 3: Orchestration Plane
- Script: `00-ORCHESTRATION/scripts/proactive_orchestrator.sh`
- Hardening:
  - Layer-0 gate before cycle mutation
  - circuit breaker states: `OPEN`, `HALF_OPEN`, `CLOSED`
  - hard budgets:
    - max dispatches per cycle
    - max net new tasks per day
    - max concurrent failed backlog threshold
  - capability-aware routing:
    - Cartographer: sensing/survey
    - Adjudicator: verification/audit
    - Psyche/Commander: implementation/infra
  - queue rendering is filename-safe (no word-splitting loops)

## Breaker Semantics
- File: `00-ORCHESTRATION/state/breakers/orchestration.breaker`
- `OPEN`:
  - dispatch/retry paused
  - wait for cooldown and/or operator remediation
- `HALF_OPEN`:
  - limited dispatch (single-cycle probe)
- `CLOSED`:
  - normal bounded operation

## Verification Plane
- Primary verifier:
  - `00-ORCHESTRATION/scripts/verify_orchestration_hardening.sh`
- Checks:
  - strict integrity gate
  - executable/syntax checks for core scripts
  - breaker state sanity
  - unsafe queue iteration pattern guard

## Expected Operator Workflow
1. Run `verify_orchestration_hardening.sh`.
2. If integrity fails, repair refs/index and re-run verification.
3. Ensure breaker transitions to `CLOSED` before normal autonomy.
4. Monitor:
  - `00-ORCHESTRATION/state/DYN-CONSTELLATION_STATE.md`
  - `00-ORCHESTRATION/state/DYN-CONSTELLATION_HEALTH.md`
  - `00-ORCHESTRATION/state/.orchestrator_last_run`

## Design Constraint
Autonomy is subordinate to integrity. If integrity is uncertain, system behavior must be conservative and fail-closed.
