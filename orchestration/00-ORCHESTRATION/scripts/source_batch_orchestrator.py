#!/usr/bin/env python3
"""
source_batch_orchestrator.py — DC-208-4 Batch Orchestrator

Runs atomic extraction across the full source corpus using the proven
source_extract.py pipeline. Reads triage results, batches sources by
token budget, runs extraction with concurrency control, checkpoints
progress for resume, and produces a final report.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import signal
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

log = logging.getLogger("batch_orchestrator")

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class SourceRecord:
    source_id: str
    filename: str
    total: float
    rank: int
    signal_tier: str
    topics: list[str]
    line_count: int = 0       # populated during planning
    token_estimate: int = 0   # line_count * 1.3


@dataclass
class Batch:
    batch_id: int
    sources: list[SourceRecord]
    total_token_estimate: int = 0


@dataclass
class SourceResult:
    source_id: str
    status: str               # "OK", "FAILED", "SKIPPED"
    atoms_extracted: int = 0
    duration_s: float = 0.0
    error: str = ""


@dataclass
class BatchResult:
    batch_id: int
    source_results: list[SourceResult] = field(default_factory=list)
    duration_s: float = 0.0


# ---------------------------------------------------------------------------
# Graceful shutdown
# ---------------------------------------------------------------------------

_shutdown_requested = False


def _signal_handler(signum: int, frame: object) -> None:
    global _shutdown_requested
    log.warning("Signal %d received — finishing current batch then exiting", signum)
    _shutdown_requested = True


signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)

# ---------------------------------------------------------------------------
# Triage loading
# ---------------------------------------------------------------------------

def load_triage(path: Path, source_dir: Path) -> list[SourceRecord]:
    """Load DYN-SOURCE_TRIAGE.json, sort by triage score descending."""
    with open(path) as f:
        data = json.load(f)

    records: list[SourceRecord] = []
    for r in data["records"]:
        rec = SourceRecord(
            source_id=r["source_id"],
            filename=r["filename"],
            total=r["total"],
            rank=r["rank"],
            signal_tier=r.get("signal_tier", "unknown"),
            topics=r.get("topics", []),
        )
        # Compute line count from actual file
        src_path = source_dir / rec.filename
        if src_path.is_file():
            rec.line_count = sum(1 for _ in open(src_path, errors="replace"))
            rec.token_estimate = int(rec.line_count * 1.3)
        else:
            log.warning("Source file missing: %s", src_path)
            rec.line_count = 0
            rec.token_estimate = 0
        records.append(rec)

    records.sort(key=lambda r: r.total, reverse=True)
    log.info("Loaded %d source records from triage", len(records))
    return records


# ---------------------------------------------------------------------------
# Batch planning
# ---------------------------------------------------------------------------

def plan_batches(
    sources: list[SourceRecord],
    batch_size: int = 10,
    max_tokens_per_batch: int = 50_000,
) -> list[Batch]:
    """Group sources into batches respecting token budget.

    Large sources (>3000 lines) get their own batch to avoid budget blowout.
    """
    LARGE_THRESHOLD = 3000  # lines

    batches: list[Batch] = []
    batch_id = 0
    current_sources: list[SourceRecord] = []
    current_tokens = 0
    has_large = False

    for src in sources:
        is_large = src.line_count > LARGE_THRESHOLD

        # Large source gets its own batch
        if is_large:
            # Flush current batch first
            if current_sources:
                batches.append(Batch(
                    batch_id=batch_id,
                    sources=current_sources,
                    total_token_estimate=current_tokens,
                ))
                batch_id += 1
                current_sources = []
                current_tokens = 0
                has_large = False

            batches.append(Batch(
                batch_id=batch_id,
                sources=[src],
                total_token_estimate=src.token_estimate,
            ))
            batch_id += 1
            continue

        # Would adding this source exceed budget or batch size?
        would_exceed_tokens = (current_tokens + src.token_estimate) > max_tokens_per_batch
        would_exceed_size = len(current_sources) >= batch_size

        if current_sources and (would_exceed_tokens or would_exceed_size):
            batches.append(Batch(
                batch_id=batch_id,
                sources=current_sources,
                total_token_estimate=current_tokens,
            ))
            batch_id += 1
            current_sources = []
            current_tokens = 0
            has_large = False

        current_sources.append(src)
        current_tokens += src.token_estimate

    # Flush remainder
    if current_sources:
        batches.append(Batch(
            batch_id=batch_id,
            sources=current_sources,
            total_token_estimate=current_tokens,
        ))

    log.info("Planned %d batches from %d sources", len(batches), len(sources))
    return batches


# ---------------------------------------------------------------------------
# Checkpointing
# ---------------------------------------------------------------------------

def checkpoint(
    source_id: str,
    status: str,
    atoms_extracted: int,
    duration_s: float,
    error: str,
    checkpoint_file: Path,
) -> None:
    """Append one record to DYN-BATCH_CHECKPOINTS.jsonl."""
    record = {
        "source_id": source_id,
        "status": status,
        "atoms_extracted": atoms_extracted,
        "duration_s": round(duration_s, 2),
        "error": error,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    checkpoint_file.parent.mkdir(parents=True, exist_ok=True)
    with open(checkpoint_file, "a") as f:
        f.write(json.dumps(record) + "\n")


def load_checkpoints(checkpoint_file: Path) -> set[str]:
    """Load already-completed source IDs (OK or SKIPPED) for resume."""
    completed: set[str] = set()
    if not checkpoint_file.is_file():
        return completed
    with open(checkpoint_file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                if rec.get("status") in ("OK", "SKIPPED"):
                    completed.add(rec["source_id"])
            except json.JSONDecodeError:
                continue
    log.info("Loaded %d completed source IDs from checkpoint", len(completed))
    return completed


# ---------------------------------------------------------------------------
# Extraction runner (single source)
# ---------------------------------------------------------------------------

_ATOM_COUNT_RE = re.compile(r"Final:\s*(\d+)\s*atoms")


def _run_one_source(
    source: SourceRecord,
    extract_script: Path,
    source_dir: Path,
    out_dir: Path,
    env_vars: dict[str, str],
    checkpoint_file: Path,
    max_retries: int = 2,
    retry_delay: float = 30.0,
) -> SourceResult:
    """Run extraction subprocess for a single source with retry logic."""
    src_path = source_dir / source.filename
    if not src_path.is_file():
        result = SourceResult(source.source_id, "SKIPPED", error="file not found")
        checkpoint(source.source_id, "SKIPPED", 0, 0.0, result.error, checkpoint_file)
        return result

    cmd = [
        sys.executable, str(extract_script),
        "--source", str(src_path),
        "--out-dir", str(out_dir),
        "--verbose",
    ]

    env = {**os.environ, **env_vars}
    attempts = 0
    last_error = ""

    while attempts < max_retries:
        attempts += 1
        t0 = time.monotonic()
        try:
            proc = subprocess.run(
                cmd, env=env, capture_output=True, text=True, timeout=600,
            )
            elapsed = time.monotonic() - t0

            if proc.returncode == 0:
                # Parse atom count from stderr (logging goes to stderr)
                atoms = 0
                combined = proc.stderr + proc.stdout
                m = _ATOM_COUNT_RE.search(combined)
                if m:
                    atoms = int(m.group(1))
                result = SourceResult(source.source_id, "OK", atoms, elapsed)
                checkpoint(source.source_id, "OK", atoms, elapsed, "", checkpoint_file)
                return result
            else:
                last_error = (proc.stderr or proc.stdout or "")[-500:]
                log.warning(
                    "Extraction failed for %s (attempt %d/%d, rc=%d): %s",
                    source.source_id, attempts, max_retries, proc.returncode,
                    last_error[:200],
                )
                if attempts < max_retries:
                    log.info("Waiting %.0fs before retry...", retry_delay)
                    time.sleep(retry_delay)

        except subprocess.TimeoutExpired:
            elapsed = time.monotonic() - t0
            last_error = "timeout (600s)"
            log.warning("Extraction timed out for %s (attempt %d/%d)",
                        source.source_id, attempts, max_retries)
            if attempts < max_retries:
                time.sleep(retry_delay)

    # All retries exhausted
    result = SourceResult(source.source_id, "FAILED", 0, 0.0, last_error[:500])
    checkpoint(source.source_id, "FAILED", 0, 0.0, last_error[:500], checkpoint_file)
    return result


# ---------------------------------------------------------------------------
# Batch runner
# ---------------------------------------------------------------------------

def run_batch(
    batch: Batch,
    extract_script: Path,
    source_dir: Path,
    out_dir: Path,
    env_vars: dict[str, str],
    checkpoint_file: Path,
) -> BatchResult:
    """Run extraction on each source in a batch sequentially."""
    t0 = time.monotonic()
    br = BatchResult(batch_id=batch.batch_id)

    for src in batch.sources:
        if _shutdown_requested:
            log.warning("Shutdown requested — skipping remaining sources in batch %d", batch.batch_id)
            break
        sr = _run_one_source(src, extract_script, source_dir, out_dir, env_vars, checkpoint_file)
        br.source_results.append(sr)
        log.info("  %s: %s (%d atoms, %.1fs)", src.source_id, sr.status, sr.atoms_extracted, sr.duration_s)

    br.duration_s = time.monotonic() - t0
    return br


def run_all(
    batches: list[Batch],
    extract_script: Path,
    source_dir: Path,
    out_dir: Path,
    env_vars: dict[str, str],
    checkpoint_file: Path,
    max_concurrency: int = 4,
) -> list[BatchResult]:
    """Run batches with ProcessPoolExecutor, respecting concurrency cap."""
    total_sources = sum(len(b.sources) for b in batches)
    completed_sources = 0
    total_atoms = 0
    results: list[BatchResult] = []

    # For subprocess-based work, ProcessPoolExecutor is used per the spec.
    # Each worker runs one batch (sequential sources within the batch).
    with ProcessPoolExecutor(max_workers=max_concurrency) as executor:
        future_to_batch = {}
        for batch in batches:
            if _shutdown_requested:
                break
            fut = executor.submit(
                run_batch, batch, extract_script, source_dir, out_dir, env_vars, checkpoint_file,
            )
            future_to_batch[fut] = batch

        for fut in as_completed(future_to_batch):
            if _shutdown_requested:
                break
            batch = future_to_batch[fut]
            try:
                br = fut.result()
            except Exception as exc:
                log.error("Batch %d raised exception: %s", batch.batch_id, exc)
                br = BatchResult(batch_id=batch.batch_id)
            results.append(br)

            batch_atoms = sum(sr.atoms_extracted for sr in br.source_results)
            completed_sources += len(br.source_results)
            total_atoms += batch_atoms
            log.info(
                "Batch %d/%d: %d/%d sources complete, %d atoms extracted",
                len(results), len(batches), completed_sources, total_sources, total_atoms,
            )

    results.sort(key=lambda r: r.batch_id)
    return results


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def report(results: list[BatchResult], out_path: Path) -> None:
    """Write DYN-BATCH_REPORT.md with summary statistics."""
    total_sources = sum(len(br.source_results) for br in results)
    ok = sum(1 for br in results for sr in br.source_results if sr.status == "OK")
    failed = sum(1 for br in results for sr in br.source_results if sr.status == "FAILED")
    skipped = sum(1 for br in results for sr in br.source_results if sr.status == "SKIPPED")
    total_atoms = sum(sr.atoms_extracted for br in results for sr in br.source_results)
    total_time = sum(br.duration_s for br in results)

    # Top extractors
    all_sr = [(sr.source_id, sr.atoms_extracted, sr.duration_s)
              for br in results for sr in br.source_results if sr.status == "OK"]
    all_sr.sort(key=lambda x: x[1], reverse=True)
    top_10 = all_sr[:10]

    # Failures
    failures = [(sr.source_id, sr.error[:120])
                for br in results for sr in br.source_results if sr.status == "FAILED"]

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"# DYN-BATCH_REPORT",
        f"",
        f"**Generated**: {ts}",
        f"**Batches**: {len(results)}",
        f"**Sources processed**: {total_sources}",
        f"**Successful**: {ok}",
        f"**Failed**: {failed}",
        f"**Skipped**: {skipped}",
        f"**Total atoms extracted**: {total_atoms:,}",
        f"**Wall-clock time (sum of batches)**: {total_time:.0f}s ({total_time/3600:.1f}h)",
        f"",
        f"## Top Extractors",
        f"",
        f"| Rank | Source ID | Atoms | Time (s) |",
        f"|------|-----------|-------|----------|",
    ]
    for i, (sid, atoms, dur) in enumerate(top_10, 1):
        lines.append(f"| {i} | {sid} | {atoms} | {dur:.1f} |")

    if failures:
        lines.extend([
            f"",
            f"## Failures ({len(failures)})",
            f"",
            f"| Source ID | Error |",
            f"|-----------|-------|",
        ])
        for sid, err in failures:
            lines.append(f"| {sid} | {err} |")

    lines.append("")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines))
    log.info("Report written to %s", out_path)


# ---------------------------------------------------------------------------
# Batch plan persistence
# ---------------------------------------------------------------------------

def save_batch_plan(batches: list[Batch], path: Path) -> None:
    """Write DYN-BATCH_PLAN.json."""
    plan = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_batches": len(batches),
        "total_sources": sum(len(b.sources) for b in batches),
        "batches": [
            {
                "batch_id": b.batch_id,
                "source_count": len(b.sources),
                "token_estimate": b.total_token_estimate,
                "source_ids": [s.source_id for s in b.sources],
            }
            for b in batches
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(plan, f, indent=2)
    log.info("Batch plan written to %s", path)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="DC-208-4 Batch Orchestrator — run extraction across full source corpus.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--triage", type=Path, required=True,
                        help="Path to DYN-SOURCE_TRIAGE.json")
    parser.add_argument("--source-dir", type=Path, required=True,
                        help="Directory containing SOURCE-*.md files")
    parser.add_argument("--out-dir", type=Path, required=True,
                        help="Output directory for batch artifacts")
    parser.add_argument("--extract-script", type=Path, required=True,
                        help="Path to source_extract.py")
    parser.add_argument("--batch-size", type=int, default=10,
                        help="Max sources per batch (default: 10)")
    parser.add_argument("--max-concurrency", type=int, default=4,
                        help="Max parallel batches (default: 4)")
    parser.add_argument("--max-tokens-per-batch", type=int, default=50_000,
                        help="Token budget per batch (default: 50000)")
    parser.add_argument("--resume", action="store_true",
                        help="Resume from checkpoint, skipping completed sources")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Enable debug logging")

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    # Validate inputs
    if not args.triage.is_file():
        log.error("Triage file not found: %s", args.triage)
        sys.exit(1)
    if not args.source_dir.is_dir():
        log.error("Source directory not found: %s", args.source_dir)
        sys.exit(1)
    if not args.extract_script.is_file():
        log.error("Extract script not found: %s", args.extract_script)
        sys.exit(1)

    args.out_dir.mkdir(parents=True, exist_ok=True)

    # Checkpoint paths
    checkpoint_file = args.out_dir / "DYN-BATCH_CHECKPOINTS.jsonl"
    plan_path = args.out_dir / "DYN-BATCH_PLAN.json"
    report_path = args.out_dir / "DYN-BATCH_REPORT.md"

    # Environment variables for extraction subprocess
    env_vars: dict[str, str] = {
        "LLM_BACKEND": "openrouter",
        "OPENROUTER_MODEL": "google/gemini-2.5-flash",
        "KMP_DUPLICATE_LIB_OK": "TRUE",
    }
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if api_key:
        env_vars["OPENROUTER_API_KEY"] = api_key
    else:
        log.warning("OPENROUTER_API_KEY not set — extraction will likely fail")

    # Load triage
    sources = load_triage(args.triage, args.source_dir)
    if not sources:
        log.error("No sources loaded from triage")
        sys.exit(1)

    # Resume: filter out completed sources
    if args.resume:
        completed = load_checkpoints(checkpoint_file)
        before = len(sources)
        sources = [s for s in sources if s.source_id not in completed]
        log.info("Resume: %d already done, %d remaining", before - len(sources), len(sources))
        if not sources:
            log.info("All sources already completed — nothing to do")
            sys.exit(0)

    # Plan batches
    batches = plan_batches(sources, args.batch_size, args.max_tokens_per_batch)
    save_batch_plan(batches, plan_path)

    # Run
    log.info("Starting extraction: %d batches, %d sources, concurrency=%d",
             len(batches), sum(len(b.sources) for b in batches), args.max_concurrency)

    results = run_all(
        batches,
        extract_script=args.extract_script,
        source_dir=args.source_dir,
        out_dir=args.out_dir,
        env_vars=env_vars,
        checkpoint_file=checkpoint_file,
        max_concurrency=args.max_concurrency,
    )

    # Report
    report(results, report_path)

    # Summary
    ok = sum(1 for br in results for sr in br.source_results if sr.status == "OK")
    failed = sum(1 for br in results for sr in br.source_results if sr.status == "FAILED")
    atoms = sum(sr.atoms_extracted for br in results for sr in br.source_results)
    log.info("DONE — %d OK, %d FAILED, %d atoms extracted", ok, failed, atoms)

    if _shutdown_requested:
        log.warning("Run was interrupted — use --resume to continue")
        sys.exit(130)


if __name__ == "__main__":
    main()
