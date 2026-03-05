#!/usr/bin/env python3
"""Watch an office inbox/pending lane and claim tasks into inbox/active."""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path


STOP = False
LINE_ID_RE = re.compile(r"^\*\*Line-ID\*\*:\s*(.+?)\s*$")


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def timestamp() -> str:
    return utc_now().strftime("%Y%m%dT%H%M%SZ")


def log(msg: str) -> None:
    print(f"[{utc_now().isoformat()}] {msg}", flush=True)


def load_line_id(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None
    for line in text.splitlines():
        m = LINE_ID_RE.match(line.strip())
        if m:
            value = m.group(1).strip()
            return value or None
    return None


def candidate_tasks(pending_dir: Path) -> list[Path]:
    tasks = []
    for path in sorted(pending_dir.glob("*"), key=lambda p: p.stat().st_mtime):
        if not path.is_file():
            continue
        if path.name.startswith("."):
            continue
        if path.name.upper().startswith("README"):
            continue
        tasks.append(path)
    return tasks


def unique_target(active_dir: Path, src_name: str) -> Path:
    target = active_dir / src_name
    if not target.exists():
        return target
    stem = target.stem
    suffix = target.suffix
    return active_dir / f"{stem}--claimed-{timestamp()}{suffix}"


def write_receipt(
    *,
    office: str,
    task_ref: str,
    claimed_by: str,
    pending_path: Path,
    active_path: Path,
    receipts_dir: Path,
    handler_status: str,
    handler_note: str,
) -> Path:
    receipt_name = f"RECEIPT-{task_ref}--{timestamp()}.md"
    receipt_path = receipts_dir / receipt_name
    body = (
        "# RECEIPT\n\n"
        "**Kind**: RECEIPT\n"
        f"**Task-Ref**: `{task_ref}`\n"
        f"**From**: `dispatch`\n"
        f"**To**: `{office}`\n"
        f"**Claimed-By**: `{claimed_by}`\n"
        f"**Claimed-At**: `{utc_now().isoformat()}`\n"
        "**State**: CLAIMED\n"
        "**Decision-Envelope**: `office-inbox-watch`\n"
        "**Next-Action**: `active-lane`\n"
        "**Expected-Completion**: `unspecified`\n"
        "**Escalation-Path**: `offices/commander/inbox/pending`\n\n"
        "## Notes\n\n"
        f"- Pending path: `{pending_path}`\n"
        f"- Active path: `{active_path}`\n"
        f"- Handler status: `{handler_status}`\n"
        f"- Handler note: `{handler_note}`\n"
    )
    receipt_path.write_text(body, encoding="utf-8")
    return receipt_path


def run_handler(handler_template: str, task_path: Path, office: str, repo_root: Path) -> tuple[str, str]:
    rendered = (
        handler_template.replace("{task_path}", str(task_path))
        .replace("{office}", office)
        .replace("{repo_root}", str(repo_root))
    )
    env = os.environ.copy()
    env["SYNC_OFFICE"] = office
    env["SYNC_TASK_PATH"] = str(task_path)
    env["SYNC_REPO_ROOT"] = str(repo_root)
    try:
        proc = subprocess.run(
            rendered,
            shell=True,
            text=True,
            capture_output=True,
            check=False,
            env=env,
            timeout=900,
        )
    except subprocess.TimeoutExpired:
        return "timeout", "handler timed out after 900s"

    if proc.returncode == 0:
        output = (proc.stdout or "").strip()
        return "ok", output[:500] if output else "handler completed"
    output = ((proc.stderr or "") + "\n" + (proc.stdout or "")).strip()
    return "error", output[:500] if output else f"handler exited with {proc.returncode}"


def claim_task(
    *,
    office: str,
    pending_path: Path,
    active_dir: Path,
    receipts_dir: Path,
    claimed_by: str,
    handler_template: str | None,
    repo_root: Path,
) -> None:
    task_ref = load_line_id(pending_path) or pending_path.stem
    active_path = unique_target(active_dir, pending_path.name)
    shutil.move(str(pending_path), str(active_path))
    log(f"{office}: claimed '{pending_path.name}' -> '{active_path.name}'")

    handler_status = "skipped"
    handler_note = "no handler configured"
    if handler_template:
        handler_status, handler_note = run_handler(handler_template, active_path, office, repo_root)
        log(f"{office}: handler {handler_status} ({handler_note})")

    receipt_path = write_receipt(
        office=office,
        task_ref=task_ref,
        claimed_by=claimed_by,
        pending_path=pending_path,
        active_path=active_path,
        receipts_dir=receipts_dir,
        handler_status=handler_status,
        handler_note=handler_note,
    )
    log(f"{office}: receipt -> {receipt_path.name}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--office", required=True, help="Office slug, e.g. psyche")
    parser.add_argument("--repo-root", default=None, help="Repo root path (defaults to cwd)")
    parser.add_argument("--poll-seconds", type=float, default=2.0)
    parser.add_argument("--claimed-by", default=None, help="Claim identity (defaults to '<office>-watcher')")
    parser.add_argument(
        "--handler",
        default=None,
        help="Optional shell handler template with placeholders {task_path} {office} {repo_root}",
    )
    parser.add_argument(
        "--once",
        action="store_true",
        help="Process current pending tasks once then exit.",
    )
    return parser.parse_args()


def install_signal_handlers() -> None:
    def _handle(_signum: int, _frame: object) -> None:
        global STOP
        STOP = True

    signal.signal(signal.SIGINT, _handle)
    signal.signal(signal.SIGTERM, _handle)


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve() if args.repo_root else Path.cwd().resolve()
    office = args.office.strip().lower()
    claimed_by = args.claimed_by or f"{office}-watcher"

    office_root = repo_root / "offices" / office
    pending_dir = office_root / "inbox" / "pending"
    active_dir = office_root / "inbox" / "active"
    receipts_dir = office_root / "outbox" / "receipts"

    for d in (pending_dir, active_dir, receipts_dir):
        d.mkdir(parents=True, exist_ok=True)

    install_signal_handlers()
    log(f"{office}: watcher online (pending={pending_dir})")

    while not STOP:
        tasks = candidate_tasks(pending_dir)
        for task in tasks:
            try:
                claim_task(
                    office=office,
                    pending_path=task,
                    active_dir=active_dir,
                    receipts_dir=receipts_dir,
                    claimed_by=claimed_by,
                    handler_template=args.handler,
                    repo_root=repo_root,
                )
            except FileNotFoundError:
                continue
            except Exception as exc:  # noqa: BLE001
                log(f"{office}: claim failed for {task.name}: {exc}")
        if args.once:
            break
        time.sleep(max(0.5, args.poll_seconds))

    log(f"{office}: watcher stopping")
    return 0


if __name__ == "__main__":
    sys.exit(main())
