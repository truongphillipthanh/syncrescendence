# Chat Bus Architecture v1

**Status**: proposed live design  
**Class**: architectural design memo  
**Authority chain**: constitution -> communications law -> runtime/channel surfaces -> promotion law

## Purpose

Define how Slack, Discord, and Telegram should be used inside the successor shell so they reduce coordination friction without becoming a second authority surface.

## Core Rule

Slack, Discord, and Telegram are **conversation and coordination surfaces**.

They are not:

- constitutional law
- the final decision ledger
- the durable archive of record
- the only place a strategic or technical decision survives

The shell should treat them as:

- dispatch bus
- receipt bus
- alert bus
- clarification bus
- edge/mobile ingress surfaces

while keeping:

- `repo` as authority
- `communications/` as durable lineage
- `executive/` and `program/` as federal steering
- `runtime/` as operational evidence
- `ontology` as typed registry/projection

## Teleology by Surface

### Slack

Slack is the best fit for the **federal work bus**.

Why:

- channels and threads are optimized for work coordination
- app workflows, webhooks, bots, slash commands, and events are mature
- search and message permalinks are strong enough for operational recall
- the product is natively oriented toward workspace-scale execution rather than loose social flow

Use Slack for:

- dispatch summaries that point to repo artifacts
- claims, receipts, confirms, and alerts
- office-local coordination and escalation
- runtime/service status and operational incident handling
- high-signal decision clarification before lawful promotion

Do not use Slack as:

- sole memory of what was decided
- final archive for architecture
- the only place a handoff exists

### Discord

Discord is the best fit for the **role/community/mesh bus**.

Why:

- category + channel + role architecture is excellent for persistent sub-worlds
- forum-style surfaces and threads support semi-structured discussion
- voice and presence afford richer ambient collaboration than Slack
- bot ergonomics are good for agentic or semi-agentic surfaces

Use Discord for:

- office-like subspaces with ambient context
- community or peer-coil style coordination
- longer-lived discussion around workstreams and ecosystems
- runtime interaction surfaces where live agents may participate
- social/exocortex adjacency that is too communal or fluid for Slack’s work grammar

Do not use Discord as:

- final legal memory
- the only place a strategic directive lives
- a dumping ground for unpromoted architectural thinking

### Telegram

Telegram is the best fit for **edge ingress, mobile relay, and broadcast/control at the edge**.

Why:

- bot model is simple and strong
- mobile reliability and ubiquity are high
- channels and groups are good for broadcast plus lightweight interaction
- it is well-suited to alerts, commands, intake, and mobile-first interaction

Use Telegram for:

- urgent alerts and lightweight control messages
- mobile ingress for the Sovereign
- edge-triggered notifications
- narrow command-style bot interactions
- broadcast surfaces where speed and reach matter more than deep threaded work

Do not use Telegram as:

- the main architecture workspace
- the primary place for long-form coordination
- the final archive for nuanced technical or strategic discussion

## Non-Duplication Rule

These surfaces should not all do the same job.

Recommended split:

- **Slack** = work bus
- **Discord** = mesh/community/role bus
- **Telegram** = edge/mobile/broadcast bus

This prevents platform sprawl while letting each surface do what it is naturally good at.

## Shell Mapping

### Slack maps to

- `communications/` summaries and dispatch notices
- `offices/` operational coordination
- `runtime/` alerts and status
- `program/` milestone / tranche visibility

### Discord maps to

- office-adjacent mesh spaces
- research and peer-coil discussion
- exocortex/community layers
- longer-lived, role-aware collaboration

### Telegram maps to

- urgent alerting
- mobile approval or awareness flows
- ingress notifications
- lightweight command-and-control surfaces

## Channel Taxonomy

### Slack

- `executive-intent`
- `dispatch-commander`
- `dispatch-adjudicator`
- `dispatch-ajna`
- `dispatch-cartographer`
- `dispatch-psyche`
- `receipts`
- `alerts`
- `runtime-status`
- `program-tranches`
- `research-intake`
- `compaction-review`

### Discord

- category: `executive`
- category: `offices`
- category: `runtime`
- category: `research`
- category: `community`
- category: `feedcraft`

Representative channels:

- `executive-briefings`
- `office-commander`
- `office-ajna`
- `office-psyche`
- `research-sensing`
- `runtime-observatory`
- `community-coils`
- `feedcraft-lab`

### Telegram

- `syncrescendence-alerts`
- `syncrescendence-mobile-ops`
- `syncrescendence-broadcast`

## Promotion Law

Every meaningful message or thread must end in one of four dispositions:

1. **discard**
   - ephemeral coordination
   - no durable consequence

2. **runtime event**
   - health/status/change signal
   - lands in `runtime/` or event ledger

3. **communications artifact**
   - prompt, response, handoff, briefing, assessment
   - lands in `communications/`

4. **doctrine/operator delta**
   - repeatable lesson
   - lands in `playbooks/`, `operators/`, `validated-patterns/`, or shell law

If a message changes:

- direction
- policy
- architecture
- routing
- playbook behavior
- operator behavior

it must leave chat and be promoted into the repo.

## Agent Interaction Model

Agents should not “live” in chat as their primary memory substrate.

They should use bounded actions:

- post dispatch
- claim task
- post receipt
- post result summary
- post confirm
- post alert
- post runtime status
- request clarification

That means the desired bridge surface is action-oriented, not conversationally unbounded.

## Suggested Bridge Operations

- `post_dispatch(surface, office, artifact_ref, summary)`
- `post_receipt(surface, task_ref, claimer, eta)`
- `post_result(surface, task_ref, result_ref, summary, verification)`
- `post_confirm(surface, result_ref, closure_state)`
- `post_alert(surface, severity, subject, artifact_ref)`
- `sync_thread_to_repo(surface, thread_id, disposition)`

## Anti-Patterns

- letting Slack or Discord become the durable memory of what happened
- using Telegram as the primary architecture workspace
- mirroring the same discussion into all three surfaces
- allowing platform-local discussion to outrun repo promotion
- treating chat history as canonical because it is convenient to search

## Comparative Advantages Summary

| Surface | Best role | Strength | Main risk |
|---|---|---|---|
| Slack | federal work bus | work-native coordination, workflows, search, structured status | hidden decision history if promotion is weak |
| Discord | mesh/community/role bus | persistent role spaces, ambient coordination, community energy | discussion sprawl becoming pseudo-canon |
| Telegram | edge/mobile/broadcast bus | mobile reach, alerting, lightweight control, ingress | oversimplifying nuanced work into chat commands |

## Recommended Successor-Shell Posture

Start with:

1. Slack as the primary operational bus
2. Discord as community and office-adjacent mesh
3. Telegram as mobile alert and ingress edge

Then bind all three through the same invariant:

`chat event -> disposition -> repo artifact / runtime event / promotion`

## Current Fit with Live Stack

This design is aligned with current reality:

- Slack and Discord are already healthy as OpenClaw runtime surfaces
- the shell already has receipts, result/confirm logic, and communications law
- what is missing is not concept but stricter promotion tooling and channel-specific bridge operators

## Current-World Recon Notes

Useful official references that support the above division of labor:

- Slack platform overview and app surfaces: [Slack Platform](https://api.slack.com/)
- Slack conversations/channels model: [Conversations API](https://api.slack.com/apis/conversations-api)
- Discord API and bot surface: [Discord Developer Portal Docs](https://discord.com/developers/docs/intro)
- Discord channel and thread model: [Discord Channel Resource](https://discord.com/developers/docs/resources/channel)
- Telegram bots and Mini Apps: [Telegram Bots API](https://core.telegram.org/bots/api), [Telegram Mini Apps](https://core.telegram.org/bots/webapps)
