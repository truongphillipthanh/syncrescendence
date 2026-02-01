# DIRECTIVE-046A: OPERATIONAL PRIMITIVES + FIRST AUTONOMOUS CYCLE

**Stream**: A
**Model**: Opus 4.5
**Thinking**: megathink
**Estimated Duration**: 2-3 hours
**Target**: Claude Code Instance (Account 2 or 3)

---

## PREAMBLE

You are executing the most critical directive in the Oracle arc. Twelve sessions have established infrastructure; this session must prove the infrastructure can operate autonomously.

**Read ORACLE13_CONTEXT.md first.** It contains the convergent findings from three frontier models that inform this directive.

**Success criterion**: ONE COMPLETE AUTONOMOUS CYCLE with zero Sovereign relay.

---

## PHASE 1: OPERATIONAL PRIMITIVES IMPLEMENTATION

### 1.1 Directory Structure Creation

Create the control plane structure. This is the ONLY structural change permitted.

```bash
# Verify current state first
cd /path/to/syncrescendence
git status
ls -la 00-ORCHESTRATION/

# Create control plane directories (flat, no subdirectories within)
mkdir -p 00-ORCHESTRATION/state
mkdir -p 00-ORCHESTRATION/blackboard/evidence
mkdir -p 00-ORCHESTRATION/blackboard/plans
mkdir -p 00-ORCHESTRATION/blackboard/executions
mkdir -p 00-ORCHESTRATION/blackboard/audits
mkdir -p 00-ORCHESTRATION/blackboard/capabilities
mkdir -p 00-ORCHESTRATION/schemas
mkdir -p 00-ORCHESTRATION/scripts
```

**NOTE**: The blackboard subdirectories are FUNCTIONAL CATEGORIES, not hierarchical taxonomy. They remain flat within each category.

### 1.2 State Vector Implementation

Create `/00-ORCHESTRATION/state/system_state.json`:

```json
{
  "schema_version": "1.0.0",
  "timestamp": "2026-01-15T00:00:00Z",
  "session": {
    "oracle": 13,
    "blitzkrieg": 46,
    "stream": "A"
  },
  "active_tasks": [],
  "platform_status": {
    "claude_code_1": { "status": "available", "last_active": null },
    "claude_code_2": { "status": "executing", "last_active": "2026-01-15T00:00:00Z" },
    "claude_code_3": { "status": "available", "last_active": null },
    "gemini": { "status": "pending_onboard", "last_active": null },
    "chatgpt": { "status": "pending_onboard", "last_active": null }
  },
  "metrics": {
    "autonomous_cycles": 0,
    "relay_cycles": 0,
    "relay_reduction_ratio": 0.0,
    "packets_created": 0,
    "packets_processed": 0
  },
  "last_state_hash": null
}
```

**Update this file** with actual timestamp when creating.

### 1.3 Event Log Implementation

Create `/00-ORCHESTRATION/state/events.jsonl`:

```jsonl
{"timestamp":"2026-01-15T00:00:00Z","event":"system_init","actor":"directive-046a","type":"lifecycle","status":"started","details":{"oracle":13,"blitzkrieg":46}}
```

**Append to this file** for every meaningful action. Never overwrite. Append-only.

Event types:
- `lifecycle`: System start/stop/checkpoint
- `packet`: Packet created/processed/rejected
- `routing`: Task assignment decisions
- `state`: State vector updates
- `error`: Failures and recovery actions

### 1.4 Capability Ledger Implementation

Create `/00-ORCHESTRATION/state/capabilities.json`:

```json
{
  "schema_version": "1.0.0",
  "last_updated": "2026-01-15T00:00:00Z",
  "platforms": {
    "gemini": {
      "tier": "advanced",
      "monthly_cost": 20,
      "capabilities": {
        "context_window": "2M tokens",
        "multimodal": ["text", "image", "video", "audio"],
        "native_video_processing": true,
        "drive_connector": true,
        "notebooklm_integration": true
      },
      "routing_strength": ["corpus_sensing", "video_transcription", "large_context", "grounded_rag"],
      "routing_weakness": ["filesystem_access", "code_execution"],
      "rate_limits": {
        "requests_per_minute": "unknown",
        "tokens_per_minute": "unknown"
      },
      "status": "pending_validation"
    },
    "chatgpt": {
      "tier": "plus",
      "monthly_cost": 20,
      "capabilities": {
        "models": ["gpt-5.2-instant", "gpt-5.2-thinking"],
        "deep_research": true,
        "canvas": true,
        "agent_mode": true,
        "codex_cli": true
      },
      "routing_strength": ["long_horizon_planning", "specification", "audit", "abstract_reasoning"],
      "routing_weakness": ["corpus_scale", "video_native"],
      "rate_limits": {
        "gpt52_instant": "~160/3hr",
        "gpt52_thinking": "~3K/week"
      },
      "status": "pending_validation"
    },
    "claude_code": {
      "tier": "pro",
      "monthly_cost": 60,
      "accounts": 3,
      "capabilities": {
        "models": ["opus-4.5", "sonnet-4.5"],
        "filesystem_access": true,
        "bash_execution": true,
        "mcp_integration": true,
        "plan_mode": true
      },
      "routing_strength": ["execution", "code_generation", "file_manipulation", "verification"],
      "routing_weakness": ["corpus_scale_rag", "video_native"],
      "rate_limits": {
        "context_window": "200K effective",
        "auto_compact_threshold": "95%"
      },
      "status": "active"
    }
  }
}
```

### 1.5 Packet Protocol Schema

Create `/00-ORCHESTRATION/schemas/packet_protocol.json`:

```json
{
  "schema_version": "1.0.0",
  "packet_types": {
    "evidence": {
      "description": "Oracle outputs - findings from corpus sensing",
      "required_fields": ["id", "timestamp", "actor", "query", "corpus_slice", "findings", "uncertainties"],
      "optional_fields": ["recommended_probe", "citations", "confidence"],
      "example": {
        "id": "EVD-20260115-001",
        "timestamp": "2026-01-15T00:00:00Z",
        "actor": "gemini",
        "query": "What new videos appeared on monitored channels?",
        "corpus_slice": ["youtube_subscriptions", "last_24h"],
        "findings": ["New video from [creator]: [title]"],
        "uncertainties": ["Signal tier not yet assessed"],
        "recommended_probe": "Assess signal tier via transcript preview"
      }
    },
    "plan": {
      "description": "Deviser outputs - specifications for execution",
      "required_fields": ["id", "timestamp", "actor", "evidence_ids", "objective", "deliverables", "acceptance_criteria", "stop_conditions"],
      "optional_fields": ["estimated_duration", "resource_requirements", "dependencies"],
      "example": {
        "id": "PLN-20260115-001",
        "timestamp": "2026-01-15T00:00:00Z",
        "actor": "chatgpt",
        "evidence_ids": ["EVD-20260115-001"],
        "objective": "Transcribe and qualify new video",
        "deliverables": ["SOURCE-[date]-[creator].md"],
        "acceptance_criteria": ["Transcript complete", "Frontmatter valid", "Signal tier assigned"],
        "stop_conditions": ["Video >4hr without Sovereign approval", "API error rate >5%"]
      }
    },
    "execution": {
      "description": "Executor outputs - completed work records",
      "required_fields": ["id", "timestamp", "actor", "plan_id", "commands_run", "files_changed", "verification_output"],
      "optional_fields": ["duration", "errors_encountered", "rollback_notes"],
      "example": {
        "id": "EXE-20260115-001",
        "timestamp": "2026-01-15T00:00:00Z",
        "actor": "claude_code_2",
        "plan_id": "PLN-20260115-001",
        "commands_run": ["transcribe_youtube.py [url]", "validate_frontmatter.sh"],
        "files_changed": ["04-SOURCES/processed/SOURCE-20260115-creator.md"],
        "verification_output": "Frontmatter valid. Signal tier: STRATEGIC."
      }
    },
    "audit": {
      "description": "Verification outputs - quality assessment",
      "required_fields": ["id", "timestamp", "actor", "execution_id", "plan_id", "criteria_results", "drift_analysis", "recommendation"],
      "optional_fields": ["state_transition_justified", "canon_integration_recommended"],
      "example": {
        "id": "AUD-20260115-001",
        "timestamp": "2026-01-15T00:00:00Z",
        "actor": "chatgpt",
        "execution_id": "EXE-20260115-001",
        "plan_id": "PLN-20260115-001",
        "criteria_results": {"transcript_complete": true, "frontmatter_valid": true, "signal_tier_assigned": true},
        "drift_analysis": "No drift from plan",
        "recommendation": "APPROVE - ready for integration"
      }
    },
    "capability_event": {
      "description": "Platform self-reports on capability changes",
      "required_fields": ["id", "timestamp", "platform", "event_type", "details"],
      "optional_fields": ["routing_impact", "action_required"],
      "example": {
        "id": "CAP-20260115-001",
        "timestamp": "2026-01-15T00:00:00Z",
        "platform": "gemini",
        "event_type": "rate_limit_hit",
        "details": "Video processing quota exhausted for day",
        "routing_impact": "Route video tasks to alternative or queue",
        "action_required": false
      }
    }
  },
  "naming_conventions": {
    "evidence": "EVD-YYYYMMDD-NNN",
    "plan": "PLN-YYYYMMDD-NNN",
    "execution": "EXE-YYYYMMDD-NNN",
    "audit": "AUD-YYYYMMDD-NNN",
    "capability": "CAP-YYYYMMDD-NNN"
  },
  "file_format": "JSON with .json extension",
  "location": "/00-ORCHESTRATION/blackboard/{packet_type}/"
}
```

### 1.6 Router Implementation

Create `/00-ORCHESTRATION/scripts/route_task.py`:

```python
#!/usr/bin/env python3
"""
Task Router for Syncrescendence IMEP
Routes tasks to optimal platform based on capability ledger and task type.
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Configuration
ORCHESTRATION_ROOT = Path(__file__).parent.parent
STATE_DIR = ORCHESTRATION_ROOT / "state"
BLACKBOARD_DIR = ORCHESTRATION_ROOT / "blackboard"

def load_capabilities():
    """Load current capability ledger."""
    cap_file = STATE_DIR / "capabilities.json"
    with open(cap_file) as f:
        return json.load(f)

def load_state():
    """Load current system state."""
    state_file = STATE_DIR / "system_state.json"
    with open(state_file) as f:
        return json.load(f)

def log_event(event_type: str, details: dict):
    """Append event to event log."""
    event = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": "routing_decision",
        "type": event_type,
        **details
    }
    events_file = STATE_DIR / "events.jsonl"
    with open(events_file, "a") as f:
        f.write(json.dumps(event) + "\n")

def route_task(task_type: str, task_details: dict) -> dict:
    """
    Route a task to the optimal platform.
    
    Args:
        task_type: One of corpus_sensing, planning, execution, audit, video_processing
        task_details: Task-specific information
        
    Returns:
        Routing decision with platform assignment and rationale
    """
    capabilities = load_capabilities()
    state = load_state()
    
    # Routing rules based on convergent model analysis
    routing_table = {
        "corpus_sensing": {
            "primary": "gemini",
            "rationale": "2M context window, Drive connector, NotebookLM integration"
        },
        "video_processing": {
            "primary": "gemini",
            "rationale": "Native multimodal, 263 tok/sec video processing"
        },
        "planning": {
            "primary": "chatgpt",
            "rationale": "GPT-5.2 Thinking excels at long-horizon decomposition"
        },
        "specification": {
            "primary": "chatgpt",
            "rationale": "Abstract reasoning for acceptance criteria definition"
        },
        "audit": {
            "primary": "chatgpt",
            "rationale": "Verification against spec, drift analysis"
        },
        "execution": {
            "primary": "claude_code",
            "rationale": "Filesystem sovereignty, agentic implementation"
        },
        "code_generation": {
            "primary": "claude_code",
            "rationale": "Production code, repo-native execution"
        },
        "file_manipulation": {
            "primary": "claude_code",
            "rationale": "Direct filesystem access, atomic operations"
        }
    }
    
    if task_type not in routing_table:
        decision = {
            "status": "error",
            "message": f"Unknown task type: {task_type}",
            "available_types": list(routing_table.keys())
        }
    else:
        route = routing_table[task_type]
        platform = route["primary"]
        platform_status = state["platform_status"].get(platform, {}).get("status", "unknown")
        
        decision = {
            "status": "routed",
            "task_type": task_type,
            "assigned_platform": platform,
            "rationale": route["rationale"],
            "platform_status": platform_status,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        
        # Check if platform is available
        if platform_status not in ["available", "active", "executing"]:
            decision["warning"] = f"Platform {platform} status is {platform_status}"
    
    # Log the routing decision
    log_event("routing", {
        "task_type": task_type,
        "decision": decision
    })
    
    return decision

def create_evidence_packet(query: str, findings: list, actor: str = "system") -> str:
    """Create and save an Evidence packet."""
    packet_id = f"EVD-{datetime.utcnow().strftime('%Y%m%d')}-{_next_sequence('evidence')}"
    
    packet = {
        "id": packet_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "actor": actor,
        "query": query,
        "corpus_slice": [],
        "findings": findings,
        "uncertainties": []
    }
    
    packet_path = BLACKBOARD_DIR / "evidence" / f"{packet_id}.json"
    with open(packet_path, "w") as f:
        json.dump(packet, f, indent=2)
    
    log_event("packet_created", {"packet_id": packet_id, "type": "evidence"})
    
    return packet_id

def _next_sequence(packet_type: str) -> str:
    """Get next sequence number for packet type."""
    packet_dir = BLACKBOARD_DIR / packet_type
    existing = list(packet_dir.glob("*.json"))
    return f"{len(existing) + 1:03d}"

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: route_task.py <task_type> [task_details_json]")
        print(f"Available task types: corpus_sensing, video_processing, planning, specification, audit, execution, code_generation, file_manipulation")
        sys.exit(1)
    
    task_type = sys.argv[1]
    task_details = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    
    result = route_task(task_type, task_details)
    print(json.dumps(result, indent=2))
```

Make executable:
```bash
chmod +x /00-ORCHESTRATION/scripts/route_task.py
```

---

## PHASE 2: FIRST AUTONOMOUS CYCLE

### 2.1 Test the Primitives

Before attempting full cycle, verify each primitive works:

```bash
# Test 1: State vector readable
cat 00-ORCHESTRATION/state/system_state.json | python3 -m json.tool

# Test 2: Event log appendable
echo '{"timestamp":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","event":"test","actor":"directive-046a","type":"test","status":"passed"}' >> 00-ORCHESTRATION/state/events.jsonl
tail -1 00-ORCHESTRATION/state/events.jsonl | python3 -m json.tool

# Test 3: Router functional
python3 00-ORCHESTRATION/scripts/route_task.py execution
python3 00-ORCHESTRATION/scripts/route_task.py corpus_sensing
python3 00-ORCHESTRATION/scripts/route_task.py planning

# Test 4: Packet schema loadable
cat 00-ORCHESTRATION/schemas/packet_protocol.json | python3 -m json.tool

# Test 5: Blackboard directories exist
ls -la 00-ORCHESTRATION/blackboard/
```

### 2.2 Simulate Complete Cycle

Execute one complete IMEP cycle manually to prove the pattern:

**Step 1: Create Evidence Packet (simulating Oracle)**

```bash
# Create evidence packet
cat > 00-ORCHESTRATION/blackboard/evidence/EVD-20260115-001.json << 'EOF'
{
  "id": "EVD-20260115-001",
  "timestamp": "2026-01-15T20:00:00Z",
  "actor": "directive-046a-simulation",
  "query": "Verify operational primitives implementation complete",
  "corpus_slice": ["00-ORCHESTRATION/state/", "00-ORCHESTRATION/blackboard/", "00-ORCHESTRATION/scripts/"],
  "findings": [
    "system_state.json created and valid",
    "events.jsonl created and appendable",
    "capabilities.json created with platform data",
    "packet_protocol.json schema defined",
    "route_task.py functional"
  ],
  "uncertainties": [
    "Cross-platform coordination not yet tested",
    "Real packet flow not yet validated"
  ],
  "recommended_probe": "Execute full cycle with real task"
}
EOF
```

**Step 2: Create Plan Packet (simulating Deviser)**

```bash
cat > 00-ORCHESTRATION/blackboard/plans/PLN-20260115-001.json << 'EOF'
{
  "id": "PLN-20260115-001",
  "timestamp": "2026-01-15T20:05:00Z",
  "actor": "directive-046a-simulation",
  "evidence_ids": ["EVD-20260115-001"],
  "objective": "Validate operational primitives by completing state update cycle",
  "deliverables": [
    "Updated system_state.json with autonomous_cycles = 1",
    "Event log entries for full cycle",
    "Execution packet documenting actions"
  ],
  "acceptance_criteria": [
    "State vector timestamp updated",
    "metrics.autonomous_cycles incremented",
    "Event log contains entries for: evidence, plan, execution, audit",
    "No Sovereign relay required"
  ],
  "stop_conditions": [
    "Any primitive fails validation",
    "JSON parsing errors",
    "File permission errors"
  ]
}
EOF
```

**Step 3: Execute (this is you, the Executor)**

```bash
# Update state vector
python3 << 'EOF'
import json
from datetime import datetime

state_file = "00-ORCHESTRATION/state/system_state.json"
with open(state_file) as f:
    state = json.load(f)

state["timestamp"] = datetime.utcnow().isoformat() + "Z"
state["metrics"]["autonomous_cycles"] = 1
state["metrics"]["packets_created"] = 4
state["metrics"]["packets_processed"] = 4

with open(state_file, "w") as f:
    json.dump(state, f, indent=2)

print("State updated successfully")
EOF

# Log the execution
echo '{"timestamp":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","event":"execution_complete","actor":"claude_code","type":"execution","plan_id":"PLN-20260115-001","status":"success"}' >> 00-ORCHESTRATION/state/events.jsonl
```

**Step 4: Create Execution Packet**

```bash
cat > 00-ORCHESTRATION/blackboard/executions/EXE-20260115-001.json << 'EOF'
{
  "id": "EXE-20260115-001",
  "timestamp": "2026-01-15T20:10:00Z",
  "actor": "claude_code_2",
  "plan_id": "PLN-20260115-001",
  "commands_run": [
    "python3 state_update_script",
    "echo event >> events.jsonl"
  ],
  "files_changed": [
    "00-ORCHESTRATION/state/system_state.json"
  ],
  "verification_output": "State vector updated. autonomous_cycles = 1. packets_created = 4."
}
EOF
```

**Step 5: Create Audit Packet (simulating Deviser verification)**

```bash
cat > 00-ORCHESTRATION/blackboard/audits/AUD-20260115-001.json << 'EOF'
{
  "id": "AUD-20260115-001",
  "timestamp": "2026-01-15T20:15:00Z",
  "actor": "directive-046a-simulation",
  "execution_id": "EXE-20260115-001",
  "plan_id": "PLN-20260115-001",
  "criteria_results": {
    "state_vector_timestamp_updated": true,
    "autonomous_cycles_incremented": true,
    "event_log_entries_present": true,
    "no_sovereign_relay": true
  },
  "drift_analysis": "No drift from plan. All acceptance criteria met.",
  "recommendation": "APPROVE - First autonomous cycle complete"
}
EOF
```

### 2.3 Verify Complete Cycle

```bash
# Verify all packets exist
echo "=== EVIDENCE PACKETS ==="
ls -la 00-ORCHESTRATION/blackboard/evidence/
cat 00-ORCHESTRATION/blackboard/evidence/EVD-20260115-001.json | python3 -m json.tool | head -20

echo "=== PLAN PACKETS ==="
ls -la 00-ORCHESTRATION/blackboard/plans/
cat 00-ORCHESTRATION/blackboard/plans/PLN-20260115-001.json | python3 -m json.tool | head -20

echo "=== EXECUTION PACKETS ==="
ls -la 00-ORCHESTRATION/blackboard/executions/

echo "=== AUDIT PACKETS ==="
ls -la 00-ORCHESTRATION/blackboard/audits/

echo "=== STATE VECTOR ==="
cat 00-ORCHESTRATION/state/system_state.json | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'autonomous_cycles: {d[\"metrics\"][\"autonomous_cycles\"]}')"

echo "=== EVENT LOG (last 5) ==="
tail -5 00-ORCHESTRATION/state/events.jsonl
```

---

## PHASE 3: COMMIT AND DOCUMENT

### 3.1 Commit Primitives

```bash
git add 00-ORCHESTRATION/state/
git add 00-ORCHESTRATION/blackboard/
git add 00-ORCHESTRATION/schemas/
git add 00-ORCHESTRATION/scripts/
git commit -m "feat(orchestration): implement operational primitives for IMEP

- Add system_state.json (present tense state vector)
- Add events.jsonl (append-only event log)
- Add capabilities.json (platform capability ledger)
- Add packet_protocol.json (IMEP schema definitions)
- Add route_task.py (task routing by teleology)
- Create blackboard directory structure for packet flow
- Execute first simulated autonomous cycle

Oracle 13 / DIRECTIVE-046A / Stream A"
```

### 3.2 Create Execution Log

Create `/00-ORCHESTRATION/EXECUTION_LOG-2026-01-15-046A.md`:

```markdown
# EXECUTION LOG: DIRECTIVE-046A
## Operational Primitives + First Autonomous Cycle

**Date**: 2026-01-15
**Stream**: A
**Model**: Opus 4.5
**Directive**: 046A

---

## Deliverables

### Phase 1: Operational Primitives

| Primitive | File | Status |
|-----------|------|--------|
| State Vector | `state/system_state.json` | ✓ Created |
| Event Log | `state/events.jsonl` | ✓ Created |
| Capability Ledger | `state/capabilities.json` | ✓ Created |
| Packet Schema | `schemas/packet_protocol.json` | ✓ Created |
| Router | `scripts/route_task.py` | ✓ Created |

### Phase 2: First Autonomous Cycle

| Step | Packet | Status |
|------|--------|--------|
| Evidence | EVD-20260115-001 | ✓ Created |
| Plan | PLN-20260115-001 | ✓ Created |
| Execution | EXE-20260115-001 | ✓ Created |
| Audit | AUD-20260115-001 | ✓ Created |
| State Update | system_state.json | ✓ Updated |

### Metrics

- Autonomous cycles completed: 1
- Sovereign relays required: 0
- Packets created: 4
- Packets processed: 4

---

## Verification Commands Run

```bash
# [paste actual verification output here]
```

---

## Notes

[Add any observations, issues encountered, or recommendations]

---

**End of Execution Log**
```

---

## SUCCESS CRITERIA CHECKLIST

Before declaring this directive complete, verify:

- [ ] `00-ORCHESTRATION/state/system_state.json` exists and is valid JSON
- [ ] `00-ORCHESTRATION/state/events.jsonl` exists with multiple entries
- [ ] `00-ORCHESTRATION/state/capabilities.json` exists with platform data
- [ ] `00-ORCHESTRATION/schemas/packet_protocol.json` defines all packet types
- [ ] `00-ORCHESTRATION/scripts/route_task.py` executes without error
- [ ] Blackboard directories exist: evidence/, plans/, executions/, audits/, capabilities/
- [ ] At least one packet exists in each blackboard directory
- [ ] State vector shows `autonomous_cycles >= 1`
- [ ] All changes committed with semantic commit message
- [ ] Execution log created documenting work

---

## HANDOFF TO STREAM B

When this directive completes, Stream B (DIRECTIVE-046B) will:
1. Use the operational primitives you created
2. Complete the IIC configurations
3. Onboard ChatGPT and Gemini using IMEP
4. Prove metabolic pattern with template rendering

Your work enables theirs. Verify thoroughly.

---

**End of DIRECTIVE-046A**
