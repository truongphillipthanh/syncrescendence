# Research Protocols: Methodologies and Quality Standards

## I. Research Methodology Framework

### The Source Triad Method

For every decision-bearing question, execute three research passes:

#### Pass 1: Primary Sources
**Target**: Original material from authoritative sources

**Preferred sources**:
- Academic papers (peer-reviewed journals, conference proceedings)
- Official documentation (product docs, technical specifications)
- Company blogs (engineering/research teams at elite institutions)
- Government reports (SEC filings, policy documents)
- Patent filings (especially for technical mechanisms)

**Evaluation criteria**:
- Is this the original source of the claim?
- What's the credibility of the institution/author?
- How recent is this information?
- What's the methodology used?

**Red flags**:
- Secondary reporting without links to primary source
- Marketing material masquerading as research
- Claims without evidence or methodology
- Unclear authorship or institution

#### Pass 2: High-Signal Secondary Analysis
**Target**: Expert interpretation and synthesis

**Preferred sources**:
- Technical deep-dives (blog posts from practitioners)
- Research reviews (survey papers, meta-analyses)
- Industry analysis (from reputable analysts)
- Expert commentary (from recognized authorities)

**Evaluation criteria**:
- Does this add interpretation beyond the primary source?
- What's the expertise of the analyst?
- Is the analysis rigorous or speculative?
- Does it reveal non-obvious implications?

**Red flags**:
- Hype or sensationalism
- Cherry-picking evidence
- Conflicting interest not disclosed
- Extrapolation far beyond evidence

#### Pass 3: Counter-Position
**Target**: Alternative interpretations, critiques, limitations

**Preferred sources**:
- Academic rebuttals and responses
- Skeptical analyses
- Limitation acknowledgments (often in primary source's discussion section)
- Competing approaches or frameworks

**Evaluation criteria**:
- What are the genuine limitations?
- What assumptions might not hold?
- What alternative explanations exist?
- Where might this approach fail?

**Red flags**:
- Strawman arguments
- Dismissal without engagement with evidence
- Ideological opposition without substantive critique

### Decision-Bearing Questions First

**Before researching, answer**:
1. What decision does this inform?
2. What would we do differently if the answer is X vs. Y?
3. What level of confidence is needed to act?
4. What's the cost of being wrong?

**Only research questions where**:
- Answer materially changes decisions
- Current uncertainty is blocking action
- Investment of research time is justified by decision impact

**Skip research when**:
- Answer doesn't affect decisions
- Uncertainty is acceptable given stakes
- Other information is more decision-critical

### Verdicting Process

For each research question, produce a verdict with five components:

#### 1. Claim
**Format**: Clear, testable statement

**Example**: "Sonnet 4.5 can maintain reliable performance over 30-hour work sessions"

**Not**: "Sonnet 4.5 is better for long tasks"

#### 2. Confidence Level
**Scale**: 
- **High (>85%)**: Multiple primary sources, consensus among experts, replicated results
- **Medium (50-85%)**: Primary source plus supporting analysis, plausible but not conclusive
- **Low (<50%)**: Single report, no verification, speculative extrapolation
- **Speculative (<25%)**: Rumor, prediction, no evidence yet

**Tagging**: Explicitly state confidence percentage and rationale

#### 3. Recency
**Format**: Date of primary source + freshness assessment

**Freshness categories**:
- **Current (0-3 months)**: Likely still accurate
- **Recent (3-12 months)**: Probably still relevant, worth checking
- **Dated (1-2 years)**: May have changed, verify if critical
- **Stale (>2 years)**: Likely outdated, use with caution

#### 4. Volatility Tag
**Categories**:
- **Stable**: Unlikely to change (fundamental principles, established patterns)
- **Shifting**: Actively evolving (current capabilities, best practices)
- **Speculative**: Not yet real (predictions, roadmaps, research directions)

**Implications**:
- Stable claims can be built upon with confidence
- Shifting claims need freshness checking
- Speculative claims require contingency planning

#### 5. Design Delta
**Format**: "If this is true, then we should [specific action]"

**Example**: "If Sonnet 4.5 maintains reliable 30-hour sessions, then we can design workflows that span multiple days without checkpoint/resume logic"

**Not**: "This is interesting information"

**Test**: Can someone reading this verdict make a different decision? If no, clarify the design delta.

### Ledgering and Contradiction Management

**Research Log Format**:
```
Entry ID: <unique identifier>
Timestamp: <when recorded>
Question: <decision-bearing question>
Source: <primary source with URL>
Gist: <one-sentence summary>
Extracted Claims: <numbered list>
Confidence: <percentage + rationale>
Recency: <date + freshness category>
Volatility: <stable/shifting/speculative>
Design Delta: <if true, then...>
Contradictions: <IDs of conflicting entries>
Next Actions: <follow-up needed?>
```

**When contradictions arise**:
1. Document both claims explicitly
2. Assess relative source quality
3. Identify what would resolve the contradiction
4. Mark as "pending resolution"
5. Use most conservative estimate for decisions
6. Flag for follow-up research if critical

**Contradiction Resolution Priority**:
- **Critical**: Blocks major decisions → Resolve immediately
- **Important**: Affects strategy → Resolve within sprint
- **Minor**: Interesting but not blocking → Track for future
- **Ignorable**: No decision impact → Note and move on

## II. Research Anti-Patterns (What to Avoid)

### Anti-Pattern 1: Benchmark Shopping
**Description**: Selectively citing benchmarks that support desired conclusion

**Why it's harmful**: Creates false confidence, ignores limitations, leads to poor decisions

**How to avoid**:
- Always include context (what was tested, how, limitations)
- Cite competing benchmarks
- Note what's NOT measured
- Acknowledge when benchmarks don't match real use cases

**Better approach**: Describe evaluation landscape comprehensively, let reader assess

### Anti-Pattern 2: Link Dumping
**Description**: Including many sources without synthesis or verdict

**Why it's harmful**: Appears thorough but provides no guidance, overwhelms reader, doesn't answer question

**How to avoid**:
- Every source must have explicit contribution
- Synthesize into unified verdict
- Provide clear design delta
- Include only sources that change the analysis

**Better approach**: Few well-analyzed sources > many undigested links

### Anti-Pattern 3: Hype Amplification
**Description**: Uncritically repeating marketing claims or speculative predictions

**Why it's harmful**: Creates false expectations, misallocates resources, damages credibility

**How to avoid**:
- Distinguish claims from evidence
- Note when source has commercial interest
- Separate current capability from roadmap
- Tag speculation explicitly

**Better approach**: "Company X claims Y, but current evidence shows Z"

### Anti-Pattern 4: Recency Bias
**Description**: Assuming newer information is always better

**Why it's harmful**: Ignores stable principles, chases shiny objects, creates thrash

**How to avoid**:
- Assess volatility explicitly
- Value timeless principles
- Separate fundamental from fashionable
- Build on stable foundations

**Better approach**: Layer stable principles + shifting practices + speculative futures

### Anti-Pattern 5: Confirmation Bias
**Description**: Seeking information that supports existing beliefs

**Why it's harmful**: Misses important challenges, creates blind spots, leads to preventable failures

**How to avoid**:
- Actively seek counter-arguments
- Red team your own proposals
- Include Pass 3 (counter-position) always
- Reward finding limitations of your own ideas

**Better approach**: "Here's the strongest case AGAINST this approach..."

## III. Frontier Tracking (Staying Current)

### Target Domains

**Elite Academic Institutions**:
- Stanford (Agentic Context Engineering, HAI)
- MIT (CSAIL, Brain and Cognitive Sciences)
- UC Berkeley (BAIR, Center for Human-Compatible AI)
- CMU (Machine Learning Department)
- Oxford/Cambridge/UCL (AI research groups)

**Leading AI Labs**:
- Anthropic (Constitutional AI, long-context models)
- OpenAI (GPT series, reasoning systems)
- Google DeepMind (AlphaGo to Gemini)
- Meta AI (LLaMA, fundamental research)
- xAI (Grok, explanation focus)

**Mission-Driven Organizations**:
- Center for AI Safety
- AI Alignment Forum
- Future of Humanity Institute
- Effective Altruism AI work

**Commercial/Product Leaders**:
- Cursor (AI-native IDE)
- Replit (AI-assisted development)
- Perplexity (AI search)
- Palantir (ontology and FDE model)
- Anduril (embodied AI, Lattice)

### Tracking Methodology

**Weekly Scan**:
- Key lab blogs and Twitter accounts
- ArXiv cs.AI and cs.CL sections
- Hacker News front page
- Relevant subreddits (r/MachineLearning, r/LocalLLaMA)

**Monthly Deep Dive**:
- Read 3-5 significant papers in depth
- Analyze major product releases
- Update frontier map with new developments
- Reassess previous predictions

**Quarterly Review**:
- Comprehensive landscape assessment
- Identify emerging paradigm shifts
- Update taxonomies with new patterns
- Revise theoretical frameworks if needed

### Frontier Map Structure

**Claim → Implications Graph**:
```json
{
  "claim_id": "sonnet_30h_sessions",
  "claim": "Sonnet 4.5 maintains reliable performance over 30-hour sessions",
  "source": "Anthropic blog, 2025-01-15",
  "confidence": 0.75,
  "volatility": "shifting",
  "dependencies": ["extended_context", "persistent_memory"],
  "implications": [
    "multi_day_workflows",
    "reduced_checkpoint_overhead",
    "new_interaction_patterns"
  ],
  "contradictions": [],
  "next_verification": "2025-04-15"
}
```

**Benefits**:
- Queryable ("what breaks if claim X flips?")
- Traceable (why do we believe this?)
- Updateable (mark claims as verified/refuted)
- Actionable (what implications follow?)

## IV. Quality Standards and Evaluation

### Research Quality Checklist

**For each research deliverable, verify**:

- [ ] Every claim has source attribution
- [ ] Sources are primary when possible
- [ ] Secondary sources add analysis, not just relay
- [ ] Counter-positions included
- [ ] Confidence levels explicit with rationale
- [ ] Recency and volatility tagged
- [ ] Design deltas specified
- [ ] Contradictions acknowledged
- [ ] No benchmark shopping
- [ ] No link dumping without synthesis
- [ ] Hype distinguished from evidence
- [ ] Limitations explicitly noted

### Report Quality Standards

**Structure**:
1. **Executive Summary**: Key findings and decisions they inform
2. **Decision-Bearing Questions**: What we needed to answer and why
3. **Methodology**: How research was conducted
4. **Findings**: By question, with verdicts
5. **Implications**: Design deltas and action items
6. **Limitations**: What we don't know, what could change
7. **Next Steps**: Follow-up research needed

**Writing Quality**:
- Lead with conclusions (inverted pyramid)
- Use clear, testable claims
- Separate evidence from interpretation
- Provide sufficient context for decisions
- Include enough detail for verification
- Avoid jargon without definition

**Intellectual Honesty**:
- Acknowledge uncertainty
- Note conflicts of interest
- Present contrary evidence
- Distinguish speculation from fact
- Update when proven wrong

### Peer Review Protocol

**Before finalizing research**:

1. **Self-review**: Read with adversarial mindset
   - What could I be wrong about?
   - What evidence am I ignoring?
   - What assumptions am I making?
   - How would a skeptic respond?

2. **Source validation**: Verify claims
   - Can I find the original source?
   - Does it actually say what I claim?
   - Is context preserved?
   - Are quotes accurate?

3. **Logic check**: Test reasoning
   - Do conclusions follow from evidence?
   - Are there alternative explanations?
   - What would falsify this?
   - What's the strongest counter-argument?

4. **Impact assessment**: Consider consequences
   - What decisions will this inform?
   - What's the cost of being wrong?
   - Do we need higher confidence?
   - Should we hedge or delay?

## V. Context-Specific Research Patterns

### When Evaluating New AI Capabilities

**Key questions to answer**:
1. What's the actual capability vs. the claim?
2. What are the reliability characteristics?
3. What are the cost/latency trade-offs?
4. What are the failure modes?
5. How does it compare to alternatives?
6. What's the adoption path?

**Specific tests to run** (when possible):
- Replicate benchmark results
- Try edge cases and adversarial inputs
- Stress test with real use cases
- Compare to previous best alternative
- Assess learning curve for users

**Red flags that indicate over-hype**:
- Only cherry-picked examples shown
- No discussion of limitations
- Comparison to weak baselines
- Unclear about when it fails
- No cost/performance data

### When Assessing Paradigm Shifts

**Key questions to answer**:
1. What's actually changing fundamentally?
2. What's just incremental improvement?
3. What enables this shift now?
4. What are the adoption barriers?
5. What's the trajectory?

**Evidence needed**:
- Technical breakthrough that changes economics
- Real user behavior changes (not just early adopters)
- Multiple independent validation sources
- Clear mechanism explaining the shift
- Comparison to past "paradigm shifts" that fizzled

**Distinguish**:
- Capability unlock (truly new possible things)
- Efficiency gain (same things, cheaper/faster)
- Interface improvement (same capability, better UX)
- Hype cycle (attention but no fundamental change)

### When Exploring Emerging Frameworks

**Key questions to answer**:
1. What problem does this solve?
2. Why wasn't it solved before?
3. What are the core principles?
4. How does it relate to existing approaches?
5. What are the boundary conditions?

**Analysis approach**:
- Map to existing taxonomies
- Identify truly novel elements
- Test against known edge cases
- Assess generality vs. specificity
- Evaluate adoption feasibility

**Integration strategy**:
- Identify where it fits in current frameworks
- Note contradictions with existing models
- Assess whether it requires revision of fundamentals
- Plan for gradual adoption vs. paradigm replacement

### When Evaluating Infrastructure Services

**New section for AI infrastructure evaluation**

**Key questions to answer**:
1. What neo-layer does this occupy? (Vector DB, Inference, Routing, etc.)
2. What object types does it provide? (O.SVC, O.MOD, O.DP, etc.)
3. Own vs. lease assessment based on sensitivity/latency/leverage?
4. What are the lock-in risks and mitigation strategies?
5. Does vendor meet capability contract requirements?

**Source Triad for Infrastructure**:

**Pass 1: Vendor Primary Sources**
- Official documentation (API specs, architecture docs)
- Performance benchmarks (vendor-published)
- Pricing documentation (cost models, tiers)
- Security & compliance certifications (SOC 2, ISO 27001, GDPR)
- Service Level Agreements (uptime, latency guarantees)

**Pass 2: Independent Analysis**
- Third-party benchmarks (compare to vendor claims)
- Customer case studies (real-world usage patterns)
- Technical reviews (deep-dives from practitioners)
- Cost analysis (TCO comparisons across vendors)
- Architecture reviews (how does it actually work)

**Pass 3: Critical Assessment**
- Known limitations (from vendor docs or issues)
- Customer complaints (support forums, Twitter, reviews)
- Alternative vendors (competitive analysis)
- Build vs. buy analysis (cost of self-hosting)
- Exit strategy feasibility (can we actually leave?)

**Infrastructure-Specific Evaluation Dimensions**:

**Technical Performance**:
- Latency: p50, p95, p99 measured (not just claimed)
- Throughput: requests/second at scale
- Reliability: Historical uptime, incident frequency
- Quality: Model accuracy, retrieval relevance, etc.
- Scalability: Cost/performance at 10x, 100x volume

**Business Viability**:
- Funding: Runway, profitability trajectory
- Market position: Customer count, growth rate
- Strategic risk: Acquisition likelihood, pivot risk
- Pricing stability: Historical price changes
- Support quality: Response time, resolution rate

**Governance & Compliance**:
- Security: Certifications, audit reports, penetration testing
- Privacy: Data handling practices, residency options
- Compliance: Industry-specific requirements (HIPAA, etc.)
- Audit capability: Logging, tracing, reporting
- Incident response: Communication, remediation process

**Lock-in Risk**:
- Data portability: Export format, completeness, ease
- API compatibility: Proprietary vs. standard interfaces
- Feature dependency: Reliance on unique capabilities
- Migration cost: Engineering effort to switch
- Alternative availability: Competitive landscape

**Capability Contract Assessment**:
- Performance SLOs: Documented, measured, enforced?
- Data governance: Residency, retention, deletion guarantees?
- Provenance: Can we trace model outputs to sources?
- Exit strategy: Clear migration path? Transition support?
- Cost accounting: Transparent pricing? Optimization options?

**Vendor Scoring Rubric**:
```
Technical Capability:    [1-5] × 0.40 = [Score]
Business Viability:      [1-5] × 0.30 = [Score]
Governance & Compliance: [1-5] × 0.20 = [Score]
Lock-in Risk:           [1-5] × 0.10 = [Score]
                         ____________
Total Weighted Score:               [Score]

Qualitative Notes:
- Unique strengths: 
- Specific concerns:
- Recommended use cases:
- Alternatives to consider:
```

**Decision Framework Integration**:

After completing infrastructure research, map findings to economic decision matrix:

```
Data Sensitivity:    [LOW | MEDIUM | HIGH]
Latency Requirements: [FLEXIBLE | MODERATE | IMPORTANT | CRITICAL]
Economic Leverage:   [LOW | MEDIUM | HIGH]
Lock-in Risk:        [LOW | MODERATE | MATERIAL]
                     ↓
Decision:           [OWN | LEASE | HYBRID]
Confidence:         [LOW | MEDIUM | HIGH]
```

**Research Output: Infrastructure Evaluation Report**

```markdown
# Infrastructure Service Evaluation: [Service Name]

## Executive Summary
- Vendor: [Name]
- Neo-layer: [NL1-NL8]
- Recommendation: [OWN | LEASE | HYBRID | DO NOT USE]
- Confidence: [HIGH | MEDIUM | LOW]
- Decision rationale: [Key factors]

## Technical Assessment
- Performance: [Summary with metrics]
- Reliability: [Uptime, incident history]
- Quality: [Capability assessment]
- Scalability: [Cost/performance at scale]
- Rating: [1-5]

## Business Assessment
- Financial viability: [Funding, profitability]
- Market position: [Customer base, growth]
- Strategic risk: [Acquisition, pivot concerns]
- Support quality: [Response, resolution]
- Rating: [1-5]

## Governance Assessment
- Security: [Certifications, practices]
- Privacy: [Data handling, residency]
- Compliance: [Industry requirements met?]
- Audit capability: [Logging, reporting]
- Rating: [1-5]

## Lock-in Assessment
- Data portability: [Export ease]
- API compatibility: [Proprietary vs. standard]
- Feature dependency: [Unique features needed?]
- Migration cost: [Effort to switch]
- Rating: [1-5]

## Capability Contract
- Performance SLOs: [Documented guarantees]
- Data governance: [Residency, retention, deletion]
- Provenance: [Traceability]
- Exit strategy: [Migration support]
- Cost accounting: [Pricing model]

## Economic Decision
- Data sensitivity: [Assessment]
- Latency requirements: [Assessment]
- Economic leverage: [Assessment]
- Lock-in risk: [Assessment]
- **Decision**: [OWN | LEASE | HYBRID]

## Alternatives Considered
- [Alternative 1]: [Brief comparison]
- [Alternative 2]: [Brief comparison]

## Implementation Recommendations
- Deployment strategy: [Phased rollout, etc.]
- Risk mitigations: [Specific actions]
- Success metrics: [How to measure]
- Review schedule: [When to reassess]

## Next Actions
- [ ] Action item 1
- [ ] Action item 2
```

### When Evaluating Tool for Primitive Extraction

**Key questions to answer**:
1. What primitives does this tool contain?
2. Which primitives are unique vs. duplicative?
3. What's the extraction difficulty for each primitive?
4. What reuse potential does each primitive have?
5. Should we adopt tool or just extract primitives?

**Extraction Research Process**:

**Phase 1: Tool Survey**
- Feature inventory (what does it do?)
- Interface patterns (how do you interact?)
- Platform characteristics (desktop/mobile/XR/etc.)
- Performance characteristics (latency, reliability)
- Quality assessment (does it work well?)

**Phase 2: Primitive Identification**
- Interface primitives (navigation, input, layout patterns)
- Capability primitives (transformations, operations)
- Algorithm primitives (processing approaches)
- Platform optimizations (how adapted to platform)

**Phase 3: Overlap Analysis**
- Compare to existing primitive catalog
- Identify unique primitives (new capabilities)
- Identify redundant primitives (already have)
- Assess quality differential (better/worse than existing)

**Phase 4: Extraction Feasibility**
- Technical difficulty (can we extract this?)
- Legal constraints (licensing, copyright)
- Maintenance burden (effort to preserve)
- Composition potential (will this combine well?)

**Phase 5: Reuse Validation**
- Test extraction in composition
- Measure performance in real usage
- Assess combination with other primitives
- Document successful patterns

**Research Output: Tool Extraction Report**

```markdown
# Tool Extraction Analysis: [Tool Name]

## Tool Overview
- Category: [Type of tool]
- Platform: [Desktop/Mobile/XR/Ambient/CLI]
- Entity state: [Active/Trial/Repository]
- Assessment date: [Date]

## Identified Primitives

### Interface Primitives
1. [Primitive name]
   - Description: [What it does]
   - Uniqueness: [Novel/Redundant/Better than existing]
   - Extraction difficulty: [Low/Medium/High]
   - Reuse potential: [High/Medium/Low]

### Capability Primitives
[Same structure as above]

### Algorithm Primitives
[Same structure as above]

## Unique Primitives (Worth Extracting)
- [Primitive 1]: [Why valuable]
- [Primitive 2]: [Why valuable]

## Redundant Primitives (Already Have)
- [Primitive 1]: [What we already have]
- [Primitive 2]: [Quality comparison]

## Consolidation Opportunities
- Could replace: [Existing tool names]
- With extraction of: [These primitives]
- Estimated effort: [Time investment]

## Recommendation
- [ ] Adopt tool (unique value beyond primitives)
- [ ] Extract primitives only (primitives valuable, tool not)
- [ ] Skip (no unique value)

## Extraction Plan
IF extracting:
1. [Primitive 1]: [Extraction approach]
2. [Primitive 2]: [Extraction approach]
Validation: [How to test reuse]
Timeline: [Estimated duration]
```

## VI. Research Output Formats

### Research Report (Comprehensive Analysis)

**When to use**: Major strategic questions, significant uncertainty, high decision impact

**Structure**:
```
Title: [Question being answered]

Executive Summary
- Key findings (3-5 bullet points)
- Primary recommendation
- Confidence level

Background
- Why this question matters
- Current state of understanding
- What's at stake

Methodology
- How research was conducted
- Sources consulted
- Analysis approach

Findings
[For each sub-question]
- Claim
- Evidence
- Confidence assessment
- Implications

Synthesis
- Overall conclusion
- Design deltas
- Trade-offs

Limitations
- What we don't know
- What could change
- Uncertainties remaining

Next Steps
- Follow-up research
- Decision points
- Review schedule
```

### Research Log Entry (Quick Investigation)

**When to use**: Targeted questions, confirming/disconfirming specific claims, updating frontier map

**Structure**:
```
Question: [Specific claim to verify]
Source: [Primary source URL]
Finding: [What the source actually says]
Confidence: [High/Medium/Low + rationale]
Design Delta: [If true, then...]
Next: [Follow-up needed?]
```

### Frontier Map Update (Tracking Developments)

**When to use**: New capability announcements, research breakthroughs, paradigm evolution

**Structure**:
```json
{
  "development": "Description",
  "source": "URL",
  "date": "YYYY-MM-DD",
  "implications": [
    "implication 1",
    "implication 2"
  ],
  "related_claims": ["claim_id_1", "claim_id_2"],
  "confidence": 0.7,
  "volatility": "shifting"
}
```

### Decision Brief (Action-Oriented)

**When to use**: Immediate decision needed, stakeholder briefing, proposal evaluation

**Structure**:
```
Decision: [What needs to be decided]

Recommendation: [Clear, actionable recommendation]

Rationale:
- Supporting evidence
- Why alternatives are inferior
- Risks and mitigations

If wrong:
- What happens if this recommendation is wrong
- How we'll know
- Correction strategy

Timeline: [When decision is needed, when we'll review]
```

### Infrastructure Evaluation Report

**When to use**: Evaluating AI services for adoption, vendor comparison, build vs. buy decisions

**Structure**: See detailed template in Section V under "Infrastructure Service Evaluation"

### Tool Extraction Report

**When to use**: Assessing tools for primitive extraction, consolidation planning, adoption decisions

**Structure**: See detailed template in Section V under "Tool Extraction Analysis"

## VII. Capability Contract Audit Process

### Purpose

Systematic review of infrastructure service providers to ensure compliance with capability contracts and identify risks.

### Audit Cadence

**Monthly (Quick Check)**:
- Review performance metrics (meet SLOs?)
- Check cost vs. budget
- Scan incident reports
- Note any degradation trends

**Quarterly (Comprehensive Audit)**:
- Full capability contract review
- Vendor relationship health check
- Alternative evaluation (market changes?)
- Capability contract renegotiation if needed

**Annual (Strategic Review)**:
- Own vs. lease reassessment
- Vendor landscape analysis
- Major migration consideration
- Long-term vendor strategy

### Audit Checklist

**Performance SLOs**:
- [ ] Latency targets met? (p50, p95, p99)
- [ ] Availability target met? (uptime %)
- [ ] Throughput adequate? (requests/second)
- [ ] Quality maintained? (accuracy, relevance)
- [ ] Degradation trends? (getting worse?)

**Data Governance**:
- [ ] Data residency compliant? (correct regions)
- [ ] Retention policy followed? (deletion on schedule)
- [ ] Export capability verified? (can we get data out)
- [ ] Encryption current? (at rest and in transit)
- [ ] Access controls appropriate? (who can access)

**Provenance & Explainability**:
- [ ] Model versions documented? (what changed when)
- [ ] Training data disclosed? (what's it trained on)
- [ ] Inference traceable? (output → input path)
- [ ] Explanations adequate? (understand decisions)

**Cost Accounting**:
- [ ] Actual vs. expected costs? (within budget?)
- [ ] Pricing changes? (new tiers, rate adjustments)
- [ ] Optimization opportunities? (cheaper alternatives)
- [ ] ROI positive? (value exceeds cost)

**Exit Strategy**:
- [ ] Migration path still viable? (can we leave)
- [ ] Alternatives available? (market options)
- [ ] Data extraction tested? (verified we can export)
- [ ] Transition support adequate? (vendor cooperation)

### Audit Findings Classification

**Green (No action needed)**:
- All criteria met
- Performance stable or improving
- Cost within expectations
- No significant risks

**Yellow (Monitor closely)**:
- Some criteria borderline
- Minor performance degradation
- Cost creeping higher
- Emerging risks identified

**Red (Action required)**:
- Critical criteria violated
- Significant performance issues
- Cost overruns
- Material risks requiring mitigation

### Audit Response Actions

**For Yellow findings**:
1. Increase monitoring frequency
2. Engage vendor to discuss concerns
3. Research alternatives (don't commit yet)
4. Set clear improvement targets with deadlines
5. Escalate to Red if no improvement

**For Red findings**:
1. Immediate vendor escalation
2. Serious alternative evaluation
3. Migration planning (may not execute but be ready)
4. Risk mitigation (reduce dependency if possible)
5. Executive notification (if strategic impact)

### Audit Report Template

```markdown
# Capability Contract Audit: [Service Name]

**Audit date**: [Date]
**Audit type**: [Monthly | Quarterly | Annual]
**Previous audit**: [Date and overall status]
**Overall status**: [GREEN | YELLOW | RED]

## Performance SLOs
**Status**: [GREEN | YELLOW | RED]
- Latency: [Actual vs. target]
- Availability: [Actual vs. target]
- Throughput: [Actual vs. target]
- Quality: [Actual vs. target]
**Issues**: [List any problems]
**Action required**: [If yellow/red]

## Data Governance
**Status**: [GREEN | YELLOW | RED]
- [Each criterion with status]
**Issues**: [List any problems]
**Action required**: [If yellow/red]

## Provenance & Explainability
**Status**: [GREEN | YELLOW | RED]
- [Each criterion with status]
**Issues**: [List any problems]
**Action required**: [If yellow/red]

## Cost Accounting
**Status**: [GREEN | YELLOW | RED]
- Actual monthly cost: [Amount]
- Expected cost: [Amount]
- Variance: [% over/under]
**Issues**: [List any problems]
**Action required**: [If yellow/red]

## Exit Strategy
**Status**: [GREEN | YELLOW | RED]
- [Each criterion with status]
**Issues**: [List any problems]
**Action required**: [If yellow/red]

## Overall Assessment
**Strengths**: [What's working well]
**Weaknesses**: [What's concerning]
**Trends**: [Improving/stable/degrading]
**Risks**: [Identified risks]

## Recommendations
- [ ] Continue as-is (GREEN)
- [ ] Monitor closely (YELLOW)
- [ ] Vendor escalation (YELLOW/RED)
- [ ] Evaluate alternatives (RED)
- [ ] Plan migration (RED)

## Next Review
**Date**: [When]
**Focus areas**: [What to watch]
```

## VIII. Conclusion: Operational Research Excellence

**The research principles**:
1. Decision-bearing questions first (if it doesn't change decisions, don't research it)
2. Source triad always (primary + secondary + counter-position)
3. Verdict with confidence (claim + confidence + recency + volatility + design delta)
4. Intellectual honesty (acknowledge limitations, contradictions, uncertainty)
5. Continuous validation (update when proven wrong)

**Infrastructure research additions**:
1. Neo-layer classification (understand where service fits)
2. Capability contract assessment (can vendor deliver what they promise?)
3. Own vs. lease decision framework (systematic approach to economics)
4. Lock-in risk analysis (can we leave if needed?)
5. Regular contract audits (ensure compliance, catch degradation early)

**Quality over quantity**: Few high-confidence verdicts > many unvalidated claims

**Actionable over academic**: Every research output must enable better decisions

**Evolving over static**: Frontier tracking, claim updating, contradiction resolution

**The goal**: Make better decisions faster by knowing what's true, what's uncertain, what's changing, and what it means for action.

**Begin researching with rigor.**
