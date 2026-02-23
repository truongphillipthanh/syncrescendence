---
id: SOURCE-undated-001
title: Complete Guide Learn Anything
platform: x
format: transcript
creator: ArmanHezarkhani
date_published: "2026-01-23"
status: triaged
url: https://x.com/ArmanHezarkhani/status/2014708119029399914
original_filename: research/x-bookmarks/TRANS-ArmanHezarkhani-complete_guide_learn_anything.md
aliases:
  - "Arman Learn Anything Transcript"
  - "Spaced Repetition Claude Transcript"
teleology: extract
notebooklm_category: claude-code
synopsis: "Detailed transcript of Arman Hezarkhani's system for rapid expertise acquisition using Claude Code + Notion MCP. Includes full database schema, spaced repetition intervals, three-phase workflow (learning sessions, daily reviews, Socratic challenges), and the exact prompts and Notion structure for replication."
key_insights:
  - "The Notion database schema with confidence tracking, next-review dates, and concept relations creates a machine-readable knowledge graph that Claude can query and maintain autonomously"
  - "Failed recall resets the spaced repetition interval to 1 day — the system is self-correcting and forces re-engagement with weak spots"
  - "Cross-domain connections compound: each new domain enriches the entire knowledge base through relational links"
topics:
  - claude-code
  - mcp
  - tutorial
  - best-practices
signal_tier: strategic
---

# The Complete Guide: How to Learn Anything. For Good.
> **Author**: Arman Hezarkhani (@ArmanHezarkhani) — cofounder @tenex_labs, previously @google, @carnegiemellon
> **Date**: January 23, 2026 · 6:33 AM
> **Type**: X Article
> **URL**: https://x.com/ArmanHezarkhani/status/2014708119029399914
> **Engagement**: 13 replies · 102 reposts · 698 likes · 1,452 bookmarks · 93K views
> **Transcribed**: 2026-02-04 by Ajna

---

## Summary

A systematic framework for rapid domain expertise acquisition using Claude Code + Notion + Notion MCP. Core thesis: spaced repetition + active recall + AI-powered Socratic teaching = genuine expertise in weeks instead of years. The system produces a personal knowledge base, daily review "newsletters," and compounds across domains.

## Core Thesis

The author runs a consulting company and needs to become expert-level in new industries within days/hours. Traditional learning takes years. Surface-level "faking it" fails at follow-up questions. The solution: a system built on three scientifically-backed learning principles:

1. **Spaced repetition** — revisit information at increasing intervals before forgetting
2. **Active recall** — actively retrieve from memory (struggle = learning)
3. **Connected understanding** — see how concepts relate, where exceptions lie, what experts debate

**Key insight**: Claude Code can manage all three automatically — remembering what you've learned, when, what you'll forget, and generating calibrated review material.

## The System Architecture

### Stack
- **Claude Code** — the AI teacher and system manager
- **Notion** — the knowledge database
- **Notion MCP** — connector letting Claude Code read/write to Notion

### Database Structure

**Knowledge Base** (primary database):
| Property | Type | Purpose |
|----------|------|---------|
| Topic | Title | Concept name |
| Domain | Select | Field (e.g., "Pharma Supply Chain") |
| Explanation | Text | Actual content |
| Last Reviewed | Date | When last reviewed |
| Next Review | Date | Spaced repetition schedule |
| Confidence | Select | Low / Medium / High |
| Times Reviewed | Number | Review count |
| Questions | Text | Follow-up questions |
| Connections | Relation | Links to related concepts |

**Learning Sessions** (secondary database):
| Property | Type | Purpose |
|----------|------|---------|
| Date | Date | Session date |
| Domain | Select | Field studied |
| Concepts Covered | Relation | Links to Knowledge Base |
| Key Insights | Text | What clicked |
| Open Questions | Text | Remaining confusion |

### Spaced Repetition Intervals
- 1st review: 1 day
- 2nd review: 3 days
- 3rd review: 7 days
- 4th review: 14 days
- 5th+: 30 days
- **Failed recall: Reset to 1 day**

## Core Workflow (3 Phases)

### Phase 1: Learning Session
Start with mental models/frameworks, NOT facts.

**Opening Prompt Pattern**:
```
I'm a consultant starting a project in [DOMAIN]. I need to become genuinely knowledgeable—not surface-level—within [TIMEFRAME].
My current knowledge: [HONEST ASSESSMENT]
Start by giving me the conceptual foundation. What are the 3-5 mental models that experts in this field use to think about problems?
Don't give me facts yet—give me frameworks.
After each concept, log it to my Notion Knowledge Base with:
- A clear explanation
- Why it matters
- Common misconceptions
- One question I should be able to answer if I understand it
Set the confidence to "Low" and the next review date to tomorrow.
```

### Phase 2: Deep Dives
Socratic method — Claude asks questions FIRST, then builds on correct/incorrect understanding.

**Deep Dive Prompt Pattern**:
```
Now go deeper on [SPECIFIC CONCEPT]. I want to understand it well enough to:
1. Explain it to a smart non-expert
2. Identify when someone is wrong about it
3. Know what experts disagree about
Use the Socratic method. Ask me questions to test my understanding before giving me more information.
When I get something wrong, explain why—don't just give me the right answer.
Log any new concepts we cover to Notion. Update my confidence level based on how I perform.
```

### Phase 3: Daily Newsletter
The compound payoff mechanism. Every morning, Claude queries the Knowledge Base and generates:

1. **Review These Today** — spaced repetition items due
2. **Test Yourself** — active recall questions for each
3. **Connections You Might Have Missed** — cross-concept synthesis
4. **This Week's Focus** — what needs deeper attention

## Additional Protocols

### Question Protocol
For ad-hoc questions during client calls, reading, or curiosity:
```
Quick question about [DOMAIN]: [YOUR QUESTION]
Answer it, then:
1. Log the answer to my Notion Knowledge Base as a new concept
2. Connect it to any related concepts already in my database
3. Note if this changes my understanding of anything I've already learned
4. Give me one follow-up question I should be able to answer in 3 days
```

### Expert Test Prompt
Pre-meeting readiness verification:
```
I have a meeting with [CLIENT TYPE] in [TIMEFRAME]. Test my readiness:
1. What questions will they likely ask me?
2. What questions should I ask them to demonstrate expertise?
3. What mistakes do smart outsiders typically make in this domain?
4. What contrarian or nuanced take could I offer that would surprise them?
Be tough. I'd rather fail here than in the meeting.
```

### Domain Templates
Three specialized starting templates:
1. **Technical Domains** — tradeoffs, quality signals, failure modes
2. **Business/Strategy Domains** — economics, competitive dynamics, disruptions, insider language
3. **Regulatory/Legal Domains** — regulatory intent, key requirements, common violations, enforcement reality

## The Compound Effect
- Knowledge compounds across domains (pattern recognition)
- Author has 400+ concepts across 12+ domains, all connected
- 10th domain takes half the time of the 1st
- 20th domain takes a quarter
- **"This is what expertise actually is: pattern recognition across contexts."**

## Common Mistakes
1. **Passive learning** — reading explanations without answering questions
2. **Skipping the newsletter** — breaks compound effect (3 missed days = back to cramming)
3. **Going too broad** — "supply chain" too vague; "pharmaceutical cold chain logistics" is actionable
4. **Not logging questions** — lost insights
5. **Trusting your confidence** — always test before claiming expertise

## Limitations Acknowledged
- Notion MCP in early days (complex queries sometimes fail)
- Token limits on long sessions (start new, rebuild from Notion)
- Spaced repetition intervals are approximations
- Claude can be wrong (cross-reference for high-stakes)
- Requires discipline (garbage in, garbage out)

## What It Doesn't Replace
- **Primary experience** — intellectual understanding ≠ practical skill
- **Relationships** — experts valuable for network, judgment, reputation
- **Judgment** — can't teach which experts to trust
- **Doing the work** — better prepared ≠ exempt from execution

---

## Syncrescendence Relevance

### Direct Applications
- **Learning acceleration protocol** maps to Sovereign's multi-domain acquisition needs (mechatronics, cybersecurity, embedded systems)
- **Claude Code + Notion MCP** architecture directly applicable to Ajna/Psyche orchestration
- **Spaced repetition intervals** could be formalized as a DYN protocol
- **Knowledge Base schema** aligns with ontology bridge work (ARCH-ROSETTA_ONTOLOGY_BRIDGE)

### Key Resonances
- "Mental models first, facts second" = Syncrescendence's coherence-first approach
- "Pattern recognition across contexts" = the Constellation's distributed sensing thesis
- "Compound effect across domains" validates the multi-domain sovereignty stack (IET + CCNA + Cyber)
- "Daily newsletter" pattern parallels heartbeat-driven knowledge surfacing

### Tensions
- Author assumes Claude Code + Notion (centralized). Syncrescendence uses distributed multi-agent architecture.
- "Genuine expertise in 2-3 weeks" claim needs reality-checking against Sovereign's burnout vectors
- Single-tool dependency (Claude Code) vs. Constellation's multi-model approach
