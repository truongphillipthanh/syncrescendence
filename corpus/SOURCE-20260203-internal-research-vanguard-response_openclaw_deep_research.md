# OpenClaw Best Practices Audit

Audit security and config (P0). Ensure gateway is bound to localhost only (gateway.bind: "loopback") and use the built-in gateway token; lock down channels with allowlists/pairing[1][2]. Use openclaw pairing or Slack/iMessage DM allowlists so only authorized users can trigger the agent[2]. Inspect and pin all plugins/skills before enabling (treat npm-based plugins as untrusted code)[3]. Set workspace file permissions (e.g. ~/.openclaw/openclaw.json to 600) and firewall to block unwanted ports[4][5]. Verify that the gateway isn't exposed on 0.0.0.0; use VPN/Tailscale for any remote access[6][7]. Run openclaw security audit to catch misconfigurations and require human approval for risky actions[7].

Enable sandboxing and tool limits (P0). OpenClaw strongly recommends running tools in Docker sandboxes and strict allowlists when processing untrusted content[8][9]. In practice, set agents.defaults.sandbox.mode="all" with workspaceAccess: "ro" for agents that run tools, and deny dangerous tools (exec, browser, process, etc.) to non-owner agents[9][8]. For example:

```json
{
  "agents": {
    "defaults": {
      "sandbox": { "mode": "all", "workspaceAccess": "ro" },
      "tools": {
        "exec": { "enabled": false }, 
        "browser": { "enabled": false },
        "web_search": { "enabled": false }
      }
    }
  }
}
```

This isolates file ops and limits prompt injection risks[8]. Use the latest instruction-tuned models (e.g. Claude Opus 4.5, GPT-5.2) for any agent with tool access; weaker models (Sonnet, Haiku) should only see trusted input or run in locked-down mode[10][2].

Close missing gaps (P1). We lack a web search API and sandbox. Obtain a Brave Search API key and add it to config (see Section 5). For isolation, consider running the gateway in a Docker container or VM (the DigitalOcean 1‑Click deploy uses container isolation and hardened firewall[11]). Audit and remove any unnecessary or suspicious ClawdHub skills – the community has reported "hundreds of malicious skills" in the registry (e.g. the "ClawHavoc" campaign)[12][13]. Update all skills/plugins to exact versions (no *) and run static scans. Disable auto-updates of skills and periodically run openclaw security audit[14][7]. Apply prompt-guard measures: require confirmation for any tool execution, and log all actions.

Quick wins (immediate) (P0):

- Enable access controls: enforce pairing/allowlist for DMs and mention-trigger in groups[2].
- Lock config: file permissions, gateway auth token, minimal mDNS mode, no open ports[15][16].
- Install Brave key: follow Brave setup below and configure web_search (Section 5).
- Skill vetting: remove any skill that asks you to paste shell commands or installs packages. Audit existing ones for external prerequisites[13].
- Set sandbox default: add agents.defaults.sandbox as above and test critical skills in isolation.
- Pin plugin versions: use explicit @version in extensions.allowlist and review their code[3].

30-day improvements (P1–P2):

- Infrastructure: Move to a managed or containerized deployment (e.g. Ubuntu VM with Docker) to gain OS-level isolation[11]. Use tools like Tailscale instead of LAN bind to access remotely[6][7].
- Multi-agent config: Formalize separate agent identities for each role (see Section 2). Maintain per-agent config directories and memory.
- Memory & logging: Upgrade from raw text logs to structured DB or vector memory; ensure logs are on append-only storage and rotated.
- Skill governance: Establish a policy (see Section 3) including periodic audits, least-privilege checks, and an approval process for new skills[13][7].
- Model usage policy: Track token consumption per agent/model; adjust prompts to be concise. Use fallbacks and throttling (see next section).

What we're doing right: We run 24/7 on a static Mac mini (avoiding sleep issues[17]), use persistent file memory (OpenClaw "remembering" conversations[18]), and have multiple agents/skills set up for different tasks. We also have watcher scripts and a Slack protocol for coordination, which aligns with the multi-agent architecture (each role has its own workspace)[19].

Missing: Key security practices (sandboxing, allowlists, auth) and Brave API for search. We also need a disciplined skill governance process; the recent "ClawHavoc" incident shows how dangerous unvetted skills can be[13][20].

# Multi-Model Collaboration Architecture

Define agent roles and model fallbacks (P0). In openclaw.json, declare separate agents or default models for Ajna vs Psyche. For example, use the Models CLI config to set primary/fallback chains[21]:

```json
{
  "agents": {
    "defaults": {
      "model": {
        "primary": "anthropic/claude-opus-4-5",
        "fallbacks": ["openai/gpt-5.2", "anthropic/claude-dolphin-3.5"]
      },
      "models": {
        "anthropic/claude-opus-4-5": { "alias": "Ajna" },
        "openai/gpt-5.2": { "alias": "Psyche" },
        "anthropic/claude-dolphin-3.5": { "alias": "DeepSeek" }
      }
    }
  }
}
```

This ensures Ajna (Opus) is used by default and GPT-5.2 is an approved model[21]. We can also create a distinct agent entry for Psyche in agents.list if needed, binding it to Slack iMessage channels[19].

sessions_spawn vs direct execution (P0–P1). Use sessions_spawn for parallelizable sub-tasks and concurrency[22]. For example, Ajna can spawn Psyche (GPT-5.2) and Sonnet (Claude Sonnet 4.5) in parallel to handle different subtasks of a user query. sessions_spawn runs the sub-agent asynchronously, returning {status:"accepted",runId} and later announcing the result back[22]. This is ideal for background research or analysis. By contrast, use direct execution (normal chat) for quick answers or to keep the conversation thread intact. Direct calls are simpler but block until response; use them for low-cost queries or follow-ups. Remember: spawned sub-agents cannot themselves spawn further sub-sessions[23], so design tasks hierarchically.

Routing by complexity/cost (P1). Establish rules so heavy tasks go to high-capacity models and light tasks to cheap ones. For instance:

- Complex reasoning or final synthesis: Let Ajna (Opus 4.5 or GPT-5.2) handle these.
- Holistic execution tasks: Use Psyche (GPT-5.2) for end-to-end work (code writing, deep analysis).
- Data lookup / web research: Spawn a Gemini-based model or Claude for fast search integration (Gemini if Google provider is available). If using Brave web_search, Ajna or Psyche can fetch facts from the API.
- Bulk processing / preparation: Offload to Sonnet/Haiku/DeepSeek (cheaper models) for summarization, list-making, or multi-item tasks. These models may be more error-prone, so wrap them in sandbox and verify outputs.

For example, an incoming request might cause Ajna to do: sessions_spawn({ task: "...", model: "openai/gpt-5.2" }) for one subtask and another sessions_spawn with "anthropic/claude-sonnet-4-5" for another. The Orchestrator then collects results and synthesizes. This "divide and conquer" saves tokens: cheap models handle grunt work, and costly models only run once on refined input.

"Council" multi-perspective pattern (P1). To converge different views, have Ajna pose the same problem to multiple "advisors" (sub-agents) and aggregate their answers. For example, /sessions_send can implement a multi-agent dialogue[24]. Ajna might /sessions_send Psyche: "What do you think?" and likewise send tasks to other agents. OpenClaw injects message context and supports a ping-pong reply loop between agents[24]. Alternatively, spawn separate sessions (one per advisor) and then have Ajna read each transcript or wait for each announce. At the end, Ajna (or a final GPT/Claude) synthesizes consensus or picks the best parts. This simulates a "council" of AI: each sub-agent offers its answer, and the lead agent merges them.

Token-optimization strategy (P1). With a $160 budget, minimize expensive calls. Use Sonnet/Haiku for low-stakes drafts, reserve Opus/GPT-5.2 for final outputs. Turn on stream: false to get entire answers at once (reduces overhead of repeated calls). Use the OpenAI/Claude cutoff parameters to limit output length where possible. Also use fallback – if GPT-5.2 hits rate limits, let Ajna fall back to Claude (and vice versa) without losing context[21]. Finally, exploit OpenAI's plus plan free compute: offload as much as possible to ChatGPT-5.2 since its $20 flat fee covers unlimited chat (effectively "no marginal tokens" for now). Claude Max ($100) should be used for specialized tasks that GPT-5.2 cannot or for better tool-safety (since Claude Opus is good at resisting prompt hacks[25]).

# Skill Strategy

Prioritize key categories. Focus on skills that support our workflows. Likely top categories include: Productivity/Collaboration (Slack/iMessage integration, Notion/Reminders, scheduling tools); DevOps/Developer (GitHub, shell/exec, log readers, code search); Research/Data (web_search, browser, Wikipedia, DB query tools); Automation/IO (email, calendar, file system management); Analysis/Creative (summarizers, text analyzers, document converters). The DigitalOcean article notes OpenClaw's many integrations – e.g. GitHub, Notion, browser, calendar, Spotify, etc.[26][27] – so pick the 20–30 most relevant skills in these areas. Also consider Parallel/Coordination skills (e.g. the existing "council" or "parallel-research" patterns) to streamline multi-agent flows.

Use and extend ClawdHub. The ClawdHub registry (GitHub repo) has 1,700+ skills, but quality varies. Start with well-known, bundled skills (the Quickstart notes ~50 built-in skills: weather, GitHub, Slack, etc.[27]). Search ClawdHub by keyword (e.g. clawdhub search summarize) and read each SKILL.md. If a needed integration is missing (e.g. a custom CI/CD pipeline or niche API), build a custom skill. Create each custom skill by writing the SKILL.md prompt and tooling as code; test it thoroughly in a sandboxed environment. For syncrescendence-specific workflows, custom skills might include "TwinCoord" (parallel Slack workflows), "MemoryRouter" (automated file-based logging), or "ModelSwitcher" (skill to manage sessions_spawn calls). Any custom skill should follow a standard template (description, arguments, outputs) and include example uses.

Skill security audit (P0–P1). Treat third-party skills as potential malware. Before installing:

- Review code: Clone the skill repo and inspect SKILL.md for suspicious instructions (e.g. npm install or curl | bash)[28]. Check if it references external scripts or asks to paste shell commands – these are red flags.
- Run in sandbox: Install unknown skills first in an isolated environment (or with tools.subagents.tools limited)[13]. Observe network calls.
- Least-privilege: Only enable a skill's tools if needed. For example, if a skill only reads Gmail, don't give it browser or exec. Use allowlists in AGENTS.md to limit which agents can use which skills.
- Disable auto-updates: Ensure skills/ are not overwritten silently. Periodically re-run openclaw security audit to catch tampering[14].
- Allowlist sources: Prefer skills from trusted authors or the OpenClaw official repo. The JFrog security guide warns that "OpenClaw's third-party extensions are largely unvetted" and recommends only using reviewed extensions[20].

Skill governance policy (P1–P2). Formalize a process: require sign-off before any new skill is added. Maintain a private registry or metadata list of approved skills and their versions. For each approved skill, record its purpose, author, review date, and any required runtime dependencies. Enforce least privilege by default: new skills get no tool permissions until explicitly granted. Regularly rotate API keys and tokens that skills use. Lock down the Gateway (e.g. tools.subagents.tools and tools.exec.host="sandbox") as recommended in the security docs[13][7]. Monitor network traffic for skills (e.g. via a firewall or syslog) to detect exfiltration. If a skill requires installation of an external executable (brew, pip, etc.), review that binary carefully – the ClawHavoc case showed attackers sneaking malware via install instructions[29]. Finally, train the team: everyone must understand the risks of an AI supply-chain[13].

# Conversational AI Pattern

Session and agent setup. There are two main technical approaches: (a) use one multi-model agent and switch models via /model or sessions_spawn, or (b) configure multiple agents (each with a fixed model) and use sessions_send between them[19]. For a council-like dialogue, (b) is cleaner: define separate agent IDs (e.g. "ajna", "psyche", "gemini", "deepseek") in agents.list with appropriate agentDir and channel bindings[19]. This isolates their workspaces and memory. Then Ajna (Claude) can send messages to Psyche (GPT-5.2) or others.

Example workflow. Suppose the user asks Ajna a complex question. Ajna (Opus 4.5) orchestrates by spawning tasks:

- Psyche (GPT-5.2) as executor: Ajna does sessions_spawn with model: "openai/gpt-5.2" to draft an answer or perform reasoning.
- Gemini (search): If external information is needed, Ajna asks a Gemini-style agent via web search (OpenClaw's web_search using Brave), or spawns an agent with a Google model to fetch facts.
- DeepSeek (bulk): For large-scale data crunching (e.g. scanning logs or generating multiple variations), Ajna spawns a sub-agent using a small model (like Claude Dolphin or Sonnet) in sandbox to handle it.

As each sub-agent finishes, OpenClaw posts their results back: Ajna receives statuses and outputs (via the announce step)[23]. Ajna then synthesizes a final answer by combining these inputs.

Coordination mechanics. Use sessions_spawn for one-way delegation (non-blocking parallel calls)[22], and sessions_send for two-way dialogues between agents[24]. For example, Ajna might /sessions_send a clarifying question to Psyche and wait, leveraging the built-in ping-pong (reply-back) logic[24]. If multiple rounds of back-and-forth are needed among agents, sessions_send handles it automatically, up to a configurable limit of turns. Otherwise, use separate spawns for single-turn queries to each agent.

Failure modes. Be aware of known issues: e.g. a bug reported by Herbert Yang indicates that using agentId in sessions_spawn can silently ignore the model override, defaulting to the calling agent's model. In practice, avoid combining agentId and model parameters, or spawn without specifying agentId (letting it default) and then assign the model. Also watch for timeouts (runTimeoutSeconds) if a subtask hangs. If a sub-agent throws an error, Ajna will see a "Status: error" reply. Log and inspect these. Overuse of sessions_send can lead to deep loops or extra token use; limit agent-to-agent turns (agent.wait or agentToAgent.maxPingPongTurns). Finally, ensure each agent's context is isolated properly: without sandbox, one agent could in theory read another's workspace. Use separate agentDir or enable sandbox to enforce isolation[19][30].

Cost-awareness. Each model call uses tokens. To stay under budget: consolidate contexts (don't spawn redundant agents on similar tasks), cap output lengths, and use cheaper models wherever acceptable[10]. Track token usage (Ajna's announce lines include token counts). Prioritize using our paid models' flat fees: GPT-5.2 (ChatGPT+) first, then Claude Max, then fall back to Claude Pro or lower tiers only if needed. If budget becomes tight, temporarily disable the most expensive agent (e.g. turn off GPT-5.2 spawn) or reduce tokens in prompts.

# Brave Search API Setup

Get a Brave API key: Create an account at Brave Search API. In the dashboard select the "Data for Search" plan (the free tier) and generate a subscription token[31]. Copy this API key.

Configure OpenClaw: Add the key to your OpenClaw config (or environment). For example, in openclaw.json add:

```json
{
  "tools": {
    "web": {
      "search": {
        "provider": "brave",
        "apiKey": "YOUR_BRAVE_KEY_HERE",
        "maxResults": 5,
        "timeoutSeconds": 30
      }
    }
  }
}
```

This tells OpenClaw to use Brave Search for web_search[32]. You can also set BRAVE_API_KEY as an env var instead of in the file.

Cost implications: Brave Search offers 2,000 free queries/month[33]. Beyond that, the Base AI plan charges $5 per 1,000 requests[34] (up to 20M queries). In practice, typical RAG usage (a few searches per task) will stay within the free tier. If you hit the limit, the extra cost (e.g. $5–$10 for 1–2k extra queries) is small relative to $160.

Note Brave's AI policy: Officially Brave's terms discourage "AI inference", but OpenClaw's docs endorse Brave as the default search provider for agents[31]. Use it judiciously. As a fallback, you might enable other search tools (e.g. a custom browser plugin or alternative API) if Brave becomes restricted.

## References

[1] [2] [3] [4] [5] [6] [8] [9] [10] [15] [16] [25] [30] Security - OpenClaw
https://docs.openclaw.ai/gateway/security

[7] [20] OpenClaw can be Hazardous to your Software Supply Chain
https://jfrog.com/blog/giving-openclaw-the-keys-to-your-kingdom-read-this-first/

[11] [17] OpenClaw Is Here. Now What? A Practical Guide for the Post-Hype Moment | by Toni Maxx | Feb, 2026 | Medium
https://medium.com/@tonimaxx/openclaw-is-here-now-what-a-practical-guide-for-the-post-hype-moment-8baa9aa00157

[12] [13] [14] [28] [29] Hundreds of Malicious Skills Found in OpenClaw's ClawHub | eSecurity Planet
https://www.esecurityplanet.com/threats/hundreds-of-malicious-skills-found-in-openclaws-clawhub/

[18] [26] What is OpenClaw? Your Open-Source AI Assistant for 2026 | DigitalOcean
https://www.digitalocean.com/resources/articles/what-is-openclaw

[19] Multi-Agent Routing - OpenClaw
https://docs.openclaw.ai/concepts/multi-agent

[21] Models CLI - OpenClaw
https://docs.openclaw.ai/concepts/models

[22] [23] [24] Session Tools - OpenClaw
https://docs.openclaw.ai/concepts/session-tool

[27] Moltbot Quickstart Guide | DigitalOcean
https://www.digitalocean.com/community/tutorials/moltbot-quickstart-guide

[31] [32] Brave Search - OpenClaw
https://docs.openclaw.ai/brave-search

[33] [34] Brave Search API | Brave
https://brave.com/search/api/
