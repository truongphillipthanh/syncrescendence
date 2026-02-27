#!/usr/bin/env python3
"""
Semantic Notation Decoder
Transforms SN compressed format → verbose prose

Usage:
    sn_decode.py <file_or_text>

Examples:
    sn_decode.py document.md                # Decode file
    sn_decode.py "Ψ :: civilizational infrastructure"  # Decode text
    echo "α >> ε" | sn_decode.py -          # Decode stdin
"""
from config import *

import yaml
import re
import sys
from pathlib import Path
from typing import Dict, Any

# Path to glossary (relative to script location)
SCRIPT_DIR = Path(__file__).parent
GLOSSARY_PATH = SCRIPT_DIR / "sn_symbols.yaml"

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

def decode_text(text: str, glossary: Dict[str, Any]) -> str:
    """
    Replace symbols with verbose terms

    Decoding priority (reverse of encoding):
    1. Operators → prose
    2. Artifact classes → words
    3. Virtues → words
    4. Chains → words
    5. Root symbol → word
    """
    result = text

    # Operators → prose (spacing important)
    result = result.replace(' :: ', ' is defined as ')
    result = result.replace(' | ', ' constrained by ')
    result = result.replace(' >> ', ' transforms into ')
    result = result.replace(' => ', ' implies ')
    result = result.replace(' <-> ', ' corresponds to ')
    result = result.replace(' := ', ' binds to ')
    result = result.replace(' -> ', ' becomes ')

    # Artifact classes
    result = re.sub(r'(?<![a-zA-Z])Κ(?![a-zA-Z])', 'CANON', result)
    result = re.sub(r'(?<![a-zA-Z])Ο(?![a-zA-Z])', 'OPERATIONAL', result)
    result = re.sub(r'(?<![a-zA-Z])Σ(?![a-zA-Z])', 'SOURCE', result)
    result = re.sub(r'(?<![a-zA-Z])Δ(?![a-zA-Z])', 'DIRECTIVE', result)
    result = re.sub(r'(?<![a-zA-Z])Λ(?![a-zA-Z])', 'LOG', result)

    # Virtues
    virtue_reverse = {
        'α': 'Acumen',
        'χ': 'Coherence',
        'ε': 'Efficacy',
        'μ': 'Mastery',
        'τ': 'Transcendence'
    }
    for symbol, name in virtue_reverse.items():
        # Use word boundaries for safety
        result = re.sub(rf'(?<![a-zA-Z]){re.escape(symbol)}(?![a-zA-Z])', name, result)

    # Chains
    chain_reverse = {
        'I': 'Intelligence',
        'ℹ': 'Information',
        '∴': 'Insight',
        'E': 'Expertise',
        'K': 'Knowledge',
        'W': 'Wisdom'
    }

    # Handle chain notation (e.g., "I-chain" → "Intelligence Chain")
    for symbol, name in chain_reverse.items():
        escaped_symbol = re.escape(symbol)
        result = re.sub(rf'{escaped_symbol}-chain\b', f'{name} Chain', result)

        # Handle standalone usage (be conservative)
        # Only if clearly not part of another word
        if symbol in ['ℹ', '∴']:  # Safe symbols (not common letters)
            result = re.sub(rf'(?<![a-zA-Z]){escaped_symbol}(?![a-zA-Z])', name, result)

    # Root symbol (do last to avoid interfering)
    result = result.replace('Ψ', 'Syncrescendence')

    return result

def decode_file(file_path: Path, glossary: Dict[str, Any]) -> None:
    """Decode a single file and print to stdout"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        decoded = decode_text(content, glossary)
        print(decoded)

    except Exception as e:
        print(f"Error decoding {file_path}: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    target = sys.argv[1]
    glossary = load_glossary()

    # Handle stdin
    if target == '-':
        content = sys.stdin.read()
        decoded = decode_text(content, glossary)
        print(decoded)
        return

    # Check if target is a file
    target_path = Path(target)
    if target_path.exists() and target_path.is_file():
        decode_file(target_path, glossary)
    else:
        # Treat as inline text
        decoded = decode_text(target, glossary)
        print(decoded)

if __name__ == "__main__":
    main()
