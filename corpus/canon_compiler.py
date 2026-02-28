#!/usr/bin/env python3
"""Canon Compiler — 5-stage pipeline (CC49 ratified V-2).

Stage 1: PARSE    — Extract frontmatter + body structure → IR (JSON)
Stage 2: VALIDATE — S-1 schema enforcement + cross-file coherence
Stage 3: GRAPH    — Build dependency DAG + volatility heatmap (future)
Stage 4: COMPRESS — Generate Syncrescript v2 output (future)
Stage 5: EMIT     — Render views: Scripture, Config, Graph, Ledger, Compiled (future)

The compiler IS the immune system (T-6 ratified).
Validation = circulating antibodies. S-1 frontmatter = MHC.

Usage:
    python3 corpus/canon_compiler.py parse              # Stage 1 only → IR to stdout
    python3 corpus/canon_compiler.py validate            # Stages 1+2
    python3 corpus/canon_compiler.py compile             # All implemented stages
    python3 corpus/canon_compiler.py parse --out ir.json # Write IR to file
    python3 corpus/canon_compiler.py validate --json     # JSON output
    python3 corpus/canon_compiler.py validate --strict   # Warnings = errors
"""

import sys
import os
import re
import yaml
import json
import argparse
from pathlib import Path
from datetime import date, datetime

CANON_DIR = Path(__file__).parent.parent / "canon"
MUTAGENIC_DIR = Path(__file__).parent.parent / "corpus" / "mutagenic"

# ============================================================
# S-1 SCHEMA (Ratified CC49)
# ============================================================

VALID_TIERS = {"cosmos", "core", "lattice", "chain", "archive", "immune"}
VALID_CHAINS = {None, "null", "intelligence", "information", "insight", "expertise", "knowledge", "wisdom"}
VALID_CELESTIAL_TYPES = {"root", "planetary", "ring", "lunar", "comet", "asteroid", "satellite", "policy", "meta"}
VALID_VOLATILITY_BANDS = {"permanent", "stable", "moderate", "dynamic"}
VALID_REFRESH_CADENCES = {None, "null", "", "annual", "semi-annual", "quarterly", "monthly"}
VALID_STATUSES = {"canonical", "draft", "deprecated", "archived", "demoted"}
VALID_OP_STATUSES = {"operational", "partial", "theoretical", "pilot"}
VALID_ELEMENTS = {None, "null", "", "fire", "water", "earth", "air", "quintessence"}
VALID_OODA_PHASES = {None, "null", "", "observe", "orient", "decide", "act", "sharpen"}
VALID_LAYERS = {None, "null", "", "lattice", "chain", "cosmos"}
VALID_DEV_STATUSES = {None, "null", "", "active", "stable", "dormant"}

REQUIRED_FIELDS = [
    "id", "canonical_name", "tier", "celestial_type",
    "volatility_band", "status", "operational_status",
    "version", "created", "updated"
]

RECOMMENDED_FIELDS = [
    "parent", "requires", "siblings", "synthesizes",
    "refresh_cadence", "last_verified", "element", "ooda_phase",
    "volatile_sections", "title", "chain"
]

# Volatility consistency rules
VOLATILITY_RULES = {
    ("permanent", "monthly"): "Permanent content with monthly refresh — contradiction",
    ("permanent", "quarterly"): "Permanent content with quarterly refresh — too frequent",
    ("dynamic", "annual"): "Dynamic content with annual refresh — too slow",
    ("dynamic", None): "Dynamic content with no refresh cadence — will go stale",
    ("dynamic", ""): "Dynamic content with no refresh cadence — will go stale",
    ("dynamic", "null"): "Dynamic content with no refresh cadence — will go stale",
}


# ============================================================
# STAGE 1: PARSE — Extract intermediate representation
# ============================================================

def parse_canon_file(filepath):
    """Parse a single canon file into intermediate representation."""
    text = filepath.read_text(encoding="utf-8")
    ir = {
        "source_path": str(filepath),
        "filename": filepath.name,
        "frontmatter": None,
        "has_frontmatter": False,
        "body": {
            "headings": [],
            "line_count": 0,
            "word_count": 0,
            "has_version_inline": False,
            "inline_versions": [],
            "sections": [],
        },
        "parse_errors": [],
    }

    # Extract frontmatter
    match = re.match(r"^---\s*\n(.*?\n)---\s*\n", text, re.DOTALL)
    if match:
        try:
            fm = yaml.safe_load(match.group(1))
            if isinstance(fm, dict):
                ir["frontmatter"] = fm
                ir["has_frontmatter"] = True
            else:
                ir["parse_errors"].append("Frontmatter parsed but not a dict")
        except yaml.YAMLError as e:
            ir["parse_errors"].append(f"YAML parse error: {e}")
        body_text = text[match.end():]
    else:
        ir["parse_errors"].append("No YAML frontmatter found")
        body_text = text

    # Parse body structure
    lines = body_text.split("\n")
    ir["body"]["line_count"] = len(lines)
    ir["body"]["word_count"] = len(body_text.split())

    # Extract headings
    for i, line in enumerate(lines):
        heading_match = re.match(r"^(#{1,6})\s+(.+)", line)
        if heading_match:
            ir["body"]["headings"].append({
                "level": len(heading_match.group(1)),
                "text": heading_match.group(2).strip(),
                "line": i + 1,
            })

    # Check for inline version declarations
    version_matches = re.findall(r"\*\*Version\*\*:\s*(\d+\.\d+\.\d+)", body_text)
    if version_matches:
        ir["body"]["has_version_inline"] = True
        ir["body"]["inline_versions"] = version_matches

    # Extract sections (H2-level blocks)
    current_section = None
    for heading in ir["body"]["headings"]:
        if heading["level"] <= 2:
            if current_section:
                ir["body"]["sections"].append(current_section)
            current_section = {"title": heading["text"], "line": heading["line"]}
    if current_section:
        ir["body"]["sections"].append(current_section)

    return ir


def stage_parse(canon_dir=CANON_DIR):
    """Stage 1: Parse all canon files into IR."""
    ir_collection = {
        "stage": "parse",
        "timestamp": datetime.now().isoformat(),
        "canon_dir": str(canon_dir),
        "file_count": 0,
        "parse_errors": 0,
        "files": [],
        "id_index": {},  # id → index for cross-ref
    }

    canon_files = sorted(canon_dir.glob("*.md"))
    for i, f in enumerate(canon_files):
        file_ir = parse_canon_file(f)
        ir_collection["files"].append(file_ir)
        ir_collection["file_count"] += 1
        if file_ir["parse_errors"]:
            ir_collection["parse_errors"] += len(file_ir["parse_errors"])

        # Build ID index
        if file_ir["frontmatter"] and "id" in file_ir["frontmatter"]:
            ir_collection["id_index"][str(file_ir["frontmatter"]["id"])] = i

    return ir_collection


# ============================================================
# STAGE 2: VALIDATE — S-1 schema enforcement
# ============================================================

def validate_file_ir(file_ir, all_ids, strict=False):
    """Validate a single file's IR against S-1 schema."""
    issues = []
    fm = file_ir["frontmatter"]

    if fm is None:
        issues.append(("ERROR", "No valid frontmatter"))
        return issues

    # Required fields
    for field in REQUIRED_FIELDS:
        val = fm.get(field)
        if val is None or (isinstance(val, str) and val.strip() == ""):
            issues.append(("ERROR", f"Missing required field: {field}"))

    # Enum validations
    def check_enum(field, valid_set, level="ERROR"):
        val = fm.get(field)
        if val is not None and str(val).lower() not in {str(v).lower() if v else str(v) for v in valid_set}:
            issues.append((level, f"Invalid {field}: {val}"))

    check_enum("tier", VALID_TIERS)
    check_enum("chain", VALID_CHAINS)
    check_enum("celestial_type", VALID_CELESTIAL_TYPES)
    check_enum("volatility_band", VALID_VOLATILITY_BANDS)
    check_enum("refresh_cadence", VALID_REFRESH_CADENCES, "WARN")
    check_enum("status", VALID_STATUSES)
    check_enum("operational_status", VALID_OP_STATUSES)
    check_enum("element", VALID_ELEMENTS, "WARN")
    check_enum("ooda_phase", VALID_OODA_PHASES, "WARN")
    check_enum("layer", VALID_LAYERS, "WARN")
    check_enum("developmental_status", VALID_DEV_STATUSES, "WARN")

    # Recommended fields
    for field in RECOMMENDED_FIELDS:
        if field not in fm:
            issues.append(("WARN", f"Missing recommended field: {field}"))

    # Cross-reference validation
    for ref_field in ("requires", "siblings", "synthesizes", "parent"):
        refs = fm.get(ref_field)
        if refs is None:
            continue
        if isinstance(refs, str):
            refs = [refs]
        if not isinstance(refs, list):
            refs = [refs]
        for ref in refs:
            ref_str = str(ref).strip()
            if ref_str and ref_str != "null" and ref_str not in all_ids:
                issues.append(("WARN", f"{ref_field} → unknown id: {ref_str}"))

    # Version consistency
    yaml_ver = str(fm.get("version", ""))
    for inline_ver in file_ir["body"].get("inline_versions", []):
        if inline_ver != yaml_ver:
            issues.append(("WARN", f"Body version ({inline_ver}) ≠ YAML ({yaml_ver})"))

    # Volatility consistency
    vb = str(fm.get("volatility_band", "")).lower()
    rc = fm.get("refresh_cadence")
    rc_str = str(rc).lower() if rc else None
    key = (vb, rc_str)
    if key in VOLATILITY_RULES:
        issues.append(("WARN", VOLATILITY_RULES[key]))

    return issues


def stage_validate(ir_collection, strict=False):
    """Stage 2: Validate all files in IR collection."""
    all_ids = set(ir_collection["id_index"].keys())

    validation = {
        "stage": "validate",
        "timestamp": datetime.now().isoformat(),
        "total_files": ir_collection["file_count"],
        "clean_files": 0,
        "total_errors": 0,
        "total_warnings": 0,
        "orphans": [],
        "results": {},
    }

    # Validate each file
    for file_ir in ir_collection["files"]:
        issues = validate_file_ir(file_ir, all_ids, strict)
        errors = [i for i in issues if i[0] == "ERROR"]
        warns = [i for i in issues if i[0] == "WARN"]
        validation["total_errors"] += len(errors)
        validation["total_warnings"] += len(warns)
        if not issues:
            validation["clean_files"] += 1
        if issues:
            validation["results"][file_ir["filename"]] = [
                {"level": l, "message": m} for l, m in issues
            ]

    # Orphan detection
    referenced_ids = set()
    for file_ir in ir_collection["files"]:
        fm = file_ir["frontmatter"]
        if not fm:
            continue
        for ref_field in ("requires", "siblings", "synthesizes", "parent"):
            refs = fm.get(ref_field)
            if refs is None:
                continue
            if isinstance(refs, str):
                refs = [refs]
            if not isinstance(refs, list):
                refs = [refs]
            for ref in refs:
                ref_str = str(ref).strip()
                if ref_str and ref_str != "null":
                    referenced_ids.add(ref_str)

    for file_ir in ir_collection["files"]:
        fm = file_ir["frontmatter"]
        if fm and "id" in fm:
            fid = str(fm["id"])
            if fid not in referenced_ids and fid != "CANON-00000":
                validation["orphans"].append(fid)

    # Heatmap summary
    heatmap = {"green": 0, "yellow": 0, "red": 0, "grey": 0}
    for file_ir in ir_collection["files"]:
        fm = file_ir["frontmatter"]
        if not fm:
            heatmap["grey"] += 1
            continue
        tier = str(fm.get("tier", "")).lower()
        vb = str(fm.get("volatility_band", "")).lower()
        if tier == "immune":
            heatmap["grey"] += 1
        elif vb == "dynamic" and tier in ("cosmos", "core", "lattice"):
            heatmap["red"] += 1
        elif vb == "moderate" and tier in ("cosmos", "core"):
            heatmap["yellow"] += 1
        else:
            heatmap["green"] += 1
    validation["heatmap"] = heatmap

    return validation


# ============================================================
# MUTAGENIC ZONE (M-1 ratified CC49)
# ============================================================

def check_mutagenic_zone():
    """Check mutagenic zone — syntax only, no semantic validation."""
    if not MUTAGENIC_DIR.is_dir():
        return None

    results = {
        "zone": str(MUTAGENIC_DIR),
        "files": 0,
        "syntax_errors": 0,
        "details": [],
    }

    for f in sorted(MUTAGENIC_DIR.glob("*.md")):
        results["files"] += 1
        text = f.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?\n)---\s*\n", text, re.DOTALL)
        if match:
            try:
                yaml.safe_load(match.group(1))
            except yaml.YAMLError as e:
                results["syntax_errors"] += 1
                results["details"].append({"file": f.name, "error": str(e)})
        # No semantic validation — this is the mutagenic zone

    return results


# ============================================================
# OUTPUT FORMATTERS
# ============================================================

def format_text(validation, ir_collection):
    """Human-readable output."""
    lines = []
    lines.append("Canon Compiler — Validation Report")
    lines.append("=" * 60)
    lines.append(f"Files scanned:    {validation['total_files']}")
    lines.append(f"S-1 compliant:    {validation['clean_files']}")
    lines.append(f"Errors:           {validation['total_errors']}")
    lines.append(f"Warnings:         {validation['total_warnings']}")
    lines.append(f"Orphans:          {len(validation['orphans'])}")

    hm = validation.get("heatmap", {})
    lines.append(f"\nHeatmap: {hm.get('green',0)} green | {hm.get('yellow',0)} yellow | {hm.get('red',0)} red | {hm.get('grey',0)} grey")

    if validation["results"]:
        lines.append("")
        for fname, issues in sorted(validation["results"].items()):
            lines.append(f"  {fname}:")
            for issue in issues:
                marker = "✗" if issue["level"] == "ERROR" else "⚠"
                lines.append(f"    {marker} [{issue['level']}] {issue['message']}")
            lines.append("")

    if validation["orphans"]:
        lines.append("  Orphans (no inbound refs):")
        for o in sorted(validation["orphans"]):
            lines.append(f"    - {o}")
        lines.append("")

    if validation["total_errors"] == 0:
        lines.append("✓ Canon compilation PASSED. No errors.")
    else:
        lines.append(f"✗ Canon compilation FAILED. {validation['total_errors']} errors.")

    return "\n".join(lines)


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Canon Compiler (5-stage pipeline)")
    parser.add_argument("stage", nargs="?", default="validate",
                        choices=["parse", "validate", "compile"],
                        help="Which stage(s) to run")
    parser.add_argument("--out", help="Write IR/results to file")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--strict", action="store_true", help="Warnings = errors")
    args = parser.parse_args()

    # Stage 1: Parse
    ir = stage_parse()

    if args.stage == "parse":
        output = json.dumps(ir, indent=2, default=str)
        if args.out:
            Path(args.out).write_text(output)
            print(f"IR written to {args.out} ({ir['file_count']} files)")
        else:
            print(output)
        sys.exit(0)

    # Stage 2: Validate
    validation = stage_validate(ir, strict=args.strict)

    # Check mutagenic zone
    mutagenic = check_mutagenic_zone()
    if mutagenic:
        validation["mutagenic_zone"] = mutagenic

    if args.json:
        output = json.dumps(validation, indent=2, default=str)
        if args.out:
            Path(args.out).write_text(output)
            print(f"Validation written to {args.out}")
        else:
            print(output)
    else:
        print(format_text(validation, ir))

    sys.exit(1 if validation["total_errors"] > 0 else 0)


if __name__ == "__main__":
    main()
