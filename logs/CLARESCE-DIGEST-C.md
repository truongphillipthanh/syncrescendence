# CLARESCE-DIGEST-C: Feb 9 MBA/Ajna Setup + Discord Architecture
## Files: 2 | Lines: 1,920 | Date range: 2026-02-09

---

## KEY DECISIONS (named decision atoms, architectural choices)

- **Ajna-on-MBA as permanent home**: Ajna (CSO/Strategos) is locked to the MacBook Air. Mac mini is Psyche's domain. Not temporary — constitutionally assigned.
- **Kimi K2.5 via NVIDIA NIM**: Ajna's model is `nvidia/moonshotai/kimi-k2.5` (routing prefix form), with provider model ID `moonshotai/kimi-k2.5`. Two-level resolution: provider prefix in agent config, bare ID in provider block.
- **No Docker on MBA** (DA-03): MBA is a lightweight strategic node. Docker services (Neo4j, Graphiti, Qdrant) stay on Mac mini. Ajna uses file-based memorySearch instead of Mem0.
- **No Mem0 on MBA Phase 1** (DA-04): File-based memory only. Mem0 deferred to Phase 2 if Docker is ever added.
- **No Discord integration on Mac mini** (DA-05): Psyche handles Discord cross-posts from Slack. Ajna has the live Discord bot connection.
- **Same gateway token across machines** (DA-06): Both MBA and Mac mini use the same `${OPENCLAW_GATEWAY_TOKEN}`. Loopback-only, not internet-exposed.
- **Concurrent limits lowered for MBA** (DA-08): `maxConcurrent=2`, `subagents.maxConcurrent=4` (vs Mac mini's 4+8). MBA has less RAM/thermal headroom.
- **`prompt-guard` skill explicitly excluded**: Flagged for credential exfiltration — DO NOT INSTALL. This is a security finding, not just a feature gap.
- **Discord MESSAGE_CONTENT intent is BLOCKING** (discord DA-02): Without it, Ajna's bot receives only message metadata — zero text content. Must be enabled in Discord Developer Portal before any bot behavior is functional.
- **GitHub native webhook first, Make Scenario A later** (discord DA-01): GitHub's `/github` append to Discord webhook URL is zero-config. Custom formatting via Make is a Phase 2 concern.
- **Plain-text cross-post tags** (discord DA-07): `[from-slack]` / `[from-discord]` as loop-prevention markers. Human-readable and machine-filterable without special platform formatting.
- **Psyche stays Slack-only in Discord Phase 1** (discord DA-03): No Psyche-Bot for Discord. Her Discord presence is entirely cross-posted from Slack via Make Scenario B.
- **Community category private by default** (discord DA-04): Flip to public at community launch. Zero-cost change when ready.

---

## CORE CONCEPTS INTRODUCED

- **OpenClaw two-level model routing**: `provider/modelId` in agent config routes to provider; bare `modelId` in provider block is what the API receives. Critical distinction that caused the original deployment guide to fail.
- **launchd path absolutism**: `~` does not expand in plist XML. Every path must be a hardcoded absolute path. All MBA plists use the actual user home path (`/Users/system`). No variables, no tildes.
- **launchd EnvironmentVariables injection**: API keys and PATH must be inlined in plist `EnvironmentVariables` dict. launchd never sources `.zshrc`. This pattern reappears later as a documented constellation lesson.
- **`--` before `-INBOX` paths**: The leading dash in `-INBOX` is interpreted as a flag argument by shell utilities. All mkdir, ls, git add commands against `-INBOX` require `--` to signal end-of-options.
- **bun as OpenClaw's node manager**: Skills install via `npx skills add obra/lace@<skill> -g -y`, landing in `~/.agents/skills/`. The `install.nodeManager` key in openclaw.json must be set to `"bun"`.
- **Ajna's 7-phase loop**: ORIENT → SITUATE → CALIBRATE → TRIAGE → PROACTIVE → SOVEREIGN → REPEAT. The canonical boot sequence when services are operational.
- **Discord server as constellation mirror**: 8 categories map exactly to the enterprise hierarchy: SOVEREIGN, STRATEGY (Ajna), OPERATIONS (Commander), INFRASTRUCTURE (Psyche), QUALITY (Adjudicator), INTELLIGENCE (Cartographer), SYSTEM, COMMUNITY.
- **Reaction-based acknowledgment protocol**: Ajna uses emoji reactions (checkmark, eyes, rocket, brain, rotating_light, inbox_tray) as silent processing signals to avoid cluttering channels with text acknowledgments.
- **Channel behavior taxonomy**: Four operational modes for Discord channels — ACTIVE RESPOND, OBSERVE + ACT, WRITE ONLY, IGNORE. Each of Ajna's 24 channels has an explicit mode assignment.
- **Message-to-Inbox dispatch rules**: Specific Discord channels trigger TASK file creation in agent inboxes. `#decisions` → Ajna inbox (DIRECTIVE), `#alerts` CRITICAL → Psyche inbox (TASK), `#strategic-direction` Sovereign request → Commander inbox (TASK).
- **Make Scenario B cross-post bridge**: Four sub-scenarios (B-1 through B-4) handling bidirectional Discord/Slack sync. `#all-syncrescendence` is the unified activity feed on both platforms.
- **Falsifier discipline**: The discord clarescence names its own falsifier — if OpenClaw's Discord plugin doesn't support channel-level allowlisting or content reading, the entire bot config in Pass 4 must be redesigned.

---

## TENSIONS IDENTIFIED

- **NVIDIA API key exposure risk**: The key was potentially compromised by inclusion in a task file (flagged in Ajna's RESULT doc). Decision logged as DA-09: rotate within 24 hours of deployment. Status at time of clarescence: TODO/unresolved.
- **Gateway token in plist file**: API keys inlined in launchd plist have 644 permissions by default. Acknowledged as acceptable for loopback-only, user-scoped LaunchAgents; guidance to `chmod 600` if paranoid. Trade-off between operational simplicity and security hygiene.
- **fswatch vs polling**: watch_dispatch.sh has both event-driven (fswatch) and polling (10s) modes. The clarescence opts for fswatch primary with polling fallback. This tension later fully resolves in the 2026-02-17 deprecation of watch_dispatch.
- **Discord bot schema uncertainty**: The `openclaw-discord` plugin configuration in PASS 4 is described as "intended" — exact field names depend on OpenClaw v2026.2.9's actual Discord plugin API. This is the stated falsifier for the entire discord bot config section.
- **Make dependency for Linear webhooks**: Linear has no native Discord integration (as of 2026-02). Linear → Make → Discord is the only path, making Phase 7 (cross-posts + Linear) contingent on Make account setup.
- **Psyche as Slack-native agent on Discord**: Commander, Adjudicator, and Cartographer are entirely webhook-driven on Discord — they have no active bot presence. Only Ajna has a live bot. This means Discord is Ajna's platform in a way it isn't for any other agent.

---

## THEMES

- **Ajna as strategic surface**: Both documents reinforce that Discord is Ajna's primary real-time channel, and that her CSO function is specifically expressed through Discord (strategic direction, dispatch visibility, alert triage). The other four agents are present on Discord only through webhooks and cross-posts.
- **Lightweight vs heavyweight nodes**: A recurring design principle — MBA is intentionally stripped of Docker, Mem0, Discord management complexity. The Mac mini bears the service load. This asymmetry is by design and should be preserved.
- **Verification culture**: The MBA setup guide has 10 named verification checks (V-01 through V-10) with explicit PASS/FAIL criteria. The discord guide has 12 verification checkpoints (V-01 through V-12). Both clarescence documents model verification as a first-class output.
- **Launchd as the autonomy layer**: The three plists (openclaw-gateway, watch-ajna, git-sync) are the technical expression of "Ajna survives reboots without human intervention." The entire PASS 6 is essentially about making Ajna's presence unconditional on human action.
- **Cross-platform parity without full replication**: The Discord architecture is explicitly not a full mirror of Slack. It's selective: only strategically significant signals cross-post. The loop-prevention design enforces this discipline mechanically.

---

## PER-FILE HIGH-VALUE EXTRACTS

### mba-ajna-setup
- The **5 issues table** (lines 43-49) is a forensic record of what the previous deployment guide got wrong: model ID form, `~` in plists, OpenClaw binary path for Apple Silicon, skills install command format, `-INBOX` leading-dash flag parsing. Each is a class of error that recurs across the system.
- **DA-03** (no Docker on MBA) and **DA-04** (no Mem0 Phase 1) are foundational architectural decisions for MBA's role. Reversing either requires a deliberate re-clarescence.
- **`prompt-guard` security exclusion** (line 699): explicitly flagged as credential exfiltration risk. This is the only skill in the list with a security note rather than a functional reason for exclusion.
- The **rollback procedure** (PASS 10) covers complete teardown: plist bootout and removal, openclaw config backup + delete, skills removal, daemon infrastructure cleanup, log purge. Useful if MBA needs to be handed off or reinitialized.
- **Decision atom DA-09** (NVIDIA key rotation) is explicitly a TODO with a 24-hour deadline. Whether this was executed is not recorded in this document.
- The dependency chain diagram (lines 990-1013) shows all passes are strictly sequential — no parallelism is safe because each depends on the previous. This is the correct reading; the MBA cannot be partially configured.

### discord-server-architecture
- The **channel behavior map** (PASS 4, lines 275-299) is the highest-density artifact: 24 channels each with an explicit behavior mode (ACTIVE RESPOND / OBSERVE / WRITE ONLY / IGNORE). This is Ajna's operating charter for Discord.
- The **response decision tree** (lines 303-326) is a formal branching algorithm: @mention → respond; #strategic-direction → evaluate; #alerts → severity triage; OBSERVE channel → ingest silently. Encodes the difference between a chatbot and a CSO-in-Discord.
- **Loop prevention is a two-layer system**: primary (tag-based: `[from-discord]` / `[from-slack]`), secondary (bridge bot name check). Both must fail independently for a loop to occur.
- **24-channel architecture** across 8 categories: 3 human-authored protected channels (SOVEREIGN), 6 bot-active channels (Ajna's categories), 10 webhook-fed channels, 2 dormant community channels, and 3 channels that are Slack cross-post mirrors (Psyche's category).
- The **critical path** statement (line 815): Phase 1 (categories) + Phase 3 (MESSAGE_CONTENT intent) + Phase 4 (bot config) + Phase 9 (verify) is the minimum viable Discord setup. Everything else is instrumentation.
- The **Make Scenario B-3 filter** (lines 528-539) is precise: only Ajna's messages in #strategic-direction that contain "STRATEGIC SUMMARY", "DISPATCH DECISION", or exceed 500 characters cross-post to Slack. All other messages stay in Discord. This prevents Slack from becoming a noisy mirror.

---

## WHAT THIS BATCH CONTRIBUTES TO THE WHOLE

These two documents represent the operational instantiation of Ajna as a fully autonomous agent: the first establishes her technical substrate (model, services, persistence), and the second establishes her strategic interface (Discord as command surface). Together they define Ajna's dual presence — a launchd-managed headless processor on the MBA and a live Discord CSO operating across 24 organized channels. They also surface two durable lessons that later become canonical: launchd's rejection of `.zshrc` environment (encoded in MEMORY.md as a seared lesson) and the security risk of credential exposure in task files (DA-09 key rotation).
