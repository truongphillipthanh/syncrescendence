# Chorus Protocol v1
**Generated**: 2026-01-17T04:55:00Z
**Purpose**: When to use multiple platforms, how to reconcile outputs, how to prevent analysis paralysis

---

## Core Principle

**Chorus is a selective instrument, not a default mode.**

Using multiple platforms for every query creates:
- Coordination overhead (3x cost, 3x time)
- Reconciliation burden (whose answer wins?)
- Analysis paralysis (too many perspectives)
- Prompt maintenance proliferation

Use chorus when the stakes justify the cost.

---

## When to Use Chorus

### Tier 1: Mandatory Chorus (High Stakes)

| Situation | Why | Platforms |
|-----------|-----|-----------|
| Constitutional changes | Irreversible, affects all future work | Claude + ChatGPT + Gemini |
| Canon integration (paradigm) | Permanent knowledge addition | At least 2 platforms |
| Strategic pivot | Changes system direction | All available |

### Tier 2: Recommended Chorus (Medium Stakes)

| Situation | Why | Platforms |
|-----------|-----|-----------|
| Complex architectural decision | Multiple valid approaches | 2 platforms |
| Contradiction detected in sources | Need reconciliation | 2 platforms |
| Novel technical challenge | Diverse reasoning helps | 2 platforms |

### Tier 3: Single Platform (Low Stakes)

| Situation | Why | Platform |
|-----------|-----|----------|
| Routine execution | Clear instructions | Claude Code |
| Simple research query | Speed over depth | Perplexity or Gemini |
| Known pattern application | No ambiguity | Routed platform |
| Incremental iteration | Context continuity | Same platform |

---

## Chorus Dispatch Protocol

### Step 1: Formulate Query

Create a **single, unambiguous query** that all platforms will receive.

```markdown
## Chorus Query: [QUERY-ID]

**Question**: [Specific question with no ambiguity]

**Context**: [Minimum necessary context, identical for all]

**Expected Output**: [What form should the answer take?]

**Evaluation Criteria**: [How will we judge answers?]
```

### Step 2: Parallel Dispatch

Send identical query to selected platforms **simultaneously**.

```yaml
dispatch:
  platforms: [claude_web, chatgpt, gemini]
  query_id: QUERY-20260116-001
  timeout: 10_minutes
  expected_output: structured_analysis
```

### Step 3: Collect Responses

Gather all responses before evaluation. Do not read responses until all arrive.

### Step 4: Reconcile

Apply reconciliation protocol (see below).

---

## Reconciliation Protocol

### Method 1: Convergent Answer

**When**: All platforms agree on key points.

**Action**: Accept convergent answer, note any nuance differences in documentation.

### Method 2: Complementary Answers

**When**: Platforms provide different but compatible perspectives.

**Action**: Synthesize into unified answer that incorporates all perspectives.

```markdown
## Synthesized Answer

### From Claude
- [Unique contribution]

### From ChatGPT
- [Unique contribution]

### From Gemini
- [Unique contribution]

### Unified Position
[How these combine into coherent answer]
```

### Method 3: Conflicting Answers

**When**: Platforms directly contradict each other.

**Action**: Apply decision framework.

```yaml
conflict_resolution:
  1. Check grounding:
     - Which answer cites sources?
     - Which can be verified against repo?

  2. Apply 18 Lenses:
     - Which answer passes more lenses?
     - Which aligns with constitutional rules?

  3. Principal judgment:
     - If still unresolved, escalate to Principal
     - Document reasoning for decision
```

### Method 4: Irreconcilable Conflict

**When**: Fundamental disagreement with no clear resolution.

**Action**: Do not proceed. Gather more evidence.

```yaml
irreconcilable_action:
  1. Document the conflict explicitly
  2. Identify what additional evidence would resolve it
  3. Dispatch evidence-gathering query to appropriate platform
  4. Return to reconciliation with new evidence
```

---

## Anti-Patterns (Chorus Failure Modes)

### Analysis Paralysis

**Symptom**: Multiple rounds of chorus queries without reaching decision.

**Detection**: Same question asked 3+ times with no closure.

**Prevention**:
- Set decision deadline before dispatch
- Accept "good enough" over "perfect"
- Principal makes final call if deadline reached

### Regression to Mean

**Symptom**: Reconciliation loses each platform's best insight.

**Detection**: Synthesized answer is worse than any individual answer.

**Prevention**:
- Preserve unique contributions explicitly
- Don't over-compromise
- Mark "minority positions worth noting"

### Prompt Proliferation

**Symptom**: Maintaining N different prompts for N platforms.

**Detection**: Prompts diverge, results become incomparable.

**Prevention**:
- Single source of truth for chorus queries
- Identical query text across platforms
- Vary only output format if needed

### Coordination Tax

**Symptom**: More time spent orchestrating than thinking.

**Detection**: Chorus overhead exceeds single-platform time.

**Prevention**:
- Default to single platform
- Chorus only when explicitly triggered
- Streamline dispatch/collect process

---

## Platform Selection for Chorus

### By Question Type

| Question Type | Recommended Platforms | Rationale |
|---------------|----------------------|-----------|
| Factual research | Perplexity + Gemini | Citation discipline |
| Strategic decision | Claude + ChatGPT | Reasoning depth |
| Technical architecture | Claude + ChatGPT | Different strengths |
| Corpus analysis | Gemini (single) | 2M context advantage |
| Real-time intelligence | Grok + Perplexity | Current information |

### By Risk Level

| Risk Level | Chorus Size | Reconciliation Depth |
|------------|-------------|----------------------|
| Low | 0 (single platform) | N/A |
| Medium | 2 | Quick comparison |
| High | 3 | Full protocol |
| Critical | 3+ Principal | Full protocol + sign-off |

---

## Chorus Artifacts

### Chorus Query Log

Store in `00-ORCHESTRATION/blackboard/chorus/`:

```json
{
  "id": "CHR-20260116-001",
  "timestamp": "2026-01-16T15:00:00Z",
  "query": "...",
  "platforms_dispatched": ["claude", "chatgpt", "gemini"],
  "responses_received": 3,
  "reconciliation_method": "convergent",
  "final_answer": "...",
  "minority_positions": [],
  "time_to_resolution": "25m"
}
```

### Conflict Record

When irreconcilable:

```json
{
  "id": "CHR-20260116-002",
  "query": "...",
  "conflict_type": "fundamental_disagreement",
  "positions": {
    "claude": "X because...",
    "chatgpt": "Y because...",
    "gemini": "Z because..."
  },
  "evidence_needed": "...",
  "escalated_to": "principal",
  "resolution": "...",
  "resolution_date": "..."
}
```

---

## Metrics

Track chorus effectiveness:

| Metric | Target | Meaning |
|--------|--------|---------|
| Chorus frequency | <10% of queries | Most work is single-platform |
| Convergence rate | >70% | Usually platforms agree |
| Resolution time | <30m | Quick reconciliation |
| Escalation rate | <5% | Rarely need Principal |
| Regression incidents | 0 | Never lose quality in synthesis |

---

## Integration with Trinity Architecture

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

Chorus happens **before** plan generation, not during execution.
