# REINIT: Commander Post-Sync-Bomb Recovery State

**Issued**: 2026-02-17 16:55 UTC
**From**: Commander (self)
**Priority**: P0
**Kind**: REINIT
**Status**: PENDING

---

## What Happened

### The Sync Bomb (2026-02-17 ~08:59-09:15 UTC)
MBA's `git_sync.sh` committed mass deletions of 1070+ files. Root cause was three bugs:
1. No index reset before work — stale `git add -A` from agent sessions contaminated the index
2. Silent failure suppression — `2>/dev/null || true` masked rebase/merge failures
3. No scope guard — committed ALL staged changes, not just INBOX/OUTGOING

### The Deeper Root Cause: Google Drive File Sync
**CRITICAL DISCOVERY**: Both MBA (`/Users/system`) and Mac mini (`/Users/home`) have Google Drive syncing the same account (`truongphillipthanh@gmail.com`). The `.git/` directory is being file-synced between machines via Google Drive. This means:
- MBA commits → Google Drive syncs `.git/objects/` and `.git/refs/` to Mac mini
- Mac mini's HEAD moves WITHOUT `git pull` — working tree doesn't update
- Mac mini agents write files → Google Drive syncs back to MBA → git_sync.sh commits them → loop
- Finder duplicate conflict files (`" 2"`, `" 3"` suffixes) are Google Drive conflict resolution
- `.DS_Store` inside `.git/refs/` = Google Drive Finder integration artifact
- `main 2` ghost branch = Google Drive created duplicate ref file

**This Google Drive sync of .git/ MUST be stopped.** Git requires atomic filesystem operations and file locking. Google Drive provides neither. The proper sync mechanism is git push/pull through GitHub, which already works.

---

## What Was Fixed (Commit a62faeb)

### 1. git_sync.sh Rewritten (`~/.syncrescendence/scripts/git_sync.sh` on MBA)
- Scope guard: only stages `-INBOX/` and `-OUTGOING/`
- Explicit unstage of everything else (scope guard list)
- `flock` prevents concurrent runs
- `git reset HEAD` at start cleans contaminated index
- Safety check: aborts if >20 deletions staged
- Stale `index.lock` cleanup (>5min = remove)
- Proper error handling on fetch/rebase/merge

### 2. Primary Repo Restored from Pre-Bomb Commit 0a604dd
- 1103 files, 303,983 lines restored (including 98 research files in 04-SOURCES/research/)
- All CANON, ENGINE, ORCHESTRATION, SOURCES content recovered

### 3. Hardened Orchestration Scripts Merged (from adjudicator fork)
Source: `/Users/system/syncrescendence-before-full/` (adjudicator's refactored clone)

8 scripts + 1 arch doc copied to primary repo:
- `repo_integrity_gate.sh` — NEW. Layer-0 fail-closed integrity gate
- `verify_orchestration_hardening.sh` — NEW. Verification suite
- `auto_ingest_loop.sh` — Structured failure envelopes, breaker gating, lease tracking, heartbeat, retry budgets
- `proactive_orchestrator.sh` — Circuit breaker (OPEN/HALF_OPEN/CLOSED), daily dispatch budgets, capability-aware routing
- `constellation_watchdog.sh` — Multi-signal liveness (pane + heartbeat + artifact age)
- `auto_ingest_supervisor.sh` — Removed eval-based env, integrity gate check
- `dispatch.sh` — Aborts on integrity failure or OPEN breaker
- `verify_all.sh` — Wired in orchestration hardening check
- `ARCH-AUTONOMOUS_ORCHESTRATION_HARDENED.md` — Control plane spec

### 4. Git Metadata Cleaned
- Removed `.git/refs/.DS_Store` (Finder artifact corrupting refs)
- Removed `.git/refs/heads/main 2` (ghost branch with zero SHA)
- Removed `.git/logs/refs/remotes/origin/HEAD 2` (duplicate reflog)

### 5. Pushed to GitHub
- Commit `a62faeb` is on `origin/main`
- Mac mini received it (via Google Drive sync of .git/, NOT via git pull)

---

## Current State of Both Machines

### MBA (MacBook Air — /Users/system) — ABOUT TO RESTART
- Repo at `/Users/system/syncrescendence` — HEAD is `a62faeb`, working tree has minor runtime state diffs
- `com.syncrescendence.git-sync` — UNLOADED (stopped before restart)
- git_sync.sh at `~/.syncrescendence/scripts/git_sync.sh` — FIXED (scoped, safe)
- Adjudicator fork at `/Users/system/syncrescendence-before-full/` — still exists, can be deleted after confirming primary is stable

### Mac mini (M1 — /Users/home) — ABOUT TO RESTART
- Repo at `/Users/home/Desktop/syncrescendence` — HEAD is `a62faeb` but **1165 dirty files** in working tree:
  - 1104 deletions (files in index from restoration that don't exist on Mac mini filesystem)
  - 45 untracked (new agent work)
  - 13 modified (active agent state files)
  - 1 rename, 1 add-delete
- ALL 18 syncrescendence launchd services — UNLOADED
- tmux — KILLED
- `main 2` ghost branch still exists at `.git/refs/heads/main 2` (needs cleanup)
- Google Drive FinderSyncExtension was running
- Webhook receiver was at port 8888

---

## Immediate TODO After Restart

### Priority 0: Stop Google Drive from syncing .git/
- **Option A**: Add `.git` to Google Drive's ignore/exclusion list (check Google Drive preferences → "Folders from your computer")
- **Option B**: Move the repo OUT of a Google Drive-synced folder
- **Option C**: Create a `.gitignore`-like exclusion — but Google Drive uses its own mechanism, not `.gitignore`
- Without this fix, all other fixes are undermined. Google Drive will keep creating ghost branches, duplicate files, and race conditions.

### Priority 1: Clean Mac mini working tree
After restart, on Mac mini:
```bash
cd ~/Desktop/syncrescendence
# Remove ghost branch
rm -f ".git/refs/heads/main 2"
# Remove any .DS_Store in .git
find .git -name .DS_Store -delete
# Reset index to match HEAD, then let working tree be
git reset HEAD
```
The 1104 "deletions" will become untracked absences — not tracked, not staged, not dangerous.

### Priority 2: Selective service restart on Mac mini
Do NOT restart all 18 services blindly. Start only:
1. `auto-ingest-supervisor` — core agent loop
2. `watchdog` — health monitoring
3. `webhook-receiver` — API endpoint
Leave disabled until verified:
- `proactive-orchestrator` (was exit code 1 — broken)
- `watch-canon` (was exit code 1)
- All `sensing-*` daemons (secondary)
- `emacs-server`, `qmd-update` (non-critical)

### Priority 3: Restart MBA sync daemon
```bash
launchctl load ~/Library/LaunchAgents/com.syncrescendence.git-sync.plist
```
Only AFTER Google Drive exclusion is confirmed.

### Priority 4: Verify end-to-end
```bash
bash 00-ORCHESTRATION/scripts/verify_all.sh
```

---

## Key Facts (Do Not Forget)

- `/Users/system` = MacBook Air (Ajna's home, Commander runs here)
- `/Users/home` = Mac mini (Psyche's home)
- SSH: `ssh mini` (MBA→MM), `ssh macbook-air` (MM→MBA)
- ICMP ping BLOCKED by Stealth Mode — always use SSH
- Google Drive account: `truongphillipthanh@gmail.com` — syncing on BOTH machines
- Adjudicator fork: `/Users/system/syncrescendence-before-full/`
- The old `git_sync.sh` did `git add -A` → never again
- launchd does NOT source ~/.zshrc — use plist EnvironmentVariables
- Mac mini plist still MISSING `SYNCRESCENDENCE_REMOTE_AGENT_HOST_*` env vars (SCP-back routing blocked)

---

## Neural Bridge
- MBA → MM: `ssh mini` (key: `~/.ssh/id_ed25519_ajna`)
- MM → MBA: `ssh macbook-air` (key: `~/.ssh/id_ed25519_ajna_to_psyche`)
- After restart, verify with: `ssh mini "echo OK && hostname"`

---

## Reference Documents
- Kaizen autopsy: `00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-2026-02-17-autonomous-orchestration-kaizen-autopsy.md`
- Hardened arch spec: `00-ORCHESTRATION/state/ARCH-AUTONOMOUS_ORCHESTRATION_HARDENED.md`
- Agent loops: `00-ORCHESTRATION/state/ARCH-CONSTELLATION_AGENT_LOOPS.md`
- Running logs: `/Users/system/Desktop/desktop/running_logs/` (note: extra `desktop/`)
