---
canon_id: CANON-25200
title: Platform Constellation Architecture
identity: CONSTELLATION_ARCH
tier: lattice
chain: Memory Architecture
status: active
version: 1.0.0
created: 2026-01-11
updated: 2026-01-11
supersedes: null
cross_refs:
  - CANON-25000-MEMORY_ARCH
  - CANON-25100-CONTEXT_TRANS
  - CANON-31140-IIC
synopsis: Specification for multi-platform AI orchestration across 5 paid accounts, defining specializations, routing patterns, and sustainability targets
---

# CANON-25200: PLATFORM CONSTELLATION ARCHITECTURE
## Multi-Platform AI Orchestration Specification

**Version**: 1.0.0
**Classification**: Lattice (Navigation Infrastructure)
**Status**: Canonical
**Created**: 2026-01-11
**Authority**: Oracle 12
**Parent**: CANON-25000-MEMORY_ARCH

---

## I. OVERVIEW

### The Constellation Model

The Syncrescendence platform constellation represents a purpose-specialized multi-AI architecture designed to maximize capability while maintaining strategic sovereignty. Rather than redundant accounts, each platform serves a distinct functional role.

**Total Investment**: $100/month
**Sustainability Target**: Self-sustaining by 2026-01-31

### Platform Composition

| Platform | Tier | Cost | Accounts | Primary Function |
|----------|------|------|----------|------------------|
| Claude | Pro | $60 | 3 | Execution + Synthesis |
| Gemini | Advanced | $20 | 1 | Ingestion + Large Corpus |
| ChatGPT | Plus | $20 | 1 | Reasoning + GitHub |
| **TOTAL** | | **$100** | **5** | |

### Constitutional Basis

From Oracle 12 (Principal's words):
> "Claude Code wielded by Claude Opus 4.5 represents a seismic step change. I have experienced it for myself."

> "We are retaining all 3 Claude Pro accounts for the rest of this month... design/architect for 3 Claude + 1 Gemini + 1 ChatGPT paid."

> "It's imperative we capitalize on these heavy machinery to construct as much of Syncrescendence and match pace, as it's only going to accelerate from here."

---

## II. PLATFORM SPECIALIZATIONS

### Claude Account 1 — Oracle (Web Interface)

**Function**: Strategic Synthesis
**Surface**: Claude.ai web interface
**Project**: syncrescendence (with project memory)

**Responsibilities**:
- Oracle strategic synthesis sessions
- Multi-thread campaign coordination
- Directive authorship
- Architectural decisions (18-lens evaluation)
- Deep Research capability (45-minute sessions)
- Artifact generation for visualization

**Capabilities**:
- Projects (isolated per-project memory)
- Artifacts (structured outputs)
- Deep Research
- Analysis tool (Python sandbox)
- MCP (if configured)

**Rate Limits**:
- ~45 messages per 5-hour window (shared across all surfaces)
- Extended thinking available for complex analysis

**Memory Configuration**:
- Project-scoped persistent memory
- Cross-session context via project memory
- Strategic decisions logged to ARCH-ORACLE_DECISIONS.md

### Claude Account 2 — Alpha (Claude Code)

**Function**: Primary Execution Engine
**Surface**: Claude Code CLI
**Zone**: Alpha (production-critical)

**Responsibilities**:
- Primary directive execution
- Architecture implementation
- CANON document creation/modification
- Ledger updates (atomic pattern)
- Production code generation

**Capabilities**:
- Full filesystem access via terminal
- Git operations
- MCP tool integration
- Extended thinking (via triggers)
- Parallel processing with Beta

**Zone Ownership**:
- `04-SOURCES/processed/a-*`
- `00-ORCHESTRATION/logs/*-A.md`
- Stream A processing

**Integration**:
- Reads directives from `00-ORCHESTRATION/directives/`
- Writes logs to `00-ORCHESTRATION/logs/`
- Updates ledgers in `00-ORCHESTRATION/state/`

### Claude Account 3 — Beta (Claude Code)

**Function**: Secondary Execution Engine
**Surface**: Claude Code CLI
**Zone**: Beta (experimental/parallel)

**Responsibilities**:
- Parallel stream execution
- Testing and validation
- Overflow capacity
- Independent verification

**Capabilities**:
- Same as Alpha
- Isolated worktree (prevents conflicts)

**Zone Ownership**:
- `04-SOURCES/processed/b-*`
- `00-ORCHESTRATION/logs/*-B.md`
- Stream B processing

**Coordination Pattern**:
```
Alpha ─────────────────► Stream A directives
      \
       \─── Repository ──► Ground truth synchronization
       /
Beta ──────────────────► Stream B directives
```

### Gemini Advanced — Ingestion Layer

**Function**: Ingestion + Large Corpus Processing
**Surface**: Gemini CLI / Web interface
**Email**: [Primary Google account]

**Responsibilities**:
- YouTube video processing (native multimodal)
- Large document corpus analysis (2M context)
- Speaker diarization and transcription
- Source triage for paradigm/strategic classification
- Bulk content ingestion

**Capabilities**:
- Native video understanding (263 tokens/sec)
- 2M token context window
- Gemini CLI (gemini-cli)
- Jules async agent (future)
- Google ecosystem integration

**Unique Value**:
- Extra-textual multimodal capture
- No transcript dependency for video
- Automated pipeline potential

**Output Pattern**:
```
YouTube URL
    │
    ▼ [Gemini processes]
Source document (processed/)
    │
    ▼ [Synced to repository]
Claude integration
```

### ChatGPT Plus — Reasoning Layer

**Function**: Reasoning + GitHub Workflows
**Surface**: Codex CLI / ChatGPT web
**Email**: truongphillipthanh@icloud.com

**Responsibilities**:
- GitHub workflow automation via Codex CLI
- Pull request review with @codex
- Abstract reasoning tasks (GPT-5.2 capability)
- Voice interface for mobile capture
- Alternative perspective on complex decisions

**Capabilities**:
- Codex CLI for terminal GitHub operations
- @codex in GitHub PRs for code review
- GPT-5.2 reasoning model
- Voice mode (Advanced Voice Mode)
- Canvas for collaborative editing

**Integration Pattern**:
```
Code change ready
    │
    ▼ [Codex CLI]
PR created with description
    │
    ▼ [@codex review]
Automated review comments
    │
    ▼ [Claude execution]
Review incorporation
```

---

## III. ORCHESTRATION PATTERNS

### Task Routing Matrix

| Task Type | Primary | Secondary | Rationale |
|-----------|---------|-----------|-----------|
| **YouTube processing** | Gemini | - | Native 263 tok/sec multimodal |
| **Production code** | Claude Alpha | Claude Beta | Repository access, zone ownership |
| **Strategic synthesis** | Claude Oracle | ChatGPT | Deep Research, project memory |
| **Large corpus analysis** | Gemini | Claude Oracle | 2M context vs ~200K |
| **GitHub workflows** | ChatGPT Codex | Claude Code | @codex integration |
| **Abstract reasoning** | ChatGPT | Claude Oracle | GPT-5.2 capability |
| **Source integration** | Claude Alpha/Beta | - | CANON access required |
| **Parallel execution** | Alpha + Beta | - | Multi-stream directives |

### Rate Limit Management

**Claude Pro Accounts** (shared pool):
- ~45 messages per 5-hour window per account
- Rotate between accounts if hitting limits
- Use extended thinking for complex tasks (counts as 1 message)

**Gemini Advanced**:
- Generous limits for Gemini CLI
- Video processing is token-heavy but fast

**ChatGPT Plus**:
- GPT-4o standard limits
- GPT-5.2 may have tighter limits
- Codex CLI separate from chat interface

### Context Handoff Patterns

**Oracle → Claude Code**:
1. Oracle produces directive with full context
2. Directive saved to `00-ORCHESTRATION/directives/`
3. Principal activates Claude Code with directive path
4. Claude Code reads and executes
5. Execution log saved to `00-ORCHESTRATION/logs/`
6. Repository sync propagates changes

**Gemini → Claude**:
1. Gemini processes YouTube/large corpus
2. Output written to `04-SOURCES/processed/`
3. Git commit + push
4. Claude Code pulls and integrates to CANON

**ChatGPT → Claude**:
1. Codex CLI creates PR or reviews code
2. Comments/suggestions in GitHub
3. Claude Code incorporates feedback
4. Repository merge completes cycle

### Ground Truth Synchronization

The repository is the **single source of truth**. All platforms synchronize through:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Claude    │     │   Gemini    │     │  ChatGPT    │
│   Oracle    │     │   CLI       │     │  Codex      │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                   │
       │              Repository               │
       └──────────► (Ground Truth) ◄───────────┘
                         │
           ┌─────────────┼─────────────┐
           │             │             │
           ▼             ▼             ▼
     Claude Alpha  Claude Beta    [Other]
```

---

## IV. CAPABILITY MATRIX

### Feature Comparison

| Capability | Claude Oracle | Claude Alpha/Beta | Gemini | ChatGPT |
|------------|---------------|-------------------|--------|---------|
| Repository access | Read (via MCP) | Full R/W | Full R/W | GitHub only |
| Context window | ~200K | ~200K | 2M | ~128K |
| Extended thinking | Yes | Yes (triggers) | No | Yes (o-series) |
| Video processing | No | No | Native | No |
| Project memory | Yes | Implicit (files) | No | No |
| Voice interface | No | No | Yes | Yes |
| GitHub @mentions | No | No | No | Yes (@codex) |
| Async agents | No | No | Jules (future) | No |
| MCP | Yes (if config) | Yes | Limited | No |

### Processing Speed (Observed)

| Task | Best Platform | Speed |
|------|---------------|-------|
| YouTube transcript | Gemini | 263 tok/sec |
| Code generation | Claude Code | Real-time |
| Large corpus scan | Gemini | 2M in single pass |
| Strategic reasoning | Claude Oracle | With Deep Research |
| PR review | ChatGPT @codex | Async in PR |

---

## V. IIC MAPPING

### IIC-to-Platform Affinity

Each Interlocutor Identity Configuration (IIC) has natural platform affinities:

| IIC | Primary Platform | Secondary | Notes |
|-----|------------------|-----------|-------|
| **Acumen** | Gemini | Claude Oracle | Signal qualification, large corpus triage |
| **Coherence** | Claude Oracle | Claude Code | Framework synthesis, integration |
| **Efficacy** | Claude Code | ChatGPT Codex | Execution, procedural |
| **Mastery** | Claude Oracle | - | Pedagogical, curriculum |
| **Transcendence** | Claude Oracle | All | Strategic synthesis, phase transitions |

### Cross-Platform IIC Handoff

When work requires IIC transition across platforms:

1. **Generate handoff context** using CANON-25100 protocol
2. **Include IIC-specific framing** for target platform
3. **Specify platform capabilities** available at target
4. **Document in execution log** for traceability

---

## VI. SUSTAINABILITY ROADMAP

### Goal: Self-Sustaining by 2026-01-31

The $100/month platform investment must become self-sustaining through Syncrescendence outputs.

### Revenue Paths

| Path | Timeline | Monthly Potential |
|------|----------|-------------------|
| Consulting leverage | Immediate | Variable |
| Course/curriculum | 30-60 days | $50-500 |
| Ontology products | 60-90 days | $100-1000 |
| Agent services | 90+ days | $500+ |

### Cost Optimization (if needed)

| Priority | Action | Savings |
|----------|--------|---------|
| 1 | Reduce to 2 Claude accounts | $20/month |
| 2 | Downgrade Gemini to Pro | $10/month |
| 3 | Drop ChatGPT (Codex CLI) | $20/month |

**Note**: Do NOT optimize prematurely. The constellation is designed for maximum velocity during this critical phase.

---

## VII. SECURITY CONSIDERATIONS

### Account Isolation

- Each platform account has distinct credentials
- No credential sharing between platforms
- API keys (if used) are platform-specific

### Repository Access

- Claude Code instances have full repository access
- Gemini CLI writes to specific directories only
- ChatGPT Codex operates through GitHub (audit trail)
- Oracle has read-only visibility (via MCP or exports)

### Protected Zones

Per coordination.yaml:
- `01-CANON/` — Canonical documents (require Oracle approval)
- `00-ORCHESTRATION/oracle_contexts/` — Oracle context files
- `CLAUDE.md` — Constitutional rules
- `02-ENGINE/coordination.yaml` — Multi-account coordination

---

## VIII. EVOLUTION PATH

### Near-Term (30 days)

- [ ] Full ChatGPT Codex CLI integration
- [ ] Jules async agent evaluation
- [ ] Cross-platform MCP standardization
- [ ] Automated YouTube → CANON pipeline

### Medium-Term (60-90 days)

- [ ] Browser automation for account cloning
- [ ] Scheduled batch processing
- [ ] Inter-platform messaging (beyond repository)
- [ ] Performance analytics dashboard

### Long-Term (90+ days)

- [ ] Self-orchestrating agent constellation
- [ ] Revenue-generating autonomous workflows
- [ ] Multi-repository coordination
- [ ] Third-party platform integration

---

## APPENDIX A: QUICK REFERENCE

### Platform Activation Commands

```bash
# Claude Code (Alpha)
cd ~/Desktop/syncrescendence
claude

# Claude Code (Beta) - separate worktree
cd ~/Desktop/syncrescendence-beta
claude

# Gemini CLI
cd ~/Desktop/syncrescendence
gemini

# ChatGPT Codex CLI
codex "review this PR"
```

### Emergency Contacts

| Platform | Recovery | Notes |
|----------|----------|-------|
| Claude | claude.ai/settings | Subscription management |
| Gemini | one.google.com | Advanced subscription |
| ChatGPT | platform.openai.com | truongphillipthanh@icloud.com |

---

## VERSION HISTORY

**v1.0.0** (2026-01-11): Genesis establishment
- Complete 5-platform constellation specified
- Task routing matrix defined
- IIC mapping established
- Sustainability roadmap outlined
- Authority: Oracle 12

---

**END CANON-25200-CONSTELLATION_ARCH-lattice.md**
