#!/usr/bin/env python3
"""
CANON Regeneration Script
Renders CANON files from Jinja2 templates + live data.

Convention-based discovery:
- Templates: 00-ORCHESTRATION/templates/CANON-{id}.md.j2
- Data mapping: 00-ORCHESTRATION/templates/template_registry.json
- Output: 01-CANON/CANON-{id}-*.md (discovered by prefix match)

Usage:
    python3 regenerate_canon.py 31150
    python3 regenerate_canon.py --list
    python3 regenerate_canon.py --all
"""

import json
import sys
import argparse
from datetime import datetime
from pathlib import Path

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("ERROR: jinja2 not installed. Run: pip install jinja2")
    sys.exit(1)

# Configuration
SCRIPT_DIR = Path(__file__).parent
ORCHESTRATION_ROOT = SCRIPT_DIR.parent
TEMPLATES_DIR = ORCHESTRATION_ROOT / "templates"
STATE_DIR = ORCHESTRATION_ROOT / "state"
CANON_DIR = ORCHESTRATION_ROOT.parent / "01-CANON"
REGISTRY_FILE = TEMPLATES_DIR / "template_registry.json"

TEMPLATES_DIR.mkdir(exist_ok=True)
STATE_DIR.mkdir(exist_ok=True)
CANON_DIR.mkdir(exist_ok=True)


def load_registry():
    """Load template registry mapping CANON IDs to data sources."""
    if REGISTRY_FILE.exists():
        with open(REGISTRY_FILE) as f:
            return json.load(f)
    # Auto-discover from templates if no registry
    registry = {}
    for template in sorted(TEMPLATES_DIR.glob("CANON-*.md.j2")):
        canon_id = template.stem.replace("CANON-", "").replace(".md", "")
        registry[canon_id] = {
            "description": "Auto-discovered (no registry entry)",
            "data_sources": [],
            "output_pattern": None
        }
    return registry


def load_data_for_canon(canon_id, registry_entry):
    """Load and merge all data sources for a CANON template."""
    data = {}
    sources = registry_entry.get("data_sources", [])

    for source in sources:
        source_path = STATE_DIR / source
        if source_path.exists():
            with open(source_path) as f:
                source_data = json.load(f)
                data.update(source_data)
        else:
            print(f"  ⚠ Data source not found: {source}")

    # Always inject regeneration metadata
    if "metadata" not in data:
        data["metadata"] = {}
    data["metadata"]["last_regenerated"] = datetime.now().astimezone().isoformat()
    data["metadata"]["canon_id"] = canon_id
    data["metadata"]["data_sources"] = sources

    return data


def find_output_file(canon_id, registry_entry):
    """Find existing CANON output file by prefix match or registry pattern."""
    # Check registry for explicit output filename
    output_pattern = registry_entry.get("output_pattern")
    if output_pattern:
        return CANON_DIR / output_pattern

    # Discover by prefix match in 01-CANON/
    matches = sorted(CANON_DIR.glob(f"CANON-{canon_id}-*.md"))
    if matches:
        return matches[0]

    # Fallback
    return CANON_DIR / f"CANON-{canon_id}.md"


def regenerate(canon_id, quiet=False):
    """Regenerate a single CANON file from its template + data."""
    registry = load_registry()
    entry = registry.get(canon_id, {
        "description": "Unknown",
        "data_sources": [],
        "output_pattern": None
    })

    template_file = f"CANON-{canon_id}.md.j2"
    template_path = TEMPLATES_DIR / template_file

    if not template_path.exists():
        print(f"✗ Template not found: {template_path}")
        return None

    if not quiet:
        print(f"{'=' * 60}")
        print(f"CANON-{canon_id}: {entry.get('description', 'No description')}")
        print(f"{'=' * 60}")

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    try:
        template = env.get_template(template_file)
    except Exception as e:
        print(f"✗ Error loading template: {e}")
        return None

    data = load_data_for_canon(canon_id, entry)

    try:
        output = template.render(**data)
    except Exception as e:
        print(f"✗ Error rendering CANON-{canon_id}: {e}")
        return None

    output_file = find_output_file(canon_id, entry)

    if not quiet:
        print(f"\n✓ Template: {template_file}")
        print(f"✓ Data sources: {entry.get('data_sources', ['none'])}")
        print(f"✓ Rendered: {len(output)} characters")

    with open(output_file, 'w') as f:
        f.write(output)

    print(f"✓ CANON-{canon_id} → {output_file.name} ({len(output)} chars)")
    return output


def regenerate_all():
    """Regenerate all CANON files that have templates."""
    registry = load_registry()
    templates = sorted(TEMPLATES_DIR.glob("CANON-*.md.j2"))

    if not templates:
        print("No templates found in", TEMPLATES_DIR)
        return

    print(f"Regenerating {len(templates)} CANON template(s)...\n")

    results = []
    for template_path in templates:
        canon_id = template_path.stem.replace("CANON-", "").replace(".md", "")
        result = regenerate(canon_id, quiet=True)
        results.append((canon_id, result is not None))

    print(f"\n{'=' * 60}")
    print(f"Results: {sum(1 for _, ok in results if ok)}/{len(results)} succeeded")
    for canon_id, ok in results:
        status = "✓" if ok else "✗"
        desc = registry.get(canon_id, {}).get("description", "")
        print(f"  {status} CANON-{canon_id} — {desc}")
    print(f"{'=' * 60}")


def list_templates():
    """List all available CANON templates with their registry info."""
    registry = load_registry()
    templates = sorted(TEMPLATES_DIR.glob("CANON-*.md.j2"))

    print(f"\nAvailable CANON Templates ({len(templates)}):")
    print("=" * 60)

    if not templates:
        print("No templates found in", TEMPLATES_DIR)
    else:
        for template_path in templates:
            canon_id = template_path.stem.replace("CANON-", "").replace(".md", "")
            entry = registry.get(canon_id, {})
            desc = entry.get("description", "No description")
            sources = entry.get("data_sources", [])
            print(f"  CANON-{canon_id}: {desc}")
            if sources:
                print(f"    Data: {', '.join(sources)}")

    print("=" * 60)
    if REGISTRY_FILE.exists():
        print(f"Registry: {REGISTRY_FILE}")
    else:
        print("Registry: not found (using auto-discovery)")


def main():
    parser = argparse.ArgumentParser(
        description="Regenerate CANON files from Jinja2 templates + live data"
    )
    parser.add_argument(
        "canon_id",
        nargs="?",
        help="CANON ID to regenerate (e.g., 31150)"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available templates"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Regenerate all CANON templates"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON"
    )

    args = parser.parse_args()

    if args.list:
        if args.json:
            registry = load_registry()
            templates = sorted(TEMPLATES_DIR.glob("CANON-*.md.j2"))
            entries = []
            for t in templates:
                cid = t.stem.replace("CANON-", "").replace(".md", "")
                entry = registry.get(cid, {})
                entries.append({"canon_id": cid, "description": entry.get("description", ""), "data_sources": entry.get("data_sources", [])})
            print(json.dumps({"templates": entries}, indent=2))
        else:
            list_templates()
        return

    if args.all:
        if args.json:
            registry = load_registry()
            templates = sorted(TEMPLATES_DIR.glob("CANON-*.md.j2"))
            results = []
            for t in templates:
                cid = t.stem.replace("CANON-", "").replace(".md", "")
                result = regenerate(cid, quiet=True)
                results.append({"canon_id": cid, "success": result is not None, "chars": len(result) if result else 0})
            print(json.dumps({"results": results, "total": len(results), "succeeded": sum(1 for r in results if r["success"])}, indent=2))
        else:
            regenerate_all()
        return

    if not args.canon_id:
        parser.print_help()
        return

    regenerate(args.canon_id)


if __name__ == "__main__":
    main()
