#!/usr/bin/env python3
"""
memsync_daemon.py — Journal → Graphiti sync daemon.

Watches agents/*/memory/journal/*.jsonl for new records.
Posts each record to Graphiti /messages with idempotent UUIDs.
Maintains per-agent sync/state.json and sync/outbox.jsonl for retries.

Usage:
    python3 memsync_daemon.py [--once] [--graphiti-base URL] [--repo-root PATH]

    --once          Process pending records and exit (no polling loop)
    --graphiti-base Graphiti HTTP base URL (default: http://localhost:8001)
    --repo-root     Repository root (default: cwd)
"""

import argparse
import glob
import json
import logging
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import urllib.request
import urllib.error

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [memsync] %(levelname)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
log = logging.getLogger("memsync")

AGENTS = ["commander", "psyche", "ajna", "adjudicator", "cartographer"]
POLL_INTERVAL_S = 10


def graphiti_post(base_url: str, path: str, payload: dict, timeout: int = 15) -> dict:
    """POST JSON to Graphiti, return parsed response."""
    url = f"{base_url.rstrip('/')}{path}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body) if body.strip() else {"status": resp.status}
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Graphiti {path} returned {e.code}: {body}") from e


def graphiti_healthy(base_url: str) -> bool:
    """Check Graphiti healthcheck."""
    try:
        url = f"{base_url.rstrip('/')}/healthcheck"
        with urllib.request.urlopen(url, timeout=5) as resp:
            data = json.loads(resp.read())
            return data.get("status") == "healthy"
    except Exception:
        return False


def load_sync_state(state_path: Path) -> dict:
    """Load sync state for an agent."""
    if state_path.exists():
        try:
            return json.loads(state_path.read_text())
        except (json.JSONDecodeError, OSError):
            log.warning("Corrupt state file %s, resetting", state_path)
    return {"last_processed_line": 0, "last_processed_file": None, "sent_uuids": []}


def save_sync_state(state_path: Path, state: dict):
    """Atomically save sync state."""
    tmp = state_path.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2))
    tmp.rename(state_path)


def append_outbox(outbox_path: Path, record: dict, error: str):
    """Append a failed record to the outbox for later retry."""
    entry = {"record": record, "error": error, "ts": datetime.now(timezone.utc).isoformat()}
    with open(outbox_path, "a") as f:
        f.write(json.dumps(entry) + "\n")


def record_to_graphiti_payload(record: dict) -> dict:
    """Convert a JSONL journal record to a Graphiti /messages payload."""
    scope = record.get("scope", "private")
    group_id = "CONSTELLATION" if scope == "shared" else f"AGENT:{record.get('agent', 'unknown')}"

    agent_name = record.get("agent", "unknown")
    kind = record.get("kind", "observation")
    text = record.get("text", "")
    content = f"{agent_name}(agent): [{kind}] {text}"

    return {
        "group_id": group_id,
        "messages": [
            {
                "content": content,
                "name": f"{agent_name}:{kind}",
                "role_type": "assistant",
                "role": agent_name,
                "timestamp": record.get("ts", datetime.now(timezone.utc).isoformat()),
                "source_description": record.get("refs", {}).get("path", "unknown"),
            }
        ],
    }


def process_agent(agent: str, repo_root: Path, graphiti_base: str, state: dict) -> dict:
    """Process new journal records for one agent. Returns updated state."""
    memory_dir = repo_root / "agents" / agent / "memory"
    journal_dir = memory_dir / "journal"
    sync_dir = memory_dir / "sync"
    outbox_path = sync_dir / "outbox.jsonl"

    sent_uuids = set(state.get("sent_uuids", []))

    # Find all journal files (sorted chronologically)
    journal_files = sorted(journal_dir.glob("*.jsonl"))
    # Exclude archive
    journal_files = [f for f in journal_files if "archive" not in str(f)]

    new_count = 0
    skip_count = 0

    for jfile in journal_files:
        with open(jfile) as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    log.warning("%s:%d invalid JSON, skipping", jfile.name, line_num)
                    continue

                uuid = record.get("uuid")
                if not uuid:
                    log.warning("%s:%d missing uuid, skipping", jfile.name, line_num)
                    continue

                if uuid in sent_uuids:
                    skip_count += 1
                    continue

                # Post to Graphiti
                payload = record_to_graphiti_payload(record)
                try:
                    graphiti_post(graphiti_base, "/messages", payload)
                    sent_uuids.add(uuid)
                    new_count += 1
                    log.info("Synced %s → Graphiti (group=%s)", uuid, payload["group_id"])
                except Exception as e:
                    log.error("Failed to sync %s: %s", uuid, e)
                    append_outbox(outbox_path, record, str(e))

    if new_count > 0:
        log.info("[%s] synced %d new, %d skipped (already sent)", agent, new_count, skip_count)

    state["sent_uuids"] = list(sent_uuids)
    state["last_processed_file"] = str(journal_files[-1].name) if journal_files else None
    return state


def retry_outbox(agent: str, repo_root: Path, graphiti_base: str):
    """Retry failed records from the outbox."""
    outbox_path = repo_root / "agents" / agent / "memory" / "sync" / "outbox.jsonl"
    if not outbox_path.exists() or outbox_path.stat().st_size == 0:
        return

    remaining = []
    with open(outbox_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            record = entry.get("record", {})
            payload = record_to_graphiti_payload(record)
            try:
                graphiti_post(graphiti_base, "/messages", payload)
                log.info("[%s] Retried %s successfully", agent, record.get("uuid"))
            except Exception:
                remaining.append(line)

    # Rewrite outbox with only still-failed records
    with open(outbox_path, "w") as f:
        for line in remaining:
            f.write(line + "\n")


def run_once(repo_root: Path, graphiti_base: str):
    """Single pass over all agents."""
    if not graphiti_healthy(graphiti_base):
        log.warning("Graphiti unhealthy at %s, skipping sync pass", graphiti_base)
        return

    for agent in AGENTS:
        state_path = repo_root / "agents" / agent / "memory" / "sync" / "state.json"
        state = load_sync_state(state_path)
        state = process_agent(agent, repo_root, graphiti_base, state)
        save_sync_state(state_path, state)
        retry_outbox(agent, repo_root, graphiti_base)


def main():
    parser = argparse.ArgumentParser(description="memsync: journal → Graphiti sync daemon")
    parser.add_argument("--once", action="store_true", help="Process once and exit")
    parser.add_argument("--graphiti-base", default="http://localhost:8001", help="Graphiti URL")
    parser.add_argument("--repo-root", default=".", help="Repository root path")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    log.info("memsync starting (repo=%s, graphiti=%s, mode=%s)", repo_root, args.graphiti_base, "once" if args.once else "daemon")

    if args.once:
        run_once(repo_root, args.graphiti_base)
        return

    while True:
        try:
            run_once(repo_root, args.graphiti_base)
        except KeyboardInterrupt:
            log.info("Shutting down")
            break
        except Exception as e:
            log.error("Sync pass failed: %s", e)
        time.sleep(POLL_INTERVAL_S)


if __name__ == "__main__":
    main()
