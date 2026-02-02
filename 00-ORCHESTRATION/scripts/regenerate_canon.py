#!/usr/bin/env python3
"""
CANON Regeneration Script
Renders CANON files from Jinja2 templates + live data.

Demonstrates the metabolic pattern:
- Temporal data lives in JSON files (state/)
- Evergreen structure lives in templates (templates/)
- CANON files are regenerated when data changes
- Old data deleted, new data merged, structure persists

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

# Try to import jinja2, install if missing
try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("jinja2 not found. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "jinja2"])
    from jinja2 import Environment, FileSystemLoader

# Configuration
SCRIPT_DIR = Path(__file__).parent
ORCHESTRATION_ROOT = SCRIPT_DIR.parent
TEMPLATES_DIR = ORCHESTRATION_ROOT / "templates"
STATE_DIR = ORCHESTRATION_ROOT / "state"
CANON_DIR = ORCHESTRATION_ROOT.parent / "01-CANON"

# Ensure directories exist
TEMPLATES_DIR.mkdir(exist_ok=True)
STATE_DIR.mkdir(exist_ok=True)
CANON_DIR.mkdir(exist_ok=True)


def load_platform_capabilities():
    """Load current platform capability data from state/."""
    cap_file = STATE_DIR / "platform_capabilities.json"

    if cap_file.exists():
        with open(cap_file) as f:
            return json.load(f)
    else:
        # Return sample data for initial proof of concept
        print(f"⚠️  {cap_file} not found. Using sample data.")
        return get_sample_platform_data()


def get_sample_platform_data():
    """Sample platform capability data for proof of concept."""
    return {
        "metadata": {
            "last_regenerated": datetime.utcnow().isoformat() + "Z",
            "data_source": "platform_capabilities.json",
            "data_version": "1.0.0"
        },
        "platforms": [
            {
                "name": "Claude Code",
                "tier": "Pro x3",
                "monthly_cost": 60,
                "role": "Commander",
                "status": "Active",
                "utilization": 75,
                "cost_per_hour": "2.00"
            },
            {
                "name": "Gemini",
                "tier": "Advanced",
                "monthly_cost": 20,
                "role": "Oracle",
                "status": "Active",
                "utilization": 40,
                "cost_per_hour": "0.67"
            },
            {
                "name": "ChatGPT",
                "tier": "Plus",
                "monthly_cost": 20,
                "role": "Vanguard",
                "status": "Active",
                "utilization": 30,
                "cost_per_hour": "0.67"
            }
        ],
        "total_monthly_cost": 100,
        "oracle_platform": "Gemini",
        "vanguard_platform": "ChatGPT",
        "commander_platform": "Claude",
        "claude": {
            "account": "truongphillipthanh@gmail.com (+ 2 others)",
            "models": ["Opus 4.5", "Sonnet 4.5"],
            "capabilities": [
                {"name": "Filesystem Access", "status": "Active", "notes": "Full repository sovereignty"},
                {"name": "Code Generation", "status": "Active", "notes": "Opus 4.5 / Sonnet 4.5"},
                {"name": "MCP Integration", "status": "Active", "notes": "External tool access"},
                {"name": "Plan Mode", "status": "Active", "notes": "Separates planning from execution"},
                {"name": "Context Management", "status": "Active", "notes": "~200K tokens, auto-compact"}
            ],
            "routing_strengths": [
                "Execution (filesystem operations)",
                "Code generation (writing functions)",
                "File manipulation (read/edit/write)",
                "Verification (command-based proof)",
                "Repository operations (git, ledger updates)"
            ],
            "routing_weaknesses": [
                "Corpus-scale RAG (context limit ~200K)",
                "Video processing (no native multimodal)",
                "Long-horizon planning (better as executor than planner)"
            ],
            "cost_structure": "$20/month per seat, 3 seats = $60/month"
        },
        "gemini": {
            "account": "truongphillipthanh@gmail.com",
            "models": ["Gemini 2.5 Pro", "Gemini 2.5 Flash"],
            "capabilities": [
                {"name": "2M Context Window", "status": "Active", "notes": "Entire corpus fits"},
                {"name": "Drive Connector", "status": "Active", "notes": "Repository visibility"},
                {"name": "NotebookLM", "status": "Active", "notes": "Grounded RAG, zero hallucination"},
                {"name": "Video Processing", "status": "Active", "notes": "263 tok/sec native ingestion"},
                {"name": "Audio Processing", "status": "Active", "notes": "Speaker diarization"}
            ],
            "routing_strengths": [
                "Corpus-scale sensing (2M context)",
                "Video transcription (native multimodal)",
                "Large context queries (entire repo + conversations)",
                "Grounded RAG (NotebookLM)",
                "Historical analysis (Oracle 0-13 in single context)"
            ],
            "routing_weaknesses": [
                "Filesystem access (read-only, no execution)",
                "Code execution (not designed for)",
                "Planning (sensing role, not planning)"
            ],
            "cost_structure": "$20/month"
        },
        "chatgpt": {
            "account": "truongphillipthanh@icloud.com",
            "models": ["GPT-5.2 Instant", "GPT-5.2 Thinking"],
            "capabilities": [
                {"name": "GPT-5.2 Thinking", "status": "Active", "notes": "~3K messages/week"},
                {"name": "Deep Research", "status": "Active", "notes": "Comprehensive investigation"},
                {"name": "Canvas", "status": "Active", "notes": "Collaborative editing"},
                {"name": "Codex CLI", "status": "Available", "notes": "GitHub integration (if enabled)"},
                {"name": "Connectors", "status": "Available", "notes": "Drive, GitHub (if enabled)"}
            ],
            "routing_strengths": [
                "Long-horizon planning (GPT-5.2 Thinking)",
                "Specification (clear acceptance criteria)",
                "Audit (verification against plan)",
                "Abstract reasoning (architectural decisions)",
                "Multi-step decomposition"
            ],
            "routing_weaknesses": [
                "Corpus-scale sensing (context limit)",
                "Video processing (no native multimodal)",
                "Code execution (not designed for)"
            ],
            "cost_structure": "$20/month"
        },
        "routing_table": [
            {"task_type": "Corpus Sensing", "primary": "Gemini", "rationale": "2M context window", "fallback": "Claude (limited context)"},
            {"task_type": "Video Processing", "primary": "Gemini", "rationale": "Native multimodal", "fallback": "Manual transcription"},
            {"task_type": "Planning", "primary": "ChatGPT", "rationale": "GPT-5.2 Thinking", "fallback": "Claude Plan Mode"},
            {"task_type": "Audit", "primary": "ChatGPT", "rationale": "Spec verification", "fallback": "Claude verification"},
            {"task_type": "Execution", "primary": "Claude", "rationale": "Filesystem sovereignty", "fallback": "Manual operations"},
            {"task_type": "Code Generation", "primary": "Claude", "rationale": "Opus 4.5 / Sonnet 4.5", "fallback": "ChatGPT"},
            {"task_type": "Grounded RAG", "primary": "Gemini", "rationale": "NotebookLM integration", "fallback": "Claude with citations"},
            {"task_type": "Long-Horizon Decomposition", "primary": "ChatGPT", "rationale": "GPT-5.2 Thinking", "fallback": "Claude ultrathink"}
        ],
        "metrics": {
            "autonomous_cycles": 0,
            "relay_reduction": 0,
            "sources_processed": 0,
            "canon_integrations": 0,
            "cost_per_cycle": "N/A"
        },
        "regeneration_log": [
            {
                "date": "2026-01-15",
                "change_description": "Initial capability catalog creation"
            }
        ]
    }


def regenerate_canon_31150():
    """Regenerate CANON-31150 Platform Capability Catalog."""

    print("=" * 60)
    print("CANON-31150: Platform Capability Catalog")
    print("=" * 60)

    # Load template
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template_file = "CANON-31150.md.j2"

    try:
        template = env.get_template(template_file)
    except Exception as e:
        print(f"✗ Error loading template: {e}")
        return None

    # Load data
    data = load_platform_capabilities()

    # Ensure metadata exists
    if "metadata" not in data:
        data["metadata"] = {}

    data["metadata"]["last_regenerated"] = datetime.utcnow().isoformat() + "Z"

    # Render template
    try:
        output = template.render(**data)
    except Exception as e:
        print(f"✗ Error rendering template: {e}")
        return None

    # Output path
    output_file = CANON_DIR / "CANON-31150-PLATFORM_CAPABILITY_CATALOG.md"

    # Preview
    print(f"\n✓ Template loaded: {template_file}")
    print(f"✓ Data loaded: {len(data)} keys")
    print(f"✓ Rendered: {len(output)} characters\n")
    print("─" * 60)
    print("PREVIEW (first 2000 chars):")
    print("─" * 60)
    print(output[:2000])
    print("...")
    print(f"\n[Total length: {len(output)} characters]")
    print("─" * 60)

    # Write to file
    print(f"\n✓ Writing to: {output_file}")
    with open(output_file, 'w') as f:
        f.write(output)

    print(f"✓ CANON-31150 regenerated successfully!")
    print(f"\nTo review: cat {output_file}")
    print(f"To commit: git add {output_file} && git commit -m 'feat(canon): regenerate 31150'")

    return output


def list_templates():
    """List all available CANON templates."""
    print("\nAvailable CANON Templates:")
    print("=" * 60)

    templates = list(TEMPLATES_DIR.glob("CANON-*.md.j2"))

    if not templates:
        print("No templates found in", TEMPLATES_DIR)
    else:
        for template in sorted(templates):
            canon_id = template.stem.replace(".md", "")
            print(f"  - {canon_id}")

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Regenerate CANON files from templates + data"
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

    args = parser.parse_args()

    if args.list:
        list_templates()
        return

    if args.all:
        print("Regenerating all CANON templates...")
        # For now, only 31150 exists
        regenerate_canon_31150()
        return

    if not args.canon_id:
        parser.print_help()
        return

    canon_id = args.canon_id

    if canon_id == "31150":
        regenerate_canon_31150()
    else:
        print(f"✗ Unknown CANON ID: {canon_id}")
        print("\nAvailable CANON IDs:")
        print("  - 31150 (Platform Capability Catalog)")
        list_templates()


if __name__ == "__main__":
    main()
