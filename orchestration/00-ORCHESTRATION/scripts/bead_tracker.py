#!/usr/bin/env python3
"""
bead_tracker.py — Git-native tracking ("Beads") for Syncrescendence.

Implements DC-150: commit trailers, commit wrapper, JSONL index, query, stats.
Wraps git commit with Bead-* trailers via git interpret-trailers.
Builds incremental JSONL index from git log.
Queries and stats over the index.

Usage:
    python3 bead_tracker.py commit -m "message" --agent commander --directive DC-208 [--intent INT-2210] [-- <git-commit-args>]
    python3 bead_tracker.py index [--full]
    python3 bead_tracker.py query [--agent X] [--directive DC-xxx] [--intent INT-xxxx] [--since DATE] [--until DATE] [--commit HASH]
    python3 bead_tracker.py stats [--by agent|directive|day]

Stdlib only. Target: 480-720 LOC.
"""

import argparse
import json
import os
import subprocess
import sys
import uuid
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REPO_ROOT = subprocess.run(
    ["git", "rev-parse", "--show-toplevel"],
    capture_output=True, text=True, check=False
).stdout.strip() or os.getcwd()

STATE_DIR = os.path.join(REPO_ROOT, "orchestration", "00-ORCHESTRATION", "state")
INDEX_PATH = os.path.join(STATE_DIR, "DYN-BEAD_INDEX.jsonl")
CURSOR_PATH = os.path.join(STATE_DIR, ".bead_cursor")

TRAILER_PREFIX = "Bead-"
REQUIRED_TRAILERS = ["Bead-ID", "Bead-Agent", "Bead-Directive"]
OPTIONAL_TRAILERS = ["Bead-Intent"]
ALL_TRAILERS = REQUIRED_TRAILERS + OPTIONAL_TRAILERS

KNOWN_AGENTS = [
    "commander", "psyche", "ajna", "adjudicator", "cartographer", "sovereign"
]

# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------


def run_git(*args: str, check: bool = True, capture: bool = True) -> subprocess.CompletedProcess:
    """Run a git command, returning CompletedProcess."""
    cmd = ["git"] + list(args)
    return subprocess.run(
        cmd,
        capture_output=capture,
        text=True,
        check=check,
        cwd=REPO_ROOT,
    )


def die(msg: str, code: int = 1) -> None:
    """Print error and exit."""
    print(f"bead: error: {msg}", file=sys.stderr)
    sys.exit(code)


def warn(msg: str) -> None:
    """Print warning to stderr."""
    print(f"bead: warn: {msg}", file=sys.stderr)


def generate_bead_id() -> str:
    """Generate a deterministic-format Bead UUID."""
    return str(uuid.uuid4())


def validate_agent(agent: str) -> str:
    """Validate and normalize agent name."""
    normalized = agent.lower().strip()
    if normalized not in KNOWN_AGENTS:
        warn(f"unknown agent '{normalized}' (known: {', '.join(KNOWN_AGENTS)})")
    return normalized


def validate_directive(directive: str) -> str:
    """Validate directive format DC-xxx."""
    d = directive.upper().strip()
    if not d.startswith("DC-"):
        die(f"directive must start with 'DC-': got '{directive}'")
    try:
        int(d[3:])
    except ValueError:
        die(f"directive must be DC-<number>: got '{directive}'")
    return d


def validate_intent(intent: Optional[str]) -> Optional[str]:
    """Validate optional intent format INT-xxxx."""
    if intent is None:
        return None
    i = intent.upper().strip()
    if not i.startswith("INT-"):
        die(f"intent must start with 'INT-': got '{intent}'")
    return i


def iso_now() -> str:
    """Current UTC ISO timestamp."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_date(s: str) -> datetime:
    """Parse a date string (YYYY-MM-DD or ISO)."""
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z"):
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    die(f"cannot parse date: '{s}' (use YYYY-MM-DD)")
    return datetime.min  # unreachable


# ---------------------------------------------------------------------------
# COMMIT command
# ---------------------------------------------------------------------------


def build_trailer_args(bead_id: str, agent: str, directive: str,
                       intent: Optional[str]) -> list[str]:
    """Build --trailer arguments for git interpret-trailers."""
    trailers = [
        f"Bead-ID: {bead_id}",
        f"Bead-Agent: {agent}",
        f"Bead-Directive: {directive}",
    ]
    if intent:
        trailers.append(f"Bead-Intent: {intent}")
    args = []
    for t in trailers:
        args.extend(["--trailer", t])
    return args


def cmd_commit(args: argparse.Namespace) -> None:
    """Execute bead commit: wrap git commit with trailers."""
    agent = validate_agent(args.agent)
    directive = validate_directive(args.directive)
    intent = validate_intent(args.intent)
    bead_id = generate_bead_id()

    if not args.message:
        die("commit message required (-m)")

    # Build message with trailers via git interpret-trailers
    trailer_args = build_trailer_args(bead_id, agent, directive, intent)
    interpret = subprocess.run(
        ["git", "interpret-trailers"] + trailer_args,
        input=args.message,
        capture_output=True,
        text=True,
        check=True,
        cwd=REPO_ROOT,
    )
    full_message = interpret.stdout.strip()

    # Determine commit method based on repo size (sandbox kill workaround)
    # For safety: always try git commit-tree plumbing first on large repos
    use_plumbing = args.plumbing
    if not use_plumbing:
        # Check file count heuristic
        try:
            count = run_git("rev-list", "--count", "--all")
            if int(count.stdout.strip()) > 1500:
                use_plumbing = True
        except (subprocess.CalledProcessError, ValueError):
            pass

    if use_plumbing:
        _commit_plumbing(full_message, args.passthrough)
    else:
        _commit_porcelain(full_message, args.passthrough)

    print(f"Bead committed: {bead_id}")
    print(f"  Agent:     {agent}")
    print(f"  Directive: {directive}")
    if intent:
        print(f"  Intent:    {intent}")


def _commit_porcelain(message: str, passthrough: list[str]) -> None:
    """Standard git commit."""
    cmd = ["git", "commit", "-m", message] + passthrough
    result = subprocess.run(cmd, cwd=REPO_ROOT, check=False)
    if result.returncode != 0:
        die(f"git commit failed (exit {result.returncode})")


def _commit_plumbing(message: str, passthrough: list[str]) -> None:
    """Plumbing commit for large repos (sandbox kill workaround).

    Uses git write-tree + git commit-tree + git update-ref.
    """
    # Ensure index is clean (files should already be staged)
    tree = run_git("write-tree")
    tree_hash = tree.stdout.strip()

    # Get parent
    try:
        head = run_git("rev-parse", "HEAD")
        parent_hash = head.stdout.strip()
        parent_args = ["-p", parent_hash]
    except subprocess.CalledProcessError:
        parent_args = []  # initial commit

    # Create commit object
    commit = subprocess.run(
        ["git", "commit-tree", tree_hash] + parent_args,
        input=message,
        capture_output=True,
        text=True,
        check=True,
        cwd=REPO_ROOT,
    )
    commit_hash = commit.stdout.strip()

    # Update HEAD
    run_git("update-ref", "HEAD", commit_hash)
    print(f"  (plumbing commit: {commit_hash[:12]})")


# ---------------------------------------------------------------------------
# INDEX command
# ---------------------------------------------------------------------------


def read_cursor() -> Optional[str]:
    """Read the last indexed commit hash."""
    if os.path.exists(CURSOR_PATH):
        with open(CURSOR_PATH, "r") as f:
            return f.read().strip() or None
    return None


def write_cursor(commit_hash: str) -> None:
    """Write the cursor to last indexed commit."""
    os.makedirs(os.path.dirname(CURSOR_PATH), exist_ok=True)
    with open(CURSOR_PATH, "w") as f:
        f.write(commit_hash)


def parse_trailers_from_message(message: str) -> dict[str, str]:
    """Extract Bead-* trailers from a commit message."""
    trailers: dict[str, str] = {}
    for line in message.splitlines():
        line = line.strip()
        for key in ALL_TRAILERS:
            prefix = f"{key}:"
            if line.startswith(prefix):
                trailers[key] = line[len(prefix):].strip()
    return trailers


def extract_beads_from_log(since_commit: Optional[str] = None,
                           full: bool = False) -> list[dict[str, Any]]:
    """Scan git log for commits with Bead-* trailers."""
    # Format: hash|timestamp|subject
    # Then parse body for trailers
    log_args = [
        "log",
        "--format=%H|%aI|%s",
        "--all",
    ]
    if since_commit and not full:
        log_args.append(f"{since_commit}..HEAD")

    result = run_git(*log_args, check=False)
    if result.returncode != 0 or not result.stdout.strip():
        return []

    commits = result.stdout.strip().splitlines()
    beads: list[dict[str, Any]] = []

    for line in commits:
        parts = line.split("|", 2)
        if len(parts) < 3:
            continue
        commit_hash, timestamp, summary = parts

        # Get full message for this commit to extract trailers
        msg_result = run_git("log", "-1", "--format=%B", commit_hash, check=False)
        if msg_result.returncode != 0:
            continue

        trailers = parse_trailers_from_message(msg_result.stdout)
        if "Bead-ID" not in trailers:
            continue  # Not a bead commit

        # Get files changed
        files_result = run_git(
            "diff-tree", "--no-commit-id", "-r", "--name-only", commit_hash,
            check=False
        )
        files_changed = [
            f for f in files_result.stdout.strip().splitlines() if f
        ] if files_result.returncode == 0 else []

        bead: dict[str, Any] = {
            "bead_id": trailers["Bead-ID"],
            "commit_hash": commit_hash,
            "timestamp": timestamp,
            "agent": trailers.get("Bead-Agent", "unknown"),
            "directive": trailers.get("Bead-Directive", "unknown"),
            "intent": trailers.get("Bead-Intent"),
            "files_changed": files_changed,
            "summary": summary,
        }
        beads.append(bead)

    return beads


def load_index() -> list[dict[str, Any]]:
    """Load existing JSONL index."""
    if not os.path.exists(INDEX_PATH):
        return []
    entries: list[dict[str, Any]] = []
    with open(INDEX_PATH, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    warn(f"skipping malformed index line: {line[:60]}...")
    return entries


def write_index(entries: list[dict[str, Any]]) -> None:
    """Write JSONL index atomically."""
    os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
    tmp = INDEX_PATH + ".tmp"
    with open(tmp, "w") as f:
        for entry in entries:
            f.write(json.dumps(entry, separators=(",", ":")) + "\n")
    os.replace(tmp, INDEX_PATH)


def cmd_index(args: argparse.Namespace) -> None:
    """Build or update the bead index."""
    full = args.full
    cursor = None if full else read_cursor()

    if full:
        print("bead: full index rebuild...")
        existing: list[dict[str, Any]] = []
    else:
        existing = load_index()
        if cursor:
            print(f"bead: incremental index from {cursor[:12]}...")
        else:
            print("bead: initial index build...")

    new_beads = extract_beads_from_log(since_commit=cursor, full=full)

    if not new_beads and not full:
        print(f"bead: index up to date ({len(existing)} beads)")
        return

    # Deduplicate by bead_id
    seen = {e["bead_id"] for e in existing}
    added = 0
    for bead in new_beads:
        if bead["bead_id"] not in seen:
            existing.append(bead)
            seen.add(bead["bead_id"])
            added += 1

    # Sort by timestamp
    existing.sort(key=lambda b: b.get("timestamp", ""))

    write_index(existing)

    # Update cursor to current HEAD
    head = run_git("rev-parse", "HEAD", check=False)
    if head.returncode == 0:
        write_cursor(head.stdout.strip())

    print(f"bead: indexed {added} new beads (total: {len(existing)})")


# ---------------------------------------------------------------------------
# QUERY command
# ---------------------------------------------------------------------------


def matches_query(bead: dict[str, Any], filters: dict[str, Any]) -> bool:
    """Check if a bead matches all query filters."""
    if filters.get("agent") and bead.get("agent") != filters["agent"]:
        return False
    if filters.get("directive") and bead.get("directive") != filters["directive"]:
        return False
    if filters.get("intent") and bead.get("intent") != filters["intent"]:
        return False
    if filters.get("commit") and not bead.get("commit_hash", "").startswith(filters["commit"]):
        return False

    # Date filters
    if filters.get("since") or filters.get("until"):
        try:
            ts = datetime.fromisoformat(bead["timestamp"].replace("Z", "+00:00"))
        except (ValueError, KeyError):
            return False
        if filters.get("since") and ts < filters["since"]:
            return False
        if filters.get("until") and ts > filters["until"]:
            return False

    return True


def cmd_query(args: argparse.Namespace) -> None:
    """Query the bead index."""
    index = load_index()
    if not index:
        print("[]")
        return

    filters: dict[str, Any] = {}
    if args.agent:
        filters["agent"] = args.agent.lower()
    if args.directive:
        filters["directive"] = args.directive.upper()
    if args.intent:
        filters["intent"] = args.intent.upper()
    if args.commit:
        filters["commit"] = args.commit
    if args.since:
        filters["since"] = parse_date(args.since)
    if args.until:
        filters["until"] = parse_date(args.until)

    results = [b for b in index if matches_query(b, filters)]

    if args.count:
        print(len(results))
        return

    if args.compact:
        for b in results:
            agent = b.get("agent", "?")
            directive = b.get("directive", "?")
            summary = b.get("summary", "")
            commit = b.get("commit_hash", "")[:12]
            ts = b.get("timestamp", "")[:10]
            print(f"{ts}  {commit}  {agent:<13}  {directive:<8}  {summary}")
    else:
        print(json.dumps(results, indent=2))


# ---------------------------------------------------------------------------
# STATS command
# ---------------------------------------------------------------------------


def cmd_stats(args: argparse.Namespace) -> None:
    """Print summary statistics from the bead index."""
    index = load_index()
    if not index:
        print("bead: no beads indexed")
        return

    by = args.by or "all"

    print(f"Bead Statistics ({len(index)} total beads)")
    print("=" * 56)

    if by in ("all", "agent"):
        agent_counts: dict[str, int] = defaultdict(int)
        for b in index:
            agent_counts[b.get("agent", "unknown")] += 1
        print("\nBy Agent:")
        for agent, count in sorted(agent_counts.items(), key=lambda x: -x[1]):
            bar = "#" * min(count, 40)
            print(f"  {agent:<14} {count:>5}  {bar}")

    if by in ("all", "directive"):
        dir_counts: dict[str, int] = defaultdict(int)
        for b in index:
            dir_counts[b.get("directive", "unknown")] += 1
        print("\nBy Directive:")
        for d, count in sorted(dir_counts.items(), key=lambda x: -x[1]):
            bar = "#" * min(count, 40)
            print(f"  {d:<14} {count:>5}  {bar}")

    if by in ("all", "day"):
        day_counts: dict[str, int] = defaultdict(int)
        for b in index:
            ts = b.get("timestamp", "")[:10]
            if ts:
                day_counts[ts] += 1
        print("\nBy Day:")
        for day, count in sorted(day_counts.items()):
            bar = "#" * min(count, 40)
            print(f"  {day}  {count:>5}  {bar}")

    if by == "all":
        # Additional summary
        agents = set(b.get("agent", "unknown") for b in index)
        directives = set(b.get("directive", "unknown") for b in index)
        intents = set(b.get("intent") for b in index if b.get("intent"))
        first = index[0].get("timestamp", "?")[:10]
        last = index[-1].get("timestamp", "?")[:10]
        print(f"\nSummary:")
        print(f"  Agents:     {len(agents)} ({', '.join(sorted(agents))})")
        print(f"  Directives: {len(directives)} ({', '.join(sorted(directives))})")
        print(f"  Intents:    {len(intents)}")
        print(f"  Date range: {first} .. {last}")


# ---------------------------------------------------------------------------
# VALIDATE command (bonus: check recent commits for missing trailers)
# ---------------------------------------------------------------------------


def cmd_validate(args: argparse.Namespace) -> None:
    """Validate recent commits for bead trailer compliance."""
    count = args.count or 10
    result = run_git("log", f"-{count}", "--format=%H|%s", check=False)
    if result.returncode != 0 or not result.stdout.strip():
        print("bead: no commits to validate")
        return

    compliant = 0
    missing = 0
    for line in result.stdout.strip().splitlines():
        parts = line.split("|", 1)
        if len(parts) < 2:
            continue
        commit_hash, summary = parts

        msg_result = run_git("log", "-1", "--format=%B", commit_hash, check=False)
        if msg_result.returncode != 0:
            continue

        trailers = parse_trailers_from_message(msg_result.stdout)
        has_bead = "Bead-ID" in trailers
        missing_keys = [k for k in REQUIRED_TRAILERS if k not in trailers]

        if has_bead and not missing_keys:
            status = "OK"
            compliant += 1
        elif has_bead:
            status = f"PARTIAL (missing: {', '.join(missing_keys)})"
            missing += 1
        else:
            status = "NO-BEAD"
            missing += 1

        print(f"  {commit_hash[:12]}  {status:<30}  {summary[:50]}")

    total = compliant + missing
    pct = (compliant / total * 100) if total else 0
    print(f"\nCompliance: {compliant}/{total} ({pct:.0f}%)")


# ---------------------------------------------------------------------------
# BACKFILL command (tag historical commits retroactively via notes)
# ---------------------------------------------------------------------------


def cmd_backfill(args: argparse.Namespace) -> None:
    """Backfill bead metadata onto historical commits using git notes.

    Does NOT rewrite history. Stores trailers in git notes namespace
    'beads' so they can be indexed alongside real trailers.
    """
    agent = validate_agent(args.agent)
    directive = validate_directive(args.directive)
    intent = validate_intent(args.intent)

    # Determine commits to backfill
    rev_range = args.range or "HEAD~5..HEAD"
    result = run_git("log", "--format=%H", rev_range, check=False)
    if result.returncode != 0 or not result.stdout.strip():
        die(f"no commits found in range '{rev_range}'")

    commits = result.stdout.strip().splitlines()
    count = 0

    for commit_hash in commits:
        # Skip if already has bead trailers
        msg = run_git("log", "-1", "--format=%B", commit_hash, check=False)
        if msg.returncode == 0 and "Bead-ID:" in msg.stdout:
            warn(f"skip {commit_hash[:12]}: already has Bead-ID")
            continue

        # Check for existing note
        note = run_git("notes", "--ref=beads", "show", commit_hash, check=False)
        if note.returncode == 0 and "Bead-ID:" in note.stdout:
            warn(f"skip {commit_hash[:12]}: already has bead note")
            continue

        bead_id = generate_bead_id()
        note_body = f"Bead-ID: {bead_id}\nBead-Agent: {agent}\nBead-Directive: {directive}"
        if intent:
            note_body += f"\nBead-Intent: {intent}"
        note_body += f"\nBead-Backfill: {iso_now()}"

        run_git("notes", "--ref=beads", "add", "-m", note_body, commit_hash, check=True)
        count += 1
        print(f"  {commit_hash[:12]}  <- {bead_id}")

    print(f"\nbead: backfilled {count} commits")


# ---------------------------------------------------------------------------
# CLI Parser
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    parser = argparse.ArgumentParser(
        prog="bead",
        description="Git-native tracking (Beads) for Syncrescendence — DC-150",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # -- commit --
    p_commit = sub.add_parser("commit", help="Commit with Bead trailers")
    p_commit.add_argument("-m", "--message", required=True, help="Commit message")
    p_commit.add_argument("--agent", required=True, help="Agent name")
    p_commit.add_argument("--directive", required=True, help="Directive (DC-xxx)")
    p_commit.add_argument("--intent", default=None, help="Intent (INT-xxxx, optional)")
    p_commit.add_argument(
        "--plumbing", action="store_true",
        help="Force plumbing commit (write-tree/commit-tree) for sandbox safety"
    )
    p_commit.add_argument(
        "passthrough", nargs="*", default=[],
        help="Additional args passed to git commit"
    )

    # -- index --
    p_index = sub.add_parser("index", help="Build/update bead JSONL index")
    p_index.add_argument("--full", action="store_true", help="Full rebuild (ignore cursor)")

    # -- query --
    p_query = sub.add_parser("query", help="Query the bead index")
    p_query.add_argument("--agent", help="Filter by agent")
    p_query.add_argument("--directive", help="Filter by directive")
    p_query.add_argument("--intent", help="Filter by intent")
    p_query.add_argument("--since", help="Filter from date (YYYY-MM-DD)")
    p_query.add_argument("--until", help="Filter until date (YYYY-MM-DD)")
    p_query.add_argument("--commit", help="Filter by commit hash prefix")
    p_query.add_argument("--count", action="store_true", help="Only print count")
    p_query.add_argument("--compact", action="store_true", help="One-line-per-bead output")

    # -- stats --
    p_stats = sub.add_parser("stats", help="Bead statistics")
    p_stats.add_argument(
        "--by", choices=["agent", "directive", "day", "all"], default="all",
        help="Group by dimension"
    )

    # -- validate --
    p_validate = sub.add_parser("validate", help="Check recent commits for bead compliance")
    p_validate.add_argument("--count", type=int, default=10, help="Number of recent commits to check")

    # -- backfill --
    p_backfill = sub.add_parser("backfill", help="Backfill bead notes onto historical commits")
    p_backfill.add_argument("--agent", required=True, help="Agent name")
    p_backfill.add_argument("--directive", required=True, help="Directive (DC-xxx)")
    p_backfill.add_argument("--intent", default=None, help="Intent (INT-xxxx, optional)")
    p_backfill.add_argument("--range", default="HEAD~5..HEAD", help="Git rev range to backfill")

    return parser


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


DISPATCH = {
    "commit": cmd_commit,
    "index": cmd_index,
    "query": cmd_query,
    "stats": cmd_stats,
    "validate": cmd_validate,
    "backfill": cmd_backfill,
}


def main() -> None:
    """Entry point."""
    parser = build_parser()
    args = parser.parse_args()
    handler = DISPATCH.get(args.command)
    if handler is None:
        parser.print_help()
        sys.exit(1)
    handler(args)


if __name__ == "__main__":
    main()
