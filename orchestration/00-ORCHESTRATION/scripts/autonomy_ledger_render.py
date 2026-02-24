#!/usr/bin/env python3
"""Regenerate AUTONOMY_LEDGER.md from AUTONOMY_LEDGER.json.

Usage:
    python3 autonomy_ledger_render.py --agent commander
"""

import argparse
import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def main() -> None:
    parser = argparse.ArgumentParser(description="Render autonomy ledger .md from .json")
    parser.add_argument("--agent", required=True, help="Agent name")
    args = parser.parse_args()

    json_path = os.path.join(REPO_ROOT, "agents", args.agent, "AUTONOMY_LEDGER.json")
    md_path = os.path.join(REPO_ROOT, "agents", args.agent, "AUTONOMY_LEDGER.md")

    if not os.path.exists(json_path):
        print(f"ERROR: No ledger at {json_path}", file=sys.stderr)
        sys.exit(1)

    with open(json_path, "r") as f:
        ledger = json.load(f)

    agent_title = args.agent.capitalize()
    overall = ledger["autonomy_levels"]["overall"]
    level_def = ledger["level_definitions"].get(overall, {})
    label = level_def.get("label", "Unknown")
    mode = ledger["recovery_protocol"]["mode"]
    state = ledger["recovery_protocol"]["state"]
    since = ledger["recovery_protocol"]["sandbox_start_date"]

    # Gate status rows
    g1 = ledger["gates"]["gate1_execution_accuracy"]["current"]
    g1_status = ledger["gates"]["gate1_execution_accuracy"]["status"]
    g1_progress = f"{g1['passed']}/{g1.get('total', 200)} ({g1['accuracy']:.1%})"

    g2 = ledger["gates"]["gate2_scope_probe"]["current"]
    g2_status = ledger["gates"]["gate2_scope_probe"]["status"]
    g2_total = g2.get("total", 0)
    g2_progress = f"{g2['passed']}/{g2_total} ({g2['rate']:.1%})" if g2_total > 0 else "0/0 (0.0%)"

    g3 = ledger["gates"]["gate3_consecutive_sessions"]["current"]
    g3_status = ledger["gates"]["gate3_consecutive_sessions"]["status"]
    g3_progress = f"{g3['sessions']}/14"

    # Level definitions
    level_rows = []
    for lvl in ["L1", "L2", "L3", "L4"]:
        d = ledger["level_definitions"].get(lvl, {})
        level_rows.append(f"| {lvl} | {d.get('label', '')} | {d.get('allowed', '')} |")

    # History
    history_lines = []
    for entry in ledger["history"]:
        ts = entry["ts"]
        event = entry["event"]
        parts = [f"- {ts}: {event}"]
        if "reason" in entry:
            parts.append(f" — {entry['reason']}")
        elif "detail" in entry:
            parts.append(f" — {entry['detail']}")
        elif "task_id" in entry:
            outcome = entry.get("outcome", "")
            parts.append(f" — {entry['task_id']} = {outcome}")
        if "authority" in entry:
            parts.append(f" ({entry['authority']})")
        history_lines.append("".join(parts))

    md = f"""# {agent_title} Autonomy Ledger

**Current Level**: {overall} — {label}
**Mode**: {mode} ({state})
**Since**: {since}

## Gate Status
| Gate | Threshold | Status | Progress |
|------|-----------|--------|----------|
| Execution Accuracy | >99% on 200 tasks | {g1_status} | {g1_progress} |
| Scope Probe | >98% suite pass | {g2_status} | {g2_progress} |
| Consecutive Sessions | 14 sessions, 0 violations | {g3_status} | {g3_progress} |

## Level Definitions
| Level | Label | Allowed |
|-------|-------|---------|
{chr(10).join(level_rows)}

## History
{chr(10).join(history_lines)}
"""

    with open(md_path, "w") as f:
        f.write(md)

    print(f"Rendered: {md_path}")


if __name__ == "__main__":
    main()
