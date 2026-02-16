# RESULT — TASK-20260205-ajna_openclaw_path_fix (Ajna / Mac mini)

## 1) Binary/path diagnostics (requested)
```bash
which openclaw
# /opt/homebrew/bin/openclaw

openclaw --version
# 2026.2.3-1

which node
# /opt/homebrew/bin/node

node -v
# v25.6.0

echo /opt/homebrew/bin:/usr/local/bin:/Users/system/Library/pnpm:/Users/system/.local/bin:/usr/bin:/bin
# /opt/homebrew/bin:/usr/local/bin:/Users/system/Library/pnpm:/Users/system/.local/bin:/usr/bin:/bin
```

## 2) Do we need to install/upgrade OpenClaw?
No.
- OpenClaw is present at `/opt/homebrew/bin/openclaw` and already at **2026.2.3-1**.

## 3) launchd watcher PATH sanity
Ajna mini watcher plist includes PATH with Homebrew first:
- `00-ORCHESTRATION/scripts/launchd-mini/com.syncrescendence.watch-ajna.plist`
  - `PATH=/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin`
  - `NODE_NO_WARNINGS=1`

So the watcher environment should be able to resolve `openclaw` (via `/opt/homebrew/bin`).

## 4) Gateway restart + verification
Ran:
```bash
openclaw gateway restart
openclaw gateway status
```
Result:
- Gateway LaunchAgent restarted successfully.
- `openclaw gateway status` shows **running** with RPC probe **ok**.

## 5) Revive/auth/model verification
From Ajna `~/.openclaw/openclaw.json`:
- `auth.profiles.openai-codex:default` present (oauth)
- `agents.defaults.model.primary = openai-codex/gpt-5.2`

## 6) Notes / likely cause of prior Exit-Code 127
Given current state, `openclaw` is definitely present in the expected PATH.
The earlier 127 likely came from a process environment that did **not** include `/opt/homebrew/bin` (e.g., older watcher plist or an earlier shell env) or from invoking `openclaw` before it was installed/updated.

## Blockers
None remaining for PATH/OpenClaw/gateway.
(Separate blocker still exists for *memory_search indexing* until `OPENAI_API_KEY` is set; tracked in other tasks.)
