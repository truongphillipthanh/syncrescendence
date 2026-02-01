---
id: CANON-30340
name: Implementation Patterns
identity: IMPLEMENTATION_PATTERNS
tier: CANON
type: asteroid
parent: CANON-30300
chain: INTELLIGENCE
comet: TECH_STACK
version: 2.0.0
status: canonical
created: 2025-12-31
updated: 2025-12-31
change_velocity: quarterly
dependencies:
  - CANON-30300
  - CANON-30330
  - CANON-30000
synopsis: >
  Production-validated implementation patterns for AI-augmented systems:
  architectural anti-patterns, memory bootstrapping, orchestration strategies,
  context engineering economics, security governance, and operational cadences.
---

# CANON-30340: IMPLEMENTATION PATTERNS
## Production Workflows and Operational Guidance

---

## I. Architectural Wisdom

### The Over-Engineering Anti-Pattern

**What fails:**

---

## CELESTIAL NAVIGATION

**Orbital Class**: 🪨 Asteroid

**Parent**: [[CANON-30300-TECH_STACK-comet-INTELLIGENCE]] (Technology Stack Database)

**Siblings**:
- [[CANON-30310-MIGRATION-asteroid-TECH_STACK-comet-INTELLIGENCE]] (Tech Stack Migration)
- [[CANON-30320-WORKFLOW_INTEL-asteroid-TECH_STACK-comet-INTELLIGENCE]] (Workflow Intelligence)
- [[CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE]] (Research Protocols)

---

1. Building infrastructure before validating concepts
2. Elaborate schemas before understanding requirements
3. Rigid taxonomies resisting evolution
4. Tool-centric organization instead of primitive extraction
5. Prescriptive workflows specified upfront

**Core corrections:**

| Anti-Pattern | Correct Approach |
|-------------|------------------|
| Database schemas → theory | Theory → derived implementation |
| Specify field types, intervals | Document concepts, let details emerge |
| Comprehensive tool catalogs | Stable primitives extracted when needed |
| Prescribe workflows upfront | Observe patterns, crystallize apparatus |
| Linear effort growth | Intelligence scales with data |

### Implementation Principles

**Start Lightweight, Scale Intelligently**: Don't build comprehensive databases. Start with simple tracking, let patterns emerge, formalize what proves valuable.

**Observation Over Prescription**: Don't design workflows upfront. Use tools naturally, track usage, identify apparatus from observation.

**Primitives Over Tools**: Don't catalog every feature. Extract primitives only when considering consolidation or encountering gaps.

**Intelligence Through Data**: Don't manually classify everything. Instrument systems, collect signals, let patterns emerge algorithmically.

**Governance As Enabler**: Design governance that enables capability while managing risk. Good governance accelerates, not restricts.

---

## II. Memory System Bootstrapping

### Phase Architecture

| Phase | Timeline | Goal | Success Criteria |
|-------|----------|------|------------------|
| Working | Week 1 | Context continuity | Multi-turn coherence |
| Episodic | Weeks 2-4 | Interaction logging | Pattern identification |
| Semantic | Months 2-3 | Knowledge extraction | Cross-session answers |
| Procedural | Months 3-4 | Workflow caching | Zero-reasoning execution |
| Integration | Months 4-6 | Unified retrieval | Multi-tier intelligence |

### Working Memory (Week 1)
Maintain conversation history in model context window. No external storage required.

**Pattern**: Append user/assistant messages to history, pass full history to LLM.

### Episodic Memory (Weeks 2-4)
Log interactions to structured format (JSON/SQLite): timestamp, input, output, metadata, session_id.

**Pattern**: Append-only log file, chronological retrieval, keyword search.

### Semantic Memory (Months 2-3)
Extract and retrieve factual knowledge.

**Option A (Simple)**: LLM-based fact extraction + keyword search in fact store.

**Option B (Production)**: Vector database (Pinecone, etc.) with embeddings for semantic retrieval.

### Procedural Memory (Months 3-4)
Cache high-frequency workflows as reusable functions.

**Pattern**: Analyze episodic log for repeated sequences → convert to executable procedure → invoke without re-reasoning.

### Unified Memory (Months 4-6)
Intelligent multi-tier retrieval hierarchy:
1. Working memory (fastest)
2. Procedural cache (fast)
3. Semantic knowledge (medium)
4. Similar episodes (slower)

### Memory Architecture Patterns

**Context Window Optimization**:
- Static knowledge at beginning (enables caching)
- Recent conversation in middle
- Current query at end
- Result: 90% cost reduction via prompt caching

**Hierarchical Summarization**:
- Detailed episodes → session summaries → weekly digests → monthly insights
- Retrieval starts at appropriate abstraction level

**Sleep-Time Reorganization**:
- During idle: consolidate memories, update indices, prune low-value entries
- Background optimization improves retrieval quality

---

## III. Orchestration Patterns

### Decision Tree

```
Is workflow deterministic with clear stages?
├─ Yes → Sequential coordination (60%+ of workflows)
└─ No
   └─ Are subtasks independent?
      ├─ Yes → Concurrent execution
      └─ No
         └─ Is brainstorming/creativity needed?
            ├─ Yes → Group chat (max 3 agents)
            └─ No
               └─ Does expertise shift between phases?
                  ├─ Yes → Explicit handoff
                  └─ No → Magnetic routing (adaptive)
```

### Pattern 1: Sequential Coordination

**When**: Linear pipeline with clear stage boundaries.

**Structure**: Research → Draft → Edit → Format (stage outputs feed next stage).

**Tips**:
- Add checkpoints for failure recovery
- Log intermediate results
- Time stages to identify bottlenecks
- Cache outputs for common inputs

### Pattern 2: Concurrent Execution

**When**: Independent subtasks that parallelize.

**Structure**: Spawn parallel tasks → gather results → synthesize.

**Validation**: 45% faster than sequential for independent tasks.

**Tips**:
- Set timeout per task (prevent blocking)
- Retry with exponential backoff
- Monitor API rate limits
- Priority queue if some results more important

### Pattern 3: Critic-Refiner Loop

**When**: Quality > speed, iterative improvement beneficial.

**Structure**: Generate → Critique → Refine (loop until threshold met).

**Validation**: 30-40% quality improvement on complex generation.

**Tips**:
- Clear evaluation criteria
- Limit iterations (diminishing returns)
- Track iteration count as quality metric

### Pattern 4: Specialist Swarm

**When**: Complex problem benefiting from multiple expert perspectives.

**Structure**: Parallel specialists → Coordinator synthesis.

**Validation**: 45% faster resolution, 60% higher accuracy than single-agent.

**Tips**:
- Ensure specialists are complementary, not redundant
- Weight by historical accuracy
- Surface disagreements (often reveals nuance)
- Include confidence scores

### Pattern 5: Hub-and-Spoke

**When**: Mission-critical applications requiring centralized oversight.

**Structure**: Hub creates plan → routes to specialists → monitors → synthesizes.

**Tips**:
- Circuit breakers in hub
- Log all hub decisions
- Approval gates for high-impact actions
- Monitor hub (it's the bottleneck)

---

## IV. Context Engineering Economics

### Prompt Caching

**Economics**:
- Cache write: 1.25x (5min TTL) or 2x (1hr TTL)
- Cache read: 0.1x (90% discount)
- Cache miss: Full price

**Break-even**: Static docs cache after 2 uses. Semi-static content after 10+ daily uses.

**Pattern**: Structure prompts with static content first, dynamic last. Cache static portion.

**Observed savings**: 40-90% cost reduction, 10-85% latency reduction.

### RAG Strategy Selection

```
Is knowledge static or dynamic?
├─ Static → Semantic memory + caching
└─ Dynamic
   └─ Simple lookup or complex reasoning?
      ├─ Simple → Basic RAG
      └─ Complex
         └─ Query ambiguous/evolving?
            ├─ No → GraphRAG
            └─ Yes → Agentic RAG
```

### RAG Implementations

| Type | When | Cost | Latency | Accuracy |
|------|------|------|---------|----------|
| Basic | Simple Q&A | ~1¢ | 200-500ms | 70% |
| Hybrid | Production systems | ~1-2¢ | 400-800ms | 85-90% |
| Agentic | Research, high-stakes | ~5-15¢ | 2-8s | 92-96% |

**Basic RAG**: Embed query → vector search → inject context → generate.

**Hybrid RAG**: Vector + keyword + metadata search → rerank → generate. 49% reduction in retrieval misses.

**Agentic RAG**: Iterative retrieval with agent evaluation and query refinement. Reserve for complex/ambiguous queries.

### Context Overflow Strategies

**Sliding Window**: Process chunks with overlap for continuity.

**Hierarchical Summarization**: Sections → section summaries → combined summary (recurse if needed).

**Context Offloading**: Heavy processing in separate agent, return summary only. 8x cleaner signal.

---

## V. Security and Governance

### Threat Model

- **Prompt injection**: Malicious inputs overriding instructions
- **Agent hijacking**: Tricking agent into unauthorized actions
- **Tool misuse**: Access beyond intended scope
- **Data exfiltration**: Sensitive info in outputs
- **Jailbreaking**: Bypassing safety constraints

### Defense Patterns

**1. Input Validation**
- Detect injection patterns
- Mask PII before processing
- Rate limit per user/IP

**2. Capability-Based Access Control**
- Explicit allowed capabilities per agent
- Fine-grained action permissions
- Log all violations

**3. Output Filtering**
- Remove leaked PII
- Content policy enforcement
- Detect exfiltration attempts

**4. Circuit Breaker**
- Track failure count
- Trip open after threshold
- Auto-reset after timeout
- Alert operators on trip

**5. Approval Gates**
- Assess action impact
- Pause for human approval on high-impact
- Provide reasoning and alternatives
- Timeout with escalation

### Production Security Checklist

**Input**: [ ] Injection validation [ ] PII masking [ ] Rate limiting [ ] File sanitization

**Agent**: [ ] Capability access control [ ] Action logging [ ] Resource limits [ ] Circuit breakers

**Output**: [ ] PII filtering [ ] Content policy [ ] Anti-exfiltration [ ] Watermarking

**Audit**: [ ] Security event logging [ ] Anomaly monitoring [ ] Violation alerts [ ] Regular audits

---

## VI. Bootstrap Roadmap

| Phase | Timeline | Goal | Investment |
|-------|----------|------|------------|
| Foundation | Week 1 | Baseline + observation | 4-6 hrs |
| Observation | Weeks 2-4 | Pattern understanding | 30min/day + 1hr/week |
| First Optimizations | Month 2 | 1-2 improvements | 6-8 hrs |
| Memory Infrastructure | Months 3-4 | Multi-tier memory | 12-16 hrs |
| Intelligent Routing | Months 5-6 | Context-aware selection | 8-10 hrs |
| Multi-Agent | Months 7-9 | Complex orchestration | 16-20 hrs |
| Meta-Orchestration | Months 10-12 | Self-optimization | 20-24 hrs |

**Total Year 1**: 60-80 hours investment → 200-400 hours saved

---

## VII. Common Pitfalls

### Over-Delegation Too Early
**Symptom**: Complex tasks to AI before trust established.
**Prevention**: Start copilot mode, gradually increase delegation.
**Recovery**: Reduce scope, add monitoring, rebuild through small successes.

### Insufficient Context
**Symptom**: Low quality despite good prompts.
**Prevention**: Memory systems early, RAG for domain knowledge, examples.
**Recovery**: Audit received context, implement missing memory tiers.

### No Governance Until Crisis
**Symptom**: Deployment without security/compliance controls.
**Prevention**: Design governance from start.
**Recovery**: Immediate audit, retrofit controls, review past actions.

### Tool Accumulation Without Extraction
**Symptom**: Growing similar tools, each used occasionally.
**Prevention**: Default extraction mindset, quarterly consolidation.
**Recovery**: Tool audit, identify overlap, extract primitives, deprecate.

---

## VIII. Maintenance Cadences

| Cadence | Duration | Focus |
|---------|----------|-------|
| Daily | 5 min | Security alerts, failures, anomalies |
| Weekly | 30 min | Usage patterns, friction points, routing |
| Monthly | 2 hrs | Reuse stats, memory performance, costs |
| Quarterly | 4 hrs | Framework validity, consolidation, governance |
| Annual | 8 hrs | Paradigm shifts, strategic direction |

---

## IX. Success Metrics

### Individual
- **Cognitive overhead**: Tool management time ↓, decision fatigue ↓, context switching ↓
- **Capability expansion**: Tasks accomplishable ↑, specialist needs ↓, quality ↑
- **Synapticality**: Intention-to-execution latency ↓, conscious decisions ↓, flow state ↑

### System
- **Memory**: Assembly time ↓, retrieval accuracy ↑, reuse rate ↑
- **Orchestration**: Completion time ↓, coordination overhead ↓, success rate ↑
- **Primitives**: Reuse count ↑, redundancy ↓, composition success ↑
- **Cost**: Cost per task ↓, latency ↓, quality ↑

### Meta
- **Learning rate**: Pattern recognition time ↓, apparatus crystallization ↑, routing accuracy ↑
- **Governance**: Security incidents = 0, compliance = 100%, gate effectiveness ↑

---

## X. Implementation Imperatives

**The core insight**: Build for observation and learning first, add complexity only when patterns justify it.

**The path**:
1. Start lightweight—observation before infrastructure
2. Let patterns emerge—don't prescribe workflows
3. Extract primitives—build on what persists
4. Enable intelligence—observation creates learning
5. Implement governance—safety and quality matter
6. Iterate continuously—system improves with use

**The progression**:
- Tool mastery → intent specification
- Manual workflows → apparatus patterns
- App adoption → primitive composition
- Static systems → reflexive improvement
- Human oversight → intelligent autonomy

---

## VERSION HISTORY

**v2.0.0** (December 2025): Canonization from Technology Lunar - 4 Implementation_Guide.md
- Compressed from ~43K to ~16K (63% reduction)
- Converted Python code to pattern descriptions and tables
- Preserved all production-validated metrics and patterns
- Added CANON frontmatter and hierarchy placement

---

## CROSS-REFERENCES

- [[CANON-00000-SCHEMA-cosmos]] — Master Schema
- [[CANON-30000-INTELLIGENCE-chain]] — Intelligence Chain (Chain Root)
- [[CANON-00006-CORPUS-cosmos]] — Corpus Management

