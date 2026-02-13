# RESULT — TASK-20260205-outfitment_sync_and_smoketest_v3 (Ajna)

Date: 2026-02-05 (America/Los_Angeles)
Host: ajna-M1-Mac-mini (user `home`)
Source host: `psyche` (SSH alias) → `system@Lisas-MacBook-Air.local`

## 1) Repo update

```bash
cd ~/Desktop/syncrescendence
# repo had local changes; stashed to allow pull
git stash push -u -m "ajna: WIP before outfitment_sync_and_smoketest_v3"
git pull --rebase
```
Output:
- `Already up to date.`

## 2) Skill sync (rsync allowlist; no secrets)

Command:
```bash
bash 00-ORCHESTRATION/scripts/sync_openclaw_skills.sh --pull --from psyche --persona ajna
```

Output summary:
    [sync] persona: ajna
    [sync] from: psyche:/Users/system/.openclaw/workspace/skills
    [sync] to:   /Users/home/.openclaw/workspace/skills/
    [sync] syncing: supermemory
    [sync] syncing: hindsight
    [sync] syncing: graphiti-memory
    [sync] syncing: agent-browser-stagehand
    [sync] syncing: prompt-guard
    [sync] syncing: cron-writer
    [sync] syncing: dont-hack-me
    [sync] syncing: find-skills
    [sync] syncing: clawguard
    [sync] syncing: qmd-skill
    [sync] syncing: summarize
    [sync] done. Next: run 'openclaw doctor --fix' and restart gateway if plugin loads changed.

## 3) Verify synced skills (ls/du receipts)

### `ls -la ~/.openclaw/workspace/skills` (first 220 lines)
```text
total 0
drwxr-xr-x@ 13 home  staff   416 Feb  5 18:40 .
drwxr-xr-x@ 11 home  staff   352 Feb  5 16:55 ..
drwxr-xr-x@  8 home  staff   256 Feb  5 14:09 agent-browser-stagehand
drwxr-xr-x@  5 home  staff   160 Feb  5 14:06 clawguard
drwxr-xr-x@  6 home  staff   192 Feb  5 14:09 cron-writer
drwxr-xr-x@  5 home  staff   160 Feb  5 14:18 dont-hack-me
drwxr-xr-x@  5 home  staff   160 Feb  5 14:18 find-skills
drwxr-xr-x@ 11 home  staff   352 Feb  5 14:18 graphiti-memory
drwxr-xr-x@ 38 home  staff  1216 Feb  5 14:19 hindsight
drwxr-xr-x@ 13 home  staff   416 Feb  5 14:18 prompt-guard
drwxr-xr-x@  5 home  staff   160 Feb  5 14:18 qmd-skill
drwxr-xr-x@  5 home  staff   160 Feb  5 14:08 summarize
drwxr-xr-x@ 23 home  staff   736 Feb  5 14:20 supermemory

```

### `du -sh ~/.openclaw/workspace/skills/* | sort -h | tail -40`
```text
--- du skills (tail 40) ---
 12K	/Users/home/.openclaw/workspace/skills/clawguard
 12K	/Users/home/.openclaw/workspace/skills/summarize
 16K	/Users/home/.openclaw/workspace/skills/cron-writer
 16K	/Users/home/.openclaw/workspace/skills/find-skills
 20K	/Users/home/.openclaw/workspace/skills/dont-hack-me
 40K	/Users/home/.openclaw/workspace/skills/agent-browser-stagehand
136K	/Users/home/.openclaw/workspace/skills/qmd-skill
176K	/Users/home/.openclaw/workspace/skills/prompt-guard
248K	/Users/home/.openclaw/workspace/skills/graphiti-memory
321M	/Users/home/.openclaw/workspace/skills/hindsight
373M	/Users/home/.openclaw/workspace/skills/supermemory
```

Notable sizes:
- `supermemory` ~ **373M**
- `hindsight` ~ **321M**

## 4) OpenClaw doctor

### After initial sync (pre-fix)
Receipt: `/tmp/ajna-doctor-after-v3.txt`

Key findings:
- **CRITICAL:** OAuth dir missing `~/.openclaw/credentials`
- **ERROR:** `hindsight-openclaw` failed to load due to missing `dist/index.js`

Excerpt:
```text
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▄░██░▄▄░██░▄▄▄██░▀██░██░▄▄▀██░████░▄▄▀██░███░██
██░███░██░▀▀░██░▄▄▄██░█░█░██░█████░████░▀▀░██░█░█░██
██░▀▀▀░██░█████░▀▀▀██░██▄░██░▀▀▄██░▀▀░█░██░██▄▀▄▀▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                  🦞 OPENCLAW 🦞                    
 
┌  OpenClaw doctor
│
◇  State integrity ──────────────────────────────────────────╮
│                                                            │
│  - CRITICAL: OAuth dir missing (~/.openclaw/credentials).  │
│                                                            │
├────────────────────────────────────────────────────────────╯
│
◇  Security ─────────────────────────────────────────────────────────────╮
│                                                                        │
│  - Discord DMs: locked (channels.discord.dm.policy="pairing") with no  │
│    allowlist; unknown senders will be blocked / get a pairing code.    │
│    Approve via: openclaw pairing list discord / openclaw pairing       │
│    approve discord <code>                                              │
│  - Run: openclaw security audit --deep                                 │
│                                                                        │
├────────────────────────────────────────────────────────────────────────╯
│
◇  Skills status ────────────╮
│                            │
│  Eligible: 46              │
│  Missing requirements: 15  │
│  Blocked by allowlist: 0   │
│                            │
├────────────────────────────╯
│
◇  Plugins ──────────────╮
│                        │
│  Loaded: 2             │
│  Disabled: 30          │
│  Errors: 1             │
│  - hindsight-openclaw  │
│                        │
├────────────────────────╯
│
◇  Plugin diagnostics ─────────────────────────────────────────────────────╮
│                                                                          │
│  - ERROR hindsight-openclaw: failed to load plugin: Error: Cannot find   │
│    module                                                                │
│    '/Users/home/.openclaw/workspace/skills/hindsight/hindsight-integrat  │
│    ions/openclaw/dist/index.js'                                          │
│  Require stack:                                                          │
│  - /Users/home/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/di  │
│    st/loader-BAZoAqqR.js                                                 │
│    (/Users/home/.openclaw/workspace/skills/hindsight/hindsight-integrat  │
│    ions/openclaw/dist/index.js)                                          │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────╯
Discord: ok (@Ajna) (674ms)
Agents: main (default)
Heartbeat interval: 30m (main)
Session store (main): /Users/home/.openclaw/agents/main/sessions/sessions.json (1 entries)
- agent:main:main (0m ago)
Run "openclaw doctor --fix" to apply changes.
│
└  Doctor complete.

```

### Fixes applied
- Created credentials dir: `mkdir -p ~/.openclaw/credentials`
- Built/installed Hindsight OpenClaw integration:
  - `cd ~/.openclaw/workspace/skills/hindsight/hindsight-integrations/openclaw && bash ./install.sh`

Receipt: `/tmp/hindsight-openclaw-install.log`

### Doctor after fixes
Receipt: `/tmp/ajna-doctor-after2-v3.txt`

Key findings now:
- OAuth dir missing **resolved** (no longer reported as CRITICAL)
- Plugins: **Errors 0**
- **WARN:** duplicate plugin id `hindsight-openclaw` (workspace + extensions)

Excerpt:
```text
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▄░██░▄▄░██░▄▄▄██░▀██░██░▄▄▀██░████░▄▄▀██░███░██
██░███░██░▀▀░██░▄▄▄██░█░█░██░█████░████░▀▀░██░█░█░██
██░▀▀▀░██░█████░▀▀▀██░██▄░██░▀▀▄██░▀▀░█░██░██▄▀▄▀▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                  🦞 OPENCLAW 🦞                    
 
┌  OpenClaw doctor
│
◇  Config warnings ───────────────────────────────────────────────────────╮
│                                                                         │
│  - plugins.entries.hindsight-openclaw: plugin hindsight-openclaw:       │
│    duplicate plugin id detected; later plugin may be overridden         │
│    (/Users/home/.openclaw/extensions/hindsight-openclaw/dist/index.js)  │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────╯
│
◇  Security ─────────────────────────────────────────────────────────────╮
│                                                                        │
│  - Discord DMs: locked (channels.discord.dm.policy="pairing") with no  │
│    allowlist; unknown senders will be blocked / get a pairing code.    │
│    Approve via: openclaw pairing list discord / openclaw pairing       │
│    approve discord <code>                                              │
│  - Run: openclaw security audit --deep                                 │
│                                                                        │
├────────────────────────────────────────────────────────────────────────╯
│
◇  Skills status ────────────╮
│                            │
│  Eligible: 46              │
│  Missing requirements: 15  │
│  Blocked by allowlist: 0   │
│                            │
├────────────────────────────╯
│
◇  Plugins ──────╮
│                │
│  Loaded: 2     │
│  Disabled: 32  │
│  Errors: 0     │
│                │
├────────────────╯
│
◇  Plugin diagnostics ────────────────────────────────────────────────────╮
│                                                                         │
│  - WARN hindsight-openclaw: duplicate plugin id detected; later plugin  │
│    may be overridden                                                    │
│    (/Users/home/.openclaw/extensions/hindsight-openclaw/dist/index.js)  │
│    (/Users/home/.openclaw/extensions/hindsight-openclaw/dist/index.js)  │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────╯
Discord: ok (@Ajna) (391ms)
Agents: main (default)
Heartbeat interval: 30m (main)
Session store (main): /Users/home/.openclaw/agents/main/sessions/sessions.json (1 entries)
- agent:main:main (1m ago)
Run "openclaw doctor --fix" to apply changes.
│
└  Doctor complete.

```

Permissions hardening:
```bash
chmod 700 ~/.openclaw/credentials
```
Receipt:
```text
drwx------@ 2 home  staff  64 Feb  5 18:40 /Users/home/.openclaw/credentials
```

## 5) Gateway status

```bash
openclaw gateway status
```

Receipt:
```text
│
◇  Config warnings ───────────────────────────────────────────────────────╮
│                                                                         │
│  - plugins.entries.hindsight-openclaw: plugin hindsight-openclaw:       │
│    duplicate plugin id detected; later plugin may be overridden         │
│    (/Users/home/.openclaw/extensions/hindsight-openclaw/dist/index.js)  │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────╯
Service: LaunchAgent (loaded)
File logs: /tmp/openclaw/openclaw-2026-02-05.log
Command: /opt/homebrew/bin/node /Users/home/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/dist/index.js gateway --port 18789
Service file: ~/Library/LaunchAgents/ai.openclaw.gateway.plist
Service env: OPENCLAW_GATEWAY_PORT=18789

Config (cli): ~/.openclaw/openclaw.json
Config (service): ~/.openclaw/openclaw.json

Gateway: bind=loopback (127.0.0.1), port=18789 (service args)
Probe target: ws://127.0.0.1:18789
Dashboard: http://127.0.0.1:18789/
Probe note: Loopback-only gateway; only local clients can connect.

Runtime: running (pid 46883, state active)
RPC probe: ok

Listening: 127.0.0.1:18789
Troubles: run openclaw status
Troubleshooting: https://docs.openclaw.ai/troubleshooting
```

## 6) Smoke agent run

Attempted:
```bash
openclaw agent --agent main \
  --message "SMOKE V3: confirm synced workspace skills present (supermemory+hindsight etc) and OpenAI Codex OAuth usable." \
  --timeout 60 --json
```

Result:
- The CLI displayed config warnings and did not return a JSON reply within the observed wall-clock time; I terminated the command.

## 7) Plugins/skills listing (CLI)

### `openclaw plugins list`
Receipt excerpt:
```text
│
◇  Config warnings ───────────────────────────────────────────────────────╮
│                                                                         │
│  - plugins.entries.hindsight-openclaw: plugin hindsight-openclaw:       │
│    duplicate plugin id detected; later plugin may be overridden         │
│    (/Users/home/.openclaw/extensions/hindsight-openclaw/dist/index.js)  │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────╯
Plugins (2/34 loaded)
┌──────────────┬──────────┬──────────┬───────────────────────────────────────────────────────────────────┬────────────┐
│ Name         │ ID       │ Status   │ Source                                                            │ Version    │
├──────────────┼──────────┼──────────┼───────────────────────────────────────────────────────────────────┼────────────┤
│ Supermemory  │ openclaw │ disabled │ ~/.openclaw/workspace/skills/supermemory/index.ts                 │ 1.0.3      │
│              │ -        │          │ OpenClaw powered by Supermemory plugin                            │            │
│              │ supermem │          │                                                                   │            │
│              │ ory      │          │                                                                   │            │
│ Hindsight    │ hindsigh │ disabled │ ~/.openclaw/workspace/skills/hindsight/hindsight-integrations/    │ 0.4.9      │
│ Memory       │ t-       │          │ openclaw/dist/index.js                                            │            │
│              │ openclaw │          │ Hindsight memory plugin for OpenClaw - biomimetic long-term       │            │
│              │          │          │ memory with fact extraction                                       │            │
│ Hindsight    │ hindsigh │ disabled │ ~/.openclaw/extensions/hindsight-openclaw/dist/index.js           │ 0.4.9      │
│ Memory       │ t-       │          │ Hindsight memory plugin for OpenClaw - biomimetic long-term       │            │
│              │ openclaw │          │ memory with fact extraction                                       │            │
│ @openclaw/   │ bluebubb │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ bluebubbles  │ les      │          │ extensions/bluebubbles/index.ts                                   │            │
│              │          │          │ OpenClaw BlueBubbles channel plugin                               │            │
│ @openclaw/   │ copilot- │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ copilot-     │ proxy    │          │ extensions/copilot-proxy/index.ts                                 │            │
│ proxy        │          │          │ OpenClaw Copilot Proxy provider plugin                            │            │
│ @openclaw/   │ diagnost │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ diagnostics- │ ics-otel │          │ extensions/diagnostics-otel/index.ts                              │            │
│ otel         │          │          │ OpenClaw diagnostics OpenTelemetry exporter                       │            │
│ Discord      │ discord  │ loaded   │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│              │          │          │ extensions/discord/index.ts                                       │            │
│              │          │          │ Discord channel plugin                                            │            │
│ @openclaw/   │ feishu   │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ feishu       │          │          │ extensions/feishu/index.ts                                        │            │
│              │          │          │ OpenClaw Feishu channel plugin                                    │            │
│ @openclaw/   │ google-  │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ google-      │ antigrav │          │ extensions/google-antigravity-auth/index.ts                       │            │
│ antigravity- │ ity-auth │          │ OpenClaw Google Antigravity OAuth provider plugin                 │            │
│ auth         │          │          │                                                                   │            │
│ @openclaw/   │ google-  │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ google-      │ gemini-  │          │ extensions/google-gemini-cli-auth/index.ts                        │            │
│ gemini-cli-  │ cli-auth │          │ OpenClaw Gemini CLI OAuth provider plugin                         │            │
│ auth         │          │          │                                                                   │            │
│ @openclaw/   │ googlech │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ googlechat   │ at       │          │ extensions/googlechat/index.ts                                    │            │
│              │          │          │ OpenClaw Google Chat channel plugin                               │            │
│ @openclaw/   │ imessage │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ imessage     │          │          │ extensions/imessage/index.ts                                      │            │
│              │          │          │ OpenClaw iMessage channel plugin                                  │            │
│ @openclaw/   │ line     │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ line         │          │          │ extensions/line/index.ts                                          │            │
│              │          │          │ OpenClaw LINE channel plugin                                      │            │
│ LLM Task     │ llm-task │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│              │          │          │ extensions/llm-task/index.ts                                      │            │
│              │          │          │ Generic JSON-only LLM tool for structured tasks callable from     │            │
│              │          │          │ workflows.                                                        │            │
│ Lobster      │ lobster  │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│              │          │          │ extensions/lobster/index.ts                                       │            │
│              │          │          │ Typed workflow tool with resumable approvals.                     │            │
│ @openclaw/   │ matrix   │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ matrix       │          │          │ extensions/matrix/index.ts                                        │            │
│              │          │          │ OpenClaw Matrix channel plugin                                    │            │
│ @openclaw/   │ mattermo │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ mattermost   │ st       │          │ extensions/mattermost/index.ts                                    │            │
│              │          │          │ OpenClaw Mattermost channel plugin                                │            │
│ Memory       │ memory-  │ loaded   │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ (Core)       │ core     │          │ extensions/memory-core/index.ts                                   │            │
│              │          │          │ File-backed memory search tools and CLI                           │            │
│ @openclaw/   │ memory-  │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ memory-      │ lancedb  │          │ extensions/memory-lancedb/index.ts                                │            │
│ lancedb      │          │          │ OpenClaw LanceDB-backed long-term memory plugin with auto-recall/ │            │
│              │          │          │ capture                                                           │            │
│ @openclaw/   │ minimax- │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ minimax-     │ portal-  │          │ extensions/minimax-portal-auth/index.ts                           │            │
│ portal-auth  │ auth     │          │ OpenClaw MiniMax Portal OAuth provider plugin                     │            │
│ @openclaw/   │ msteams  │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ msteams      │          │          │ extensions/msteams/index.ts                                       │            │
│              │          │          │ OpenClaw Microsoft Teams channel plugin                           │            │
│ @openclaw/   │ nextclou │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ nextcloud-   │ d-talk   │          │ extensions/nextcloud-talk/index.ts                                │            │
│ talk         │          │          │ OpenClaw Nextcloud Talk channel plugin                            │            │
│ @openclaw/   │ nostr    │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ nostr        │          │          │ extensions/nostr/index.ts                                         │            │
│              │          │          │ OpenClaw Nostr channel plugin for NIP-04 encrypted DMs            │            │
│ OpenProse    │ open-    │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│              │ prose    │          │ extensions/open-prose/index.ts                                    │            │
│              │          │          │ OpenProse VM skill pack with a /prose slash command.              │            │
│ qwen-portal- │          │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │            │
│ auth         │          │          │ extensions/qwen-portal-auth/index.ts                              │            │
│ @openclaw/   │ signal   │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ signal       │          │          │ extensions/signal/index.ts                                        │            │
│              │          │          │ OpenClaw Signal channel plugin                                    │            │
│ @openclaw/   │ slack    │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ slack        │          │          │ extensions/slack/index.ts                                         │            │
│              │          │          │ OpenClaw Slack channel plugin                                     │            │
│ @openclaw/   │ telegram │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ telegram     │          │          │ extensions/telegram/index.ts                                      │            │
│              │          │          │ OpenClaw Telegram channel plugin                                  │            │
│ @openclaw/   │ tlon     │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ tlon         │          │          │ extensions/tlon/index.ts                                          │            │
│              │          │          │ OpenClaw Tlon/Urbit channel plugin                                │            │
│ @openclaw/   │ twitch   │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ twitch       │          │          │ extensions/twitch/index.ts                                        │            │
│              │          │          │ OpenClaw Twitch channel plugin                                    │            │
│ @openclaw/   │ voice-   │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ voice-call   │ call     │          │ extensions/voice-call/index.ts                                    │            │
│              │          │          │ OpenClaw voice-call plugin                                        │            │
│ @openclaw/   │ whatsapp │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ whatsapp     │          │          │ extensions/whatsapp/index.ts                                      │            │
│              │          │          │ OpenClaw WhatsApp channel plugin                                  │            │
│ @openclaw/   │ zalo     │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ zalo         │          │          │ extensions/zalo/index.ts                                          │            │
│              │          │          │ OpenClaw Zalo channel plugin                                      │            │
│ @openclaw/   │ zalouser │ disabled │ ~/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/          │ 2026.2.3-1 │
│ zalouser     │          │          │ extensions/zalouser/index.ts                                      │            │
│              │          │          │ OpenClaw Zalo Personal Account plugin via zca-cli                 │            │
└──────────────┴──────────┴──────────┴───────────────────────────────────────────────────────────────────┴────────────┘
```

### `openclaw skills list`
Receipt excerpt:
```text
│
◇  Config warnings ───────────────────────────────────────────────────────╮
│                                                                         │
│  - plugins.entries.hindsight-openclaw: plugin hindsight-openclaw:       │
│    duplicate plugin id detected; later plugin may be overridden         │
│    (/Users/home/.openclaw/extensions/hindsight-openclaw/dist/index.js)  │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────╯
Skills (46/61 ready)
┌───────────┬──────────────────┬─────────────────────────────────────────────────────────────────┬────────────────────┐
│ Status    │ Skill            │ Description                                                     │ Source             │
├───────────┼──────────────────┼─────────────────────────────────────────────────────────────────┼────────────────────┤
│ ✓ ready   │ 🔐 1password      │ Set up and use 1Password CLI (op). Use when installing the      │ openclaw-bundled   │
│           │                  │ CLI, enabling desktop app integration, signing in (single or    │                    │
│           │                  │ multi-account), or reading/injecting/running secrets via op.    │                    │
│ ✓ ready   │ 📝 apple-notes    │ Manage Apple Notes via the `memo` CLI on macOS (create, view,   │ openclaw-bundled   │
│           │                  │ edit, delete, search, move, and export notes). Use when a user  │                    │
│           │                  │ asks OpenClaw to add a note, list notes, search notes, or       │                    │
│           │                  │ manage note folders.                                            │                    │
│ ✓ ready   │ ⏰ apple-         │ Manage Apple Reminders via the `remindctl` CLI on macOS (list,  │ openclaw-bundled   │
│           │ reminders        │ add, edit, complete, delete). Supports lists, date filters,     │                    │
│           │                  │ and JSON/plain output.                                          │                    │
│ ✓ ready   │ 🐻 bear-notes     │ Create, search, and manage Bear notes via grizzly CLI.          │ openclaw-bundled   │
│ ✓ ready   │ 🐦 bird           │ X/Twitter CLI for reading, searching, posting, and engagement   │ openclaw-bundled   │
│           │                  │ via cookies.                                                    │                    │
│ ✓ ready   │ 📰 blogwatcher    │ Monitor blogs and RSS/Atom feeds for updates using the          │ openclaw-bundled   │
│           │                  │ blogwatcher CLI.                                                │                    │
│ ✓ ready   │ 🫐 blucli         │ BluOS CLI (blu) for discovery, playback, grouping, and volume.  │ openclaw-bundled   │
│ ✗ missing │ 🫧 bluebubbles    │ Use when you need to send or manage iMessages via BlueBubbles   │ openclaw-bundled   │
│           │                  │ (recommended iMessage integration). Calls go through the        │                    │
│           │                  │ generic message tool with channel="bluebubbles".                │                    │
│ ✓ ready   │ 📸 camsnap        │ Capture frames or clips from RTSP/ONVIF cameras.                │ openclaw-bundled   │
│ ✓ ready   │ 📦 clawhub        │ Use the ClawHub CLI to search, install, update, and publish     │ openclaw-bundled   │
│           │                  │ agent skills from clawhub.com. Use when you need to fetch new   │                    │
│           │                  │ skills on the fly, sync installed skills to latest or a         │                    │
│           │                  │ specific version, or publish new/updated skill folders with     │                    │
│           │                  │ the npm-installed clawhub CLI.                                  │                    │
│ ✓ ready   │ 🧩 coding-agent   │ Run Codex CLI, Claude Code, OpenCode, or Pi Coding Agent via    │ openclaw-bundled   │
│           │                  │ background process for programmatic control.                    │                    │
│ ✓ ready   │ 🎛️ eightctl      │ Control Eight Sleep pods (status, temperature, alarms,          │ openclaw-bundled   │
│           │                  │ schedules).                                                     │                    │
│ ✓ ready   │ ♊️ gemini        │ Gemini CLI for one-shot Q&A, summaries, and generation.         │ openclaw-bundled   │
│ ✓ ready   │ 🧲 gifgrep        │ Search GIF providers with CLI/TUI, download results, and        │ openclaw-bundled   │
│           │                  │ extract stills/sheets.                                          │                    │
│ ✓ ready   │ 🐙 github         │ Interact with GitHub using the `gh` CLI. Use `gh issue`, `gh    │ openclaw-bundled   │
│           │                  │ pr`, `gh run`, and `gh api` for issues, PRs, CI runs, and       │                    │
│           │                  │ advanced queries.                                               │                    │
│ ✓ ready   │ 🎮 gog            │ Google Workspace CLI for Gmail, Calendar, Drive, Contacts,      │ openclaw-bundled   │
│           │                  │ Sheets, and Docs.                                               │                    │
│ ✗ missing │ 📍 goplaces       │ Query Google Places API (New) via the goplaces CLI for text     │ openclaw-bundled   │
│           │                  │ search, place details, resolve, and reviews. Use for human-     │                    │
│           │                  │ friendly place lookup or JSON output for scripts.               │                    │
│ ✓ ready   │ 📦 healthcheck    │ Host security hardening and risk-tolerance configuration for    │ openclaw-bundled   │
│           │                  │ OpenClaw deployments. Use when a user asks for security         │                    │
│           │                  │ audits, firewall/SSH/update hardening, risk posture, exposure   │                    │
│           │                  │ review, OpenClaw cron scheduling for periodic checks, or        │                    │
│           │                  │ version status checks on a machine running OpenClaw (laptop,    │                    │
│           │                  │ workstation, Pi, VPS).                                          │                    │
│ ✓ ready   │ 📧 himalaya       │ CLI to manage emails via IMAP/SMTP. Use `himalaya` to list,     │ openclaw-bundled   │
│           │                  │ read, write, reply, forward, search, and organize emails from   │                    │
│           │                  │ the terminal. Supports multiple accounts and message            │                    │
│           │                  │ composition with MML (MIME Meta Language).                      │                    │
│ ✓ ready   │ 📨 imsg           │ iMessage/SMS CLI for listing chats, history, watch, and         │ openclaw-bundled   │
│           │                  │ sending.                                                        │                    │
│ ✗ missing │ 📍 local-places   │ Search for places (restaurants, cafes, etc.) via Google Places  │ openclaw-bundled   │
│           │                  │ API proxy on localhost.                                         │                    │
│ ✓ ready   │ 📦 mcporter       │ Use the mcporter CLI to list, configure, auth, and call MCP     │ openclaw-bundled   │
│           │                  │ servers/tools directly (HTTP or stdio), including ad-hoc        │                    │
│           │                  │ servers, config edits, and CLI/type generation.                 │                    │
│ ✗ missing │ 📊 model-usage    │ Use CodexBar CLI local cost usage to summarize per-model usage  │ openclaw-bundled   │
│           │                  │ for Codex or Claude, including the current (most recent) model  │                    │
│           │                  │ or a full model breakdown. Trigger when asked for model-level   │                    │
│           │                  │ usage/cost data from codexbar, or when you need a scriptable    │                    │
│           │                  │ per-model summary from codexbar cost JSON.                      │                    │
│ ✗ missing │ 🍌 nano-banana-   │ Generate or edit images via Gemini 3 Pro Image (Nano Banana     │ openclaw-bundled   │
│           │ pro              │ Pro).                                                           │                    │
│ ✓ ready   │ 📄 nano-pdf       │ Edit PDFs with natural-language instructions using the nano-    │ openclaw-bundled   │
│           │                  │ pdf CLI.                                                        │                    │
│ ✗ missing │ 📝 notion         │ Notion API for creating and managing pages, databases, and      │ openclaw-bundled   │
│           │                  │ blocks.                                                         │                    │
│ ✓ ready   │ 💎 obsidian       │ Work with Obsidian vaults (plain Markdown notes) and automate   │ openclaw-bundled   │
│           │                  │ via obsidian-cli.                                               │                    │
│ ✗ missing │ 🖼️ openai-image- │ Batch-generate images via OpenAI Images API. Random prompt      │ openclaw-bundled   │
│           │ gen              │ sampler + `index.html` gallery.                                 │                    │
│ ✗ missing │ 🎙️ openai-       │ Local speech-to-text with the Whisper CLI (no API key).         │ openclaw-bundled   │
│           │ whisper          │                                                                 │                    │
│ ✗ missing │ ☁️ openai-       │ Transcribe audio via OpenAI Audio Transcriptions API (Whisper). │ openclaw-bundled   │
│           │ whisper-api      │                                                                 │                    │
│ ✓ ready   │ 💡 openhue        │ Control Philips Hue lights/scenes via the OpenHue CLI.          │ openclaw-bundled   │
│ ✓ ready   │ 🧿 oracle         │ Best practices for using the oracle CLI (prompt + file          │ openclaw-bundled   │
│           │                  │ bundling, engines, sessions, and file attachment patterns).     │                    │
│ ✓ ready   │ 🛵 ordercli       │ Foodora-only CLI for checking past orders and active order      │ openclaw-bundled   │
│           │                  │ status (Deliveroo WIP).                                         │                    │
│ ✓ ready   │ 👀 peekaboo       │ Capture and automate macOS UI with the Peekaboo CLI.            │ openclaw-bundled   │
│ ✗ missing │ 🗣️ sag           │ ElevenLabs text-to-speech with mac-style say UX.                │ openclaw-bundled   │
│ ✓ ready   │ 📜 session-logs   │ Search and analyze your own session logs (older/parent          │ openclaw-bundled   │
│           │                  │ conversations) using jq.                                        │                    │
│ ✗ missing │ 🗣️ sherpa-onnx-  │ Local text-to-speech via sherpa-onnx (offline, no cloud)        │ openclaw-bundled   │
│           │ tts              │                                                                 │                    │
│ ✓ ready   │ 📦 skill-creator  │ Create or update AgentSkills. Use when designing, structuring,  │ openclaw-bundled   │
│           │                  │ or packaging skills with scripts, references, and assets.       │                    │
│ ✗ missing │ 💬 slack          │ Use when you need to control Slack from OpenClaw via the slack  │ openclaw-bundled   │
│           │                  │ tool, including reacting to messages or pinning/unpinning       │                    │
│           │                  │ items in Slack channels or DMs.                                 │                    │
│ ✓ ready   │ 🌊 songsee        │ Generate spectrograms and feature-panel visualizations from     │ openclaw-bundled   │
│           │                  │ audio with the songsee CLI.                                     │                    │
│ ✓ ready   │ 🔊 sonoscli       │ Control Sonos speakers (discover/status/play/volume/group).     │ openclaw-bundled   │
│ ✗ missing │ 🎵 spotify-player │ Terminal Spotify playback/search via spogo (preferred) or       │ openclaw-bundled   │
│           │                  │ spotify_player.                                                 │                    │
│ ✓ ready   │ 📦 summarize      │ Summarize URLs or files with the summarize CLI (web, PDFs,      │ openclaw-workspace │
│           │                  │ images, audio, YouTube).                                        │                    │
│ ✓ ready   │ ✅ things-mac     │ Manage Things 3 via the `things` CLI on macOS (add/update       │ openclaw-bundled   │
│           │                  │ projects+todos via URL scheme; read/search/list from the local  │                    │
│           │                  │ Things database). Use when a user asks OpenClaw to add a task   │                    │
│           │                  │ to Things, list inbox/today/upcoming, search tasks, or inspect  │                    │
│           │                  │ projects/areas/tags.                                            │                    │
│ ✓ ready   │ 🧵 tmux           │ Remote-control tmux sessions for interactive CLIs by sending    │ openclaw-bundled   │
│           │                  │ keystrokes and scraping pane output.                            │                    │
│ ✗ missing │ 📋 trello         │ Manage Trello boards, lists, and cards via the Trello REST API. │ openclaw-bundled   │
│ ✓ ready   │ 🎞️ video-frames  │ Extract frames or short clips from videos using ffmpeg.         │ openclaw-bundled   │
```

## Notes / next steps

1) **Duplicate plugin id warning (hindsight-openclaw)**
   - Present at both:
     - `~/.openclaw/workspace/skills/hindsight/hindsight-integrations/openclaw/dist/index.js`
     - `~/.openclaw/extensions/hindsight-openclaw/dist/index.js`
   - Recommend: choose one canonical load path (prefer extension deploy) to eliminate duplication.

2) **Security audit warning:** extensions exist but `plugins.allow` not set.
   - `openclaw status` reports this as CRITICAL in security audit summary. Recommend setting `plugins.allow` to an explicit allowlist.

3) **Smoke agent not returning**
   - Next attempt: run with an explicit `--session-id` or `--to` so routing is unambiguous; or use `--deliver` to route output to a channel.
