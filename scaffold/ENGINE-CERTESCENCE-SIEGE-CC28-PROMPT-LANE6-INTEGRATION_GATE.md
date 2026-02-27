# SIEGE CC28 — Lane 6: Integration-First Gate

**Agent**: Adjudicator (Codex)
**Repo**: `/Users/system/syncrescendence` (main branch)
**Date**: 2026-02-24
**Reply-To**: commander
**CC**: commander

---

## OBJECTIVE

Build the Integration-First Gate — a session-close enforcement script that ensures every session produces at least one end-to-end value artifact. This is the constitutional amendment DC-310.

## SPEC (from Adjudicator CC28)

### Dual Enforcement

1. **Session-close gate (primary)**: Checks whether at least one value artifact was produced and atom lifecycle advanced
2. **Commit-time gate (secondary)**: Validates commit trailers point to real value artifacts (future — not in scope for this lane)

### Architecture
```
Session close / PreCompact
    -> integration_gate.py --repo-root <path>
    -> Checks diffs since baseline commit from DYN-SESSION_BASELINE.json
    -> Pass/Fail with explicit report
```

### Pass Condition (ANY of these)
- At least one new/changed file under `praxis/05-SIGMA/` or `canon/01-CANON/sn/`, OR
- At least one `DYN-ATOM_INDEX.jsonl` transition to `consumed` or `promoted_*`, OR
- At least one RESULT-* or HANDOFF-* file created in `agents/commander/outbox/`

### Controlled Bypass
- `INTEGRATION_GATE_BYPASS=1` env var
- Must also create a reason file: `-SOVEREIGN/BYPASS-INTEGRATION_GATE-<timestamp>.md` explaining why
- Script warns loudly on bypass but exits 0

### Input Files (READ ONLY — do not modify)
- `orchestration/00-ORCHESTRATION/state/DYN-SESSION_BASELINE.json` — baseline commit hash
- `sources/04-SOURCES/_meta/DYN-ATOM_INDEX.jsonl` — atom lifecycle states
- Git diff since baseline

### Output
- Stdout: pass/fail report with evidence
- Exit code: 0 = pass, 1 = fail (blocks closure), 0 = bypass (with warning)
- Append gate result to `orchestration/00-ORCHESTRATION/state/DYN-INTEGRATION_GATE_LOG.jsonl`:
  - Fields: `timestamp`, `session_id`, `result` (pass|fail|bypass), `evidence` (list of artifacts), `baseline_commit`, `head_commit`

### CLI
```bash
# Normal check
python3 orchestration/00-ORCHESTRATION/scripts/integration_gate.py \
  --repo-root /Users/system/syncrescendence

# With bypass
INTEGRATION_GATE_BYPASS=1 python3 orchestration/00-ORCHESTRATION/scripts/integration_gate.py \
  --repo-root /Users/system/syncrescendence
```

### Future Hook Wiring (NOT in scope — document only)
- Will be called from `cc_handoff.sh` before final handoff write
- Will be called from PreCompact hook chain

## CONSTRAINTS
- Write to `orchestration/00-ORCHESTRATION/scripts/integration_gate.py`
- ~200 LOC target
- Use only stdlib + subprocess (for git commands)
- Commit with prefix `feat: CC28-L6 integration-first gate (DC-310)`
- Run the script against current session and verify it reports correctly
- Create the gate log file if it doesn't exist
- Do NOT modify cc_handoff.sh, DYN-ATOM_INDEX.jsonl, DYN-SESSION_BASELINE.json, or any files outside your lane
