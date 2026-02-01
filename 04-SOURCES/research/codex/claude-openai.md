# OpenAI Platform Ecosystem: Forensic Evidence-Based Catalog

**Research Date:** January 13, 2026
**Temporal Note:** User requested January 2025 snapshot; this catalog reflects the ecosystem as it exists in January 2026, documenting evolution from January 2025 forward.

---

## 0. AS-OF SNAPSHOT

### Executive Summary of Recent Material Changes

OpenAI's platform underwent radical transformation between January 2025 and January 2026. The most consequential shifts include the **GPT-5/5.1/5.2 model series** replacing GPT-4, **Operator's integration into ChatGPT agent mode**, **Assistants API deprecation** (sunset August 2026), and **ChatGPT Team's rebrand to Business**. The introduction of the **Responses API** as the recommended entry point signals OpenAI's strategic shift toward agentic workflows with built-in tools.

**Critical January 2025 Events:**
- **January 23, 2025:** Operator launched (CUA-powered browser agent) for Pro users in US
- **January 31, 2025:** o3-mini released to all ChatGPT users including free tier

**Key Evolutions Since January 2025:**
| Change | Date | Impact |
|--------|------|--------|
| Operator → ChatGPT agent mode | July 2025 | Browser automation integrated into main product |
| GPT-5 release | August 2025 | Flagship model upgrade |
| ChatGPT Team → Business rename | August 2025 | Tier naming standardization |
| Assistants API deprecation notice | August 2025 | Migration to Responses API required |
| Sora 2 API release | September/October 2025 | Video generation API availability |
| GPT-5.2 release | December 2025 | Current flagship with Instant/Thinking modes |
| ChatGPT Go launch | August 2025 | New $5/month regional tier |

### Scope Boundaries

**What Was Checked:**
- OpenAI pricing/plan pages (chatgpt.com, openai.com/pricing)
- Platform documentation (platform.openai.com/docs)
- Help Center (help.openai.com) - 40+ articles reviewed
- GitHub organization (github.com/openai) - 228+ repos scanned
- Official blog posts and product announcements
- Status page (status.openai.com)
- App store listings (iOS, Android, Microsoft Store)
- Community forums and practitioner channels

**What Was Not Checked:**
- Internal/enterprise-only documentation requiring authentication
- Azure OpenAI-specific configurations
- Detailed SOC 2/compliance audit reports
- Regional pricing variations outside US

---

## 1. ECOSYSTEM TAXONOMY (Full Surface Area)

### A. ChatGPT Consumer Platform

```
ChatGPT Consumer
├── Chat Interface
│   ├── Models: GPT-5.2 Instant, GPT-5.2 Thinking, GPT-5.2 Pro, GPT-5/5.1, GPT-4o, GPT-4.1
│   ├── Reasoning: o3 (100/week), o4-mini (300/day), o4-mini-high (100/day)
│   ├── Model Picker (paid tiers only)
│   └── Thinking Time Settings: Light/Standard/Extended/Heavy (Pro)
├── Browsing/Search
│   └── ChatGPT Search (GA all users Dec 2024)
├── File Handling
│   ├── Uploads: 2M tokens/file, 80 files/3hrs (paid), 3/day (free)
│   ├── Code Interpreter/Data Analysis
│   └── Export/Download
├── Memory
│   ├── Saved Memories (explicit)
│   └── Reference Chat History (Plus/Pro)
├── Projects
│   ├── Custom Instructions per project
│   ├── File attachments: 5-40 files by tier
│   ├── Shared Projects (Business/Enterprise)
│   └── Unlimited projects per user
├── Custom GPTs
│   ├── GPT Builder (paid tiers)
│   ├── GPT Store/Apps Directory
│   ├── 20 knowledge files per GPT
│   └── Custom Actions (API connections)
├── Voice Mode
│   ├── Advanced Voice (realtime)
│   ├── Video/Screenshare (Plus+, not EU)
│   └── Voice characters (multiple voices)
├── Image Generation
│   ├── GPT Image 1.5 (current)
│   ├── DALL-E 3 (deprecated May 2026)
│   ├── Images App (iOS/Android/Web)
│   └── Image editing (inpainting)
├── Video Generation (Sora)
│   ├── Sora 2/Sora 2 Pro
│   ├── sora.com + Sora app
│   ├── 10-25 second videos
│   └── Plus/Pro only, EU/UK restricted
├── Deep Research
│   ├── Multi-step research agent
│   ├── 10-125 queries/month by tier
│   └── Lightweight fallback after quota
├── Canvas
│   ├── Writing workspace
│   ├── Code workspace (Python execution)
│   └── Collaborative editing
├── Agent Mode
│   ├── Visual browser (GUI automation)
│   ├── Text-based browser
│   ├── Terminal (code execution)
│   ├── Task scheduling
│   └── Connectors (60+ apps)
├── Connectors/Apps
│   ├── Slack, Google Drive, SharePoint
│   ├── GitHub, Atlassian, HubSpot
│   └── Custom MCP connectors
└── Notifications & Tasks
    └── Scheduled recurring tasks
```

**Access Gates:**

| Feature | Free | Go | Plus | Pro | Business | Enterprise |
|---------|------|-----|------|-----|----------|------------|
| GPT-5.2 Instant | Limited | Extended | ✓ | Unlimited | Unlimited | Unlimited |
| GPT-5.2 Thinking | ✗ | ✗ | 3K/week | Unlimited | 3K/week | Pool |
| GPT-5.2 Pro | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ |
| Deep Research | 5 light/mo | ✗ | 10+15/mo | Extended | 10+15/mo | Pool |
| Agent Mode | ✗ | ✗ | ~40/mo | ~400/mo | ~40/mo | Pool |
| Sora | Images only | ✗ | ✓ | Priority | Consumer | ✗ |
| Codex | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ |
| Custom GPTs (create) | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ |

### B. ChatGPT Organization (Business/Enterprise)

```
ChatGPT Organization
├── Admin Controls
│   ├── User Management
│   ├── Role-Based Access Control (Enterprise only)
│   ├── Usage Analytics/Dashboards
│   └── Domain Verification
├── Identity & Access
│   ├── SAML SSO
│   ├── OIDC SSO
│   ├── SCIM Provisioning (Enterprise only)
│   └── MFA Enforcement
├── Data & Compliance
│   ├── Training Opt-Out (default)
│   ├── SOC 2 Type 2 Compliance
│   ├── GDPR/CCPA Support
│   ├── Data Residency (select regions)
│   ├── Inference Residency (Enterprise)
│   ├── Audit Logs (Enterprise)
│   └── Compliance API (Enterprise)
├── Collaboration
│   ├── Shared Projects
│   ├── Workspace GPTs
│   └── Connectors Administration
└── Flexible Pricing
    ├── Per-seat limits (Business)
    ├── Credit pools (Enterprise)
    └── Overage handling
```

### C. Developer Platform (API)

```
Developer Platform
├── APIs
│   ├── Responses API (NEW - recommended)
│   │   ├── Built-in tools: web_search, file_search, computer_use, code_interpreter
│   │   └── Remote MCP servers support
│   ├── Chat Completions API (legacy standard)
│   ├── Assistants API (DEPRECATED Aug 2026)
│   ├── Realtime API (WebSocket/WebRTC)
│   │   └── Beta deprecation: Feb 2026
│   ├── Batch API (50% cost savings)
│   ├── Images API
│   │   ├── gpt-image-1.5 (current)
│   │   ├── gpt-image-1, gpt-image-1-mini
│   │   └── DALL-E 2/3 (deprecated May 2026)
│   ├── Videos API (Preview)
│   │   ├── sora-2, sora-2-pro
│   │   └── Duration: 4-25 seconds
│   ├── Audio APIs
│   │   ├── Text-to-Speech (tts-1, tts-1-hd, gpt-4o-mini-tts)
│   │   ├── Transcription (whisper-1, gpt-4o-transcribe)
│   │   └── Translation
│   ├── Embeddings API
│   │   └── text-embedding-3-small/large
│   ├── Fine-tuning API
│   │   └── gpt-4.1, gpt-4o-mini, o4-mini
│   ├── Moderation API (free)
│   └── Files API
├── SDKs
│   ├── Python (openai) - v2.15.0
│   ├── Node.js (openai) - v6.15.0
│   ├── .NET (OpenAI) - active
│   ├── Go (openai-go) - beta
│   ├── Java (openai-java) - beta
│   └── Ruby (openai-ruby) - active
├── Authentication
│   ├── API Keys (user-scoped)
│   ├── Admin API Keys
│   └── Organization structure
├── Rate Limits (Tiers 1-5)
│   ├── RPM (requests/minute)
│   ├── TPM (tokens/minute)
│   ├── RPD (requests/day)
│   └── IPM (images/minute)
└── Pricing Tiers
    ├── Standard (pay-as-you-go)
    ├── Priority (higher reliability)
    ├── Flex (lower cost, higher latency)
    └── Batch (50% discount, 24hr)
```

### D. Agentic/Automation Stack

```
Agentic Platform
├── Codex (Cloud Coding Agent)
│   ├── Codex CLI (@openai/codex)
│   │   ├── Interactive mode
│   │   ├── Headless mode (codex exec)
│   │   └── Approval modes: Suggest/Auto-Edit/Full Auto
│   ├── IDE Extensions (VS Code, Cursor, JetBrains)
│   ├── Codex Cloud (chatgpt.com/codex)
│   ├── GitHub Integration (@codex mentions)
│   ├── GitHub Action (openai/codex-action)
│   ├── Slack/Linear Integrations
│   └── AGENTS.md custom instructions
├── Agents SDK
│   ├── Python (openai-agents) - v0.5+
│   │   ├── Agents, Handoffs, Guardrails, Sessions
│   │   ├── Built-in tools
│   │   └── MCP integration
│   └── TypeScript (@openai/agents)
├── ChatGPT Agent Mode
│   ├── Visual browser (GUI)
│   ├── Text browser
│   ├── Terminal
│   ├── Watch mode (sensitive sites)
│   └── Task scheduling
├── Computer-Using Agent (CUA)
│   ├── API: computer-use-preview
│   ├── Responses API only
│   └── Tier 3-5 developers
├── Tool Protocols
│   ├── Function calling
│   ├── Structured outputs
│   └── MCP (Model Context Protocol)
│       ├── Streamable HTTP
│       └── HTTP/SSE transports
└── Deprecated
    └── Operator (standalone) - sunset Aug 2025
```

### E. Media Stack

```
Media Generation
├── Video (Sora)
│   ├── Models: sora-2, sora-2-pro
│   ├── Modes: text-to-video, image-to-video, remix, storyboard, blend, loop
│   ├── Durations: 4-25 seconds
│   ├── Resolutions: 480p-1080p (app), 720x1280-1792x1024 (API)
│   ├── Audio: Synchronized generation
│   └── Watermarking: Visible + C2PA metadata
├── Images
│   ├── Models: gpt-image-1.5, gpt-image-1, gpt-image-1-mini
│   ├── Deprecated: DALL-E 2/3 (May 2026)
│   ├── Quality: Low/Medium/High
│   ├── Resolutions: 1024×1024, 1024×1536, 1536×1024
│   ├── Editing: Inpainting, image-to-image
│   └── Formats: PNG, JPEG, WebP
├── Audio/Voice
│   ├── Text-to-Speech
│   │   ├── Models: gpt-4o-mini-tts, tts-1, tts-1-hd
│   │   ├── 13 built-in voices
│   │   └── Custom voices (sales contact)
│   ├── Speech-to-Text
│   │   ├── whisper-1, gpt-4o-transcribe
│   │   └── 25MB file limit
│   └── Realtime (speech-to-speech)
│       └── gpt-realtime, gpt-realtime-mini
└── Policies
    ├── Deepfake blocking
    ├── Real people restrictions
    ├── Voice disclosure required
    └── IP content blocking (Sora)
```

### F. Policy/Governance

```
Governance Layer
├── Data Usage
│   ├── Consumer: May train (opt-out available)
│   ├── Business/Enterprise/API: No training (default)
│   └── Data retention: 30 days post-deletion
├── Training Opt-Out
│   └── Settings > Data Controls > "Improve model for everyone"
├── Enterprise Guarantees
│   ├── SOC 2 Type 2
│   ├── Encryption (transit + rest)
│   ├── Data residency (select regions)
│   └── Inference residency (Enterprise)
├── Safety
│   ├── Moderation API
│   ├── Content filters
│   ├── Prompt injection monitoring
│   └── Harmful task refusals (97%)
└── Regional Constraints
    ├── Sora: Not available EU/UK/Switzerland
    ├── Connectors: Some not available EEA/UK
    ├── Video/screenshare: Not available EU
    └── ChatGPT Go: Geo-restricted to select countries
```

---

## 2. SERVICE CATALOG MATRICES

### 2.1 Models Matrix

| Model Family | Context Window | Max Output | Input $/1M | Output $/1M | Endpoints | Status |
|--------------|----------------|------------|------------|-------------|-----------|--------|
| **GPT-5.2** | 400,000 | 128,000 | $1.75 | $14.00 | Responses, Chat, Batch | GA |
| **GPT-5/5.1** | — | — | $1.25 | $10.00 | Responses, Chat | GA |
| **GPT-4.1** | 1,000,000 | — | $2.50 | $10.00 | Responses, Chat, FT | GA |
| **GPT-4.1-mini** | 1,000,000 | — | Lower | Lower | Responses, Chat, FT | GA |
| **GPT-4o** | 128,000 | — | $2.50 | $10.00 | Responses, Chat | GA |
| **GPT-4o-mini** | 128,000 | — | $0.15 | $0.60 | Responses, Chat, FT | GA |
| **o3** | — | — | Higher | Higher | Responses, Chat | GA |
| **o3-pro** | — | — | Highest | Highest | Responses | GA |
| **o4-mini** | — | — | $4.00 | $16.00 | Responses, Chat, FT | GA |
| **gpt-realtime** | — | — | $32 audio | $64 audio | Realtime | Beta |
| **gpt-realtime-mini** | — | — | $10 audio | $20 audio | Realtime | Beta |

### 2.2 Agentic Tools Matrix

| Tool/Feature | Free | Go | Plus | Pro | Business | Enterprise | API |
|--------------|------|-----|------|-----|----------|------------|-----|
| **Codex CLI** | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | Via key |
| **Codex Cloud** | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | — |
| **Agent Mode** | ✗ | ✗ | 40/mo | 400/mo | 40/mo | Pool | — |
| **Deep Research** | 5 light | ✗ | 10+15/mo | Extended | 10+15/mo | Pool | Limited |
| **CUA API** | — | — | — | — | — | — | Tier 3-5 |
| **Agents SDK** | — | — | — | — | — | — | ✓ |
| **MCP Support** | ✗ | ✗ | Via Codex | ✓ | ✓ | ✓ | ✓ |

### 2.3 Media Generation Matrix

| Feature | Free | Plus ($20) | Pro ($200) | API |
|---------|------|------------|------------|-----|
| **DALL-E/GPT-Image** | 2-3/day | 50/3hrs | Unlimited | Pay-per-image |
| **Image quality tiers** | Low | All | All | All |
| **Sora video** | ✗ | 1,000 credits | 10K + unlimited relaxed | $0.10-0.50/sec |
| **Sora max duration** | — | 10s | 20s | 25s |
| **Sora max resolution** | — | 720p | 1080p | 1792×1024 |
| **TTS** | Limited | ✓ | Unlimited | $15-30/1M chars |
| **Voice cloning** | ✗ | ✗ | ✗ | Contact sales |
| **Whisper transcription** | ✓ | ✓ | ✓ | $0.006/min |

### 2.4 Data Tools Matrix

| Feature | Free | Plus | Pro | Business | Enterprise |
|---------|------|------|-----|----------|------------|
| **Code Interpreter** | Limited | ✓ | ✓ | ✓ | ✓ |
| **File uploads/3hr** | 3/day | 80 | 80 | 80 | 80 |
| **Max file size** | 2M tokens | 2M tokens | 2M tokens | 2M tokens | 2M tokens |
| **Project files** | 5 | 25 | 40 | 40 | 40 |
| **Connectors** | ✗ | ✓ | ✓ | ✓ | ✓ |
| **Export** | Limited | ✓ | ✓ | ✓ | ✓ |

### 2.5 Governance Matrix

| Feature | Free | Plus | Pro | Business | Enterprise |
|---------|------|------|-----|----------|------------|
| **Training opt-out** | Available | Available | Available | Default | Default |
| **SSO (SAML/OIDC)** | ✗ | ✗ | ✗ | ✓ | ✓ |
| **SCIM provisioning** | ✗ | ✗ | ✗ | ✗ | ✓ |
| **RBAC** | ✗ | ✗ | ✗ | ✗ | ✓ |
| **Audit logs** | ✗ | ✗ | ✗ | ✗ | ✓ |
| **Data residency** | ✗ | ✗ | ✗ | ✗ | ✓ |
| **SOC 2 compliance** | N/A | N/A | N/A | ✓ | ✓ |
| **Admin console** | ✗ | ✗ | ✗ | Essential | Full |

---

## 3. LIMITS & QUOTAS: Official vs Observed

### ChatGPT Message Limits

| Model | Plan | Official | Community-Observed | Confidence | Reset |
|-------|------|----------|-------------------|------------|-------|
| GPT-5.2 | Free | 10/5hrs | 5-10 (load varies) | Medium | Rolling |
| GPT-5.2 | Plus | 160/3hrs* | 120-160 | Medium | Rolling |
| GPT-5.2 Thinking | Plus | 3,000/week | ~3,000 | High | Weekly |
| GPT-5.2 Pro | Pro | Unlimited | Abuse guardrails | High | — |
| o3 | Plus | 100/week | 100 | High | 7 days from first |
| o4-mini | Plus | 300/day | ~300 | High | Daily |
| o4-mini-high | Plus | 100/day | ~100 | High | Daily |
| GPT-4o | Plus | 80/3hrs | 80-150 | Medium | Rolling |

*Plus GPT-5.2 limit noted as "temporary increase—will revert"

### Image Generation Limits

| Plan | Official | Community-Observed | Confidence |
|------|----------|-------------------|------------|
| Free | 2-3/day | 2/24hrs consistently | High |
| Plus | 50/3hrs rolling | ~50/3hrs, ~180-200/day soft cap | High |
| Team/Business | 100/3hrs | ~100/3hrs | Medium |
| Pro | Effectively unlimited | Very high, abuse detection | Medium |

**Key Observations:**
- Failed generations count against quota (High confidence)
- GPT-Image and DALL-E share quota pool (Medium confidence)
- No in-app counter—notification only at limit (High confidence)

### Deep Research Limits

| Plan | Full Version | Lightweight | Observed Behavior |
|------|--------------|-------------|-------------------|
| Free | 0 | 5/month | 5 lightweight only |
| Plus | 25/month | +15/month | Auto-fallback to lightweight |
| Pro | 125/month | +125/month | Extended access |
| Enterprise | 25/month | Pool varies | Same as Plus baseline |

### Voice Mode Limits

| Plan | Official | Observed |
|------|----------|----------|
| Free | Hours/day (GPT-4o mini) | 15 min - several hours (variable) |
| Plus | Nearly unlimited (GPT-4o) | ~60 min/session, ~60 min/day premium |
| Pro | Unlimited | True unlimited (guardrails) |

**Key Observation:** Voice mode counts time even during silence (High confidence)

---

## 4. DEPRECATION / MIGRATION / ROADMAP

### 4.1 Deprecation Table

| Item | Deprecation Date | Shutdown Date | Replacement | Migration Steps |
|------|-----------------|---------------|-------------|-----------------|
| **Assistants API** | Aug 26, 2025 | Aug 26, 2026 | Responses API | Migrate to Responses API + built-in tools |
| **Realtime API Beta** | — | Feb 27, 2026 | New Realtime GA | Upgrade to stable endpoints |
| **DALL-E 3 snapshots** | Nov 14, 2025 | May 12, 2026 | gpt-image-1.5 | Use gpt-image-1.5 or gpt-image-1 |
| **DALL-E 2** | Legacy | May 12, 2026 | gpt-image-1 | Migrate to GPT Image models |
| **chatgpt-4o-latest** | Nov 18, 2025 | Feb 17, 2026 | gpt-4o snapshots | Use dated snapshots |
| **codex-mini-latest** | Nov 17, 2025 | Jan 16, 2026 | GPT-5-Codex | Use GPT-5-Codex |
| **gpt-4.5-preview** | Apr 14, 2025 | Jul 14, 2025 | GPT-5 | Migrate to GPT-5 |
| **o1-preview** | Apr 28, 2025 | Jul 2025 | o1/o3 | Use o1 or o3 family |
| **text-moderation** | Apr 28, 2025 | Oct 2025 | omni-moderation | Use omni-moderation (free) |
| **Operator (standalone)** | Jul 17, 2025 | Aug 31, 2025 | ChatGPT agent mode | Use agent mode in ChatGPT |

### 4.2 Rename/Merge Table

| Former Name | New Name | Date | Notes |
|-------------|----------|------|-------|
| ChatGPT Team | ChatGPT Business | Aug 29, 2025 | Pricing unchanged |
| SearchGPT | ChatGPT Search | Oct 31, 2024 | Prototype → product |
| Sora | Sora Turbo → Sora 2 | Dec 2024/Sep 2025 | Model version updates |
| Operator | ChatGPT agent mode | Jul 2025 | Full integration |
| Swarm (SDK) | Agents SDK | 2025 | Production upgrade |

### 4.3 Likely-to-Change Watchlist

| Item | Change Type | Risk Level | Recheck Frequency |
|------|-------------|------------|-------------------|
| Plus GPT-5.2 message limit (160/3hr) | Official "temporary increase" | High | Monthly |
| Sora EU/UK availability | Regulatory clearance pending | Medium | Monthly |
| Realtime API transition | Beta → GA before Feb 2026 | High | Weekly |
| gpt-image-1 vs 1.5 default | Model version standardization | Medium | Quarterly |
| Agent mode limits | Dynamic based on capacity | High | Monthly |
| o3/o4 pricing | Compute costs | Medium | Quarterly |
| Codex GitHub Actions | Feature expansion | Low | Quarterly |
| MCP connector ecosystem | Rapid expansion | Medium | Monthly |
| Enterprise credit pricing | Contract negotiations | Low | Annually |
| Voice mode limits | Capacity-based adjustments | High | Monthly |

---

## 5. CODEX & DEVELOPER-AGENT DEEP DIVE

### Interaction Modes

| Mode | Environment | Use Case | Internet |
|------|-------------|----------|----------|
| **Codex CLI (Interactive)** | Local terminal | Pair programming, local dev | Enabled |
| **Codex CLI (Headless)** | Local terminal | CI/CD, automation | Enabled |
| **Codex Cloud** | chatgpt.com/codex | Parallel tasks, GitHub integration | Disabled during execution |
| **IDE Extension** | VS Code, Cursor, JetBrains | In-editor assistance | Enabled |
| **GitHub Integration** | GitHub PR/Issues | Code review, automated fixes | Cloud sandbox |
| **Slack/Linear** | Productivity tools | Task initiation | Cloud sandbox |

### Sandbox/Permissions Model

Codex Cloud operates with **internet disabled during task execution** for security. Each task runs in an isolated container preloaded with the repository.

**Approval Modes:**
- **Suggest:** Review all changes before application
- **Auto-Edit:** Auto-apply file changes, prompt for commands
- **Full Auto:** Maximum autonomy (terminal + file changes)

**Configuration:** `~/.codex/config.toml` (shared between CLI and IDE)

### Models Available

| Model | Optimization | Use Case |
|-------|--------------|----------|
| GPT-5.2-Codex | Latest frontier | Complex reasoning, architecture |
| GPT-5-Codex | Agentic coding | General development |
| o3 | Deep reasoning | Complex problem-solving |
| gpt-4.1 | Long context | Large codebase analysis |

Configurable via `-m` flag: `codex -m o3`

### GitHub Integration Deep Dive

| Feature | Trigger | Capability |
|---------|---------|------------|
| PR Review | `@codex review` | Intent analysis, code execution, feedback |
| Task Execution | `@codex` mention in issue/PR | Cloud task with commit capabilities |
| GitHub Action | `openai/codex-action@v1` | CI/CD automation |
| AGENTS.md | Repository file | Custom per-repo instructions |

### Context Management

- **Persistent context:** Via AGENTS.md and project files
- **Session resumption:** `/resume` command
- **Compaction:** Automatic for long conversations
- **Branch support:** `codex cloud exec --branch` for isolated work

### MCP Integration

```toml
# ~/.codex/config.toml
[mcp_servers.my_server]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-example"]
```

Supports STDIO, SSE, Streamable HTTP transports.

### Codex vs Claude Code Comparison

| Aspect | OpenAI Codex | Claude Code |
|--------|--------------|-------------|
| **Primary mode** | Cloud-first, multi-interface | Terminal-first, local |
| **Execution** | Cloud sandboxed, parallelizable | Local by default |
| **Philosophy** | "Move fast, iterate" | "Measure twice, cut once" |
| **GitHub native** | Deep integration (@codex, Actions) | Manual git workflows |
| **MCP** | STDIO via config | Native HTTP support |
| **Parallelization** | Multiple cloud tasks simultaneous | Sequential focus |
| **Open source** | CLI is Apache 2.0 | Proprietary |

**Routing Rules of Thumb:**
- **Use Codex:** Quick scaffolding, parallel PR reviews, GitHub-integrated workflows
- **Use Claude Code:** Complex refactoring, investigative debugging, detailed architecture work
- **Use both:** Multi-agent verification, cross-validation of approaches

---

## 6. BROWSER / COMPUTER AGENTS

### Product Evolution Timeline

| Date | Product | Status |
|------|---------|--------|
| Jan 23, 2025 | Operator launched (Pro, US only) | Research Preview |
| Feb 1, 2025 | Operator public access | Active |
| Mar 11, 2025 | CUA API released (computer-use-preview) | Beta |
| Jul 17, 2025 | ChatGPT agent mode launched | GA |
| Aug 31, 2025 | Operator standalone shutdown | Deprecated |

### ChatGPT Agent Mode Capabilities

| Capability | Details | Restrictions |
|------------|---------|--------------|
| **Visual browser** | GUI interaction (click, type, scroll) | Watch mode on sensitive sites |
| **Text browser** | Reasoning-based queries | — |
| **Terminal** | Code execution | GET requests only for downloads |
| **File generation** | Spreadsheets, documents | — |
| **Connectors** | 60+ apps (Gmail, Drive, GitHub) | Some restricted in EEA |
| **Scheduling** | Daily/weekly/monthly tasks | Counts against limit |

**Safety Mechanisms:**
- Watch mode: Required supervision on email, banking
- Confirmation: 100% recall on financial transactions
- Blocklist: Gambling, adult content, weapons
- PII: No screenshots during user browser takeover

### Autonomy & Error Recovery

- Task duration: 5-30 minutes typical
- On-screen narration: Shows what ChatGPT is doing
- User interrupt: Can take control at any point
- Error handling: Hands back to user when stuck
- CAPTCHA: May require manual intervention

### CUA API Specification

| Parameter | Value |
|-----------|-------|
| Model | `computer-use-preview` |
| API | Responses API only (not Chat Completions) |
| Access | Tier 3-5 developers |
| Status | Beta |

**Actions:**
- `click(x, y)` - Click at coordinates
- `type(text)` - Type text
- `scroll` - Scroll actions
- `key` - Keyboard events
- Screenshot analysis via vision

**Benchmarks:**
| Benchmark | CUA Score | Claude Computer Use |
|-----------|-----------|---------------------|
| OSWorld | 38.1% | 22.0% |
| WebArena | 58.1% | — |
| WebVoyager | 87% | 56% |

---

## 7. UNIQUE CAPABILITIES VS CLAUDE

### 7.1 Pure Additive (No Claude Equivalent)

| Capability | Description | Concrete Workflow |
|------------|-------------|-------------------|
| **Sora video generation** | Text/image-to-video, 25 sec, synced audio | Marketing: Generate product explainer videos from text briefs |
| **ChatGPT Search** | Integrated real-time web search | Research: Get current events with source links inline |
| **Deep Research** | Multi-step autonomous research agent | Analysis: Comprehensive market research reports in 30 min |
| **Codex Cloud parallelization** | Multiple tasks in isolated sandboxes | Development: Review 10 PRs simultaneously |
| **GitHub @codex mentions** | Native PR/issue integration | DevOps: Automated code review on every PR |
| **ChatGPT agent mode** | Full browser automation integrated | Operations: Book appointments, order groceries autonomously |
| **60+ app connectors** | Native integrations (Slack, Drive, etc.) | Productivity: Pull context from multiple tools in conversation |
| **Voice mode video/screenshare** | Visual context in voice conversations | Support: Show your screen while voice chatting |
| **GPT Store/Apps Directory** | Custom GPT marketplace | Discovery: Find specialized tools for specific workflows |
| **AGENTS.md** | Per-repo agent configuration | Standards: Consistent agent behavior across team |

### 7.2 Overlap but Valuable for Verification

| Area | OpenAI Advantage | Claude Advantage | Use Case |
|------|------------------|------------------|----------|
| **Coding agents** | Cloud parallel execution | Deeper reasoning per task | Cross-validate complex refactors |
| **Long context** | GPT-4.1 at 1M tokens | Claude at 200K | Second opinion on large codebases |
| **Computer use** | Higher benchmarks (87% WebVoyager) | More desktop flexibility | Redundancy for critical automation |
| **Reasoning** | o3-pro for hardest problems | Claude for nuanced analysis | Ensemble on complex decisions |
| **Writing** | Canvas for collaboration | Longer form, less templated | Style diversity |

---

## 8. INTEGRATION ARCHITECTURE FOR CLAUDE-CENTRIC CONSTELLATION

### Routing Decision Tree

```
User Request
    │
    ├─► Is it video generation? ─────────────────────► OpenAI Sora
    │
    ├─► Is it real-time web search? ─────────────────► OpenAI ChatGPT Search
    │
    ├─► Is it autonomous multi-step research? ───────► OpenAI Deep Research
    │
    ├─► Is it GitHub-integrated code review? ────────► OpenAI Codex
    │
    ├─► Is it browser automation task? ──────────────► OpenAI Agent Mode
    │
    ├─► Is it multi-app workflow (Slack+Drive+...)? ─► OpenAI Connectors
    │
    ├─► Is it complex reasoning/analysis? ───────────► Claude (primary)
    │                                                   OpenAI o3-pro (verification)
    │
    ├─► Is it creative writing/nuanced? ─────────────► Claude (primary)
    │
    ├─► Is it large codebase understanding? ─────────► Claude (primary)
    │                                                   OpenAI GPT-4.1 (context window)
    │
    └─► Default coding/assistance ───────────────────► Claude Code (local)
                                                        Codex (cloud parallel)
```

### Integration Blueprint

**UI Handoffs:**
- Claude as conversational interface
- OpenAI ChatGPT for: video generation, deep research, agent tasks
- Handoff via explicit user invocation or detected capability need

**API Handoffs:**
```python
# Claude-centric orchestration pattern
from anthropic import Anthropic
from openai import OpenAI

claude = Anthropic()
openai_client = OpenAI()

def route_request(task):
    if task.needs_video:
        return openai_client.videos.create(...)
    elif task.needs_web_search:
        return openai_client.responses.create(
            tools=[{"type": "web_search"}], ...
        )
    elif task.needs_deep_research:
        # Trigger via ChatGPT UI or future API
        return redirect_to_chatgpt_deep_research(task)
    else:
        return claude.messages.create(...)
```

### Tool-Layer Strategy

**Shared Protocol (MCP):**
- OpenAI adopted MCP March 2025
- Both Claude and OpenAI can connect to same MCP servers
- Deploy MCP servers for: file systems, databases, APIs
- Single tool implementation serves both orchestrators

**Example MCP Server Setup:**
```python
# mcp_server.py - Works with both Claude and OpenAI
from mcp import FastMCP

server = FastMCP("shared-tools")

@server.tool()
def query_database(query: str) -> str:
    # Both Claude and OpenAI can call this
    return execute_query(query)
```

### Operational Concerns

| Concern | Mitigation |
|---------|------------|
| **Reliability** | Status monitoring for both providers; fallback routing |
| **Logging** | Unified logging layer capturing all API calls |
| **Privacy** | Route sensitive data to provider with appropriate guarantees |
| **Reproducibility** | Pin model versions; log full request/response |
| **Cost tracking** | Aggregate billing dashboard across providers |
| **Rate limits** | Implement circuit breakers per provider |

---

## 9. COST / VALUE MODEL

### Subscription Economics

| Plan | Monthly Cost | Key Value Prop | Break-Even vs API |
|------|--------------|----------------|-------------------|
| **Free** | $0 | Basic access, limited | N/A |
| **Go** | ~$5 | Budget option, regional | Very low usage threshold |
| **Plus** | $20 | Power user baseline | ~$20 API equivalent usage |
| **Pro** | $200 | Unlimited flagship + Sora | ~$200+ API usage (heavy video/reasoning) |
| **Business** | $25-30/seat | Team + admin | ~$30 API + management overhead |

### API Economics (Key Models)

| Model | Input $/1M | Output $/1M | 1000 queries estimate* |
|-------|------------|-------------|------------------------|
| GPT-5.2 | $1.75 | $14.00 | ~$15-20 |
| GPT-4o-mini | $0.15 | $0.60 | ~$0.75 |
| o3-pro | Higher | Higher | $50-100+ |
| gpt-image-1.5 | — | $0.01-0.17/image | $10-170 (100 images) |
| Sora | — | $0.10-0.50/sec | $100-500 (100 videos @ 10s) |

*Estimates assume average query/response sizes

### Break-Even Analysis

**Plus ($20/mo) beats API when:**
- Using >~15,000 GPT-5.2 output tokens/month
- OR generating >~120 images/month
- OR using Deep Research, agent mode, voice regularly

**Pro ($200/mo) beats API when:**
- Heavy video generation (>~500 seconds Sora/month)
- Heavy o3-pro reasoning usage
- Unlimited voice mode needed
- Deep Research power user (>50 queries/month)

### Recommended Configuration (Claude-Primary Stack)

| Use Case | Recommendation | Monthly Cost |
|----------|----------------|--------------|
| **Individual developer** | Claude Pro + OpenAI Plus | ~$40 |
| **Power user/researcher** | Claude Pro + OpenAI Pro | ~$220 |
| **Small team (5 people)** | Claude Team + OpenAI Business | ~$200-300 |
| **Enterprise** | Claude Enterprise + OpenAI Enterprise | Custom |
| **API-heavy automation** | Claude API + OpenAI API (pay-as-go) | Variable |

**Upgrade Triggers:**
- Upgrade to OpenAI Pro: Need video generation, unlimited reasoning
- Upgrade to Business: Need SSO, shared projects
- Downgrade from Pro: Not using video/unlimited features

---

## 10. APPENDICES

### A) Evidence Ledger Index

| Category | Primary Sources | Articles Reviewed |
|----------|-----------------|-------------------|
| Pricing/Plans | openai.com/pricing, chatgpt.com/pricing | 8 |
| Help Center | help.openai.com | 40+ |
| API Docs | platform.openai.com/docs | 25+ |
| Blog/Announcements | openai.com/index | 15+ |
| GitHub | github.com/openai | 20+ repos |
| Status | status.openai.com | Incident history |
| App Stores | iOS/Android/Microsoft Store | 4 listings |

### B) Source Classification

**First-Party (High Confidence):**
- platform.openai.com/docs/*
- help.openai.com/en/articles/*
- openai.com/index/*
- openai.com/pricing/*
- github.com/openai/* (official repos)

**Official Third-Party:**
- apps.apple.com (iOS app listing)
- play.google.com (Android app listing)
- apps.microsoft.com (Windows app listing)

**Community (Medium-Low Confidence):**
- community.openai.com
- Reddit (r/ChatGPT, r/OpenAI)
- Twitter/X practitioner discussions
- Tech news (TechCrunch, Ars Technica)

### C) Known Unknowns

| Unknown | Resolution Method |
|---------|-------------------|
| Exact Pro Deep Research limit | Monitor product UI; contact OpenAI |
| Enterprise custom pricing | Sales inquiry required |
| Upcoming model releases | Monitor changelog, events |
| Regional Sora timeline | Monitor official announcements |
| Realtime API GA specifications | Wait for Feb 2026 update |
| Agent mode future limits | Monitor Help Center |

### D) Re-Run Playbook

**Monthly:**
1. Check platform.openai.com/docs/changelog
2. Check help.openai.com release notes articles
3. Verify current limits match documentation
4. Monitor status.openai.com for patterns
5. Scan openai.com/index for announcements

**Quarterly:**
1. Re-fetch all pricing pages
2. Review GitHub repos for major releases
3. Update deprecation timeline
4. Verify regional availability changes
5. Check app store version histories

**On Major Events:**
- Dev Day announcements
- Model releases
- Feature launches
- Pricing changes

---

*This catalog represents OpenAI's platform ecosystem as researched January 13, 2026. Given the rapid pace of OpenAI's product development, verify critical details against current official documentation before implementation decisions.*