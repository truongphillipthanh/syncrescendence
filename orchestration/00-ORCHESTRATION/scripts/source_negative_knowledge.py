#!/usr/bin/env python3
"""DC-208-8: Negative Knowledge Store for the Syncrescendence mining pipeline.

Records failed hypotheses, methods, and query patterns as FAILED_PATH edges
with mandatory context scoping, confidence decay, and rehabilitation support.

Anti-bias protections:
  - Never hard-blocks; failures are ranking penalties ONLY
  - Decay half-life on all failure edges
  - 5% scheduled retest of negative-marked paths
  - Requires context_scope — no global blanket failures
  - Explicit REHABILITATED_PATH counter-edges override failures

Data flow:
  - Integrates with memsync via record_type="failure_pheromone"
  - Persists to sources/04-SOURCES/_meta/DYN-NEGATIVE_KNOWLEDGE.jsonl (append-only)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import math
import os
import random
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger("negative_knowledge")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

VALID_FAILURE_CLASSES = frozenset({
    "contradiction",
    "low_evidence",
    "non_reproducible",
    "scope_mismatch",
    "obsolete",
})

GRAPH_EDGE_TYPE = "FAILED_PATH"
GRAPH_REHAB_EDGE_TYPE = "REHABILITATED_PATH"
MEMSYNC_RECORD_TYPE = "failure_pheromone"

# Repo-relative default JSONL path
_REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_JSONL = _REPO_ROOT / "sources" / "04-SOURCES" / "_meta" / "DYN-NEGATIVE_KNOWLEDGE.jsonl"


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _make_failure_id(source_id: str, hypothesis_id: str, context_scope: str) -> str:
    digest = hashlib.sha256(
        f"{source_id}{hypothesis_id}{context_scope}".encode()
    ).hexdigest()[:12]
    return f"FAIL-{digest}"


def _make_rehab_id(failure_id: str, evidence: str) -> str:
    digest = hashlib.sha256(
        f"{failure_id}{evidence}".encode()
    ).hexdigest()[:12]
    return f"REHAB-{digest}"


@dataclass
class FailureRecord:
    failure_id: str
    source_id: str
    hypothesis_id: str
    failure_class: str
    confidence: float
    context_scope: str
    evidence: str
    created_at: str
    expires_at: Optional[str] = None
    retest_after: Optional[str] = None
    decayed_confidence: Optional[float] = None
    rehabilitated: bool = False
    record_kind: str = field(default="failure", init=False)

    def __post_init__(self) -> None:
        if self.failure_class not in VALID_FAILURE_CLASSES:
            raise ValueError(
                f"Invalid failure_class '{self.failure_class}'. "
                f"Must be one of: {', '.join(sorted(VALID_FAILURE_CLASSES))}"
            )
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(f"Confidence must be 0-1, got {self.confidence}")
        if not self.context_scope or self.context_scope.strip() == "":
            raise ValueError("context_scope is required — no global blanket failures")
        if self.decayed_confidence is None:
            self.decayed_confidence = self.confidence


@dataclass
class RehabilitationRecord:
    rehab_id: str
    failure_id: str
    evidence: str
    rehabilitated_by: str
    created_at: str
    record_kind: str = field(default="rehabilitation", init=False)


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------

def record_failure(
    source_id: str,
    hypothesis_id: str,
    failure_class: str,
    confidence: float,
    context_scope: str,
    evidence: str,
    expires_days: Optional[int] = None,
    retest_days: Optional[int] = None,
) -> FailureRecord:
    """Create a new FailureRecord and return it."""
    now = datetime.now(timezone.utc)
    failure_id = _make_failure_id(source_id, hypothesis_id, context_scope)

    expires_at = None
    if expires_days is not None:
        expires_at = (now + timedelta(days=expires_days)).isoformat()

    retest_after = None
    if retest_days is not None:
        retest_after = (now + timedelta(days=retest_days)).isoformat()

    rec = FailureRecord(
        failure_id=failure_id,
        source_id=source_id,
        hypothesis_id=hypothesis_id,
        failure_class=failure_class,
        confidence=confidence,
        context_scope=context_scope,
        evidence=evidence,
        created_at=now.isoformat(),
        expires_at=expires_at,
        retest_after=retest_after,
    )
    return rec


def record_rehabilitation(
    failure_id: str,
    evidence: str,
    rehabilitated_by: str,
) -> RehabilitationRecord:
    """Create a RehabilitationRecord for an existing failure."""
    rehab_id = _make_rehab_id(failure_id, evidence)
    return RehabilitationRecord(
        rehab_id=rehab_id,
        failure_id=failure_id,
        evidence=evidence,
        rehabilitated_by=rehabilitated_by,
        created_at=_now_iso(),
    )


def load_negative_knowledge(jsonl_path: Path) -> list[FailureRecord]:
    """Load all FailureRecords from the JSONL file, applying rehabilitations."""
    if not jsonl_path.exists():
        return []

    failures: dict[str, FailureRecord] = {}
    rehab_ids: set[str] = set()

    with open(jsonl_path, "r", encoding="utf-8") as fh:
        for line_num, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                logger.warning("Skipping malformed JSON at line %d", line_num)
                continue

            kind = obj.get("record_kind")
            if kind == "failure":
                rec = FailureRecord(**{
                    k: v for k, v in obj.items() if k != "record_kind"
                })
                failures[rec.failure_id] = rec
            elif kind == "rehabilitation":
                rehab_ids.add(obj["failure_id"])

    # Mark rehabilitated failures
    for fid in rehab_ids:
        if fid in failures:
            failures[fid].rehabilitated = True

    return list(failures.values())


def query_failures(
    context_scope: str,
    active_only: bool = True,
    jsonl_path: Optional[Path] = None,
) -> list[FailureRecord]:
    """Query failures matching a context_scope prefix."""
    path = jsonl_path or DEFAULT_JSONL
    records = load_negative_knowledge(path)
    now = datetime.now(timezone.utc)

    results = []
    for rec in records:
        # Prefix match on context_scope
        if not rec.context_scope.startswith(context_scope):
            continue
        if active_only:
            if rec.rehabilitated:
                continue
            if rec.expires_at:
                try:
                    exp = datetime.fromisoformat(rec.expires_at)
                    if exp <= now:
                        continue
                except ValueError:
                    pass
        results.append(rec)

    return results


def apply_decay(
    records: list[FailureRecord],
    half_life_days: float = 90.0,
) -> list[FailureRecord]:
    """Apply exponential decay to confidence based on age. Mutates and returns records."""
    now = datetime.now(timezone.utc)
    for rec in records:
        try:
            created = datetime.fromisoformat(rec.created_at)
        except ValueError:
            continue
        age_days = (now - created).total_seconds() / 86400.0
        decay_factor = math.pow(0.5, age_days / half_life_days)
        rec.decayed_confidence = round(rec.confidence * decay_factor, 6)
    return records


def select_retest_candidates(
    records: list[FailureRecord],
    pct: float = 0.05,
) -> list[FailureRecord]:
    """Select ~pct of active (non-rehabilitated) failures for retesting.

    Prioritises records past their retest_after date, then fills remaining
    quota randomly from the rest.
    """
    now = datetime.now(timezone.utc)
    active = []
    for r in records:
        if r.rehabilitated:
            continue
        if r.expires_at is not None:
            try:
                if datetime.fromisoformat(r.expires_at) < now:
                    continue
            except ValueError:
                pass
        active.append(r)
    if not active:
        return []

    n = max(1, int(len(active) * pct))

    # Prioritise records past retest_after
    due = []
    rest = []
    for rec in active:
        if rec.retest_after:
            try:
                rt = datetime.fromisoformat(rec.retest_after)
                if rt <= now:
                    due.append(rec)
                    continue
            except ValueError:
                pass
        rest.append(rec)

    selected = due[:n]
    if len(selected) < n and rest:
        remaining = n - len(selected)
        selected.extend(random.sample(rest, min(remaining, len(rest))))

    return selected


def to_memsync_record(failure: FailureRecord) -> dict:
    """Convert a FailureRecord to a memsync-compatible FailurePheromoneRecord dict."""
    # Deterministic UUID from failure_id
    uuid = hashlib.sha256(failure.failure_id.encode()).hexdigest()[:32]
    confidence = failure.decayed_confidence if failure.decayed_confidence is not None else failure.confidence
    return {
        "record_type": MEMSYNC_RECORD_TYPE,
        "schema_version": "1.0.0",
        "uuid": uuid,
        "timestamp": failure.created_at,
        "source_id": failure.source_id,
        "stage": failure.failure_class,
        "error": failure.evidence,
        "severity": "warning",
        "metadata": {
            "failure_id": failure.failure_id,
            "hypothesis_id": failure.hypothesis_id,
            "confidence": confidence,
            "context_scope": failure.context_scope,
            "expires_at": failure.expires_at,
            "retest_after": failure.retest_after,
            "rehabilitated": failure.rehabilitated,
        },
    }


def to_graphiti_edge(failure: FailureRecord) -> dict:
    """Convert a FailureRecord to a Graphiti FAILED_PATH edge format."""
    edge_type = GRAPH_REHAB_EDGE_TYPE if failure.rehabilitated else GRAPH_EDGE_TYPE
    return {
        "edge_type": edge_type,
        "source_node": failure.hypothesis_id,
        "target_node": failure.failure_id,
        "metadata": {
            "failure_class": failure.failure_class,
            "confidence": failure.decayed_confidence if failure.decayed_confidence is not None else failure.confidence,
            "context_scope": failure.context_scope,
            "expires_at": failure.expires_at,
            "retest_after": failure.retest_after,
        },
        "evidence": failure.evidence,
        "source_id": failure.source_id,
        "created_at": failure.created_at,
    }


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------

def _append_jsonl(record: FailureRecord | RehabilitationRecord, jsonl_path: Path) -> None:
    """Append a single record to the JSONL file."""
    jsonl_path.parent.mkdir(parents=True, exist_ok=True)
    with open(jsonl_path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(asdict(record), default=str) + "\n")
    logger.info("Appended %s to %s", getattr(record, "failure_id", None) or getattr(record, "rehab_id", None), jsonl_path)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="source_negative_knowledge",
        description="Negative Knowledge Store — DC-208-8",
    )
    parser.add_argument(
        "--jsonl", type=Path, default=DEFAULT_JSONL,
        help=f"Path to JSONL store (default: {DEFAULT_JSONL})",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="Enable debug logging",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    # -- record --
    rec = sub.add_parser("record", help="Record a new failure")
    rec.add_argument("--source-id", required=True)
    rec.add_argument("--hypothesis-id", required=True)
    rec.add_argument(
        "--failure-class", required=True,
        choices=sorted(VALID_FAILURE_CLASSES),
    )
    rec.add_argument("--confidence", required=True, type=float)
    rec.add_argument("--context-scope", required=True)
    rec.add_argument("--evidence", required=True)
    rec.add_argument("--expires-days", type=int, default=None)
    rec.add_argument("--retest-days", type=int, default=None)

    # -- rehabilitate --
    reh = sub.add_parser("rehabilitate", help="Rehabilitate a failure")
    reh.add_argument("--failure-id", required=True)
    reh.add_argument("--evidence", required=True)
    reh.add_argument("--rehabilitated-by", required=True)

    # -- query --
    qry = sub.add_parser("query", help="Query active failures")
    qry.add_argument("--context-scope", required=True)
    qry.add_argument("--active-only", action="store_true", default=True)
    qry.add_argument("--include-rehabilitated", action="store_true")

    # -- retest --
    ret = sub.add_parser("retest", help="Select retest candidates")
    ret.add_argument("--pct", type=float, default=0.05)

    # -- decay --
    dec = sub.add_parser("decay", help="Apply decay and display results")
    dec.add_argument("--half-life-days", type=float, default=90.0)

    return parser


def _cmd_record(args: argparse.Namespace) -> int:
    rec = record_failure(
        source_id=args.source_id,
        hypothesis_id=args.hypothesis_id,
        failure_class=args.failure_class,
        confidence=args.confidence,
        context_scope=args.context_scope,
        evidence=args.evidence,
        expires_days=args.expires_days,
        retest_days=args.retest_days,
    )
    _append_jsonl(rec, args.jsonl)
    print(json.dumps(asdict(rec), indent=2, default=str))
    return 0


def _cmd_rehabilitate(args: argparse.Namespace) -> int:
    rec = record_rehabilitation(
        failure_id=args.failure_id,
        evidence=args.evidence,
        rehabilitated_by=args.rehabilitated_by,
    )
    _append_jsonl(rec, args.jsonl)
    print(json.dumps(asdict(rec), indent=2, default=str))
    return 0


def _cmd_query(args: argparse.Namespace) -> int:
    active_only = args.active_only and not args.include_rehabilitated
    results = query_failures(
        context_scope=args.context_scope,
        active_only=active_only,
        jsonl_path=args.jsonl,
    )
    for rec in results:
        print(json.dumps(asdict(rec), indent=2, default=str))
    logger.info("Found %d matching failure(s)", len(results))
    if not results:
        print("No matching failures found.")
    return 0


def _cmd_retest(args: argparse.Namespace) -> int:
    records = load_negative_knowledge(args.jsonl)
    candidates = select_retest_candidates(records, pct=args.pct)
    for rec in candidates:
        print(json.dumps(asdict(rec), indent=2, default=str))
    logger.info("Selected %d retest candidate(s) from %d records", len(candidates), len(records))
    if not candidates:
        print("No retest candidates.")
    return 0


def _cmd_decay(args: argparse.Namespace) -> int:
    records = load_negative_knowledge(args.jsonl)
    decayed = apply_decay(records, half_life_days=args.half_life_days)
    for rec in decayed:
        print(json.dumps(asdict(rec), indent=2, default=str))
    logger.info("Applied decay (half-life=%.1fd) to %d record(s)", args.half_life_days, len(decayed))
    if not decayed:
        print("No records to decay.")
    return 0


_DISPATCH = {
    "record": _cmd_record,
    "rehabilitate": _cmd_rehabilitate,
    "query": _cmd_query,
    "retest": _cmd_retest,
    "decay": _cmd_decay,
}


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    handler = _DISPATCH.get(args.command)
    if handler is None:
        parser.print_help()
        return 1
    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
