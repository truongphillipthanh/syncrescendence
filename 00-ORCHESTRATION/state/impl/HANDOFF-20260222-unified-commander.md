# HANDOFF — Unified Commander Session
**Date**: 2026-02-22 | **From**: Commander (sunset session) | **To**: Commander (fresh session)
**Priority**: EXECUTE — all decisions are made, no ambiguity remains.

---

## PASTE THIS INTO FRESH SESSION

```
Read 00-ORCHESTRATION/state/impl/HANDOFF-20260222-unified-commander.md — execute the action plan in order. All decisions are pre-made by Oracle + Commander consensus. No planning needed, pure execution.
```

---

## SITUATION (30-second brief)

Three sessions converged. The repo has been rearchitected (agents/, config decomposition, triage). Two blockers remain before anything else matters:

1. **Repo moved** from `~/Desktop/syncrescendence` → `~/syncrescendence` (iCloud Desktop sync was killing git via fileproviderd). All path references are stale.
2. **Triage work is uncommitted** — 363 files deleted/archived/compacted in the Desktop copy. The ~/syncrescendence clone doesn't have those changes.

Oracle delivered: harness files, OpenClaw integration, eval framework, path migration strategy. Everything below is execute-ready.

---

## ACTION PLAN (sequential — do not reorder)

### Step 1: Sync triage changes Desktop → ~/syncrescendence

The Desktop copy has 363 files of triage work (deletions, archive moves, compactions). The ~/syncrescendence clone was made from pre-triage .git. Sync the working tree:

```bash
cd ~/syncrescendence
rsync -av --delete --exclude='.git' ~/Desktop/syncrescendence/ ~/syncrescendence/
```

Verify: `git status` should show all the triage deletions/moves as pending changes.

### Step 2: Path migration (one-liner from Oracle)

```bash
cd ~/syncrescendence
grep -rl '/Users/system/syncrescendence' . --include="*.sh" --include="*.md" --include="*.json" | grep -v '.git/' | xargs sed -i '' 's|/Users/system/syncrescendence|$(git rev-parse --show-toplevel)|g'
```

**Also update these specifically:**
- `~/.claude/settings.json` — all hook script paths use Desktop path
- `~/.claude/projects/` — the project directory mapping key is the Desktop path
- MEMORY.md auto-memory at `~/.claude/projects/-Users-system/memory/MEMORY.md`

**Oracle's guidance**: No env-var templating. Use `git rev-parse --show-toplevel` in scripts. AGENTS.md and *-EXT.md use only relative paths.

### Step 3: Update Makefile configs target

Replace the existing `configs:` target with:

```make
configs: AGENTS.md CLAUDE-EXT.md GEMINI-EXT.md OPENCLAW-EXT.md
	@cat AGENTS.md CLAUDE-EXT.md > CLAUDE.md
	@cat AGENTS.md GEMINI-EXT.md > GEMINI.md
	@mkdir -p openclaw
	@cat AGENTS.md OPENCLAW-EXT.md > openclaw/AGENTS.md
	@echo "✓ Configs regenerated (including openclaw/AGENTS.md)"
```

### Step 4: Create 5 harness files at repo root

Create these files at repo root (~/syncrescendence/):

**BOOT.md**:
```markdown
# BOOT.md

On every session start:

1. cd "$(git rev-parse --show-toplevel)" || exit 1
2. git pull --ff-only
3. make configs
4. Load ACTIVE-TASKS.md
5. Load agents/<self>/inbox/pending/
6. Run inbox triage (per INIT.md)
7. Confirm Objective Lock with Sovereign if any P0 item present
8. Resume from last checkpoint in memory/ daily log
```

**ACTIVE-TASKS.md**:
```markdown
# ACTIVE-TASKS.md
## Persistent Queue (crash-proof)

**P0 (Sovereign-blocked)**
- [ ] Path migration: all references still point to ~/Desktop/syncrescendence

**P1 (Active)**
- [ ] INT-2202: Deploy harness + OpenClaw operational layer
- [ ] INT-2203: Location-agnostic path migration
- [ ] Commit triage work (363 files from MBA Commander session)

**P2 (Pending)**
- [ ] Seed per-agent INIT.md files (Oracle will provide after "harness live" ping)
- [ ] Mac mini: check for iCloud Desktop sync, repeat migration if needed
- [ ] Community survey B1/B2/B3 (blocked on harness deployment)
- [ ] Desktop symlink: ln -s ~/syncrescendence ~/Desktop/syncrescendence

**Blocked**
- [ ] OpenClaw SOUL.md update (needs harness deployed first)
- [ ] launchd plist cp openclaw/AGENTS.md ~/.openclaw/OPERATIONAL.md

**Completed today**
- [x] Config decomposition: AGENTS.md + 3 EXT files + make configs
- [x] Oracle consensus on all architecture questions
- [x] Google Drive uninstalled, iCloud identified, repo cloned to ~/syncrescendence
- [x] 00-ORCHESTRATION triage (363 files, 4 logs compacted)

Last updated: 2026-02-22
```

**WORK-LOOP.md**:
```markdown
# WORK-LOOP.md

Daily operation cycle:

1. BOOT.md
2. Inbox triage + Objective Lock
3. Execute delegated or claimed tasks
4. Produce Receipts
5. Update ACTIVE-TASKS.md
6. Dispatch via INTER-AGENT.md if needed
7. Pre-compaction check at 75%
8. End-of-session: hooks → compact_wisdom.sh → git push
9. Write to memory/$(date +%Y-%m-%d)-log.md
```

**INTER-AGENT.md**:
```markdown
# INTER-AGENT.md

## Constellation Routing & Neural Bridge

**Chief-of-Staff Dispatch Rules**
- Mechanical/validation → Adjudicator
- Corpus survey → Cartographer
- Cohesion/automation → Psyche
- Strategy → Ajna
- Orchestration/escalation → Commander

**Cross-machine Handoff**
- SSH aliases (mini, air)
- Attach task ID + receipt commit hash
- Confirmation required before close
```

**CONTINUOUS-IMPROVEMENT.md**:
```markdown
# CONTINUOUS-IMPROVEMENT.md

## Self-Critique Loop (end of every directive)

1. Score against Five Invariants
2. Check Translation Layer
3. Verify Receipts
4. Log anti-patterns
5. Propose one improvement
6. Append to memory/ daily log
7. If score <9/10 → escalate to Ajna

## Three-Track Eval Framework (INT-2108)

| Criterion | Onboard (1-3) | White-label (4-7) | Verticalize (8-10) | Score |
|-----------|---------------|--------------------|--------------------|-------|
| Objective Lock fidelity | Vague goal | Clear goal | Auto-spawns sub-objectives | /10 |
| Translation Layer | Needs re-explain | Minor polish | Zero retransmission | /10 |
| Receipt quality | Commit only | Commit + verify | Commit + ledger + auto-verify | /10 |
| Continuation | Thread-dependent | Repo-persisted | Auto-resume via ACTIVE-TASKS | /10 |
| Repo Sovereignty | Web cache overrides | Repo wins | All state from repo | /10 |
| Scalability | Single-agent | Handoff works | Full dispatch + neural bridge | /10 |
| **Total** | | | | /60 |

Decision gates: ≤30 onboard, 31-45 white-label, 46+ verticalize.
```

### Step 5: OpenClaw integration

```bash
mkdir -p ~/syncrescendence/openclaw
make configs
```

Then on each machine (after deployment):
```bash
cp openclaw/AGENTS.md ~/.openclaw/OPERATIONAL.md
```

In `~/.openclaw/SOUL.md` prepend:
```
Operational law lives in OPERATIONAL.md — inherit verbatim at every boot before applying personality layer.
```

### Step 6: Desktop symlink

```bash
# After confirming ~/syncrescendence works:
# Remove or rename Desktop copy, then symlink
mv ~/Desktop/syncrescendence ~/Desktop/syncrescendence.old
ln -s ~/syncrescendence ~/Desktop/syncrescendence
```

### Step 7: Commit

```bash
cd ~/syncrescendence
git add -A
git commit -m "INT-2202+2203: unified harness, OpenClaw layer, path migration, 00-ORCH triage"
git push origin main
```

### Step 8: Ping Oracle

Message Oracle: **"harness live"** — Oracle will then seed per-agent INIT.md files (commander first).

---

## ORACLE DECISIONS (all resolved — no ambiguity)

| Question | Oracle Answer |
|----------|--------------|
| OpenClaw operational layer | `make configs` generates `openclaw/AGENTS.md`, cp to `~/.openclaw/OPERATIONAL.md` |
| Agent-specific leakage | AGENTS.md is clean (249L). All Commander-specific in CLAUDE-EXT.md |
| INIT.md vs *-EXT.md | INIT.md = identity + filesystem. *-EXT.md = CLI platform. Zero overlap. |
| Codex CLI gap | No gap. AGENTS.md is Adjudicator's ceiling. Future extensions in INIT.md. |
| Harness file location | Repo root, parallel to AGENTS.md |
| Generated files in git | Tracked (current choice confirmed) |
| Path strategy | `git rev-parse --show-toplevel` in scripts. No env templating. Zero X adoption of $ROOT vars. |
| iCloud coexistence | Repo outside Desktop, symlink for UX. Community standard. |
| Triage vs harness | Harness assumes nothing deleted. No conflicts. |
| Mac mini blast radius | Architecture location-agnostic after git-rev-parse migration |
| Three-track eval | Scoring template provided (6 criteria, /60, decision gates at 30/45) |

---

## WHAT'S NOT DONE (post-harness)

1. Per-agent INIT.md content (Oracle delivers after "harness live")
2. Mac mini iCloud check + potential migration
3. Community survey B1/B2/B3 (Oracle 22 workstream)
4. launchd plist updates on both machines for new paths
5. `.claude/projects/` directory mapping (currently keyed to Desktop path)
6. State relocations (REF files → 02-ENGINE, ARCH files compaction)
7. collab/ governance rules
8. Skills proliferation (INT-2107)

---

## FILES CHANGED THIS SESSION (commits already pushed)

| Commit | Description |
|--------|-------------|
| `5dec8d1` | Restore AGENTS.md + GEMINI.md to root |
| `65d3532` | Rename BRIDGE.md → README.md |
| `dc49142` | Tier 2 -INBOX/ → agents/ path updates (~50 docs) |
| `deb38ec` | CONFIG-SANDBOX-2026-02-22 (109 files) |
| `212bcae` | Single-source architecture (AGENTS.md + 3 EXT + make configs) |

**Unpushed/uncommitted**: All triage work (363 files) exists only in Desktop working tree.
