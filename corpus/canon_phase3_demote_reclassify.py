#!/usr/bin/env python3
"""Phase 3: Canon Demotions (T-2) + Reclassifications (T-3) — CC49 Ratified.

T-2: Move demoted files from canon/ to corpus/demoted/ with flag.
T-3: Update volatility_band on mismatched files (22 yellow + 10 red from Pass 6).

Usage:
    python3 corpus/canon_phase3_demote_reclassify.py --dry-run   # default
    python3 corpus/canon_phase3_demote_reclassify.py --execute
"""

import sys
import os
import re
import shutil
import yaml
import argparse
from pathlib import Path

CANON_DIR = Path(__file__).parent.parent / "canon"
DEMOTED_DIR = Path(__file__).parent.parent / "corpus" / "demoted"

# === T-2: DEMOTIONS (Ratified CC49) ===
# Files to remove from canon entirely — textbook imports, dated, incomplete, auto-generated

DEMOTIONS = {
    # 30400 Peninsula — textbook imports, never integrated (Pass 6 §D.3)
    "CANON-30410-COGNITIVE_ARCHITECTURE-asteroid-INTELLIGENCE.md": "Textbook import — 30400 peninsula, never integrated, theoretical status",
    "CANON-30420-MULTI_AGENT_ORCHESTRATION-asteroid-INTELLIGENCE.md": "Textbook import — 30400 peninsula, never integrated, theoretical status",
    "CANON-30430-MEMORY_SYSTEMS-asteroid-INTELLIGENCE.md": "Textbook import — 30400 peninsula, never integrated, theoretical status",
    "CANON-30440-SAFETY_ALIGNMENT-asteroid-INTELLIGENCE.md": "Textbook import — 30400 peninsula, never integrated, theoretical status",
    "CANON-30450-PRODUCTION_FRAMEWORKS-asteroid-INTELLIGENCE.md": "Textbook import — 30400 peninsula, dated 'Upcoming' sections already past",
    # Other demotions
    "CANON-34120-SYLLABUS-lunar-MASTERY-planetary-KNOWLEDGE.md": "Explicitly dated 'October 2025' — stale reference, not scripture",
    "CANON-31150-PLATFORM_CAPABILITY_CATALOG.md": "Auto-generated catalog, no sovereign voice — reference material not canon",
    "CANON-33111-BIZ_ENHANCE-satellite-BIZ_BACKBONE-lunar-EFFICACY-planetary-EXPERTISE.md": "Incomplete — partial status, never developed beyond skeleton",
}

# === T-3: RECLASSIFICATIONS — Volatility corrections from Pass 5/6 heatmap ===

# RED nodes (DYNAMIC content in STABLE+ tier) — immediate correction
RED_RECLASSIFICATIONS = {
    "CANON-00006-CORPUS-cosmos.md": {"volatility_band": "dynamic", "refresh_cadence": "monthly"},
    "CANON-00014-CONTENT_PROTOCOL-cosmos.md": {"volatility_band": "dynamic", "refresh_cadence": "quarterly"},
    "CANON-25200-CONSTELLATION_ARCH-lattice.md": {"volatility_band": "dynamic", "refresh_cadence": "quarterly"},
    "CANON-30200-POSITIONING-comet-INTELLIGENCE.md": {"volatility_band": "dynamic", "refresh_cadence": "quarterly"},
    "CANON-30300-TECH_STACK-comet-INTELLIGENCE.md": {"volatility_band": "dynamic", "refresh_cadence": "monthly"},
    # 30450 is being demoted so skip it
    "CANON-31115-IIC_IMPL-lunar-ACUMEN-planetary-INFORMATION.md": {"volatility_band": "dynamic", "refresh_cadence": "monthly"},
    "CANON-31141-FIVE_ACCOUNT-satellite-IIC-lunar-ACUMEN-planetary-INFORMATION.md": {"volatility_band": "dynamic", "refresh_cadence": "quarterly"},
    "CANON-31142-PLATFORM_GRAMMAR-satellite-IIC-lunar-ACUMEN-planetary-INFORMATION.md": {"volatility_band": "dynamic", "refresh_cadence": "quarterly"},
    # 31150 is being demoted so skip it
    # 34120 is being demoted so skip it
}

# YELLOW nodes (MODERATE content in STABLE tier) — monitoring correction
YELLOW_RECLASSIFICATIONS = {
    "CANON-00004-EVOLUTION-cosmos.md": {"volatility_band": "moderate", "refresh_cadence": "semi-annual"},
    "CANON-00007-EVALUATION-cosmos.md": {"volatility_band": "moderate", "refresh_cadence": "semi-annual"},
    "CANON-00009-STRATEGY-cosmos.md": {"volatility_band": "moderate", "refresh_cadence": "semi-annual"},
    "CANON-00010-OPERATIONS-cosmos.md": {"volatility_band": "moderate", "refresh_cadence": "semi-annual"},
    "CANON-00012-MODAL_SEQUENCE-cosmos.md": {"volatility_band": "moderate", "refresh_cadence": "semi-annual"},
    "CANON-00013-QUICKSTART-cosmos.md": {"volatility_band": "moderate", "refresh_cadence": "semi-annual"},
    "CANON-00017-AGENTIC_CONSTITUTION-cosmos.md": {"volatility_band": "moderate", "refresh_cadence": "quarterly"},
    "CANON-21000-CHAIN_MATRIX-lattice.md": {"volatility_band": "moderate", "refresh_cadence": "semi-annual"},
    "CANON-21100-TRI_HELIX-lattice.md": {"volatility_band": "moderate", "refresh_cadence": "semi-annual"},
    "CANON-25000-MEMORY_ARCH-lattice.md": {"volatility_band": "moderate", "refresh_cadence": "quarterly"},
    "CANON-25100-CONTEXT_TRANS-lattice.md": {"volatility_band": "moderate", "refresh_cadence": "quarterly"},
    "CANON-25610-DIVINER_PROMPTING_FORMULA-lattice.md": {"volatility_band": "moderate", "refresh_cadence": "quarterly"},
    "CANON-30310-MIGRATION-asteroid-TECH_STACK-comet-INTELLIGENCE.md": {"volatility_band": "moderate", "refresh_cadence": "quarterly"},
    "CANON-30340-IMPLEMENTATION_PATTERNS-asteroid-TECH_STACK-comet-INTELLIGENCE.md": {"volatility_band": "moderate", "refresh_cadence": "quarterly"},
    "CANON-30400-AGENTIC_ARCHITECTURE-comet-INTELLIGENCE.md": {"volatility_band": "moderate", "refresh_cadence": "quarterly"},
    "CANON-30420-MULTI_AGENT_ORCHESTRATION-asteroid-INTELLIGENCE.md": {"volatility_band": "moderate", "refresh_cadence": "quarterly"},  # if not demoted
    "CANON-30430-MEMORY_SYSTEMS-asteroid-INTELLIGENCE.md": {"volatility_band": "moderate", "refresh_cadence": "quarterly"},  # if not demoted
    "CANON-30440-SAFETY_ALIGNMENT-asteroid-INTELLIGENCE.md": {"volatility_band": "moderate", "refresh_cadence": "quarterly"},  # if not demoted
    "CANON-30460-INTERACTION_DYNAMICS-comet.md": {"volatility_band": "moderate", "refresh_cadence": "quarterly"},
    "CANON-31110-FEEDCRAFT-lunar-ACUMEN-planetary-INFORMATION.md": {"volatility_band": "moderate", "refresh_cadence": "quarterly"},
    "CANON-31130-SEVEN_LAYER-lunar-ACUMEN-planetary-INFORMATION.md": {"volatility_band": "moderate", "refresh_cadence": "quarterly"},
    "CANON-31140-IIC-lunar-ACUMEN-planetary-INFORMATION.md": {"volatility_band": "moderate", "refresh_cadence": "quarterly"},
    "CANON-33110-BIZ_BACKBONE-lunar-EFFICACY-planetary-EXPERTISE.md": {"volatility_band": "moderate", "refresh_cadence": "semi-annual"},
    # 33111 is being demoted
    "CANON-33112-REVENUE_MODEL-satellite-BIZ_BACKBONE-lunar-EFFICACY-planetary-EXPERTISE.md": {"volatility_band": "moderate", "refresh_cadence": "semi-annual"},
    "CANON-35200-GAIAN_NODE-lunar-TRANSCENDENCE-ring-WISDOM.md": {"volatility_band": "moderate", "refresh_cadence": "semi-annual"},
}


def parse_frontmatter(filepath):
    """Extract YAML frontmatter and body."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?\n)---\s*\n", text, re.DOTALL)
    if not match:
        return None, text, text
    try:
        fm = yaml.safe_load(match.group(1))
        body = text[match.end():]
        raw_fm = match.group(1)
        return fm if isinstance(fm, dict) else None, body, text, raw_fm
    except yaml.YAMLError:
        return None, text, text, ""


def update_frontmatter_field(full_text, field, new_value):
    """Update a single field in YAML frontmatter."""
    # Match the field line in frontmatter
    pattern = rf"^({field}:\s*)(.+)$"
    replacement = rf"\g<1>{new_value}"
    updated = re.sub(pattern, replacement, full_text, count=1, flags=re.MULTILINE)
    return updated


def demote_file(filepath, reason, execute=False):
    """Move a canon file to corpus/demoted/ with demoted flag."""
    if execute:
        DEMOTED_DIR.mkdir(parents=True, exist_ok=True)

        # Read file, add demoted flag to frontmatter
        text = filepath.read_text(encoding="utf-8")
        text = update_frontmatter_field(text, "status", "demoted")

        # Add demotion metadata after status line
        demotion_meta = f"demotion_reason: \"{reason}\"\ndemoted_from: canon\ndemoted_date: 2026-02-27"
        text = re.sub(
            r"^(status:\s*demoted)$",
            rf"\1\n{demotion_meta}",
            text,
            count=1,
            flags=re.MULTILINE
        )

        dest = DEMOTED_DIR / filepath.name
        dest.write_text(text, encoding="utf-8")
        filepath.unlink()
        return dest
    return DEMOTED_DIR / filepath.name


def reclassify_file(filepath, updates, execute=False):
    """Update volatility_band and refresh_cadence in frontmatter."""
    if execute:
        text = filepath.read_text(encoding="utf-8")
        for field, value in updates.items():
            text = update_frontmatter_field(text, field, value)
        filepath.write_text(text, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Phase 3: Demotions + Reclassifications")
    parser.add_argument("--execute", action="store_true", help="Execute changes")
    parser.add_argument("--dry-run", action="store_true", help="Report only (default)")
    args = parser.parse_args()

    print("=" * 70)
    print("Phase 3: Canon Demotions (T-2) + Reclassifications (T-3)")
    print("=" * 70)

    # === T-2: DEMOTIONS ===
    print(f"\n{'─' * 70}")
    print(f"T-2: DEMOTIONS ({len(DEMOTIONS)} files → corpus/demoted/)")
    print(f"{'─' * 70}")

    demoted_count = 0
    for fname, reason in DEMOTIONS.items():
        fpath = CANON_DIR / fname
        if not fpath.exists():
            print(f"  [SKIP] {fname} — not found")
            continue
        dest = demote_file(fpath, reason, execute=args.execute)
        action = "DEMOTED" if args.execute else "WOULD DEMOTE"
        print(f"  [{action}] {fname}")
        print(f"           → {dest}")
        print(f"           Reason: {reason}")
        demoted_count += 1

    # === T-3: RED RECLASSIFICATIONS ===
    print(f"\n{'─' * 70}")
    print(f"T-3 RED: Volatility corrections ({len(RED_RECLASSIFICATIONS)} files)")
    print(f"{'─' * 70}")

    red_count = 0
    for fname, updates in RED_RECLASSIFICATIONS.items():
        fpath = CANON_DIR / fname
        if not fpath.exists():
            # Might have been demoted
            if fname in [d for d in DEMOTIONS]:
                print(f"  [SKIP] {fname} — already demoted")
            else:
                print(f"  [SKIP] {fname} — not found")
            continue
        reclassify_file(fpath, updates, execute=args.execute)
        action = "RECLASSIFIED" if args.execute else "WOULD RECLASSIFY"
        print(f"  [{action}] {fname}")
        print(f"           volatility_band → {updates['volatility_band']}, refresh_cadence → {updates['refresh_cadence']}")
        red_count += 1

    # === T-3: YELLOW RECLASSIFICATIONS ===
    print(f"\n{'─' * 70}")
    print(f"T-3 YELLOW: Volatility corrections ({len(YELLOW_RECLASSIFICATIONS)} files)")
    print(f"{'─' * 70}")

    yellow_count = 0
    for fname, updates in YELLOW_RECLASSIFICATIONS.items():
        fpath = CANON_DIR / fname
        if not fpath.exists():
            if fname in [d for d in DEMOTIONS]:
                print(f"  [SKIP] {fname} — already demoted")
            else:
                print(f"  [SKIP] {fname} — not found")
            continue
        reclassify_file(fpath, updates, execute=args.execute)
        action = "RECLASSIFIED" if args.execute else "WOULD RECLASSIFY"
        print(f"  [{action}] {fname}")
        print(f"           volatility_band → {updates['volatility_band']}, refresh_cadence → {updates['refresh_cadence']}")
        yellow_count += 1

    # === SUMMARY ===
    print(f"\n{'=' * 70}")
    mode = "EXECUTED" if args.execute else "DRY RUN"
    print(f"{mode} Summary:")
    print(f"  Demotions:              {demoted_count} files")
    print(f"  Red reclassifications:  {red_count} files")
    print(f"  Yellow reclassifications: {yellow_count} files")
    print(f"  Canon files remaining:  {86 - demoted_count}")
    print(f"{'=' * 70}")

    if not args.execute:
        print("\nRun with --execute to apply changes.")


if __name__ == "__main__":
    main()
