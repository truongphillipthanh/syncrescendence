# Teleology Variables Schema
**Generated**: 2026-01-17T03:23:54Z
**Purpose**: Stable schema for mapping every platform feature to operational dimensions

---

## Overview

Every surface feature in the platform constellation must be characterized along these variables to enable rational routing, cost optimization, and failure mode prediction.

---

## Variable Definitions

### 1. teleology
**Type**: string (one sentence)
**Definition**: The primary purpose this feature serves in the Syncrescendence architecture.
**Examples**:
- "Enable filesystem-native code execution with persistent context"
- "Process video at 263 tok/sec with visual speaker diarization"
- "Generate plans with acceptance criteria from evidence packets"

### 2. inputs
**Type**: array of strings
**Definition**: What the feature consumes.
**Categories**:
- `text_prompt` — Natural language instruction
- `file_path` — Local filesystem path
- `url` — Web resource
- `packet` — Structured JSON packet
- `conversation_history` — Prior messages in session
- `project_memory` — Persistent project-scoped memory
- `account_memory` — Account-level persistent memory
- `google_services` — Gmail, Drive, Calendar, etc.

### 3. outputs
**Type**: array of strings
**Definition**: What the feature produces.
**Categories**:
- `text_response` — Natural language output
- `file_creation` — New file on filesystem
- `file_modification` — Changed existing file
- `structured_data` — JSON/CSV/structured output
- `execution_result` — Command/code execution output
- `artifact` — Claude web artifact
- `audio` — Generated audio file
- `video` — Generated video file
- `image` — Generated image

### 4. persistence_stratum
**Type**: enum
**Definition**: Where state persists.
| Value | Description |
|-------|-------------|
| ephemeral | Lost when session ends |
| session | Persists within conversation |
| project | Persists across sessions in same project |
| account | Persists across all projects for user |
| external_doc | Persists in external system (Drive, GitHub) |
| repo | Persists in Git repository |

### 5. permissions
**Type**: object
**Definition**: What the feature can access.
```yaml
permissions:
  filesystem: read|write|none
  network: full|limited|none
  external_services: [list of services]
  secrets: can_access|cannot_access
```

### 6. account_boundary
**Type**: string
**Definition**: Which account context this feature operates within.
**Values**: `personal`, `hybrid`, `gmail`, `google_workspace`, `openai`, `multi_account`

### 7. failure_modes
**Type**: array of objects
**Definition**: How this feature fails and lies.
```yaml
failure_modes:
  - mode: "context_invisibility"
    description: "Chat history not visible in web app"
    detection: "Ask feature to recall prior context"
    recovery: "Export and re-inject context"
  - mode: "rate_limit"
    description: "Quota exhausted"
    detection: "Error message or degraded response"
    recovery: "Wait or switch platform"
```

### 8. verification_method
**Type**: string
**Definition**: How to verify the feature worked correctly.
**Examples**:
- "Check file exists at expected path"
- "Validate JSON structure of output"
- "Run verification command and check exit code"
- "Compare output against acceptance criteria"

### 9. cost_profile
**Type**: object
**Definition**: Resource consumption characteristics.
```yaml
cost_profile:
  pricing_model: "per_token|per_message|per_minute|per_call|subscription"
  approximate_cost: "$X per Y"
  rate_limit: "N calls per time_period"
  thinking_overhead: "none|variable|fixed"
```

### 10. latency_profile
**Type**: object
**Definition**: Time characteristics.
```yaml
latency_profile:
  time_to_first_token: "Xms"
  typical_completion: "Xs"
  max_timeout: "Xs"
  async_available: true|false
```

### 11. best_fit_tasks
**Type**: array of strings
**Definition**: Task types this feature excels at.
**Examples**: `corpus_sensing`, `video_processing`, `planning`, `execution`, `audit`

### 12. anti_fit_tasks
**Type**: array of strings
**Definition**: Task types this feature should NOT be used for.
**Examples**: `real_time_interaction`, `large_file_processing`, `sensitive_credentials`

### 13. second_order_effects
**Type**: array of objects
**Definition**: Non-obvious consequences of using this feature.
```yaml
second_order_effects:
  - effect: "coordination_tax"
    description: "Requires manual context graduation"
    severity: "medium"
  - effect: "drift_risk"
    description: "Stateless queries may diverge from repo truth"
    severity: "low"
```

### 14. third_order_effects
**Type**: array of objects
**Definition**: Systemic consequences at scale.
```yaml
third_order_effects:
  - effect: "platform_lock_in"
    description: "Deep integration creates switching cost"
    severity: "high"
  - effect: "cognitive_load"
    description: "User must track multiple platform states"
    severity: "medium"
```

---

## Example: Complete Feature Profile

```yaml
feature: claude_code_cli
teleology: "Enable filesystem-native agentic execution with constitutional governance"
inputs:
  - text_prompt
  - file_path
  - conversation_history
outputs:
  - text_response
  - file_creation
  - file_modification
  - execution_result
persistence_stratum: repo
permissions:
  filesystem: write
  network: limited
  external_services: [mcp_servers]
  secrets: cannot_access
account_boundary: hybrid
failure_modes:
  - mode: context_overflow
    description: "Context fills to 95% triggering auto-compaction"
    detection: "claude status shows high context usage"
    recovery: "/compact or start new session"
  - mode: tool_rejection
    description: "Safety filter blocks legitimate operation"
    detection: "Tool call rejected with policy message"
    recovery: "Rephrase or escalate to Principal"
verification_method: "git status shows expected changes; verification commands pass"
cost_profile:
  pricing_model: subscription
  approximate_cost: "$20/month (Pro tier)"
  rate_limit: "~45 Opus/5hr, ~100 Sonnet/5hr"
  thinking_overhead: variable
latency_profile:
  time_to_first_token: "~500ms"
  typical_completion: "2-30s depending on complexity"
  max_timeout: "600s"
  async_available: false
best_fit_tasks:
  - execution
  - code_generation
  - file_manipulation
  - verification
anti_fit_tasks:
  - corpus_sensing (limited context)
  - video_processing (no multimodal)
  - long_planning (better in web with artifacts)
second_order_effects:
  - effect: session_fragmentation
    description: "Each session starts fresh without project memory"
    severity: low
third_order_effects:
  - effect: cli_dependency
    description: "Heavy reliance on CLI creates macOS lock-in"
    severity: medium
```

---

## Usage

This schema enables:
1. **Rational routing**: Match task to feature by best_fit_tasks
2. **Failure prediction**: Anticipate failure_modes before they occur
3. **Cost optimization**: Compare cost_profiles across alternatives
4. **Systemic awareness**: Track nth_order_effects at scale
