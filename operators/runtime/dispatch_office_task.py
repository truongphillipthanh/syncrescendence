#!/usr/bin/env python3
"""Create a TASK envelope directly in an office inbox/pending lane."""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def safe_slug(text: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in text.strip())
    cleaned = "-".join(part for part in cleaned.split("-") if part)
    return cleaned or "dispatch"


def load_payload(args: argparse.Namespace) -> str:
    if args.payload_file:
        return Path(args.payload_file).read_text(encoding="utf-8").strip()
    if args.payload:
        return args.payload.strip()
    return ""


def build_task_markdown(args: argparse.Namespace, line_id: str, payload: str) -> str:
    return (
        "# TASK\n\n"
        "**Kind**: TASK\n"
        f"**Line-ID**: {line_id}\n"
        f"**From**: {args.sender}\n"
        f"**To**: {args.office}\n"
        f"**Reply-To**: {args.reply_to}\n"
        "**CC**: \n"
        f"**Issued-At**: {now_utc()}\n"
        f"**Priority**: {args.priority}\n"
        f"**Decision-Envelope**: {args.decision_envelope}\n"
        f"**Objective-Lock**: {args.objective_lock}\n"
        f"**Expected-Output**: {args.expected_output}\n"
        "**Receipts-Required**: Yes\n"
        f"**Completion-Condition**: {args.completion_condition}\n"
        f"**Escalation-Path**: {args.escalation_path}\n\n"
        "## Payload\n\n"
        f"{payload}\n"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--office", required=True, help="Office slug, e.g. psyche")
    parser.add_argument("--repo-root", default=None, help="Repo root (defaults to cwd)")
    parser.add_argument("--title", required=True, help="Task title used in filename")
    parser.add_argument("--line-id", default=None, help="Optional explicit line id")
    parser.add_argument("--sender", default="commander")
    parser.add_argument("--reply-to", default="offices/commander/inbox/pending")
    parser.add_argument("--priority", default="normal")
    parser.add_argument("--decision-envelope", default="office-dispatch")
    parser.add_argument("--objective-lock", default="complete exactly the payload")
    parser.add_argument("--expected-output", default="receipt and result artifact")
    parser.add_argument("--completion-condition", default="task marked complete with evidence")
    parser.add_argument("--escalation-path", default="offices/commander/inbox/blocked")
    parser.add_argument("--payload", default=None, help="Inline payload text")
    parser.add_argument("--payload-file", default=None, help="Path to markdown payload")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve() if args.repo_root else Path.cwd().resolve()
    office = args.office.strip().lower()
    pending_dir = repo_root / "offices" / office / "inbox" / "pending"
    pending_dir.mkdir(parents=True, exist_ok=True)

    line_id = args.line_id or f"{office}-{safe_slug(args.title)}-{now_utc().replace(':', '').replace('-', '')}"
    payload = load_payload(args)
    if not payload:
        raise SystemExit("Dispatch payload is empty. Use --payload or --payload-file.")

    file_slug = safe_slug(args.title)
    task_name = f"TASK-{file_slug}-{now_utc().replace(':', '').replace('-', '')}.md"
    task_path = pending_dir / task_name
    task_path.write_text(build_task_markdown(args, line_id, payload), encoding="utf-8")
    print(task_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
