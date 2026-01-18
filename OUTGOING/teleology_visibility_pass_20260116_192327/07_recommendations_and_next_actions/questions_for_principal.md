# Questions for Principal
**Generated**: 2026-01-17T03:23:54Z
**Purpose**: Only logically unavoidable questions; everything else inferred or flagged as assumption

---

## Overview

This document contains only questions that cannot be answered from repository artifacts or reasonable inference. All other uncertainties are documented as assumptions.

---

## Category 1: Strategic Direction

### Q1: Chorus vs. Single-Surface Priority
**Context**: The chorus design (multi-platform dispatch + reconciliation) adds significant coordination overhead. The INTERACTION_PARADIGM.md already establishes platform specialization.

**Question**: Should chorus be the default pattern, or reserved for high-stakes decisions where multiple perspectives are genuinely needed?

**Why This Can't Be Inferred**: Trade-off between thoroughness and velocity is a values judgment. Repository shows both patterns documented but no explicit priority.

**Assumption if No Answer**: Use single-platform routing by default per coordination.yaml; chorus only when explicitly requested or when evidence suggests high uncertainty.

---

### Q2: Gemini/ChatGPT Onboarding Priority
**Context**: system_state.json shows both Gemini and ChatGPT as "pending_onboard". INTERACTION_PARADIGM.md describes their roles but onboarding hasn't occurred.

**Question**: Should Gemini (Oracle/sensing) or ChatGPT (Deviser/planning) be onboarded first?

**Why This Can't Be Inferred**: Both are valuable; sequencing is strategic choice. Gemini enables content processing; ChatGPT enables planning. Either is defensible.

**Assumption if No Answer**: Gemini first—the 184-source backlog needs processing more urgently than planning infrastructure.

---

### Q3: Rate Limit Management Strategy
**Context**: $100/month budget across 5 subscriptions. Rate limits vary by platform. Some tasks benefit from more expensive models (Opus, GPT-5.2 Thinking).

**Question**: Should the system optimize for (a) maximum throughput with cheaper models, or (b) quality-first with expensive models for strategic work?

**Why This Can't Be Inferred**: Resource allocation reflects priorities not explicitly documented.

**Assumption if No Answer**: Quality for strategic (Oracle synthesis, Canon updates); throughput for routine (source processing, ledger updates). Per existing model_routing in coordination.yaml.

---

## Category 2: Operational Boundaries

### Q4: Principal Approval Threshold
**Context**: Guardrails specify Principal approval for Canon modifications and irreversible actions.

**Question**: What is the approval threshold for Canon modifications?
- All modifications require explicit approval?
- Only paradigm-level integrations?
- Only deletions/major restructuring?

**Why This Can't Be Inferred**: CLAUDE.md says "require Principal approval for deletions" but doesn't specify modification thresholds.

**Assumption if No Answer**:
- Deletions: Always require approval
- Additions from paradigm sources: Require approval
- Additions from strategic sources: Notify, proceed unless blocked
- Minor corrections (typos, formatting): No approval needed

---

### Q5: Automation Boundaries
**Context**: INTERACTION_PARADIGM.md describes Phase 2 (Semi-Automated) and Phase 3 (Autonomous) as future states. Current state is Manual Trigger.

**Question**: What triggers should be automated first?
- YouTube Watch Later polling?
- RSS feed processing?
- Daily intelligence brief generation?

**Why This Can't Be Inferred**: Automation sequence affects Principal's daily experience significantly.

**Assumption if No Answer**: Defer automation until backlog reduced by 50% through manual processing. Automation adds complexity; clear the queue first.

---

## Category 3: Architecture Decisions

### Q6: NotebookLM Integration Depth
**Context**: NotebookLM is mentioned as grounded RAG tool. Notebooks require manual source upload.

**Question**: Should NotebookLM have dedicated notebooks for:
- Full Oracle history?
- Full Canon?
- Active project context?
- All of the above?

**Why This Can't Be Inferred**: Notebook maintenance is ongoing cost. Multiple notebooks multiply maintenance.

**Assumption if No Answer**:
- Oracle Corpus notebook: Active Oracle exports only (last 5 sessions)
- Canon Reference: Core cosmos-level documents only
- No project-specific notebooks (overhead exceeds value)

---

### Q7: Concentric Rings Output Layer
**Context**: Ring 7 (Output Layer) is defined but not populated. Future outputs include "publication-ready content" and "Gaian Field Node interface."

**Question**: Is Ring 7 implementation in scope for current work, or should it remain placeholder until Modal 2/3?

**Why This Can't Be Inferred**: Publication is external-facing and may have timing/strategic considerations not in repo.

**Assumption if No Answer**: Ring 7 remains placeholder. Focus on Rings 1-5 (sensing to Canon). Output layer activates when content production begins.

---

## Documented Assumptions

The following assumptions were made during this visibility pass. No question needed; flagged for transparency:

| ID | Assumption | Basis |
|----|------------|-------|
| A1 | Opus 4.5 is the current frontier Claude model | platform_features.md, CLAUDE.md |
| A2 | Three Claude Pro accounts are active | coordination.yaml |
| A3 | Principal prefers minimal web-to-repo context graduation | INTERACTION_PARADIGM.md anti-pattern note |
| A4 | Backlog processing is higher priority than infrastructure | Explicit in previous_thread.md |
| A5 | Flat directory principle applies to OUTGOING as well | CLAUDE.md generalization |
| A6 | Session lifecycle protocol is the highest priority gap | Protocol presence report analysis |
| A7 | Temporal content should not enter Canon | REF-STANDARDS.md Lens #2 |
| A8 | Event log is append-only and never truncated | events.jsonl design pattern |
| A9 | Blackboard packets are immutable once created | packet_protocol.json design |
| A10 | Principal operates primarily from MacBook Air | SSH remote execution reference |

---

## Questions NOT Asked

The following were considered but deemed inferable:

1. **"Should we use Claude Code or Claude Web?"** — Already specified in INTERACTION_PARADIGM.md
2. **"Which sources to process first?"** — Signal tier determines priority
3. **"How often to commit?"** — CLAUDE.md specifies "frequently"
4. **"What format for execution logs?"** — Established pattern in execution_logs/
5. **"When to run verification?"** — Guardrail 3 specifies always
