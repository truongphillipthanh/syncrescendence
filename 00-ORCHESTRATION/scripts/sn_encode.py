#!/usr/bin/env python3
"""
Semantic Notation Encoder
Transforms verbose prose → SN compressed format

Usage:
    sn_encode.py <file_or_directory> [--dry-run]

Examples:
    sn_encode.py document.md                    # Encode single file
    sn_encode.py 01-CANON/ --dry-run            # Preview encoding
    echo "Syncrescendence" | sn_encode.py -     # Encode stdin
"""

import yaml
import re
import sys
from pathlib import Path
from typing import Dict, Any

# Path to glossary (relative to script location)
SCRIPT_DIR = Path(__file__).parent
GLOSSARY_PATH = SCRIPT_DIR.parent / "notation" / "symbols.yaml"

def load_glossary() -> Dict[str, Any]:
    """Load the Semantic Notation glossary"""
    try:
        with open(GLOSSARY_PATH) as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: Glossary not found at {GLOSSARY_PATH}", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Invalid YAML in glossary: {e}", file=sys.stderr)
        sys.exit(1)

def encode_text(text: str, glossary: Dict[str, Any]) -> str:
    """
    Replace verbose terms with symbols

    Encoding priority:
    1. Root symbol (Ψ)
    2. Chains (I, ℹ, ∴, E, K, W)
    3. Virtues (α, χ, ε, μ, τ)
    4. Relations (prose → operators)
    5. Artifact classes (Κ, Ο, Σ, Δ, Λ)
    """
    result = text

    # Root symbol
    result = re.sub(r'\bSyncrescendence\b', 'Ψ', result)

    # Chains (be careful with single letters - need word boundaries)
    chain_map = {
        'Intelligence': 'I',
        'Information': 'ℹ',
        'Insight': '∴',
        'Expertise': 'E',
        'Knowledge': 'K',
        'Wisdom': 'W'
    }
    for name, symbol in chain_map.items():
        # Match "Intelligence chain" or "Intelligence Chain"
        result = re.sub(rf'\b{name}\s+[Cc]hain\b', f'{symbol}-chain', result)
        # Match standalone "Intelligence" when clearly used as chain
        # (This is conservative - could expand)

    # Virtues
    virtue_map = {
        'Acumen': 'α',
        'Coherence': 'χ',
        'Efficacy': 'ε',
        'Mastery': 'μ',
        'Transcendence': 'τ'
    }
    for name, symbol in virtue_map.items():
        result = re.sub(rf'\b{name}\b', symbol, result)

    # Relations (prose → operators)
    # Order matters - longer phrases first
    relation_replacements = [
        (r'\bis defined as\b', '::'),
        (r'\bexpands to\b', '::'),
        (r'\bconstrained by\b', '|'),
        (r'\bfiltered by\b', '|'),
        (r'\btransforms into\b', '>>'),
        (r'\bflows to\b', '>>'),
        (r'\bcorresponds to\b', '<->'),
        (r'\bimplies\b', '=>'),
        (r'\bproduces\b', '=>'),
    ]

    for pattern, replacement in relation_replacements:
        result = re.sub(pattern, f' {replacement} ', result)

    # Artifact classes (careful - these are single letters)
    # Only replace when clearly in canonical context
    result = re.sub(r'\bCANON\b', 'Κ', result)
    result = re.sub(r'\bOPERATIONAL\b', 'Ο', result)
    result = re.sub(r'\bSOURCE\b', 'Σ', result)
    result = re.sub(r'\bDIRECTIVE\b', 'Δ', result)

    # Clean up spacing around operators
    result = re.sub(r'\s+::\s+', ' :: ', result)
    result = re.sub(r'\s+\|\s+', ' | ', result)
    result = re.sub(r'\s+>>\s+', ' >> ', result)
    result = re.sub(r'\s+=>\s+', ' => ', result)
    result = re.sub(r'\s+<->\s+', ' <-> ', result)

    return result

def encode_file(file_path: Path, glossary: Dict[str, Any], dry_run: bool = False) -> None:
    """Encode a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        encoded = encode_text(content, glossary)

        if dry_run:
            print(f"\n{'='*60}")
            print(f"File: {file_path}")
            print(f"{'='*60}")
            print(encoded)
        else:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(encoded)
            print(f"Encoded: {file_path}")

    except Exception as e:
        print(f"Error encoding {file_path}: {e}", file=sys.stderr)

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    target = sys.argv[1]
    dry_run = '--dry-run' in sys.argv

    glossary = load_glossary()

    # Handle stdin
    if target == '-':
        content = sys.stdin.read()
        encoded = encode_text(content, glossary)
        print(encoded)
        return

    target_path = Path(target)

    # Handle single file
    if target_path.is_file():
        encode_file(target_path, glossary, dry_run)

    # Handle directory
    elif target_path.is_dir():
        md_files = list(target_path.glob("**/*.md"))
        if not md_files:
            print(f"No markdown files found in {target_path}", file=sys.stderr)
            sys.exit(1)

        print(f"Found {len(md_files)} markdown files")
        if dry_run:
            print("DRY RUN - No files will be modified\n")

        for md_file in md_files:
            encode_file(md_file, glossary, dry_run)

    else:
        print(f"Error: {target} is not a file or directory", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
