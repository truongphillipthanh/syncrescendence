# Accounts and Entitlements Ledger
**Generated**: 2026-01-17T03:23:54Z
**Total Monthly**: $100

---

## Account Inventory

### Account 1: Personal (Claude Pro)
**Email**: [personal email]
**Platform**: Claude (Anthropic)
**Tier**: Pro ($20/month)
**Role in System**: Oracle/Synthesizer

**Entitlements**:
| Feature | Included | Notes |
|---------|----------|-------|
| Claude Web App | Yes | Project memory, artifacts |
| Claude Cowork | Yes | Sandboxed desktop automation |
| Extended Thinking | Yes | Opus 4.5, Sonnet 4 |
| Project Memory | Yes | Cross-session persistence |
| MCP Support | Limited | Web app doesn't support CLI MCP |
| Rate Limit | ~45 Opus/5hr | ~100 Sonnet/5hr |

**Primary Uses**:
- Oracle sessions (strategic synthesis)
- Directive generation
- Long-form analysis
- Claude Cowork desktop tasks

**Constraints**:
- Cannot execute code on repo
- Artifacts require manual export
- No direct filesystem access

---

### Account 2: Hybrid (Claude Pro)
**Email**: [hybrid email]
**Platform**: Claude (Anthropic)
**Tier**: Pro ($20/month)
**Role in System**: Primary Executor (Alpha)

**Entitlements**:
| Feature | Included | Notes |
|---------|----------|-------|
| Claude Code CLI | Yes | Filesystem-native execution |
| Extended Thinking | Yes | Opus 4.5, Sonnet 4 |
| MCP Servers | Yes | Full connector ecosystem |
| Tool Execution | Yes | Bash, file operations |
| Rate Limit | ~45 Opus/5hr | ~100 Sonnet/5hr |

**Primary Uses**:
- Directive execution (Stream A)
- Code generation
- File manipulation
- Verification commands

**Constraints**:
- No web app project memory integration
- Session context resets on new session
- macOS requirement for Claude Code

**Zone Ownership**:
- `04-SOURCES/processed/a-*`
- `00-ORCHESTRATION/logs/*-A.md`

---

### Account 3: Gmail (Claude Pro)
**Email**: [gmail address]
**Platform**: Claude (Anthropic)
**Tier**: Pro ($20/month)
**Role in System**: Parallel Executor (Beta) / Auditor

**Entitlements**:
| Feature | Included | Notes |
|---------|----------|-------|
| Claude Code CLI | Yes | Parallel execution |
| Extended Thinking | Yes | For complex verification |
| MCP Servers | Yes | Shared connector ecosystem |
| Tool Execution | Yes | Parallel stream capability |
| Rate Limit | ~45 Opus/5hr | Independent of Account 2 |

**Primary Uses**:
- Parallel directive execution (Stream B)
- Cross-validation of Account 2 outputs
- Verification and audit tasks
- Backup execution capacity

**Constraints**:
- Same as Account 2
- Must coordinate via repository (no direct communication)

**Zone Ownership**:
- `04-SOURCES/processed/b-*`
- `00-ORCHESTRATION/logs/*-B.md`

---

### Account 4: Google (Gemini Advanced)
**Email**: [google account]
**Platform**: Gemini (Google)
**Tier**: Advanced ($20/month)
**Role in System**: Oracle (Sensing Layer)

**Entitlements**:
| Feature | Included | Notes |
|---------|----------|-------|
| Gemini Web App | Yes | 2M context window |
| Personal Intelligence | Beta (US) | Cross-service synthesis |
| NotebookLM | Yes | Zero-hallucination RAG |
| Google Drive Connector | Yes | Repo visibility |
| Video Processing | Yes | 263 tok/sec native |
| Veo 3.1 Fast | Yes | Video generation |
| Jules (coding agent) | Beta | Async GitHub operations |
| Rate Limit | Liberal | Less restrictive than Claude |

**Primary Uses**:
- Corpus-scale queries
- Video transcription and processing
- YouTube monitoring
- Evidence packet generation
- NotebookLM audio overviews

**Constraints**:
- No project-scoped memory isolation
- Personal Intelligence is US-only
- Cannot execute on local filesystem

---

### Account 5: OpenAI (ChatGPT Plus)
**Email**: truongphillipthanh@icloud.com
**Platform**: ChatGPT (OpenAI)
**Tier**: Plus ($20/month)
**Role in System**: Deviser (Planning/Audit)

**Entitlements**:
| Feature | Included | Notes |
|---------|----------|-------|
| ChatGPT Web App | Yes | GPT-5.2 Instant |
| GPT-5.2 Thinking | Yes | ~3K/week thinking quota |
| Agent Mode | Yes | 40 tasks/month |
| Codex CLI | Yes | GitHub integration |
| Deep Research | Yes | Multi-pass external research |
| Canvas | Yes | Collaborative editing |
| Health | Yes (US) | Isolated health memory |
| Rate Limit | ~160 Instant/3hr | Thinking limited weekly |

**Primary Uses**:
- Plan packet generation
- Specification authoring
- Audit packet generation
- Deep Research for external intel
- GitHub workflow management via Codex

**Constraints**:
- Memory fragmentation across silos
- Thinking quota limits complex planning
- Agent mode has monthly task limit
- Cannot access local filesystem directly

---

## Monthly Cost Breakdown

| Account | Platform | Tier | Cost |
|---------|----------|------|------|
| Personal | Claude | Pro | $20 |
| Hybrid | Claude | Pro | $20 |
| Gmail | Claude | Pro | $20 |
| Google | Gemini | Advanced | $20 |
| OpenAI | ChatGPT | Plus | $20 |
| **TOTAL** | | | **$100** |

---

## Sustainability Target

**Target Date**: 2026-01-31
**Condition**: System must demonstrate value exceeding $100/month operational cost

**Value Metrics**:
- Sources processed per month
- Canon integrations completed
- Autonomous cycles without Principal intervention
- Relay reduction ratio (autonomous vs manual)

---

## Entitlement Gaps

| Need | Current State | Gap |
|------|---------------|-----|
| Enterprise audit logs | Not available on Pro tiers | Claude Cowork activity unauditable |
| Cross-platform memory | Each platform isolated | Manual context graduation required |
| Unified billing | 5 separate subscriptions | No consolidated billing |
| API access | Limited without separate API keys | Additional cost for programmatic access |
