#!/usr/bin/env python3
"""
Task Router for Syncrescendence IMEP
Routes tasks to optimal platform based on capability ledger and task type.
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> datetime:
    """Return current UTC time (timezone-aware)."""
    return datetime.now(timezone.utc)

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
        "timestamp": utc_now().isoformat() + "Z",
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
            "timestamp": utc_now().isoformat() + "Z"
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
    packet_id = f"EVD-{utc_now().strftime('%Y%m%d')}-{_next_sequence('evidence')}"

    packet = {
        "id": packet_id,
        "timestamp": utc_now().isoformat() + "Z",
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
