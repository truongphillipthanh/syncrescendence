#!/usr/bin/env python3
"""
source_extract_validate.py — Schema validator for extracted atom JSONL files.

DC-208-2: Source Mining Pipeline — Component 2 (Validation)

Validates each atom in an EXTRACT-*.jsonl file against the canonical atom schema.
Reports per-atom errors and aggregate reject rates.

Dependencies: jsonschema
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft7Validator, ValidationError
except ImportError:
    print("ERROR: jsonschema is required. Install with: pip install jsonschema", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Canonical atom JSON schema
# ---------------------------------------------------------------------------

ATOM_SCHEMA: dict[str, Any] = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": [
        "atom_id",
        "source_id",
        "category",
        "content",
        "line_start",
        "line_end",
        "chaperone",
    ],
    "properties": {
        "atom_id": {
            "type": "string",
            "pattern": r"^ATOM-.+-\d{4}$",
        },
        "source_id": {
            "type": "string",
            "minLength": 1,
        },
        "category": {
            "type": "string",
            "enum": [
                "claim",
                "framework",
                "prediction",
                "concept",
                "analogy",
                "praxis_hook",
            ],
        },
        "content": {
            "type": "string",
            "minLength": 10,
        },
        "line_start": {
            "type": "integer",
            "minimum": 1,
        },
        "line_end": {
            "type": "integer",
            "minimum": 1,
        },
        "chaperone": {
            "type": "object",
            "required": [
                "context_type",
                "argument_role",
                "tension_vector",
            ],
            "properties": {
                "context_type": {
                    "type": "string",
                    "enum": [
                        "hypothesis",
                        "rebuttal",
                        "consensus",
                        "speculation",
                        "anecdote",
                        "method",
                    ],
                },
                "argument_role": {
                    "type": "string",
                    "enum": [
                        "claim",
                        "evidence",
                        "counterevidence",
                        "limitation",
                    ],
                },
                "tension_vector": {
                    "type": "array",
                    "items": {
                        "type": "number",
                        "minimum": 0.0,
                        "maximum": 1.0,
                    },
                    "minItems": 6,
                    "maxItems": 6,
                },
                "opposes_atom_ids": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
        },
        "extensions": {
            "type": "object",
        },
    },
}

_VALIDATOR = Draft7Validator(ATOM_SCHEMA)


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass
class AtomValidationResult:
    atom_id: str
    line_number: int  # line in JSONL file
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


@dataclass
class FileValidationReport:
    path: Path
    total_atoms: int = 0
    valid_atoms: int = 0
    rejected_atoms: int = 0
    warnings_count: int = 0
    results: list[AtomValidationResult] = field(default_factory=list)

    @property
    def reject_rate(self) -> float:
        if self.total_atoms == 0:
            return 0.0
        return self.rejected_atoms / self.total_atoms


# ---------------------------------------------------------------------------
# Semantic validation (beyond schema)
# ---------------------------------------------------------------------------


def semantic_validate(atom: dict) -> tuple[list[str], list[str]]:
    """Apply semantic validation rules beyond JSON schema.

    Returns (errors, warnings).
    """
    errors: list[str] = []
    warnings: list[str] = []

    # Rule: claims must have argument_role and should ideally have counterpoint info
    category = atom.get("category", "")
    chaperone = atom.get("chaperone", {})
    argument_role = chaperone.get("argument_role", "")

    if category == "claim" and not argument_role:
        errors.append("Claim atom missing argument_role in chaperone")

    # Rule: line_end >= line_start
    ls = atom.get("line_start", 0)
    le = atom.get("line_end", 0)
    if le < ls:
        errors.append(f"line_end ({le}) < line_start ({ls})")

    # Rule: predictions should have speculation_risk > 0
    if category == "prediction":
        tv = chaperone.get("tension_vector", [0] * 6)
        if len(tv) >= 4 and tv[3] <= 0.0:
            warnings.append("Prediction atom has speculation_risk=0.0")

    # Rule: praxis_hook should have actionability > 0
    if category == "praxis_hook":
        tv = chaperone.get("tension_vector", [0] * 6)
        if len(tv) >= 5 and tv[4] <= 0.0:
            warnings.append("Praxis hook atom has actionability=0.0")

    # Rule: content should not be trivially short
    content = atom.get("content", "")
    if len(content) < 20:
        warnings.append(f"Content suspiciously short ({len(content)} chars)")

    return errors, warnings


# ---------------------------------------------------------------------------
# Core validation
# ---------------------------------------------------------------------------


def validate_atom(atom: dict, line_number: int) -> AtomValidationResult:
    """Validate a single atom dict against schema + semantic rules."""
    atom_id = atom.get("atom_id", f"<unknown-line-{line_number}>")
    errors: list[str] = []
    warnings: list[str] = []

    # Schema validation
    for error in _VALIDATOR.iter_errors(atom):
        errors.append(f"Schema: {error.message} (path: {'.'.join(str(p) for p in error.absolute_path)})")

    # Semantic validation
    sem_errors, sem_warnings = semantic_validate(atom)
    errors.extend(sem_errors)
    warnings.extend(sem_warnings)

    return AtomValidationResult(
        atom_id=atom_id,
        line_number=line_number,
        valid=len(errors) == 0,
        errors=errors,
        warnings=warnings,
    )


def validate_jsonl_file(path: Path) -> FileValidationReport:
    """Validate all atoms in a JSONL file."""
    report = FileValidationReport(path=path)

    if not path.exists():
        logging.error("File not found: %s", path)
        return report

    with open(path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            report.total_atoms += 1

            try:
                atom = json.loads(line)
            except json.JSONDecodeError as e:
                result = AtomValidationResult(
                    atom_id=f"<parse-error-line-{line_num}>",
                    line_number=line_num,
                    valid=False,
                    errors=[f"JSON parse error: {e}"],
                )
                report.results.append(result)
                report.rejected_atoms += 1
                continue

            result = validate_atom(atom, line_num)
            report.results.append(result)

            if result.valid:
                report.valid_atoms += 1
            else:
                report.rejected_atoms += 1

            report.warnings_count += len(result.warnings)

    return report


# ---------------------------------------------------------------------------
# Report printer
# ---------------------------------------------------------------------------


def print_report(report: FileValidationReport) -> None:
    """Print validation report to stdout."""
    log = logging.getLogger("validate")

    print(f"\n{'=' * 60}")
    print(f"Validation Report: {report.path.name}")
    print(f"{'=' * 60}")
    print(f"Total atoms:    {report.total_atoms}")
    print(f"Valid:          {report.valid_atoms}")
    print(f"Rejected:       {report.rejected_atoms}")
    print(f"Warnings:       {report.warnings_count}")
    print(f"Reject rate:    {report.reject_rate:.1%}")

    if report.reject_rate > 0.15:
        print(f"\n*** WARNING: Reject rate {report.reject_rate:.1%} exceeds 15% threshold ***")

    # Print errors
    error_results = [r for r in report.results if not r.valid]
    if error_results:
        print(f"\n--- Rejected Atoms ({len(error_results)}) ---")
        for r in error_results:
            print(f"\n  [{r.atom_id}] (JSONL line {r.line_number})")
            for e in r.errors:
                print(f"    ERROR: {e}")
            for w in r.warnings:
                print(f"    WARN:  {w}")

    # Print warnings for valid atoms
    warn_results = [r for r in report.results if r.valid and r.warnings]
    if warn_results:
        print(f"\n--- Warnings on Valid Atoms ({len(warn_results)}) ---")
        for r in warn_results:
            print(f"\n  [{r.atom_id}] (JSONL line {r.line_number})")
            for w in r.warnings:
                print(f"    WARN:  {w}")

    print(f"\n{'=' * 60}\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate extracted atom JSONL files against canonical schema.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--jsonl",
        type=Path,
        required=True,
        nargs="+",
        help="Path(s) to EXTRACT-*.jsonl file(s)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with error code if any atom is rejected",
    )
    parser.add_argument(
        "--warn-threshold",
        type=float,
        default=0.15,
        help="Reject rate threshold for warning (default: 0.15 = 15%%)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable debug logging",
    )

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    any_failures = False
    any_high_reject = False

    for jsonl_path in args.jsonl:
        report = validate_jsonl_file(jsonl_path)
        print_report(report)

        if report.rejected_atoms > 0:
            any_failures = True
        if report.reject_rate > args.warn_threshold:
            any_high_reject = True

    if args.strict and any_failures:
        sys.exit(1)
    if any_high_reject:
        sys.exit(2)


if __name__ == "__main__":
    main()
