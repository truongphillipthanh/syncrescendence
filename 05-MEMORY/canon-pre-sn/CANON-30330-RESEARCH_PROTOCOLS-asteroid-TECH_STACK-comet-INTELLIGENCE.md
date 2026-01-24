---
id: [[CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE]]
name: Research Protocols
identity: RESEARCH_PROTOCOLS
tier: CANON
type: asteroid
parent: [[CANON-30300-TECH_STACK-comet-INTELLIGENCE]]
chain: INTELLIGENCE
comet: TECH_STACK
version: 2.0.0
status: canonical
created: 2025-12-31
updated: 2025-12-31
change_velocity: quarterly
dependencies:
  - [[CANON-30300-TECH_STACK-comet-INTELLIGENCE]]
  - [[CANON-30000-INTELLIGENCE-chain]]
synopsis: >
  Methodologies and quality standards for AI-augmented research,
  including the Source Triad Method, verdicting process, decision-bearing
  question prioritization, anti-patterns, and infrastructure evaluation.
---

# [[CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE]]: RESEARCH PROTOCOLS
## Methodologies and Quality Standards

---

## I. Core Methodology

### The Source Triad Method

For every decision-bearing question, execute three research passes:

**Pass 1: Primary Sources**
Target original material from authoritative sources: academic papers, official documentation, company engineering blogs, government reports, patent filings.

*Evaluate*: Is this the original source? Institution credibility? Recency? Methodology used?

*Red flags*: Secondary reporting without primary links, marketing masquerading as research, claims without evidence.

**Pass 2: High-Signal Secondary Analysis**
Target expert interpretation: technical deep-dives, research reviews, industry analysis, expert commentary.

*Evaluate*: Does this add interpretation? Analyst expertise? Rigor vs. speculation? Non-obvious implications revealed?

*Red flags*: Hype, cherry-picking, undisclosed conflicts, extrapolation beyond evidence.

**Pass 3: Counter-Position**
Target alternative interpretations: academic rebuttals, skeptical analyses, limitation acknowledgments, competing approaches.

*Evaluate*: Genuine limitations? Assumptions that might fail? Alternative explanations? Failure modes?

*Red flags*: Strawman arguments, dismissal without engagement, ideological opposition.

### Decision-Bearing Questions First

**Before researching, answer:**
1. What decision does this inform?
2. What would we do differently if X vs. Y?
3. What confidence level needed to act?
4. What's the cost of being wrong?

**Only research when**: Answer materially changes decisions, uncertainty blocks action, time investment justified.

**Skip when**: Answer doesn't affect decisions, uncertainty acceptable, other information more critical.

### The Verdicting Process

For each research question, produce five components:

**1. Claim**: Clear, testable statement
*Example*: "Sonnet 4.5 maintains reliable performance over 30-hour sessions"

**2. Confidence Level**:
- High (>85%): Multiple primary sources, expert consensus, replicated results
- Medium (50-85%): Primary source plus analysis, plausible but inconclusive
- Low (<50%): Single report, unverified, speculative
- Speculative (<25%): Rumor, prediction, no evidence

**3. Recency**: Date + freshness category
- Current (0-3 months): Likely accurate
- Recent (3-12 months): Worth checking
- Dated (1-2 years): May have changed
- Stale (>2 years): Use with caution

**4. Volatility**:
- Stable: Unlikely to change (fundamental principles)
- Shifting: Actively evolving (current capabilities)
- Speculative: Not yet real (predictions)

**5. Design Delta**: "If true, then we should [specific action]"
*Test*: Can someone make a different decision from this? If no, clarify.

### Ledgering and Contradiction Management

**Research Log Format:**
```
Entry ID | Timestamp | Question | Source | Gist | Claims | Confidence | Recency | Volatility | Design Delta | Contradictions | Next Actions
```

**When contradictions arise:**
1. Document both claims explicitly
2. Assess relative source quality
3. Identify resolution path
4. Mark as "pending resolution"
5. Use most conservative estimate
6. Flag for follow-up if critical

**Priority**: Critical (blocks decisions) → Important (affects strategy) → Minor (interesting) → Ignorable (no impact)

---

## II. Research Anti-Patterns

### Benchmark Shopping
Selectively citing benchmarks that support desired conclusion. Creates false confidence.

*Avoid*: Include context, cite competing benchmarks, note what's NOT measured.

### Link Dumping
Many sources without synthesis or verdict. Appears thorough but provides no guidance.

*Avoid*: Every source must have explicit contribution. Few well-analyzed > many undigested.

### Hype Amplification
Uncritically repeating marketing claims or speculative predictions.

*Avoid*: Distinguish claims from evidence, note commercial interest, separate current from roadmap.

### Recency Bias
Assuming newer is always better. Ignores stable principles, creates thrash.

*Avoid*: Assess volatility explicitly, value timeless principles, separate fundamental from fashionable.

### Confirmation Bias
Seeking information that supports existing beliefs. Creates blind spots.

*Avoid*: Actively seek counter-arguments, red team proposals, always include Pass 3.

---

## III. Frontier Tracking

### Target Domains

**Academic**: Stanford HAI, MIT CSAIL, UC Berkeley BAIR, CMU ML, Oxford/Cambridge AI

**AI Labs**: Anthropic, OpenAI, Google DeepMind, Meta AI, xAI

**Mission-Driven**: Center for AI Safety, AI Alignment Forum, FHI

**Commercial**: Cursor, Replit, Perplexity, Palantir, Anduril

### Tracking Cadence

**Weekly**: Key lab blogs, ArXiv cs.AI/cs.CL, Hacker News, relevant subreddits

**Monthly**: 3-5 papers in depth, major product releases, frontier map update, prediction reassessment

**Quarterly**: Comprehensive landscape, emerging paradigm shifts, taxonomy updates, framework revision

### Frontier Map Structure

```json
{
  "claim_id": "identifier",
  "claim": "Testable statement",
  "source": "URL, date",
  "confidence": 0.75,
  "volatility": "shifting",
  "dependencies": ["related_claims"],
  "implications": ["design_changes"],
  "contradictions": [],
  "next_verification": "date"
}
```

*Benefits*: Queryable, traceable, updateable, actionable.

---

## IV. Quality Standards

### Research Quality Checklist

- [ ] Every claim has source attribution
- [ ] Sources are primary when possible
- [ ] Secondary sources add analysis
- [ ] Counter-positions included
- [ ] Confidence levels explicit with rationale
- [ ] Recency and volatility tagged
- [ ] Design deltas specified
- [ ] Contradictions acknowledged
- [ ] No benchmark shopping or link dumping
- [ ] Hype distinguished from evidence

### Report Standards

**Structure**: Executive Summary → Decision-Bearing Questions → Methodology → Findings → Implications → Limitations → Next Steps

**Writing**: Lead with conclusions, clear testable claims, separate evidence from interpretation, acknowledge uncertainty.

### Peer Review Protocol

1. **Self-review**: What could I be wrong about? What evidence am I ignoring?
2. **Source validation**: Can I find original? Does it say what I claim?
3. **Logic check**: Do conclusions follow? Alternative explanations?
4. **Impact assessment**: What decisions will this inform? Cost of being wrong?

---

## V. Context-Specific Patterns

### AI Capability Evaluation

**Key questions**: Actual vs. claimed capability? Reliability? Cost/latency trade-offs? Failure modes? Alternatives? Adoption path?

**Red flags for over-hype**: Cherry-picked examples, no limitations, weak baselines, unclear failure modes.

### Paradigm Shift Assessment

**Key questions**: What's fundamentally changing? What's incremental? What enables this now? Adoption barriers? Trajectory?

**Distinguish**: Capability unlock vs. efficiency gain vs. interface improvement vs. hype cycle.

### Infrastructure Service Evaluation

**Source Triad for Infrastructure:**
- Pass 1: Vendor docs, benchmarks, pricing, SLAs, certifications
- Pass 2: Third-party benchmarks, case studies, technical reviews
- Pass 3: Known limitations, customer complaints, alternatives, exit feasibility

**Evaluation Dimensions:**
- Technical: Latency p50/p95/p99, throughput, reliability, quality, scalability
- Business: Funding, market position, strategic risk, pricing stability, support
- Governance: Security certs, privacy, compliance, audit capability, incident response
- Lock-in: Data portability, API compatibility, feature dependency, migration cost

**Capability Contract Assessment:**
- Performance SLOs documented and enforced?
- Data governance (residency, retention, deletion)?
- Provenance (trace outputs to sources)?
- Exit strategy (migration path, transition support)?
- Cost accounting (transparent pricing)?

**Decision Framework:**
```
Data Sensitivity × Latency Requirements × Economic Leverage × Lock-in Risk
→ Decision: OWN | LEASE | HYBRID
```

### Tool Primitive Extraction

**Phases:**
1. Tool Survey: Features, interface patterns, platform, performance, quality
2. Primitive Identification: Interface, capability, algorithm, platform optimizations
3. Overlap Analysis: Compare to catalog, identify unique vs. redundant
4. Extraction Feasibility: Technical difficulty, legal constraints, maintenance, composition
5. Reuse Validation: Test in composition, measure performance, assess combinations

**Recommendation**: Adopt tool (unique value beyond primitives) | Extract primitives only | Skip (no unique value)

---

## VI. Output Formats

### Research Report (Comprehensive)
When: Major strategic questions, significant uncertainty, high impact

```
Title | Executive Summary | Background | Methodology | Findings | Synthesis | Limitations | Next Steps
```

### Research Log Entry (Quick)
When: Targeted questions, confirming claims, updating frontier

```
Question | Source | Finding | Confidence | Design Delta | Next
```

### Decision Brief (Action-Oriented)
When: Immediate decision, stakeholder briefing

```
Decision | Recommendation | Rationale | If Wrong | Timeline
```

---

## VII. Capability Contract Audit

### Audit Cadence

**Monthly**: Performance metrics, cost vs. budget, incident scan, degradation trends

**Quarterly**: Full contract review, vendor health, alternatives evaluation, renegotiation if needed

**Annual**: Own vs. lease reassessment, landscape analysis, migration consideration, long-term strategy

### Audit Checklist

**Performance**: Latency, availability, throughput, quality targets met? Trends?

**Data Governance**: Residency, retention, export, encryption, access controls compliant?

**Provenance**: Model versions, training data, inference traceability, explanations adequate?

**Cost**: Actual vs. expected? Pricing changes? Optimization opportunities? ROI positive?

**Exit Strategy**: Migration viable? Alternatives available? Export tested? Transition support?

### Findings Classification

**Green**: All criteria met, stable/improving, cost expected, no significant risks

**Yellow**: Borderline criteria, minor degradation, cost creeping, emerging risks → Monitor closely

**Red**: Critical violations, significant issues, overruns, material risks → Action required

### Response Actions

**Yellow**: Increase monitoring, engage vendor, research alternatives, set improvement targets

**Red**: Immediate escalation, serious alternative evaluation, migration planning, risk mitigation, executive notification

---

## VIII. Operational Research Excellence

**Core Principles:**
1. Decision-bearing questions first
2. Source triad always (primary + secondary + counter)
3. Verdict with confidence (claim + confidence + recency + volatility + design delta)
4. Intellectual honesty (acknowledge limitations, contradictions, uncertainty)
5. Continuous validation (update when proven wrong)

**Infrastructure Additions:**
1. Neo-layer classification
2. Capability contract assessment
3. Own vs. lease decision framework
4. Lock-in risk analysis
5. Regular contract audits

**Quality over quantity**: Few high-confidence verdicts > many unvalidated claims

**Actionable over academic**: Every output must enable better decisions

**The goal**: Make better decisions faster by knowing what's true, what's uncertain, what's changing, and what it means for action.

---

## VERSION HISTORY

**v2.0.0** (December 2025): Canonization from Technology Lunar - 3 Research_Protocols.md
- Compressed from ~31K to ~20K (35% reduction)
- Removed redundant examples and verbose explanations
- Preserved all core methodology
- Added CANON frontmatter and hierarchy placement
