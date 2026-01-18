# Accounts and Entitlements v2
**Generated**: 2026-01-17T04:55:00Z
**Purpose**: Account boundaries, service constraints, and entitlement mapping

---

## Account Overview

| Account | Email Domain | Primary Use | Monthly Cost | Constraint Notes |
|---------|--------------|-------------|--------------|------------------|
| **Personal (iCloud)** | @icloud.com | Primary personal, synthesis | ~$60 | Apple ecosystem integration |
| **Hybrid (Gmail)** | @gmail.com | Execution, development | ~$45 | Google Workspace, Claude Code |
| **OpenAI** | @icloud.com | Planning, Codex CLI | ~$20 | ChatGPT Plus |
| **Google** | @gmail.com | Gemini, Drive, YouTube | ~$20 | Full Google ecosystem |
| **xAI** | @icloud.com | Real-time sensing | ~$0 | Free tier currently |

**Total Monthly Platform Spend**: ~$145

---

## Account 1: Personal (iCloud)

### Services

| Service | Tier | Features Enabled | Constraints |
|---------|------|------------------|-------------|
| Claude Pro | Paid | Web app, Project Memory, Artifacts | ~45 Opus/5hr |
| Apple One | Paid | iCloud, Notes, Reminders | No AI integration |
| Notion | Paid | Workspace, Notion AI | Single workspace |
| Midjourney | Paid | Image generation | Discord-based |

### Account-Level Constraints
- Cannot create YouTube channels (Apple ID limitation)
- Cannot use Google Workspace features
- iCloud storage limits apply to exports

### Platform Assignment
- Claude-1 (Synthesizer): Primary strategic synthesis
- ChatGPT Deviser: Planning and specification

---

## Account 2: Hybrid (Gmail)

### Services

| Service | Tier | Features Enabled | Constraints |
|---------|------|------------------|-------------|
| Claude Pro | Paid | Claude Code CLI primary | ~45 Opus/5hr |
| Google Workspace | Free | Drive, Docs, Sheets | 15GB storage |
| GitHub | Free | Repos, Actions | Public repos unlimited |
| Supabase | Paid | Database, Auth, Storage | Usage-based |

### Account-Level Constraints
- Shared between personal and professional contexts
- Must maintain data separation discipline
- GitHub requires care about public/private

### Platform Assignment
- Claude-2 (Engineer): Primary execution
- Gemini (via Google): Corpus sensing

### Special Configurations
- Claude Code CLAUDE.md loaded from repo
- MCP servers configured for extended tools
- SSH access to orbit-2 (Mac Mini)

---

## Account 3: OpenAI (iCloud)

### Services

| Service | Tier | Features Enabled | Constraints |
|---------|------|------------------|-------------|
| ChatGPT Plus | Paid | Web, Canvas, Agent Mode, Deep Research | ~160 instant/3hr |
| Codex CLI | Included | GitHub integration | GitHub repos only |
| DALL-E | Included | Image generation | Usage limits |

### Account-Level Constraints
- Thinking mode has weekly quotas (~3K messages)
- Agent Mode limited to ~40/month on Plus tier
- Deep Research has rate limits

### Platform Assignment
- ChatGPT (Deviser): Planning, specification, audit
- Codex CLI: GitHub-specific operations

### Feature-Specific Limits
| Feature | Limit | Reset |
|---------|-------|-------|
| Instant messages | ~160 | 3 hours |
| Thinking messages | ~3000 | Weekly |
| Agent Mode tasks | ~40 | Monthly |
| Deep Research | Unclear | Per query |

---

## Account 4: Google (Gmail)

### Services

| Service | Tier | Features Enabled | Constraints |
|---------|------|------------------|-------------|
| Gemini Advanced | Paid | 2M context, Deep Research | Liberal limits |
| NotebookLM | Free | 50 sources/notebook | US only |
| AI Studio | Free tier | API access | Rate limited |
| YouTube Premium | Paid | No ads, background play | Via family plan |
| Drive | Free | 15GB | Shared with Gmail |

### Account-Level Constraints
- Personal Intelligence requires US location
- NotebookLM notebooks are project-isolated
- Gemini sees all Google data (privacy consideration)

### Platform Assignment
- Gemini (Oracle): Corpus-scale sensing
- NotebookLM: Grounded RAG

### Service Creation Constraints
| Action | Allowed? | Notes |
|--------|----------|-------|
| Create YouTube channel | Yes | Via Google account |
| Create Drive folders | Yes | Limited storage |
| Create NotebookLM notebooks | Yes | 50 sources each |
| Create Gemini Gems | Yes | Custom agents |

---

## Account 5: xAI (iCloud)

### Services

| Service | Tier | Features Enabled | Constraints |
|---------|------|------------------|-------------|
| Grok Web | Free | Real-time queries, X integration | Usage limits unclear |
| Grok Voice API | Pay-per-use | Voice agents | $0.05/minute |

### Account-Level Constraints
- Free tier may have unpublished limits
- Voice API requires billing setup
- X/Twitter bias in training

### Platform Assignment
- Grok: Real-time sensing, social temperature

---

## Cross-Account Constraints

### Data Flow Restrictions

| From Account | To Account | Allowed Data | Prohibited |
|--------------|------------|--------------|------------|
| Personal | Hybrid | Non-sensitive artifacts | Credentials, PII |
| Hybrid | Personal | Public outputs | API keys, tokens |
| Google | Any | Anonymized research | Personal data |
| OpenAI | Any | Plans, audits | Chat history |

### Service Interaction Matrix

| Service A | Service B | Integration | Notes |
|-----------|-----------|-------------|-------|
| Claude Code | GitHub | Direct | MCP or CLI |
| Claude Code | Drive | Via sync | Local folder synced |
| Gemini | Drive | Native | Built-in connector |
| ChatGPT | GitHub | Via Codex | GitHub-only |
| NotebookLM | Drive | Upload | Manual upload required |

---

## Entitlement Summary by Role

### Oracle (Gemini/NotebookLM)

| Entitlement | Status | Source |
|-------------|--------|--------|
| 2M context window | Yes | Gemini Advanced |
| Video processing | Yes | Gemini |
| Grounded RAG | Yes | NotebookLM |
| Drive visibility | Yes | Google connector |
| Real-time web | Yes | Gemini |

### Deviser (ChatGPT)

| Entitlement | Status | Source |
|-------------|--------|--------|
| Long-horizon planning | Yes | GPT-5.2 Thinking |
| Deep Research | Yes | ChatGPT Plus |
| Canvas editing | Yes | ChatGPT Plus |
| Audit capability | Yes | Structured prompting |

### Executor (Claude Code)

| Entitlement | Status | Source |
|-------------|--------|--------|
| Filesystem write | Yes | Claude Code CLI |
| Git operations | Yes | Bash tool |
| Script execution | Yes | Bash tool |
| MCP tools | Yes | Configuration |
| Constitutional governance | Yes | CLAUDE.md |

### Sensor (Perplexity/Grok)

| Entitlement | Status | Source |
|-------------|--------|--------|
| Real-time web search | Yes | Both |
| Citation generation | Yes | Perplexity |
| Social sensing | Yes | Grok/X |

---

## Upgrade Considerations

### High-Value Upgrades

| Upgrade | Cost | Value | Priority |
|---------|------|-------|----------|
| Gemini Business | ~$20/month | Team features, API | Low (solo use) |
| NotebookLM Plus | Unknown | Higher limits | Medium |
| ChatGPT Pro | $200/month | Unlimited, o1 | Low (cost prohibitive) |

### Low-Value/Avoid

| Service | Reason to Avoid |
|---------|-----------------|
| Claude Team | Solo use, redundant |
| Multiple ChatGPT accounts | Rate limit doesn't stack |
| Cursor/Windsurf | Fragments execution surface |

---

## Security Considerations

### Credential Isolation

| Credential Type | Storage Location | Access Pattern |
|-----------------|------------------|----------------|
| API keys | Environment variables | Never in repo |
| OAuth tokens | System keychain | Automatic refresh |
| SSH keys | ~/.ssh | Per-machine |
| Service passwords | Password manager | Never in chat |

### Data Classification

| Data Type | Allowed Platforms | Prohibited Platforms |
|-----------|-------------------|----------------------|
| Personal PII | Local only | All cloud AI |
| Client data | Local + encrypted | All cloud AI |
| Public research | All platforms | None |
| Repo content | Claude Code, Gemini (via Drive) | Sensitive exclusions |

---

## Account Recovery Procedures

### If Account Locked

1. **Claude**: Contact Anthropic support, use alternate account
2. **OpenAI**: Password reset, use backup email
3. **Google**: Recovery phone/email, security keys
4. **Notion**: Team recovery or personal backup

### If Service Degraded

1. Route work to alternate platform
2. Document degradation in events.jsonl
3. Adjust routing rules temporarily
4. Return to primary when resolved
