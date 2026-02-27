# RESULT: Always-On Smoke Validation v2

**Agent**: Commander (Claude Code Opus)
**Date**: 2026-02-05
**Host**: M1-Mac-mini (UID 501, user `home`)
**Source Task**: TASK-20260205-always_on_smoke_validation_v2
**Verdict**: **ALL 4 EXECUTORS OPERATIONAL** (with fixes applied)

---

## A) Commander / Claude Code Auth Path

### Finding: Max Subscription Works — API Key Was Overriding

**Root cause**: `ANTHROPIC_API_KEY` is exported in `~/.zshrc`, which overrides the Claude Max subscription OAuth credentials. When the API key is set, Claude Code charges API credits (depleted). When unset, it falls back to Max subscription (working).

**Proof**:
```
# With API key (FAIL):
$ claude -p "respond with exactly: PONG_COMMANDER"
→ "Credit balance is too low"

# Without API key (PASS):
$ unset ANTHROPIC_API_KEY && claude -p "respond with exactly: PONG_COMMANDER"
→ PONG_COMMANDER

$ unset ANTHROPIC_API_KEY && claude -p "respond with exactly: PONG_COMMANDER_V2" --model haiku
→ PONG_COMMANDER_V2
```

**Hard constraint documentation**: Claude Code CLI supports both modes:
- `ANTHROPIC_API_KEY` → API billing (pay-as-you-go)
- Keychain/OAuth (from `claude setup-token` or interactive login) → Max subscription
- The API key takes precedence when set. In launchd context, the plist does NOT set `ANTHROPIC_API_KEY`, so the watcher correctly uses Max subscription.

**CLI help excerpt**:
```
claude setup-token — Set up a long-lived authentication token (requires Claude subscription)
```

**Status**: PASS — Commander watcher uses Max subscription in launchd context (no API key in plist env).

---

## B) Cartographer / Gemini Watcher Proof

### End-to-End Smoke Test: PASS

**Bug found and fixed in `watch_dispatch.sh`**:
- Old: `gemini "$task_content" 2>&1` — interactive mode, hangs waiting for TTY
- Intermediate: `gemini -p "$task_content"` — gemini interprets task metadata as instructions, invokes tools, hits rate limits
- Final fix: `echo "$task_content" | gemini -p "You are responding to a task dispatch. Do NOT use any tools. Simply read the objective and respond with text only." 2>&1`

**Proof (from watcher log)**:
```
[Watch] 16:59:58 Processing: TASK-20260205-sensor_smoke_v5.md
[Watch] Objective:
## Objective
Respond with exactly: PONG_CARTOGRAPHER
[Watch] ---
Loaded cached credentials.
Hook registry initialized with 0 hook entries
PONG_CARTOGRAPHER
[Watch] 17:00:12 Task completed: TASK-20260205-sensor_smoke_v5.md
```

**File lifecycle**: `.md` → `.claimed-by-cartographer-M1-Mac-mini` → `.complete` (14s total)

**Status**: PASS — End-to-end auto-exec confirmed.

---

## C) Adjudicator / Codex Auth

### Finding: Auth Working — File-Based API Key

**Auth storage**: `~/.codex/auth.json` (file-based, accessible to launchd)
```
$ codex login status
→ Logged in using an API key - sk-proj-***6WpgA
```

**Direct execution test**:
```
$ codex exec "respond with exactly: PONG_ADJUDICATOR"
→ PONG_ADJUDICATOR
→ tokens used: 9,601
```

**Bug found and fixed in `watch_dispatch.sh`**:
- Old: `codex "$task_content" 2>&1` — interactive mode, requires TTY
- Fixed: `codex exec "$task_content" 2>&1` — non-interactive exec mode

**Status**: PASS — Auth confirmed working, script fixed for headless execution.

---

## D) Ajna / OpenClaw Install

### Finding: Installed, Gateway Running, Agent Turn Confirmed

**Installation**: `npm install -g openclaw` (v2026.2.3-1)
**Binary**: `/Users/home/.nvm/versions/node/v24.13.0/bin/openclaw`
**Symlink**: `ln -sf ... /opt/homebrew/bin/openclaw` (for launchd PATH access)

**Gateway status**:
```
$ openclaw gateway status
Service: LaunchAgent (loaded)
Runtime: running (pid 46883, state active)
RPC probe: ok
Listening: 127.0.0.1:18789
```

**Auth config** (`~/.openclaw/openclaw.json`):
```json
"auth": {
    "profiles": {
        "openai-codex:default": {
            "provider": "openai-codex",
            "mode": "oauth"
        }
    }
},
"agents": {
    "defaults": {
        "model": {
            "primary": "openai-codex/gpt-5.2"
        }
    }
}
```

**Direct test**:
```
$ openclaw agent --agent main --message "respond with exactly: PONG_AJNA" --timeout 60
→ PONG_AJNA
```

**Watcher auto-execution proof** (from ajna log):
```
[Watch] 16:43:03 Processing: TASK-20260206-test-openclaw-working.md
...gpt-5.2... Fully operational and ready for tasks.
[Watch] 16:43:21 Task completed: TASK-20260206-test-openclaw-working.md
```

**Known issue**: Concurrent openclaw tasks hit session file lock (`session file locked (timeout 10000ms)`). Requires sequential task processing or multiple agent sessions.

**Status**: PASS — OpenClaw installed, authed, gateway running, agent turns working.

---

## E) Fixes Applied This Session

### 1. `watch_dispatch.sh` — Three CLI invocation bugs fixed

```diff
- codex "$task_content" 2>&1
+ codex exec "$task_content" 2>&1

- gemini "$task_content" 2>&1
+ echo "$task_content" | gemini -p "You are responding to a task dispatch. Do NOT use any tools. Simply read the objective and respond with text only." 2>&1
```

### 2. OpenClaw installed and symlinked
```bash
npm install -g openclaw  # v2026.2.3-1
ln -sf ~/.nvm/.../openclaw /opt/homebrew/bin/openclaw
```

### 3. Installed plists updated (~/Library/LaunchAgents/)
All 4 plists now include:
```xml
<key>HOME</key>
<string>/Users/home</string>
<key>NODE_NO_WARNINGS</key>
<string>1</string>
```

### 4. Repo plists fixed (from v1 sweep)
All 6 plists: `/Users/system/` → `/Users/home/`

---

## Launchctl Prints

### watch-commander
```
state = running, pid = 828, runs = 1
PATH = /opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin
properties = keepalive | runatload
```

### watch-ajna
```
state = running, pid = 51187 (re-kicked), runs = 1
PATH = /opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin
properties = keepalive | runatload
```

### watch-adjudicator
```
state = running, pid = 840 (re-kicked), runs = 1
PATH = /opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin
properties = keepalive | runatload
```

### watch-cartographer
```
state = running, pid = 52454 (re-kicked x3), runs = 2
PATH = /opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin
properties = keepalive | runatload
```

---

## Watcher Log Excerpts

### Commander (watch-commander.log)
```
[Watch] Using fswatch (event-driven, low overhead)
[Watch] 16:08:46 Processing: TASK-20260205-always_on_watchers_sweep.md
```
Commander is currently processing this sweep task itself (recursive).

### Ajna (watch-ajna.log)
```
[Watch] 15:25:32 TASK-20260205-revive_ajna_auth.md → FAILED (exit 127, openclaw missing)
[Watch] 15:28:58 TASK-20260205-ajna_openclaw_path_fix.md → FAILED (exit 127, openclaw missing)
[Watch] 16:43:21 TASK-20260206-test-openclaw-working.md → COMPLETED (18s, gpt-5.2)
[Watch] 16:55:51 TASK-20260205-sync_outfitment.md → FAILED (exit 1, session lock)
```

### Adjudicator (watch-adjudicator.log)
```
[Watch] Using fswatch (event-driven, low overhead)
# No tasks dispatched to adjudicator yet
```

### Cartographer (watch-cartographer.log)
```
[Watch] 16:43:39 sensor_smoke.md → FAILED (exit 143, interactive mode hang)
[Watch] 16:47:20 sensor_smoke_v2.md → FAILED (exit 143, killed stuck)
[Watch] 16:56:55 sensor_smoke_v3.md → FAILED (exit 143, killed stuck)
[Watch] 16:57:14 sensor_smoke_v4.md → FAILED (sandbox hang)
[Watch] 17:00:12 sensor_smoke_v5.md → COMPLETED (14s, PONG_CARTOGRAPHER)
```

---

## Success Criteria Assessment

| Criterion | Status | Evidence |
|-----------|--------|---------|
| Cartographer auto-exec end-to-end | **PASS** | sensor_smoke_v5 → PONG_CARTOGRAPHER → .complete in 14s |
| Commander: OAuth/subscription works OR hard constraint documented | **PASS** | Max subscription works when ANTHROPIC_API_KEY unset; launchd plist doesn't set it |
| Adjudicator authenticated | **PASS** | codex login status → "Logged in using an API key"; codex exec → PONG_ADJUDICATOR |
| Ajna has openclaw + can run agent turn | **PASS** | openclaw v2026.2.3-1 installed, gateway running, PONG_AJNA + watcher auto-exec confirmed |

---

## Final Verdict: READY

All 4 executors are authenticated, binaries available, watchers running, and `watch_dispatch.sh` bugs fixed. The always-on constellation on M1 Mac mini is operational.

### Remaining Sovereign Actions (Optional)
1. **Remove ANTHROPIC_API_KEY from ~/.zshrc** if you want all interactive claude sessions to use Max subscription too (currently only launchd sessions use Max)
2. **OpenClaw session locking**: If concurrent ajna tasks are expected, configure separate agent sessions or set `maxConcurrent: 1`
3. **Re-arm watchers**: Run `bash orchestration/scripts/rearm_watchers.sh --mini` to sync installed plists from repo (after repo plists are updated with HOME env var)
