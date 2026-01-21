# ACCOUNT ENTITLEMENT LEDGER
## Complete Enumeration of Accounts, Services, and Constraints
**Generated**: 2026-01-17
**Purpose**: Ground truth for what you own, what each account can do, and data flow rules

---

## I. ACCOUNT OVERVIEW

| # | Account Name | Email Domain | Primary Purpose | Monthly Cost | Account Type |
|---|--------------|--------------|-----------------|--------------|--------------|
| 1 | **Personal** | @icloud.com | Synthesis, Concierge | ~$60 | Apple ecosystem |
| 2 | **Hybrid** | @gmail.com | Execution, Development | ~$45 | Google+GitHub |
| 3 | **OpenAI** | @icloud.com | Planning, Codex | ~$20 | OpenAI ecosystem |
| 4 | **Google** | @gmail.com | Sensing, Corpus | ~$20 | Google ecosystem |
| 5 | **xAI** | @icloud.com | Real-time Social | ~$0 | Free tier |

**Total Monthly Platform Spend**: ~$145

---

## II. ACCOUNT 1: PERSONAL (iCloud)

### Services

| Service | Tier | Monthly Cost | Key Features |
|---------|------|--------------|--------------|
| Claude Pro | Paid | $20 | Web app, Project Memory, Artifacts, ~45 Opus/5hr |
| Apple One | Paid | $20 | iCloud, Notes, Reminders, no AI |
| Notion | Paid | $10 | Workspace, Notion AI |
| Midjourney | Paid | $10 | Discord-based image generation |

### Platform Assignments
- **Claude-1 (Web)**: Concierge cockpit, Oracle synthesis sessions
- **Notion**: External document storage, kanban

### Hard Constraints

| Constraint | Description | Workaround |
|------------|-------------|------------|
| Cannot create YouTube channel | Apple ID limitation | Use Google account |
| Cannot use Google Workspace | No GSuite integration | Use Hybrid account |
| iCloud storage limits | 200GB (Family plan) | Archive to external |
| No filesystem access | Web app only | Export artifacts to Claude Code |

### Data Flow Rules
- **Incoming**: Public artifacts, CANON documents, Oracle contexts
- **Outgoing**: Directives, synthesis artifacts, Oracle contexts
- **Prohibited**: API keys, credentials, client PII

---

## III. ACCOUNT 2: HYBRID (Gmail)

### Services

| Service | Tier | Monthly Cost | Key Features |
|---------|------|--------------|--------------|
| Claude Pro | Paid | $20 | Claude Code CLI primary, ~45 Opus/5hr |
| Google Workspace | Free | $0 | Drive (15GB), Docs, Sheets |
| GitHub | Free | $0 | Unlimited public repos, Actions |
| Supabase | Paid | ~$25 | Database, Auth, Storage (usage-based) |

### Platform Assignments
- **Claude-2 (Code)**: Primary executor, filesystem sovereignty
- **Claude-3 (Code)**: Parallel stream executor
- **Gemini**: Via Google account connector

### Hard Constraints

| Constraint | Description | Workaround |
|------------|-------------|------------|
| Shared context | Personal + professional overlap | Maintain data separation |
| 15GB Drive limit | Shared with Gmail | Regular pruning |
| GitHub public by default | Free tier limitation | Check visibility on create |

### Special Configurations
- Claude Code: CLAUDE.md loaded from repo root
- MCP servers: filesystem, github (direct); others via gateway
- SSH access: orbit-2 (Mac Mini) for remote execution

### Data Flow Rules
- **Incoming**: Directives from Oracle, Plan packets from ChatGPT
- **Outgoing**: Execution packets, commits, continuation artifacts
- **Prohibited**: Personal PII, Apple account credentials

---

## IV. ACCOUNT 3: OPENAI (iCloud)

### Services

| Service | Tier | Monthly Cost | Key Features |
|---------|------|--------------|--------------|
| ChatGPT Plus | Paid | $20 | Web, Canvas, Agent Mode, Deep Research |
| Codex CLI | Included | $0 | GitHub integration |
| DALL-E | Included | $0 | Image generation (limits) |

### Platform Assignments
- **ChatGPT (Deviser)**: Planning, specification, audit
- **Codex CLI**: GitHub-specific operations only

### Rate Limits (NEEDS VERIFICATION)

| Feature | Limit | Reset Period | Confidence |
|---------|-------|--------------|------------|
| Instant messages | ~160 | 3 hours | Medium |
| Thinking messages | ~3000 | Weekly | Low |
| Agent Mode tasks | ~40 | Monthly | **UNKNOWN** |
| Deep Research | Unclear | Per query | **UNKNOWN** |

### Hard Constraints

| Constraint | Description | Workaround |
|------------|-------------|------------|
| Thinking quota | Weekly limit on o-series | Batch strategic work |
| Agent Mode limit | Monthly cap | Reserve for high-value |
| GitHub-only (Codex) | Cannot access local repos | Use Claude Code |
| Memory fragmentation | Memory unreliable | Rely on repo artifacts |

### Data Flow Rules
- **Incoming**: Evidence packets from Gemini, execution for audit
- **Outgoing**: Plan packets to Claude Code, audit packets to repo
- **Prohibited**: Repository write access, sensitive credentials

---

## V. ACCOUNT 4: GOOGLE (Gmail)

### Services

| Service | Tier | Monthly Cost | Key Features |
|---------|------|--------------|--------------|
| Gemini Advanced | Paid | $20 | 2M context, Deep Research, liberal limits |
| NotebookLM | Free | $0 | 50 sources/notebook, grounded RAG |
| AI Studio | Free tier | $0 | API access, rate limited |
| YouTube Premium | Family | ~$0 | No ads, background play |

### Platform Assignments
- **Gemini (Oracle)**: Corpus-scale sensing, video processing
- **NotebookLM**: Grounded RAG, source verification

### Hard Constraints

| Constraint | Description | Workaround |
|------------|-------------|------------|
| Personal Intelligence | US-only beta | VPN if needed |
| NotebookLM isolation | 50 sources per notebook | Multiple notebooks |
| Gemini sees all Google data | Privacy consideration | Use for non-sensitive |
| No project memory | Unlike Claude | Use Drive for continuity |

### Service Creation Rights

| Action | Allowed | Notes |
|--------|---------|-------|
| Create YouTube channel | Yes | Via Google account |
| Create Drive folders | Yes | Limited to 15GB |
| Create NotebookLM notebooks | Yes | 50 sources each |
| Create Gemini Gems | Yes | Custom agents possible |

### Data Flow Rules
- **Incoming**: Corpus files via Drive, video URLs
- **Outgoing**: Evidence packets, research findings
- **Prohibited**: Client confidential data (Gemini trains on inputs)

---

## VI. ACCOUNT 5: XAI (iCloud)

### Services

| Service | Tier | Monthly Cost | Key Features |
|---------|------|--------------|--------------|
| Grok Web | Free | $0 | Real-time queries, X integration |
| Grok Voice API | Pay-per-use | ~$0.05/min | Voice agents |

### Platform Assignments
- **Grok (Sensor)**: Real-time intelligence, social temperature

### Hard Constraints

| Constraint | Description | Workaround |
|------------|-------------|------------|
| Free tier limits | **UNPUBLISHED** | Monitor for walls |
| X/Twitter bias | Training data skew | Cross-check with Perplexity |
| Voice API billing | Requires setup | Set up if needed |
| No memory | Stateless | Provide context each time |

### Data Flow Rules
- **Incoming**: Query context
- **Outgoing**: Real-time findings (not archived)
- **Prohibited**: Sensitive queries (no privacy guarantees)

---

## VII. CROSS-ACCOUNT CONSTRAINTS

### Data Flow Matrix

| From → To | Personal | Hybrid | OpenAI | Google | xAI |
|-----------|----------|--------|--------|--------|-----|
| **Personal** | — | Non-sensitive | Non-sensitive | Non-sensitive | Query only |
| **Hybrid** | Public outputs | — | Plans | Research | Query only |
| **OpenAI** | Plans, audits | Plans, audits | — | Plans | None |
| **Google** | Anon research | Research | Evidence | — | None |
| **xAI** | Findings | Findings | None | None | — |

### Never Cross These Boundaries

| Data Type | Prohibited Destinations | Why |
|-----------|-------------------------|-----|
| API keys | Any non-local | Exposure risk |
| Client PII | Any cloud AI | Privacy breach |
| Passwords | Any surface | Credential exposure |
| Private repo contents | Google (Gemini trains) | IP exposure |

### Service Integration Matrix

| Service A | Service B | Integration Method | Notes |
|-----------|-----------|-------------------|-------|
| Claude Code | GitHub | MCP or CLI direct | Bidirectional |
| Claude Code | Drive | Local sync folder | Manual setup |
| Gemini | Drive | Native connector | Built-in |
| ChatGPT | GitHub | Via Codex | GitHub repos only |
| NotebookLM | Drive | Upload | Manual, one-way |
| All | Repository | Ground truth | Authoritative |

---

## VIII. ENTITLEMENTS BY ROLE

### Oracle Role (Sensing)
| Entitlement | Platform | Status |
|-------------|----------|--------|
| 2M context window | Gemini | Yes |
| Video processing | Gemini | Yes |
| Grounded RAG | NotebookLM | Yes |
| Drive visibility | Gemini | Yes |
| Real-time web | Gemini, Grok, Perplexity | Yes |

### Deviser Role (Planning)
| Entitlement | Platform | Status |
|-------------|----------|--------|
| Long-horizon planning | ChatGPT | Yes |
| Deep Research | ChatGPT | Yes |
| Canvas editing | ChatGPT | Yes |
| Structured spec output | ChatGPT | Yes |

### Executor Role (Implementation)
| Entitlement | Platform | Status |
|-------------|----------|--------|
| Filesystem write | Claude Code | Yes |
| Git operations | Claude Code | Yes |
| Script execution | Claude Code | Yes |
| MCP tool access | Claude Code | Yes |
| Constitutional governance | Claude Code | Yes |

### Concierge Role (Governance)
| Entitlement | Platform | Status |
|-------------|----------|--------|
| Project memory | Claude Web | Yes |
| Extended thinking | Claude Web | Yes |
| Artifact creation | Claude Web | Yes |
| Session continuity | Claude Web | Via projects |

---

## IX. UNKNOWNS REQUIRING CONFIRMATION

### High Priority (Affects Daily Operations)

| Unknown | Current Assumption | How to Verify | Impact if Wrong |
|---------|-------------------|---------------|-----------------|
| ChatGPT Agent Mode limit | ~40/month | Test or OpenAI docs | May run out mid-month |
| Grok free tier limits | Liberal | Hit walls and observe | Sudden degradation |
| Gemini Personal Intelligence | US-only | Test from location | Feature unavailable |

### Medium Priority (Affects Planning)

| Unknown | Current Assumption | How to Verify | Impact if Wrong |
|---------|-------------------|---------------|-----------------|
| NotebookLM Plus pricing | TBD | Watch for announcement | May not be worth cost |
| Supabase actual spend | ~$25/month | Check billing | Budget variance |
| Claude Code Opus limit | ~45/5hr | Monitor usage | May need to tier down |

### Low Priority (Nice to Know)

| Unknown | Current Assumption | How to Verify | Impact if Wrong |
|---------|-------------------|---------------|-----------------|
| Midjourney v7 features | Coming soon | Watch announcements | Workflow changes |
| Codex CLI improvements | Stable | Monitor OpenAI | Capability gains |

---

## X. UPGRADE CONSIDERATIONS

### High Value (Consider)

| Upgrade | Cost | Value Add | Decision |
|---------|------|-----------|----------|
| Gemini Business | ~$20/month | Team features, higher limits | Low (solo use) |
| Perplexity Pro | $20/month | Better research, higher limits | Medium (if hitting walls) |

### Low Value (Avoid)

| Service | Reason to Skip |
|---------|----------------|
| Claude Team | Redundant for solo |
| ChatGPT Pro ($200) | Cost prohibitive |
| Multiple ChatGPT accounts | Limits don't stack |
| Cursor/Windsurf | Fragments execution surface |

---

## XI. SECURITY CHECKLIST

### Credential Storage
| Type | Location | Access Pattern |
|------|----------|----------------|
| API keys | Environment variables | Never in repo |
| OAuth tokens | System keychain | Auto-refresh |
| SSH keys | ~/.ssh | Per-machine |
| Passwords | Password manager | Never in chat |

### Data Classification
| Type | Allowed Platforms | Notes |
|------|-------------------|-------|
| Personal PII | Local only | Never cloud AI |
| Client data | Local + encrypted | Never cloud AI |
| Public research | All | No restrictions |
| Repo content | Claude Code, carefully Gemini | Exclude sensitive |

---

## XII. RECOVERY PROCEDURES

### If Account Locked
1. **Claude**: Contact Anthropic, use alternate account
2. **OpenAI**: Password reset via backup email
3. **Google**: Recovery phone/email, security keys
4. **Notion**: Team recovery or personal backup

### If Service Degraded
1. Route work to alternate platform
2. Document in events.jsonl
3. Adjust routing rules temporarily
4. Return to primary when resolved

---

**This ledger is the source of truth for account capabilities. Update when entitlements change.**
