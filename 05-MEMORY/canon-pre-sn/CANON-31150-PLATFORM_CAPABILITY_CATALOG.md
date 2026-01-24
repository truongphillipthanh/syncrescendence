# [[CANON-31150-PLATFORM_CAPABILITY_CATALOG]]: PLATFORM CAPABILITY CATALOG
## Definitive Inventory of Constellation Capabilities

**Chain**: INFORMATION (31000)
**Parent**: ACUMEN (31100)
**Status**: CRYSTALLINE
**Last Regenerated**: 2026-01-16T00:44:33.749179Z
**Data Source**: platform_capabilities.json

---

## ⚠️ TEMPORAL DATA NOTICE

This document is **auto-generated** from `.state/platform_capabilities.json`.

**DO NOT EDIT DIRECTLY.** To update capability data:
1. Edit `00-ORCHESTRATION/state/platform_capabilities.json`
2. Run: `python3 00-ORCHESTRATION/scripts/regenerate_canon.py 31150`
3. Commit regenerated file

This demonstrates the **metabolic pattern**: temporal data lives externally, evergreen structure lives in template.

---

## I. PLATFORM OVERVIEW

### Active Platforms

| Platform | Tier | Monthly Cost | Primary Role | Status |
|----------|------|--------------|--------------|--------|

| Claude Code | Pro x3 | $60 | Executor | Active |

| Gemini | Advanced | $20 | Oracle | Active |

| ChatGPT | Plus | $20 | Deviser | Active |


**Total Monthly Investment**: $100

### Trinity Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   TRINITY ARCHITECTURE                      │
│                                                             │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────┐ │
│  │   ORACLE     │      │   DEVISER    │      │ EXECUTOR │ │
│  │  (Gemini)   │──────▶│ (ChatGPT)  │──────▶│(Claude)│ │
│  │              │Evidence│              │ Plan │          │ │
│  │ - Sensing    │      │ - Planning   │      │- Execute │ │
│  │ - RAG        │      │ - Audit      │      │- Verify  │ │
│  │ - Corpus     │      │ - Specify    │      │- Deliver │ │
│  └──────────────┘      └──────────────┘      └──────────┘ │
│                              │                      │       │
│                              │                      │       │
│                              └──────────────────────┘       │
│                                   Audit Packet              │
└─────────────────────────────────────────────────────────────┘
```

---

## II. CAPABILITY MATRICES

### Claude (Executor)

**Account**: truongphillipthanh@gmail.com (+ 2 others)
**Primary Models**: Opus 4.5, Sonnet 4.5

| Capability | Status | Notes |
|------------|--------|-------|

| Filesystem Access | Active | Full repository sovereignty |

| Code Generation | Active | Opus 4.5 / Sonnet 4.5 |

| MCP Integration | Active | External tool access |

| Plan Mode | Active | Separates planning from execution |

| Context Management | Active | ~200K tokens, auto-compact |


**Routing Strengths**:

- Execution (filesystem operations)

- Code generation (writing functions)

- File manipulation (read/edit/write)

- Verification (command-based proof)

- Repository operations (git, ledger updates)


**Routing Weaknesses**:

- Corpus-scale RAG (context limit ~200K)

- Video processing (no native multimodal)

- Long-horizon planning (better as executor than planner)


**Cost Structure**:
- $20/month per seat, 3 seats = $60/month

---

### Gemini (Oracle)

**Account**: truongphillipthanh@gmail.com
**Primary Models**: Gemini 2.5 Pro, Gemini 2.5 Flash

| Capability | Status | Notes |
|------------|--------|-------|

| 2M Context Window | Active | Entire corpus fits |

| Drive Connector | Active | Repository visibility |

| NotebookLM | Active | Grounded RAG, zero hallucination |

| Video Processing | Active | 263 tok/sec native ingestion |

| Audio Processing | Active | Speaker diarization |


**Routing Strengths**:

- Corpus-scale sensing (2M context)

- Video transcription (native multimodal)

- Large context queries (entire repo + conversations)

- Grounded RAG (NotebookLM)

- Historical analysis (Oracle 0-13 in single context)


**Routing Weaknesses**:

- Filesystem access (read-only, no execution)

- Code execution (not designed for)

- Planning (sensing role, not planning)


**Cost Structure**:
- $20/month

---

### ChatGPT (Deviser)

**Account**: truongphillipthanh@icloud.com
**Primary Models**: GPT-5.2 Instant, GPT-5.2 Thinking

| Capability | Status | Notes |
|------------|--------|-------|

| GPT-5.2 Thinking | Active | ~3K messages/week |

| Deep Research | Active | Comprehensive investigation |

| Canvas | Active | Collaborative editing |

| Codex CLI | Available | GitHub integration (if enabled) |

| Connectors | Available | Drive, GitHub (if enabled) |


**Routing Strengths**:

- Long-horizon planning (GPT-5.2 Thinking)

- Specification (clear acceptance criteria)

- Audit (verification against plan)

- Abstract reasoning (architectural decisions)

- Multi-step decomposition


**Routing Weaknesses**:

- Corpus-scale sensing (context limit)

- Video processing (no native multimodal)

- Code execution (not designed for)


**Cost Structure**:
- $20/month

---

## III. ROUTING DECISION TABLE

This table guides which platform receives which task type.

| Task Type | Primary Platform | Rationale | Fallback |
|-----------|------------------|-----------|----------|

| Corpus Sensing | Gemini | 2M context window | Claude (limited context) |

| Video Processing | Gemini | Native multimodal | Manual transcription |

| Planning | ChatGPT | GPT-5.2 Thinking | Claude Plan Mode |

| Audit | ChatGPT | Spec verification | Claude verification |

| Execution | Claude | Filesystem sovereignty | Manual operations |

| Code Generation | Claude | Opus 4.5 / Sonnet 4.5 | ChatGPT |

| Grounded RAG | Gemini | NotebookLM integration | Claude with citations |

| Long-Horizon Decomposition | ChatGPT | GPT-5.2 Thinking | Claude ultrathink |


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

### 1. Trinity Architecture Roles

**Oracle** (Gemini): Sensing, RAG, corpus-scale intelligence gathering
- NEVER plans or executes
- ONLY observes and reports with citations

**Deviser** (ChatGPT): Planning, specification, audit
- NEVER executes code
- ONLY designs plans and verifies outcomes

**Executor** (Claude): Implementation, filesystem sovereignty
- NEVER does corpus-scale sensing
- ONLY executes plans and verifies deliverables

### 2. IMEP Protocol

Models communicate through structured packets, not free-form dialogue:
```
Oracle (Evidence Packet) → Deviser (Plan Packet) → Executor (Execution Packet) → Deviser (Audit Packet)
```

The repository is the **only place where truth congeals**. No model has direct access except Executor.

### 3. Routing by Teleology

Route tasks to platforms based on **functional fit**, not brand loyalty:
- Match task requirements to platform strengths
- Consider cost/performance trade-offs
- Respect platform role boundaries (Oracle/Deviser/Executor)

### 4. Ground-Truth Discipline

Every platform must maintain ground-truth discipline appropriate to its role:
- **Oracle**: Cite every claim (file:line, timestamp)
- **Deviser**: Specify verifiable acceptance criteria
- **Executor**: Verify every deliverable with command output

### 5. Capability Evolution

Platform capabilities change frequently:
- Models upgrade (GPT-5.2 → GPT-6, Gemini 2.5 → 3.0)
- Features added (new connectors, tools, integrations)
- Pricing changes

**This catalog regenerates** to track current state while evergreen principles persist in template.

---

## V. INTEGRATION PATTERNS

### Pattern 1: Source Processing

```
1. Oracle: Sense video/article/transcript → Evidence Packet
2. Deviser: Plan processing workflow → Plan Packet
3. Executor: Process, integrate, update ledger → Execution Packet
4. Deviser: Verify integration complete → Audit Packet
```

**Platform Assignments**:
- Gemini: Native video/audio processing, signal tier assessment
- ChatGPT: Decompose into processable steps, specify verification
- Claude: Execute transcription function, update sources.csv, integrate to CANON

### Pattern 2: Corpus-Scale Query

```
1. Oracle: Load repository + history, search, cite → Evidence Packet
2. Sovereign: Review findings (no Deviser/Executor needed if just query)
```

**Platform Assignments**:
- Gemini: 2M context window, upload entire corpus, search comprehensively
- (No other platforms needed unless findings trigger action)

### Pattern 3: Complex Implementation

```
1. Deviser: Decompose objective, specify phases → Plan Packet (batch)
2. Executor: Implement Phase 1 → Execution Packet 1
3. Deviser: Audit Phase 1 → Audit Packet 1
4. Executor: Implement Phase 2 → Execution Packet 2
5. [Continue until complete]
```

**Platform Assignments**:
- ChatGPT: GPT-5.2 Thinking for long-horizon decomposition
- Claude: Opus 4.5 for complex synthesis, Sonnet 4.5 for execution

---

## VI. COST OPTIMIZATION

### Current Monthly Spend

| Platform | Tier | Cost | Utilization | Cost/Hour Estimate |
|----------|------|------|-------------|-------------------|

| Claude Code | Pro x3 | $60 | 75% | $2.00 |

| Gemini | Advanced | $20 | 40% | $0.67 |

| ChatGPT | Plus | $20 | 30% | $0.67 |


**Total**: $100/month

### Optimization Strategies

1. **Model Selection**: Use Sonnet over Opus when task is well-specified
2. **Thinking Budget**: Reserve GPT-5.2 Thinking for truly complex decomposition
3. **Context Reuse**: Load corpus once per session, query multiple times
4. **Batch Operations**: Group similar tasks to minimize context-switching

### ROI Assessment

**Value Generated**:
- Autonomous IMEP cycles: 0 (target: ≥10)
- Relay reduction: 0% (target: ≥25%)
- Sources processed: 0
- CANON integrations: 0

**Cost per Autonomous Cycle**: $100 / 0 = $N/A

---

## VII. FUTURE STATE PROJECTIONS

### Phase 2: Juvenile (Target: April 2026)

**Expected Changes**:
- API-based IMEP (no manual relay)
- Direct inter-platform communication
- Automated routing logic
- Cost reduction via efficiency gains

**Capability Additions**:
- Claude: MCP server integrations (Drive, Notion, etc.)
- Gemini: NotebookLM API access (Enterprise tier)
- ChatGPT: Codex CLI integration for GitHub automation

### Phase 3: Adolescent (Target: January 2027)

**Expected Changes**:
- Multi-modal outputs (video, audio, interactive)
- External API endpoints (query interface)
- Cost optimization via fine-tuned models

**Capability Additions**:
- Claude: Video generation (if available)
- Gemini: Advanced multimodal synthesis
- ChatGPT: Agent-mode orchestration

---

## VIII. VERSION HISTORY

**Last Regenerated**: 2026-01-16T00:44:33.749179Z
**Data Version**: 1.0.0
**Template Version**: 1.0.0 (2026-01-15)

### Regeneration Log


- 2026-01-15: Initial capability catalog creation


---

## IX. REGENERATION INSTRUCTIONS

To update this document when platform capabilities change:

```bash
# 1. Edit data source
vim 00-ORCHESTRATION/state/platform_capabilities.json

# 2. Regenerate CANON
python3 00-ORCHESTRATION/scripts/regenerate_canon.py 31150

# 3. Review diff
git diff 01-CANON/CANON-31150-PLATFORM_CAPABILITY_CATALOG.md

# 4. Commit if correct
git add 01-CANON/CANON-31150-PLATFORM_CAPABILITY_CATALOG.md
git add 00-ORCHESTRATION/state/platform_capabilities.json
git commit -m "feat(canon): regenerate 31150 with updated platform data"
```

**When to Regenerate**:
- New platform added or removed
- Capability status changes (beta → active, deprecated, etc.)
- Pricing changes
- Major model upgrades
- Monthly (as part of system health review)

---

**End of [[CANON-31150-PLATFORM_CAPABILITY_CATALOG]]**

<!--
AUTO-GENERATED FILE - DO NOT EDIT DIRECTLY
Template: 00-ORCHESTRATION/templates/[[CANON-31150-PLATFORM_CAPABILITY_CATALOG]].md.j2
Data: 00-ORCHESTRATION/state/platform_capabilities.json
Generated: 2026-01-16T00:44:33.749179Z
-->