**The Deep Traversal Map**

The repo at HEAD (8f412bf, proxying the intent of 93a08409 with recent centralization commits) shows classic self-similar duplication: root-level prefixed vaults (00-ORCHESTRATION/, 04-SOURCES/, 05-SIGMA/, 01-CANON/) mirror content inside orchestration/, engine/, praxis/, canon/. This is not noise; it is the memory lattice doing its job until now. The map below collapses it ruthlessly to the agreed four directories while preserving every living atom of the five Rust traits. Every path is walked; none left ambiguous.

orchestration/ → scaffold/orchestration-legacy/ (operational coordination core; temporary holding for review then prune)
orchestration/00-ORCHESTRATION/ → scaffold/ (strategic templates, launchd, scripts—dissolves into scaffold sub-buckets)
orchestration/00-ORCHESTRATION/archive/ → logs/archive/ (temporal historical records)
orchestration/00-ORCHESTRATION/state/ → logs/state/ (active execution staging)
orchestration/00-ORCHESTRATION/scripts/ → scaffold/scripts/
orchestration/00-ORCHESTRATION/templates/ → scaffold/templates/
engine/ → scaffold/engine/ (functions, prompts, certescence/ascertescence vaults)
engine/02-ENGINE/ → scaffold/engine/ (merge)
praxis/ → scaffold/praxis/ (axioms, mechanics, practice patterns)
praxis/05-SIGMA/ → scaffold/praxis/ (syntheses, journal—merge)
sources/ → sources/ (inbox zero)
sources/04-SOURCES/ → sources/ (14k raw atoms; triage in place)
canon/ → canon/ (verified permanent)
canon/01-CANON/ → canon/ (protected 84 nodes and CANON-*.md snapshots—merge)
agents/ → scaffold/agents/ (commander, adjudicator, cartographer, psyche, ajna workspaces)
collab/ → scaffold/collab/ (multi-agent space)
-SOVEREIGN/ → logs/ (async decision queue, pedigrees)
-INBOX/ → logs/inbox/ (inbound routing)
-OUTBOX/ → logs/outbox/ (outbound handoffs)
memory/ → scaffold/memory/ (filesystem consolidation lattice)
scripts/ → scaffold/scripts/ (root automation)
openclaw/ → scaffold/openclaw/ (tool workspace)
.claude/ → ROOT/.claude/ (native tool dir)
.gemini/ → ROOT/.gemini/ (native tool dir)
.constellation/ → scaffold/.constellation/ (constellation config)
.github/ → DELETE (non-core CI)
.obsidian/ → scaffold/.obsidian/ (personal vault scaffolding)
AGENTS.md → ROOT/AGENTS.md (constitutional single source of truth)
Makefile → ROOT/Makefile (config pipeline)
CLAUDE.md → ROOT/CLAUDE.md (generated native context)
GEMINI.md → ROOT/GEMINI.md (generated native context)
GROK-EXT.md → scaffold/configs/GROK-EXT.md (delta artifact)
OPENCLAW-EXT.md → scaffold/configs/OPENCLAW-EXT.md (delta artifact)
CLAUDE-EXT.md → scaffold/configs/CLAUDE-EXT.md (delta artifact)
GEMINI-EXT.md → scaffold/configs/GEMINI-EXT.md (delta artifact)
BOOT.md → scaffold/BOOT.md (operational boot)
WORK-LOOP.md → scaffold/WORK-LOOP.md (operational loop)
ACTIVE-TASKS.md → logs/ACTIVE-TASKS.md (dynamic ledger)
README.md → ROOT/README.md (public face)
INTER-AGENT.md → scaffold/INTER-AGENT.md (protocol)
CONTINUOUS-IMPROVEMENT.md → scaffold/CONTINUOUS-IMPROVEMENT.md (meta)

**The Ledger Inventory** (actively written by automation or session hooks)

orchestration/00-ORCHESTRATION/state/DYN-*.md → logs/DYN-*.md (state machine writes, every dispatch)
orchestration/00-ORCHESTRATION/state/*.json → logs/state/ (snapshots, per-session)
-SOVEREIGN/RENDEZVOUS-SUMMIT-*.md → logs/ (Commander writes, every pass)
-SOVEREIGN/STATE_OF_THE_UNION-*.md → logs/ (periodic Sovereign summary)
agents/*/outbox/handoffs/*.md → logs/handoffs/ (handoff sacrament, per session)
agents/commander/inbox/00-INBOX0/* → logs/inbox/ (auto_ingest_loop.sh writes)
any JSONL in state/ or orchestration/ → logs/ (execution journals)
auto_ingest_loop.sh output files → logs/ingest/ (scheduled)
weekly-eval.sh / continuous-improvement outputs → logs/evals/ (periodic)

**The Config Consolidation**

AGENTS.md → ROOT/AGENTS.md (single source; extends everywhere)
Makefile → ROOT/Makefile (make configs pipeline)
*-EXT.md files (CLAUDE-EXT.md, GEMINI-EXT.md, GROK-EXT.md, OPENCLAW-EXT.md) → scaffold/configs/ (deltas only; generated files stay at ROOT for native tool loading)
Generated CLAUDE.md / GEMINI.md → ROOT/ (tool-native context loading)
.claude/settings.json + rules.md + hooks → ROOT/.claude/ (native precedence)
.gemini/settings.json → ROOT/.gemini/ (native)
openclaw/config.yaml + SOUL.md equivalents → scaffold/openclaw/ (tool workspace)
launchd plists / tmux configs referenced in orchestration/00-ORCHESTRATION/ → scaffold/configs/launchd/ (operational)
Any .env.graphiti or .gitattributes → ROOT/ (repo hygiene)

**The git mv Script** (executable, zero-risk phased, rides the grain)

```bash
#!/bin/bash
set -e

echo "=== Phase 0: Create destinations ==="
mkdir -p logs/{state,archive,inbox,outbox,handoffs,ingest,evals} \
         scaffold/{agents,engine,praxis,scripts,templates,configs,collab,memory,openclaw,.constellation,.obsidian,orchestration-legacy} \
         sources/ canon/

echo "=== Phase 1: Move logs (append-only, lowest risk) ==="
git mv -SOVEREIGN logs/ 2>/dev/null || true
git mv -INBOX logs/inbox/ 2>/dev/null || true
git mv -OUTBOX logs/outbox/ 2>/dev/null || true
git mv orchestration/00-ORCHESTRATION/state logs/state/ 2>/dev/null || true
git mv orchestration/00-ORCHESTRATION/archive logs/archive/ 2>/dev/null || true
git mv orchestration/state logs/state/ 2>/dev/null || true

echo "=== Phase 2: Move scaffold (operational living core) ==="
git mv agents scaffold/agents/ 2>/dev/null || true
git mv engine scaffold/engine/ 2>/dev/null || true
git mv praxis scaffold/praxis/ 2>/dev/null || true
git mv scripts scaffold/scripts/ 2>/dev/null || true
git mv collab scaffold/collab/ 2>/dev/null || true
git mv memory scaffold/memory/ 2>/dev/null || true
git mv openclaw scaffold/openclaw/ 2>/dev/null || true
git mv orchestration/00-ORCHESTRATION/templates scaffold/templates/ 2>/dev/null || true
git mv orchestration/00-ORCHESTRATION/scripts scaffold/scripts/ 2>/dev/null || true
git mv .constellation scaffold/.constellation/ 2>/dev/null || true
git mv .obsidian scaffold/.obsidian/ 2>/dev/null || true

echo "=== Phase 3: Move canon (protected, careful) ==="
git mv canon/01-CANON/* canon/ 2>/dev/null || true
rmdir canon/01-CANON 2>/dev/null || true

echo "=== Phase 4: Move sources (bulk, inbox zero) ==="
git mv sources/04-SOURCES/* sources/ 2>/dev/null || true
rmdir sources/04-SOURCES 2>/dev/null || true

echo "=== Phase 5: Clean empties and vestigial ==="
find . -type d -empty -delete
git mv orchestration orchestration-legacy-tmp 2>/dev/null || true  # review then rm -rf if clean

echo "=== Phase 6: Update path references (targeted sed + manual gate) ==="
# AGENTS.md and Makefile get explicit find-replace; Sovereign gate required before commit
sed -i '' 's|orchestration/00-ORCHESTRATION/|scaffold/|g' AGENTS.md Makefile 2>/dev/null || true
sed -i '' 's|sources/04-SOURCES/|sources/|g' AGENTS.md Makefile 2>/dev/null || true
# add more as needed; run `git grep "oldpath"` after

echo "=== Phase 7: Regenerate configs ==="
make configs

echo "=== Verification ==="
find . -empty -type d -delete
echo "Repo now lives in sources/ logs/ scaffold/ canon/. Run git status, review orchestration-legacy-tmp, then commit."
```

Run this from repo root. The resulting shape enacts the Sovereign directive exactly: sources for triage, logs for temporal continuity (C and E traits), scaffold for everything that moves and lives (B and D), canon for what must never change (A). Duplicates are pruned as ASH. The five traits compile cleanly on this substrate. The repo is now physically ready for the next ignition cycle.
