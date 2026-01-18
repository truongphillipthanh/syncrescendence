# Replay Procedure v1
**Generated**: 2026-01-17T04:50:00Z
**Purpose**: Reconstruct system state from event log for audit, recovery, or verification

---

## Purpose

The event log (`events.jsonl`) is an append-only history of system actions. This procedure uses that log to:

1. **Audit**: Verify that state reflects actual events
2. **Recover**: Reconstruct state after corruption
3. **Debug**: Understand how state reached current condition
4. **Verify**: Confirm no events were lost or altered

---

## Prerequisites

- `00-ORCHESTRATION/state/events.jsonl` exists and is intact
- Access to `system_state.json` for comparison
- Python 3.x with json library (standard)

---

## Manual Replay Procedure

### Step 1: Inspect Event Log

```bash
# Count total events
wc -l 00-ORCHESTRATION/state/events.jsonl

# View event distribution
jq -r '.event' 00-ORCHESTRATION/state/events.jsonl | sort | uniq -c | sort -rn

# View last 20 events
tail -20 00-ORCHESTRATION/state/events.jsonl | jq '.'

# View events from specific date
grep '2026-01-16' 00-ORCHESTRATION/state/events.jsonl | jq '.'
```

### Step 2: Initialize Simulated State

```python
# Starting state (before any events)
simulated_state = {
    "session_numbers": {"oracle": 0, "blitzkrieg": 0},
    "metrics": {
        "autonomous_cycles": 0,
        "relay_cycles": 0,
        "packets_created": 0,
        "sources_processed": 0
    },
    "platform_status": {}
}
```

### Step 3: Replay Events

For each event in chronological order, update simulated state:

| Event Type | State Update |
|------------|--------------|
| `session_started` | Set platform_status to active |
| `session_ended` | Set platform_status to idle |
| `packet_created` | Increment packets_created |
| `execution_completed` | Increment autonomous_cycles |
| `source_processed` | Increment sources_processed |
| `state_updated` | Apply explicit state changes |
| `relay_required` | Increment relay_cycles |

### Step 4: Compare States

```bash
# Extract key metrics from current state
jq '.metrics' 00-ORCHESTRATION/state/system_state.json

# Compare with simulated state
# Discrepancies indicate either:
# - Events missing from log
# - State updated without logging
# - Manual state modification
```

---

## Automated Replay Script

Save as `scripts/replay_events.py`:

```python
#!/usr/bin/env python3
"""
Replay events.jsonl to reconstruct and verify system state.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def load_events(events_file: Path) -> list:
    """Load all events from JSONL file."""
    events = []
    with open(events_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                events.append(json.loads(line))
    return events

def replay_events(events: list) -> dict:
    """Replay events to reconstruct state."""
    state = {
        "session_numbers": {"oracle": 0, "blitzkrieg": 0},
        "metrics": {
            "autonomous_cycles": 0,
            "relay_cycles": 0,
            "packets_created": 0,
            "sources_processed": 0,
            "canon_integrations": 0
        },
        "platform_status": {},
        "last_event": None
    }

    for event in events:
        event_type = event.get("event", "")
        data = event.get("data", {})
        timestamp = event.get("timestamp", "")
        actor = event.get("actor", "")

        # Update based on event type
        if event_type == "session_started":
            state["platform_status"][actor] = "active"
            if "oracle" in data:
                state["session_numbers"]["oracle"] = max(
                    state["session_numbers"]["oracle"],
                    data["oracle"]
                )
            if "blitzkrieg" in data:
                state["session_numbers"]["blitzkrieg"] = max(
                    state["session_numbers"]["blitzkrieg"],
                    data["blitzkrieg"]
                )

        elif event_type == "session_ended":
            state["platform_status"][actor] = "idle"

        elif event_type == "packet_created":
            state["metrics"]["packets_created"] += 1

        elif event_type == "execution_completed":
            state["metrics"]["autonomous_cycles"] += 1

        elif event_type == "relay_required":
            state["metrics"]["relay_cycles"] += 1

        elif event_type == "source_processed":
            state["metrics"]["sources_processed"] += 1

        elif event_type == "canon_integrated":
            state["metrics"]["canon_integrations"] += 1

        elif event_type == "state_updated":
            # Apply explicit state changes
            if "metrics" in data:
                for k, v in data["metrics"].items():
                    if k in state["metrics"]:
                        state["metrics"][k] = v

        state["last_event"] = timestamp

    return state

def load_current_state(state_file: Path) -> dict:
    """Load current system state."""
    with open(state_file, 'r') as f:
        return json.load(f)

def compare_states(replayed: dict, current: dict) -> list:
    """Compare replayed state with current state, return discrepancies."""
    discrepancies = []

    # Compare metrics
    replayed_metrics = replayed.get("metrics", {})
    current_metrics = current.get("metrics", {})

    for key in set(replayed_metrics.keys()) | set(current_metrics.keys()):
        r_val = replayed_metrics.get(key, 0)
        c_val = current_metrics.get(key, 0)
        if r_val != c_val:
            discrepancies.append({
                "field": f"metrics.{key}",
                "replayed": r_val,
                "current": c_val,
                "delta": c_val - r_val
            })

    # Compare session numbers
    replayed_sessions = replayed.get("session_numbers", {})
    current_sessions = current.get("session_numbers", {})

    for key in ["oracle", "blitzkrieg"]:
        r_val = replayed_sessions.get(key, 0)
        c_val = current_sessions.get(key, 0)
        if r_val != c_val:
            discrepancies.append({
                "field": f"session_numbers.{key}",
                "replayed": r_val,
                "current": c_val,
                "delta": c_val - r_val
            })

    return discrepancies

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Replay events to verify state")
    parser.add_argument("--events", default="00-ORCHESTRATION/state/events.jsonl")
    parser.add_argument("--state", default="00-ORCHESTRATION/state/system_state.json")
    parser.add_argument("--verify", action="store_true", help="Compare with current state")
    parser.add_argument("--output", help="Write replayed state to file")
    args = parser.parse_args()

    events_file = Path(args.events)
    state_file = Path(args.state)

    if not events_file.exists():
        print(f"Error: Events file not found: {events_file}")
        sys.exit(1)

    # Load and replay events
    events = load_events(events_file)
    print(f"Loaded {len(events)} events")

    replayed_state = replay_events(events)
    print(f"Replayed state: {json.dumps(replayed_state, indent=2)}")

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(replayed_state, f, indent=2)
        print(f"Written to {args.output}")

    if args.verify:
        if not state_file.exists():
            print(f"Error: State file not found: {state_file}")
            sys.exit(1)

        current_state = load_current_state(state_file)
        discrepancies = compare_states(replayed_state, current_state)

        if discrepancies:
            print("\n⚠️  DISCREPANCIES FOUND:")
            for d in discrepancies:
                print(f"  {d['field']}: replayed={d['replayed']}, current={d['current']} (delta={d['delta']})")
            sys.exit(1)
        else:
            print("\n✓ State verification passed: replayed state matches current state")
            sys.exit(0)

if __name__ == "__main__":
    main()
```

---

## Usage Examples

### Verify Current State

```bash
python3 scripts/replay_events.py --verify
```

Expected output (success):
```
Loaded 127 events
Replayed state: {...}
✓ State verification passed: replayed state matches current state
```

Expected output (discrepancy):
```
Loaded 127 events
Replayed state: {...}
⚠️  DISCREPANCIES FOUND:
  metrics.autonomous_cycles: replayed=5, current=7 (delta=2)
```

### Generate Replayed State

```bash
python3 scripts/replay_events.py --output replayed_state.json
```

### Recovery from Corruption

```bash
# 1. Generate replayed state
python3 scripts/replay_events.py --output recovered_state.json

# 2. Review differences
diff <(jq '.' recovered_state.json) <(jq '.' system_state.json)

# 3. If replayed state is correct, replace current state
cp recovered_state.json 00-ORCHESTRATION/state/system_state.json

# 4. Log the correction
echo '{"timestamp":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","event":"state_corrected","actor":"principal","data":{"reason":"replay recovery"}}' >> 00-ORCHESTRATION/state/events.jsonl
```

---

## Audit Scenarios

### Scenario 1: Missing Events

**Symptom**: Replayed state shows fewer cycles than current state

**Diagnosis**: Events were not logged during some operations

**Prevention**: Enforce event logging in session lifecycle protocol

### Scenario 2: Direct State Modification

**Symptom**: Current state differs from replayed state with no corresponding events

**Diagnosis**: State was modified without logging

**Prevention**: All state changes must be logged as `state_updated` events

### Scenario 3: Truncated Event Log

**Symptom**: Event log has fewer entries than expected

**Diagnosis**: Log may have been truncated or rotated

**Prevention**: Archive event logs before rotation, maintain checksums

---

## Integration Points

### Pre-Commit Hook

```bash
#!/bin/bash
# Verify state coherence before commit
python3 scripts/replay_events.py --verify || {
    echo "State verification failed. Run replay manually to diagnose."
    exit 1
}
```

### Session Culmination

Add to session lifecycle:
```bash
# Before committing, verify state coherence
python3 scripts/replay_events.py --verify
```

### Weekly Audit

```bash
# Generate replay report
python3 scripts/replay_events.py --verify --output audit_$(date +%Y%m%d).json
```

---

## Event Schema Reference

All events follow this structure:

```json
{
  "timestamp": "ISO8601 timestamp",
  "event": "event_type",
  "actor": "platform_or_principal",
  "data": {}
}
```

Standard event types:
- `session_started`
- `session_ended`
- `packet_created`
- `execution_completed`
- `relay_required`
- `source_processed`
- `canon_integrated`
- `state_updated`
- `error_occurred`
- `state_corrected`
