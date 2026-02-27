#!/usr/bin/env python3
"""state_vector.py — Dual-tier state snapshot generator (CC28 Lane 3).

Generates:
  Tier 1: DYN-STATE_VECTOR.md   (~300 tokens, epigenetic priming)
  Tier 2: DYN-PORTAL_EXPANDED.md (~2000 tokens, expanded portal)
  Both:   DYN-STATE_VECTOR.json  (machine-readable intermediate)

All tiers generated from the same intermediate JSON to prevent divergence.
"""
from config import *

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

STATE_DIR = ORCHESTRATION_DIR / "state"
DEFERRED_PATH = STATE_DIR / "DYN-DEFERRED_COMMITMENTS.md"
INTENTION_PATH = STATE_DIR / "ARCH-INTENTION_COMPASS.md"
BASELINE_PATH = STATE_DIR / "DYN-SESSION_BASELINE.json"
AGENTS_MD_PATH = REPO_ROOT / "AGENTS.md"

OUT_VECTOR_MD = STATE_DIR / "DYN-STATE_VECTOR.md"
OUT_PORTAL_MD = STATE_DIR / "DYN-PORTAL_EXPANDED.md"
OUT_VECTOR_JSON = STATE_DIR / "DYN-STATE_VECTOR.json"

# Token budget approximation: 1 token ≈ 4 chars
TIER1_CHAR_LIMIT = 300 * 4   # 1200 chars
TIER2_CHAR_LIMIT = 2000 * 4  # 8000 chars

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_file(path: Path) -> str:
    """Read file contents, return empty string on failure."""
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def git_safe_point(repo_root: Path) -> dict:
    """Get latest commit hash + date."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%H %aI"],
            cwd=repo_root, capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            parts = result.stdout.strip().split(" ", 1)
            return {"hash": parts[0][:8], "date": parts[1][:10] if len(parts) > 1 else "unknown"}
    except Exception:
        pass
    # Fallback: read baseline
    baseline = read_file(BASELINE_PATH)
    if baseline:
        try:
            data = json.loads(baseline)
            return {"hash": data.get("commit", "unknown")[:8],
                    "date": data.get("timestamp", "unknown")[:10]}
        except Exception:
            pass
    return {"hash": "unknown", "date": "unknown"}


def estimate_tokens(text: str) -> int:
    """Rough token estimate: chars / 4."""
    return len(text) // 4


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------

def parse_phase_status(text: str) -> list:
    """Extract phase headers and their status from DYN-DEFERRED_COMMITMENTS.md."""
    phases = []
    # Match lines like: ### Phase 0: Infrastructure Alive — ✅ DONE (2026-02-23)
    pattern = re.compile(
        r"^###\s+Phase\s+(\d+[A-Za-z]?):\s+(.+?)\s*[—–-]\s*(.+)$", re.MULTILINE
    )
    for m in pattern.finditer(text):
        phase_id = m.group(1).strip()
        title = m.group(2).strip()
        status_raw = m.group(3).strip()
        # Normalize status
        if "DONE" in status_raw.upper():
            status = "DONE"
        elif "IN PROGRESS" in status_raw.upper() or "NEXT" in status_raw.upper():
            status = "IN PROGRESS"
        else:
            status = status_raw[:40]
        phases.append({"id": phase_id, "title": title, "status": status})
    return phases


def current_phase(phases: list) -> dict:
    """Determine the current active phase."""
    for p in phases:
        if p["status"] == "IN PROGRESS":
            return p
    # If none in progress, find the first non-DONE
    for p in phases:
        if p["status"] != "DONE":
            return p
    # All done
    if phases:
        return phases[-1]
    return {"id": "?", "title": "Unknown", "status": "Unknown"}


def parse_intentions(text: str, limit: int = 10) -> list:
    """Extract active intentions from ARCH-INTENTION_COMPASS.md tables.

    Looks for table rows matching: | INT-XXXX | ... | "text" | active | ... |
    Returns up to `limit` results, prioritized by category order in the file.
    """
    intentions = []
    # Table format varies:
    #   | INT-XXXX | N | "text" | active | notes |
    #   | INT-XXXX | N | "text" | active | integrated |
    # The quoted text is the intention; status follows.
    pattern = re.compile(
        r"\|\s*(INT-\w+)\s*\|[^|]*\|\s*\"([^\"]+)\"\s*\|\s*(active)\s*\|",
        re.MULTILINE
    )
    seen = set()
    for m in pattern.finditer(text):
        int_id = m.group(1).strip()
        if int_id in seen:
            continue
        seen.add(int_id)
        title = m.group(2).strip()
        # Truncate long titles
        if len(title) > 80:
            title = title[:77] + "..."
        intentions.append({"id": int_id, "title": title})
        if len(intentions) >= limit:
            break
    return intentions


def parse_inhibitions(agents_text: str, phases: list) -> list:
    """Extract concrete inhibitions from AGENTS.md anti-patterns + phase gates."""
    inhibitions = []

    # Phase gate inhibitions
    cur = current_phase(phases)
    cur_id = cur["id"]
    for p in phases:
        if p["status"] != "DONE" and p["id"] != cur_id:
            inhibitions.append(f"Phase {p['id']} ({p['title']}) blocked until Phase {cur_id} P0 complete")
            if len(inhibitions) >= 2:
                break

    # Anti-patterns from AGENTS.md
    in_section = False
    for line in agents_text.splitlines():
        if "Anti-Patterns" in line and "PROHIBITED" in line:
            in_section = True
            continue
        if in_section:
            if line.startswith("---") or (line.startswith("#") and "Anti-Patterns" not in line):
                break
            stripped = line.strip()
            if stripped.startswith("- "):
                # Extract the core prohibition
                item = stripped[2:].strip()
                # Remove bold markers
                item = re.sub(r"\*\*([^*]+)\*\*", r"\1", item)
                # Truncate
                if len(item) > 100:
                    item = item[:97] + "..."
                inhibitions.append(item)

    # Cap at 5
    return inhibitions[:5]


def parse_handoff_refs(repo_root: Path, limit: int = 3) -> list:
    """Find recent HANDOFF files in commander outbox."""
    outbox = repo_root / "agents" / "commander" / "outbox"
    refs = []
    try:
        files = sorted(outbox.glob("HANDOFF-*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
        for f in files[:limit]:
            refs.append(f.name)
    except Exception:
        pass
    return refs


def parse_key_scripts() -> list:
    """List key operational scripts."""
    scripts = [
        "scaffold_validate.sh",
        "dispatch.sh",
        "auto_ingest_loop.sh",
        "memsync_daemon.py",
        "ascertescence_relay.sh",
        "session_state_brief.py",
        "state_vector.py",
    ]
    result = []
    for s in scripts:
        path = SCRIPTS_DIR / s
        if path.exists():
            result.append(s)
    return result


def memory_status_summary(repo_root: Path) -> str:
    """Brief memory system status."""
    parts = []
    memsync = SCRIPTS_DIR / "memsync_daemon.py"
    if memsync.exists():
        parts.append("memsync_daemon: present")
    journal_dir = repo_root / "agents" / "commander" / "memory" / "journal"
    if journal_dir.exists():
        try:
            count = len(list(journal_dir.glob("*.jsonl")))
            parts.append(f"journal files: {count}")
        except Exception:
            pass
    graphiti_health = ORCHESTRATION_DIR / "state" / "DYN-CONSTELLATION_HEALTH.md"
    if graphiti_health.exists():
        text = read_file(graphiti_health)
        if "graphiti" in text.lower():
            if "healthy" in text.lower() or "✅" in text:
                parts.append("Graphiti: healthy")
            else:
                parts.append("Graphiti: status unknown")
    return "; ".join(parts) if parts else "No memory telemetry available"


# ---------------------------------------------------------------------------
# Intermediate JSON builder
# ---------------------------------------------------------------------------

def build_intermediate(repo_root: Path) -> dict:
    """Build the canonical intermediate JSON from all sources."""
    deferred_text = read_file(DEFERRED_PATH)
    intention_text = read_file(INTENTION_PATH)
    agents_text = read_file(AGENTS_MD_PATH)

    phases = parse_phase_status(deferred_text)
    cur = current_phase(phases)
    intentions_all = parse_intentions(intention_text, limit=10)
    inhibitions = parse_inhibitions(agents_text, phases)
    safe_point = git_safe_point(repo_root)
    handoffs = parse_handoff_refs(repo_root)
    scripts = parse_key_scripts()
    mem_status = memory_status_summary(repo_root)

    now = datetime.now(timezone.utc).isoformat()

    return {
        "generated": now,
        "safe_point": safe_point,
        "current_phase": cur,
        "phases": phases,
        "inhibitions": inhibitions,
        "promoters": intentions_all[:3],
        "intentions_top10": intentions_all,
        "transcription_factors": f"Phase {cur['id']} output: structured markdown artifacts committed to repo with semantic prefixes",
        "handoff_refs": handoffs,
        "key_scripts": scripts,
        "memory_status": mem_status,
    }


# ---------------------------------------------------------------------------
# Tier renderers
# ---------------------------------------------------------------------------

def render_tier1(data: dict) -> str:
    """Render Tier 1 State Vector (~300 tokens)."""
    lines = []
    lines.append("# State Vector (Tier 1)")
    lines.append(f"*Generated: {data['generated'][:19]}Z*")
    lines.append("")

    # Phase
    cp = data["current_phase"]
    lines.append(f"## Phase: {cp['id']} — {cp['title']}")
    lines.append(f"Status: {cp['status']}")
    lines.append("")

    # Inhibitions
    lines.append("## Inhibitions")
    for inh in data["inhibitions"][:5]:
        lines.append(f"- {inh}")
    lines.append("")

    # Promoters
    lines.append("## Promoters (Top 3 Active Intentions)")
    for p in data["promoters"][:3]:
        lines.append(f"- **{p['id']}**: {p['title']}")
    lines.append("")

    # Transcription Factors
    lines.append("## Transcription Factors")
    lines.append(data["transcription_factors"])
    lines.append("")

    # Last Safe Point
    sp = data["safe_point"]
    lines.append(f"## Last Safe Point: `{sp['hash']}` ({sp['date']})")

    result = "\n".join(lines)

    # Hard cap: truncate intentions if over budget
    if len(result) > TIER1_CHAR_LIMIT:
        # Try with only 2 promoters
        data_copy = dict(data)
        data_copy["promoters"] = data["promoters"][:2]
        data_copy["inhibitions"] = data["inhibitions"][:3]
        return render_tier1_minimal(data_copy)

    return result


def render_tier1_minimal(data: dict) -> str:
    """Minimal Tier 1 for when full version exceeds budget."""
    lines = []
    lines.append("# State Vector (Tier 1)")
    lines.append(f"*Generated: {data['generated'][:19]}Z*")
    lines.append("")
    cp = data["current_phase"]
    lines.append(f"**Phase**: {cp['id']} — {cp['title']} [{cp['status']}]")
    lines.append("")
    lines.append("**Inhibitions**:")
    for inh in data["inhibitions"][:3]:
        lines.append(f"- {inh}")
    lines.append("")
    lines.append("**Promoters**:")
    for p in data["promoters"][:2]:
        lines.append(f"- {p['id']}: {p['title']}")
    lines.append("")
    lines.append(f"**Output**: {data['transcription_factors']}")
    sp = data["safe_point"]
    lines.append(f"**Safe Point**: `{sp['hash']}` ({sp['date']})")
    result = "\n".join(lines)
    # Absolute hard cap
    if len(result) > TIER1_CHAR_LIMIT:
        result = result[:TIER1_CHAR_LIMIT - 3] + "..."
    return result


def render_tier2(data: dict) -> str:
    """Render Tier 2 Expanded Portal (~2000 tokens)."""
    lines = []
    lines.append("# Expanded Portal (Tier 2)")
    lines.append(f"*Generated: {data['generated'][:19]}Z*")
    lines.append("")

    # Phase status table
    lines.append("## Phase Status")
    lines.append("")
    lines.append("| Phase | Title | Status |")
    lines.append("|-------|-------|--------|")
    for p in data["phases"]:
        lines.append(f"| {p['id']} | {p['title']} | {p['status']} |")
    lines.append("")

    # Current phase highlight
    cp = data["current_phase"]
    lines.append(f"**Active Phase**: {cp['id']} — {cp['title']} [{cp['status']}]")
    lines.append("")

    # Inhibitions
    lines.append("## Inhibitions")
    for inh in data["inhibitions"]:
        lines.append(f"- {inh}")
    lines.append("")

    # Top 10 intentions
    lines.append("## Active Intentions (Top 10)")
    for i, intent in enumerate(data["intentions_top10"][:10], 1):
        lines.append(f"{i}. **{intent['id']}**: {intent['title']}")
    lines.append("")

    # Transcription Factors
    lines.append("## Transcription Factors")
    lines.append(data["transcription_factors"])
    lines.append("")

    # Key scripts
    lines.append("## Key Scripts")
    for s in data["key_scripts"]:
        lines.append(f"- `orchestration/00-ORCHESTRATION/scripts/{s}`")
    lines.append("")

    # Memory status
    lines.append("## Memory Status")
    lines.append(data["memory_status"])
    lines.append("")

    # Recent handoffs
    if data["handoff_refs"]:
        lines.append("## Recent Handoffs")
        for h in data["handoff_refs"]:
            lines.append(f"- `agents/commander/outbox/{h}`")
        lines.append("")

    # Safe point
    sp = data["safe_point"]
    lines.append(f"## Last Safe Point: `{sp['hash']}` ({sp['date']})")
    lines.append("")

    # Depth links
    lines.append("## Depth Links")
    lines.append("- Deferred Commitments: `orchestration/00-ORCHESTRATION/state/DYN-DEFERRED_COMMITMENTS.md`")
    lines.append("- Intention Compass: `orchestration/00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md`")
    lines.append("- Constitutional Law: `AGENTS.md`")

    result = "\n".join(lines)

    # Hard cap with priority truncation (intentions first)
    if len(result) > TIER2_CHAR_LIMIT:
        # Reduce intentions to 5
        data_reduced = dict(data)
        data_reduced["intentions_top10"] = data["intentions_top10"][:5]
        lines_reduced = []
        lines_reduced.append("# Expanded Portal (Tier 2)")
        lines_reduced.append(f"*Generated: {data['generated'][:19]}Z*")
        lines_reduced.append("")
        lines_reduced.append("## Phase Status")
        lines_reduced.append("")
        lines_reduced.append("| Phase | Title | Status |")
        lines_reduced.append("|-------|-------|--------|")
        for p in data["phases"]:
            lines_reduced.append(f"| {p['id']} | {p['title']} | {p['status']} |")
        lines_reduced.append("")
        cp = data["current_phase"]
        lines_reduced.append(f"**Active Phase**: {cp['id']} — {cp['title']} [{cp['status']}]")
        lines_reduced.append("")
        lines_reduced.append("## Inhibitions")
        for inh in data["inhibitions"]:
            lines_reduced.append(f"- {inh}")
        lines_reduced.append("")
        lines_reduced.append("## Active Intentions (Top 5)")
        for i, intent in enumerate(data_reduced["intentions_top10"], 1):
            lines_reduced.append(f"{i}. **{intent['id']}**: {intent['title']}")
        lines_reduced.append("")
        lines_reduced.append("## Transcription Factors")
        lines_reduced.append(data["transcription_factors"])
        lines_reduced.append("")
        lines_reduced.append("## Memory Status")
        lines_reduced.append(data["memory_status"])
        lines_reduced.append("")
        sp = data["safe_point"]
        lines_reduced.append(f"## Last Safe Point: `{sp['hash']}` ({sp['date']})")
        result = "\n".join(lines_reduced)
        if len(result) > TIER2_CHAR_LIMIT:
            result = result[:TIER2_CHAR_LIMIT - 3] + "..."

    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="State Vector Generator (CC28 Lane 3)")
    parser.add_argument("--repo-root", type=str, default=None,
                        help="Repository root (default: auto-detect from config.py)")
    parser.add_argument("--tier", choices=["tier1", "tier2", "both"], default="both",
                        help="Which tier(s) to generate")
    args = parser.parse_args()

    repo_root = Path(args.repo_root) if args.repo_root else REPO_ROOT

    # Build intermediate
    data = build_intermediate(repo_root)

    # Write JSON intermediate always
    OUT_VECTOR_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_VECTOR_JSON.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"[state_vector] JSON: {OUT_VECTOR_JSON}")

    # Generate requested tiers
    if args.tier in ("tier1", "both"):
        tier1 = render_tier1(data)
        OUT_VECTOR_MD.write_text(tier1 + "\n", encoding="utf-8")
        t1_tokens = estimate_tokens(tier1)
        print(f"[state_vector] Tier 1: {OUT_VECTOR_MD} ({t1_tokens} tokens, {len(tier1)} chars)")
        if t1_tokens > 300:
            print(f"[state_vector] WARNING: Tier 1 exceeds 300 token budget ({t1_tokens})")

    if args.tier in ("tier2", "both"):
        tier2 = render_tier2(data)
        OUT_PORTAL_MD.write_text(tier2 + "\n", encoding="utf-8")
        t2_tokens = estimate_tokens(tier2)
        print(f"[state_vector] Tier 2: {OUT_PORTAL_MD} ({t2_tokens} tokens, {len(tier2)} chars)")
        if t2_tokens > 2000:
            print(f"[state_vector] WARNING: Tier 2 exceeds 2000 token budget ({t2_tokens})")

    print("[state_vector] Done.")


if __name__ == "__main__":
    main()
