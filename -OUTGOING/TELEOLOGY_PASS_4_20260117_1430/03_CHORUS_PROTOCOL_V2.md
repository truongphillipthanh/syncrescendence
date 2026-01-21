# CHORUS PROTOCOL V2
## Multi-Platform Dispatch, Reconciliation, and Guardrails
**Generated**: 2026-01-17
**Purpose**: When to use multiple platforms, how to reconcile outputs, cost/latency guardrails

---

## I. CORE PRINCIPLE

**Chorus is a selective instrument, not a default mode.**

Using multiple platforms creates:
- 3x cost (tokens, time, attention)
- Reconciliation burden (whose answer wins?)
- Coordination overhead
- Prompt maintenance proliferation

**Use chorus when the stakes justify the cost.**

---

## II. WHEN TO USE CHORUS

### Tier 1: MANDATORY Chorus

**Use for decisions that are irreversible or affect all future work.**

| Situation | Platforms | Reconciliation |
|-----------|-----------|----------------|
| Constitutional changes to CLAUDE.md | Claude + ChatGPT + Gemini | Full protocol |
| CANON integration (paradigm tier) | At least 2 platforms | Full protocol |
| Strategic pivot | All available | Principal sign-off |
| Delete protected zone content | Claude + ChatGPT | Full protocol |

**Mandatory chorus cannot be skipped.**

### Tier 2: RECOMMENDED Chorus

**Use for complex decisions with multiple valid approaches.**

| Situation | Platforms | Reconciliation |
|-----------|-----------|----------------|
| Architectural decision | Claude + ChatGPT | Quick comparison |
| Contradiction in sources | 2 platforms | Explicit resolution |
| Novel technical challenge | 2 platforms | Synthesis |
| High-uncertainty estimate | 2 platforms | Range consensus |

**Recommended chorus can be skipped if time-critical, but note the skip.**

### Tier 3: SINGLE PLATFORM

**Use for routine work with clear instructions.**

| Situation | Platform | Reconciliation |
|-----------|----------|----------------|
| Clear directive execution | Claude Code | None |
| Simple research query | Perplexity or Gemini | None |
| Known pattern application | Routed platform | None |
| Incremental iteration | Same as previous | None |

**Most work should be single platform.**

---

## III. CHORUS DISPATCH PROTOCOL

### Step 1: Formulate Query

Create a **single, unambiguous query** for all platforms.

```markdown
## CHORUS QUERY: CHR-YYYYMMDD-NNN

**Question**: [Specific question with no ambiguity]

**Context**: [Minimum necessary context, identical for all]

**Expected Output**: [What form should the answer take?]

**Evaluation Criteria**: [How will we judge answers?]

**Deadline**: [When must this be resolved?]
```

### Step 2: Select Platforms

Match question type to platform strengths:

| Question Type | Recommended Platforms | Rationale |
|---------------|----------------------|-----------|
| Factual research | Perplexity + Gemini | Citation discipline |
| Strategic decision | Claude + ChatGPT | Reasoning depth |
| Technical architecture | Claude + ChatGPT | Different model strengths |
| Corpus analysis | Gemini alone | 2M context required |
| Real-time intelligence | Grok + Perplexity | Current information |
| Code review | Claude + ChatGPT | Complementary lenses |

### Step 3: Parallel Dispatch

Send identical query to all selected platforms **simultaneously**.

**Do not read any response until all arrive.** This prevents anchoring.

```yaml
dispatch:
  query_id: CHR-YYYYMMDD-NNN
  platforms: [claude, chatgpt, gemini]
  query: "[exact same text to all]"
  timeout: 10_minutes
  expected_output: structured_analysis
```

### Step 4: Collect Responses

Wait for all responses. Time out if one platform is slow.

If a platform times out:
- Note the timeout
- Proceed with available responses
- Document the gap

### Step 5: Reconcile

Apply the reconciliation protocol (see Section IV).

---

## IV. RECONCILIATION PROTOCOL

### Method 1: CONVERGENT (All Agree)

**When**: All platforms agree on key points.

**Action**: Accept the convergent answer.

```markdown
## RECONCILIATION: CONVERGENT

All platforms agree:
- [Key point 1]
- [Key point 2]

Minor nuance differences:
- [Claude noted X]
- [ChatGPT emphasized Y]

**Final Answer**: [Convergent position]
```

### Method 2: COMPLEMENTARY (Different but Compatible)

**When**: Platforms provide different perspectives that don't contradict.

**Action**: Synthesize into unified answer preserving unique contributions.

```markdown
## RECONCILIATION: COMPLEMENTARY

### Claude's Unique Contribution
[What only Claude said]

### ChatGPT's Unique Contribution
[What only ChatGPT said]

### Gemini's Unique Contribution
[What only Gemini said]

### Unified Position
[How these combine into coherent answer]

**Final Answer**: [Synthesis]
```

### Method 3: CONFLICTING (Direct Disagreement)

**When**: Platforms directly contradict each other.

**Action**: Apply decision framework.

```yaml
conflict_resolution:
  1_check_grounding:
    - Which answer cites sources?
    - Which can be verified against repo?
    - Which aligns with CANON?

  2_apply_lenses:
    - Which passes more of the 18 lenses?
    - Which aligns with constitutional rules?

  3_confidence_weighting:
    - Higher confidence = higher weight
    - "I'm not sure" = lower weight

  4_principal_judgment:
    - If still tied, Principal decides
    - Document reasoning
```

```markdown
## RECONCILIATION: CONFLICTING

### Claude's Position
[Position + reasoning]
Confidence: [high/medium/low]

### ChatGPT's Position
[Position + reasoning]
Confidence: [high/medium/low]

### Resolution
Applied: [which method from above]
Winner: [which position]
Rationale: [why]

**MINORITY POSITION PRESERVED**:
[The losing position, in case it's later vindicated]

**Final Answer**: [Chosen position]
```

### Method 4: IRRECONCILABLE

**When**: Fundamental disagreement with no clear resolution.

**Action**: Do not proceed. Gather more evidence.

```markdown
## RECONCILIATION: IRRECONCILABLE

### The Conflict
[What they disagree about]

### Why Unresolvable Now
[What's missing]

### Evidence Needed
[What would resolve this]

### Next Action
Dispatch evidence-gathering query to: [platform]
Query: [specific question]

**STATUS**: BLOCKED pending evidence
```

---

## V. PRESERVING MINORITY POSITIONS

**Rule**: Always preserve minority positions, even when rejected.

**Why**: The minority might be right. Future evidence might vindicate them.

```markdown
## MINORITY POSITION: [Topic]

**Platform**: [Who held this view]
**Position**: [What they argued]
**Confidence**: [Their stated confidence]
**Why Rejected**: [Reason we didn't go with this]
**Trigger for Revisit**: [What would make us reconsider]
```

---

## VI. CONFIDENCE TAGGING

All chorus outputs should include confidence:

| Tag | Meaning | Use |
|-----|---------|-----|
| **HIGH** | Strong evidence, high certainty | Can act on this |
| **MEDIUM** | Reasonable confidence, some uncertainty | Act with caution |
| **LOW** | Weak evidence, significant uncertainty | Gather more info |
| **UNKNOWN** | Cannot assess | Must verify before acting |

```markdown
Finding: [Statement]
Confidence: HIGH
Basis: [Why confident]
```

---

## VII. COST/LATENCY GUARDRAILS

### When Chorus is OVERKILL

| Situation | Why Skip | Do Instead |
|-----------|----------|------------|
| Time-critical (< 5 min) | No time to reconcile | Single platform + note |
| Low stakes | Not worth the cost | Single platform |
| Clear consensus already | Redundant | Document the consensus |
| Same question asked before | We know the answer | Reference prior chorus |

### Cost Estimation

| Chorus Size | Token Cost | Time Cost | Attention Cost |
|-------------|------------|-----------|----------------|
| 2 platforms | 2x | 15-30 min | Moderate |
| 3 platforms | 3x | 25-45 min | High |
| 4+ platforms | 4x+ | 40-60 min | Very high |

**Rule of Thumb**: If reconciliation takes longer than getting a single good answer, chorus was overkill.

### Latency Budgets

| Decision Type | Acceptable Latency | Chorus Justified? |
|---------------|-------------------|-------------------|
| Urgent fix | < 10 min | No |
| Daily task | < 30 min | Maybe |
| Strategic decision | < 1 hr | Yes |
| Constitutional change | < 1 day | Yes |

---

## VIII. CHORUS ARTIFACTS

### Where to Store

```
00-ORCHESTRATION/
├── blackboard/
│   └── chorus/
│       ├── CHR-20260117-001.md
│       ├── CHR-20260117-002.md
│       └── ...
```

### Chorus Packet Template

```markdown
# CHORUS PACKET: CHR-YYYYMMDD-NNN

**Created**: YYYY-MM-DD HH:MM UTC
**Query**: [What was being investigated]
**Platforms**: [List of platforms used]
**Reconciliation Method**: [convergent/complementary/conflicting/irreconcilable]

## Perspectives

### Claude
**Finding**: [What Claude contributed]
**Confidence**: [high/medium/low]

### ChatGPT
**Finding**: [What ChatGPT contributed]
**Confidence**: [high/medium/low]

### Gemini
**Finding**: [What Gemini contributed]
**Confidence**: [high/medium/low]

## Convergence
[Where they agree]

## Divergence
[Where they disagree]

## Synthesis
[Unified answer]

## Minority Positions Preserved
[Rejected positions worth remembering]

## Recommended Action
[What to do next]

## Time to Resolution
[How long this took]
```

---

## IX. ANTI-PATTERNS

### Analysis Paralysis
**Symptom**: Same question asked 3+ times, no decision.
**Detection**: Query history shows repetition.
**Prevention**: Set decision deadline before dispatch.
**Recovery**: Principal makes final call at deadline.

### Regression to Mean
**Symptom**: Synthesis is worse than any individual answer.
**Detection**: Unified position has less insight than components.
**Prevention**: Preserve unique contributions explicitly.
**Recovery**: Pick best individual answer, note others as supplements.

### Prompt Proliferation
**Symptom**: Maintaining different prompts for different platforms.
**Detection**: Prompts diverge, results become incomparable.
**Prevention**: Single source of truth for chorus queries.
**Recovery**: Reconverge on single query format.

### Coordination Tax
**Symptom**: More time orchestrating than thinking.
**Detection**: Overhead > single-platform time.
**Prevention**: Default to single platform.
**Recovery**: Ask: "Was chorus worth it?" If no, don't use next time.

---

## X. METRICS

Track chorus effectiveness:

| Metric | Target | Healthy Sign |
|--------|--------|--------------|
| Chorus frequency | < 10% of queries | Most work is single-platform |
| Convergence rate | > 70% | Usually platforms agree |
| Resolution time | < 30 min | Quick reconciliation |
| Escalation rate | < 5% | Rarely need Principal |
| Regression incidents | 0 | Never lose quality in synthesis |

---

## XI. INTEGRATION WITH TRINITY

```
Oracle (Gemini)          Deviser (ChatGPT)         Executor (Claude)
      │                        │                         │
      │                        │                         │
      └────────────┬───────────┘                         │
                   │                                     │
           [Chorus Query]                                │
                   │                                     │
                   ▼                                     │
            Reconciliation                               │
                   │                                     │
                   ▼                                     │
             Plan Packet ────────────────────────────────┘
                   │
                   ▼
            Execution Packet
```

**Chorus happens BEFORE plan generation, not during execution.**

Once a plan is accepted, execute it. Don't re-chorus during execution.

---

## XII. QUICK REFERENCE

### Should I Use Chorus?

```
Is this a constitutional change?
  YES → MANDATORY chorus
  NO → Continue

Is this irreversible?
  YES → MANDATORY chorus
  NO → Continue

Is there time for reconciliation?
  NO → Single platform + note
  YES → Continue

Are there multiple valid approaches?
  YES → RECOMMENDED chorus
  NO → Single platform

Is the stake high enough to justify 3x cost?
  YES → Chorus
  NO → Single platform
```

### Chorus Checklist

- [ ] Query is unambiguous
- [ ] Platforms selected for question type
- [ ] All platforms received identical query
- [ ] All responses collected before reading
- [ ] Reconciliation method applied
- [ ] Minority positions preserved
- [ ] Confidence tagged
- [ ] Final answer documented
- [ ] Packet written to repo

---

**Chorus is for convergence under uncertainty. Use it selectively.**
