# Packet Schema Index
**Generated**: 2026-01-17T03:23:54Z
**Source**: `00-ORCHESTRATION/schemas/packet_protocol.json`

---

## Overview

The Syncrescendence system uses typed packets for inter-platform communication. Each packet type has a defined schema, naming convention, and storage location.

---

## Packet Types

### 1. Evidence Packet (EVD)
**Description**: Oracle outputs—findings from corpus sensing

**Required Fields**:
| Field | Type | Description |
|-------|------|-------------|
| id | string | EVD-YYYYMMDD-NNN |
| timestamp | ISO8601 | Creation time |
| actor | string | Platform that created (gemini, claude, etc.) |
| query | string | The sensing query |
| corpus_slice | array | Sources consulted |
| findings | array | What was discovered |
| uncertainties | array | What remains unknown |

**Optional Fields**:
| Field | Type | Description |
|-------|------|-------------|
| recommended_probe | string | Suggested next query |
| citations | array | Specific source references |
| confidence | float | Certainty level (0-1) |

**Storage**: `00-ORCHESTRATION/blackboard/evidence/EVD-YYYYMMDD-NNN.json`

**Example**:
```json
{
  "id": "EVD-20260116-001",
  "timestamp": "2026-01-16T00:36:12Z",
  "actor": "directive-046a",
  "query": "Verify operational primitives implementation complete",
  "corpus_slice": ["00-ORCHESTRATION/state/", "00-ORCHESTRATION/blackboard/"],
  "findings": ["system_state.json created and valid", "route_task.py functional"],
  "uncertainties": ["Cross-platform coordination not yet tested"],
  "recommended_probe": "Execute full autonomous cycle"
}
```

---

### 2. Plan Packet (PLN)
**Description**: Deviser outputs—specifications for execution

**Required Fields**:
| Field | Type | Description |
|-------|------|-------------|
| id | string | PLN-YYYYMMDD-NNN |
| timestamp | ISO8601 | Creation time |
| actor | string | Platform that created |
| evidence_ids | array | Evidence packets this plan responds to |
| objective | string | What this plan accomplishes |
| deliverables | array | Expected outputs |
| acceptance_criteria | array | How to verify success |
| stop_conditions | array | When to abort |

**Optional Fields**:
| Field | Type | Description |
|-------|------|-------------|
| estimated_duration | string | Time estimate |
| resource_requirements | array | Required tools/access |
| dependencies | array | Must complete before this |

**Storage**: `00-ORCHESTRATION/blackboard/plans/PLN-YYYYMMDD-NNN.json`

**Example**:
```json
{
  "id": "PLN-20260115-001",
  "timestamp": "2026-01-15T00:05:00Z",
  "actor": "chatgpt",
  "evidence_ids": ["EVD-20260115-001"],
  "objective": "Transcribe and qualify new video",
  "deliverables": ["SOURCE-20260115-creator.md"],
  "acceptance_criteria": ["Transcript complete", "Frontmatter valid", "Signal tier assigned"],
  "stop_conditions": ["Video >4hr without Principal approval", "API error rate >5%"]
}
```

---

### 3. Execution Packet (EXE)
**Description**: Executor outputs—completed work records

**Required Fields**:
| Field | Type | Description |
|-------|------|-------------|
| id | string | EXE-YYYYMMDD-NNN |
| timestamp | ISO8601 | Completion time |
| actor | string | Executor platform |
| plan_id | string | Plan this execution implements |
| commands_run | array | Commands executed |
| files_changed | array | Files created/modified |
| verification_output | string | Result of verification |

**Optional Fields**:
| Field | Type | Description |
|-------|------|-------------|
| duration | string | Time taken |
| errors_encountered | array | Any errors (even if resolved) |
| rollback_notes | string | If rollback needed, why |

**Storage**: `00-ORCHESTRATION/blackboard/executions/EXE-YYYYMMDD-NNN.json`

**Example**:
```json
{
  "id": "EXE-20260115-001",
  "timestamp": "2026-01-15T00:10:00Z",
  "actor": "claude_code_2",
  "plan_id": "PLN-20260115-001",
  "commands_run": ["transcribe_youtube.py [url]", "validate_frontmatter.sh"],
  "files_changed": ["04-SOURCES/processed/SOURCE-20260115-creator.md"],
  "verification_output": "Frontmatter valid. Signal tier: STRATEGIC."
}
```

---

### 4. Audit Packet (AUD)
**Description**: Verification outputs—quality assessment

**Required Fields**:
| Field | Type | Description |
|-------|------|-------------|
| id | string | AUD-YYYYMMDD-NNN |
| timestamp | ISO8601 | Audit time |
| actor | string | Auditor platform |
| execution_id | string | Execution being audited |
| plan_id | string | Plan the execution was based on |
| criteria_results | object | Pass/fail for each acceptance criterion |
| drift_analysis | string | Assessment of deviation from plan |
| recommendation | string | APPROVE / REJECT / ITERATE |

**Optional Fields**:
| Field | Type | Description |
|-------|------|-------------|
| state_transition_justified | boolean | Was state change appropriate |
| canon_integration_recommended | boolean | Should this integrate into Canon |

**Storage**: `00-ORCHESTRATION/blackboard/audits/AUD-YYYYMMDD-NNN.json`

**Example**:
```json
{
  "id": "AUD-20260115-001",
  "timestamp": "2026-01-15T00:15:00Z",
  "actor": "chatgpt",
  "execution_id": "EXE-20260115-001",
  "plan_id": "PLN-20260115-001",
  "criteria_results": {
    "transcript_complete": true,
    "frontmatter_valid": true,
    "signal_tier_assigned": true
  },
  "drift_analysis": "No drift from plan",
  "recommendation": "APPROVE - ready for integration"
}
```

---

### 5. Capability Event Packet (CAP)
**Description**: Platform self-reports on capability changes

**Required Fields**:
| Field | Type | Description |
|-------|------|-------------|
| id | string | CAP-YYYYMMDD-NNN |
| timestamp | ISO8601 | Event time |
| platform | string | Platform reporting |
| event_type | string | Type of capability event |
| details | string | Description |

**Optional Fields**:
| Field | Type | Description |
|-------|------|-------------|
| routing_impact | string | How this affects routing |
| action_required | boolean | Does Principal need to act |

**Storage**: `00-ORCHESTRATION/blackboard/capabilities/CAP-YYYYMMDD-NNN.json`

**Example**:
```json
{
  "id": "CAP-20260115-001",
  "timestamp": "2026-01-15T00:20:00Z",
  "platform": "gemini",
  "event_type": "rate_limit_hit",
  "details": "Video processing quota exhausted for day",
  "routing_impact": "Route video tasks to alternative or queue",
  "action_required": false
}
```

---

## Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Evidence | EVD-YYYYMMDD-NNN | EVD-20260116-001 |
| Plan | PLN-YYYYMMDD-NNN | PLN-20260116-001 |
| Execution | EXE-YYYYMMDD-NNN | EXE-20260116-001 |
| Audit | AUD-YYYYMMDD-NNN | AUD-20260116-001 |
| Capability | CAP-YYYYMMDD-NNN | CAP-20260116-001 |

NNN = Sequential number within day, zero-padded to 3 digits.

---

## Current Blackboard State

As of 2026-01-16:
```
00-ORCHESTRATION/blackboard/
├── evidence/
│   └── EVD-20260116-001.json
├── plans/
│   └── PLN-20260116-001.json
├── executions/
│   └── EXE-20260116-001.json
├── audits/
│   └── AUD-20260116-001.json
└── capabilities/
    (empty)
```

Metrics from system_state.json:
- packets_created: 4
- packets_processed: 4
- autonomous_cycles: 1
