#!/usr/bin/env python3
"""Periodic corpus health checker for Syncrescendence vault."""
from config import *

import re
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path

VAULT = Path("/Users/home/Desktop/syncrescendence")
STATE_DIR = VAULT / "orchestration/state"
MODEL_INDEX = VAULT / "engine/MODEL-INDEX.md"
HEALTH_REPORT = STATE_DIR / "DYN-CORPUS_HEALTH.md"
NOTIFIER = "/opt/homebrew/bin/terminal-notifier"
STALE_DAYS = 7

NOW = datetime.now(timezone.utc)


def parse_date(text: str) -> datetime | None:
    """Try to parse common date formats from markdown content."""
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d %H:%M"):
        try:
            return datetime.strptime(text.strip(), fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def check_model_index() -> dict:
    """Check MODEL-INDEX.md for last_verified staleness."""
    if not MODEL_INDEX.exists():
        return {"status": "MISSING", "detail": "MODEL-INDEX.md not found"}
    content = MODEL_INDEX.read_text(encoding="utf-8")
    match = re.search(r"\*\*Last [Vv]erified\*\*:\s*(\S+)", content)
    if not match:
        return {"status": "STALE", "detail": "No 'Last Verified' timestamp found"}
    dt = parse_date(match.group(1))
    if dt is None:
        return {"status": "UNKNOWN", "detail": f"Unparseable date: {match.group(1)}"}
    age = NOW - dt
    if age > timedelta(days=STALE_DAYS):
        return {"status": "STALE", "detail": f"Last verified {age.days}d ago ({match.group(1)})"}
    return {"status": "OK", "detail": f"Verified {match.group(1)} ({age.days}d ago)"}


def check_dyn_files() -> list[dict]:
    """Check all DYN-*.md files for staleness based on mtime."""
    results = []
    for f in sorted(STATE_DIR.glob("DYN-*.md")):
        mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)
        age = NOW - mtime
        status = "STALE" if age > timedelta(days=STALE_DAYS) else "OK"
        results.append({
            "file": f.name,
            "status": status,
            "age_days": age.days,
            "modified": mtime.strftime("%Y-%m-%d %H:%M"),
        })
    return results


def check_git_status() -> dict:
    """Check for uncommitted work in the vault.

    DYN state files and constellation state are excluded from dirty detection
    because session hooks (session_log.sh, ajna_pedigree.sh, etc.) write to
    them at session end, leaving them always uncommitted between sessions.
    """
    # Files that are expected to be uncommitted between sessions
    EXPECTED_DIRTY = {
        ".constellation/state/current.yaml",
        "orchestration/state/DYN-CORPUS_HEALTH.md",
        "orchestration/state/DYN-EXECUTION_STAGING.md",
        "orchestration/state/DYN-INTENTIONS_QUEUE.md",
        "orchestration/state/DYN-PEDIGREE_LOG.md",
        "orchestration/state/DYN-SESSION_LOG.md",
    }
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=str(VAULT), capture_output=True, text=True, timeout=10,
        )
        all_lines = [l for l in result.stdout.rstrip("\n").split("\n") if l]
        # Filter out expected DYN state file changes (porcelain: "XY path")
        lines = [l for l in all_lines if l[3:] not in EXPECTED_DIRTY]
        ignored = len(all_lines) - len(lines)
        if lines:
            detail = f"{len(lines)} uncommitted changes"
            if ignored:
                detail += f" ({ignored} expected DYN files excluded)"
            return {"status": "DIRTY", "detail": detail, "files": lines[:15]}
        detail = "Working tree clean"
        if ignored:
            detail += f" ({ignored} expected DYN files excluded)"
        return {"status": "CLEAN", "detail": detail}
    except Exception as e:
        return {"status": "ERROR", "detail": str(e)}


def send_alert(message: str):
    """Send macOS notification if terminal-notifier is available."""
    try:
        subprocess.run(
            [NOTIFIER, "-title", "Syncrescendence Health", "-message", message,
             "-group", "corpus-health", "-sound", "Basso"],
            timeout=5, capture_output=True,
        )
    except FileNotFoundError:
        pass  # terminal-notifier not installed


def write_report(model_status: dict, dyn_results: list[dict], git_status: dict):
    """Write health report to DYN-CORPUS_HEALTH.md."""
    stale_items = []
    lines = [
        "# Corpus Health Report",
        f"**Generated**: {NOW.strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## MODEL-INDEX",
        f"- **Status**: {model_status['status']}",
        f"- {model_status['detail']}",
        "",
        "## DYN State Files",
        "",
        "| File | Status | Age (days) | Last Modified |",
        "|------|--------|------------|---------------|",
    ]
    for r in dyn_results:
        lines.append(f"| {r['file']} | {r['status']} | {r['age_days']} | {r['modified']} |")
        if r["status"] == "STALE":
            stale_items.append(r["file"])
    lines.extend(["", "## Git Status", f"- **Status**: {git_status['status']}", f"- {git_status['detail']}"])
    if git_status.get("files"):
        lines.append("")
        for f in git_status["files"]:
            lines.append(f"  - `{f}`")
    if model_status["status"] == "STALE":
        stale_items.insert(0, "MODEL-INDEX.md")
    if git_status["status"] == "DIRTY":
        stale_items.append("uncommitted git changes")
    lines.extend(["", "---", f"**Findings**: {len(stale_items)} issue(s)" if stale_items else "**Findings**: All clear"])
    HEALTH_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return stale_items


def main():
    model_status = check_model_index()
    dyn_results = check_dyn_files()
    git_status = check_git_status()
    stale_items = write_report(model_status, dyn_results, git_status)
    if stale_items:
        alert = f"{len(stale_items)} issue(s): {', '.join(stale_items[:3])}"
        send_alert(alert)
        print(f"ALERT: {alert}")
    else:
        print("Corpus health: all clear")


if __name__ == "__main__":
    main()
