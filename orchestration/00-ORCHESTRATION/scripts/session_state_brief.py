#!/usr/bin/env python3
# session_state_brief.py — Descriptive session state brief generator
# CC26 Adjudicator spec Task 2A-2D
#
# Generates a ≤300-word markdown brief showing system state.
# Descriptive only — NO commands, NO to-dos, NO "you should".
# Every section wrapped in try/except with fallback text.

import json, re, subprocess, glob, os, sys
from pathlib import Path
from datetime import datetime, timezone
from urllib.request import urlopen
from urllib.error import URLError

REPO_ROOT = Path("/Users/system/syncrescendence")
STATE_DIR = REPO_ROOT / "orchestration/00-ORCHESTRATION/state"
BRIEF_PATH = STATE_DIR / "DYN-SESSION_STATE_BRIEF.md"
BASELINE_PATH = STATE_DIR / "DYN-SESSION_BASELINE.json"
ERR_LOG = STATE_DIR / "DYN-SESSION_STATE_BRIEF.err.log"

MAX_WORDS = 300
MAX_BULLETS = 5

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def log_error(section: str, err: Exception):
    """Append error to log file."""
    try:
        with open(ERR_LOG, "a") as f:
            f.write(f"{datetime.now(timezone.utc).isoformat()} [{section}] {err}\n")
    except Exception:
        pass

def word_count(text: str) -> int:
    return len(text.split())

def truncate_section_bullets(lines: list[str], max_bullets: int = MAX_BULLETS) -> list[str]:
    """Keep header + up to max_bullets bullet lines."""
    header = []
    bullets = []
    for ln in lines:
        if ln.strip().startswith("- "):
            bullets.append(ln)
        else:
            if not bullets:
                header.append(ln)
            # ignore trailing non-bullet lines
    return header + bullets[:max_bullets]

# ---------------------------------------------------------------------------
# Section 1: Current Priorities
# ---------------------------------------------------------------------------

def section_priorities() -> list[str]:
    lines = ["## Current Priorities", ""]
    try:
        # Sovereign intents from intentions queue
        iq_path = STATE_DIR / "DYN-INTENTIONS_QUEUE.md"
        intents = []
        if iq_path.exists():
            text = iq_path.read_text()
            blocks = re.findall(
                r"### .+? — SOVEREIGN INTENT: (.+?)$(.+?)(?=###|\Z)",
                text, re.MULTILINE | re.DOTALL
            )
            for title, body in blocks:
                pri_m = re.search(r"\*\*Priority\*\*:\s*(P\d)", body)
                status_m = re.search(r"\*\*Status\*\*:\s*(\S+)", body)
                pri = pri_m.group(1) if pri_m else "?"
                status = status_m.group(1) if status_m else ""
                if status.upper() in ("DONE", "RESOLVED", "SUPERSEDED"):
                    continue
                intents.append((pri, title.strip()))
        # Sort by priority
        intents.sort(key=lambda x: x[0])

        # Deferred commitments — P0/P1, OPEN/IN PROGRESS/READY
        dc_path = STATE_DIR / "DYN-DEFERRED_COMMITMENTS.md"
        dc_items = []
        if dc_path.exists():
            text = dc_path.read_text()
            # Match table rows: | DC-xxx | ... | commitment | Pri | Status |
            for m in re.finditer(
                r"\|\s*(DC-\S+)\s*\|[^|]*\|([^|]*)\|\s*(P[01])\s*\|\s*\*{0,2}(OPEN|IN PROGRESS|READY)\*{0,2}\s*\|",
                text
            ):
                dc_id, commitment, pri, status = m.group(1), m.group(2).strip(), m.group(3), m.group(4)
                dc_items.append(f"- [{pri}] {dc_id}: {commitment[:60]}")

        if intents:
            for pri, title in intents[:3]:
                lines.append(f"- [{pri}] Sovereign intent: {title[:60]}")
        if dc_items:
            for item in dc_items[:max(0, MAX_BULLETS - len(intents[:3]))]:
                lines.append(item)
        if len(lines) == 2:
            lines.append("- No open priorities found")
    except Exception as e:
        log_error("priorities", e)
        lines.append(f"- (Error reading priorities: {e})")
    return lines

# ---------------------------------------------------------------------------
# Section 2: Open Decisions
# ---------------------------------------------------------------------------

def section_open_decisions() -> list[str]:
    lines = ["## Open Decisions", ""]
    try:
        sov_dir = REPO_ROOT / "-SOVEREIGN"
        if not sov_dir.exists():
            lines.append("- No -SOVEREIGN/ directory found")
            return lines

        pending = []
        for pattern in ["SOVEREIGN-*.md", "DECISION-*.md"]:
            for fpath in sorted(sov_dir.glob(pattern)):
                try:
                    text = fpath.read_text(errors="replace")[:4000]
                    # Check for Status: PENDING or no Status line at all in DECISION files
                    status_m = re.search(r"\*\*Status\*\*:\s*(.+?)$", text, re.MULTILINE)
                    if status_m:
                        status_val = status_m.group(1).strip().upper()
                        if "PENDING" in status_val or "OPEN" in status_val:
                            title_m = re.search(r"^#\s+(.+)", text, re.MULTILINE)
                            title = title_m.group(1).strip() if title_m else fpath.name
                            pending.append(f"- {fpath.name}: {title[:55]}")
                    elif "DECISION" in fpath.name:
                        # Decision files without explicit status might be pending
                        title_m = re.search(r"^#\s+(.+)", text, re.MULTILINE)
                        title = title_m.group(1).strip() if title_m else fpath.name
                        # Only if no APPROVED/DONE/RESOLVED
                        if not re.search(r"(APPROVED|DONE|RESOLVED|EXECUTED)", text, re.IGNORECASE):
                            pending.append(f"- {fpath.name}: {title[:55]}")
                except Exception:
                    pass

        if pending:
            for item in pending[:MAX_BULLETS]:
                lines.append(item)
        else:
            lines.append("- No pending decisions in -SOVEREIGN/")
    except Exception as e:
        log_error("open_decisions", e)
        lines.append(f"- (Error reading decisions: {e})")
    return lines

# ---------------------------------------------------------------------------
# Section 3: Last 3 Agent Actions
# ---------------------------------------------------------------------------

def section_last_actions() -> list[str]:
    lines = ["## Last 3 Agent Actions", ""]
    try:
        journal_dir = REPO_ROOT / "agents/commander/memory/journal"
        if not journal_dir.exists():
            lines.append("- No journal directory found")
            return lines

        # Collect all jsonl files, sorted desc
        jfiles = sorted(journal_dir.glob("*.jsonl"), reverse=True)
        entries = []
        seen = set()
        for jf in jfiles:
            if len(entries) >= 3:
                break
            try:
                for raw_line in reversed(jf.read_text().strip().splitlines()):
                    if not raw_line.strip():
                        continue
                    rec = json.loads(raw_line)
                    kind = rec.get("kind", "")
                    text = rec.get("text", "")
                    key = f"{kind}:{text[:80]}"
                    if key in seen:
                        continue
                    seen.add(key)
                    ts = rec.get("ts", "")[:16].replace("T", " ")
                    entries.append(f"- [{ts}] {kind}: {text[:70]}")
                    if len(entries) >= 3:
                        break
            except Exception:
                pass

        if entries:
            for item in entries:
                lines.append(item)
        else:
            lines.append("- No journal entries found")
    except Exception as e:
        log_error("last_actions", e)
        lines.append(f"- (Error reading journal: {e})")
    return lines

# ---------------------------------------------------------------------------
# Section 4: Graph Health
# ---------------------------------------------------------------------------

def section_graph_health() -> list[str]:
    lines = ["## Graph Health", ""]
    try:
        # Try Graphiti healthcheck
        try:
            resp = urlopen("http://M1-Mac-mini.local:8001/healthcheck", timeout=3)
            data = resp.read().decode()
            lines.append(f"- Graphiti: HEALTHY ({data[:60].strip()})")
            return lines
        except (URLError, OSError, Exception):
            pass

        # Fallback: constellation health file
        health_path = STATE_DIR / "DYN-CONSTELLATION_HEALTH.md"
        if not health_path.exists():
            health_path = REPO_ROOT / "orchestration/00-ORCHESTRATION/state/DYN-CONSTELLATION_HEALTH.md"
        if health_path.exists():
            text = health_path.read_text()
            last_m = re.search(r"Last check:\s*(.+)", text)
            lines.append(f"- Graphiti: UNREACHABLE (endpoint timed out)")
            if last_m:
                lines.append(f"- Last constellation check: {last_m.group(1).strip()}")
            # Extract agent statuses
            for m in re.finditer(r"\|\s*(\w+)\s*\|[^|]*\|[^|]*\|\s*(\w+)\s*\|", text):
                agent, status = m.group(1), m.group(2)
                if agent.lower() in ("agent",):
                    continue
                lines.append(f"- {agent}: {status}")
                if len(lines) > MAX_BULLETS + 2:
                    break
        else:
            lines.append("- Graphiti: UNREACHABLE")
            lines.append("- No constellation health file found")
    except Exception as e:
        log_error("graph_health", e)
        lines.append(f"- (Error checking health: {e})")
    return lines

# ---------------------------------------------------------------------------
# Section 5: What Changed Since Last
# ---------------------------------------------------------------------------

SIGNAL_PATHS = re.compile(
    r"(canon/|praxis/05-SIGMA/|engine/02-ENGINE/|orchestration/00-ORCHESTRATION/scripts/|-SOVEREIGN/|AGENTS\.md|CLAUDE\.md|DYN-DEFERRED_COMMITMENTS\.md)"
)
SIGNAL_SUBJECTS = re.compile(r"(feat|fix|decision|protocol|gate|autonomy)", re.IGNORECASE)
NOISE_PATHS = re.compile(r"^(\.DS_Store|.*\.log|budgets/.*\.count)$")
NOISE_SUBJECTS = re.compile(r"(chore:\s*update state hash|auto-compact|sync counters)", re.IGNORECASE)


def classify_commit(subject: str, files: list[str]) -> str:
    """Return 'signal' or 'noise'."""
    # Noise check first
    if NOISE_SUBJECTS.search(subject):
        if all(NOISE_PATHS.match(f) for f in files if f.strip()):
            return "noise"
    # Signal check
    if SIGNAL_SUBJECTS.search(subject):
        return "signal"
    for f in files:
        if SIGNAL_PATHS.search(f):
            return "signal"
    return "noise"


def section_delta() -> list[str]:
    lines = ["## What Changed Since Last", ""]
    try:
        baseline_ts = None
        baseline_commit = None
        if BASELINE_PATH.exists():
            bl = json.loads(BASELINE_PATH.read_text())
            baseline_ts = bl.get("timestamp")
            baseline_commit = bl.get("commit")

        git_args = ["git", "-C", str(REPO_ROOT), "log", "--pretty=format:%H|%s", "--name-only"]
        if baseline_commit:
            git_args.append(f"{baseline_commit}..HEAD")
        else:
            git_args.extend(["-20"])

        result = subprocess.run(git_args, capture_output=True, text=True, timeout=10)
        if result.returncode != 0:
            lines.append("- (git log failed)")
            return lines

        raw = result.stdout.strip()
        if not raw:
            lines.append("- No new commits since last brief")
            return lines

        # Parse commits: hash|subject followed by file lines until next hash|subject
        commits = []
        current_hash = None
        current_subject = None
        current_files = []

        for ln in raw.splitlines():
            if "|" in ln and len(ln.split("|")[0]) == 40:
                if current_hash:
                    commits.append((current_hash[:8], current_subject, current_files))
                parts = ln.split("|", 1)
                current_hash = parts[0]
                current_subject = parts[1] if len(parts) > 1 else ""
                current_files = []
            elif ln.strip():
                current_files.append(ln.strip())

        if current_hash:
            commits.append((current_hash[:8], current_subject, current_files))

        signal_commits = []
        noise_count = 0
        for h, subj, files in commits:
            cls = classify_commit(subj, files)
            if cls == "signal":
                signal_commits.append(f"- `{h}` {subj[:60]}")
            else:
                noise_count += 1

        if baseline_ts:
            lines.append(f"- Baseline: {baseline_ts}")

        total = len(commits)
        lines.append(f"- {total} commits ({len(signal_commits)} signal, {noise_count} noise)")

        for item in signal_commits[:3]:
            lines.append(item)

        if not commits:
            lines.append("- No commits found")

    except Exception as e:
        log_error("delta", e)
        lines.append(f"- (Error reading git log: {e})")
    return lines

# ---------------------------------------------------------------------------
# Assembly + Word Budget
# ---------------------------------------------------------------------------

def build_brief() -> str:
    sections = [
        section_priorities,
        section_open_decisions,
        section_last_actions,
        section_graph_health,
        section_delta,
    ]

    built = []
    for fn in sections:
        try:
            built.append(fn())
        except Exception as e:
            log_error(fn.__name__, e)
            built.append([f"## {fn.__name__}", "", f"- (Section failed: {e})"])

    # Header
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    header = [f"# Session State Brief", f"**Generated**: {now}", "**Cadence**: on-demand", ""]

    # Assemble full text, then enforce word limit
    full_lines = header[:]
    for sec in built:
        full_lines.extend(sec)
        full_lines.append("")
        full_lines.append("---")
        full_lines.append("")

    full_text = "\n".join(full_lines)

    # Word budget enforcement — trim priorities first, then actions
    if word_count(full_text) > MAX_WORDS:
        # Rebuild with truncated priorities (keep header + 1 bullet)
        built[0] = truncate_section_bullets(built[0], 1)
        full_lines = header[:]
        for sec in built:
            full_lines.extend(sec)
            full_lines.append("")
            full_lines.append("---")
            full_lines.append("")
        full_text = "\n".join(full_lines)

    if word_count(full_text) > MAX_WORDS:
        # Truncate last actions to 1
        built[2] = truncate_section_bullets(built[2], 1)
        full_lines = header[:]
        for sec in built:
            full_lines.extend(sec)
            full_lines.append("")
            full_lines.append("---")
            full_lines.append("")
        full_text = "\n".join(full_lines)

    return full_text.rstrip() + "\n"

# ---------------------------------------------------------------------------
# Baseline update
# ---------------------------------------------------------------------------

def update_baseline():
    try:
        result = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=5
        )
        commit = result.stdout.strip() if result.returncode == 0 else "unknown"
        bl = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "commit": commit,
        }
        BASELINE_PATH.write_text(json.dumps(bl, indent=2) + "\n")
    except Exception as e:
        log_error("baseline", e)

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Clear error log for this run
    try:
        ERR_LOG.write_text("")
    except Exception:
        pass

    brief = build_brief()

    # Write to file
    try:
        BRIEF_PATH.write_text(brief)
    except Exception as e:
        log_error("write_brief", e)
        print(f"ERROR: Could not write brief to {BRIEF_PATH}: {e}", file=sys.stderr)

    # Print to stdout
    print(brief)

    # Update baseline
    update_baseline()


if __name__ == "__main__":
    main()
