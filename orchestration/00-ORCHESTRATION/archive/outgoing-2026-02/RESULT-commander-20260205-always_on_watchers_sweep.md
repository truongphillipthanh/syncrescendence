# RESULT: Always-On Watchers Sweep

**Agent**: Commander (Claude Code Opus)
**Date**: 2026-02-05
**Host**: M1-Mac-mini (UID 501, user `home`)
**Source Task**: TASK-20260205-always_on_watchers_sweep
**Verdict**: **NOT READY** — 3 of 4 executors blocked (see remediation)

---

## 1. Checklist Summary

| # | Requirement | Status | Detail |
|---|------------|--------|--------|
| 1 | Binary: `claude` | PASS | `/opt/homebrew/bin/claude` → `../lib/node_modules/@anthropic-ai/claude-code/cli.js` (v2.1.32) |
| 1 | Binary: `codex` | PASS | `/opt/homebrew/bin/codex` (codex-cli v0.94.0) |
| 1 | Binary: `gemini` | PASS | `/opt/homebrew/bin/gemini` (v0.27.1) |
| 1 | Binary: `fswatch` | PASS | `/opt/homebrew/bin/fswatch` |
| 1 | Binary: `openclaw` | **FAIL** | Not found on any PATH, not installed via npm/pip/brew |
| 1 | Binary: `node` | PASS | v24.13.0 (NVM) |
| 2 | Auth: `claude` | **FAIL** | Auth works but "Credit balance is too low" — billing issue |
| 2 | Auth: `codex` | **FAIL** | 401 Unauthorized — no bearer token configured; needs `codex login` (interactive) |
| 2 | Auth: `gemini` | PASS | Cached credentials loaded; non-interactive PONG confirmed |
| 2 | Auth: `openclaw` | **FAIL** | N/A — binary not installed |
| 3 | Plists: correct location | PASS | All 4 plists in `~/Library/LaunchAgents/` (not `/Users/system/`) |
| 3 | Plists: repo vs installed | **FIXED** | Repo plists had `/Users/system/` — corrected to `/Users/home/` this session |
| 4 | PATH in plists | PASS | `/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin` — sufficient for claude, codex, gemini, fswatch |
| 4 | NODE_NO_WARNINGS | WARN | Present in repo plists, missing from installed copies (cosmetic) |
| 5 | Watcher: watch-commander | PASS | `state = running`, fswatch mode, claimed this task successfully |
| 5 | Watcher: watch-ajna | PASS* | `state = running` but executor fails (openclaw missing) |
| 5 | Watcher: watch-adjudicator | PASS* | `state = running` but executor would fail (codex 401) |
| 5 | Watcher: watch-cartographer | PASS | `state = running`, gemini auth confirmed |
| 6 | Smoke: commander | **SKIP** | Would fail — claude credits depleted |
| 6 | Smoke: ajna | **SKIP** | Would fail — openclaw not installed |
| 6 | Smoke: adjudicator | **SKIP** | Would fail — codex 401 |
| 6 | Smoke: cartographer | PASS | gemini confirmed functional via "PONG" test |

---

## 2. CLI Outputs

### Binary Check
```
claude:   /opt/homebrew/bin/claude    (v2.1.32 — Claude Code)
codex:    /opt/homebrew/bin/codex     (codex-cli v0.94.0)
gemini:   /opt/homebrew/bin/gemini    (v0.27.1)
fswatch:  /opt/homebrew/bin/fswatch
openclaw: NOT FOUND
node:     v24.13.0
```

### Auth Tests
```
claude -p "respond with exactly: PONG"
→ "Credit balance is too low"

codex exec "respond with exactly: PONG"
→ ERROR: http 401 Unauthorized: "Missing bearer or basic authentication in header"

echo "respond with exactly: PONG" | gemini
→ "Loaded cached credentials."
→ "PONG"

openclaw → command not found
```

### Watcher States (launchctl print gui/501/)
```
watch-commander:    state = running, active count = 1
watch-ajna:         state = running, active count = 1
watch-adjudicator:  state = running, active count = 1
watch-cartographer: state = running, active count = 1
```

### Watcher Logs (Historical Failures)
```
ajna.log: "openclaw: command not found" (exit 127) — 2 tasks FAILED
adjudicator.log: idle (no tasks dispatched yet)
cartographer.log: idle (no tasks dispatched yet)
commander.log: processing THIS task
```

---

## 3. Config Diffs Applied

### Repo Plists Fixed (6 files)
All plists in `orchestration/scripts/launchd/` had `/Users/system/` hardcoded.
Changed to `/Users/home/` in this session:
- `com.syncrescendence.watch-commander.plist`
- `com.syncrescendence.watch-ajna.plist`
- `com.syncrescendence.watch-adjudicator.plist`
- `com.syncrescendence.watch-cartographer.plist`
- `com.syncrescendence.watch-psyche.plist`
- `com.syncrescendence.watch-canon.plist`

Installed plists (`~/Library/LaunchAgents/`) were already manually corrected to `/Users/home/` — no reinstall needed.

### Environment Variables (Installed Plists)
```
PATH=/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin
```
This is sufficient: `claude`, `codex`, `gemini`, and `fswatch` all resolve from `/opt/homebrew/bin`.

Missing from installed (present in repo): `NODE_NO_WARNINGS=1`. Cosmetic — reduces Node.js deprecation noise.

---

## 4. Remediation Plan (Sovereign Action Required)

### BLOCKER 1: OpenClaw Not Installed (ajna)
**Impact**: Ajna watcher running but all tasks fail exit 127
**Action**: Install OpenClaw. Check if available via:
- `npm install -g openclaw` or `brew install openclaw`
- Verify with `openclaw --version` and `openclaw gateway status`
- If OpenClaw requires a subscription/license, document the signup flow

### BLOCKER 2: Codex Auth Missing (adjudicator)
**Impact**: Adjudicator watcher running but all tasks fail 401
**Action**: Run `codex login` interactively on the Mac mini. This requires a browser for OAuth flow.
- Alternative: Set `OPENAI_API_KEY` environment variable in the adjudicator plist
- After auth: verify with `codex exec "PONG"`

### BLOCKER 3: Claude Credits Depleted (commander)
**Impact**: Commander watcher running but tasks fail with "Credit balance is too low"
**Action**: Top up Anthropic API credits at console.anthropic.com, or switch to Claude Max subscription if applicable
- Auth itself is working (ANTHROPIC_API_KEY is set in env)
- This is a billing issue, not a configuration issue

### RECOMMENDED: Re-arm After Fixes
Once all 3 blockers are resolved:
```bash
cd ~/Desktop/syncrescendence && bash orchestration/scripts/rearm_watchers.sh --mini
```
Then drop 4 smoke-test tasks to validate end-to-end.

---

## 5. Always-On Readiness Verdict

| Agent | Watcher | Binary | Auth | Verdict |
|-------|---------|--------|------|---------|
| Commander (claude) | RUNNING | OK | NO CREDITS | **NOT READY** |
| Ajna (openclaw) | RUNNING | MISSING | N/A | **NOT READY** |
| Adjudicator (codex) | RUNNING | OK | 401 UNAUTH | **NOT READY** |
| Cartographer (gemini) | RUNNING | OK | OK | **READY** |

**Overall: NOT READY** — Only 1 of 4 executors is fully operational (Cartographer/Gemini).

The watcher infrastructure (launchd + fswatch + watch_dispatch.sh + claim-locking) is **sound**. The failures are all at the executor auth/install layer, not at the orchestration layer. Once the 3 blockers above are resolved, re-arm and full smoke test should pass.
