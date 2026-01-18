# Operational Spine Overview
**Generated**: 2026-01-17T03:23:54Z

---

## The Spine: How Decisions Become Artifacts

The Syncrescendence operational spine routes signals from sensing through planning, execution, and verification into persistent artifacts. This document describes the complete flow.

---

## 1. State Model

### Ground Truth Location
```
00-ORCHESTRATION/state/
├── system_state.json      # Current system vector
├── events.jsonl           # Append-only event log
├── tasks.csv              # Task ledger (authoritative)
├── capabilities.json      # Platform capability ledger
├── projects.csv           # Project tracking
├── sprints.csv            # Sprint tracking
└── burndown.csv           # Velocity tracking
```

### system_state.json Structure
```json
{
  "schema_version": "1.0.0",
  "timestamp": "ISO8601",
  "session": {
    "oracle": 13,           // Current Oracle session number
    "blitzkrieg": 46,       // Current Blitzkrieg number
    "stream": "A"           // Current stream (A/B for parallel)
  },
  "active_tasks": [],       // Currently executing tasks
  "platform_status": {
    "claude_code_1": { "status": "available|executing", "last_active": "ISO8601" },
    "claude_code_2": { ... },
    "claude_code_3": { ... },
    "gemini": { ... },
    "chatgpt": { ... }
  },
  "metrics": {
    "autonomous_cycles": 1,
    "relay_cycles": 0,
    "relay_reduction_ratio": 0.0,
    "packets_created": 4,
    "packets_processed": 4
  },
  "last_state_hash": null    // For integrity verification
}
```

### Event Log Model (events.jsonl)
Append-only JSONL format. Each line is a discrete event:
```json
{"timestamp":"ISO8601","event":"event_type","actor":"who","type":"category","details":{}}
```

Event types:
- `system_init` — Session/directive initialization
- `routing_decision` — Task routing to platform
- `execution_complete` — Work completion
- `packet_created` — New packet in blackboard
- `state_update` — System state change
- `context_graduation` — Web → Repository artifact creation

---

## 2. Packet Lifecycle

### Blackboard Structure
```
00-ORCHESTRATION/blackboard/
├── evidence/              # EVD-YYYYMMDD-NNN.json
├── plans/                 # PLN-YYYYMMDD-NNN.json
├── executions/            # EXE-YYYYMMDD-NNN.json
├── audits/                # AUD-YYYYMMDD-NNN.json
└── capabilities/          # CAP-YYYYMMDD-NNN.json (platform events)
```

### Packet Flow
```
┌─────────────────────────────────────────────────────────────────┐
│                         SENSING LAYER                           │
│  (Gemini: corpus queries, video processing, YouTube monitoring) │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
                    ┌──────────────────┐
                    │  EVIDENCE PACKET │
                    │  EVD-YYYYMMDD-N  │
                    │  (Oracle role)   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   PLAN PACKET    │
                    │  PLN-YYYYMMDD-N  │
                    │  (Deviser role)  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ EXECUTION PACKET │
                    │  EXE-YYYYMMDD-N  │
                    │ (Executor role)  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   AUDIT PACKET   │
                    │  AUD-YYYYMMDD-N  │
                    │ (Verifier role)  │
                    └────────┬─────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
    ┌─────────┐        ┌─────────┐        ┌─────────┐
    │ APPROVE │        │ REJECT  │        │ ITERATE │
    │→ CANON  │        │→ REVIEW │        │→ REVISE │
    └─────────┘        └─────────┘        └─────────┘
```

### Role Assignments (from coordination.yaml)
| Role | Platform | Rationale |
|------|----------|-----------|
| Oracle (sensing) | Gemini | 2M context, Drive connector, NotebookLM |
| Deviser (planning) | ChatGPT | GPT-5.2 Thinking, long-horizon decomposition |
| Executor (implementation) | Claude Code | Filesystem sovereignty, agentic execution |
| Auditor (verification) | ChatGPT | Verification against spec, drift analysis |

---

## 3. Routing Mechanism

### route_task.py Logic
```python
routing_table = {
    "corpus_sensing":    {"primary": "gemini"},
    "video_processing":  {"primary": "gemini"},
    "planning":          {"primary": "chatgpt"},
    "specification":     {"primary": "chatgpt"},
    "audit":             {"primary": "chatgpt"},
    "execution":         {"primary": "claude_code"},
    "code_generation":   {"primary": "claude_code"},
    "file_manipulation": {"primary": "claude_code"}
}
```

### Model Routing (from coordination.yaml)
```yaml
model_routing:
  default: sonnet-4.5
  by_task_type:
    oracle_synthesis: opus-4.5
    architectural_decisions: opus-4.5
    complex_integration: opus-4.5
    repository_maintenance: sonnet-4.5
    ledger_updates: sonnet-4.5
    content_processing: sonnet-4.5
    verification_tasks: sonnet-4.5

  thinking_defaults:
    oracle_synthesis: ultrathink
    architectural_decisions: megathink
    complex_integration: megathink
    repository_maintenance: think
    ledger_updates: default
    content_processing: think
    verification_tasks: default
```

---

## 4. Verification Expectations

### Pre-Commit Verification
```bash
make verify  # Runs all validation checks
```

### Verification Components
1. **Ledger Validation**: CSV integrity (proper escaping, row counts)
2. **State Consistency**: system_state.json valid JSON, session numbers match
3. **Event Log Integrity**: JSONL lines valid, no corruption
4. **Protected Zone Check**: No unauthorized modifications to 00-ORCHESTRATION/state/, 01-CANON/
5. **Flat Principle Check**: No subdirectories created in violation

### Verification in Audit Packets
```json
{
  "criteria_results": {
    "deliverable_present": true,
    "verification_passed": true,
    "no_drift": true
  },
  "drift_analysis": "No drift from plan",
  "recommendation": "APPROVE"
}
```

---

## 5. Ground Truth Assertion

### Where Ground Truth Lives
| Truth | Location | Authority |
|-------|----------|-----------|
| Task status | tasks.csv | Authoritative ledger |
| Session state | system_state.json | Current vector |
| Event history | events.jsonl | Immutable log |
| Platform capabilities | capabilities.json | Capability ledger |
| Canonical knowledge | 01-CANON/ | Protected, Principal-approved |
| Constitutional rules | CLAUDE.md | Absolute |

### Verification Over Claims
From CLAUDE.md:
```
| Verification | Claims-based |
Before: Claims in chat
After: Commands-based verification
```

The system never trusts claims without verification. "Done" means:
1. Artifact exists at expected location
2. Verification command passes
3. Ledger updated
4. Event logged

---

## 6. Communication Patterns

### Directive → Execution → Log
```
00-ORCHESTRATION/directives/DIRECTIVE-{number}{stream}.md
    ↓ (read by Claude Code)
00-ORCHESTRATION/execution_logs/EXECUTION_LOG-{date}-{directive}.md
    ↓ (updates)
00-ORCHESTRATION/state/{ledgers}
```

### Inter-Instance Coordination
From coordination.yaml:
```yaml
inter_instance:
  method: "git_branches"
  notes: "No direct communication; coordinate via shared repository"
```

Instances NEVER communicate directly. All coordination through:
1. Git branches and commits
2. Blackboard packets
3. Ledger updates
4. Event log

---

## 7. Ledger Protocol

### Atomic Update Pattern
```yaml
ledger_protocol:
  backup_before_write: true
  temp_file_pattern: "{name}.csv.tmp"
  backup_pattern: "{name}.csv.bak.{timestamp}"
  validation_required: true
  atomic_rename: true
```

### Update Sequence
1. Read current CSV
2. Create backup with timestamp
3. Write changes to .tmp file
4. Validate .tmp file
5. Atomic rename .tmp → .csv
6. Log event

---

## Summary

The operational spine ensures:
- **Traceability**: Every action logged in events.jsonl
- **Verifiability**: Verification commands prove state
- **Separation**: Roles cleanly map to platforms
- **Atomicity**: Ledger updates are transactional
- **Ground Truth**: Repository is the single source of truth
