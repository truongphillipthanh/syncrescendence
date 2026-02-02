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
**Last Regenerated**: 2026-02-02T01:19:54.503920-08:00
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

| ChatGPT | Plus | $20 | Vanguard | Active |

| Google AI | AI Pro | $20 | Cartographer/Diviner | Active |


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

### Claude (Commander)

**Account**: truongphillipthanh@icloud.com (A1, Max) + icloud.truongphillipthanh@gmail.com (A2, Pro)
**Primary Models**: Claude 4.5 Opus, Claude 4.5 Sonnet, Claude 4.5 Haiku

| Capability | Status | Notes |
|------------|--------|-------|

| Filesystem Access | Active | Full repository sovereignty |

| Code Generation | Active | Opus 4.5 / Sonnet 4.5 / Haiku 4.5 |

| MCP Integration | Active | External tool access |

| Plan Mode | Active | Separates planning from execution |

| Context Management | Active | ~200K tokens, 1M beta, auto-compact |

| Extended Thinking | Active | Auto-enabled at 31,999 tokens |

| Hooks System | Active | Stop, PreCompact, UserPromptSubmit |

| Skills | Active | 7 operational skills |


**Routing Strengths**:

- Execution (filesystem operations)

- Code generation (writing functions)

- File manipulation (read/edit/write)

- Verification (command-based proof)

- Repository operations (git, ledger updates)

- Multi-agent dispatch (hook-based automation)


**Routing Weaknesses**:

- Corpus-scale RAG (context limit ~200K)

- Video processing (no native multimodal)

- Long-horizon planning (better as executor than planner)


**Cost Structure**:
- A1: $100/month (Max 5x) + A2: $20/month (Pro) = $120/month

---

### Gemini (Cartographer + Diviner)

**Account**: icloud.truongphillipthanh@gmail.com (A2, Google AI Pro)
**Primary Models**: Gemini 3 Pro, Gemini 3 Flash, Gemini 3 Deep Think

| Capability | Status | Notes |
|------------|--------|-------|

| 1M Context Window | Active | Full corpus sensing |

| Drive Connector | Active | Repository visibility via Gems |

| NotebookLM | Active | Grounded RAG, zero hallucination |

| Video Processing | Active | Native multimodal ingestion |

| Audio Processing | Active | Speaker diarization |

| Gems | Active | Custom instruction profiles |

| CLI Access | Installed | API key pending (Sovereign) |


**Routing Strengths**:

- Corpus-scale sensing (1M context)

- Video transcription (native multimodal)

- Large context queries (entire repo + conversations)

- Grounded RAG (NotebookLM)

- Multimodal clarification (text, image, audio, video)


**Routing Weaknesses**:

- Filesystem access (read-only, no execution)

- Code execution (not designed for)

- Planning (sensing role, not planning)


**Cost Structure**:
- $20/month (Google AI Pro)

---

### ChatGPT (Vanguard)

**Account**: truongphillipthanh@icloud.com (A1, Plus)
**Primary Models**: GPT-5.2 Instant, GPT-5.2 Thinking

| Capability | Status | Notes |
|------------|--------|-------|

| GPT-5.2 Thinking | Active | ~3K messages/week |

| Deep Research | Active | Comprehensive investigation |

| Canvas | Active | Collaborative editing |

| Codex CLI | Installed | API key pending (Sovereign) |

| Connectors | Available | Drive, GitHub (if enabled) |

| Projects | Active | Context isolation, project-only memory |


**Routing Strengths**:

- Long-horizon planning (GPT-5.2 Thinking)

- Specification (clear acceptance criteria)

- Audit (verification against plan)

- Abstract reasoning (architectural decisions)

- Multi-step decomposition

- Creative expansion and ideation


**Routing Weaknesses**:

- Corpus-scale sensing (128K context limit)

- Video processing (no native multimodal)

- Code execution (not designed for)


**Cost Structure**:
- $20/month (Plus)

---

## III. ROUTING DECISION TABLE

This table guides which platform receives which task type.

| Task Type | Primary Platform | Rationale | Fallback |
|-----------|------------------|-----------|----------|

| Corpus Sensing | Gemini | 1M context window | Claude (limited context) |

| Video Processing | Gemini | Native multimodal | Manual transcription |

| Planning | ChatGPT | GPT-5.2 Thinking | Claude Plan Mode |

| Audit | ChatGPT | Spec verification | Claude verification |

| Execution | Claude | Filesystem sovereignty | Codex CLI |

| Code Generation | Claude | Opus 4.5 / Sonnet 4.5 | ChatGPT |

| Grounded RAG | Gemini | NotebookLM integration | Claude with citations |

| Long-Horizon Decomposition | ChatGPT | GPT-5.2 Thinking | Claude ultrathink |

| Real-time Discourse | Grok | X/Twitter integration | Perplexity |

| External Verification | Perplexity | Citation-backed search | Gemini |


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

| ChatGPT | Plus | $20 | 25% | $0.67 |

| Google AI | AI Pro | $20 | 20% | $0.67 |


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

**Last Regenerated**: 2026-02-02T01:19:54.503920-08:00
**Data Version**: 2.0.0

### Regeneration Log

- 2026-01-15: Initial capability catalog creation

- 2026-02-02: v2.0: Trinity→Constellation, Deviser→Vanguard, Executor→Commander, Oracle→Grok, updated economics to $160/mo


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
Generated: 2026-02-02T01:19:54.503920-08:00
-->

---

## CROSS-REFERENCES

- [[CANON-00000-SCHEMA-cosmos]] — Master Schema
- [[CANON-31000-INFORMATION-chain]] — Information Chain (Chain Root)
- [[CANON-00006-CORPUS-cosmos]] — Corpus Management
- [[CANON-30000-INTELLIGENCE-chain]] — Intelligence Chain (Substrate)