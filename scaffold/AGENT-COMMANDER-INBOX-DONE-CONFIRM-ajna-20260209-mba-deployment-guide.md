# CONFIRM-ajna-20260209-mba-deployment-guide

**Kind**: CONFIRM
**Task**: TASK-20260209-mba-deployment-guide.md
**From-Agent**: ajna
**To-Agent**: commander
**Status**: COMPLETE
**Exit-Code**: 0
**Completed-At**: 2026-02-09T18:58:30Z
**Finalized-Task-Path**: `/Users/home/Desktop/syncrescendence/-INBOX/ajna/40-DONE/TASK-20260209-mba-deployment-guide.md`
**Result-Path**: `/Users/home/Desktop/syncrescendence/-OUTBOX/ajna/RESULTS/RESULT-ajna-20260209-mba-deployment-guide.md`
**Execution-Log**: `/Users/home/Desktop/syncrescendence/-INBOX/commander/00-INBOX0/EXECLOG-ajna-20260209-mba-deployment-guide.log`

---

## Execution Log Tail

```text
[plugins] openclaw-mem0: registered (mode: open-source, user: sovereign, graph: false, autoRecall: true, autoCapture: true)
A few critical fixes before Phillip runs this on **Lisas-MacBook-Air** (and one security issue):

## 0) Security: the NVIDIA API key is exposed in this task text
Treat that key as **compromised** and **rotate it** in NVIDIA immediately. Don’t commit it, don’t paste it into tasks. Going forward, only refer to it as `NVIDIA_API_KEY` and load it from `~/.openclaw/.env` (chmod 600) or 1Password.

## 1) Model id mismatch (will break as written)
Your config sets:

- primary: `nvidia/moonshotai/kimi-k2.5`
- provider model id: `moonshotai/kimi-k2.5`

Pick one convention and use it consistently. Usually it should be:

- provider model id: `moonshotai/kimi-k2.5`
- primary: `nvidia/moonshotai/kimi-k2.5` **only if** OpenClaw expects `provider/modelId` form.

If OpenClaw expects the *provider* to be selected by the provider mapping (common), then `primary` should likely be just:
- `moonshotai/kimi-k2.5`

I need one quick confirmation from you: on Ajna (Mac mini), what does `~/.openclaw/openclaw.json` (or whatever config file you’re using) set for `agents.defaults.model.primary` today?

## 2) Launchd plists: `~` won’t expand reliably; also missing fswatch install
- Your watcher uses `/usr/bin/fswatch` but you never install it. On macOS it’s typically `brew install fswatch` and the binary ends up in `/opt/homebrew/bin/fswatch` (Apple Silicon) or `/usr/local/bin/fswatch` (Intel).
- launchd often won’t expand `~` inside `ProgramArguments`. Use absolute paths and/or set `WorkingDirectory`.

Safer watcher approach:
- install: `brew install fswatch`
- plist should use:
  - `<key>WorkingDirectory</key><string>/Users/<user>/Desktop/syncrescendence</string>`
  - absolute binary path for fswatch
  - absolute inbox path (not `-INBOX/...` unless that’s actually a literal directory name)

Also: your `fswatch ... -INBOX/ajna/00-INBOX0/` argument is suspicious: `-INBOX` looks like an option because it starts with a dash. If that folder is literally named `-INBOX`, fswatch may still treat it as a flag. Use `--` before the path or quote and ensure fswatch treats it as a path.

## 3) Gateway launchd path: `/usr/local/bin/openclaw` may be wrong on MBA
On Apple Silicon with Homebrew+global npm, `openclaw` is often at:
- `/opt/homebrew/bin/openclaw` or
- `~/.nvm/.../bin/openclaw`

In launchd, don’t rely on PATH. Hardcode the resolved path:
- `which openclaw`
- `realpath $(which openclaw)`

Then put that exact path in the plist.

## 4) “Install universal skills” loop is almost certainly wrong
`npx skills add "obra/superpowers@$skill"` doesn’t match normal OpenClaw skill installation flows (and the skill names listed don’t look like versions/tags).

If you want this to be push-button reliable, tell me which method you actually use on Ajna today:
- `openclaw skills ...` (what subcommands?), or
- `clawhub ...`, or
- skills are just checked into the repo under `~/.openclaw/workspace/skills/` and loaded locally.

## 5) Suggested “MBA Ajna” deployment guide structure (what I’ll produce)
If you confirm the 2 items above (model primary format + skill install mechanism), I’ll rewrite this as a clean, copy/paste guide with:
- preflight checks (Apple Silicon vs Intel, node version, `openclaw --version`)
- exact file paths (config + env)
- launchd plists that actually work (WorkingDirectory, absolute paths, logs)
- verification commands + expected outputs
- rollback steps (launchctl bootout, remove plists, etc.)

Answer these two and I’ll finalize the corrected guide:
1) On current Ajna, what is the exact value of `agents.defaults.model.primary` that works?
2) How are skills installed on Ajna (exact command you use that works)?
```

