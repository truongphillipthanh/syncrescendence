# Chorus Design: Jarvis Concierge + Dispatch + Reconciliation
**Generated**: 2026-01-17T03:23:54Z
**Purpose**: Define multi-platform prompt dispatch and synthesis protocol

---

## Overview

The Chorus model treats platforms as specialized instruments in an ensemble. A single question/task is decomposed, dispatched to optimal platforms, and reconciled into unified output. This document specifies the operational protocol.

---

## 1. Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      JARVIS CONCIERGE                           │
│            (Principal's unified interaction surface)            │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                    ┌──────────┴──────────┐
                    │  PROMPT COMPILER    │
                    │  - Parse intent     │
                    │  - Identify tasks   │
                    │  - Select platforms │
                    └──────────┬──────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
         ▼                     ▼                     ▼
    ┌─────────┐          ┌─────────┐          ┌─────────┐
    │ GEMINI  │          │ CHATGPT │          │ CLAUDE  │
    │ sensing │          │ planning│          │ execute │
    └────┬────┘          └────┬────┘          └────┬────┘
         │                    │                    │
         └────────────────────┼────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │   RECONCILIATION  │
                    │   - Merge outputs │
                    │   - Resolve tension│
                    │   - Synthesize    │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   REPO PACKET    │
                    │  (ground truth)  │
                    └──────────────────┘
```

---

## 2. Prompt Compiler

### Input
Natural language task/question from Principal.

### Processing Steps

**Step 1: Intent Classification**
```yaml
intent_types:
  - sensing: "What exists? What changed? What's the state?"
  - planning: "How should we approach? What's the plan?"
  - execution: "Do this. Create that. Modify this."
  - verification: "Did this work? Is this correct?"
  - synthesis: "What does this mean? How does it connect?"
```

**Step 2: Task Decomposition**
Break complex queries into platform-appropriate subtasks:
```yaml
example_query: "Research the latest on video generation, create a summary, and update our tech stack document"
decomposition:
  - task: "Research video generation landscape"
    platform: chatgpt
    reason: "Deep Research for external intel"
  - task: "Synthesize findings with existing Canon"
    platform: gemini
    reason: "2M context for full Canon read"
  - task: "Update CANON-30300-TECH_STACK"
    platform: claude_code
    reason: "File modification requires execution"
```

**Step 3: Steelman Prompt Generation**
For each platform, generate optimized prompt variant:

| Platform | Prompt Optimization |
|----------|---------------------|
| Gemini | Emphasize corpus scope, request citations, leverage Drive context |
| ChatGPT | Emphasize structured output, request acceptance criteria, leverage Canvas |
| Claude Code | Emphasize file paths, verification commands, constitutional compliance |
| Claude Web | Emphasize synthesis, artifact creation, extended thinking for complex |

### Output
```yaml
dispatch_manifest:
  tasks:
    - id: 1
      platform: chatgpt
      prompt: "[steelman prompt for research]"
      expected_output: "research_report"
    - id: 2
      platform: gemini
      prompt: "[steelman prompt for synthesis]"
      expected_output: "synthesis_with_citations"
    - id: 3
      platform: claude_code
      prompt: "[steelman prompt for execution]"
      expected_output: "file_modification"
      depends_on: [1, 2]
```

---

## 3. Dispatch Map

### Platform Selection Rules

| Task Characteristic | Primary | Secondary | Avoid |
|---------------------|---------|-----------|-------|
| Needs external research | ChatGPT (Deep Research) | Perplexity | Claude (no web) |
| Needs large corpus | Gemini (2M context) | Claude Web (200K) | ChatGPT (400K) |
| Needs file execution | Claude Code | - | All web apps |
| Needs video processing | Gemini | - | All others |
| Needs specification | ChatGPT | Claude Web | Claude Code |
| Needs verification | Claude Code | ChatGPT | - |
| Needs voice output | Grok Voice API | - | All text-only |

### Dispatch Sequencing

**Parallel Dispatch**: When tasks are independent
```
Task 1 → Gemini   ─────┐
Task 2 → ChatGPT  ─────┼──→ Reconciliation
Task 3 → Claude   ─────┘
```

**Sequential Dispatch**: When tasks depend on prior outputs
```
Task 1 → Gemini → Evidence
                    ↓
Task 2 → ChatGPT → Plan (uses Evidence)
                    ↓
Task 3 → Claude → Execution (uses Plan)
```

---

## 4. Tension Map

### Known Tension Patterns

| Tension Type | Manifestation | Resolution |
|--------------|---------------|------------|
| Factual Disagreement | Platform A claims X, Platform B claims Y | Verify via authoritative source; if both plausible, flag uncertainty |
| Scope Conflict | Platform A gives broad answer, Platform B narrow | Choose scope appropriate to original query |
| Recommendation Conflict | Platform A suggests approach X, Platform B suggests Y | Apply 18 Lenses to evaluate; escalate to Principal if both pass |
| Confidence Divergence | Platform A certain, Platform B uncertain | Weight by platform's domain expertise |
| Format Conflict | Platform A returns prose, Platform B returns JSON | Normalize to query's expected format |

### Resolution Protocol

```yaml
resolution_steps:
  1. detect:
      - Compare outputs for factual claims
      - Identify contradictions
      - Flag confidence divergence

  2. classify:
      - factual: Can be verified
      - judgment: Requires evaluation
      - preference: Principal decides

  3. resolve:
      factual: Verify against authoritative source
      judgment: Apply 18 Lenses
      preference: Present options to Principal

  4. document:
      - Log tension in reconciliation record
      - Note resolution method
      - Flag if recurrence expected
```

---

## 5. Reconciliation Rules

### Merge Strategy

**For Evidence (Sensing Tasks)**:
```yaml
merge_rule: union_with_citations
process:
  - Combine all findings
  - Deduplicate by semantic similarity
  - Preserve all unique citations
  - Flag contradictions explicitly
output: Unified evidence packet with all sources
```

**For Plans (Planning Tasks)**:
```yaml
merge_rule: best_of_breed
process:
  - Compare acceptance criteria clarity
  - Evaluate stop conditions completeness
  - Select clearer specification
  - Supplement with unique elements from others
output: Single plan packet combining best elements
```

**For Synthesis (Analysis Tasks)**:
```yaml
merge_rule: hierarchical_integration
process:
  - Identify highest-level synthesis (usually Claude Web)
  - Integrate specific findings from others
  - Preserve nuance from each platform
  - Resolve tensions per tension map
output: Unified synthesis with attributed sections
```

---

## 6. Culmination to Repo

### Packet Creation

Every chorus cycle culminates in one or more repo packets:

```yaml
culmination_artifacts:
  - evidence_packet:
      location: 00-ORCHESTRATION/blackboard/evidence/
      format: EVD-YYYYMMDD-NNN.json
      content: Merged sensing outputs

  - plan_packet:
      location: 00-ORCHESTRATION/blackboard/plans/
      format: PLN-YYYYMMDD-NNN.json
      content: Reconciled planning output

  - execution_log:
      location: 00-ORCHESTRATION/execution_logs/
      format: EXECUTION_LOG-YYYY-MM-DD-directive.md
      content: Execution results and verification

  - canon_update:
      location: 01-CANON/
      format: Modification to existing Canon file
      content: Integrated findings
```

### Commit Protocol

```bash
git add 00-ORCHESTRATION/blackboard/*.json
git add 00-ORCHESTRATION/execution_logs/*.md
git add 01-CANON/*.md  # if updated
git commit -m "feat(chorus): [task description]

Platforms: [gemini, chatgpt, claude_code]
Tensions: [none | resolved: method]

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## 7. Example Chorus Cycle

### Query
"What's the current state of agentic AI across platforms, and update our positioning document"

### Dispatch
```yaml
Task 1 (parallel):
  platform: chatgpt
  prompt: "Use Deep Research to survey current agentic AI capabilities across major platforms (Claude, ChatGPT, Gemini, Grok). Focus on: agent modes, tool calling, autonomy levels, rate limits."

Task 2 (parallel):
  platform: gemini
  prompt: "Query our Canon (CANON-30400, CANON-30300) and recent sources. What's our current documented understanding of agentic architecture?"

Task 3 (sequential, depends on 1+2):
  platform: claude_code
  prompt: "Given [research findings] and [current Canon state], update CANON-30200-POSITIONING to reflect current competitive landscape. Verify changes with git diff."
```

### Reconciliation
- ChatGPT research finds new Claude Cowork features
- Gemini surfaces existing Canon claims about Claude Code primacy
- Tension: Canon says Claude Code is primary agent; research shows Claude Cowork emerging
- Resolution: Update Canon to acknowledge both, differentiate use cases
- Claude Code executes update with verification

### Culmination
- Evidence packet: EVD-YYYYMMDD-001.json (research + Canon query)
- Execution packet: EXE-YYYYMMDD-001.json (Canon update)
- Commit: `feat(chorus): update positioning for Claude Cowork emergence`
