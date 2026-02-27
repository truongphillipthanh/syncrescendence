# SIEGE CC28 — Lane 3: State Vector Generator

**Agent**: Commander (Claude Code)
**Repo**: `/Users/system/syncrescendence` (main branch)
**Date**: 2026-02-24
**Reply-To**: commander
**CC**: commander

---

## OBJECTIVE

Build `state_vector.py` — Adjudicator Spec 4. Generates a dual-tier state snapshot at session close: Tier 1 (300-token State Vector for epigenetic priming) and Tier 2 (2000-token expanded portal).

## SPEC (from Adjudicator CC28 + Diviner's State Vector concept)

### Architecture
```
PreCompact/SessionClose
    -> state_vector.py --tier both
Collectors:
  phase/dependencies: DYN-DEFERRED_COMMITMENTS.md
  intentions: ARCH-INTENTION_COMPASS.md (active, ranked)
  inhibitions: AGENTS.md anti-patterns + current phase-gate blocks
  output contract: latest active directive/task artifacts
Writers:
  Tier 1 -> DYN-STATE_VECTOR.md (~300 tokens)
  Tier 2 -> DYN-PORTAL_EXPANDED.md (~2,000 tokens)
  optional machine form -> DYN-STATE_VECTOR.json
cc_handoff embeds links to both
```

### Tier 1 — State Vector (300 tokens, Diviner's "Histone Header")
Must contain exactly:
- **Phase**: Current phase + one-line status
- **Inhibitions**: What we are NOT doing (3-5 concrete constraints from AGENTS.md anti-patterns + phase gate)
- **Promoters**: Top 3 active intentions (INT-ID + title)
- **Transcription Factors**: Required output format for current phase
- **Last Safe Point**: commit hash + date

### Tier 2 — Expanded Portal (2000 tokens)
- Everything in Tier 1 plus:
- Phase status table (all phases)
- Top 10 active intentions
- Key script invocations
- Memory status summary
- Recent handoff references
- Depth links (GitHub raw URLs)

### Both tiers generated from same intermediate JSON (prevents Tier divergence)

### Input Files
- `orchestration/00-ORCHESTRATION/state/DYN-DEFERRED_COMMITMENTS.md` — phase status
- `orchestration/00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — intentions
- `AGENTS.md` — anti-patterns section for inhibitions
- `orchestration/00-ORCHESTRATION/state/DYN-SESSION_BASELINE.json` — current session baseline

### Output Files
- `orchestration/00-ORCHESTRATION/state/DYN-STATE_VECTOR.md` — Tier 1
- `orchestration/00-ORCHESTRATION/state/DYN-PORTAL_EXPANDED.md` — Tier 2
- `orchestration/00-ORCHESTRATION/state/DYN-STATE_VECTOR.json` — machine-readable intermediate

### CLI
```bash
python3 orchestration/00-ORCHESTRATION/scripts/state_vector.py \
  --repo-root /Users/system/syncrescendence \
  --tier both
```
Options: `--tier tier1|tier2|both`

### Failure Modes to Handle
- Token budgets exceeded → hard token cap + priority truncation (intentions truncated first, inhibitions preserved)
- Intention parser drift on markdown tables → use regex with fallback
- Inhibitions too generic → generate from concrete anti-pattern lines in AGENTS.md

## CONSTRAINTS
- Write to `orchestration/00-ORCHESTRATION/scripts/state_vector.py`
- ~345 LOC target
- Use only stdlib
- Commit with prefix `feat: CC28-L3 state vector generator (Tier 1 + Tier 2)`
- Run the script and verify Tier 1 is ≤300 tokens, Tier 2 is ≤2000 tokens
- Do NOT modify `AGENTS.md`, `cc_handoff.sh`, or any files outside your lane
