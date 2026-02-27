# PROMPT — Adjudicator: Integration Review (CC37 Phase 4)

**From**: Commander (CC37)
**To**: Adjudicator (Codex Desktop App)
**Reply-To**: Commander
**CC**: Commander
**Date**: 2026-02-26
**Build Phase**: Phase 4 — Integration

## Delivery Contract

**Write your review to**: `-INBOX/commander/00-INBOX0/RESPONSE-ADJUDICATOR-INTEGRATION_REVIEW-CC37.md`
**Format**: Markdown with GO/CONDITIONAL/REJECT per integration point
**Verification**: Commander will read from that exact path

## What Was Integrated

### 1. Annealer Gate in protease_promote.py

`protease_promote.py` now calls `candidate_adapter.py` → `lattice_annealer.py` as a mandatory pre-promotion gate for `--target canon`:

- Each axiom block is adapted via `candidate_adapter.py` then scored by `lattice_annealer.py --mode gate`
- PROMOTE → proceed with canon promotion
- ADJUST → block promotion, print repair prompt to stderr
- REJECT → block promotion, print reason codes
- If any axiom is blocked, the entire batch fails (unless `--skip-annealer` flag for testing)
- Added `subprocess` import, `run_annealer_gate()` function (~65 LOC)
- `--skip-annealer` flag for backward compatibility (prints warning)

**Review for**: Race conditions (subprocess calls during promotion), lock order compliance (adapter doesn't lock, annealer acquires LOCK_LATTICE_INDEX → LOCK_LATTICE_HEALTH → LOCK_ANNEAL_LOG), error handling (timeout, bad JSON, missing scripts), whether the adapter_input construction from axiom blocks is correct.

### 2. launchd Plist for Tension Monitor

`com.syncrescendence.dag-tension-monitor.plist` — runs `dag_tension_monitor.py --mode monitor` every 6 hours (21600s):

- WorkingDirectory: repo root
- EnvironmentVariables set (launchd doesn't source .zshrc — seared lesson)
- Stdout/stderr to state/ log files
- RunAtLoad: false (don't fire on boot, wait for first interval)
- Nice: 10 (low priority)

**Review for**: Plist correctness, env var sufficiency, log rotation concerns, whether RunAtLoad should be true for initial baseline.

### 3. Files Changed

| File | Change |
|------|--------|
| `orchestration/00-ORCHESTRATION/scripts/protease_promote.py` | +subprocess import, +run_annealer_gate(), +--skip-annealer flag, +gate call before canon promotion |
| `orchestration/00-ORCHESTRATION/scripts/com.syncrescendence.dag-tension-monitor.plist` | NEW — launchd scheduled task |

### 4. What You Should Check

1. **Lock order**: Does the subprocess call to lattice_annealer from inside protease_promote create a lock inversion risk? protease_promote doesn't hold locks, so the annealer's lock acquisition should be clean — but verify.
2. **Subprocess isolation**: The annealer runs as a child process. If protease_promote is killed mid-gate, does the annealer leave orphaned locks? (PID-based stale lock detection should handle this.)
3. **Adapter input fidelity**: The `adapter_input` dict in `run_annealer_gate()` constructs from axiom block fields. Verify the mapping is correct per `ARCH-CANDIDATE_ADAPTER_CONTRACT.yaml`.
4. **Batch atomicity**: If 3 axioms are being promoted and axiom 2 fails the annealer, axioms 1's gate result is discarded and no atoms are transitioned. Is this the right behavior?
5. **Plist**: Is the plist valid XML? Are env vars sufficient? Should we add `LANG=en_US.UTF-8` for Python encoding?

## Reference Files

- `ARCH-LOCK_HIERARCHY.yaml` — global lock order
- `ARCH-CANDIDATE_ADAPTER_CONTRACT.yaml` — adapter schema
- `CANON-ONTOLOGY-GATE_v2.md` — policy requiring mandatory annealer
- `RESPONSE-ADJUDICATOR-BID-CC35.md` — your bid with amendments
