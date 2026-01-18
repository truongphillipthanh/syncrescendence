# PLATFORM FEATURE TELEOLOGY TABLES
## Feature-by-Feature Purpose, Use Cases, and Governance

**Purpose**: Teleologize every configurable feature across the platform ecosystem
**Generated**: 2026-01-16
**Sources**: platform_features.md, platform research documents

---

## I. HOW TO USE THESE TABLES

Each table follows this structure:

| Feature | Purpose | Best Use Cases | Failure Modes | Governance Rule | Account Dependency |
|---------|---------|----------------|---------------|-----------------|-------------------|

**Legend**:
- **Purpose**: Why this feature exists (teleology)
- **Best Use Cases**: When to use it
- **Failure Modes**: What can go wrong
- **Governance Rule**: How to use it correctly
- **Account Dependency**: Required tier/entitlement

---

## II. CLAUDE (Anthropic)

### Web App Features

| Feature | Purpose | Best Use Cases | Failure Modes | Governance Rule | Account Dependency |
|---------|---------|----------------|---------------|-----------------|-------------------|
| **Projects** | Isolate context per work domain | Separate clients, research areas | Context leakage if wrong project | One project per major work stream | Pro+ |
| **Project Knowledge** | Persistent files available to project | Reference docs, configs | Outdated files mislead model | Review quarterly, keep current | Pro+ |
| **Memory** | Cross-session user context | Preferences, background | Stale memory, wrong assumptions | Periodic review, opt-out sensitive | Pro+ |
| **Artifacts** | Downloadable file generation | Code, docs, data | Lost if not downloaded | Always download before session end | Free+ |
| **Extended Thinking** | Deeper reasoning with thinking budget | Complex analysis, architecture | Token cost, latency | Use ultrathink for architectural decisions only | Pro+ |
| **Deep Research** | Multi-source research synthesis | Comprehensive investigation | 45-min sessions consume quota | Reserve for paradigm-level queries | Max |

### Claude Code Features

| Feature | Purpose | Best Use Cases | Failure Modes | Governance Rule | Account Dependency |
|---------|---------|----------------|---------------|-----------------|-------------------|
| **CLAUDE.md** | Constitutional rules per project | Persistent context, anti-patterns | Ignored if too long | Keep under 4K tokens, essential rules only | Free |
| **Plan Mode** | Separate planning from execution | Complex multi-step tasks | Over-planning without execution | Time-box planning, then execute | Free |
| **Sub-agents** | Parallel execution with context isolation | Complex projects needing parallel work | Coordination failure, orphaned agents | Use for independent work streams | Free |
| **Background agents** | Non-blocking long tasks | Build, test, research while coding | Forgotten running agents | Check /tasks regularly | Free |
| **MCP Servers** | External tool integration | Database, API, service access | Context bloat from too many | Progressive disclosure pattern | Free |
| **Slash commands** | Custom reusable prompts | Repetitive tasks | Stale commands | Review and update with workflow | Free |
| **Hooks** | Pre/post tool automation | Git hooks, linting, validation | Breaking automation | Test thoroughly before enabling | Free |
| **Extended thinking** | Deep reasoning in CLI | Architecture, complex bugs | Cost, latency | ultrathink/megathink/think tiering | Pro |

### Claude Desktop Features

| Feature | Purpose | Best Use Cases | Failure Modes | Governance Rule | Account Dependency |
|---------|---------|----------------|---------------|-----------------|-------------------|
| **System-wide access** | Use Claude anywhere | Quick queries, writing assist | Distraction, context switching | Define clear use cases | Pro+ |
| **MCP in Desktop** | Tools available in desktop app | File access, integrations | Configuration drift from CLI | Keep configs synchronized | Pro+ |

---

## III. CHATGPT (OpenAI)

### Web App Features

| Feature | Purpose | Best Use Cases | Failure Modes | Governance Rule | Account Dependency |
|---------|---------|----------------|---------------|-----------------|-------------------|
| **Custom Instructions** | Persistent user context | Role definition, preferences | Stale instructions | Review monthly | Free+ |
| **Memory** | Cross-conversation learning | Background, preferences | Wrong memories, privacy | Review and clear periodically | Plus+ |
| **Custom GPTs** | Purpose-built assistants | Specialized workflows | Maintenance burden | Only create for frequently-used patterns | Plus+ |
| **Projects** | Isolated conversation contexts | Separate work streams | Context leakage | Clear project boundaries | Plus+ |
| **Canvas** | Collaborative document editing | Iterative specs, writing | Abandoned drafts | Complete or export, never leave in canvas | Plus+ |
| **Deep Research** | Multi-source synthesis | Comprehensive investigation | Long wait times (2-4 min) | Reserve for research-heavy tasks | Pro |
| **Agent Mode** | Autonomous web browsing | Web tasks, form filling | Prompt injection, quota limits | Monitor carefully, verify outputs | Plus+ (40/mo) |
| **Voice** | Spoken conversation | Hands-free, emotional nuance | Transcription errors | Confirm critical info in text | Free+ |
| **Health Integration** | Wellness queries | Health data synthesis | Privacy sensitivity, EEA excluded | Use only for personal health | Free+ |

### Codex CLI Features

| Feature | Purpose | Best Use Cases | Failure Modes | Governance Rule | Account Dependency |
|---------|---------|----------------|---------------|-----------------|-------------------|
| **GitHub Integration** | Native repo access | PR review, issue management | Conflicts with Claude Code | Use for GitHub-specific workflows only | Plus+ |
| **@codex in PRs** | AI-assisted code review | Automated PR feedback | Over-reliance on AI review | Human review still required | Plus+ |

---

## IV. GEMINI (Google)

### Web App Features

| Feature | Purpose | Best Use Cases | Failure Modes | Governance Rule | Account Dependency |
|---------|---------|----------------|---------------|-----------------|-------------------|
| **2M Context Window** | Massive document processing | Entire codebase, long videos | Latency on full utilization | Use for genuinely large contexts | AI Pro+ |
| **Personal Intelligence** | Cross-Google-service synthesis | Personal productivity | No project isolation, US-only | Personal tasks only, not confidential | AI Pro+ |
| **Drive Connector** | Repository visibility | Corpus queries, file finding | Sync lag, permission issues | Verify folder access at session start | AI Pro+ |
| **Video Processing** | Native video analysis | YouTube transcription, analysis | Context budget (1hr = 1M tokens) | Pre-triage video value before processing | AI Pro+ |
| **Audio Processing** | Efficient audio analysis | Podcast transcription | Speaker diarization quality | Verify speaker attribution | AI Pro+ |
| **Gems** | Custom specialized assistants | Role-specific configurations | Maintenance burden | Only for frequently-used roles | AI Pro+ |

### NotebookLM Features

| Feature | Purpose | Best Use Cases | Failure Modes | Governance Rule | Account Dependency |
|---------|---------|----------------|---------------|-----------------|-------------------|
| **Grounded RAG** | Zero-hallucination Q&A | Citation-critical queries | Limited to uploaded sources | Upload comprehensive source set | Free |
| **Audio Overview** | Audio digest of sources | Ambient learning | Simplified content | Use for familiarization, not precision | Free |
| **Source Citations** | Precise source attribution | Verification, audit trails | Only works with uploaded content | Upload authoritative sources | Free |

### AI Studio Features

| Feature | Purpose | Best Use Cases | Failure Modes | Governance Rule | Account Dependency |
|---------|---------|----------------|---------------|-----------------|-------------------|
| **Context Caching** | 90% cost reduction on repeated context | Batch processing | Cache expiration | Plan batch operations together | API |
| **Batch API** | Programmatic access | Automation, pipelines | API key security | Rotate keys, monitor usage | API |

### Jules Agent

| Feature | Purpose | Best Use Cases | Failure Modes | Governance Rule | Account Dependency |
|---------|---------|----------------|---------------|-----------------|-------------------|
| **Async Execution** | Background coding without supervision | Bug fixes, dependency updates | Unsupervised changes | Review all PRs before merge | AI Pro+ |
| **GitHub Clone** | Independent repo access | Issue-based fixes | Conflicts with local work | Coordinate with local changes | AI Pro+ |

---

## V. PERPLEXITY

### Core Features

| Feature | Purpose | Best Use Cases | Failure Modes | Governance Rule | Account Dependency |
|---------|---------|----------------|---------------|-----------------|-------------------|
| **Citation Search** | Accuracy-first research | Fact-checking, sourcing | Copyright concerns (litigation) | Cross-verify with primary sources | Free+ |
| **Deep Research** | Comprehensive multi-source synthesis | Topic deep dives | 2-4 min wait, quota limits | Reserve for research-heavy needs | Pro |
| **Multi-Model** | Access to multiple providers | Comparative queries | Model-specific quirks | Specify model when needed | Pro |
| **API** | Programmatic search | Automated fact-checking | Rate limits, cost | Batch queries efficiently | Pro/API |

### Limitations

| Limitation | Implication | Workaround |
|------------|-------------|------------|
| **Stateless** | No cross-query memory | Export immediately, use other platforms for synthesis |
| **No execution** | Cannot act on findings | Route to Claude Code for action |
| **Legal exposure** | Publisher lawsuits | Cross-verify, don't rely exclusively |

---

## VI. GROK (xAI)

### Core Features

| Feature | Purpose | Best Use Cases | Failure Modes | Governance Rule | Account Dependency |
|---------|---------|----------------|---------------|-----------------|-------------------|
| **X Integration** | Social signal sensing | Trend analysis, discourse | Terms allow "forever" data use | Never process confidential via X-connected Grok | Premium |
| **Voice API** | Cost-effective voice | Voice assistants, hands-free | Quality varies by language | Test before production use | API |
| **Projects** | Multi-session threads | Extended research | Limited compared to others | Export findings regularly | Premium |
| **Image Generation** | Visual content creation | Imagery for content | Disabled for real people | Check current restrictions before using | Premium |

### Limitations

| Limitation | Implication | Workaround |
|------------|-------------|------------|
| **No desktop automation** | Voice API only | Use for voice, other platforms for execution |
| **Safety restrictions** | Features may be disabled | Monitor xAI announcements |
| **Regulatory scrutiny** | Uncertain feature availability | Have fallback for critical workflows |

---

## VII. CROSS-PLATFORM GOVERNANCE SUMMARY

### Feature Selection Matrix

| Need | Primary Platform | Fallback |
|------|------------------|----------|
| **Strategic synthesis** | Claude Web (Oracle) | ChatGPT |
| **Execution** | Claude Code | — |
| **Planning/Spec** | ChatGPT | Claude Web |
| **Corpus-scale sensing** | Gemini | — |
| **Video processing** | Gemini | — |
| **Citation research** | Perplexity | Gemini |
| **Social signals** | Grok | — |
| **Voice** | Grok API (cost) / ChatGPT (quality) | — |

### Account Budget Allocation

| Platform | Tier | Monthly Cost | Role |
|----------|------|--------------|------|
| Claude | Pro x3 | $60 | Oracle + Executor x2 |
| ChatGPT | Plus | $20 | Deviser |
| Gemini | AI Pro | $20 | Sensor |
| **Total** | — | **$100** | Full constellation |

### Feature Rotation Policy

Not all features are used constantly. Review quarterly:
1. Which features were actually used?
2. Which can be downgraded/removed?
3. Which emerging features should be adopted?

---

## VIII. GOVERNANCE RULES SUMMARY

### Universal Rules

1. **Ground truth is repository** — never let platform be sole storage
2. **Export before delete** — always create continuation before ending significant session
3. **Verify before claim** — run verification commands, don't assume
4. **Tiered model use** — expensive models (Opus, GPT-5.2 Thinking) for judgment, cheap for volume
5. **Progressive disclosure** — don't load all tools, search then load

### Platform-Specific Rules

| Platform | Critical Rule |
|----------|---------------|
| Claude Web | Always download artifacts before session end |
| Claude Code | Never claim done without verification evidence |
| ChatGPT | Always include acceptance criteria in plans |
| Gemini | Always cite sources; never claim without citation |
| Perplexity | Export immediately (stateless!) |
| Grok | Never process confidential data via X connection |

---

**This table governs all platform feature decisions. Consult before configuring.**
