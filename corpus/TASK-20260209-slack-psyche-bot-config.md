# TASK: Configure @psyche Slack Bot on Mac Mini

**To**: psyche
**From**: commander
**Reply-To**: commander
**CC**: commander
**Kind**: TASK
**Priority**: P1
**Exit-Code**: 0
**Completed-At**: 2026-02-10T00:18:40Z
**Claimed-At**: 2026-02-10T00:18:12Z
**Claimed-By**: psyche-Lisas-MacBook-Air
**Kanban**: DONE
**Status**: COMPLETE
**Issued**: 2026-02-09
**Fingerprint**: SLACK-PSYCHE-BOT-001
**Timeout**: none (requires Sovereign action first)

---

## Context

The constellation now has two chat channels operational:
- **Slack** (@ajna bot running on MBA via OpenClaw Socket Mode) — ACTIVE
- **Discord** (@Ajna bot running on MBA via OpenClaw Discord plugin) — ACTIVE

Per Sovereign directive, Psyche needs its own Slack bot (`@psyche`) on the Mac mini. This requires:
1. Sovereign creates a second Slack app in the Syncrescendence workspace
2. Psyche configures OpenClaw on Mac mini with the new bot tokens

## Sovereign Prerequisites (BEFORE Psyche can execute)

The Sovereign must complete these steps in the Slack Developer Portal:

### Step 1: Create New Slack App
1. Go to https://api.slack.com/apps
2. Click "Create New App" → "From scratch"
3. App Name: **Psyche**
4. Workspace: **Syncrescendence**

### Step 2: Configure Bot Scopes
Navigate to OAuth & Permissions → Bot Token Scopes. Add these scopes (matching @ajna's capabilities):

**Required Scopes:**
- `app_mentions:read` — React to @psyche mentions
- `channels:history` — Read channel messages
- `channels:read` — List channels
- `chat:write` — Send messages
- `emoji:read` — List custom emoji
- `groups:history` — Read private channel messages
- `groups:read` — List private channels
- `im:history` — Read DMs
- `im:read` — List DMs
- `im:write` — Open DMs
- `mpim:history` — Read group DMs
- `mpim:read` — List group DMs
- `pins:read` — List pins
- `pins:write` — Pin/unpin messages
- `reactions:read` — Read reactions
- `reactions:write` — Add reactions
- `users:read` — List users

### Step 3: Enable Socket Mode
1. Navigate to Socket Mode (left sidebar)
2. Enable Socket Mode
3. Create an App-Level Token with scope `connections:write`
4. Save the `xapp-...` token

### Step 4: Enable Events
1. Navigate to Event Subscriptions
2. Enable Events
3. Subscribe to bot events:
   - `app_mention`
   - `message.channels`
   - `message.groups`
   - `message.im`
   - `message.mpim`

### Step 5: Install to Workspace
1. Navigate to Install App
2. Click "Install to Workspace"
3. Authorize
4. Copy the Bot User OAuth Token (`xoxb-...`)

### Step 6: Provide Tokens to Psyche
Place in Psyche's `-INBOX/psyche/00-INBOX0/` or communicate directly:
- Bot Token: `xoxb-...`
- App Token: `xapp-...`

---

## Psyche Execution Steps (AFTER Sovereign provides tokens)

### 1. Update openclaw.json

Add/update the `channels.slack` section in `~/.openclaw/openclaw.json`:

```json
"channels": {
  "slack": {
    "mode": "socket",
    "webhookPath": "/slack/events",
    "enabled": true,
    "botToken": "xoxb-SOVEREIGN_PROVIDED_TOKEN",
    "appToken": "xapp-SOVEREIGN_PROVIDED_TOKEN",
    "userTokenReadOnly": true,
    "groupPolicy": "open",
    "dm": {
      "policy": "pairing"
    },
    "channels": {
      "#all-syncrescendence": {
        "allow": true
      }
    }
  }
}
```

### 2. Enable Slack Plugin

```bash
openclaw plugins enable slack
```

### 3. Restart Gateway

```bash
openclaw gateway restart
```

### 4. Verify

```bash
openclaw channels status
# Expected: Slack default: enabled, configured, running, bot:@psyche
openclaw channels capabilities
# Expected: Full Slack capabilities listed
```

### 5. Test

```bash
openclaw channels resolve '#all-syncrescendence'
# Expected: Returns channel ID
```

---

## Success Criteria
- `openclaw channels status` shows Slack running with bot @psyche
- @psyche can read and respond in #all-syncrescendence
- @ajna (MBA) and @psyche (Mac mini) coexist in the same workspace without conflicts
- Both bots appear in the Slack workspace member list
