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
**Last Regenerated**: 2026-02-05T19:38:29.086161-08:00
**Data Source**: platform_capabilities.json

---

## TEMPORAL DATA NOTICE

This document is **auto-generated** from `00-ORCHESTRATION/state/platform_capabilities.json`.

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

| Claude Code | Max 5x | $100 | Commander | Active |

| Claude Web | Pro | $20 | Vizier | Active |

| ChatGPT Web | Plus | $20 | Vanguard | Active |

| Codex CLI | (via ChatGPT) | $0 | Adjudicator | Available |

| Google AI (Gemini Web) | AI Pro | $20 | Diviner | Active |

| Gemini CLI | (API) | $0 | Cartographer | Installed |

| OpenClaw | self-hosted | $0 | Local Orchestrator (Ajna/Psyche) | Active |

| Grok | (external) | $0 | Oracle (RECON) | Optional |

| Perplexity | (external) | $0 | Augur | Optional |


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


### Claude Code — Commander (EXECUTOR-LEAD)

**Account**: A1 (Max) + A2 (Pro)
**Primary Models**: Claude 4.5 Opus, Claude 4.5 Sonnet, Claude 4.5 Haiku

| Capability | Status | Notes |
|------------|--------|-------|

| Filesystem access | Active | Full repository sovereignty |

| Code generation | Active | Opus/Sonnet/Haiku |

| MCP integration | Active | Tool access via MCP |

| Plan mode | Active | Separates plan from execution |

| Hooks system | Active | Stop/PreCompact/UserPromptSubmit |

| Verification | Active | Command-output receipts |


**Routing Strengths**:

- Filesystem sovereignty

- High-fidelity implementation

- Repo-ground-truth receipts (diffs/commands/commits)

- MCP-enabled tool use


**Routing Weaknesses**:

- Corpus-scale sensing beyond session context

- Native multimodal ingestion (video/audio)


**Cost Structure**:
- $100/mo (Max) primary executor surface

---

### Claude Web — Vizier (INTERPRETER)

**Account**: A2 (Pro)
**Primary Models**: Claude 4.5 Opus/Sonnet (web)

| Capability | Status | Notes |
|------------|--------|-------|

| Synthesis/ideation | Active | High-level reasoning + writing |

| Longform drafting | Active | Narrative + clarity |


**Routing Strengths**:

- Synthesis

- Tone/voice calibration

- Rapid ideation


**Routing Weaknesses**:

- Filesystem execution

- Deterministic receipts


**Cost Structure**:
- $20/mo (Pro)

---

### ChatGPT Web — Vanguard (PLANNING/AUDIT)

**Account**: A1 (Plus)
**Primary Models**: GPT-5.2 Instant, GPT-5.2 Thinking

| Capability | Status | Notes |
|------------|--------|-------|

| Planning + decomposition | Active | Spec-first, acceptance criteria |

| Deep research | Active | Broad investigation |

| Canvas | Active | Collaborative editing |


**Routing Strengths**:

- Long-horizon planning

- Spec/audit discipline

- Clear acceptance criteria


**Routing Weaknesses**:

- Direct filesystem execution

- Very large corpus scans


**Cost Structure**:
- $20/mo (Plus)

---

### Codex CLI — Adjudicator (PARALLEL-EXEC)

**Account**: A1 (via ChatGPT)
**Primary Models**: GPT-5.2 Codex

| Capability | Status | Notes |
|------------|--------|-------|

| Parallel execution | Active | Good for mechanical implementation lanes |

| GitHub-native workflows | Available | When used with GitHub surfaces |


**Routing Strengths**:

- Parallelization

- Mechanical refactors

- Isolated execution environments (where applicable)


**Routing Weaknesses**:

- Persistent memory

- Longform synthesis


**Cost Structure**:
- $0 incremental (depends on ChatGPT tier)

---

### Gemini Web — Diviner (MULTIMODAL DIGEST)

**Account**: A2 (Google AI Pro)
**Primary Models**: Gemini 3 Pro, Gemini 3 Flash

| Capability | Status | Notes |
|------------|--------|-------|

| Multimodal ingestion | Active | Audio/video/image |

| NotebookLM | Active | Grounded RAG / annotation |

| Gems | Active | Instruction profiles |


**Routing Strengths**:

- Multimodal clarification

- Grounded notebook workflows


**Routing Weaknesses**:

- Filesystem execution

- Deterministic receipts


**Cost Structure**:
- $20/mo (AI Pro)

---

### Gemini CLI — Cartographer (SENSOR)

**Account**: A2 (API key)
**Primary Models**: Gemini (CLI)

| Capability | Status | Notes |
|------------|--------|-------|

| Corpus-scale sensing | Active | 1M+ context (model-dependent) |

| Stateless invocation | Active | Fresh runs; reproducible prompts |

| Evidence packs | Planned | Standard output format for findings |


**Routing Strengths**:

- Repo-wide survey/search

- Large-context synthesis


**Routing Weaknesses**:

- Execution

- Write access


**Cost Structure**:
- API usage (varies)

---

### OpenClaw — Local Orchestrator (Ajna/Psyche)

**Account**: Self-hosted
**Primary Models**: Config-defined (per node)

| Capability | Status | Notes |
|------------|--------|-------|

| Persistent gateway | Active | Always-on orchestration |

| Cron + heartbeat | Active | Scheduled autonomy |

| Sub-agents | Active | Isolated background runs |

| Tool execution | Active | Shell/files/browser/messaging (per config) |


**Routing Strengths**:

- Continuity across restarts

- Dispatch + routing

- Automation glue


**Routing Weaknesses**:

- Not the primary deep-reasoning IDE

- Depends on configured channels/tools


**Cost Structure**:
- $0 incremental (self-hosted)

---


## III. ROUTING DECISION TABLE

This table guides which platform receives which task type.

| Task Type | Primary Platform | Rationale | Fallback |
|-----------|------------------|-----------|----------|

| Corpus sensing (repo-wide) | Gemini CLI (Cartographer) | Large-context corpus survey | Claude Code (Commander) (bounded) |

| Multimodal processing (audio/video/images) | Gemini Web (Diviner) | Native multimodal + NotebookLM | Manual / dedicated pipeline |

| Planning / decomposition | ChatGPT Web (Vanguard) | Spec-first planning | Claude Code plan mode |

| Implementation (repo changes) | Claude Code (Commander) | Filesystem sovereignty + receipts | Codex CLI (Adjudicator) |

| Mechanical refactors / parallel lanes | Codex CLI (Adjudicator) | Parallelization / isolation | Claude Code (Commander) |

| Autonomy glue (dispatch, reminders, cross-channel relays) | OpenClaw (Ajna/Psyche) | Persistent daemon + cron + subagents | Manual dispatch packets |

| Real-time discourse sensing | Grok (Oracle / RECON) | X/Twitter firehose | Perplexity / web search |

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

| Claude Code | Max 5x | $100 | 80% | $3.33 |

| Claude Web | Pro | $20 | 30% | $0.67 |

| ChatGPT Web | Plus | $20 | 25% | $0.67 |

| Codex CLI | (via ChatGPT) | $0 | 10% | $0.00 |

| Google AI (Gemini Web) | AI Pro | $20 | 20% | $0.67 |

| Gemini CLI | (API) | $0 | 5% | $0.00 |

| OpenClaw | self-hosted | $0 | 40% | $0.00 |

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
- Autonomous cycles: 2
- Relay reduction: 0%
- Sources processed: 43
- CANON integrations: 11

---

## VII. VERSION HISTORY

**Last Regenerated**: 2026-02-05T19:38:29.086161-08:00
**Data Version**: 3.0.0

### Regeneration Log

- 2026-01-15: Initial capability catalog creation

- 2026-02-02: v2.0: Trinity→Constellation, Deviser→Vanguard, Executor→Commander, Oracle→Grok, updated economics to $160/mo

- 2026-02-05: v3.0: Deconflate CLI vs Web; add OpenClaw + Codex as first-class entries; expand routing table.


---

## VIII. REGENERATION INSTRUCTIONS

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

---

**End of CANON-31150**

<!--
AUTO-GENERATED FILE - DO NOT EDIT DIRECTLY
Template: 00-ORCHESTRATION/templates/CANON-31150.md.j2
Data: 00-ORCHESTRATION/state/platform_capabilities.json
Generated: 2026-02-05T19:38:29.086161-08:00
-->

---

## CROSS-REFERENCES

- [[CANON-00000-SCHEMA-cosmos]] — Master Schema
- [[CANON-31000-INFORMATION-chain]] — Information Chain (Chain Root)
- [[CANON-00006-CORPUS-cosmos]] — Corpus Management
- [[CANON-30000-INTELLIGENCE-chain]] — Intelligence Chain (Substrate)