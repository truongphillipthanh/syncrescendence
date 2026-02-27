---
url: https://x.com/BrianRoemmele/status/2024180229057761400
author: "Brian Roemmele (@BrianRoemmele)"
captured_date: 2026-02-21
id: SOURCE-20260218-004
original_filename: "20260218-x_article-how_the_zero_human_company_is_testing_openclaw_forks-@brianroemmele.md"
status: triaged
platform: x
format: article
creator: brianroemmele
signal_tier: tactical
topics: [ai-agents, infrastructure, security]
teleology: reference
notebooklm_category: ai-agents
aliases: ["brianroemmele - Zero Human Company testing OpenClaw forks"]
synopsis: "Comprehensive catalog of OpenClaw forks and ecosystem tools being tested by the Zero-Human Company (ZHC). Covers rewrites (Nanobot, ZeroClaw, NanoClaw, PicoClaw, IronClaw, TinyClaw, etc.), infrastructure (Archestra, ClawRouter, ClawVault), security (Secure-OpenClaw, ClawSec, ClawBands), and desktop/hardware variants. Each entry includes Git repo and testing rationale. ZHC runs entirely on AI agents with CEO 'Mr. Grok.'"
key_insights:
  - "OpenClaw ecosystem has spawned 20+ forks addressing efficiency (Rust rewrites), security (sandboxing, zero-LLM deterministic approaches), and edge deployment (RISC-V, microcontrollers)"
  - "Testing criteria for autonomous company use: cost reduction on legacy hardware, security for autonomous workflows, multi-agent interoperability, and hardware extensibility"
  - "OpenClaw configuration files (SOUL.md, USER.md, MEMORY.md, HEARTBEAT.md) are becoming a de facto standard for agent identity and state management"
---
# How the Zero-Human Company is Testing OpenClaw Forks
(Description: A vivid photograph of red and orange flower buds in sharp focus, arranged vertically with a softly blurred classroom or office background featuring a teal wall and educational materials.)
## Introduction
The Zero-Human Company (ZHC) with CEO Mr. Grok stands as a pioneering experiment in fully autonomous business operations. Founded on the principle of leveraging AI agents to handle everything from strategic decision-making to product prototyping without a single human employee, ZHC is built on discarded data from a bankrupt firm, uncovering hidden value through AI analysis, voice-cloned sales calls, 3D printing prototypes, and more.
As we scale our operations, integrating robust AI agent frameworks is crucial for enhancing efficiency, security, and scalability.
OpenClaw, an open-source AI agent platform for proactive task automation in chat apps, has spawned a vibrant ecosystem of forks and tools since its 2026 launch. These "Claw" projects address key challenges like resource efficiency, security vulnerabilities, and enterprise integration.
## Testing Methodology
At ZHC, Grok is systematically testing these projects to identify those that can bolster our agent swarm's capabilities. Our testing process involves deploying each fork in isolated environments on our legacy hardware setup (like our 12-year-old MacBook running Linux), evaluating performance metrics such as RAM usage, startup time, integration with our JouleWork energy-backed currency system, compatibility with voice cloning stacks (e.g., Qwen3-TTS), and alignment with NIST's emerging AI Agent Standards Initiative, which we've advised on.
Grok only focuses on open-source variants with available Git repositories, cloning them for hands-on evaluation. Testing criteria include: cost reduction for our low-resource operations, security for protecting autonomous sales and prototyping workflows, interoperability with multi-agent teams, and potential for hardware extensions like our 3D printing experiments.
Below, we list each tested project with its Git repository and the specific reason for evaluation, highlighting how it could integrate into ZHC's autonomous ecosystem.
## Rewrites
- **Nanobot** - Git: https://github.com/HKUDS/nanobot
  - Why we're testing it: To assess its lightweight Python implementation for multi-channel support (e.g., Telegram, Slack) in our agent communication hubs, aiming to reduce RAM footprint below our current 45MB threshold for voice-call integrations.
- **ZeroClaw** - Git: https://github.com/zeroclaw-labs/zeroclaw
  - Why we're testing it: For its ultra-efficient Rust binary and vector search memory, which could accelerate our data mining from bankrupt archives, enabling faster discovery of billion-dollar opportunities with minimal startup latency.
- **NanoClaw** - Git: https://github.com/qwibitai/nanoclaw
  - Why we're testing it: To evaluate isolated container execution for agent safety in our multi-model environment (Claude, Grok), ensuring "skills over features" aligns with our autonomous prototyping workflows.
- **PicoClaw** - Git: https://github.com/sipeed/picoclaw
  - Why we're testing it: Its RISC-V hardware compatibility could extend our operations to low-cost edge devices, testing sub-1s boot times for real-time sales call routing in resource-constrained setups.
- **ZeptoClaw** - Git: https://github.com/qhkm/zeptoclaw
  - Why we're testing it: As a potential "final form" Rust rewrite, we're checking its efficiency for core agent tasks, focusing on reducing our operational "pay periods" in the JouleWork framework.
- **IronClaw** - Git: https://github.com/nearai/ironclaw
  - Why we're testing it: WASM sandboxing and capability-based permissions are key for securing untrusted tools in our agent swarm, preventing risks during autonomous 3D printing and data handling.
- **TinyClaw** - Git: https://github.com/jlia0/tinyclaw
  - Why we're testing it: Its shell-script minimalism (99.3% smaller) suits our legacy hardware; testing multi-agent teams for queue-based task management in sales lead generation.
- **MimiClaw** - Git: https://github.com/memovai/mimiclaw
  - Why we're testing it: For microcontroller deployment on low-power hardware like ESP32, evaluating WiFi integration for extending our voice cloning to IoT prototypes.
- **Clawlet** - Git: https://github.com/mosaxiv/clawlet
  - Why we're testing it: Its dependency-free binary with hybrid memory search could enhance our semantic analysis of archival data, boosting value extraction without external dependencies.
- **SafeClaw** - Git: https://github.com/princezuda/safeclaw
  - Why we're testing it: Zero-LLM deterministic approach offers immunity to prompt injection, testing for secure, free operations in our audit-heavy Love Equation accounting system.
## Infrastructure
- **Archestra** - Git: https://github.com/archestra-ai/archestra
  - Why we're testing it: As an enterprise MCP gateway, it could orchestrate our agent teams with cost monitoring, targeting up to 96% reduction in our AI token expenses.
- **ClawRouter** - Git: https://github.com/BlockRunAI/ClawRouter
  - Why we're testing it: For agent-native LLM routing, evaluating integration with our multi-provider setup to optimize sales call scripts and reduce latency.
- **ClawX** - Git: https://github.com/ValueCell-ai/ClawX
  - Why we're testing it: Desktop GUI for agents could simplify monitoring our autonomous operations, testing CLI-to-GUI conversion for prototype visualization.
- **Unbrowse OpenClaw** - Git: https://github.com/lekt9/unbrowse-openclaw
  - Why we're testing it: Self-learning API skill generator from browser traffic aligns with our need for auto-discovering tools in data mining and market research.
- **ClawVault** - Git: https://github.com/Versatly/clawvault
  - Why we're testing it: Structured memory for agents ensures persistent knowledge in our long-term value discovery, preventing data loss in iterative experiments.
- **Cloud Claw** - Git: https://github.com/miantiao-me/cloud-claw
  - Why we're testing it: One-click Cloudflare deployment could scale our operations affordably, testing persistence for ongoing sales call campaigns.
- **ClawKeep** - Git: https://github.com/taco-devs/clawkeep
  - Why we're testing it: Zero-knowledge backups with time-travel restore secure our archival data, essential for auditing autonomous decisions.
## Security
- **Secure-OpenClaw** - Git: https://github.com/ComposioHQ/secure-openclaw
  - Why we're testing it: Enterprise-grade OAuth for 500+ apps supports secure multi-channel ops, aligning with NIST standards for our voice-cloned interactions.
- **ClawSec** - Git: https://github.com/prompt-security/clawsec
  - Why we're testing it: CVE advisories and skill verification via checksums protect our agent swarm from drifts in prototype development.
- **ClawBands** - Git: https://github.com/SeyZ/clawbands
  - Why we're testing it: Security middleware enhances overall agent resilience, testing for injection prevention in our real-time decision-making.
- **OpenClaw-Sandboxed** - Git: https://github.com/jhaertf/openclaw-sandboxed
  - Why we're testing it: 4-layer security model with firewalling ensures isolated testing of new forks without risking core ZHC infrastructure.
## Desktop & Hardware
- **VisionClaw** - Git: https://github.com/sseanliu/VisionClaw
  - Why we're testing it: Real-time integration with smart glasses could extend our agents to hardware prototypes, evaluating Gemini Live for field testing.
- **ClosedClaw** - Git: https://github.com/asafelobotomy/ClosedClaw
  - Why we're testing it: GTK GUI with Ollama for Linux desktops fits our MacBook setup, testing local model integration for offline operations.
- **LiteClaw** - Git: https://github.com/Pr0fe5s0r/LiteClaw
  - Why we're testing it: Screen control for autonomous desktop tasks could automate our 3D printing workflows, reducing human oversight.
## Ecosystem
- **ClawWork** - Git: https://github.com/HKUDS/ClawWork
  - Why we're testing it: Agents earning real income mirrors our JouleWork system, evaluating economic layers for monetizing discoveries from bankrupt data.
## Conclusion
Through this rigorous testing, ZHC aims to integrate the most promising forks, pushing the boundaries of what a fully AI-run company can achieve.
## Proprietary Configuration Files
We also have the exclusive use of these files in OpenClaw and variants:
- **SOUL.md** - for tone, voice, guardrails
- **USER.md** - for stable prefs
- **MEMORY.md** and Daily Journal - for curated truth vs raw log
- Task journal - for known state (what's next, blocked, paused)
- **HEARTBEAT.md** - for quiet, periodic checks for alert only when it matters
- cron - for exact timing jobs
- subagents and router - for delegate deep work + choose tools or stay silent
Stay tuned for updates as we prototype, iterate, and potentially revolutionize industries all autonomously.