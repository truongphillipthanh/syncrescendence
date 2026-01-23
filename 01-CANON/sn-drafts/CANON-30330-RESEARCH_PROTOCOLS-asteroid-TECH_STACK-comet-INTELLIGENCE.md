---
id: CANON-30330
name: Research Protocols
identity: RESEARCH_PROTOCOLS
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
  - CANON-30000
synopsis: >
  Methodologies and quality standards for AI-augmented research,
  including the Source Triad Method, verdicting process, decision-bearing
  question prioritization, anti-patterns, and infrastructure evaluation.
---

# CANON-30330-RESEARCH_PROTOCOLS-asteroid-TECH_STACK-comet-INTELLIGENCE (SN Format)

**Note**: This is a Semantic Notation compressed version.
**Original**: 1,534 words, 12,193 characters

---

TERM TheSourceTriadMethod:
    sutra: "For every decision-bearing question, execute three research passes:  Pass 1: Primary Sources Targ..."
    gloss:
        For every decision-bearing question, execute three research passes:

**Pass 1: Primary Sources**
Target original material from authoritative sources: academic papers, official documentation, company engineering blogs, government reports, patent filings.

*Evaluate*: Is this the original source? Inst...
end


TERM DecisionBearingQuestionsFirst:
    sutra: "Before researching, answer: 1"
    gloss:
        **Before researching, answer:**
1. What decision does this inform?
2. What would we do differently if X vs. Y?
3. What confidence level needed to act?
4. What's the cost of being wrong?

**Only research when**: Answer materially changes decisions, uncertainty blocks action, time investment justified...
end


TERM TheVerdictingProcess:
    sutra: "For each research question, produce five components:  1"
    gloss:
        For each research question, produce five components:

**1. Claim**: Clear, testable statement
*Example*: "Sonnet 4.5 maintains reliable performance over 30-hour sessions"

**2. Confidence Level**:
- High (>85%): Multiple primary sources, expert consensus, replicated results
- Medium (50-85%): Primar...
end


TERM LedgeringandContradictionManagement:
    sutra: "Research Log Format: `` Entry ID | Timestamp | Question | Source | Gist | Claims | Confidence | R..."
    gloss:
        **Research Log Format:**
```
Entry ID | Timestamp | Question | Source | Gist | Claims | Confidence | Recency | Volatility | Design Delta | Contradictions | Next Actions
```

**When contradictions arise:**
1. Document both claims explicitly
2. Assess relative source quality
3. Identify resolution pat...
end


TERM BenchmarkShopping:
    sutra: "Selectively citing benchmarks that support desired conclusion"
    gloss:
        Selectively citing benchmarks that support desired conclusion. Creates false confidence.

*Avoid*: Include context, cite competing benchmarks, note what's NOT measured.
end


NORM LinkDumping:
    sutra: "Many sources without synthesis or verdict"
    gloss:
        Many sources without synthesis or verdict. Appears thorough but provides no guidance.

*Avoid*: Every source must have explicit contribution. Few well-analyzed > many undigested.
end


TERM HypeAmplification:
    sutra: "Uncritically repeating marketing claims or speculative predictions"
    gloss:
        Uncritically repeating marketing claims or speculative predictions.

*Avoid*: Distinguish claims from evidence, note commercial interest, separate current from roadmap.
end


TERM RecencyBias:
    sutra: "Assuming newer is always better"
    gloss:
        Assuming newer is always better. Ignores stable principles, creates thrash.

*Avoid*: Assess volatility explicitly, value timeless principles, separate fundamental from fashionable.
end


TERM ConfirmationBias:
    sutra: "Seeking information that supports existing beliefs"
    gloss:
        Seeking information that supports existing beliefs. Creates blind spots.

*Avoid*: Actively seek counter-arguments, red team proposals, always include Pass 3.

---
end


TERM TargetDomains:
    sutra: "Academic: Stanford HAI, MIT CSAIL, UC Berkeley BAIR, CMU ML, Oxford/Cambridge AI  AI Labs: Anthro..."
    gloss:
        **Academic**: Stanford HAI, MIT CSAIL, UC Berkeley BAIR, CMU ML, Oxford/Cambridge AI

**AI Labs**: Anthropic, OpenAI, Google DeepMind, Meta AI, xAI

**Mission-Driven**: Center for AI Safety, AI Alignment Forum, FHI

**Commercial**: Cursor, Replit, Perplexity, Palantir, Anduril
end


TERM TrackingCadence:
    sutra: "Weekly: Key lab blogs, ArXiv cs.AI/cs.CL, Hacker News, relevant subreddits  Monthly: 3-5 papers i..."
    gloss:
        **Weekly**: Key lab blogs, ArXiv cs.AI/cs.CL, Hacker News, relevant subreddits

**Monthly**: 3-5 papers in depth, major product releases, frontier map update, prediction reassessment

**Quarterly**: Comprehensive landscape, emerging paradigm shifts, taxonomy updates, framework revision
end


TERM FrontierMapStructure:
    sutra: "``json {   "claim_id": "identifier",   "claim": "Testable statement",   "source": "URL, date",   ..."
    gloss:
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

*Benefits*: Query...
end


TERM ResearchQualityChecklist:
    sutra: "- [ ] Every claim has source attribution - [ ] Sources are primary when possible - [ ] Secondary ..."
    gloss:
        - [ ] Every claim has source attribution
- [ ] Sources are primary when possible
- [ ] Secondary sources add analysis
- [ ] Counter-positions included
- [ ] Confidence levels explicit with rationale
- [ ] Recency and volatility tagged
- [ ] Design deltas specified
- [ ] Contradictions acknowledged
-...
end


TERM ReportStandards:
    sutra: "Structure: Executive Summary → Decision-Bearing Questions → Methodology → Findings → Implications..."
    gloss:
        **Structure**: Executive Summary → Decision-Bearing Questions → Methodology → Findings → Implications → Limitations → Next Steps

**Writing**: Lead with conclusions, clear testable claims, separate evidence from interpretation, acknowledge uncertainty.
end


TERM PeerReviewProtocol:
    sutra: "1"
    gloss:
        1. **Self-review**: What could I be wrong about? What evidence am I ignoring?
2. **Source validation**: Can I find original? Does it say what I claim?
3. **Logic check**: Do conclusions follow? Alternative explanations?
4. **Impact assessment**: What decisions will this inform? Cost of being wrong?...
end


TERM AICapabilityEvaluation:
    sutra: "Key questions: Actual vs"
    gloss:
        **Key questions**: Actual vs. claimed capability? Reliability? Cost/latency trade-offs? Failure modes? Alternatives? Adoption path?

**Red flags for over-hype**: Cherry-picked examples, no limitations, weak baselines, unclear failure modes.
end


TERM ParadigmShiftAssessment:
    sutra: "Key questions: What's fundamentally changing"
    gloss:
        **Key questions**: What's fundamentally changing? What's incremental? What enables this now? Adoption barriers? Trajectory?

**Distinguish**: Capability unlock vs. efficiency gain vs. interface improvement vs. hype cycle.
end


TERM InfrastructureServiceEvaluation:
    sutra: "Source Triad for Infrastructure: - Pass 1: Vendor docs, benchmarks, pricing, SLAs, certifications..."
    gloss:
        **Source Triad for Infrastructure:**
- Pass 1: Vendor docs, benchmarks, pricing, SLAs, certifications
- Pass 2: Third-party benchmarks, case studies, technical reviews
- Pass 3: Known limitations, customer complaints, alternatives, exit feasibility

**Evaluation Dimensions:**
- Technical: Latency p5...
end


TERM ToolPrimitiveExtraction:
    sutra: "Phases: 1"
    gloss:
        **Phases:**
1. Tool Survey: Features, interface patterns, platform, performance, quality
2. Primitive Identification: Interface, capability, algorithm, platform optimizations
3. Overlap Analysis: Compare to catalog, identify unique vs. redundant
4. Extraction Feasibility: Technical difficulty, legal...
end


TERM ResearchReportComprehensive:
    sutra: "When: Major strategic questions, significant uncertainty, high impact  `` Title | Executive Summa..."
    gloss:
        When: Major strategic questions, significant uncertainty, high impact

```
Title | Executive Summary | Background | Methodology | Findings | Synthesis | Limitations | Next Steps
```
end


TERM ResearchLogEntryQuick:
    sutra: "When: Targeted questions, confirming claims, updating frontier  `` Question | Source | Finding | ..."
    gloss:
        When: Targeted questions, confirming claims, updating frontier

```
Question | Source | Finding | Confidence | Design Delta | Next
```
end


TERM DecisionBriefActionOriented:
    sutra: "When: Immediate decision, stakeholder briefing  `` Decision | Recommendation | Rationale | If Wro..."
    gloss:
        When: Immediate decision, stakeholder briefing

```
Decision | Recommendation | Rationale | If Wrong | Timeline
```

---
end


TERM AuditCadence:
    sutra: "Monthly: Performance metrics, cost vs"
    gloss:
        **Monthly**: Performance metrics, cost vs. budget, incident scan, degradation trends

**Quarterly**: Full contract review, vendor health, alternatives evaluation, renegotiation if needed

**Annual**: Own vs. lease reassessment, landscape analysis, migration consideration, long-term strategy
end


TERM AuditChecklist:
    sutra: "Performance: Latency, availability, throughput, quality targets met"
    gloss:
        **Performance**: Latency, availability, throughput, quality targets met? Trends?

**Data Governance**: Residency, retention, export, encryption, access controls compliant?

**Provenance**: Model versions, training data, inference traceability, explanations adequate?

**Cost**: Actual vs. expected? P...
end


TERM FindingsClassification:
    sutra: "Green: All criteria met, stable/improving, cost expected, no significant risks  Yellow: Borderlin..."
    gloss:
        **Green**: All criteria met, stable/improving, cost expected, no significant risks

**Yellow**: Borderline criteria, minor degradation, cost creeping, emerging risks → Monitor closely

**Red**: Critical violations, significant issues, overruns, material risks → Action required
end


TERM ResponseActions:
    sutra: "Yellow: Increase monitoring, engage vendor, research alternatives, set improvement targets  Red: ..."
    gloss:
        **Yellow**: Increase monitoring, engage vendor, research alternatives, set improvement targets

**Red**: Immediate escalation, serious alternative evaluation, migration planning, risk mitigation, executive notification

---
end


TERM VIIIOperationalResearchExcellence:
    sutra: "Core Principles: 1"
    gloss:
        **Core Principles:**
1. Decision-bearing questions first
2. Source triad always (primary + secondary + counter)
3. Verdict with confidence (claim + confidence + recency + volatility + design delta)
4. Intellectual honesty (acknowledge limitations, contradictions, uncertainty)
5. Continuous validatio...
end


TERM VERSIONHISTORY:
    sutra: "v2.0.0 (December 2025): Canonization from Technology Lunar - 3 Research_Protocols.md - Compressed..."
    gloss:
        **v2.0.0** (December 2025): Canonization from Technology Lunar - 3 Research_Protocols.md
- Compressed from ~31K to ~20K (35% reduction)
- Removed redundant examples and verbose explanations
- Preserved all core methodology
- Added CANON frontmatter and hierarchy placement
end
