#!/usr/bin/env python3
"""Canon S-1 Frontmatter Validator — The Immune System (T-6).

Validates all canon files against the ratified S-1 schema (CC49).
This IS the compiler-as-antibody: coherence enforcement at build time.

Usage:
    python3 corpus/validate_canon.py [--json] [--strict]
"""

import sys
import os
import re
import yaml
import json
import argparse
from pathlib import Path

CANON_DIR = Path(__file__).parent.parent / "canon"

# === S-1 Schema Enums (Ratified CC49) ===

VALID_TIERS = {"cosmos", "core", "lattice", "chain", "archive", "immune"}
VALID_CHAINS = {
    None, "intelligence", "information", "insight",
    "expertise", "knowledge", "wisdom"
}
VALID_CELESTIAL_TYPES = {
    "root", "planetary", "ring", "lunar", "comet",
    "asteroid", "satellite", "policy", "meta"
}
VALID_VOLATILITY_BANDS = {"permanent", "stable", "moderate", "dynamic"}
VALID_REFRESH_CADENCES = {None, "annual", "semi-annual", "quarterly", "monthly"}
VALID_STATUSES = {"canonical", "draft", "deprecated", "archived"}
VALID_OP_STATUSES = {"operational", "partial", "theoretical", "pilot"}
VALID_ELEMENTS = {None, "fire", "water", "earth", "air", "quintessence"}
VALID_OODA_PHASES = {None, "observe", "orient", "decide", "act", "sharpen"}

# Fields required in S-1 compliant frontmatter
REQUIRED_FIELDS = [
    "id", "canonical_name", "tier", "celestial_type",
    "volatility_band", "status", "operational_status",
    "version", "created", "updated"
]

# Fields that should exist (warning if missing, not error)
RECOMMENDED_FIELDS = [
    "parent", "requires", "siblings", "synthesizes",
    "refresh_cadence", "last_verified", "element", "ooda_phase",
    "volatile_sections", "title", "chain"
]

# Valid layer values (D-1/D-2 ratified CC49)
VALID_LAYERS = {None, "lattice", "chain", "cosmos"}
# Valid developmental_status values (Diviner amendment CC49)
VALID_DEV_STATUSES = {None, "active", "stable", "dormant"}

# Legacy fields that should be migrated
LEGACY_FIELDS = ["depends_on", "identity", "synopsis", "change_velocity"]


def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?\n)---\s*\n", text, re.DOTALL)
    if not match:
        return None, text
    try:
        fm = yaml.safe_load(match.group(1))
        return fm if isinstance(fm, dict) else None, text
    except yaml.YAMLError:
        return None, text


def validate_file(filepath, all_ids, strict=False):
    """Validate a single canon file. Returns list of (level, message)."""
    issues = []
    fm, body = parse_frontmatter(filepath)
    fname = filepath.name

    if fm is None:
        issues.append(("ERROR", f"No valid YAML frontmatter"))
        return issues

    # Required fields
    for field in REQUIRED_FIELDS:
        if field not in fm or fm[field] is None:
            issues.append(("ERROR", f"Missing required field: {field}"))

    # Enum validation
    if fm.get("tier") and fm["tier"].lower() not in VALID_TIERS:
        issues.append(("ERROR", f"Invalid tier: {fm['tier']} (valid: {VALID_TIERS})"))

    chain_val = fm.get("chain")
    if chain_val is not None and chain_val.lower() not in VALID_CHAINS:
        issues.append(("ERROR", f"Invalid chain: {chain_val}"))

    ct = fm.get("celestial_type")
    if ct and ct.lower() not in VALID_CELESTIAL_TYPES:
        issues.append(("ERROR", f"Invalid celestial_type: {ct}"))

    vb = fm.get("volatility_band")
    if vb and vb.lower() not in VALID_VOLATILITY_BANDS:
        issues.append(("ERROR", f"Invalid volatility_band: {vb}"))

    rc = fm.get("refresh_cadence")
    if rc is not None and rc.lower() not in VALID_REFRESH_CADENCES:
        issues.append(("WARN", f"Invalid refresh_cadence: {rc}"))

    st = fm.get("status")
    if st and st.lower() not in VALID_STATUSES:
        issues.append(("ERROR", f"Invalid status: {st}"))

    ops = fm.get("operational_status")
    if ops and ops.lower() not in VALID_OP_STATUSES:
        issues.append(("ERROR", f"Invalid operational_status: {ops}"))

    el = fm.get("element")
    if el is not None and el.lower() not in VALID_ELEMENTS:
        issues.append(("WARN", f"Invalid element: {el}"))

    ooda = fm.get("ooda_phase")
    if ooda is not None and ooda.lower() not in VALID_OODA_PHASES:
        issues.append(("WARN", f"Invalid ooda_phase: {ooda}"))

    # Recommended fields
    for field in RECOMMENDED_FIELDS:
        if field not in fm:
            issues.append(("WARN", f"Missing recommended field: {field}"))

    # Layer validation (lattice files must declare layer)
    layer = fm.get("layer")
    if layer is not None and layer.lower() not in VALID_LAYERS:
        issues.append(("ERROR", f"Invalid layer: {layer}"))
    if fm.get("tier") and fm["tier"].lower() == "lattice" and fm.get("chain") == "intelligence":
        if not layer:
            issues.append(("WARN", f"Lattice-tier Intelligence file missing layer field"))

    # Developmental status validation
    dev_status = fm.get("developmental_status")
    if dev_status is not None and dev_status.lower() not in VALID_DEV_STATUSES:
        issues.append(("ERROR", f"Invalid developmental_status: {dev_status}"))

    # Legacy fields still present
    for field in LEGACY_FIELDS:
        if field in fm:
            issues.append(("WARN", f"Legacy field still present: {field} (migrate to S-1)"))

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
            if ref and str(ref) not in all_ids:
                issues.append(("WARN", f"{ref_field} references unknown id: {ref}"))

    # Version consistency: check body doesn't contradict YAML
    yaml_version = fm.get("version")
    if yaml_version:
        body_versions = re.findall(
            r"\*\*Version\*\*:\s*(\d+\.\d+\.\d+)", body
        )
        for bv in body_versions:
            if bv != str(yaml_version):
                issues.append(("WARN", f"Body version ({bv}) contradicts YAML ({yaml_version})"))

    # Volatility band / refresh cadence consistency
    if vb and rc:
        vb_l = vb.lower()
        rc_l = rc.lower() if rc else None
        if vb_l == "permanent" and rc_l not in (None, "annual"):
            issues.append(("WARN", f"Volatility 'permanent' but refresh '{rc}' — contradiction?"))
        if vb_l == "dynamic" and rc_l in (None, "annual"):
            issues.append(("WARN", f"Volatility 'dynamic' but refresh '{rc}' — too slow?"))

    return issues


def main():
    parser = argparse.ArgumentParser(description="Canon S-1 Frontmatter Validator")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()

    if not CANON_DIR.is_dir():
        print(f"ERROR: Canon directory not found: {CANON_DIR}", file=sys.stderr)
        sys.exit(1)

    # Collect all canon file IDs for cross-reference validation
    all_ids = set()
    canon_files = sorted(CANON_DIR.glob("*.md"))

    for f in canon_files:
        fm, _ = parse_frontmatter(f)
        if fm and "id" in fm:
            all_ids.add(str(fm["id"]))

    # Validate each file
    results = {}
    total_errors = 0
    total_warns = 0
    clean_files = 0

    for f in canon_files:
        issues = validate_file(f, all_ids, args.strict)
        errors = [i for i in issues if i[0] == "ERROR"]
        warns = [i for i in issues if i[0] == "WARN"]
        total_errors += len(errors)
        total_warns += len(warns)
        if not issues:
            clean_files += 1
        results[f.name] = issues

    # Orphan detection: files with no inbound references
    referenced_ids = set()
    for f in canon_files:
        fm, _ = parse_frontmatter(f)
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
                if ref:
                    referenced_ids.add(str(ref))

    # Files with a valid parent are positionally anchored, not orphaned
    parented_ids = set()
    for f in canon_files:
        fm, _ = parse_frontmatter(f)
        if fm and "id" in fm:
            parent = fm.get("parent")
            if parent and str(parent) != "null" and str(parent) in all_ids and str(parent) != str(fm["id"]):
                parented_ids.add(str(fm["id"]))

    orphans = []
    for f in canon_files:
        fm, _ = parse_frontmatter(f)
        if fm and "id" in fm:
            fid = str(fm["id"])
            if fid not in referenced_ids and fid != "CANON-00000" and fid not in parented_ids:
                orphans.append(fid)

    # Output
    if args.json:
        output = {
            "total_files": len(canon_files),
            "clean_files": clean_files,
            "total_errors": total_errors,
            "total_warnings": total_warns,
            "orphans": orphans,
            "files": {
                name: [{"level": l, "message": m} for l, m in issues]
                for name, issues in results.items()
                if issues
            }
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"Canon S-1 Validation Report")
        print(f"{'=' * 60}")
        print(f"Files scanned: {len(canon_files)}")
        print(f"Clean (S-1 compliant): {clean_files}")
        print(f"Errors: {total_errors}")
        print(f"Warnings: {total_warns}")
        print(f"Orphans (no inbound refs): {len(orphans)}")
        print()

        for name, issues in sorted(results.items()):
            if not issues:
                continue
            print(f"  {name}:")
            for level, msg in issues:
                marker = "✗" if level == "ERROR" else "⚠"
                print(f"    {marker} [{level}] {msg}")
            print()

        if orphans:
            print(f"  Orphan IDs (no inbound references):")
            for o in sorted(orphans):
                print(f"    - {o}")
            print()

        if total_errors == 0:
            print("✓ No errors. Canon frontmatter is S-1 compliant.")
        else:
            print(f"✗ {total_errors} errors must be resolved for S-1 compliance.")

    sys.exit(1 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
