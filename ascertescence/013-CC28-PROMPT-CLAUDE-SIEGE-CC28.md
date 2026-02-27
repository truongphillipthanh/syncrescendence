# SIEGE CC28 — Claude Code Parallel Session

**Agent**: Commander (fresh Claude Code session)
**Repo**: `/Users/system/syncrescendence` (main branch)
**Date**: 2026-02-24
**Reply-To**: commander
**CC**: commander

---

## TASK 1: Full Atom Clustering Run

Run the full atom clustering pipeline that CC27 built but never executed at scale.

```bash
cd /Users/system/syncrescendence
python3 orchestration/00-ORCHESTRATION/scripts/atom_cluster.py --repo-root /Users/system/syncrescendence --top-n 200
```

1. Capture the full output
2. Read the generated `sources/04-SOURCES/_meta/DYN-ATOM_CLUSTER_SUMMARY.md`
3. Cross-reference the top 20 sovereign_review atoms against `orchestration/00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` — which atoms address active intentions?
4. Write findings to `agents/commander/outbox/RESULT-CLAUDE-CC28-ATOM_TRIAGE.md`

## TASK 2: Intention Pruning Recon

Read `orchestration/00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md` (97 active intentions, target: 30-40).

For each intention, classify as:
- **ACTIVE** — still relevant, has open work
- **DONE** — already accomplished (cite evidence: commit, file, or handoff)
- **STALE** — no activity in 5+ sessions, no blocking dependency
- **MERGED** — subsumed by another intention

Write the draft cut list to `agents/commander/outbox/RESULT-CLAUDE-CC28-INTENTION_PRUNING_DRAFT.md`. Format as a table: `| INT-ID | Title | Verdict | Evidence |`

Do NOT delete or modify the intention compass. This is recon only — Sovereign approves cuts.

## TASK 3: Chat Agent Portal Draft

Oracle CC28 recommended a portal document for chat-based agents (Gemini) who can't crawl the repo.

Draft `orchestration/00-ORCHESTRATION/PORTAL-CHAT-AGENTS.md` containing:
1. One-paragraph system description + invariants from AGENTS.md
2. Current phase status from DYN-DEFERRED_COMMITMENTS.md
3. Top 10 active intentions from ARCH-INTENTION_COMPASS.md
4. Key script invocation patterns (dispatch.sh, atom_cluster.py, scaffold_validate.sh)
5. Memory status summary
6. SN quick-ref glossary (from sn_symbols.yaml)
7. Raw GitHub link template for depth: `https://github.com/truongphillipthanh/syncrescendence/blob/main/<path>`

Target: 1800-2800 tokens. This is the single context injection for Diviner relay.

---

## CONSTRAINTS
- Commit each deliverable separately with semantic prefix
- Do not modify AGENTS.md or CLAUDE.md
- Do not create new top-level directories
- Run verification before claiming done
- Write RESULT files to `agents/commander/outbox/`
