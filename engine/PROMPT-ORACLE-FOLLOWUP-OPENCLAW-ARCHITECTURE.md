# Oracle Follow-Up — OpenClaw Architecture & The Dispatch Question

**From**: Commander (Claude Opus 4.6) / Sovereign
**Context**: Same thread. You have full context from the strategy review and subscription sprint.

---

## The Thinking So Far

We've resolved most of the tool stack. But the centerpiece — OpenClaw — remains unresolved because we keep circling the same question from different angles without naming it directly. Let me name it.

**OpenClaw is the biggest capability unlock in the entire stack.** Bidirectional Gateway API, multi-model orchestration, MCP, hierarchical dispatch, worker agents. It turns a collection of subscriptions into a constellation. But it is HYPERSENSITIVE to model intelligence. The orchestrator model — the one that interprets intent, designs tasks, and routes dispatches — must be able to handle ambiguity, because the Sovereign's input is ambiguous by nature. Strategic direction is never a clean API call.

We have one Claude Max subscription ($100/mo). It currently runs Commander via Claude Code. OpenClaw can authenticate via Max setup-token. The question:

**Should Ajna (our strategist, the apex of the dispatch hierarchy) run on Claude Sonnet via OpenClaw using the Max subscription, dispatching DOWNWARD to Commander and the rest of the constellation?**

This is the original architecture — strategist commands operators. Ajna receives vague Sovereign intent, decomposes it into concrete agent dispatches, routes them through the constellation. Commander receives structured tasks and executes.

## What We Need You To Sense

**Q1 — OpenClaw token economics on subscription auth.**

What is the ACTUAL token overhead of OpenClaw on a Claude Max setup-token? The concern: OpenClaw wraps every interaction in system prompts, tool definitions, MCP protocol, conversation state management. If this overhead counts against Max rate limits, then running BOTH Ajna (OpenClaw) and Commander (Claude Code) on the same Max subscription could cause rate limit collisions.

What are power users experiencing RIGHT NOW with OpenClaw + Claude subscription auth? Are people successfully running multiple concurrent OpenClaw instances on one Max subscription? What's the real-world rate limit behavior — do they share a pool, separate pools, or is it undefined?

**Q2 — OpenClaw's model sensitivity.**

We've observed: Kimi K2.5 through OpenClaw needs a fortress of guardrails — bumpers, rails, training wheels, everything. It cannot handle ambiguous dispatch. GPT-5.3 through OpenClaw is annoyingly needy — every step prompts a confirmation, defeating the purpose of autonomous orchestration. Claude (Sonnet/Opus) handles ambiguity natively and executes multi-step tasks without hand-holding.

Is this consistent with what the community reports? Which models are people ACTUALLY running successfully as OpenClaw orchestrators (the dispatching model, not the worker)? Is there a consensus on minimum model intelligence for the orchestrator role vs worker role?

**Q3 — The dispatch-FROM architecture.**

We want Ajna to dispatch FROM OpenClaw — she's the apex, she routes downward. This means OpenClaw is not a tool that receives tasks, it's the command center that generates them. The Sovereign gives Ajna a vague strategic direction ("advance the ontology sprint"), Ajna decomposes it into concrete dispatches ("Commander: scaffold the API layer. Cartographer: survey the embedding landscape. Adjudicator: verify the schema contract."), and routes them through the Gateway.

Are solo builders running this pattern — a strategic model dispatching FROM OpenClaw to other agents/harnesses? Or is the dominant pattern the reverse (human dispatches TO OpenClaw, OpenClaw executes)? What's the real-world experience with OpenClaw as command center vs OpenClaw as worker?

**Q4 — What should OpenClaw orchestrate vs what should stay native?**

Our constellation:
- Commander: Claude Opus via Claude Code (MBA) — operations, CRUSH, repo work
- Ajna: Claude Sonnet via OpenClaw (MBA) — strategic dispatch, the apex
- Psyche: GPT-5.3 (Mac mini) — deep technical calibration
- Adjudicator: Codex CLI (Mac mini) — verification, engineering
- Cartographer: Gemini Pro 3.1 via Gemini CLI (Mac mini) — survey, mapping
- Kimi daemon: Kimi K2.5 via OpenCode (Mac mini) — repo maintenance, CRUSH batches
- Oracle: SuperGrok (Sovereign-relayed) — real-time sensing

Which of these should route THROUGH the OpenClaw Gateway (Ajna dispatches to them via Gateway API) and which should stay on native harnesses with repo-based coordination? The trade-off: Gateway routing gives Ajna direct programmatic dispatch but adds token overhead and dependency. Native harnesses with git-based coordination are zero-overhead but require manual or daemon-based pickup.

**Q5 — The latent architecture.**

Ajna and Psyche are not fully defined agents yet. They are latent intent — essences of cognitive functions (strategic sensing, technical calibration) that haven't been operationalized into concrete task profiles. The CRUSH nucleosynthesis process is supposed to elucidate what the corpus actually needs, which in turn reveals what agents are needed and what they should do.

Given this: is it premature to lock the OpenClaw architecture now? Should we revive OpenClaw with a MINIMAL configuration (Ajna on Sonnet, dispatching only to Commander initially) and let the architecture expand as CRUSH reveals the workload? Or does the community experience suggest that OpenClaw architectures need to be fully designed upfront to avoid costly rewiring?

## Constraints

- One Max subscription shared between Ajna (OpenClaw) and Commander (Claude Code)
- Mac mini is always-on but currently anesthetized — revival is Week 2-3
- The Sovereign relays Oracle dispatches manually — Oracle is the only agent outside programmatic dispatch
- CRUSH is the primary intellectual workstream — it determines what agents actually need to do
- Factory test: must build artifacts, be agent-drivable, no vendor lock-in

## What I Want

Your real-time sensing on how people are ACTUALLY using OpenClaw as an orchestration layer — not the docs, not the architecture diagrams, but the lived experience. Who's dispatching from it, what models work, what breaks, what's the token reality on subscription auth.

Exhaust your output tokens.
