# Teleology Variables Schema v2
**Generated**: 2026-01-17T04:55:00Z
**Purpose**: Enhanced schema for characterizing platform/feature teleology with failure modes

---

## Core Variables

### 1. Identity Variables

| Variable | Type | Description | Example Values |
|----------|------|-------------|----------------|
| `platform` | string | Parent platform | claude, openai, gemini, perplexity, xai |
| `feature` | string | Specific feature/capability | claude_code_cli, chatgpt_web_app, gemini_notebooklm |
| `account` | string | Account boundary | personal, hybrid, openai, google, xai |
| `version` | string | Feature version if relevant | gpt-5.2, gemini-2.5-pro, opus-4.5 |

### 2. Teleology Variables (Purpose)

| Variable | Type | Description | Example Values |
|----------|------|-------------|----------------|
| `teleology` | string | Core purpose/function | Filesystem-native agentic execution, Corpus-scale sensing |
| `role_in_architecture` | enum | Trinity role | oracle, deviser, executor, sensor, concierge |
| `primary_outputs` | array | What it produces | [text_response, file_creation, execution_result] |
| `primary_inputs` | array | What it consumes | [text_prompt, file_path, conversation_history] |

### 3. Capability Variables

| Variable | Type | Description | Example Values |
|----------|------|-------------|----------------|
| `context_window` | integer | Max tokens | 200000, 2000000, 128000 |
| `multimodal` | object | Media capabilities | {vision: true, audio: true, video: true} |
| `tool_calling` | boolean | Can invoke tools | true, false |
| `code_execution` | enum | Code running capability | none, sandboxed, filesystem |

### 4. Persistence Variables

| Variable | Type | Description | Example Values |
|----------|------|-------------|----------------|
| `persistence_stratum` | enum | Where state lives | ephemeral, session, project, account, repo, external_doc |
| `memory_type` | enum | Memory architecture | none, conversation, project, account |
| `memory_visibility` | enum | Can user inspect memory? | full, partial, opaque |
| `export_capability` | enum | Can export artifacts? | full, partial, none |

### 5. Permission Variables

| Variable | Type | Description | Example Values |
|----------|------|-------------|----------------|
| `permissions_filesystem` | enum | Filesystem access | none, read, write |
| `permissions_network` | enum | Network access | none, limited, full |
| `permissions_external_tools` | array | Tool integrations | [mcp, github, drive] |

### 6. Operational Variables

| Variable | Type | Description | Example Values |
|----------|------|-------------|----------------|
| `best_fit_tasks` | array | Optimal use cases | [execution, corpus_sensing, planning] |
| `anti_fit_tasks` | array | Poor use cases | [video_processing, file_manipulation] |
| `cost_per_month` | string | Subscription cost | $20, $0, pay_per_use |
| `rate_limit` | string | Usage limits | ~45_opus/5hr, liberal, 40/month |
| `latency_profile` | enum | Response speed | instant, seconds, minutes |

### 7. Failure Mode Variables (NEW)

| Variable | Type | Description | Example Values |
|----------|------|-------------|----------------|
| `failure_modes` | array | Known failure patterns | [context_overflow, session_fragmentation] |
| `failure_detection` | object | How to detect each failure | {context_overflow: "model refuses new input"} |
| `failure_recovery` | object | How to recover | {context_overflow: "compact or new session"} |
| `failure_severity` | object | Impact of each failure | {context_overflow: "high"} |

### 8. Verification Variables (NEW)

| Variable | Type | Description | Example Values |
|----------|------|-------------|----------------|
| `verification_method` | enum | How to verify it works | command_output, artifact_check, manual |
| `verification_commands` | array | Commands to verify | ["make verify", "git status"] |
| `ground_truth_signal` | string | What confirms success | "execution_log exists and is valid" |

### 9. Nth-Order Effect Variables (NEW)

| Variable | Type | Description | Example Values |
|----------|------|-------------|----------------|
| `second_order_effects` | array | Consequences of using | [context_graduation_tax, session_fragmentation] |
| `third_order_effects` | array | Deeper consequences | [synthesis_bottleneck, platform_risk] |
| `mitigation_strategies` | array | How to manage effects | [forced_export, multi_platform_literacy] |

---

## Enumeration Definitions

### persistence_stratum

| Value | Meaning | Duration |
|-------|---------|----------|
| `ephemeral` | Gone when session ends | Minutes to hours |
| `session` | Lasts within session | Hours |
| `project` | Persists in project context | Days to weeks |
| `account` | Persists across projects | Months |
| `repo` | Lives in repository | Permanent |
| `external_doc` | Lives in external document system | Permanent |

### role_in_architecture

| Value | Meaning | Artifact Produced |
|-------|---------|-------------------|
| `oracle` | Corpus-scale sensing | Evidence Packets |
| `deviser` | Planning and specification | Plan/Audit Packets |
| `executor` | Filesystem operations | Execution Packets |
| `sensor` | Real-time information gathering | Evidence fragments |
| `concierge` | Primary conversational surface | Routing decisions |

### latency_profile

| Value | Meaning | Expected Time |
|-------|---------|---------------|
| `instant` | Sub-second response | <1s |
| `seconds` | Quick response | 1-30s |
| `minutes` | Deliberate processing | 30s-10m |
| `async` | Background processing | >10m |

---

## Example Feature Record

```yaml
feature: claude_code_cli
platform: claude
account: hybrid
version: opus-4.5

teleology: "Filesystem-native agentic execution with constitutional governance"
role_in_architecture: executor

primary_inputs:
  - text_prompt
  - file_path
  - conversation_history
primary_outputs:
  - text_response
  - file_creation
  - file_modification
  - execution_result

context_window: 200000
multimodal:
  vision: true
  audio: false
  video: false
tool_calling: true
code_execution: filesystem

persistence_stratum: repo
memory_type: project
memory_visibility: full
export_capability: full

permissions_filesystem: write
permissions_network: limited
permissions_external_tools:
  - mcp
  - bash
  - git

best_fit_tasks:
  - execution
  - code_generation
  - file_manipulation
  - verification
anti_fit_tasks:
  - corpus_sensing
  - video_processing
  - long_planning

cost_per_month: "$20"
rate_limit: "~45_opus/5hr"
latency_profile: seconds

failure_modes:
  - context_overflow
  - tool_rejection
  - session_fragmentation
failure_detection:
  context_overflow: "Auto-compact triggers or model refuses input"
  tool_rejection: "Permission denied or tool call fails"
  session_fragmentation: "Context loss between sessions"
failure_recovery:
  context_overflow: "/compact or start new session with context file"
  tool_rejection: "Check permissions, adjust command"
  session_fragmentation: "Load continuation packet"
failure_severity:
  context_overflow: medium
  tool_rejection: low
  session_fragmentation: high

verification_method: command_output
verification_commands:
  - "git status"
  - "make verify"
  - "cat 00-ORCHESTRATION/state/system_state.json"
ground_truth_signal: "Files changed match expectation, verification passes"

second_order_effects:
  - execution_logging_overhead
  - commit_discipline_required
third_order_effects:
  - repo_becomes_ground_truth
  - web_apps_demoted_to_cache
mitigation_strategies:
  - atomic_commits
  - verification_before_completion
```

---

## Schema Validation

JSON Schema for validation:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["feature", "platform", "teleology", "persistence_stratum"],
  "properties": {
    "feature": {"type": "string"},
    "platform": {"type": "string", "enum": ["claude", "openai", "gemini", "perplexity", "xai", "other"]},
    "account": {"type": "string"},
    "teleology": {"type": "string"},
    "role_in_architecture": {
      "type": "string",
      "enum": ["oracle", "deviser", "executor", "sensor", "concierge", "utility"]
    },
    "persistence_stratum": {
      "type": "string",
      "enum": ["ephemeral", "session", "project", "account", "repo", "external_doc"]
    },
    "failure_modes": {
      "type": "array",
      "items": {"type": "string"}
    },
    "failure_severity": {
      "type": "object",
      "additionalProperties": {"type": "string", "enum": ["low", "medium", "high", "critical"]}
    }
  }
}
```

---

## Relationship to Other Artifacts

| This Schema | Related To | Relationship |
|-------------|------------|--------------|
| teleology_variables_v2 | teleology_atlas_v2.csv | Schema defines columns |
| teleology_variables_v2 | routing_constraints_v1 | Informs routing rules |
| teleology_variables_v2 | capabilities.json | Subsets to runtime state |
| teleology_variables_v2 | CANON-31150 | Auto-generates from this data |
