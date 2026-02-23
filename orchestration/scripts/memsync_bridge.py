#!/usr/bin/env python3
"""
memsync_bridge.py — Integration bridge between the mining extraction pipeline
and Graphiti, via the memsync subsystem (DC-208-5).

Reads EXTRACT-*.jsonl files produced by the source mining pipeline, validates
records against memsync_schema, maps them to Graphiti entities/edges, and
enqueues them for delivery with a durable SQLite retry queue.

This module is a *companion* to memsync_daemon.py — it does NOT modify or
replace it.  The daemon handles journal -> Graphiti sync; this bridge handles
extraction -> Graphiti sync.

Usage:
    # Ingest extraction output
    python3 orchestration/scripts/memsync_bridge.py \\
      --extract-jsonl sources/04-SOURCES/_meta/EXTRACT-SOURCE-*.jsonl \\
      --graphiti-base http://localhost:8001 \\
      --retry-db orchestration/state/memsync_retry.sqlite

    # Drain retry queue
    python3 orchestration/scripts/memsync_bridge.py \\
      --drain-retry \\
      --retry-db orchestration/state/memsync_retry.sqlite \\
      --graphiti-base http://localhost:8001 \\
      --max-attempts 200
"""

from __future__ import annotations

import argparse
import glob as globmod
import hashlib
import json
import logging
import os
import random
import sqlite3
import sys
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

# Ensure sibling imports work when invoked directly
_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from memsync_schema import (
    SCHEMA_VERSION,
    VALID_RECORD_TYPES,
    GraphitiEdge,
    GraphitiEntity,
    SourceAtomRecord,
    SourceRelationRecord,
    ValidationError,
    idempotency_key,
    map_atom_to_entity,
    map_relation_to_edge,
    parse_record,
    record_to_dict,
    validate_record,
)

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [memsync-bridge] %(levelname)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
log = logging.getLogger("memsync-bridge")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DEFAULT_GRAPHITI_BASE = "http://localhost:8001"
DEFAULT_RETRY_DB = "orchestration/state/memsync_retry.sqlite"
DEFAULT_DLQ_PATH = "orchestration/state/DYN-MEMSYNC_DLQ.jsonl"
MAX_DEAD_LETTER_ATTEMPTS = 10
BACKOFF_BASE_S = 5
BACKOFF_MAX_S = 1800  # 30 minutes


# ---------------------------------------------------------------------------
# Result types
# ---------------------------------------------------------------------------

@dataclass
class EnqueueResult:
    """Summary of an enqueue pass."""
    enqueued: int = 0
    skipped_duplicate: int = 0
    skipped_invalid: int = 0
    errors: List[str] = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        if self.errors is None:
            self.errors = []


@dataclass
class DrainResult:
    """Summary of a retry drain pass."""
    succeeded: int = 0
    retried: int = 0
    dead_lettered: int = 0
    remaining: int = 0


# ---------------------------------------------------------------------------
# SQLite retry queue
# ---------------------------------------------------------------------------

_CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS retry_queue (
    idempotency_key TEXT PRIMARY KEY,
    payload         TEXT NOT NULL,
    attempts        INTEGER NOT NULL DEFAULT 0,
    next_attempt_at TEXT NOT NULL,
    last_error      TEXT DEFAULT NULL,
    created_at      TEXT NOT NULL
);
"""

_CREATE_INDEX_SQL = """
CREATE INDEX IF NOT EXISTS idx_retry_next ON retry_queue(next_attempt_at);
"""


def _init_db(db_path: str) -> sqlite3.Connection:
    """Open (or create) the retry queue database."""
    parent = Path(db_path).parent
    parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute(_CREATE_TABLE_SQL)
    conn.execute(_CREATE_INDEX_SQL)
    conn.commit()
    return conn


def _backoff_seconds(attempt: int) -> float:
    """Exponential backoff with jitter: 5, 15, 45, ... capped at 30 min."""
    base = BACKOFF_BASE_S * (3 ** attempt)
    capped = min(base, BACKOFF_MAX_S)
    jitter = random.uniform(0, capped * 0.2)
    return capped + jitter


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# Graphiti HTTP helpers (mirrors memsync_daemon.graphiti_post)
# ---------------------------------------------------------------------------

def _graphiti_post(base_url: str, path: str, payload: dict, timeout: int = 15) -> dict:
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


def _graphiti_healthy(base_url: str) -> bool:
    """Check Graphiti healthcheck."""
    try:
        url = f"{base_url.rstrip('/')}/healthcheck"
        with urllib.request.urlopen(url, timeout=5) as resp:
            data = json.loads(resp.read())
            return data.get("status") == "healthy"
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Core: send a single record to Graphiti
# ---------------------------------------------------------------------------

def _send_entity(base_url: str, entity: GraphitiEntity) -> dict:
    """Send a GraphitiEntity to Graphiti /messages endpoint."""
    payload = {
        "group_id": entity.group_id,
        "messages": [
            {
                "content": f"[{entity.entity_type}] {entity.name}: {entity.summary}",
                "name": f"bridge:{entity.entity_type}:{entity.name}",
                "role_type": "assistant",
                "role": "memsync-bridge",
                "timestamp": _now_iso(),
                "source_description": f"entity:{entity.uuid}",
            }
        ],
    }
    return _graphiti_post(base_url, "/messages", payload)


def _send_edge(base_url: str, edge: GraphitiEdge) -> dict:
    """Send a GraphitiEdge to Graphiti /messages endpoint."""
    prov_str = json.dumps(edge.provenance) if edge.provenance else "{}"
    payload = {
        "group_id": edge.group_id,
        "messages": [
            {
                "content": (
                    f"[RELATION:{edge.relation_type}] "
                    f"{edge.source_entity_uuid} -> {edge.target_entity_uuid} "
                    f"(weight={edge.weight}) provenance={prov_str}"
                ),
                "name": f"bridge:edge:{edge.relation_type}",
                "role_type": "assistant",
                "role": "memsync-bridge",
                "timestamp": _now_iso(),
                "source_description": f"edge:{edge.source_entity_uuid}->{edge.target_entity_uuid}",
            }
        ],
    }
    return _graphiti_post(base_url, "/messages", payload)


def _send_record_to_graphiti(base_url: str, record: Any) -> dict:
    """Route a parsed record to the correct Graphiti send function."""
    if isinstance(record, SourceAtomRecord):
        entity = map_atom_to_entity(record)
        return _send_entity(base_url, entity)
    elif isinstance(record, SourceRelationRecord):
        edge = map_relation_to_edge(record)
        return _send_edge(base_url, edge)
    else:
        # Non-graph records (quality_gate, failure_pheromone, lineage_event)
        # are stored as informational messages
        d = record_to_dict(record)
        payload = {
            "group_id": f"PIPELINE:{d.get('record_type', 'unknown')}",
            "messages": [
                {
                    "content": json.dumps(d, default=str),
                    "name": f"bridge:{d.get('record_type', 'unknown')}",
                    "role_type": "assistant",
                    "role": "memsync-bridge",
                    "timestamp": _now_iso(),
                    "source_description": f"{d.get('record_type')}:{d.get('uuid', '')}",
                }
            ],
        }
        return _graphiti_post(base_url, "/messages", payload)


# ---------------------------------------------------------------------------
# Public API: ingest
# ---------------------------------------------------------------------------

def ingest_extraction_jsonl(path: str) -> List[Any]:
    """Read an EXTRACT-*.jsonl file and return a list of parsed Record objects.

    Lines that fail validation are logged and skipped.
    """
    records: List[Any] = []
    p = Path(path)
    if not p.exists():
        log.warning("File not found: %s", path)
        return records

    with open(p) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                raw = json.loads(line)
            except json.JSONDecodeError as e:
                log.warning("%s:%d invalid JSON: %s", p.name, line_num, e)
                continue

            # Inject schema_version if absent (backward compat)
            if "schema_version" not in raw:
                raw["schema_version"] = SCHEMA_VERSION

            # Skip memory_event — those route through memsync_daemon
            if raw.get("record_type") == "memory_event":
                continue

            try:
                rec = parse_record(raw)
                records.append(rec)
            except ValidationError as e:
                log.warning("%s:%d validation failed: %s", p.name, line_num, e)

    log.info("Ingested %d records from %s", len(records), p.name)
    return records


# ---------------------------------------------------------------------------
# Public API: Graphiti entity/edge mapping (thin wrappers for CLI symmetry)
# ---------------------------------------------------------------------------

def map_atom_to_entity_pub(atom: SourceAtomRecord) -> GraphitiEntity:
    """Public wrapper — maps a SourceAtomRecord to a GraphitiEntity."""
    return map_atom_to_entity(atom)


def map_atoms_to_relations(atoms: List[SourceRelationRecord]) -> List[GraphitiEdge]:
    """Map a list of SourceRelationRecords to GraphitiEdge payloads."""
    return [map_relation_to_edge(r) for r in atoms]


# ---------------------------------------------------------------------------
# Public API: enqueue
# ---------------------------------------------------------------------------

def enqueue_for_graphiti(
    records: List[Any],
    retry_db: str,
    graphiti_base: str = DEFAULT_GRAPHITI_BASE,
) -> EnqueueResult:
    """Attempt to send records to Graphiti.  Failures go into the retry queue.

    Returns an EnqueueResult summarizing outcomes.
    """
    result = EnqueueResult()
    conn = _init_db(retry_db)

    healthy = _graphiti_healthy(graphiti_base)
    if not healthy:
        log.warning("Graphiti unhealthy — all records will be enqueued for retry")

    for rec in records:
        d = record_to_dict(rec)
        rec_uuid = d.get("uuid", "")
        rel_type = d.get("relation_type", d.get("entity_type", d.get("record_type", "")))
        target = d.get("target_atom_id", d.get("source_id", rec_uuid))
        idem_key = idempotency_key(rec_uuid, rel_type, target)

        # Check for duplicate
        row = conn.execute(
            "SELECT idempotency_key FROM retry_queue WHERE idempotency_key = ?",
            (idem_key,),
        ).fetchone()
        if row:
            result.skipped_duplicate += 1
            continue

        if healthy:
            try:
                _send_record_to_graphiti(graphiti_base, rec)
                result.enqueued += 1
                log.info("Sent %s (%s) to Graphiti", rec_uuid, d.get("record_type"))
                continue
            except Exception as e:
                log.warning("Send failed for %s, enqueueing for retry: %s", rec_uuid, e)

        # Enqueue for retry
        now = _now_iso()
        next_at = datetime.now(timezone.utc).isoformat()
        try:
            conn.execute(
                "INSERT OR IGNORE INTO retry_queue "
                "(idempotency_key, payload, attempts, next_attempt_at, last_error, created_at) "
                "VALUES (?, ?, 0, ?, NULL, ?)",
                (idem_key, json.dumps(d, default=str), next_at, now),
            )
            conn.commit()
            result.enqueued += 1
        except sqlite3.Error as e:
            result.errors.append(f"DB error for {rec_uuid}: {e}")
            result.skipped_invalid += 1

    conn.close()
    return result


# ---------------------------------------------------------------------------
# Public API: drain retry queue
# ---------------------------------------------------------------------------

def drain_retry_queue(
    retry_db: str,
    graphiti_base: str = DEFAULT_GRAPHITI_BASE,
    max_attempts: int = 200,
) -> DrainResult:
    """Process pending retries up to max_attempts total sends.

    Records that exceed MAX_DEAD_LETTER_ATTEMPTS are moved to the DLQ.
    Returns a DrainResult summary.
    """
    result = DrainResult()
    conn = _init_db(retry_db)

    now = _now_iso()
    rows = conn.execute(
        "SELECT idempotency_key, payload, attempts, last_error "
        "FROM retry_queue WHERE next_attempt_at <= ? "
        "ORDER BY next_attempt_at ASC LIMIT ?",
        (now, max_attempts),
    ).fetchall()

    dead_letters: List[Dict[str, Any]] = []

    for idem_key, payload_str, attempts, last_error in rows:
        try:
            d = json.loads(payload_str)
        except json.JSONDecodeError:
            log.error("Corrupt payload for key %s, dead-lettering", idem_key)
            dead_letters.append({
                "idempotency_key": idem_key,
                "payload": payload_str,
                "attempts": attempts,
                "last_error": "corrupt JSON in retry queue",
                "dead_lettered_at": _now_iso(),
            })
            conn.execute("DELETE FROM retry_queue WHERE idempotency_key = ?", (idem_key,))
            result.dead_lettered += 1
            continue

        # Re-parse to get the typed record
        rt = d.get("record_type")
        try:
            rec = parse_record(d)
        except ValidationError:
            # Can't parse — treat as raw and send as informational
            rec = None

        success = False
        try:
            if rec is not None:
                _send_record_to_graphiti(graphiti_base, rec)
            else:
                # Fallback: send raw payload as informational message
                _graphiti_post(graphiti_base, "/messages", {
                    "group_id": f"RETRY:{rt or 'unknown'}",
                    "messages": [{
                        "content": json.dumps(d, default=str),
                        "name": f"bridge:retry:{idem_key[:12]}",
                        "role_type": "assistant",
                        "role": "memsync-bridge",
                        "timestamp": _now_iso(),
                        "source_description": f"retry:{idem_key}",
                    }],
                })
            success = True
        except Exception as e:
            last_error = str(e)

        if success:
            conn.execute("DELETE FROM retry_queue WHERE idempotency_key = ?", (idem_key,))
            result.succeeded += 1
            log.info("Retry succeeded: %s", idem_key[:16])
        else:
            new_attempts = attempts + 1
            if new_attempts >= MAX_DEAD_LETTER_ATTEMPTS:
                dead_letters.append({
                    "idempotency_key": idem_key,
                    "payload": d,
                    "attempts": new_attempts,
                    "last_error": last_error,
                    "dead_lettered_at": _now_iso(),
                })
                conn.execute("DELETE FROM retry_queue WHERE idempotency_key = ?", (idem_key,))
                result.dead_lettered += 1
                log.warning("Dead-lettered after %d attempts: %s", new_attempts, idem_key[:16])
            else:
                backoff = _backoff_seconds(new_attempts)
                next_at = datetime.fromtimestamp(
                    time.time() + backoff, tz=timezone.utc
                ).isoformat()
                conn.execute(
                    "UPDATE retry_queue SET attempts = ?, next_attempt_at = ?, last_error = ? "
                    "WHERE idempotency_key = ?",
                    (new_attempts, next_at, last_error, idem_key),
                )
                result.retried += 1
                log.info("Retry %d for %s, next in %.0fs", new_attempts, idem_key[:16], backoff)

    conn.commit()

    # Write dead letters
    if dead_letters:
        dlq_path = str(Path(retry_db).parent / "DYN-MEMSYNC_DLQ.jsonl")
        written = write_dead_letters(dead_letters, dlq_path)
        log.info("Wrote %d dead letters to %s", written, dlq_path)

    # Count remaining
    remaining = conn.execute("SELECT COUNT(*) FROM retry_queue").fetchone()[0]
    result.remaining = remaining

    conn.close()
    return result


# ---------------------------------------------------------------------------
# Public API: dead letter queue
# ---------------------------------------------------------------------------

def write_dead_letters(failed: List[Dict[str, Any]], dlq_path: str) -> int:
    """Append failed records to the dead-letter JSONL file. Returns count written."""
    Path(dlq_path).parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with open(dlq_path, "a") as f:
        for entry in failed:
            f.write(json.dumps(entry, default=str) + "\n")
            count += 1
    return count


# ---------------------------------------------------------------------------
# Health report helper
# ---------------------------------------------------------------------------

def health_report(retry_db: str, dlq_path: str = DEFAULT_DLQ_PATH) -> Dict[str, Any]:
    """Generate a health summary of the bridge queues."""
    report: Dict[str, Any] = {"retry_db": retry_db, "dlq_path": dlq_path}

    db_path = Path(retry_db)
    if db_path.exists():
        conn = sqlite3.connect(retry_db)
        total = conn.execute("SELECT COUNT(*) FROM retry_queue").fetchone()[0]
        stuck = conn.execute(
            "SELECT COUNT(*) FROM retry_queue WHERE attempts >= ?",
            (MAX_DEAD_LETTER_ATTEMPTS // 2,),
        ).fetchone()[0]
        conn.close()
        report["retry_queue_size"] = total
        report["retry_high_attempt_count"] = stuck
    else:
        report["retry_queue_size"] = 0
        report["retry_high_attempt_count"] = 0

    dlq = Path(dlq_path)
    if dlq.exists():
        with open(dlq) as f:
            report["dlq_size"] = sum(1 for line in f if line.strip())
    else:
        report["dlq_size"] = 0

    return report


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="memsync-bridge: extraction JSONL → Graphiti integration bridge (DC-208-5)",
    )
    parser.add_argument(
        "--extract-jsonl",
        nargs="+",
        help="Glob patterns or paths to EXTRACT-*.jsonl files to ingest",
    )
    parser.add_argument(
        "--graphiti-base",
        default=DEFAULT_GRAPHITI_BASE,
        help=f"Graphiti HTTP base URL (default: {DEFAULT_GRAPHITI_BASE})",
    )
    parser.add_argument(
        "--retry-db",
        default=DEFAULT_RETRY_DB,
        help=f"Path to SQLite retry queue (default: {DEFAULT_RETRY_DB})",
    )
    parser.add_argument(
        "--drain-retry",
        action="store_true",
        help="Drain the retry queue instead of ingesting new files",
    )
    parser.add_argument(
        "--max-attempts",
        type=int,
        default=200,
        help="Max records to process during drain (default: 200)",
    )
    parser.add_argument(
        "--health",
        action="store_true",
        help="Print health report and exit",
    )
    parser.add_argument(
        "--dlq-path",
        default=DEFAULT_DLQ_PATH,
        help=f"Dead-letter queue JSONL path (default: {DEFAULT_DLQ_PATH})",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    if args.health:
        report = health_report(args.retry_db, args.dlq_path)
        print(json.dumps(report, indent=2))
        return

    if args.drain_retry:
        log.info("Draining retry queue: %s (max=%d)", args.retry_db, args.max_attempts)
        result = drain_retry_queue(args.retry_db, args.graphiti_base, args.max_attempts)
        log.info(
            "Drain complete: succeeded=%d retried=%d dead_lettered=%d remaining=%d",
            result.succeeded, result.retried, result.dead_lettered, result.remaining,
        )
        return

    if not args.extract_jsonl:
        parser.error("Either --extract-jsonl or --drain-retry or --health is required")

    # Expand globs
    files: List[str] = []
    for pattern in args.extract_jsonl:
        expanded = globmod.glob(pattern)
        if expanded:
            files.extend(sorted(expanded))
        else:
            # Treat as literal path
            files.append(pattern)

    if not files:
        log.warning("No files matched the provided patterns")
        return

    # Ingest all files
    all_records: List[Any] = []
    for fpath in files:
        records = ingest_extraction_jsonl(fpath)
        all_records.extend(records)

    if not all_records:
        log.info("No valid records found across %d files", len(files))
        return

    log.info("Total records to enqueue: %d from %d files", len(all_records), len(files))

    # Enqueue
    result = enqueue_for_graphiti(all_records, args.retry_db, args.graphiti_base)
    log.info(
        "Enqueue complete: sent=%d skipped_dup=%d skipped_invalid=%d errors=%d",
        result.enqueued, result.skipped_duplicate, result.skipped_invalid, len(result.errors),
    )
    for err in result.errors:
        log.error("  %s", err)


if __name__ == "__main__":
    main()
