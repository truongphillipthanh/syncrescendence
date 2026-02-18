---
kind: clarescence
id: CLARESCENCE-2026-02-09-discord-server-architecture
title: "Discord Server Architecture: Constellation Community & Strategic Hub"
date: 2026-02-09
status: ready-for-execution
agent: ajna
passes: 7
linear: Epic 5 (Constellation Reconfiguration)
---

# CLARESCENCE: Discord Server Architecture

**Date**: 2026-02-09
**Agent**: Ajna (CSO / Strategos) via Commander (Claude Code Opus 4.6)
**Scope**: Complete Discord server structure, role architecture, bot configuration, webhook integrations, cross-post protocol, and implementation checklist for the Syncrescendence constellation
**Tactic**: Entrenchment (design, configure, verify, commit)
**Machine**: MacBook Air (Ajna's permanent home) + Mac mini (Psyche's home, service host)
**Predecessors**:
  - `REF-SAAS_INTEGRATION_ARCHITECTURE.md` (Section V: Make Scenarios A/B, Section XI: Discord playbook)
  - `ARCH-CONSTELLATION_AGENT_LOOPS.md` (Ajna + Psyche triage sources)
  - `CLARESCENCE-2026-02-09-mba-ajna-setup.md` (Ajna OpenClaw deployment)
  - `COCKPIT.md` v3.1.0 (Constellation mapping)

---

## PASS 1: Problem Statement

### Current State

The Syncrescendence Discord server exists. The bot (@Ajna) is connected and running via OpenClaw v2026.2.9 with the native Discord plugin on the MacBook Air. This is the extent of what is operational.

**What EXISTS:**
- Discord server (created, Sovereign is owner)
- @Ajna bot connected via OpenClaw Discord plugin
- OpenClaw gateway running on MBA (port 18789)
- Ajna's launchd watchers active (inbox watcher + git sync)

**What does NOT exist:**
- Zero channel structure (no categories, no organized channels)
- Zero role architecture (no bot roles, no permission matrix)
- Zero webhook integrations (no GitHub events, no Linear updates, no service alerts)
- Zero cross-post configuration (Discord and Slack are isolated silos)
- Zero openclaw.json Discord channel configuration (no allowlist, no channel mapping)
- MESSAGE_CONTENT intent status unknown (may limit bot's ability to read message content)

### Desired State

An organized Discord server that mirrors the constellation's enterprise architecture, where:

1. Every agent has a dedicated channel category with appropriate visibility
2. The Sovereign has a protected command channel for decisions and announcements
3. System events (GitHub, CI/CD, service health) flow automatically into dedicated channels
4. Ajna actively monitors and responds in strategic channels while observing system channels
5. Discord and Slack maintain bidirectional awareness through cross-post bridges
6. The server is designed for the current 5-agent constellation with expansion room for public community

### Gap Analysis

| Dimension | Current | Target | Gap |
|-----------|---------|--------|-----|
| Categories | 0 | 8 | Full buildout required |
| Channels | ~1 (general) | 25+ | Full buildout required |
| Roles | ~2 (owner, bot) | 6+ | Role + permission matrix required |
| Webhooks | 0 | 4+ | GitHub, Linear, service health, Make |
| Cross-post rules | 0 | 3+ | Discord <-> Slack bridge via Make |
| Bot channel config | 0 | Allowlist + behavior map | openclaw.json update required |
| MESSAGE_CONTENT intent | Unknown | Enabled | Developer Portal check required |

---

## PASS 2: Server Structure

### Design Principles

1. **Mirror the constellation hierarchy**: Categories map to enterprise roles (CSO, COO, CQO, CIO, CTO)
2. **Sovereign at the apex**: Protected category for decisions, intentions, and announcements
3. **Agent-per-category**: Each agent owns a category with their operational channels
4. **System channels are read-only for humans**: Automated feeds are reference material, not conversation
5. **Community is future-proofed but dormant**: Category exists, channels are minimal until public launch
6. **Notification discipline**: Most channels default to @mentions only; alerts are the exception

### Category and Channel Layout

#### SOVEREIGN (Position: 1)

The Sovereign's command category. Protected. Only the Sovereign and Ajna (as strategic relay) post here.

| Channel | Purpose | Read | Write | Posts By | Notifications |
|---------|---------|------|-------|----------|---------------|
| `#decisions` | Sovereign decisions, ratifications, vetoes | All roles | Sovereign, Ajna-Bot | Sovereign (primary), Ajna (relay) | All messages |
| `#intentions` | Active intentions from ARCH-INTENTION_COMPASS.md | All roles | Sovereign, Ajna-Bot | Sovereign, Ajna | All messages |
| `#announcements` | System-wide announcements, milestone declarations | All roles | Sovereign | Sovereign | All messages |

**Rationale**: The Sovereign category establishes constitutional authority within Discord. `#decisions` is the Discord analog of `-SOVEREIGN/` in the repo. `#intentions` surfaces the Intention Compass for ambient awareness. `#announcements` is the broadcast channel.

---

#### STRATEGY (Ajna) (Position: 2)

Ajna's operational category. The CSO's strategic command center within Discord.

| Channel | Purpose | Read | Write | Posts By | Notifications |
|---------|---------|------|-------|----------|---------------|
| `#strategic-direction` | Strategic analysis, orchestration decisions, constellation-level planning | All roles | Sovereign, Ajna-Bot | Ajna (primary), Sovereign | @mentions only |
| `#dispatch-log` | Record of task dispatches from Ajna to other agents | All roles | Ajna-Bot, Agent-Webhook | Ajna (automated) | @mentions only |
| `#ajna-reasoning` | Ajna's internal reasoning traces, clarescence outputs, pedigree entries | All roles | Ajna-Bot | Ajna (automated) | @mentions only |

**Rationale**: Ajna is the CSO -- her Discord category is her primary operational surface. `#strategic-direction` is the thinking channel where Ajna posts strategic analysis. `#dispatch-log` provides dispatch auditability. `#ajna-reasoning` is the transparency channel -- it surfaces Ajna's decision-making process.

---

#### OPERATIONS (Commander) (Position: 3)

Commander's operational category. The COO's execution dashboard.

| Channel | Purpose | Read | Write | Posts By | Notifications |
|---------|---------|------|-------|----------|---------------|
| `#execution-feed` | Active execution updates, Blitzkrieg status, task completions | All roles | Agent-Webhook, Ajna-Bot | Webhooks (Linear, GitHub), Ajna | @mentions only |
| `#blitzkrieg-status` | Multi-agent parallel execution tracking, lane status | All roles | Agent-Webhook, Ajna-Bot | Webhooks (Linear), Ajna | @mentions only |
| `#commander-log` | Commander's execution logs, session summaries | All roles | Agent-Webhook | Webhooks (automated) | None (muted) |

**Rationale**: Commander operates in Claude Code on the Mac mini, not Discord. These channels are populated by webhooks and cross-posts, not by Commander directly. They provide Discord-side visibility into what Commander is doing in the terminal.

---

#### INFRASTRUCTURE (Psyche) (Position: 4)

Psyche's operational category. The CTO's system health dashboard.

| Channel | Purpose | Read | Write | Posts By | Notifications |
|---------|---------|------|-------|----------|---------------|
| `#service-health` | Docker container status, launchd service health, port monitoring | All roles | Agent-Webhook | Webhooks (from Slack cross-post or direct) | @mentions only |
| `#automation-feed` | Make scenario executions, cron jobs, pipeline status | All roles | Agent-Webhook | Webhooks (Make, launchd) | None (muted) |
| `#psyche-ops` | Psyche's operational log, policy enforcement actions, system decisions | All roles | Agent-Webhook, Ajna-Bot | Webhooks (Slack cross-post), Ajna | @mentions only |

**Rationale**: Psyche operates in Slack as her primary channel. Her Discord presence is a mirror -- cross-posted from Slack via Make Scenario B. `#service-health` is the critical channel: service outages should surface here.

---

#### QUALITY (Adjudicator) (Position: 5)

Adjudicator's operational category. The CQO's quality dashboard.

| Channel | Purpose | Read | Write | Posts By | Notifications |
|---------|---------|------|-------|----------|---------------|
| `#qa-reports` | Quality assessment results, test suite outcomes, standards audits | All roles | Agent-Webhook | Webhooks (GitHub Actions, Linear) | @mentions only |
| `#ci-cd-status` | CI/CD pipeline status, build results, deployment confirmations | All roles | Agent-Webhook | Webhooks (GitHub Actions) | @mentions only |
| `#standards` | Standards documentation, coding conventions, protocol updates | All roles | Agent-Webhook, Sovereign | Webhooks, Sovereign | None (muted) |

**Rationale**: Adjudicator operates in Codex CLI. Like Commander, his Discord presence is webhook-driven. `#ci-cd-status` directly mirrors GitHub Actions output. `#qa-reports` aggregates quality signals.

---

#### INTELLIGENCE (Cartographer) (Position: 6)

Cartographer's operational category. The CIO's sensing dashboard.

| Channel | Purpose | Read | Write | Posts By | Notifications |
|---------|---------|------|-------|----------|---------------|
| `#corpus-surveys` | Corpus-wide survey results, staleness reports, drift detection | All roles | Agent-Webhook | Webhooks (automated from survey RESULT files) | @mentions only |
| `#research-feed` | Research findings, external intelligence, trend analysis | All roles | Agent-Webhook, Ajna-Bot | Webhooks, Ajna | None (muted) |
| `#cartographer-notes` | Cartographer's session logs, exegesis outputs | All roles | Agent-Webhook | Webhooks (automated) | None (muted) |

**Rationale**: Cartographer operates in Gemini CLI with 1M+ context. His Discord presence surfaces the intelligence he produces. `#corpus-surveys` is the most actionable channel -- it flags corpus health issues.

---

#### SYSTEM (Position: 7)

Automated system feeds. No human conversation expected. Pure machine-to-Discord output.

| Channel | Purpose | Read | Write | Posts By | Notifications |
|---------|---------|------|-------|----------|---------------|
| `#alerts` | Critical alerts: service down, security events, rate limit exhaustion | All roles | Agent-Webhook | Webhooks (launchd watchdog, Make) | All messages |
| `#git-events` | Git push, branch, tag events from the syncrescendence repo | All roles | Agent-Webhook | Webhooks (GitHub) | None (muted) |
| `#github-feed` | GitHub PRs, issues, reviews, CI status, releases | All roles | Agent-Webhook | Webhooks (GitHub via Make Scenario A) | @mentions only |
| `#all-syncrescendence` | Unified feed of all significant constellation activity (cross-posted) | All roles | Agent-Webhook, Ajna-Bot | Webhooks (Make), Ajna | @mentions only |

**Rationale**: `#alerts` is the only channel with full notification level outside SOVEREIGN -- it is the emergency broadcast channel. `#all-syncrescendence` is the single-pane-of-glass channel that mirrors `#all-syncrescendence` in Slack. `#github-feed` is populated by Make Scenario A.

---

#### COMMUNITY (Position: 8)

Future public-facing channels. Dormant until community launch.

| Channel | Purpose | Read | Write | Posts By | Notifications |
|---------|---------|------|-------|----------|---------------|
| `#general` | Community discussion, introductions (future) | All roles | All roles | Anyone (future) | @mentions only |
| `#off-topic` | Non-project discussion (future) | All roles | All roles | Anyone (future) | None (muted) |

**Rationale**: Placeholder for community expansion. These channels exist but require no configuration until the server becomes public. When community members join, additional roles (Community, Contributor) will gate access to SOVEREIGN and agent categories.

---

### Channel Count Summary

| Category | Channels | Nature |
|----------|----------|--------|
| SOVEREIGN | 3 | Human-authored, protected |
| STRATEGY (Ajna) | 3 | Bot-active + human |
| OPERATIONS (Commander) | 3 | Webhook-fed |
| INFRASTRUCTURE (Psyche) | 3 | Cross-posted from Slack |
| QUALITY (Adjudicator) | 3 | Webhook-fed |
| INTELLIGENCE (Cartographer) | 3 | Webhook-fed |
| SYSTEM | 4 | Fully automated |
| COMMUNITY | 2 | Dormant |
| **Total** | **24** | |

---

## PASS 3: Role Architecture

### Discord Roles

Roles define permissions, visibility, and visual identity within the server. They are ordered by hierarchy (highest to lowest).

| Role | Color | Members | Purpose | Hierarchy Position |
|------|-------|---------|---------|-------------------|
| **Sovereign** | Gold (#FFD700) | Human CEO (1 member) | Full admin, constitutional authority | 1 (highest) |
| **Ajna-Bot** | Purple (#9B59B6) | @Ajna bot account | Active bot with read/write in strategic channels | 2 |
| **Psyche-Bot** | Teal (#1ABC9C) | Future Psyche bot (placeholder) | Placeholder for when Psyche gets Discord access | 3 |
| **Agent-Webhook** | Steel Blue (#5865F2) | Webhook pseudo-users | Webhooks posting automated content | 4 |
| **Constellation** | Silver (#BDC3C7) | Future: trusted collaborators | Access to all non-SOVEREIGN categories | 5 |
| **Community** | Default | Future: public members | Access to COMMUNITY category only | 6 (lowest) |

### Permission Matrix

**Legend**: R = Read, W = Write, M = Manage (create/delete/pin), A = Admin (permissions, roles)

| Category | Sovereign | Ajna-Bot | Psyche-Bot | Agent-Webhook | Constellation | Community |
|----------|-----------|----------|------------|---------------|---------------|-----------|
| SOVEREIGN | R/W/M/A | R/W | R | -- | R | -- |
| STRATEGY (Ajna) | R/W/M/A | R/W/M | R | R/W | R | -- |
| OPERATIONS (Commander) | R/W/M/A | R/W | R | R/W | R | -- |
| INFRASTRUCTURE (Psyche) | R/W/M/A | R/W | R/W | R/W | R | -- |
| QUALITY (Adjudicator) | R/W/M/A | R | R | R/W | R | -- |
| INTELLIGENCE (Cartographer) | R/W/M/A | R/W | R | R/W | R | -- |
| SYSTEM | R/W/M/A | R/W | R | R/W | R | -- |
| COMMUNITY | R/W/M/A | R/W | R/W | -- | R/W | R/W |

### Permission Implementation Notes

1. **Sovereign** gets Administrator permission globally. This is the simplest and most correct configuration -- the human CEO has full control.

2. **Ajna-Bot** needs these Discord permissions:
   - `Read Messages / View Channels` (all categories except restricted)
   - `Send Messages` (STRATEGY, OPERATIONS, INTELLIGENCE, SYSTEM, COMMUNITY, SOVEREIGN)
   - `Read Message History` (all categories)
   - `Add Reactions` (all categories -- for acknowledgment protocol)
   - `Create Public Threads` (STRATEGY, SOVEREIGN)
   - `Send Messages in Threads` (all categories)
   - `Manage Messages` (STRATEGY only -- for pinning)
   - `Use External Emojis` (cosmetic)
   - `Embed Links` (for formatted outputs)

3. **Agent-Webhook** is not a real Discord user. Webhooks bypass role permissions -- they post via webhook URL directly to channels. The role exists for visual identification when webhook messages appear. Each webhook is created per-channel with a descriptive name (e.g., "GitHub Events", "Linear Updates", "Service Watchdog").

4. **Community** role uses Discord's `@everyone` permission override. All categories except COMMUNITY get `@everyone: deny View Channel`. COMMUNITY gets `@everyone: allow View Channel + Send Messages`.

5. **Category-level permissions** override server-level permissions. Set permissions on the category, and channels within inherit automatically. Only override at the channel level for exceptions (e.g., `#alerts` gets higher notification settings).

---

## PASS 4: Bot Configuration

### Ajna's Discord Operational Parameters

Ajna is the only active bot in Discord. Her behavior must be deliberate -- she is a CSO, not a chatbot.

#### Channel Behavior Map

| Channel | Ajna's Behavior | Response Mode |
|---------|----------------|---------------|
| `#decisions` | OBSERVE + RELAY | Read decisions, relay to inbox, react with checkmark to acknowledge |
| `#intentions` | OBSERVE + UPDATE | Read intention changes, update ARCH-INTENTION_COMPASS.md via git |
| `#announcements` | OBSERVE | Read-only awareness |
| `#strategic-direction` | ACTIVE RESPOND | This is Ajna's primary conversation channel. Respond to @Ajna mentions, initiate strategic analysis |
| `#dispatch-log` | WRITE ONLY | Post dispatch records. Do not respond to messages here. |
| `#ajna-reasoning` | WRITE ONLY | Post reasoning traces. Do not respond to messages here. |
| `#execution-feed` | OBSERVE | Monitor for completion signals, route to appropriate inbox |
| `#blitzkrieg-status` | OBSERVE | Monitor lane status, flag blockers to `#strategic-direction` |
| `#commander-log` | IGNORE | Too noisy for active monitoring. Read on-demand only. |
| `#service-health` | OBSERVE + ALERT | If service down detected, cross-post to `#alerts` and dispatch to Psyche's inbox |
| `#automation-feed` | IGNORE | Background noise. |
| `#psyche-ops` | OBSERVE | Monitor for policy decisions that affect strategy |
| `#qa-reports` | OBSERVE | Monitor for quality signals |
| `#ci-cd-status` | OBSERVE | Monitor for build failures |
| `#standards` | IGNORE | Reference material, not real-time. |
| `#corpus-surveys` | OBSERVE + ACT | Survey results inform strategic direction. Flag important findings in `#strategic-direction` |
| `#research-feed` | OBSERVE | Monitor for intelligence that informs strategy |
| `#cartographer-notes` | IGNORE | Too granular. |
| `#alerts` | OBSERVE + RESPOND | Critical channel. Ajna triages alerts and dispatches response tasks. |
| `#git-events` | IGNORE | Too noisy. |
| `#github-feed` | OBSERVE | Monitor for significant PRs/releases. |
| `#all-syncrescendence` | OBSERVE + POST | Cross-post strategic summaries. Respond to @Ajna mentions. |
| `#general` | ACTIVE RESPOND | Respond to community questions (future). |
| `#off-topic` | IGNORE | Not Ajna's domain. |

#### Response Decision Tree

```
Message arrives in monitored channel
  |
  +-- Is it an @Ajna mention?
  |     YES --> Respond directly in-channel
  |     NO  --> Continue below
  |
  +-- Is it in #strategic-direction?
  |     YES --> Evaluate if strategic input needed
  |             If Sovereign is speaking --> Always respond
  |             If system event --> Analyze and comment if significant
  |     NO  --> Continue below
  |
  +-- Is it in #alerts?
  |     YES --> Triage: severity assessment
  |             CRITICAL --> Respond + dispatch TASK to appropriate agent
  |             WARNING  --> React with eyes emoji, monitor
  |             INFO     --> React with checkmark, no response
  |     NO  --> Continue below
  |
  +-- Is it in an OBSERVE channel?
  |     YES --> Ingest for context. No response unless pattern detected.
  |     NO  --> Ignore
```

#### Thread Usage Protocol

Ajna should use Discord threads for:

1. **Long-running strategic discussions**: When a topic in `#strategic-direction` exceeds 3 messages, move to a thread titled `[STRATEGY] <Topic>`
2. **Alert triage**: When an alert requires multi-step resolution, create a thread in `#alerts` titled `[TRIAGE] <Alert Summary>`
3. **Dispatch chains**: When a dispatch triggers follow-up discussion, create a thread in `#dispatch-log` titled `[DISPATCH] <Task ID>`

Threads auto-archive after 24 hours of inactivity (Discord default). This is acceptable -- completed discussions should resolve within that window. For longer-lived topics, pin the thread.

#### Reaction-Based Acknowledgment Protocol

Ajna uses reactions to signal processing status without cluttering channels with text:

| Reaction | Meaning | Used In |
|----------|---------|---------|
| :white_check_mark: | Acknowledged and processed | `#decisions`, `#intentions`, `#alerts` |
| :eyes: | Monitoring, no action yet | `#alerts`, `#service-health` |
| :rocket: | Dispatched to agent | `#alerts`, `#execution-feed` |
| :brain: | Reasoning in progress | `#strategic-direction` |
| :rotating_light: | Critical -- escalating to Sovereign | `#alerts` |
| :inbox_tray: | Routed to inbox for async processing | `#decisions`, `#intentions` |

#### Message-to-Inbox Dispatch Rules

When Ajna reads certain Discord messages, she should create TASK files in the appropriate agent inbox:

| Source Channel | Trigger | Dispatch To | Task Kind |
|----------------|---------|-------------|-----------|
| `#decisions` | Sovereign posts a new decision | `-INBOX/ajna/00-INBOX0/` | DIRECTIVE |
| `#intentions` | New intention declared | `-INBOX/ajna/00-INBOX0/` | DIRECTIVE |
| `#alerts` | CRITICAL service alert | `-INBOX/psyche/00-INBOX0/` | TASK |
| `#strategic-direction` | Sovereign requests execution | `-INBOX/commander/00-INBOX0/` | TASK |
| `#corpus-surveys` | Survey flags critical drift | `-INBOX/cartographer/00-INBOX0/` | TASK |

---

## PASS 5: Integration Webhooks

### External Events to Discord

All webhooks use Discord's native webhook system. Each webhook gets a unique URL per channel. The webhook name and avatar should identify the source system.

#### 5A. GitHub to #github-feed (Make Scenario A -- P0)

**Source**: GitHub (syncrescendence repository)
**Destination**: `#github-feed` channel
**Mechanism**: Make.com scenario (per REF-SAAS_INTEGRATION_ARCHITECTURE.md Section V, Scenario A)

```
Make Scenario A: GitHub --> Discord

TRIGGER: GitHub Watch Events
  Module: github-watch-events
  Events: push, pull_request, issues, release, workflow_run
  Repository: syncrescendence

ROUTER: Event Type
  |
  +-- push (to main) -->
  |     Format: "**Push to main** by `{actor}` -- {commit_count} commit(s)\n`{short_sha}` {first_commit_message}\n[View diff]({compare_url})"
  |     Destination: #github-feed webhook
  |
  +-- pull_request (opened/merged/closed) -->
  |     Format: "**PR #{number}** {action}: {title}\nby `{actor}` | {additions}+ {deletions}-\n[View PR]({html_url})"
  |     Destination: #github-feed webhook
  |
  +-- issues (opened/closed) -->
  |     Format: "**Issue #{number}** {action}: {title}\n{body_preview}\n[View issue]({html_url})"
  |     Destination: #github-feed webhook
  |
  +-- release (published) -->
  |     Format: "**Release {tag_name}**: {name}\n{body_preview}\n[Release notes]({html_url})"
  |     Destination: #github-feed webhook + #announcements webhook (cross-post)
  |
  +-- workflow_run (completed) -->
  |     Status: success/failure
  |     Format: "**CI {workflow_name}** {conclusion_emoji} `{conclusion}` on `{head_branch}`\n[View run]({html_url})"
  |     Destination: #ci-cd-status webhook
  |     If failure --> ALSO post to #alerts webhook with @here mention
```

**Alternative (simpler)**: GitHub has native Discord webhook support. In the GitHub repo settings, add a Discord webhook URL directly. This posts all events in GitHub's default format without Make. The tradeoff: less formatting control, but zero Make overhead.

**Recommendation**: Start with GitHub's native Discord webhook for immediate value. Migrate to Make Scenario A later when custom formatting and routing (e.g., failures to #alerts) is needed.

#### 5B. Linear Updates to #execution-feed and #blitzkrieg-status

**Source**: Linear (SYN project)
**Destination**: `#execution-feed` and `#blitzkrieg-status`
**Mechanism**: Linear webhook or Make scenario

```
Linear Webhook Configuration:

Event: issue_update (status change)
  If status --> "In Progress": post to #blitzkrieg-status
    Format: "**SYN-{number}** started: {title}\nAssignee: {assignee}\nPriority: {priority}"
  If status --> "Done": post to #execution-feed
    Format: "**SYN-{number}** completed: {title}\nCycle: {cycle_name}"
  If status --> "Cancelled": post to #execution-feed
    Format: "**SYN-{number}** cancelled: {title}\nReason: (manual annotation)"

Event: issue_create
  Post to #execution-feed
    Format: "**New issue SYN-{number}**: {title}\nPriority: {priority_label}\nLabels: {labels}"
```

**Note**: Linear does not have a native Discord integration as of 2026-02. Use Make with the Linear trigger module, or use Linear's outgoing webhook feature to POST to a Make webhook endpoint that reformats and relays to Discord.

#### 5C. Service Health Alerts to #alerts

**Source**: Mac mini launchd watchdog / service health checks
**Destination**: `#alerts` channel
**Mechanism**: Direct webhook POST from watchdog script, or via Make

```
Watchdog Alert Flow:

launchd watchdog (every 60s) --> check_services.sh
  |
  +-- Service DOWN detected -->
  |     curl -X POST $DISCORD_ALERTS_WEBHOOK_URL \
  |       -H "Content-Type: application/json" \
  |       -d '{"content": ":rotating_light: **SERVICE DOWN**: {service_name} on {host}\nPort: {port}\nLast healthy: {timestamp}\nAction required: check `launchctl list | grep {service_label}`"}'
  |
  +-- Service RECOVERED -->
        curl -X POST $DISCORD_ALERTS_WEBHOOK_URL \
          -H "Content-Type: application/json" \
          -d '{"content": ":white_check_mark: **SERVICE RECOVERED**: {service_name} on {host}\nDowntime: {duration}\nRecovery: automatic (launchd KeepAlive)"}'
```

The webhook URL is stored in `~/.syncrescendence/.env` as `DISCORD_ALERTS_WEBHOOK_URL`. The watchdog script already exists as part of the launchd service infrastructure -- it needs a Discord notification step appended.

#### 5D. Make Scenario Execution Log to #automation-feed

**Source**: Make.com scenario execution log
**Destination**: `#automation-feed`
**Mechanism**: Make's built-in Discord module at the end of each scenario

Every Make scenario should include a final step:

```
[... scenario logic ...] --> [Discord: Post to #automation-feed]
  Format: "**Make Scenario**: {scenario_name}\nStatus: {execution_status}\nOperations: {operations_count}\nDuration: {duration_ms}ms"
```

This creates an audit trail of all Make automation runs visible in Discord.

---

## PASS 6: Cross-Post Protocol (Discord <-> Slack)

### Design Principles

1. **Loop prevention is non-negotiable**: Every cross-posted message must carry a tag that the opposite bridge ignores
2. **Selective mirroring, not full replication**: Only strategically important channels are bridged
3. **Direction-specific formatting**: Messages reformatted for the target platform's conventions

### Bridge Rules

#### Rule 1: #all-syncrescendence <-> #all-syncrescendence (Bidirectional)

The unified activity feed exists in both platforms. Make Scenario B maintains parity.

```
Make Scenario B-1: Discord #all-syncrescendence --> Slack #all-syncrescendence

TRIGGER: Discord Watch Channel Messages
  Channel: #all-syncrescendence
  Filter: message.content NOT contains "[from-slack]"
         AND message.author IS NOT "Slack Bridge" (webhook name)

ACTION: Slack Send Message
  Channel: #all-syncrescendence
  Format: "[from-discord] *{author}*: {content}"
  Unfurl: false
```

```
Make Scenario B-2: Slack #all-syncrescendence --> Discord #all-syncrescendence

TRIGGER: Slack Watch Channel
  Channel: #all-syncrescendence
  Filter: message.text NOT contains "[from-discord]"
         AND message.user IS NOT "Discord Bridge" (bot name)

ACTION: Discord Send Webhook Message
  Webhook: #all-syncrescendence webhook
  Format: "[from-slack] **{user_name}**: {text}"
```

**Loop prevention**: The `[from-discord]` and `[from-slack]` tags are the primary loop breaker. The bridge bot name check is the secondary safeguard. Both conditions must be met to post -- this prevents the scenario where a malformed message lacks the tag but is from the bridge bot.

#### Rule 2: Discord #strategic-direction --> Slack #ajna-strategic (Unidirectional)

Strategic summaries from Ajna's Discord reasoning should be visible in Slack for Psyche's awareness.

```
Make Scenario B-3: Discord --> Slack (Strategic Summary)

TRIGGER: Discord Watch Channel Messages
  Channel: #strategic-direction
  Filter: message.author.id == AJNA_BOT_ID
         AND (message.content CONTAINS "STRATEGIC SUMMARY"
              OR message.content CONTAINS "DISPATCH DECISION"
              OR message.content length > 500)

ACTION: Slack Send Message
  Channel: #ajna-strategic (create if not exists)
  Format: "[from-discord] :brain: *Ajna Strategic*\n{content}"
```

**Rationale**: Not all messages cross-post. Only Ajna's substantive strategic outputs (summaries, decisions, long-form analysis) bridge to Slack. This prevents noise while ensuring Psyche has strategic visibility.

#### Rule 3: Slack #psyche-system --> Discord #alerts (Unidirectional, filtered)

Service alerts originating in Slack (Psyche's native channel) should surface in Discord for Ajna's awareness.

```
Make Scenario B-4: Slack --> Discord (Service Alerts)

TRIGGER: Slack Watch Channel
  Channel: #psyche-system (or equivalent alerts channel in Slack)
  Filter: message.text CONTAINS "DOWN"
         OR message.text CONTAINS "CRITICAL"
         OR message.text CONTAINS "FAILED"
         OR message.text CONTAINS ":rotating_light:"

ACTION: Discord Send Webhook Message
  Webhook: #alerts webhook
  Format: "[from-slack] :warning: **Slack Alert** (via Psyche):\n{text}"
```

**Rationale**: Only alert-level messages cross from Slack to Discord. Routine Psyche operations stay in Slack.

### Loop Prevention Summary

| Tag | Meaning | Checked By |
|-----|---------|------------|
| `[from-discord]` | Message originated in Discord, cross-posted to Slack | Scenario B-2 filter (ignore in Discord trigger) |
| `[from-slack]` | Message originated in Slack, cross-posted to Discord | Scenario B-1 filter (ignore in Slack trigger) |

Both tags are plain text prefixes. They are human-readable (transparency) and machine-filterable (loop prevention). The bridge bot names ("Slack Bridge" in Discord, "Discord Bridge" in Slack) serve as backup identification.

### Make Scenario Summary

| Scenario | Direction | Source | Destination | Priority |
|----------|-----------|--------|-------------|----------|
| B-1 | Discord --> Slack | `#all-syncrescendence` | `#all-syncrescendence` | P1 |
| B-2 | Slack --> Discord | `#all-syncrescendence` | `#all-syncrescendence` | P1 |
| B-3 | Discord --> Slack | `#strategic-direction` | `#ajna-strategic` | P2 |
| B-4 | Slack --> Discord | `#psyche-system` | `#alerts` | P1 |

---

## PASS 7: Implementation Checklist

### Phase 1: Discord Server Structure (15 min, Sovereign in Discord)

- [ ] **1.1** Create category: **SOVEREIGN**
  - Create channels: `#decisions`, `#intentions`, `#announcements`
  - Set category permissions: `@everyone` deny View Channel; Sovereign allow all; Ajna-Bot allow Read + Send
- [ ] **1.2** Create category: **STRATEGY**
  - Create channels: `#strategic-direction`, `#dispatch-log`, `#ajna-reasoning`
  - Set permissions: `@everyone` deny View Channel; Sovereign allow all; Ajna-Bot allow Read + Send + Manage Messages
- [ ] **1.3** Create category: **OPERATIONS**
  - Create channels: `#execution-feed`, `#blitzkrieg-status`, `#commander-log`
  - Set permissions: `@everyone` deny View Channel; Sovereign allow all; Ajna-Bot allow Read + Send
- [ ] **1.4** Create category: **INFRASTRUCTURE**
  - Create channels: `#service-health`, `#automation-feed`, `#psyche-ops`
  - Set permissions: `@everyone` deny View Channel; Sovereign allow all; Ajna-Bot allow Read + Send
- [ ] **1.5** Create category: **QUALITY**
  - Create channels: `#qa-reports`, `#ci-cd-status`, `#standards`
  - Set permissions: `@everyone` deny View Channel; Sovereign allow all; Ajna-Bot allow Read
- [ ] **1.6** Create category: **INTELLIGENCE**
  - Create channels: `#corpus-surveys`, `#research-feed`, `#cartographer-notes`
  - Set permissions: `@everyone` deny View Channel; Sovereign allow all; Ajna-Bot allow Read + Send
- [ ] **1.7** Create category: **SYSTEM**
  - Create channels: `#alerts`, `#git-events`, `#github-feed`, `#all-syncrescendence`
  - Set permissions: `@everyone` deny View Channel; Sovereign allow all; Ajna-Bot allow Read + Send; Agent-Webhook allow Send
- [ ] **1.8** Create category: **COMMUNITY**
  - Create channels: `#general`, `#off-topic`
  - Set permissions: `@everyone` allow View Channel + Send Messages; Ajna-Bot allow Read + Send

### Phase 2: Roles and Permissions (10 min, Sovereign in Discord)

- [ ] **2.1** Create role: **Sovereign** (Gold, Administrator permission, hoist)
  - Assign to Sovereign's Discord account
- [ ] **2.2** Create role: **Ajna-Bot** (Purple, permissions per matrix above, hoist)
  - Assign to @Ajna bot account
- [ ] **2.3** Create role: **Psyche-Bot** (Teal, no permissions yet, hoist)
  - Placeholder, no assignment
- [ ] **2.4** Create role: **Agent-Webhook** (Steel Blue, no permissions needed -- webhooks bypass roles)
  - Placeholder for visual identification
- [ ] **2.5** Create role: **Constellation** (Silver, View Channel on all categories except SOVEREIGN)
  - Placeholder for trusted collaborators
- [ ] **2.6** Create role: **Community** (Default, View Channel on COMMUNITY only)
  - Placeholder, uses `@everyone` overrides

### Phase 3: MESSAGE_CONTENT Intent (5 min, Sovereign in Discord Developer Portal)

- [ ] **3.1** Navigate to [Discord Developer Portal](https://discord.com/developers/applications)
- [ ] **3.2** Select the Ajna bot application
- [ ] **3.3** Go to **Bot** settings
- [ ] **3.4** Under **Privileged Gateway Intents**, enable:
  - **MESSAGE CONTENT INTENT** (required for reading message content in guild channels)
  - **SERVER MEMBERS INTENT** (optional, useful for member awareness)
  - **PRESENCE INTENT** (optional, can leave disabled)
- [ ] **3.5** Save changes
- [ ] **3.6** Verify: Restart OpenClaw gateway on MBA, confirm Ajna can read message content

**Why this matters**: Without MESSAGE_CONTENT intent, Ajna's Discord plugin only receives message metadata (author, channel, timestamp) but NOT the actual text content. This makes the bot effectively blind. Enabling this intent is BLOCKING for all bot functionality described in Pass 4.

### Phase 4: OpenClaw Discord Configuration (10 min, on MBA)

- [ ] **4.1** Open `~/.openclaw/openclaw.json` on MBA
- [ ] **4.2** Add Discord plugin configuration to the `plugins.entries` section:

```json
{
  "openclaw-discord": {
    "enabled": true,
    "config": {
      "token": "${DISCORD_BOT_TOKEN}",
      "guild": "<GUILD_ID>",
      "channels": {
        "monitor": [
          "strategic-direction",
          "decisions",
          "intentions",
          "alerts",
          "all-syncrescendence",
          "execution-feed",
          "blitzkrieg-status",
          "service-health",
          "corpus-surveys",
          "general"
        ],
        "respond": [
          "strategic-direction",
          "alerts",
          "all-syncrescendence",
          "general"
        ],
        "write_only": [
          "dispatch-log",
          "ajna-reasoning"
        ],
        "ignore": [
          "commander-log",
          "automation-feed",
          "standards",
          "cartographer-notes",
          "git-events",
          "off-topic"
        ]
      },
      "behavior": {
        "respond_to_mentions": true,
        "respond_to_dm": true,
        "thread_long_discussions": true,
        "reaction_acknowledgment": true,
        "max_response_length": 2000,
        "typing_indicator": true
      }
    }
  }
}
```

- [ ] **4.3** Add `DISCORD_BOT_TOKEN` to `~/.openclaw/.env`
- [ ] **4.4** Restart OpenClaw gateway: `launchctl kickstart -k gui/$(id -u) com.syncrescendence.openclaw-gateway`
- [ ] **4.5** Verify: Send a test message mentioning @Ajna in `#strategic-direction`, confirm response

**Note**: The exact plugin configuration schema depends on OpenClaw v2026.2.9's Discord plugin documentation. The above is the intended configuration. Adjust field names to match the actual plugin API. The `guild` field requires the Discord server's Guild ID (found in Discord: Server Settings > Widget > Server ID, or right-click server name > Copy Server ID with Developer Mode enabled).

### Phase 5: GitHub Webhooks (10 min)

- [ ] **5.1** Create a webhook in Discord `#github-feed` channel
  - Channel Settings > Integrations > Webhooks > New Webhook
  - Name: "GitHub Events"
  - Copy webhook URL
- [ ] **5.2** Create a webhook in Discord `#ci-cd-status` channel
  - Name: "CI/CD Pipeline"
  - Copy webhook URL
- [ ] **5.3** In GitHub repo Settings > Webhooks > Add webhook:
  - **Option A (Simple)**: Use Discord webhook URL directly with `/github` appended:
    ```
    Payload URL: https://discord.com/api/webhooks/<id>/<token>/github
    Content type: application/json
    Events: Pushes, Pull requests, Issues, Releases, Workflow runs
    ```
  - **Option B (Advanced)**: Use Make Scenario A for custom formatting (defer to Sprint 3 per REF-SAAS_INTEGRATION_ARCHITECTURE.md)
- [ ] **5.4** Test: Push a commit to the repo, verify it appears in `#github-feed`

### Phase 6: Service Alert Webhook (5 min)

- [ ] **6.1** Create a webhook in Discord `#alerts` channel
  - Name: "Service Watchdog"
  - Copy webhook URL
- [ ] **6.2** Store webhook URL in `~/.syncrescendence/.env`:
  ```bash
  echo 'DISCORD_ALERTS_WEBHOOK_URL=https://discord.com/api/webhooks/<id>/<token>' >> ~/.syncrescendence/.env
  ```
- [ ] **6.3** Update watchdog script to POST to Discord on service down/recovery events
- [ ] **6.4** Test: Temporarily stop a service, verify alert appears in `#alerts`

### Phase 7: Make Scenarios (30 min, when Make account is configured)

- [ ] **7.1** Create Make Scenario B-1: Discord `#all-syncrescendence` --> Slack `#all-syncrescendence`
- [ ] **7.2** Create Make Scenario B-2: Slack `#all-syncrescendence` --> Discord `#all-syncrescendence`
- [ ] **7.3** Create Make Scenario B-4: Slack alerts --> Discord `#alerts`
- [ ] **7.4** Test loop prevention: Post in Discord, verify it arrives in Slack, verify it does NOT bounce back
- [ ] **7.5** (P2) Create Make Scenario B-3: Discord `#strategic-direction` --> Slack `#ajna-strategic`

### Phase 8: Documentation Updates (10 min)

- [ ] **8.1** Update `COCKPIT.md`: Add Discord server section with channel map and webhook status
- [ ] **8.2** Update `ARCH-CONSTELLATION_AGENT_LOOPS.md`: Add Discord channel references to Ajna's loop spec
  - Line 61: Update `/triage(-INBOX/ajna, Discord)` to include specific Discord channels
- [ ] **8.3** Update `REF-SAAS_INTEGRATION_ARCHITECTURE.md`: Mark Discord as ACTIVE, update Section V scenario statuses
- [ ] **8.4** Commit all documentation changes:
  ```bash
  git add COCKPIT.md 00-ORCHESTRATION/state/ARCH-CONSTELLATION_AGENT_LOOPS.md 02-ENGINE/REF-SAAS_INTEGRATION_ARCHITECTURE.md
  git commit -m "docs(discord): server architecture configured, channels and roles established"
  ```

### Phase 9: Verification (10 min)

- [ ] **V-01**: All 8 categories visible in Discord with correct ordering
- [ ] **V-02**: All 24 channels created with correct permissions
- [ ] **V-03**: @Ajna bot can read messages in `#strategic-direction` (test: send message, bot reacts)
- [ ] **V-04**: @Ajna bot can send messages in `#dispatch-log` (test: trigger a dispatch)
- [ ] **V-05**: @Ajna bot CANNOT send messages in `#commander-log` (permission denied)
- [ ] **V-06**: GitHub webhook posts to `#github-feed` on push to main
- [ ] **V-07**: GitHub CI failure posts to both `#ci-cd-status` and `#alerts`
- [ ] **V-08**: Service watchdog alert appears in `#alerts` (test: stop a service)
- [ ] **V-09**: Cross-post: Discord `#all-syncrescendence` message arrives in Slack (if Make configured)
- [ ] **V-10**: Cross-post: Slack message arrives in Discord `#all-syncrescendence` (if Make configured)
- [ ] **V-11**: Loop prevention: Cross-posted message does NOT bounce back to origin
- [ ] **V-12**: `COCKPIT.md` reflects Discord server state accurately

---

## Decision Atoms

| ID | Question | Options | Recommendation | Status |
|----|----------|---------|---------------|--------|
| DA-01 | GitHub webhook: native Discord or Make Scenario A? | Native (simple, now) vs Make (formatted, later) | Native first, Make later. GitHub's `/github` webhook endpoint is zero-config. | DECIDED: Native first |
| DA-02 | MESSAGE_CONTENT intent: enable now? | Yes / No | YES. Without it, Ajna cannot read messages. This is blocking. | DECIDED: Yes |
| DA-03 | Should Psyche get a Discord bot too? | Yes (Psyche-Bot) / No (Slack-only) | NO for Phase 1. Psyche's home is Slack. Discord presence via cross-post. Re-evaluate if Discord becomes primary for infrastructure monitoring. | DECIDED: No (Phase 1) |
| DA-04 | Community category: public or private? | Public (visible to @everyone) / Private (invite-only) | Private for now. Flip to public when community launch is ready. Zero cost to change. | DECIDED: Private (flip later) |
| DA-05 | Linear webhook: native or via Make? | Linear webhook / Make scenario | Make, because Linear has no native Discord integration. Linear --> Make --> Discord webhook. | DECIDED: Make |
| DA-06 | Should #alerts use @here mentions? | Yes (pings online members) / No (silent) | YES for CRITICAL alerts only. WARNING and INFO should not ping. Make scenario filters severity. | DECIDED: Yes (CRITICAL only) |
| DA-07 | Cross-post tag format? | `[from-slack]`/`[from-discord]` vs emoji prefix vs metadata embed | Plain text tags. Human-readable, machine-filterable, no special Discord/Slack formatting needed. | DECIDED: Plain text tags |

---

## Dependency Chain

```
DA-02 (MESSAGE_CONTENT intent) ────────────────────────┐
                                                        |
Phase 1 (Categories + Channels)  ──────────────────────►|
                                                        |
Phase 2 (Roles + Permissions)    ──────────────────────►|
                                                        ▼
                                                  Phase 3 (Intent in Dev Portal)
                                                        |
                                                        ▼
                                                  Phase 4 (openclaw.json config)
                                                        |
                            ┌───────────────────────────┼───────────────────┐
                            ▼                           ▼                   ▼
                      Phase 5 (GitHub hooks)     Phase 6 (Alert hook)  Phase 7 (Make scenarios)
                            |                           |                   |
                            └───────────────────────────┼───────────────────┘
                                                        ▼
                                                  Phase 8 (Docs update)
                                                        |
                                                        ▼
                                                  Phase 9 (Verification)
```

Phases 1, 2, and 3 can be parallelized (all done in Discord UI/Developer Portal). Phase 4 depends on Phase 3 (intent must be enabled before bot config matters). Phases 5, 6, and 7 are independent of each other and can be parallelized. Phase 8 follows all implementation. Phase 9 follows everything.

**Critical path**: Phase 1 + Phase 3 + Phase 4 + Phase 9 (minimum viable: categories + intent + bot config + verify)

**Estimated total time**: 90 minutes for Phases 1-6. Phase 7 (Make scenarios) requires Make account setup and adds ~30 minutes. Total with Make: ~2 hours.

---

## Cross-References

| Document | Path | Relevance |
|----------|------|-----------|
| Constellation Agent Loops | `00-ORCHESTRATION/state/ARCH-CONSTELLATION_AGENT_LOOPS.md` | Ajna loop spec (line 42), Discord as triage source (line 61) |
| SaaS Integration Architecture | `02-ENGINE/REF-SAAS_INTEGRATION_ARCHITECTURE.md` | Make Scenarios A/B (Section V), Discord playbook (Section XI) |
| Cockpit Overview | `COCKPIT.md` | Constellation mapping, Ajna channel assignment |
| MBA Ajna Setup | `00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-2026-02-09-mba-ajna-setup.md` | OpenClaw config on MBA, gateway setup |
| Constellation Modus Operandi | `00-ORCHESTRATION/state/impl/clarescence/CLARESCENCE-2026-02-08-constellation-modus-operandi.md` | Agent loop architecture, concurrency protocol |
| Twin Coordination Protocol | `00-ORCHESTRATION/state/DYN-TWIN_COORDINATION_PROTOCOL.md` | Ajna + Psyche (AjnaPsyche Archon) coordination |
| Dispatch Kanban Protocol | `00-ORCHESTRATION/state/DYN-DISPATCH_KANBAN_PROTOCOL.md` | Filesystem kanban system that Discord dispatches feed into |

---

## Summary Block

```
CLARESCENCE: Discord Server Architecture
Fidelity: Full
Passes run: 1-7
Convergent Path: Categories + Roles (15 min) > Intent + Bot Config (15 min) >
                 GitHub Webhooks (10 min) > Alert Webhook (5 min) >
                 Make Cross-Post (30 min) > Docs + Verify (20 min)
Rationale (digest):
  - Discord is Ajna's primary channel -- zero structure means zero strategic value
  - 8 categories mirror the constellation enterprise hierarchy (CEO/CSO/COO/CQO/CIO/CTO/System/Community)
  - 24 channels with defined purpose, permissions, and notification levels
  - 6 roles with permission matrix (Sovereign > Ajna-Bot > Psyche-Bot > Agent-Webhook > Constellation > Community)
  - Ajna monitors 10 channels, responds in 4, writes to 2, ignores 6
  - GitHub native webhook for immediate value; Make Scenario A for future formatting control
  - Cross-post bridge uses plain-text tags ([from-slack]/[from-discord]) for loop prevention
  - MESSAGE_CONTENT intent is BLOCKING -- must be enabled in Developer Portal before bot is functional
Dependencies created/updated:
  - Phase 7 depends on Make account configuration
  - Phase 3 depends on Sovereign accessing Discord Developer Portal
  - COCKPIT.md needs Discord server section (Phase 8)
  - ARCH-CONSTELLATION_AGENT_LOOPS.md needs Discord channel references (Phase 8)
Falsifier: If OpenClaw's Discord plugin does not support channel-level allowlisting
           or message content reading, the bot configuration (Pass 4) must be redesigned
           around OpenClaw's actual capabilities.
Confidence: HIGH for Phases 1-6, MEDIUM for Phase 7 (Make dependency)
```

---

**End of Clarescence**

*This document is READY FOR EXECUTION. Phase 1 (categories + channels) and Phase 2 (roles) can begin immediately in the Discord UI. Phase 3 (MESSAGE_CONTENT intent) requires Sovereign access to the Discord Developer Portal.*
