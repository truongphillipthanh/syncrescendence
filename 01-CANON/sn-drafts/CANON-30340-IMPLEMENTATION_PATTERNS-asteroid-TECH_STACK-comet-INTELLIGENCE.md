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

# CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE (SN Format)

**Note**: This is a Semantic Notation compressed version.
**Original**: 1,845 words, 13,484 characters

---

TERM TheOverEngineeringAntiPattern:
    sutra: "What fails: 1"
    gloss:
        **What fails:**
1. Building infrastructure before validating concepts
2. Elaborate schemas before understanding requirements
3. Rigid taxonomies resisting evolution
4. Tool-centric organization instead of primitive extraction
5. Prescriptive workflows specified upfront

**Core corrections:**

| Anti...
end


TERM ImplementationPrinciples:
    sutra: "Start Lightweight, Scale Intelligently: Don't build comprehensive databases"
    gloss:
        **Start Lightweight, Scale Intelligently**: Don't build comprehensive databases. Start with simple tracking, let patterns emerge, formalize what proves valuable.

**Observation Over Prescription**: Don't design workflows upfront. Use tools naturally, track usage, identify apparatus from observation....
end


TERM PhaseArchitecture:
    sutra: "| Phase | Timeline | Goal | Success Criteria | |-------|----------|------|------------------| | W..."
    gloss:
        | Phase | Timeline | Goal | Success Criteria |
|-------|----------|------|------------------|
| Working | Week 1 | Context continuity | Multi-turn coherence |
| Episodic | Weeks 2-4 | Interaction logging | Pattern identification |
| Semantic | Months 2-3 | Knowledge extraction | Cross-session answer...
end


TERM WorkingMemoryWeek1:
    sutra: "Maintain conversation history in model context window"
    gloss:
        Maintain conversation history in model context window. No external storage required.

**Pattern**: Append user/assistant messages to history, pass full history to LLM.
end


TERM EpisodicMemoryWeeks24:
    sutra: "Log interactions to structured format (JSON/SQLite): timestamp, input, output, metadata, session_id"
    gloss:
        Log interactions to structured format (JSON/SQLite): timestamp, input, output, metadata, session_id.

**Pattern**: Append-only log file, chronological retrieval, keyword search.
end


TERM SemanticMemoryMonths23:
    sutra: "Extract and retrieve factual knowledge"
    gloss:
        Extract and retrieve factual knowledge.

**Option A (Simple)**: LLM-based fact extraction + keyword search in fact store.

**Option B (Production)**: Vector database (Pinecone, etc.) with embeddings for semantic retrieval.
end


TERM ProceduralMemoryMonths34:
    sutra: "Cache high-frequency workflows as reusable functions"
    gloss:
        Cache high-frequency workflows as reusable functions.

**Pattern**: Analyze episodic log for repeated sequences → convert to executable procedure → invoke without re-reasoning.
end


TERM UnifiedMemoryMonths46:
    sutra: "Intelligent multi-tier retrieval hierarchy: 1"
    gloss:
        Intelligent multi-tier retrieval hierarchy:
1. Working memory (fastest)
2. Procedural cache (fast)
3. Semantic knowledge (medium)
4. Similar episodes (slower)
end


TERM MemoryArchitecturePatterns:
    sutra: "Context Window Optimization: - Static knowledge at beginning (enables caching) - Recent conversat..."
    gloss:
        **Context Window Optimization**:
- Static knowledge at beginning (enables caching)
- Recent conversation in middle
- Current query at end
- Result: 90% cost reduction via prompt caching

**Hierarchical Summarization**:
- Detailed episodes → session summaries → weekly digests → monthly insights
- Ret...
end


TERM DecisionTree:
    sutra: "`` Is workflow deterministic with clear stages"
    gloss:
        ```
Is workflow deterministic with clear stages?
├─ Yes → Sequential coordination (60%+ of workflows)
└─ No
   └─ Are subtasks independent?
      ├─ Yes → Concurrent execution
      └─ No
         └─ Is brainstorming/creativity needed?
            ├─ Yes → Group chat (max 3 agents)
            └─ No...
end


TERM Pattern1SequentialCoordination:
    sutra: "When: Linear pipeline with clear stage boundaries"
    gloss:
        **When**: Linear pipeline with clear stage boundaries.

**Structure**: Research → Draft → Edit → Format (stage outputs feed next stage).

**Tips**:
- Add checkpoints for failure recovery
- Log intermediate results
- Time stages to identify bottlenecks
- Cache outputs for common inputs
end


TERM Pattern2ConcurrentExecution:
    sutra: "When: Independent subtasks that parallelize"
    gloss:
        **When**: Independent subtasks that parallelize.

**Structure**: Spawn parallel tasks → gather results → synthesize.

**Validation**: 45% faster than sequential for independent tasks.

**Tips**:
- Set timeout per task (prevent blocking)
- Retry with exponential backoff
- Monitor API rate limits
- Pr...
end


TERM Pattern3CriticRefinerLoop:
    sutra: "When: Quality > speed, iterative improvement beneficial"
    gloss:
        **When**: Quality > speed, iterative improvement beneficial.

**Structure**: Generate → Critique → Refine (loop until threshold met).

**Validation**: 30-40% quality improvement on complex generation.

**Tips**:
- Clear evaluation criteria
- Limit iterations (diminishing returns)
- Track iteration c...
end


TERM Pattern4SpecialistSwarm:
    sutra: "When: Complex problem benefiting from multiple expert perspectives"
    gloss:
        **When**: Complex problem benefiting from multiple expert perspectives.

**Structure**: Parallel specialists → Coordinator synthesis.

**Validation**: 45% faster resolution, 60% higher accuracy than single-agent.

**Tips**:
- Ensure specialists are complementary, not redundant
- Weight by historical...
end


TERM Pattern5HubandSpoke:
    sutra: "When: Mission-critical applications requiring centralized oversight"
    gloss:
        **When**: Mission-critical applications requiring centralized oversight.

**Structure**: Hub creates plan → routes to specialists → monitors → synthesizes.

**Tips**:
- Circuit breakers in hub
- Log all hub decisions
- Approval gates for high-impact actions
- Monitor hub (it's the bottleneck)

---
end


TERM PromptCaching:
    sutra: "Economics: - Cache write: 1.25x (5min TTL) or 2x (1hr TTL) - Cache read: 0.1x (90% discount) - Ca..."
    gloss:
        **Economics**:
- Cache write: 1.25x (5min TTL) or 2x (1hr TTL)
- Cache read: 0.1x (90% discount)
- Cache miss: Full price

**Break-even**: Static docs cache after 2 uses. Semi-static content after 10+ daily uses.

**Pattern**: Structure prompts with static content first, dynamic last. Cache static p...
end


TERM RAGStrategySelection:
    sutra: "`` Is knowledge static or dynamic"
    gloss:
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
end


TERM RAGImplementations:
    sutra: "| Type | When | Cost | Latency | Accuracy | |------|------|------|---------|----------| | Basic |..."
    gloss:
        | Type | When | Cost | Latency | Accuracy |
|------|------|------|---------|----------|
| Basic | Simple Q&A | ~1¢ | 200-500ms | 70% |
| Hybrid | Production systems | ~1-2¢ | 400-800ms | 85-90% |
| Agentic | Research, high-stakes | ~5-15¢ | 2-8s | 92-96% |

**Basic RAG**: Embed query → vector search...
end


TERM ContextOverflowStrategies:
    sutra: "Sliding Window: Process chunks with overlap for continuity"
    gloss:
        **Sliding Window**: Process chunks with overlap for continuity.

**Hierarchical Summarization**: Sections → section summaries → combined summary (recurse if needed).

**Context Offloading**: Heavy processing in separate agent, return summary only. 8x cleaner signal.

---
end


TERM ThreatModel:
    sutra: "- Prompt injection: Malicious inputs overriding instructions - Agent hijacking: Tricking agent in..."
    gloss:
        - **Prompt injection**: Malicious inputs overriding instructions
- **Agent hijacking**: Tricking agent into unauthorized actions
- **Tool misuse**: Access beyond intended scope
- **Data exfiltration**: Sensitive info in outputs
- **Jailbreaking**: Bypassing safety constraints
end


TERM DefensePatterns:
    sutra: "1"
    gloss:
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
- Content po...
end


TERM ProductionSecurityChecklist:
    sutra: "Input: [ ] Injection validation [ ] PII masking [ ] Rate limiting [ ] File sanitization  Agent: [..."
    gloss:
        **Input**: [ ] Injection validation [ ] PII masking [ ] Rate limiting [ ] File sanitization

**Agent**: [ ] Capability access control [ ] Action logging [ ] Resource limits [ ] Circuit breakers

**Output**: [ ] PII filtering [ ] Content policy [ ] Anti-exfiltration [ ] Watermarking

**Audit**: [ ] S...
end


TERM VIBootstrapRoadmap:
    sutra: "| Phase | Timeline | Goal | Investment | |-------|----------|------|------------| | Foundation | ..."
    gloss:
        | Phase | Timeline | Goal | Investment |
|-------|----------|------|------------|
| Foundation | Week 1 | Baseline + observation | 4-6 hrs |
| Observation | Weeks 2-4 | Pattern understanding | 30min/day + 1hr/week |
| First Optimizations | Month 2 | 1-2 improvements | 6-8 hrs |
| Memory Infrastructu...
end


TERM OverDelegationTooEarly:
    sutra: "Symptom: Complex tasks to AI before trust established"
    gloss:
        **Symptom**: Complex tasks to AI before trust established.
**Prevention**: Start copilot mode, gradually increase delegation.
**Recovery**: Reduce scope, add monitoring, rebuild through small successes.
end


TERM InsufficientContext:
    sutra: "Symptom: Low quality despite good prompts"
    gloss:
        **Symptom**: Low quality despite good prompts.
**Prevention**: Memory systems early, RAG for domain knowledge, examples.
**Recovery**: Audit received context, implement missing memory tiers.
end


TERM NoGovernanceUntilCrisis:
    sutra: "Symptom: Deployment without security/compliance controls"
    gloss:
        **Symptom**: Deployment without security/compliance controls.
**Prevention**: Design governance from start.
**Recovery**: Immediate audit, retrofit controls, review past actions.
end


TERM ToolAccumulationWithoutExtraction:
    sutra: "Symptom: Growing similar tools, each used occasionally"
    gloss:
        **Symptom**: Growing similar tools, each used occasionally.
**Prevention**: Default extraction mindset, quarterly consolidation.
**Recovery**: Tool audit, identify overlap, extract primitives, deprecate.

---
end


TERM VIIIMaintenanceCadences:
    sutra: "| Cadence | Duration | Focus | |---------|----------|-------| | Daily | 5 min | Security alerts, ..."
    gloss:
        | Cadence | Duration | Focus |
|---------|----------|-------|
| Daily | 5 min | Security alerts, failures, anomalies |
| Weekly | 30 min | Usage patterns, friction points, routing |
| Monthly | 2 hrs | Reuse stats, memory performance, costs |
| Quarterly | 4 hrs | Framework validity, consolidation,...
end


TERM Individual:
    sutra: "- Cognitive overhead: Tool management time ↓, decision fatigue ↓, context switching ↓ - Capabilit..."
    gloss:
        - **Cognitive overhead**: Tool management time ↓, decision fatigue ↓, context switching ↓
- **Capability expansion**: Tasks accomplishable ↑, specialist needs ↓, quality ↑
- **Synapticality**: Intention-to-execution latency ↓, conscious decisions ↓, flow state ↑
end


TERM System:
    sutra: "- Memory: Assembly time ↓, retrieval accuracy ↑, reuse rate ↑ - Orchestration: Completion time ↓,..."
    gloss:
        - **Memory**: Assembly time ↓, retrieval accuracy ↑, reuse rate ↑
- **Orchestration**: Completion time ↓, coordination overhead ↓, success rate ↑
- **Primitives**: Reuse count ↑, redundancy ↓, composition success ↑
- **Cost**: Cost per task ↓, latency ↓, quality ↑
end


TERM Meta:
    sutra: "- Learning rate: Pattern recognition time ↓, apparatus crystallization ↑, routing accuracy ↑ - Go..."
    gloss:
        - **Learning rate**: Pattern recognition time ↓, apparatus crystallization ↑, routing accuracy ↑
- **Governance**: Security incidents = 0, compliance = 100%, gate effectiveness ↑

---
end


TERM XImplementationImperatives:
    sutra: "The core insight: Build for observation and learning first, add complexity only when patterns jus..."
    gloss:
        **The core insight**: Build for observation and learning first, add complexity only when patterns justify it.

**The path**:
1. Start lightweight—observation before infrastructure
2. Let patterns emerge—don't prescribe workflows
3. Extract primitives—build on what persists
4. Enable intelligence—obs...
end


TERM VERSIONHISTORY:
    sutra: "v2.0.0 (December 2025): Canonization from Technology Lunar - 4 Implementation_Guide.md - Compress..."
    gloss:
        **v2.0.0** (December 2025): Canonization from Technology Lunar - 4 Implementation_Guide.md
- Compressed from ~43K to ~16K (63% reduction)
- Converted Python code to pattern descriptions and tables
- Preserved all production-validated metrics and patterns
- Added CANON frontmatter and hierarchy place...
end
