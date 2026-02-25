# SIEGE CC28 — Lane 2: Protease Promote

**Agent**: Commander (Claude Code)
**Repo**: `/Users/system/syncrescendence` (main branch)
**Date**: 2026-02-24
**Reply-To**: commander
**CC**: commander

---

## OBJECTIVE

Build `protease_promote.py` — the second half of the Protease Protocol (Adjudicator Spec 1). This script takes Sovereign-rewritten axioms and promotes them into praxis/canon, updating atom lifecycle status.

## SPEC (from Adjudicator CC28)

### Architecture
```
Sovereign rewrites selected atoms -> 50-token SN axioms (template-constrained)
    -> protease_promote.py --target praxis|canon
    -> SN artifact append (praxis or canon)
    -> DYN-ATOM_INDEX.jsonl status update: pending -> consumed -> promoted_*
    -> DYN-PROTEASE_METRICS.jsonl + DYN-PROTEASE_METRICS.md
```

### Input
- `orchestration/00-ORCHESTRATION/state/DYN-PROTEASE_QUEUE.jsonl` — the queue (built by Lane 1)
- Sovereign-authored axiom file (passed via CLI arg): a markdown file containing SN blocks with `source_atom_ids` and `why_preserved` fields
- `--target praxis|canon` — destination tier

### Queue JSONL Format (from Lane 1)
Each line: `{"atom_id": "...", "source_file": "...", "excerpt": "...", "matched_intentions": ["INT-XXXX"], "priority_score": 0.85, "cluster_id": 7, "band": "sovereign_review", "status": "queued"}`

### Output Files
- Append axiom to target SN file:
  - praxis target: `praxis/05-SIGMA/practice/PRAC-PROTEASE_AXIOMS.sn.md`
  - canon target: `canon/01-CANON/sn/CANON-PROTEASE_AXIOMS.sn.md`
- Update `sources/04-SOURCES/_meta/DYN-ATOM_INDEX.jsonl` — transition `integration_status`:
  - `pending -> consumed` (when axiom submitted)
  - `consumed -> promoted_praxis` or `consumed -> promoted_canon` (after append succeeds)
- Write metrics to `orchestration/00-ORCHESTRATION/state/DYN-PROTEASE_METRICS.jsonl`:
  - Fields: `timestamp`, `atoms_in`, `atoms_out`, `compression_ratio`, `target_tier`, `intention_coverage` (list of INT-IDs served), `axiom_token_count`
- Write human-readable `orchestration/00-ORCHESTRATION/state/DYN-PROTEASE_METRICS.md`

### State Machine (ENFORCED)
```
pending -> queued -> consumed -> promoted_praxis
                              -> promoted_canon
                              -> rejected
```
- Re-promotion of same atom must HARD FAIL (idempotency)
- Only valid transitions above — reject any other

### CLI
```bash
# Promote a batch of axioms to praxis
python3 orchestration/00-ORCHESTRATION/scripts/protease_promote.py \
  --repo-root /Users/system/syncrescendence \
  --axiom-file /path/to/sovereign_axioms.md \
  --target praxis

# Dry run
python3 orchestration/00-ORCHESTRATION/scripts/protease_promote.py \
  --repo-root /Users/system/syncrescendence \
  --axiom-file /path/to/sovereign_axioms.md \
  --target canon \
  --dry-run
```

### Axiom File Format (what Sovereign writes)
```markdown
## Axiom: <title>

> <50-token SN axiom in Sovereign's voice>

- source_atom_ids: [atom_001, atom_042]
- why_preserved: <1-sentence rationale>
- matched_intention: INT-XXXX
```

### Failure Modes to Handle
- Re-promotion duplicates → enforce state machine, reject non-pending/queued transitions
- JSONL corruption during index write → temp file + validate + atomic rename
- SN output too lossy → require `source_atom_ids` + `why_preserved` in each block
- Missing queue file → clear error message, exit 1

## CONSTRAINTS
- Write to `orchestration/00-ORCHESTRATION/scripts/protease_promote.py`
- ~360 LOC target
- Use only stdlib
- Create empty target SN files if they don't exist (with proper headers)
- Commit with prefix `feat: CC28-L2 protease promote + lifecycle state machine`
- Include a test: create a small mock axiom file, run promote with --dry-run, verify output
- Do NOT modify any files outside your lane
