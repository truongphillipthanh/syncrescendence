# RESULT — TASK-20260205-sync_outfitment (Ajna)

Date: 2026-02-05 (America/Los_Angeles)
Host: ajna-M1-Mac-mini

## 1) OpenClaw version

```
2026.2.3-1
```

## 2) `openclaw doctor --non-interactive` summary

Key findings:
- **CRITICAL:** OAuth dir missing: `~/.openclaw/credentials`
- Discord connectivity OK: `@Ajna`
- Skills: **Eligible 35**, **Missing requirements 15**
- Plugins: **Loaded 2**, **Disabled 29**, **Errors 0**

Receipt (full output captured at `/tmp/openclaw.doctor.txt`):

```
◇  State integrity
  - CRITICAL: OAuth dir missing (~/.openclaw/credentials).

◇  Skills status
  Eligible: 35
  Missing requirements: 15

◇  Plugins
  Loaded: 2
  Disabled: 29
  Errors: 0

Discord: ok (@Ajna)
Run "openclaw doctor --fix" to apply changes.
```

## 3) Redacted config (secrets removed)

Redacted config written to:
- `/tmp/openclaw.json.redacted`

Relevant excerpts:

### `auth.profiles`
```json
{
  "openai-codex:default": {
    "provider": "openai-codex",
    "mode": "oauth"
  }
}
```

### `plugins.load.paths` (scaffolding applied)
**Expected paths added to Ajna config:**
- `~/.openclaw/workspace/skills/supermemory`
- `~/.openclaw/workspace/skills/hindsight/hindsight-integrations/openclaw`

```json
{
  "load": {
    "paths": [
      "/Users/home/.openclaw/workspace/skills/supermemory",
      "/Users/home/.openclaw/workspace/skills/hindsight/hindsight-integrations/openclaw"
    ]
  },
  "entries": {
    "discord": {
      "enabled": true
    }
  }
}
```

## 4) Skills + plugins inventory

### Built-in skills directory (OpenClaw install)
OpenClaw binary resolves to the NVM-managed install; skills are present at:
- `/Users/home/.nvm/versions/node/v24.13.0/lib/node_modules/openclaw/skills`

Receipt:
- full listing captured at `/tmp/openclaw.skills.txt`

### Workspace skills directory
Before this task, Ajna had **no** `~/.openclaw/workspace/skills` directory.

During this task, the following directories were **created as scaffolding only** (no code was available locally to mirror in):
- `~/.openclaw/workspace/skills/supermemory/`
- `~/.openclaw/workspace/skills/hindsight/hindsight-integrations/openclaw/`

### Plugins install location
- `~/.openclaw/plugins` **does not exist** on Ajna.
- NPM global packages `openclaw-supermemory` / `hindsight-openclaw` could not be found via `npm view` (likely private/local or non-npm distribution).

## 5) Psyche expectation comparison

**Requirement:** `plugins.load.paths` includes:
- `~/.openclaw/workspace/skills/supermemory` ✅ added
- `~/.openclaw/workspace/skills/hindsight/hindsight-integrations/openclaw` ✅ added

**Requirement:** plugin installs show `openclaw-supermemory` and `hindsight-openclaw` present
- ❌ not present / not discoverable on this machine with current info

## 6) Repeatable sync mechanism (proposed)

Because the *actual* Psyche workspace skill/plugin code was not present locally in this repo checkout, the remaining step is to establish a reliable source of truth and a transport:

### Option A (recommended): rsync from Psyche over SSH (no secrets)
Create a script (on Ajna) that pulls only the workspace skills:

```bash
#!/usr/bin/env bash
set -euo pipefail
SRC_HOST="psyche"  # (ssh config alias)
SRC_DIR="/Users/system/.openclaw/workspace/skills/"
DST_DIR="$HOME/.openclaw/workspace/skills/"
mkdir -p "$DST_DIR"
rsync -a --delete \
  --exclude '*/.git' \
  --exclude '**/node_modules' \
  "$SRC_HOST:$SRC_DIR" "$DST_DIR"
```

Then run `openclaw doctor --fix` and restart gateway if needed.

### Option B: vendor the skills into `syncrescendence` as a git subtree/submodule
Pros: single repo holds non-secret outfitment.
Cons: you must keep it updated + resolve licensing/private code concerns.

### Option C: clawhub install (if these are published skills)
If `supermemory` / `hindsight` are available on clawhub, install them on both machines and pin versions.

## Notes / safety
- Config redaction was corrected to avoid leaking `token` values (macOS `sed` doesn’t support `\s`; used `[[:space:]]`).
- No secrets were copied from Psyche. Only scaffolding (`plugins.load.paths`) was applied.
