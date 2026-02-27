# CANON-31150: PLATFORM CAPABILITY CATALOG

---

## CELESTIAL NAVIGATION

**Orbital Class**: Unknown

**Parent**: [[CANON-31100-ACUMEN-planetary-INFORMATION]] (Planetary Acumen)

**Siblings**:
- [[CANON-31110-FEEDCRAFT-lunar-ACUMEN-planetary-INFORMATION]] (Feedcraft)
- [[CANON-31120-TONE_LIBRARY-lunar-ACUMEN-planetary-INFORMATION]] (Tone Library)
- [[CANON-31130-SEVEN_LAYER-lunar-ACUMEN-planetary-INFORMATION]] (Seven-Layer Stack)
- [[CANON-31140-IIC-lunar-ACUMEN-planetary-INFORMATION]] (IIC Constellation)

---

## Definitive Inventory of Constellation Capabilities

**Chain**: INFORMATION (31000)
**Parent**: ACUMEN (31100)
**Status**: CRYSTALLINE
**Last Regenerated**: 2026-02-16T15:35:59.043439-08:00
**Data Source**: platform_capabilities.json

---

## TEMPORAL DATA NOTICE

This document is **auto-generated** from `orchestration/state/platform_capabilities.json`.

**DO NOT EDIT DIRECTLY.** To update capability data:
1. Edit `orchestration/state/platform_capabilities.json`
2. Run: `python3 orchestration/scripts/regenerate_canon.py 31150`
3. Commit regenerated file

This demonstrates the **metabolic pattern**: temporal data lives externally, evergreen structure lives in template.

---

## I. PLATFORM OVERVIEW

### Active Platforms

| Platform | Tier | Monthly Cost | Primary Role | Status |
|----------|------|--------------|--------------|--------|

| Claude Code | Max | $100 | Commander / COO | Active |

| Claude Web | Pro | $20 | Vizier (relay surface) | Active |

| ChatGPT Web | Plus | $20 | Psyche relay surface | Active |

| Codex CLI | (via ChatGPT Plus) | $0 | Adjudicator / CQO | Active |

| Google AI (Gemini Web) | AI Pro | $20 | Diviner (multimodal relay) | Active |

| Gemini CLI | (Google AI key) | $0 | Cartographer / CIO | Active |

| OpenClaw (Psyche) | self-hosted | $0 | Psyche / CTO | Active |

| OpenClaw (Ajna) | self-hosted | $0 | Ajna / CSO | Planned |

| Grok | (external) | $0 | Oracle (reconnaissance) | Optional |

| Perplexity | (external) | $0 | Augur (verification) | Optional |


**Total Monthly Investment**: $160

### Constellation Architecture

```
CONSTELLATION ARCHITECTURE (10 Avatars, 3 Accounts, $160/mo)

SENSING                    PLANNING                   EXECUTION
(What is happening?)       (What should happen?)       (Make it happen.)

┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│  ORACLE (Grok)   │      │ VANGUARD (ChatGPT)│      │ COMMANDER (Claude)│
│  - Recon         │─────▶│ - Planning        │─────▶│ - Execute         │
│  - EQ/grounding  │ Evid │ - Specification   │ Plan │ - Verify          │
│  - Challenge     │      │ - Audit           │      │ - Deliver         │
└──────────────────┘      └──────────────────┘      └──────────────────┘
                                  │                        │
                                  └────────────────────────┘
                                       Audit Packet

SUPPLEMENTARY ROLES:
  Diviner (Gemini Web)    — Multimodal digest + clarification
  Cartographer (Gemini CLI) — Corpus-scale sensing (1M context)
  Vizier (Claude Web)     — Synthesis + ideation
  Adjudicator (Codex CLI) — Parallel execution
  Augur (Perplexity)      — Real-time external verification
  Ajna (OpenClaw Opus)    — Local orchestration (Mac mini)
  Psyche (OpenClaw GPT5.2) — Local orchestration (MBA)
```

---

## II. CAPABILITY MATRICES


### Claude Code — Commander / COO (Viceroy)

**Account**: A1 (Max)
**Primary Models**: Claude Opus 4.6, Claude Sonnet 4.5, Claude Haiku 4.5

| Capability | Status | Notes |
|------------|--------|-------|

| Filesystem access | Active | Full repository sovereignty |

| Code generation | Active | Opus/Sonnet/Haiku model selection |

| MCP integration | Active | 9 servers: Linear, ClickUp, Graphiti, Obsidian, Filesystem, Chrome DevTools, Playwright, Qdrant, Gemini-MCP |

| Plan mode | Active | Separates planning from execution |

| Agent teams | Active | Parallel subagent dispatch for complex tasks |

| Hooks system | Active | Stop, PreCompact, UserPromptSubmit hooks |

| Extended thinking | Active | Auto-enabled, keyword signals for intent |

| Skills ecosystem | Active | 226+ universal skills + 23 codex + 8 gemini + 9 openclaw |

| Verification | Active | Command-output receipts, git verification |


**Routing Strengths**:

- Filesystem sovereignty — reads, writes, git operations

- High-fidelity implementation with verification receipts

- MCP-enabled cross-platform coordination (9 servers)

- Agent teams for parallel task execution

- Skills ecosystem (266+ capabilities)


**Routing Weaknesses**:

- Context window limits corpus-scale sensing

- No native multimodal ingestion (video/audio)


**Cost Structure**:
- $100/mo (Max plan) — primary executor surface

---

### OpenClaw (Psyche) — Psyche / CTO (Synaptarch)

**Account**: A1 (ChatGPT Plus OAuth)
**Primary Models**: GPT-5.3-codex

| Capability | Status | Notes |
|------------|--------|-------|

| Persistent gateway | Active | Always-on orchestration, port 18789 |

| Cron + heartbeat | Active | Scheduled autonomy via launchd |

| Memory systems | Active | Mem0 (auto-recall/capture) + Graphiti (knowledge graph) |

| MCP bridge | Active | Filesystem + Obsidian MCP via adapter |

| Tool execution | Active | Shell, files, browser, Discord integration |

| Sub-agents | Active | Isolated background task runs |


**Routing Strengths**:

- System cohesion and automation (Make/Zapier)

- Policy enforcement across constellation

- Pipeline fusion between tools

- Persistent memory across sessions

- Always-on daemon operation


**Routing Weaknesses**:

- Token budget constrained by ChatGPT Plus daily limit

- Not primary deep-reasoning surface

- Anthropic OAuth blocked — cannot use Claude models


**Cost Structure**:
- $0 incremental (uses ChatGPT Plus OAuth)

---

### Codex CLI — Adjudicator / CQO (Executor)

**Account**: A1 (ChatGPT Plus OAuth)
**Primary Models**: GPT-5.2-codex (gpt-5.2-codex)

| Capability | Status | Notes |
|------------|--------|-------|

| Parallel execution | Active | Mechanical implementation lanes |

| GitHub-native workflows | Active | PR review, CI fix, code review |

| Spec mode | Active | Spec-driven development workflow |

| Quality gates | Active | Linting, testing, compliance checking |


**Routing Strengths**:

- Quality assurance and compliance verification

- Parallelizable mechanical refactors

- GitHub-native workflows (PR, CI, review)

- Isolated sandbox execution


**Routing Weaknesses**:

- No persistent memory across sessions

- Limited longform synthesis

- ChatGPT Plus daily token budget shared with Psyche


**Cost Structure**:
- $0 incremental (ChatGPT Plus OAuth)

---

### Gemini CLI — Cartographer / CIO (Exegete)

**Account**: A2 (Google AI key)
**Primary Models**: Gemini 2.5 Pro

| Capability | Status | Notes |
|------------|--------|-------|

| Corpus-scale sensing | Active | 2M+ context window |

| Stateless invocation | Active | Fresh runs, reproducible prompts |

| Evidence packs | Active | Structured output for findings |

| Extensions | Active | 8 Gemini CLI extensions installed |


**Routing Strengths**:

- Repo-wide survey and intelligence gathering

- Large-context synthesis (2M tokens)

- Structured evidence output

- Extension ecosystem


**Routing Weaknesses**:

- No write access to filesystem

- Stateless — no session continuity


**Cost Structure**:
- $0 incremental (Google AI key via AI Pro plan)

---

### OpenClaw (Ajna) — Ajna / CSO (Strategos)

**Account**: NVIDIA NIM API (free tier)
**Primary Models**: Kimi K2.5

| Capability | Status | Notes |
|------------|--------|-------|

| Strategic direction | Planned | Meta/macro awareness |

| Dispatch optimization | Planned | Task routing across constellation |

| Memory systems | Planned | Shared Graphiti KG + local Mem0 |


**Routing Strengths**:

- Strategic steering (CSO role)

- Cross-agent orchestration

- Remote machine operation (MBA)


**Routing Weaknesses**:

- MBA not yet configured

- NVIDIA free tier token limits (40 RPM)

- Kimi K2.5 less capable than GPT-5.3/Opus


**Cost Structure**:
- $0 (NVIDIA NIM free tier, ~1,000 credits)

---

### Claude Web — Vizier (relay surface)

**Account**: A2 (Pro)
**Primary Models**: Claude Opus 4.6, Claude Sonnet 4.5

| Capability | Status | Notes |
|------------|--------|-------|

| Synthesis/ideation | Active | High-level reasoning + writing |

| Longform drafting | Active | Narrative + clarity |

| MCP apps | Active | Cowork integrations (Slack, Figma, etc.) |


**Routing Strengths**:

- Synthesis and tone calibration

- Rapid ideation with Sovereign

- MCP app integrations via Cowork


**Routing Weaknesses**:

- No filesystem execution

- No deterministic receipts


**Cost Structure**:
- $20/mo (Pro plan)

---

### ChatGPT Web — Planning/audit surface

**Account**: A1 (Plus)
**Primary Models**: GPT-5.3, GPT-5.3-codex

| Capability | Status | Notes |
|------------|--------|-------|

| Planning + decomposition | Active | Spec-first, acceptance criteria |

| Deep research | Active | Broad investigation |

| Canvas | Active | Collaborative editing |

| Memory | Active | Cross-conversation memory |


**Routing Strengths**:

- Long-horizon planning and specification

- Cross-conversation memory persistence

- Canvas collaborative editing


**Routing Weaknesses**:

- No filesystem execution

- Limited corpus-scale scanning


**Cost Structure**:
- $20/mo (Plus plan)

---

### Gemini Web — Diviner (multimodal digest)

**Account**: A2 (Google AI Pro)
**Primary Models**: Gemini 2.5 Pro, Gemini 2.5 Flash

| Capability | Status | Notes |
|------------|--------|-------|

| Multimodal ingestion | Active | Audio/video/image native processing |

| NotebookLM | Active | Grounded RAG, zero-hallucination annotation |

| Gems | Active | Custom instruction profiles |

| Google Drive integration | Active | Direct document access |


**Routing Strengths**:

- Multimodal clarification (audio/video/image)

- NotebookLM grounded workflows

- Google ecosystem integration


**Routing Weaknesses**:

- No filesystem execution

- No deterministic receipts


**Cost Structure**:
- $20/mo (AI Pro plan)

---


## III. ROUTING DECISION TABLE

This table guides which platform receives which task type.

| Task Type | Primary Platform | Rationale | Fallback |
|-----------|------------------|-----------|----------|

| Corpus sensing (repo-wide) | Gemini CLI (Cartographer/CIO) | 2M context corpus survey | Claude Code (Commander/COO) bounded |

| Multimodal processing (audio/video/images) | Gemini Web (Diviner) | Native multimodal + NotebookLM | Manual / dedicated pipeline |

| Planning / decomposition | ChatGPT Web + Sovereign | Spec-first planning with human oversight | Claude Code plan mode |

| Implementation (repo changes) | Claude Code (Commander/COO) | Filesystem sovereignty + verification receipts | Codex CLI (Adjudicator/CQO) |

| Quality assurance / code review | Codex CLI (Adjudicator/CQO) | GitHub-native QA workflows | Claude Code (Commander/COO) |

| System cohesion / automation | OpenClaw Psyche (CTO) | Persistent daemon + policy enforcement | Commander via dispatch |

| Strategic direction / orchestration | OpenClaw Ajna (CSO) | Meta/macro awareness + dispatch optimization | Sovereign direct command |

| Real-time discourse sensing | Grok (Oracle) | X/Twitter firehose | Perplexity / web search |

| External verification (citations) | Perplexity (Augur) | Citation-backed verification | Gemini Web grounding |


### Routing Protocol

**Decision Flow**:
```
1. Identify task type from above table
2. Route to primary platform
3. If primary unavailable/inappropriate, use fallback
4. If both unavailable, escalate to Sovereign
```

**Override Conditions**:
- Sovereign explicitly specifies platform
- Task requires capabilities only one platform has
- Cost optimization requires different routing

---

## IV. EVERGREEN PRINCIPLES

The following principles remain constant regardless of capability changes:

### 1. Constellation Architecture Roles

**Oracle** (Grok): Cultural divination, EQ, reality checks, adversarial grounding
- NEVER plans or executes
- ONLY observes and reports with authentic voice

**Vanguard** (ChatGPT): Planning, specification, audit
- NEVER executes code
- ONLY designs plans and verifies outcomes

**Commander** (Claude): Implementation, filesystem sovereignty
- NEVER does corpus-scale sensing
- ONLY executes plans and verifies deliverables

**Cartographer** (Gemini CLI): Corpus sensing, evidence packs
- 1M token context window
- Stateless, reproducible queries

**Diviner** (Gemini Web): Multimodal clarification, TTS-optimized digests
- Gems + Drive integration
- Infinite threads

### 2. Dispatch Protocol

Agents communicate through structured packets via the dispatch system:
```
Oracle (Evidence) → Vanguard (Plan) → Commander (Execute) → Vanguard (Audit) → State Update
```

The repository is the **only place where truth congeals**. Write access via CLI tools only.

### 3. Routing by Teleology

Route tasks to platforms based on **functional fit**, not brand loyalty:
- Match task requirements to platform strengths
- Consider cost/performance trade-offs
- Respect platform role boundaries

### 4. Ground-Truth Discipline

Every platform must maintain ground-truth discipline appropriate to its role:
- **Oracle**: Cite every claim (file:line, timestamp)
- **Vanguard**: Specify verifiable acceptance criteria
- **Commander**: Verify every deliverable with command output

### 5. Capability Evolution

Platform capabilities change frequently. **This catalog regenerates** to track current state while evergreen principles persist in template.

---

## V. INTEGRATION PATTERNS

### Pattern 1: Source Processing
```
1. Oracle/Cartographer: Sense video/article/transcript → Evidence
2. Vanguard: Plan processing workflow → Plan Packet
3. Commander: Process, integrate, update ledger → Execution
4. Vanguard: Verify integration complete → Audit
```

### Pattern 2: Corpus-Scale Query
```
1. Cartographer: Load repository (1M context), search, cite → Evidence
2. Sovereign: Review findings (no Vanguard/Commander needed if just query)
```

### Pattern 3: Complex Implementation
```
1. Vanguard: Decompose objective, specify phases → Plan Packet (batch)
2. Commander: Implement Phase 1 → Execution
3. Vanguard: Audit Phase 1 → Audit
4. Commander: Implement Phase 2 → Execution
5. [Continue until complete]
```

---

## VI. COST OPTIMIZATION

### Current Monthly Spend

| Platform | Tier | Cost | Utilization | Cost/Hour Estimate |
|----------|------|------|-------------|-------------------|

| Claude Code | Max | $100 | 85% | $3.33 |

| Claude Web | Pro | $20 | 20% | $0.67 |

| ChatGPT Web | Plus | $20 | 25% | $0.67 |

| Codex CLI | (via ChatGPT Plus) | $0 | 15% | $0.00 |

| Google AI (Gemini Web) | AI Pro | $20 | 20% | $0.67 |

| Gemini CLI | (Google AI key) | $0 | 10% | $0.00 |

| OpenClaw (Psyche) | self-hosted | $0 | 40% | $0.00 |

| OpenClaw (Ajna) | self-hosted | $0 | 0% | $0.00 |

| Grok | (external) | $0 | 5% | $0.00 |

| Perplexity | (external) | $0 | 5% | $0.00 |


**Total**: $160/month

### Optimization Strategies

1. **Model Selection**: Use Sonnet over Opus when task is well-specified
2. **Thinking Budget**: Reserve GPT-5.2 Thinking for truly complex decomposition
3. **Context Reuse**: Load corpus once per session, query multiple times
4. **Batch Operations**: Group similar tasks to minimize context-switching

### ROI Assessment

**Metrics**:
- Autonomous cycles: 18
- Relay reduction: %
- Sources processed: 43
- CANON integrations: 11

---

## VII. VERSION HISTORY

**Last Regenerated**: 2026-02-16T15:35:59.043439-08:00
**Data Version**: 4.0.0

### Regeneration Log

- 2026-01-15: Initial capability catalog creation

- 2026-02-02: v2.0: Trinity→Constellation, Deviser→Vanguard, Executor→Commander, Oracle→Grok, updated economics to $160/mo

- 2026-02-05: v3.0: Deconflate CLI vs Web; add OpenClaw + Codex as first-class entries; expand routing table.

- 2026-02-10: v4.0: Enterprise role mapping (CEO/CTO/COO/CQO/CIO/CSO). Model updates (Opus 4.6, GPT-5.3-codex, Kimi K2.5, Gemini 2.5 Pro). AjnaPsyche Archon. Dual-machine paradigm. MCP server inventory. Expanded metrics.


---

## VIII. REGENERATION INSTRUCTIONS

To update this document when platform capabilities change:

```bash
# 1. Edit data source
vim orchestration/state/platform_capabilities.json

# 2. Regenerate CANON
python3 orchestration/scripts/regenerate_canon.py 31150

# 3. Review diff
git diff canon/CANON-31150-PLATFORM_CAPABILITY_CATALOG.md

# 4. Commit if correct
git add canon/CANON-31150-PLATFORM_CAPABILITY_CATALOG.md
git add orchestration/state/platform_capabilities.json
git commit -m "feat(canon): regenerate 31150 with updated platform data"
```

---

**End of CANON-31150**

<!--
AUTO-GENERATED FILE - DO NOT EDIT DIRECTLY
Template: orchestration/templates/CANON-31150.md.j2
Data: orchestration/state/platform_capabilities.json
Generated: 2026-02-16T15:35:59.043439-08:00
-->

---

## CROSS-REFERENCES

- [[CANON-00000-SCHEMA-cosmos]] — Master Schema
- [[CANON-31000-INFORMATION-chain]] — Information Chain (Chain Root)
- [[CANON-00006-CORPUS-cosmos]] — Corpus Management
- [[CANON-30000-INTELLIGENCE-chain]] — Intelligence Chain (Substrate)