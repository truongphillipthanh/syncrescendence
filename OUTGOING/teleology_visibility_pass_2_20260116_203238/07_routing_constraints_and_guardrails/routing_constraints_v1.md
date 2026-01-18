# Routing Constraints v1
**Generated**: 2026-01-17T05:10:00Z
**Purpose**: Upgraded routing model with constraints beyond task_type

---

## Overview

Current routing routes by `task_type` alone. This is insufficient.

Enhanced routing considers:
1. **Task type** (what needs to be done)
2. **Context requirements** (how much input needed)
3. **Risk level** (what could go wrong)
4. **Tool requirements** (what capabilities needed)
5. **Latency tolerance** (how fast needed)
6. **Coherence requirement** (how much synthesis before action)

---

## Constraint Dimensions

### Dimension 1: Context Size

| Level | Token Requirement | Best Platform |
|-------|-------------------|---------------|
| Minimal | <10K | Any |
| Standard | 10K-100K | Claude, ChatGPT |
| Large | 100K-500K | Claude, Gemini |
| Corpus | 500K-2M | Gemini only |
| Extreme | >2M | Gemini (experimental) |

**Rule**: If context > 200K, route to Gemini. If context > 500K, Gemini is mandatory.

### Dimension 2: Risk Level

| Level | Definition | Routing Impact |
|-------|------------|----------------|
| LOW | Reversible, no protected zones | Standard routing |
| MEDIUM | Affects state files, requires verification | Add verification step |
| HIGH | Affects Canon, multiple files | Require plan packet first |
| CRITICAL | Constitutional changes, deletions | Require Principal approval + chorus |

**Rule**: Risk ≥ HIGH requires plan packet. Risk = CRITICAL requires chorus.

### Dimension 3: Tool Requirements

| Requirement | Platforms That Support |
|-------------|------------------------|
| Filesystem write | Claude Code |
| Filesystem read only | Claude Code, (Gemini via Drive) |
| Git operations | Claude Code, Codex CLI |
| Web browsing | ChatGPT, Gemini, Perplexity |
| Video processing | Gemini |
| API calls | AI Studio, Supabase |
| MCP tools | Claude Code |

**Rule**: Route to platform that has required tools. If multiple, prefer by other constraints.

### Dimension 4: Latency Tolerance

| Level | Acceptable Time | Platform Preference |
|-------|-----------------|---------------------|
| Instant | <30s | Haiku, Flash |
| Normal | 30s-5m | Sonnet, Gemini |
| Deliberate | 5m-30m | Opus, Thinking, Deep Research |
| Background | >30m | Batch operations, async |

**Rule**: Match model capability to latency requirement. Don't use Opus for instant needs.

### Dimension 5: Coherence Requirement

| Level | Description | Pre-Action Requirement |
|-------|-------------|------------------------|
| EXECUTE | Clear instructions, just do it | None |
| VERIFY | Do it, but verify after | Verification step |
| PLAN | Need plan before action | Plan packet required |
| SYNTHESIZE | Need synthesis before planning | Evidence packet → Plan packet |
| ARCHITECT | Need architectural analysis | Chorus + comprehensive synthesis |

**Rule**: Higher coherence requirement = more pre-work before execution.

---

## Routing Matrix

### By Task Type + Constraints

| Task Type | Default Platform | Context Upgrade | Risk Upgrade | Coherence Upgrade |
|-----------|------------------|-----------------|--------------|-------------------|
| execution | Claude Code | - | +verification | +plan |
| code_generation | Claude Code | - | +verification | +plan |
| corpus_query | Gemini | mandatory | - | - |
| video_processing | Gemini | mandatory | - | - |
| planning | ChatGPT | →Gemini if large | +chorus | - |
| audit | ChatGPT/Claude-3 | - | - | - |
| research_external | Perplexity/Deep Research | - | - | +grounding |
| research_internal | Gemini/NotebookLM | - | - | - |
| synthesis | Claude Web | →Gemini if large | +chorus | - |
| specification | ChatGPT | - | +Principal | - |

### By Coherence Requirement

| Coherence Level | Before Execution | During Execution | After Execution |
|-----------------|------------------|------------------|-----------------|
| EXECUTE | Nothing | Execute | Log |
| VERIFY | Nothing | Execute | Verify + Log |
| PLAN | Create plan | Execute per plan | Audit + Log |
| SYNTHESIZE | Evidence → Plan | Execute per plan | Audit + Log |
| ARCHITECT | Chorus → Synthesis → Plan | Execute per plan | Full review |

---

## Routing Decision Tree

```
START
  │
  ├─► What is the context size?
  │     ├─► >200K → Must include Gemini
  │     └─► ≤200K → Continue
  │
  ├─► What tools are needed?
  │     ├─► Filesystem write → Claude Code
  │     ├─► Git → Claude Code or Codex
  │     ├─► Video → Gemini
  │     └─► Web → ChatGPT/Gemini/Perplexity
  │
  ├─► What is the risk level?
  │     ├─► CRITICAL → Require chorus + Principal approval
  │     ├─► HIGH → Require plan packet
  │     ├─► MEDIUM → Add verification
  │     └─► LOW → Standard
  │
  ├─► What is the coherence requirement?
  │     ├─► ARCHITECT → Chorus first
  │     ├─► SYNTHESIZE → Evidence first
  │     ├─► PLAN → Plan packet first
  │     └─► EXECUTE/VERIFY → Proceed
  │
  ├─► What is latency tolerance?
  │     ├─► Instant → Haiku/Flash
  │     ├─► Normal → Sonnet/Gemini
  │     ├─► Deliberate → Opus/Thinking
  │     └─► Background → Batch
  │
  └─► ROUTE to selected platform with selected pre-work
```

---

## Escalation Paths

### When Primary Fails

| Failure Type | Escalation Path |
|--------------|-----------------|
| Context overflow | Compact → New session with packet → Gemini if still too large |
| Tool not available | Find alternate tool → Manual fallback |
| Rate limited | Wait → Alternate account → Alternate platform |
| Quality insufficient | Upgrade model → Add thinking → Chorus |

### When Plan Fails

```yaml
plan_failure_escalation:
  first_attempt: revise_plan_with_feedback
  second_attempt: escalate_to_higher_coherence_level
  third_attempt: escalate_to_principal
```

### When Execution Fails

```yaml
execution_failure_escalation:
  first_attempt: retry_with_adjusted_approach
  second_attempt: fallback_to_simpler_model
  third_attempt: manual_intervention_required
```

---

## Protected Zone Routing

Special routing for protected zones:

| Zone | Required Route |
|------|----------------|
| `01-CANON/` | Plan → Principal approval → Execute → Audit |
| `00-ORCHESTRATION/state/` | Verification required |
| `CLAUDE.md` | Principal approval mandatory |
| `config/coordination.yaml` | Principal approval mandatory |

**Never**:
- Direct execution in Canon without plan
- Deletion in protected zone without Principal
- Modification of constitutional docs via routine routing

---

## Routing Metadata

When routing, log decision:

```json
{
  "task_id": "TASK-001",
  "routed_to": "claude_code_2",
  "routing_decision": {
    "task_type": "execution",
    "context_size": "standard",
    "risk_level": "medium",
    "tools_needed": ["filesystem_write", "git"],
    "latency_tolerance": "normal",
    "coherence_requirement": "verify"
  },
  "pre_work_required": ["verification_step"],
  "escalation_path": ["retry", "haiku_fallback", "principal"]
}
```

---

## Integration with coordination.yaml

Add to existing coordination.yaml:

```yaml
routing_constraints:
  context_thresholds:
    large: 100000
    corpus: 500000
    extreme: 2000000

  risk_triggers:
    high:
      - path_contains: "01-CANON"
      - path_contains: "CLAUDE.md"
      - operation: delete
    critical:
      - path_contains: "config/coordination.yaml"
      - operation: bulk_delete

  coherence_triggers:
    synthesize:
      - task_type: strategic_decision
      - task_type: architectural_change
    architect:
      - task_type: constitutional_change
      - risk_level: critical

  escalation_defaults:
    max_retries: 3
    escalation_order: [retry, fallback_model, manual]
```

---

## Routing Commands

For Claude Code, implement routing awareness:

```bash
# Route a task
route_task "Process 50 videos from backlog" --context=corpus --risk=low --latency=background

# Check routing recommendation
route_task --check "Refactor Canon numbering" --context=large --risk=high

# Override routing
route_task "Emergency fix" --platform=claude_code --force
```
