#!/usr/bin/env python3
"""Circadian Sync — Dream Cycle Consolidation.

Between-session consolidation script that "dreams": replays journals and
handoffs, deduplicates, classifies retain/forget, and appends consolidated
memory.

Usage:
    python3 circadian_sync.py --repo-root /path/to/syncrescendence
    python3 circadian_sync.py --repo-root /path/to/syncrescendence --dry-run
    python3 circadian_sync.py --repo-root /path/to/syncrescendence --force
"""

import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths (relative to repo root, resolved at runtime)
# ---------------------------------------------------------------------------

def resolve_paths(repo_root: Path) -> dict:
    """Build all path references from repo root."""
    commander = repo_root / "agents" / "commander"
    memory = commander / "memory"
    orch = repo_root / "orchestration" / "00-ORCHESTRATION"
    return {
        "repo_root": repo_root,
        "journal_dir": memory / "journal",
        "handoff_dir": commander / "outbox" / "handoffs",
        "handoff_dir_alt": commander / "outbox",
        "deferred": orch / "state" / "DYN-DEFERRED_COMMITMENTS.md",
        "consolidation": memory / "MEMORY_CONSOLIDATION.md",
        "forget_candidates": memory / "sync" / "FORGET_CANDIDATES.jsonl",
        "state_file": memory / "sync" / "circadian_state.json",
        "dream_quality": orch / "state" / "DYN-DREAM_QUALITY.jsonl",
    }

# ---------------------------------------------------------------------------
# Safety: check for active CLI sessions
# ---------------------------------------------------------------------------

CLI_PROCESS_NAMES = ("claude", "codex", "gemini", "openclaw")

def active_session_detected() -> bool:
    """Return True if a CLI agent process is running (heuristic)."""
    try:
        out = subprocess.check_output(["ps", "aux"], text=True, timeout=5)
        for line in out.splitlines():
            low = line.lower()
            for name in CLI_PROCESS_NAMES:
                # Match the binary name but avoid matching ourselves or editors
                if name in low and "circadian_sync" not in low and "grep" not in low:
                    return True
    except Exception:
        pass
    return False

# ---------------------------------------------------------------------------
# State cursor
# ---------------------------------------------------------------------------

def load_state(path: Path) -> dict:
    """Load cursor state or return defaults."""
    if path.exists():
        try:
            with open(path) as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return {
        "last_commit": None,
        "last_timestamp": "1970-01-01T00:00:00.000Z",
        "last_cycle": 0,
        "content_hashes": [],
    }


def save_state(path: Path, state: dict):
    """Write state cursor atomically."""
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(state, f, indent=2)
    tmp.rename(path)

# ---------------------------------------------------------------------------
# Input collection
# ---------------------------------------------------------------------------

def collect_journal_entries(journal_dir: Path, since_ts: str) -> list[dict]:
    """Read all JSONL journal entries newer than since_ts."""
    entries = []
    if not journal_dir.exists():
        return entries
    for jfile in sorted(journal_dir.glob("*.jsonl")):
        with open(jfile) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    # Unparseable — include as raw excerpt
                    entries.append({
                        "source": "journal_unparsed",
                        "timestamp": "",
                        "fact": line[:500],
                        "context": str(jfile.name),
                        "decision_ids": [],
                    })
                    continue
                ts = entry.get("ts", "")
                if ts > since_ts:
                    entries.append(normalize_journal(entry, jfile.name))
    return entries


def normalize_journal(entry: dict, filename: str) -> dict:
    """Normalize a journal entry to uniform format."""
    text = entry.get("text", "")
    kind = entry.get("kind", "unknown")
    refs = entry.get("refs", {})
    session = entry.get("session", {})

    # Extract decision IDs from text (DC-NNN, INT-NNNN, CC-NN patterns)
    decision_ids = re.findall(r'(?:DC-\d+|INT-\d+|CC\d+)', text)

    context_parts = [f"kind={kind}"]
    if refs.get("git"):
        context_parts.append(f"git={refs['git']}")
    if session.get("commits"):
        context_parts.append(f"commits={session['commits']}")
    if session.get("files_changed"):
        context_parts.append(f"files={session['files_changed']}")

    return {
        "source": f"journal/{filename}",
        "timestamp": entry.get("ts", ""),
        "fact": text,
        "context": ", ".join(context_parts),
        "decision_ids": decision_ids,
    }


def collect_git_log(repo_root: Path, since_commit: str | None) -> list[dict]:
    """Collect git log entries since last sync."""
    entries = []
    try:
        cmd = ["git", "-C", str(repo_root), "log", "--format=%H|%aI|%s", "--no-merges"]
        if since_commit:
            cmd.append(f"{since_commit}..HEAD")
        else:
            cmd.extend(["-n", "50"])  # Cap initial run
        out = subprocess.check_output(cmd, text=True, timeout=10).strip()
    except (subprocess.SubprocessError, OSError):
        return entries

    for line in out.splitlines():
        parts = line.split("|", 2)
        if len(parts) < 3:
            continue
        commit_hash, ts, subject = parts
        decision_ids = re.findall(r'(?:DC-\d+|INT-\d+|CC\d+)', subject)
        entries.append({
            "source": "git_log",
            "timestamp": ts,
            "fact": f"{commit_hash[:8]} {subject}",
            "context": f"commit={commit_hash[:12]}",
            "decision_ids": decision_ids,
        })
    return entries


def collect_handoffs(handoff_dir: Path, handoff_dir_alt: Path, since_ts: str) -> list[dict]:
    """Collect new handoff files by mtime."""
    entries = []
    dirs_to_scan = []
    if handoff_dir.exists():
        dirs_to_scan.append(handoff_dir)
    if handoff_dir_alt.exists():
        dirs_to_scan.append(handoff_dir_alt)

    since_dt = _parse_ts(since_ts)

    for d in dirs_to_scan:
        for hf in d.glob("HANDOFF-*.md"):
            mtime = datetime.fromtimestamp(hf.stat().st_mtime, tz=timezone.utc)
            if mtime <= since_dt:
                continue
            try:
                content = hf.read_text(errors="replace")
            except OSError:
                continue
            # Extract key sections
            summary = _extract_handoff_summary(content, hf.name)
            entries.append({
                "source": f"handoff/{hf.name}",
                "timestamp": mtime.isoformat(),
                "fact": summary,
                "context": f"file={hf.name}",
                "decision_ids": re.findall(r'(?:DC-\d+|INT-\d+|CC\d+)', content),
            })
    return entries


def _extract_handoff_summary(content: str, filename: str) -> str:
    """Extract key accomplishments and next steps from handoff markdown."""
    lines = content.splitlines()
    sections = []
    capture = False
    current = []
    for line in lines:
        if re.match(r'^##\s+(WHAT THIS SESSION ACCOMPLISHED|WHAT WAS NOT DONE|WHAT THE NEXT SESSION MUST DO)', line):
            if current:
                sections.append("\n".join(current))
            current = [line]
            capture = True
        elif capture and line.startswith("## ") and not re.match(r'^###', line):
            sections.append("\n".join(current))
            current = []
            capture = False
        elif capture:
            current.append(line)
    if current:
        sections.append("\n".join(current))

    summary = "\n".join(sections).strip()
    if not summary:
        # Fallback: first 500 chars
        summary = content[:500].strip()
    # Compress to max 800 chars
    if len(summary) > 800:
        summary = summary[:797] + "..."
    return summary


def _parse_ts(ts_str: str) -> datetime:
    """Parse ISO timestamp to datetime, tolerant of formats."""
    try:
        # Handle Z suffix
        ts_str = ts_str.replace("Z", "+00:00")
        return datetime.fromisoformat(ts_str)
    except (ValueError, TypeError):
        return datetime(1970, 1, 1, tzinfo=timezone.utc)

# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------

def content_hash(fact: str) -> str:
    """SHA-256 of normalized fact text."""
    normalized = re.sub(r'\s+', ' ', fact.strip().lower())
    return hashlib.sha256(normalized.encode()).hexdigest()[:16]


def deduplicate(entries: list[dict], seen_hashes: list[str]) -> tuple[list[dict], list[str]]:
    """Remove duplicates by content hash. Returns (unique_entries, all_hashes)."""
    seen = set(seen_hashes)
    unique = []
    new_hashes = list(seen_hashes)
    for e in entries:
        h = content_hash(e["fact"])
        if h not in seen:
            seen.add(h)
            new_hashes.append(h)
            unique.append(e)
    # Cap hash history to prevent unbounded growth
    if len(new_hashes) > 5000:
        new_hashes = new_hashes[-3000:]
    return unique, new_hashes

# ---------------------------------------------------------------------------
# Retain / Forget classification
# ---------------------------------------------------------------------------

RETAIN_SIGNALS = [
    r'(?:DC-|INT-|CC)\d+',          # Decision/intention/council references
    r'architect',                     # Architectural
    r'phase\s*\d',                   # Phase transitions
    r'blocker|blocked',              # Blockers
    r'rationale|because|reason',     # Rationale-bearing
    r'decision|decided',             # Decisions
    r'invariant|constitutional',     # Constitutional
    r'NEVER|SEARED|CRITICAL',        # Strong signals
    r'new intention|new pattern',    # New knowledge
    r'safe.?build.?point',           # Checkpoints
]

FORGET_SIGNALS = [
    r'^[a-f0-9]{8}\s+(?:chore|style|docs):',   # Routine commits
    r'kind=session_end.*commits=0',              # Empty sessions
    r'^\s*$',                                     # Blank
    r'verification passed',                       # Mechanical
    r'git status clean',                          # Mechanical
]


def classify(entry: dict) -> str:
    """Classify entry as 'retain' or 'forget_candidate'."""
    fact = entry.get("fact", "")
    context = entry.get("context", "")
    combined = f"{fact} {context}"

    # Check retain signals
    retain_score = sum(1 for pat in RETAIN_SIGNALS if re.search(pat, combined, re.IGNORECASE))
    forget_score = sum(1 for pat in FORGET_SIGNALS if re.search(pat, combined, re.IGNORECASE))

    # Decision IDs strongly signal retention
    if entry.get("decision_ids"):
        retain_score += 2

    if retain_score > forget_score:
        return "retain"
    if forget_score > 0 and retain_score == 0:
        return "forget_candidate"
    # Default: retain (conservative)
    return "retain"

# ---------------------------------------------------------------------------
# Summarization (rationale-preserving compression)
# ---------------------------------------------------------------------------

def summarize_retained(entries: list[dict]) -> str:
    """Compress retained entries into rationale-preserving summary."""
    if not entries:
        return "_No new entries to consolidate._"

    # Group by source type
    by_source = {}
    for e in entries:
        src_type = e["source"].split("/")[0] if "/" in e["source"] else e["source"]
        by_source.setdefault(src_type, []).append(e)

    parts = []
    for src_type, group in sorted(by_source.items()):
        facts = []
        for e in group:
            fact = e["fact"].strip()
            if not fact:
                continue
            # Compress long facts
            if len(fact) > 300:
                fact = fact[:297] + "..."
            ids = e.get("decision_ids", [])
            id_tag = f" [{', '.join(ids)}]" if ids else ""
            facts.append(f"- {fact}{id_tag}")
        if facts:
            parts.append(f"**{src_type}**:\n" + "\n".join(facts))

    return "\n\n".join(parts)

# ---------------------------------------------------------------------------
# Quality metrics
# ---------------------------------------------------------------------------

def compute_quality(
    total_inputs: int,
    unique_count: int,
    retained: int,
    forgotten: int,
    unparsed: int,
) -> dict:
    """Compute dream quality metrics."""
    dedup_ratio = 1.0 - (unique_count / total_inputs) if total_inputs > 0 else 0.0
    retain_ratio = retained / unique_count if unique_count > 0 else 0.0
    return {
        "total_inputs": total_inputs,
        "after_dedup": unique_count,
        "retained": retained,
        "forget_candidates": forgotten,
        "unparsed": unparsed,
        "dedup_ratio": round(dedup_ratio, 3),
        "retain_ratio": round(retain_ratio, 3),
        "quality_score": round(retain_ratio * (1.0 - unparsed / max(total_inputs, 1)), 3),
    }

# ---------------------------------------------------------------------------
# Output writers
# ---------------------------------------------------------------------------

QUALITY_THRESHOLD = 0.1  # Below this, write as draft only


def write_consolidation(path: Path, cycle: int, summary: str, commit_range: str, ts: str, draft: bool):
    """Append one cycle block to MEMORY_CONSOLIDATION.md."""
    header = f"## Cycle {cycle}{' [DRAFT]' if draft else ''} — {ts[:10]}\n"
    header += f"_Commit range: {commit_range}_\n\n"
    block = header + summary + "\n\n---\n\n"

    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("# Memory Consolidation Log\n\nAppend-only dream cycle output from `circadian_sync.py`.\n\n---\n\n")
    with open(path, "a") as f:
        f.write(block)


def write_forget_candidates(path: Path, entries: list[dict], cycle: int, ts: str):
    """Append forget candidates to JSONL ledger."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as f:
        for e in entries:
            record = {
                "cycle": cycle,
                "ts": ts,
                "status": "candidate",
                "fact_hash": content_hash(e["fact"]),
                "fact_preview": e["fact"][:200],
                "source": e["source"],
            }
            f.write(json.dumps(record) + "\n")


def write_dream_quality(path: Path, cycle: int, ts: str, metrics: dict):
    """Append quality metrics to DYN-DREAM_QUALITY.jsonl."""
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {"cycle": cycle, "ts": ts, **metrics}
    with open(path, "a") as f:
        f.write(json.dumps(record) + "\n")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def get_head_commit(repo_root: Path) -> str | None:
    """Get current HEAD commit hash."""
    try:
        return subprocess.check_output(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            text=True, timeout=5
        ).strip()
    except (subprocess.SubprocessError, OSError):
        return None


def run(repo_root: Path, dry_run: bool = False, force: bool = False):
    """Execute one dream cycle."""
    paths = resolve_paths(repo_root)

    # Safety check
    if not force and active_session_detected():
        print("ABORT: Active CLI session detected. Use --force to override.", file=sys.stderr)
        sys.exit(1)

    # Load state
    state = load_state(paths["state_file"])
    cycle = state["last_cycle"] + 1
    since_ts = state["last_timestamp"]
    since_commit = state["last_commit"]
    now = datetime.now(timezone.utc).isoformat()

    print(f"=== Circadian Sync — Cycle {cycle} ===")
    print(f"Since: ts={since_ts}, commit={since_commit or 'INITIAL'}")

    # Collect inputs
    journal_entries = collect_journal_entries(paths["journal_dir"], since_ts)
    git_entries = collect_git_log(repo_root, since_commit)
    handoff_entries = collect_handoffs(paths["handoff_dir"], paths["handoff_dir_alt"], since_ts)

    all_entries = journal_entries + git_entries + handoff_entries
    total_inputs = len(all_entries)
    print(f"Collected: {len(journal_entries)} journal, {len(git_entries)} git, {len(handoff_entries)} handoff = {total_inputs} total")

    if total_inputs == 0:
        print("Nothing new to consolidate. Exiting.")
        return

    # Deduplicate
    unique_entries, new_hashes = deduplicate(all_entries, state.get("content_hashes", []))
    print(f"After dedup: {len(unique_entries)} unique (removed {total_inputs - len(unique_entries)})")

    # Classify
    retained = []
    forgotten = []
    unparsed_count = 0
    for e in unique_entries:
        if e["source"].endswith("_unparsed"):
            unparsed_count += 1
            retained.append(e)  # Keep unparsed for safety
        elif classify(e) == "retain":
            retained.append(e)
        else:
            forgotten.append(e)

    print(f"Classified: {len(retained)} retain, {len(forgotten)} forget candidates, {unparsed_count} unparsed")

    # Summarize
    summary = summarize_retained(retained)

    # Quality metrics
    metrics = compute_quality(total_inputs, len(unique_entries), len(retained), len(forgotten), unparsed_count)
    is_draft = metrics["quality_score"] < QUALITY_THRESHOLD
    if is_draft:
        print(f"WARNING: Quality score {metrics['quality_score']} below threshold {QUALITY_THRESHOLD} — writing as DRAFT")

    # Commit range string
    head = get_head_commit(repo_root)
    commit_range = f"{(since_commit or 'INITIAL')[:8]}..{(head or 'UNKNOWN')[:8]}"

    if dry_run:
        print("\n--- DRY RUN OUTPUT ---")
        print(f"\nCycle: {cycle}")
        print(f"Commit range: {commit_range}")
        print(f"Quality: {json.dumps(metrics, indent=2)}")
        print(f"Draft: {is_draft}")
        print(f"\n--- RETAINED SUMMARY ---\n{summary}")
        print(f"\n--- FORGET CANDIDATES ({len(forgotten)}) ---")
        for e in forgotten:
            print(f"  [{e['source']}] {e['fact'][:120]}")
        return

    # Write outputs
    write_consolidation(paths["consolidation"], cycle, summary, commit_range, now, is_draft)
    print(f"Wrote consolidation cycle {cycle} to {paths['consolidation']}")

    if forgotten:
        write_forget_candidates(paths["forget_candidates"], forgotten, cycle, now)
        print(f"Wrote {len(forgotten)} forget candidates to {paths['forget_candidates']}")

    write_dream_quality(paths["dream_quality"], cycle, now, metrics)
    print(f"Wrote quality metrics to {paths['dream_quality']}")

    # Update state cursor
    new_state = {
        "last_commit": head,
        "last_timestamp": now,
        "last_cycle": cycle,
        "content_hashes": new_hashes,
    }
    save_state(paths["state_file"], new_state)
    print(f"Updated state cursor: cycle={cycle}, commit={head[:8] if head else 'UNKNOWN'}")
    print(f"\nDream cycle {cycle} complete.")


def main():
    parser = argparse.ArgumentParser(description="Circadian Sync — Dream Cycle Consolidation")
    parser.add_argument("--repo-root", required=True, type=Path, help="Syncrescendence repo root")
    parser.add_argument("--dry-run", action="store_true", help="Show decisions without writing")
    parser.add_argument("--force", action="store_true", help="Run even if active session detected")
    args = parser.parse_args()

    if not args.repo_root.exists():
        print(f"ERROR: Repo root does not exist: {args.repo_root}", file=sys.stderr)
        sys.exit(1)

    run(args.repo_root, dry_run=args.dry_run, force=args.force)


if __name__ == "__main__":
    main()
