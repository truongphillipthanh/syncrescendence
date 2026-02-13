# SYNTHESIS: OpenClaw — Deep Research v2 (MEDLEY)

**Synthesis Date**: 2026-02-03
**Protocol**: MEDLEY — 5 parallel streams (Augur, Oracle, Diviner, Vanguard, Vizier)
**Synthesized By**: Ajna (Opus 4.5)
**Prior Version**: SYNTHESIS-openclaw.md (2026-02-02, single-source)

---

## Meta: Source Quality Assessment

| Stream | Avatar | Unique Value | Quality |
|--------|--------|-------------|---------|
| Augur (Perplexity) | Citation-backed claims, Brave API pricing | HIGH — 10 sources, all cited |
| Oracle (Grok) | X/Twitter power users, community vibe | MEDIUM-HIGH — good signal/noise separation |
| Diviner (Gemini Web) | Complete API surface, technical architecture | HIGH — most comprehensive technical reference |
| Vanguard (ChatGPT) | Implementation blueprint, config examples | HIGH — actionable, security-focused |
| Vizier (Claude Web) | Strategic framing, MCP analysis, Polaris precedent | HIGH — productive tensions preserved |

---

## 1. CRITICAL: Security Reality Check

### The Threat Landscape Is Worse Than We Knew

**CONFIRMED by multiple sources (Vanguard, Vizier):**
- **230+ malicious skills** discovered pushing password-stealing malware (BleepingComputer, eSecurity Planet)
- **MedusaLocker ransomware** demonstrated via weaponized skills (Cato Networks)
- **Supply chain attack proof**: Backdoored skill achieved real executions on 16 developer machines across 7 countries within 8 hours
- **One-click RCE vulnerability** in OpenClaw (The Hacker News, February 3, 2026 — TODAY)
- **ClawdHub has NO sandboxed execution** — skills run with full system permissions
- **JFrog report**: "OpenClaw's third-party extensions are largely unvetted"

### Immediate Security Actions (P0)

1. **Audit all 10 installed ClawdHub skills** — read every SKILL.md and script
2. **Enable sandbox mode**: `agents.defaults.sandbox.mode = "all"`
3. **Gateway security**: Ensure bound to localhost, enable auth token
4. **File permissions**: `chmod 600 ~/.openclaw/openclaw.json`
5. **Pin skill versions** — no auto-updates
6. **Run `openclaw security audit`** if available

### Productive Tension (PRESERVED)
> **Security sovereignty vs. capability expansion**: ClawdHub has valuable skills but the registry is essentially hostile territory. We MUST treat every third-party skill as potentially malicious code. Our 10 installed skills need immediate audit. The tradeoff between autonomy and security "cannot be resolved — it must be managed through layered defenses." (Vizier)

---

## 2. Skill Ecosystem — Verified Numbers

| Source | Claimed Count | Confidence |
|--------|--------------|------------|
| Oracle (X discourse) | 1,715+ | UNVERIFIED — may be ecosystem conflation |
| Augur (Perplexity) | 700+ | CONFIRMED — from video walkthrough |
| Vizier (Claude Web) | 565+ | CONFIRMED — from ClawdHub directly |
| Augur (registry) | No official paywall | CONFIRMED — paywalling is off-platform |

**Takeaway**: Real count is likely 500-700 unique, quality skills. The 1,715 number appears inflated. Growth is rapid but quality is uneven.

### Top Skill Categories (Community Consensus)
- **Browser/Web**: Browser control, web search, web fetch
- **DevOps**: GitHub, shell exec, log readers, code search
- **Communication**: Slack, iMessage, email, calendar
- **Research**: Summarizers, vector DB, embedding tools
- **Automation**: Cron patterns, file management, scheduling

### AgentSkills Spec Status
- **Still Anthropic-originated** — no community fork detected
- ClawdHub indexes AgentSkills bundles
- OpenClaw follows the spec natively

---

## 3. Multi-Model Collaboration Patterns

### Confirmed Patterns (from all 5 sources)

| Pattern | Description | Source |
|---------|-------------|--------|
| **Orchestrator + Sub-agents** | Premium model (Opus/GPT-5.2) coordinates cheap models (Sonnet/Haiku/DeepSeek) | Vanguard, Oracle |
| **Council/Chamber** | Multiple perspectives on same problem, synthesized by lead | Council skill, Diviner |
| **Driver/Navigator** | One agent executes, one reviews | Vizier (claude-flow) |
| **Reflection/Critic** | Generate → Critique → Iterate loop | Vizier |
| **3-Tier Cost Routing** | Simple→Haiku, Medium→Sonnet, Complex→Opus | Vizier (claude-flow) |
| **Cron-Driven Autonomy** | Background agents via heartbeat + cron | Diviner, Augur |
| **Parallel Research** | Spawn multiple sub-agents for different facets | Our MEDLEY pattern |

### The "Conversational AI" Pattern — Demystified
**CONFIRMED (Oracle, Augur, Diviner):** This is NOT a specific OpenClaw feature. It refers to:
- Using `sessions_spawn` with different models
- Multi-agent routing (different agents per channel)
- External API calls to other LLMs (OpenRouter, Kimi, etc.)
- Agents collaborating in shared channels (MoltSlack, Moltbook)

**Translation to our architecture**: This IS what Syncrescendence was designed for. The community is independently discovering constellation-like patterns. We have a structural advantage: formalized roles, terminology (Rosetta Stone), and protocol infrastructure.

### The Polaris Precedent (IMPORTANT)
**Vizier found**: Hippocratic AI's **Polaris** system — a 1+ trillion parameter healthcare constellation:
- Primary Agent (70B-100B) as stateful conversational driver
- Support Agents (50B-100B each) for specialized domains
- Message-passing framework, iterative co-training
- Performed on par with licensed nurses
- **arXiv:2403.13313** — peer-reviewed

**This validates our Constellation architecture at a fundamental level.** The pattern works. It's published. It's proven in healthcare (higher stakes than our domain).

### sessions_spawn Bug — Status Update
- **Bug**: `agentId` silently drops `model` param
- **Workaround**: Only pass `model`, `label`, `task` — drop `agentId`
- **Fix**: Reportedly addressed in v2026.2.2 (per Diviner, citing CHANGELOG)
- **Filed**: GitHub issue #6817

---

## 4. Technical Architecture — Key Insights (Diviner)

### Session Architecture
- Sessions are file-system backed (not DB)
- Session keys: `agent:<agentId>:<mainKey>`
- Daily reset at 04:00 AM local (configurable)
- Pruning: removes old toolResult (never user/assistant messages)
- Compaction: summarizes older segments into memory notes

### Cron Architecture
- **sessionTarget: "main"** → injects into main session (needs conversation context)
- **sessionTarget: "isolated"** → fresh session, zero-context (clean execution)
- Three schedule types: `at` (one-shot), `every` (interval), `cron` (unix cron)
- `deliver: true` posts summary back to main chat

### Tool Restriction Chain (8 Levels — CRITICAL)
1. Global Tool Profile
2. Global Provider Profile
3. Global Policy (allow/deny)
4. Provider Policy
5. **Agent Policy** (primary user config layer)
6. Agent Provider Policy
7. Sandbox Policy
8. Sub-agent Policy

**"Deny Wins"** — if any layer denies, it's blocked regardless.

### Integration Points for Syncrescendence
| Syncrescendence Phase | OpenClaw Primitive |
|----------------------|-------------------|
| CAPTURE | Gateway Event Loop (cron, webhooks, inbound messages) |
| DISPATCH | sessions_spawn + Multi-Agent Routing |
| RETURN | Announce Step (auto-injects result to parent) |

---

## 5. Brave Search API — Setup Path

**CONFIRMED (Augur, Vanguard):**
- **Free tier**: 2,000 queries/month, $0, 1 query/second
- **Base AI**: $5/1,000 requests (up to 20M/month)
- **Pro AI**: $9/1,000 requests (unlimited)

**Setup**:
1. Create account at brave.com/search/api
2. Select "Data for Search" → Free tier
3. Generate subscription token
4. Add to OpenClaw: `openclaw configure --section web` or config.patch

**Budget impact**: Free tier covers our needs. Even Base AI ($5/1k) is negligible vs $160/mo.

---

## 6. Strategic Analysis (Vizier Synthesis)

### How OpenClaw Changes Our Architecture
- **Before**: Sovereign manually relays prompts via -OUTGOING (human bottleneck)
- **Now**: Ajna can compose prompts, but web apps still need manual relay
- **Path to autonomous dispatch**: MCP servers (7,890+ available), browser automation (brittle), direct API calls

### Productive Tensions (PRESERVED — NOT RESOLVED)

1. **Repo sovereignty vs. OpenClaw memory**: "Repo is ground truth" but OpenClaw has its own MEMORY.md + memory_search. **Resolution path**: Use OpenClaw memory for operational state, repo for canonical knowledge. They serve different functions.

2. **Manual Constellation dispatch vs. autonomous agents**: Web platform avatars require human relay. OpenClaw can run autonomously. **The relay is becoming technical debt** — but premature automation without security is worse.

3. **Budget vs. capability**: $160/mo is fixed. Multi-model burns tokens. **Strategy**: Use GPT-5.2 ($20 flat fee) for high-volume work, reserve Opus for synthesis. Sonnet/Haiku for sub-agents.

4. **Publication timing**: "Early publication establishes precedent; latent development maintains sovereignty." **Vizier recommends**: Publish the coordination layer (the abstraction) while keeping implementation proprietary. "Publish doors, not rooms."

### Community Comparison
- **Are they reinventing our Constellation?** Partially. Multi-agent routing, model specialization, council patterns — all echoes of our architecture. But they lack our formalized terminology (Rosetta Stone), semantic notation (SN), and protocol infrastructure.
- **What they have that we don't**: Production deployment at scale, community-tested patterns, security hardening experience, ecosystem momentum.

---

## 7. Priority Actions

### P0 — Next 24 Hours
1. ⚠️ **SECURITY AUDIT**: Read every installed ClawdHub skill manually
2. 🔍 **Brave Search API**: Sign up, get free key, configure OpenClaw
3. 🔒 **Harden config**: Sandbox mode, localhost binding, file permissions
4. 📋 **Verify OpenClaw version**: Ensure we're on v2026.2.2+ (sessions_spawn fix)

### P1 — Next 7 Days
5. 🏗️ **Multi-agent config**: Formalize Ajna/Psyche as separate agents in openclaw.json
6. 🧪 **Test sessions_spawn**: Verify model routing works correctly (no agentId bug)
7. 📐 **Skill governance policy**: Approval process, version pinning, audit schedule
8. 🔬 **Research: MCP integration**: Can we use MCP servers to bypass -OUTGOING relay?

### P2 — Next 30 Days
9. 🌐 **Autonomous dispatch prototype**: MCP or API-based dispatch to web platforms
10. 📊 **Token tracking**: Monitor spend per agent/model, optimize routing
11. 🏛️ **Council pattern**: Implement structured multi-model deliberation
12. 📖 **Polaris paper review**: Read arXiv:2403.13313 for constellation architecture patterns

### P3 — Next 90 Days
13. 📝 **Publication decision**: Evaluate "publish doors, not rooms" — maybe a blog post or skill
14. 🔄 **Twin protocol migration**: Move Ajna↔Psyche from Slack relay to native sessions_send
15. 🛡️ **Container deployment**: Move to Docker/VM for OS-level isolation
16. 🌍 **Community engagement**: Selective participation in OpenClaw Discord

---

## 8. Key X/Twitter Threads to Read (Oracle Selection)

1. **@openclaw v2026.2.2 release** — roadmap + security: https://x.com/openclaw/status/2018875417902682137
2. **@danpeguine "why nuts"** — patterns/hype: https://x.com/danpeguine/status/2014760164113477700
3. **@aref_vc breakdown** — conversational/async patterns: https://x.com/aref_vc/status/2018286196280131678
4. **@mernit Kimi PSA** — multi-model cost optimization: https://x.com/mernit/status/2018435162334269503
5. **@ryancarson "holy shit"** — real workflows/agents as employees: https://x.com/ryancarson/status/2018343411087016048

---

## Version History
- **v1.0** (2026-02-02): Single-source synthesis from docs + web fetch
- **v2.0** (2026-02-03): MEDLEY synthesis — 5 platform streams, 90+ pages of raw intel compressed
