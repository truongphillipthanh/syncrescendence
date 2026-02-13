---
kind: clarescence
id: CLARESCENCE-2026-02-09-slack-channel-architecture
title: "Slack Channel Architecture: Constellation Communication Topology"
date: 2026-02-09
status: ready-for-execution
agent: psyche
passes: 6
linear: Epic 5 (Constellation Reconfiguration)
---

# CLARESCENCE: Slack Channel Architecture

**Date**: 2026-02-09
**Agent**: Psyche (CTO / Synaptarch)
**Scope**: Multi-channel Slack workspace design, dual-bot deployment, integration routing, and cross-platform bridging for the Syncrescendence constellation
**Predecessors**:
  - REF-SAAS_INTEGRATION_ARCHITECTURE.md (Section IV.B, IV.C, V.B, XI)
  - CLARESCENCE-2026-02-07-mcp-bridge-architecture.md (Slack MCP surface audit)
  - CLARESCENCE-2026-02-08-psyche-machine-elucidation.md (DEC-PSYCHE-007: twin coordination via Slack)
  - CLARESCENCE-2026-02-08-constellation-modus-operandi.md (4-agent always-on architecture)
  - CLARESCENCE-2026-02-09-mba-ajna-setup.md (MBA OpenClaw deployment)
  - DYN-TWIN_COORDINATION_PROTOCOL.md (Ajna/Psyche coordination rules)

---

## PASS 1: Problem Statement

### Current State

The Syncrescendence Slack workspace is operational but minimal:

| Dimension | Current Value |
|-----------|---------------|
| Workspace | Syncrescendence |
| Team ID | T0AB6TCRZGF |
| Channels | 1 -- `#all-syncrescendence` (C0ACGKZ0EU8) |
| Bots | 1 -- `@ajna` running on MBA via OpenClaw Socket Mode |
| Bot Capabilities | send, broadcast, react, reactions, read, edit, delete, pin, unpin, list-pins, member-info, emoji-list |
| DM Policy | pairing |
| Group Policy | open |
| Integrations | None active (Linear, ClickUp, GitHub all planned but not connected) |
| Cross-post | None (Slack-Discord bridge via Make not configured) |

**What works**: The `@ajna` bot on the MBA can send and receive messages in `#all-syncrescendence`. The Sovereign can interact with Ajna through Slack. Basic communication is functional.

**What does not work**:

1. **Single-channel bottleneck**: Every signal -- strategic decisions, CI/CD alerts, task updates, integration notifications, sovereign commands -- flows through one channel. No separation of concerns. Signal drowns in noise.

2. **Wrong bot on wrong machine**: `@ajna` (CSO/Strategos) is the only Slack bot, but Slack is designated as Psyche's (CTO/Synaptarch) primary channel per REF-SAAS_INTEGRATION_ARCHITECTURE.md and DYN-TWIN_COORDINATION_PROTOCOL.md. Psyche has no Slack presence. The architecture is inverted.

3. **No integration routing**: Linear issues, GitHub events, ClickUp tasks, and service alerts have nowhere to go. The planned integrations (Linear -> Slack P0 CONFIGURING, ClickUp -> Slack P1 CONFIGURING) cannot be activated without dedicated channels to receive them.

4. **No cross-post bridge**: The Slack-Discord bridge (Make Scenario B, P1) requires channel-level routing rules. With one channel, the bridge would either cross-post everything (noise) or nothing (useless).

5. **No notification tiering**: The Sovereign receives no differentiated alerts. A service crash and a routine task completion are indistinguishable.

### Desired State

A multi-channel, dual-bot, fully integrated Slack workspace where:

- Each agent has a dedicated channel for role-specific communication
- System-wide channels aggregate cross-cutting concerns (alerts, decisions)
- Integration channels receive structured updates from Linear, GitHub, and ClickUp
- Two bots operate with clear scope separation: `@ajna` (strategic/sovereign) and `@psyche` (operational/infrastructure)
- Cross-post rules bridge selected channels to Discord with loop prevention
- Notification levels are tiered so the Sovereign can tune signal-to-noise per channel

### Gap Analysis

| Gap | Severity | Blocks |
|-----|----------|--------|
| No channel taxonomy | HIGH | All integration routing, notification tiering |
| No `@psyche` bot | HIGH | Psyche has no Slack presence; CTO role unfilled on primary channel |
| No Linear integration | HIGH | P0 integration (REF-SAAS Section IV.B) stalled |
| No ClickUp integration | MEDIUM | P1 integration (REF-SAAS Section IV.C) stalled |
| No GitHub integration | MEDIUM | Event visibility gap |
| No cross-post bridge | MEDIUM | Ajna (Discord) has no Slack visibility; Psyche has no Discord visibility |
| No service alerting channel | MEDIUM | Watchdog/launchd failures invisible to Sovereign in Slack |

---

## PASS 2: Channel Taxonomy

### Design Principles

1. **Purpose-per-channel**: Each channel has one primary function. No multiplex.
2. **Agent ownership**: Agent channels are owned by their respective bot. The owning bot is the primary responder.
3. **Notification tiering**: Channels are classified as URGENT (immediate push), ACTIVE (badge), or PASSIVE (no notification). Sovereign configures per-channel notification settings in Slack client.
4. **Cross-post eligibility**: Only channels marked BRIDGE are candidates for Slack-Discord mirroring.
5. **Integration routing**: External events route to specific channels, never to `#all-syncrescendence`.

### Channel Structure

#### Tier 1: System-Wide Channels

| Channel | Purpose | Who Posts | Who Listens | Notification | Bridge | Keep/New |
|---------|---------|-----------|-------------|-------------|--------|----------|
| `#all-syncrescendence` | General coordination, announcements, sovereign broadcasts, human-readable summaries | Sovereign, any bot (announcements only) | Everyone | ACTIVE | YES | KEEP |
| `#alerts` | Service health, CI/CD failures, launchd crashes, watchdog triggers, security events | `@psyche` (automated), system webhooks | Sovereign, Psyche | URGENT | NO | NEW |
| `#sovereign-decisions` | Async decision queue from agents to Sovereign. Replaces/mirrors `-SOVEREIGN/` filesystem queue | `@ajna`, `@psyche` | Sovereign | URGENT | NO | NEW |

**`#all-syncrescendence`** (C0ACGKZ0EU8): Retained as the human-readable general channel. Reduce its scope: no automated integration dumps, no raw event streams. Use for announcements, daily summaries, and ad-hoc conversation. This is the channel the Sovereign reads first.

**`#alerts`**: Critical infrastructure channel. Only fires when something is broken or needs immediate attention. Sources: launchd service crashes (via watchdog script posting to Slack), Docker container health failures, git sync failures, API key expiration warnings, CI/CD pipeline failures (GitHub Actions). Notification level URGENT means this channel overrides Do Not Disturb.

**`#sovereign-decisions`**: When agents need Sovereign input on blocking decisions (DA-01 through DA-12 style atoms), they post here with structured decision requests. Format: decision ID, context, options, recommended default, deadline. This channel replaces the need to check `-SOVEREIGN/` folder on disk. Not bridged to Discord -- sovereign decisions stay in the secured Slack workspace.

#### Tier 2: Agent-Specific Channels

| Channel | Purpose | Primary Bot | Who Posts | Who Listens | Notification | Bridge |
|---------|---------|-------------|-----------|-------------|-------------|--------|
| `#ajna-strategic` | CSO strategic direction, orchestration signals, dispatch summaries, intention compass updates | `@ajna` | `@ajna`, Sovereign | Sovereign, Psyche | ACTIVE | YES |
| `#psyche-ops` | CTO operational status, infrastructure state, automation reports, service health summaries | `@psyche` | `@psyche`, Sovereign | Sovereign, Ajna | ACTIVE | YES |
| `#commander-execution` | COO execution logs, directive completions, commit summaries, task dispatches | `@psyche` | `@psyche` (relaying Commander output) | Sovereign, agents | PASSIVE | NO |
| `#adjudicator-qa` | CQO quality reports, test results, formatting passes, mechanical execution receipts | `@psyche` | `@psyche` (relaying Adjudicator output) | Commander, Sovereign | PASSIVE | NO |
| `#cartographer-intelligence` | CIO corpus surveys, drift reports, coverage maps, staleness alerts | `@psyche` | `@psyche` (relaying Cartographer output) | Sovereign, Commander, Ajna | PASSIVE | YES |

**Design rationale for relay pattern**: Commander, Adjudicator, and Cartographer are CLI agents (Claude Code, Codex CLI, Gemini CLI). They do not have native Slack connectivity. Their outputs flow to Slack via `@psyche` on the Mac mini, which reads RESULT/CONFIRM files from `-OUTBOX/` and posts summaries to the appropriate channel. This is the CTO's operational synthesis role -- Psyche digests raw execution receipts into human-readable Slack posts.

**`#ajna-strategic`**: Ajna's home channel. The CSO posts strategic assessments, orchestration decisions, intention compass updates, and dispatch summaries here. When Ajna dispatches tasks to the constellation, a summary appears in this channel. Bridged to Discord so Ajna's Discord community channel mirrors strategic outputs.

**`#psyche-ops`**: Psyche's home channel. The CTO posts infrastructure state (service health summaries, deployment status, automation reports). This is the operational pulse of the constellation. Bridged to Discord for visibility.

**`#commander-execution`**: Receives ClickUp task change notifications (via ClickUp integration) and `@psyche` relay of Commander's execution logs. The COO's work becomes visible here without Commander needing Slack access. Not bridged -- execution details are internal.

**`#adjudicator-qa`**: Quality assurance channel. `@psyche` relays Adjudicator's RESULT files (test outcomes, lint reports, formatting passes). Commander monitors this for task completion signals. Not bridged -- too granular for Discord.

**`#cartographer-intelligence`**: Intelligence products from the CIO. Corpus surveys, drift detection reports, coverage analysis. Bridged to Discord because intelligence products have strategic value that Ajna (Discord-native) should see.

#### Tier 3: Integration Channels

| Channel | Purpose | Who Posts | Who Listens | Notification | Bridge |
|---------|---------|-----------|-------------|-------------|--------|
| `#linear-updates` | Linear issue state changes, PR links, sprint updates for the SYN project | Linear bot (native integration) | Commander, Sovereign | PASSIVE | NO |
| `#github-events` | Push events, PR opened/merged/closed, release tags, Actions failures | GitHub bot (webhook or native) | Commander, Psyche, Sovereign | PASSIVE | YES |

**`#linear-updates`**: Receives all Linear SYN-project issue state changes via Linear's native Slack integration (Section IV.B of REF-SAAS_INTEGRATION_ARCHITECTURE.md). This is the P0 integration. Filtering: only SYN-project issues, state changes (Todo -> In Progress -> Done), assignee changes, and comment additions. Not every field edit.

**`#github-events`**: Receives GitHub push notifications, PR lifecycle events (opened, review requested, merged, closed), release publications, and Actions workflow failures. Bridged to Discord (mirrors Make Scenario A: GitHub -> Discord from REF-SAAS Section V.A).

### Channel Summary Table

| # | Channel | Notification | Bridge to Discord |
|---|---------|-------------|-------------------|
| 1 | `#all-syncrescendence` | ACTIVE | YES |
| 2 | `#alerts` | URGENT | NO |
| 3 | `#sovereign-decisions` | URGENT | NO |
| 4 | `#ajna-strategic` | ACTIVE | YES |
| 5 | `#psyche-ops` | ACTIVE | YES |
| 6 | `#commander-execution` | PASSIVE | NO |
| 7 | `#adjudicator-qa` | PASSIVE | NO |
| 8 | `#cartographer-intelligence` | PASSIVE | YES |
| 9 | `#linear-updates` | PASSIVE | NO |
| 10 | `#github-events` | PASSIVE | YES |

**Total**: 10 channels (1 existing + 9 new).

### Notification Configuration (Sovereign Slack Client)

After channel creation, the Sovereign should configure notification preferences:

| Notification Level | Slack Setting | Channels |
|--------------------|---------------|----------|
| URGENT | All messages + override DND | `#alerts`, `#sovereign-decisions` |
| ACTIVE | All messages (default) | `#all-syncrescendence`, `#ajna-strategic`, `#psyche-ops` |
| PASSIVE | Mentions only | `#commander-execution`, `#adjudicator-qa`, `#cartographer-intelligence`, `#linear-updates`, `#github-events` |

---

## PASS 3: Bot Architecture

### Two-Bot Topology

| Bot | App Name | Runs On | Model Backend | Primary Channels | Role |
|-----|----------|---------|---------------|------------------|------|
| `@ajna` | Syncrescendence Ajna | MacBook Air | Kimi K2.5 (NVIDIA NIM) | `#ajna-strategic`, `#all-syncrescendence`, `#sovereign-decisions` | Strategic responder, sovereign interaction, decision requests |
| `@psyche` | Syncrescendence Psyche | Mac mini | GPT-5.3-codex | `#psyche-ops`, `#commander-execution`, `#adjudicator-qa`, `#cartographer-intelligence`, `#alerts` | Operational responder, infrastructure reporting, agent relay |

### Scope Separation

**`@ajna` (CSO) handles:**
- Direct Sovereign conversation in `#all-syncrescendence` and `#ajna-strategic`
- Posting decision atoms to `#sovereign-decisions`
- Strategic dispatch summaries (who was dispatched what, expected outcomes)
- Intention compass updates
- Orchestration commands (Sovereign tells Ajna to dispatch work)

**`@psyche` (CTO) handles:**
- Infrastructure reporting in `#psyche-ops`
- Service alert posting to `#alerts` (via watchdog integration)
- Relaying CLI agent outputs to `#commander-execution`, `#adjudicator-qa`, `#cartographer-intelligence`
- Responding to operational queries ("What is the service status?", "Show me recent commits")
- ClickUp task change relay to `#commander-execution`

**Shared responsibilities:**
- Both bots listen in `#all-syncrescendence` but only respond when addressed by name or when the message is relevant to their role
- Both can read all channels (for context awareness) but only post to their designated channels
- DMs to either bot route to the appropriate OpenClaw agent on its respective machine

### Creating the `@psyche` Slack App

The `@ajna` app already exists and runs via OpenClaw Socket Mode on the MBA. A second Slack app is required for `@psyche`. This requires a separate Slack app because:

1. Each OpenClaw instance needs its own Socket Mode connection (one per app)
2. Bot tokens are per-app; two bots = two apps
3. Scope separation is enforced at the app level, not just in code

#### Required Slack App Configuration for `@psyche`

**App Name**: Syncrescendence Psyche
**Display Name**: psyche
**Bot Username**: @psyche
**Default Channel**: `#psyche-ops`

#### Required OAuth Bot Token Scopes

These scopes must be granted to the `@psyche` bot token (`xoxb-*`):

| Scope | Purpose |
|-------|---------|
| `channels:history` | Read messages in public channels |
| `channels:read` | List public channels, get channel info |
| `channels:join` | Join public channels programmatically |
| `chat:write` | Send messages as @psyche |
| `chat:write.customize` | Send with custom username/icon per message |
| `emoji:read` | List custom emoji (diagnostic) |
| `files:read` | Read file metadata (for shared screenshots, logs) |
| `files:write` | Upload files (log dumps, reports) |
| `groups:history` | Read messages in private channels (if any) |
| `groups:read` | List private channels |
| `im:history` | Read DM history |
| `im:read` | List DM channels |
| `im:write` | Open DM channels |
| `mpim:history` | Read group DM history |
| `mpim:read` | List group DMs |
| `pins:read` | List pinned messages |
| `pins:write` | Pin/unpin messages |
| `reactions:read` | Read reactions on messages |
| `reactions:write` | Add/remove reactions |
| `users:read` | List workspace members |
| `users:read.email` | Read member email (for identity mapping) |

**Socket Mode**: Enable (same as `@ajna`). Requires an App-Level Token (`xapp-*`) with `connections:write` scope.

**Event Subscriptions** (Socket Mode events):

| Event | Purpose |
|-------|---------|
| `message.channels` | React to messages in public channels |
| `message.groups` | React to messages in private channels |
| `message.im` | React to DMs to @psyche |
| `message.mpim` | React to group DMs |
| `app_mention` | Respond when @psyche is mentioned |
| `reaction_added` | Track emoji reactions (for acknowledgment protocol) |

#### OpenClaw Configuration for `@psyche`

The `@psyche` bot token and app token go into the Mac mini's OpenClaw configuration. The Slack channel skill on the Mac mini connects as `@psyche` via Socket Mode.

In the Mac mini's `~/.openclaw/openclaw.json` or equivalent Slack skill config:

```json
{
  "channels": {
    "slack": {
      "enabled": true,
      "mode": "socket",
      "appToken": "xapp-PSYCHE-APP-LEVEL-TOKEN",
      "botToken": "xoxb-PSYCHE-BOT-TOKEN",
      "defaultChannel": "psyche-ops",
      "capabilities": [
        "send", "broadcast", "react", "reactions", "read",
        "edit", "delete", "pin", "unpin", "list-pins",
        "member-info", "emoji-list", "file-upload"
      ],
      "dmPolicy": "pairing",
      "groupPolicy": "open"
    }
  }
}
```

#### Updating `@ajna` Configuration on MBA

The MBA's OpenClaw Slack config for `@ajna` should be updated to reflect the new channel structure. Update the default channel and add channel awareness:

```json
{
  "channels": {
    "slack": {
      "enabled": true,
      "mode": "socket",
      "appToken": "xapp-AJNA-EXISTING-APP-TOKEN",
      "botToken": "xoxb-AJNA-EXISTING-BOT-TOKEN",
      "defaultChannel": "ajna-strategic",
      "capabilities": [
        "send", "broadcast", "react", "reactions", "read",
        "edit", "delete", "pin", "unpin", "list-pins",
        "member-info", "emoji-list"
      ],
      "dmPolicy": "pairing",
      "groupPolicy": "open"
    }
  }
}
```

**Change from current**: `defaultChannel` moves from `all-syncrescendence` to `ajna-strategic`. Ajna still posts to `#all-syncrescendence` and `#sovereign-decisions` as needed, but her home channel is `#ajna-strategic`.

---

## PASS 4: Integration Routing

### Event Flow Architecture

```
                    EXTERNAL SOURCES
                         |
          +--------------+--------------+
          |              |              |
     Linear API    GitHub Webhooks  ClickUp API
          |              |              |
          v              v              v
    Native Slack    Make Scenario   Native Slack
    Integration     or Webhook      Integration
          |              |              |
          v              v              v
   #linear-updates  #github-events  #commander-execution
          |              |              |
          +------+-------+------+------+
                 |              |
                 v              v
          @psyche relay    @psyche relay
          to agent          to #alerts
          channels          (failures only)
                 |
                 v
         Agent-specific channels
         (summaries, not raw events)
```

### Route 1: Linear -> Slack (P0, CONFIGURING)

**Source**: Linear SYN-project issue events
**Target**: `#linear-updates`
**Method**: Linear's native Slack integration (first-party, OAuth-based)
**Secondary routing**: `@psyche` monitors `#linear-updates` and posts a summary to the relevant agent channel when an issue is assigned or transitions state:

| Linear Event | Primary Channel | Secondary Channel | Posted By |
|--------------|----------------|-------------------|-----------|
| Issue created (SYN-*) | `#linear-updates` | `#all-syncrescendence` (if P0/P1) | Linear bot, then @psyche summary |
| Issue state change (Todo -> In Progress) | `#linear-updates` | Channel of assigned agent | Linear bot, then @psyche |
| Issue state change (In Progress -> Done) | `#linear-updates` | `#all-syncrescendence` (completion announcement) | Linear bot, then @psyche |
| Issue commented | `#linear-updates` | -- | Linear bot only |
| Issue assigned | `#linear-updates` | Channel of assignee agent | Linear bot, then @psyche |

**Setup steps**:
1. In Linear: Settings -> Integrations -> Slack -> Install
2. Authorize the Syncrescendence workspace
3. Select `#linear-updates` as the target channel
4. Configure filter: SYN project only
5. Enable: issue created, state changes, assignee changes, comments
6. Enable: Slack -> Linear issue creation (allows typing `/linear create` in Slack)
7. Test: Create SYN-TEST issue in Linear, verify it appears in `#linear-updates`

### Route 2: GitHub -> Slack (Planned)

**Source**: GitHub `syncrescendence` repository events
**Target**: `#github-events`
**Method**: GitHub Slack integration (native) OR webhook via Make

**Option A -- GitHub native Slack app** (preferred):
1. Install GitHub app in Slack workspace
2. In `#github-events`: `/github subscribe owner/syncrescendence`
3. Configure: pushes, pull_requests, releases, deployments, workflows (failures only)
4. Disable: issues (handled by Linear), comments (too noisy)

**Option B -- Make webhook** (if native app is insufficient):
1. GitHub webhook -> Make -> Slack incoming webhook to `#github-events`
2. Make scenario filters: only `push` to main, `pull_request` open/merge/close, `release` published, `workflow_run` failed
3. Format: embed with commit count, author, diff stat, link

**Secondary routing for failures**: If a GitHub Actions workflow fails, `@psyche` cross-posts to `#alerts` with URGENT formatting.

| GitHub Event | Primary Channel | Secondary Channel | Condition |
|--------------|----------------|-------------------|-----------|
| Push to main | `#github-events` | -- | Always |
| PR opened | `#github-events` | -- | Always |
| PR merged | `#github-events` | `#all-syncrescendence` | Summary only |
| PR closed (not merged) | `#github-events` | -- | Always |
| Release published | `#github-events` | `#all-syncrescendence` | Always |
| Workflow failed | `#github-events` | `#alerts` | Always |
| Workflow succeeded | `#github-events` | -- | Always |

### Route 3: ClickUp -> Slack (P1, CONFIGURING)

**Source**: ClickUp task events in relevant spaces
**Target**: `#commander-execution`
**Method**: ClickUp's native Slack integration

**Setup steps**:
1. In ClickUp: Integrations -> Slack -> Install
2. Authorize the Syncrescendence workspace
3. Map ClickUp spaces/lists to `#commander-execution`
4. Configure: task created, status changed, assignee changed, due date changes
5. Enable: Slack -> ClickUp task creation (`/clickup create`)
6. Test: Create a task in ClickUp, verify it appears in `#commander-execution`

### Route 4: Service Alerts -> Slack

**Source**: Mac mini watchdog scripts, launchd service health checks, Docker container monitoring
**Target**: `#alerts`
**Method**: `@psyche` bot posts directly via OpenClaw Slack skill

**Implementation**: The existing watchdog/health check scripts on the Mac mini should be extended to call a Slack posting function when a failure is detected. The simplest approach:

```bash
# In watchdog scripts or health check cron:
post_alert() {
  local message="$1"
  local severity="$2"  # CRITICAL, WARNING, INFO
  # Use OpenClaw's Slack skill to post to #alerts
  openclaw skill slack send --channel alerts --message ":rotating_light: [$severity] $message"
}

# Example usage in a health check:
if ! curl -sf http://localhost:6333/healthz > /dev/null 2>&1; then
  post_alert "Qdrant (port 6333) is not responding" "CRITICAL"
fi
```

**Alert sources to configure**:

| Source | Check Method | Frequency | Severity |
|--------|-------------|-----------|----------|
| OpenClaw gateway (port 18789) | HTTP health check | Every 5 min | CRITICAL |
| Qdrant (port 6333) | HTTP health check | Every 5 min | CRITICAL |
| Neo4j (port 7474) | HTTP health check | Every 5 min | CRITICAL |
| Graphiti (port 8001) | HTTP health check | Every 5 min | CRITICAL |
| Chroma (port 8765) | HTTP health check | Every 5 min | WARNING |
| launchd watchers | `launchctl list` exit code check | Every 10 min | CRITICAL |
| Git sync (MBA) | Last sync timestamp check | Every 30 min | WARNING |
| Disk space | `df -h` threshold (>90%) | Every hour | WARNING |

### Route 5: Make/Zapier Scenarios Required

| Scenario | Direction | Trigger | Action | Priority |
|----------|-----------|---------|--------|----------|
| Scenario B-1 | Slack -> Discord | Message in bridged Slack channel | Post to mapped Discord channel | P1 |
| Scenario B-2 | Discord -> Slack | Message in bridged Discord channel | Post to mapped Slack channel | P1 |
| GitHub -> Discord (A) | GitHub -> Discord | Already in REF-SAAS Section V.A | -- | P0 |

Scenario B is detailed in Pass 5 (Cross-Post Protocol).

---

## PASS 5: Cross-Post Protocol (Slack <-> Discord Bridge)

### Bridge Topology

Per REF-SAAS_INTEGRATION_ARCHITECTURE.md Section V.B, the Slack-Discord cross-post bridge uses Make (two scenarios, one per direction). This pass specifies the channel-level mapping and loop prevention rules.

### Channel Mapping

| Slack Channel | Discord Channel | Direction | Notes |
|---------------|----------------|-----------|-------|
| `#all-syncrescendence` | `#general` | Bidirectional | Main coordination channel |
| `#ajna-strategic` | `#ajna-strategic` | Slack -> Discord | Ajna's strategic outputs visible in Discord |
| `#psyche-ops` | `#psyche-ops` | Slack -> Discord | Ops status visible in Discord |
| `#cartographer-intelligence` | `#intelligence` | Slack -> Discord | Survey results visible in Discord |
| `#github-events` | `#repo-events` | Slack -> Discord | Mirrors Make Scenario A (GitHub -> Discord) |

**NOT bridged** (stays Slack-only):
- `#alerts` -- security-sensitive, infrastructure-specific
- `#sovereign-decisions` -- private decision queue
- `#commander-execution` -- too granular
- `#adjudicator-qa` -- too granular
- `#linear-updates` -- internal task tracking noise

### Loop Prevention Protocol

Cross-post loops are the primary risk. If Slack posts to Discord and Discord posts back to Slack, an infinite cascade results. Prevention:

**Rule 1: Source Tagging**. Every cross-posted message is prefixed with a source tag:
- Slack -> Discord: Message is posted with prefix `[via Slack]` and uses a webhook bot name (e.g., "Slack Bridge") distinct from any Discord bot
- Discord -> Slack: Message is posted with prefix `[via Discord]` and uses a bot identity distinct from `@ajna` and `@psyche`

**Rule 2: Bot Ignore**. Each Make scenario ignores messages from:
- The bridge bot itself (prevent self-loop)
- Messages that already contain a cross-post source tag (prevent echo-loop)
- Messages from other integration bots (Linear bot, GitHub bot) -- these have their own routing

**Rule 3: Author Filtering**. The Make scenario checks the message author:
- If the author is the Slack-Discord bridge webhook/bot, SKIP
- If the message body starts with `[via Slack]` or `[via Discord]`, SKIP

### Make Scenario B Specification

#### Scenario B-1: Slack -> Discord

```
Trigger: Slack — Watch for New Messages in Channel
  Channels: [#all-syncrescendence, #ajna-strategic, #psyche-ops,
             #cartographer-intelligence, #github-events]
  Filter:
    - bot_id NOT IN [bridge-bot-id, linear-bot-id, github-bot-id]
    - text does NOT start with "[via Discord]"

Router: Map Slack channel -> Discord channel
  #all-syncrescendence     -> Discord #general
  #ajna-strategic          -> Discord #ajna-strategic
  #psyche-ops              -> Discord #psyche-ops
  #cartographer-intelligence -> Discord #intelligence
  #github-events           -> Discord #repo-events

Action: Discord — Send Message via Webhook
  Webhook URL: [per-channel Discord webhook]
  Username: "Slack Bridge"
  Avatar: [Slack logo or custom bridge icon]
  Content: "[via Slack] **{sender_name}** in #{channel_name}:\n{message_text}"
  Embeds: [preserve any Slack attachments/blocks as Discord embeds]
```

#### Scenario B-2: Discord -> Slack

```
Trigger: Discord — Watch for New Messages in Channel
  Channels: [#general, #ajna-strategic, #psyche-ops, #intelligence]
  Filter:
    - author is NOT a bot (or specifically: NOT the Slack Bridge webhook)
    - content does NOT start with "[via Slack]"

Router: Map Discord channel -> Slack channel
  Discord #general           -> #all-syncrescendence
  Discord #ajna-strategic    -> #ajna-strategic
  Discord #psyche-ops        -> #psyche-ops
  Discord #intelligence      -> #cartographer-intelligence

Action: Slack — Send Message
  Bot Token: [dedicated bridge bot token, NOT @ajna or @psyche token]
  Channel: [mapped Slack channel]
  Text: "[via Discord] *{author_username}* in #{discord_channel}:\n{content}"
  Username Override: "Discord Bridge"
```

**Note on bridge bot identity**: The bridge should use a THIRD identity in Slack -- not `@ajna` or `@psyche`. This can be achieved by using `chat:write.customize` scope with a generic app, or by creating a minimal third Slack app ("Syncrescendence Bridge") solely for cross-posting. This prevents confusion about which bot "said" something and makes the source tag filtering clean.

### Rate Limiting

Make free tier: 1,000 operations/month. Paid: 10,000+.

**Estimate**: With 5 bridged channels and moderate activity (20 messages/channel/day across all channels = ~100 cross-posts/day = ~3,000/month), the free tier is borderline. If cross-post volume exceeds expectations:
- Reduce bridged channels (drop `#github-events` which is already covered by Scenario A)
- Batch messages (aggregate 5-minute windows into single cross-posts)
- Upgrade Make plan

---

## PASS 6: Implementation Checklist

### Phase 1: Channel Creation (Sovereign, ~10 minutes)

These steps must be performed by the Sovereign (workspace admin) in the Slack web or desktop client.

- [ ] **1.1** Create `#alerts` channel
  - Description: "Service health, CI/CD failures, infrastructure alerts. URGENT notifications."
  - Set to public
- [ ] **1.2** Create `#sovereign-decisions` channel
  - Description: "Async decision queue from constellation agents to Sovereign. URGENT notifications."
  - Set to public (or private if preferred -- only bots + Sovereign need access)
- [ ] **1.3** Create `#ajna-strategic` channel
  - Description: "CSO strategic direction, orchestration signals, intention compass updates."
  - Set to public
- [ ] **1.4** Create `#psyche-ops` channel
  - Description: "CTO operational status, infrastructure reporting, automation state."
  - Set to public
- [ ] **1.5** Create `#commander-execution` channel
  - Description: "COO execution logs, directive completions, ClickUp task updates."
  - Set to public
- [ ] **1.6** Create `#adjudicator-qa` channel
  - Description: "CQO quality reports, test results, mechanical execution receipts."
  - Set to public
- [ ] **1.7** Create `#cartographer-intelligence` channel
  - Description: "CIO corpus surveys, drift reports, coverage analysis."
  - Set to public
- [ ] **1.8** Create `#linear-updates` channel
  - Description: "Linear SYN-project issue state changes. Automated feed."
  - Set to public
- [ ] **1.9** Create `#github-events` channel
  - Description: "GitHub push events, PR lifecycle, releases, workflow failures."
  - Set to public
- [ ] **1.10** Configure notification preferences per the table in Pass 2 (URGENT/ACTIVE/PASSIVE)

### Phase 2: Create `@psyche` Slack App (Sovereign, ~15 minutes)

- [ ] **2.1** Go to https://api.slack.com/apps -> Create New App -> From Scratch
  - App Name: `Syncrescendence Psyche`
  - Workspace: Syncrescendence
- [ ] **2.2** Navigate to "OAuth & Permissions"
  - Add all Bot Token Scopes listed in Pass 3 (channels:history, channels:read, channels:join, chat:write, chat:write.customize, emoji:read, files:read, files:write, groups:history, groups:read, im:history, im:read, im:write, mpim:history, mpim:read, pins:read, pins:write, reactions:read, reactions:write, users:read, users:read.email)
- [ ] **2.3** Navigate to "Socket Mode" -> Enable
  - Generate an App-Level Token with `connections:write` scope
  - Name: `psyche-socket-token`
  - Record the `xapp-*` token
- [ ] **2.4** Navigate to "Event Subscriptions" -> Enable Events
  - Subscribe to bot events: `message.channels`, `message.groups`, `message.im`, `message.mpim`, `app_mention`, `reaction_added`
- [ ] **2.5** Navigate to "App Home"
  - Set Display Name: `Psyche`
  - Set Default Username: `psyche`
  - Enable "Messages Tab" for DMs
  - Enable "Allow users to send Slash commands and messages from the messages tab"
- [ ] **2.6** Install App to Workspace
  - Click "Install to Workspace" -> Authorize
  - Record the Bot User OAuth Token (`xoxb-*`)
- [ ] **2.7** Invite `@psyche` to all channels:
  - In each channel, type `/invite @Psyche` or use the channel settings
  - Required channels: `#psyche-ops`, `#alerts`, `#commander-execution`, `#adjudicator-qa`, `#cartographer-intelligence`, `#all-syncrescendence`

### Phase 3: Configure `@psyche` on Mac Mini (Psyche, ~10 minutes)

- [ ] **3.1** SSH into Mac mini (or work locally)
- [ ] **3.2** Add Slack tokens to OpenClaw environment:
  ```bash
  # Add to ~/.openclaw/.env (or wherever OpenClaw reads env vars)
  echo 'SLACK_APP_TOKEN_PSYCHE=xapp-YOUR-PSYCHE-APP-TOKEN' >> ~/.openclaw/.env
  echo 'SLACK_BOT_TOKEN_PSYCHE=xoxb-YOUR-PSYCHE-BOT-TOKEN' >> ~/.openclaw/.env
  chmod 600 ~/.openclaw/.env
  ```
- [ ] **3.3** Update OpenClaw Slack channel configuration on Mac mini:
  - Edit `~/.openclaw/openclaw.json` (or the Slack skill config file)
  - Set the Slack channel config to use the `@psyche` tokens
  - Set `defaultChannel` to `psyche-ops`
  - Set capabilities as listed in Pass 3
- [ ] **3.4** Restart OpenClaw gateway on Mac mini:
  ```bash
  launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.openclaw-gateway.plist
  launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.openclaw-gateway.plist
  ```
- [ ] **3.5** Verify `@psyche` connects to Slack:
  ```bash
  # Check gateway logs for Socket Mode connection
  tail -20 /tmp/syncrescendence-openclaw-gateway.log
  # Expected: Slack Socket Mode connected, listening on channels
  ```
- [ ] **3.6** Test: Send a message from `@psyche` to `#psyche-ops`:
  ```bash
  openclaw skill slack send --channel psyche-ops --message "Psyche online. CTO reporting for duty."
  ```
  Verify the message appears in Slack.

### Phase 4: Update `@ajna` Configuration on MBA (Sovereign/Ajna, ~5 minutes)

- [ ] **4.1** SSH into MBA (or work locally)
- [ ] **4.2** Update `@ajna` OpenClaw Slack config:
  - Change `defaultChannel` from `all-syncrescendence` to `ajna-strategic`
- [ ] **4.3** Invite `@ajna` to new channels:
  - Required channels: `#ajna-strategic`, `#sovereign-decisions`, `#all-syncrescendence`
  - In Slack, in each channel: `/invite @Ajna`
- [ ] **4.4** Restart OpenClaw gateway on MBA (if config changed):
  ```bash
  launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.openclaw-gateway.plist
  launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.openclaw-gateway.plist
  ```
- [ ] **4.5** Test: Send a message from `@ajna` to `#ajna-strategic`:
  ```bash
  openclaw skill slack send --channel ajna-strategic --message "Ajna online. Strategic channel established."
  ```

### Phase 5: Configure Linear Integration (Sovereign, ~10 minutes)

- [ ] **5.1** In Linear: Settings -> Integrations -> Slack
  - Click "Add to Slack"
  - Authorize the Syncrescendence workspace
- [ ] **5.2** Configure the integration:
  - Select channel: `#linear-updates`
  - Select project: SYN
  - Enable events: issue created, state changed, assignee changed, comment added
  - Enable Slack actions: create issue from Slack message
- [ ] **5.3** Test: In Linear, create issue "SYN-TEST: Slack integration test" -> verify it appears in `#linear-updates`
- [ ] **5.4** Test: In Slack `#linear-updates`, use `/linear create Test from Slack` -> verify issue created in Linear
- [ ] **5.5** Delete test issues after verification

### Phase 6: Configure ClickUp Integration (Sovereign, ~10 minutes)

- [ ] **6.1** In ClickUp: Integrations -> Slack
  - Click "Add to Slack"
  - Authorize the Syncrescendence workspace
- [ ] **6.2** Configure:
  - Map relevant ClickUp spaces to `#commander-execution`
  - Enable events: task created, status changed, assignee changed
  - Enable Slack actions: create task from message
- [ ] **6.3** Test: Create task in ClickUp -> verify notification in `#commander-execution`

### Phase 7: Configure GitHub Integration (Sovereign, ~10 minutes)

- [ ] **7.1** Install GitHub Slack app (https://slack.github.com/)
  - Authorize the Syncrescendence workspace
- [ ] **7.2** In `#github-events` channel, run:
  ```
  /github subscribe owner/syncrescendence
  /github subscribe owner/syncrescendence workflows:{event:"pull_request" branch:"main"}
  ```
- [ ] **7.3** Configure filters (turn off noisy events):
  ```
  /github unsubscribe owner/syncrescendence issues comments
  ```
- [ ] **7.4** Test: Push a trivial commit to the repo -> verify event appears in `#github-events`

### Phase 8: Configure Make Scenarios for Cross-Post (Sovereign/Psyche, ~30 minutes)

- [ ] **8.1** Log into Make (https://make.com)
- [ ] **8.2** Create Scenario B-1: Slack -> Discord
  - Trigger: Slack "Watch for New Messages" in bridged channels
  - Filter: exclude bot messages and `[via Discord]` prefixed messages
  - Router: map channels per Pass 5 table
  - Action: Discord webhook per target channel
  - Test with a manual Slack message, verify it appears in Discord
- [ ] **8.3** Create Scenario B-2: Discord -> Slack
  - Trigger: Discord "Watch for New Messages" in bridged channels
  - Filter: exclude bot messages and `[via Slack]` prefixed messages
  - Router: map channels per Pass 5 table
  - Action: Slack "Send Message" to mapped channel
  - Test with a manual Discord message, verify it appears in Slack
- [ ] **8.4** Activate both scenarios
- [ ] **8.5** End-to-end loop prevention test:
  - Post message in `#all-syncrescendence` (Slack)
  - Verify it appears in Discord `#general` with `[via Slack]` prefix
  - Verify it does NOT echo back to Slack
  - Post message in Discord `#general`
  - Verify it appears in `#all-syncrescendence` with `[via Discord]` prefix
  - Verify it does NOT echo back to Discord

### Phase 9: Service Alert Configuration (Psyche, ~20 minutes)

- [ ] **9.1** On Mac mini, create a health check script that posts to `#alerts`:
  ```bash
  # ~/.syncrescendence/scripts/slack_health_check.sh
  # Checks all services, posts failures to #alerts via @psyche
  ```
- [ ] **9.2** Create a launchd plist to run the health check every 5 minutes:
  ```
  com.syncrescendence.slack-health-check.plist
  StartInterval: 300
  ```
- [ ] **9.3** Bootstrap the plist:
  ```bash
  launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.syncrescendence.slack-health-check.plist
  ```
- [ ] **9.4** Test: Stop a service (e.g., Qdrant) -> verify alert appears in `#alerts` within 5 minutes

### Phase 10: Verification Checklist

Run all of the following. Every one must pass.

- [ ] **V-01**: `@ajna` can post to `#ajna-strategic`, `#all-syncrescendence`, and `#sovereign-decisions`
- [ ] **V-02**: `@psyche` can post to `#psyche-ops`, `#alerts`, `#commander-execution`, `#adjudicator-qa`, `#cartographer-intelligence`
- [ ] **V-03**: Both bots respond to DMs
- [ ] **V-04**: Linear issue state change appears in `#linear-updates`
- [ ] **V-05**: ClickUp task change appears in `#commander-execution`
- [ ] **V-06**: GitHub push event appears in `#github-events`
- [ ] **V-07**: Slack -> Discord cross-post works for all 5 bridged channels
- [ ] **V-08**: Discord -> Slack cross-post works for the 4 bidirectional channels
- [ ] **V-09**: Cross-post loop prevention confirmed (no echo cascades)
- [ ] **V-10**: Service health alert appears in `#alerts` when a service is stopped
- [ ] **V-11**: Sovereign notification levels configured (URGENT channels override DND)
- [ ] **V-12**: All 10 channels visible in Slack workspace

### Implementation Priority Sequence

Execute phases in this order. Each phase is independently valuable; you can stop after any phase and have a working (partial) system.

```
Phase 1 (Channels)           <- Can stop here: organized workspace
    |
Phase 2 (Create @psyche app) <- Can stop here: dual-bot ready
    |
Phase 3 (@psyche on Mac mini) + Phase 4 (@ajna update)  <- Can stop here: dual-bot operational
    |
Phase 5 (Linear)             <- Can stop here: P0 integration live
    |
Phase 6 (ClickUp)            <- Can stop here: P1 integration live
    |
Phase 7 (GitHub)             <- Can stop here: dev events visible
    |
Phase 8 (Cross-post bridge)  <- Can stop here: Slack-Discord bridge live
    |
Phase 9 (Service alerts)     <- Can stop here: infrastructure monitoring live
    |
Phase 10 (Verification)      <- COMPLETE: all systems verified
```

**Estimated total time**: ~2 hours (Sovereign time: ~1 hour for Phases 1-2, 5-8; Psyche time: ~30 minutes for Phases 3-4, 9; Verification: ~15 minutes).

---

## Cross-References

| Document | Path | Relevance |
|----------|------|-----------|
| SaaS Integration Architecture | `/Users/system/Desktop/syncrescendence/02-ENGINE/REF-SAAS_INTEGRATION_ARCHITECTURE.md` | Sections IV.B (Linear-Slack), IV.C (ClickUp-Slack), V.B (cross-post), XI (Slack playbook) |
| MCP Bridge Architecture | `/Users/system/Desktop/syncrescendence/00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-2026-02-07-mcp-bridge-architecture.md` | Slack MCP server audit, bot token auth |
| Psyche Machine Elucidation | `/Users/system/Desktop/syncrescendence/00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-2026-02-08-psyche-machine-elucidation.md` | DEC-PSYCHE-007 (twin coordination via Slack) |
| Constellation Modus Operandi | `/Users/system/Desktop/syncrescendence/00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-2026-02-08-constellation-modus-operandi.md` | 4-agent always-on architecture, agent relay pattern |
| MBA Ajna Setup | `/Users/system/Desktop/syncrescendence/00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-2026-02-09-mba-ajna-setup.md` | MBA OpenClaw config, @ajna existing setup |
| Twin Coordination Protocol | `/Users/system/Desktop/syncrescendence/00-ORCHESTRATION/state/DYN-TWIN_COORDINATION_PROTOCOL.md` | Slack as primary inter-twin channel |
| Stack Teleology | `/Users/system/Desktop/syncrescendence/02-ENGINE/REF-STACK_TELEOLOGY.md` | Slack disposition and teleological assignment |

---

**End of Clarescence**

*This document is READY FOR EXECUTION. All 10 phases can be executed incrementally. Phase 1 (channel creation) and Phase 2 (Slack app creation) require Sovereign action in the Slack admin interface. Phases 3-4 require OpenClaw config updates on both machines. Phases 5-9 are integration configuration. Phase 10 is verification.*
