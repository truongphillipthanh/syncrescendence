# SIEGE CC28 — Lane 1: Protease Queue Builder

**Agent**: Commander (Claude Code)
**Repo**: `/Users/system/syncrescendence` (main branch)
**Date**: 2026-02-24
**Reply-To**: commander
**CC**: commander

---

## OBJECTIVE

Build `protease_queue.py` — the first half of the Protease Protocol (Adjudicator Spec 1). This script reads atom clustering output and the intention compass, then generates a prioritized "chewing queue" of atoms for Sovereign review.

## SPEC (from Adjudicator CC28)

### Architecture
```
DYN-ATOM_SCORE_AUDIT.jsonl + DYN-ATOM_INDEX.jsonl + DYN-ATOM_CLUSTER_MANIFEST.jsonl
    + ARCH-INTENTION_COMPASS.md (active intentions)
    -> protease_queue.py
    -> DYN-PROTEASE_QUEUE.jsonl (machine-readable)
    -> DYN-PROTEASE_QUEUE.md (Sovereign chewing queue; grouped by intention)
```

### Input Files
- `sources/04-SOURCES/_meta/DYN-ATOM_SCORE_AUDIT.jsonl` — per-atom 6D scores
- `sources/04-SOURCES/_meta/DYN-ATOM_INDEX.jsonl` — atom metadata with `integration_status` field
- `sources/04-SOURCES/_meta/DYN-ATOM_CLUSTER_MANIFEST.jsonl` — cluster assignments
- `orchestration/00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — active intentions (markdown table)

### Output Files
- `orchestration/00-ORCHESTRATION/state/DYN-PROTEASE_QUEUE.jsonl` — machine-readable queue
  - Fields: `atom_id`, `source_file`, `excerpt` (first 200 chars), `matched_intentions` (list of INT-IDs), `priority_score`, `cluster_id`, `band` (sovereign_review|auto_promote), `status` (queued|consumed|promoted_praxis|promoted_canon|rejected)
- `orchestration/00-ORCHESTRATION/state/DYN-PROTEASE_QUEUE.md` — human-readable, grouped by intention
  - Header with queue stats (total, per-intention, per-band)
  - Sections per matched intention with atom excerpts
  - Unmatched sovereign_review atoms in a separate section

### Logic
1. Load all atoms from DYN-ATOM_INDEX.jsonl where `integration_status == "pending"`
2. Filter to `band in ("sovereign_review", "auto_promote")` from DYN-ATOM_SCORE_AUDIT.jsonl
3. Parse ARCH-INTENTION_COMPASS.md for active intentions (extract INT-ID + title + keywords)
4. For each atom, compute intention match: keyword overlap between atom content and intention title/keywords. Score = weighted sum of keyword hits.
5. Sort by priority_score descending
6. Write both outputs with `--max-atoms N` flag (default 120)
7. Respect temp-file-validate-rename pattern for JSONL writes

### CLI
```bash
python3 orchestration/00-ORCHESTRATION/scripts/protease_queue.py \
  --repo-root /Users/system/syncrescendence \
  --max-atoms 120
```

### Failure Modes to Handle
- Intention matcher overfits keywords → use hybrid: priority keyword overlap + fallback to cluster context
- JSONL corruption → temp file + validate + atomic rename
- Empty sovereign_review set → warn but still generate queue from auto_promote if available

## CONSTRAINTS
- Write to `orchestration/00-ORCHESTRATION/scripts/protease_queue.py`
- ~400 LOC target
- Use only stdlib (json, csv, re, pathlib, argparse, tempfile, shutil). No pip installs.
- Read `orchestration/00-ORCHESTRATION/scripts/config.py` for path patterns (source it if useful, but don't depend on it — use argparse `--repo-root` as primary)
- Commit with prefix `feat: CC28-L1 protease queue builder`
- Run the script after building and include output in commit message or a verification note
- Do NOT modify any files outside your lane (see lane map above)
