#!/usr/bin/env python3
"""
Semantic Notation Variable Expander
Resolves ${DEF_NAME.field} references in SN documents

Usage:
    sn_expand.py <file_or_directory> [--dry-run] [--check]
    sn_expand.py --list-defs

Examples:
    sn_expand.py 01-CANON/sn/                   # Expand all SN files
    sn_expand.py document.md --dry-run           # Preview expansions
    sn_expand.py 01-CANON/sn/ --check            # Report unresolved refs
    sn_expand.py --list-defs                     # Show all available DEFs
    echo '${AvatarMap.Commander.platform}' | sn_expand.py -
"""

import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Path to DEF source (relative to script location)
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent
DEF_PATH = REPO_ROOT / "02-ENGINE" / "DEF-CONSTELLATION_VARIABLES.md"

# Pattern for DEF variable references: ${DefName.field.subfield}
REF_PATTERN = re.compile(r'\$\{(\w+(?:\.\w+)*)\}')


def parse_def_blocks(content: str) -> Dict[str, Any]:
    """Parse DEF blocks from the variables file into a nested dict."""
    defs = {}
    current_def = None
    current_block = []
    in_code_block = False

    for line in content.splitlines():
        # Track code block boundaries
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        if not in_code_block:
            continue

        # Inside the code block, parse DEF blocks
        if line.startswith('DEF '):
            if current_def and current_block:
                defs[current_def] = parse_def_body(current_block)
            match = re.match(r'^DEF\s+(\w+):', line)
            if match:
                current_def = match.group(1)
                current_block = []
        elif line.strip() == 'end':
            if current_def and current_block:
                defs[current_def] = parse_def_body(current_block)
            current_def = None
            current_block = []
        elif current_def is not None:
            current_block.append(line)

    return defs


def parse_def_body(lines: List[str]) -> Dict[str, Any]:
    """Parse the body of a DEF block into a structured dict.

    Handles YAML-like indented structure with key: value pairs.
    """
    result = {}
    current_section = None
    indent_stack = []  # Track (indent_level, dict_ref, key)

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue

        indent = len(line) - len(line.lstrip())

        # Key: value pair
        match = re.match(r'^(\s*)(\w+):\s*(.*)', line)
        if match:
            key = match.group(2)
            value = match.group(3).strip()

            if value:
                # Clean value: remove quotes, handle lists
                value = clean_value(value)
                set_nested(result, key, value, indent, indent_stack)
            else:
                # Section header — value will be built from children
                set_nested(result, key, {}, indent, indent_stack)
        elif stripped.startswith('- '):
            # List item
            item_text = stripped[2:].strip()
            if item_text.startswith('{') and item_text.endswith('}'):
                # Inline dict: {key: val, key2: val2}
                item = parse_inline_dict(item_text)
            else:
                item = clean_value(item_text)
            # Append to the most recent list-compatible parent
            append_to_parent(result, item, indent, indent_stack)

    return result


def clean_value(value: str) -> Any:
    """Clean a parsed value — strip quotes, convert types."""
    if value == 'null' or value == 'None':
        return None
    if value == 'true' or value == 'True':
        return True
    if value == 'false' or value == 'False':
        return False

    # Strip surrounding quotes
    if (value.startswith('"') and value.endswith('"')) or \
       (value.startswith("'") and value.endswith("'")):
        return value[1:-1]

    # Try numeric
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            pass

    # List notation [item1, item2]
    if value.startswith('[') and value.endswith(']'):
        inner = value[1:-1]
        if not inner.strip():
            return []
        items = split_respecting_brackets(inner)
        return [clean_value(item.strip()) for item in items]

    return value


def parse_inline_dict(text: str) -> Dict[str, Any]:
    """Parse {key: val, key2: val2} inline dict."""
    text = text.strip('{}').strip()
    result = {}
    for pair in split_respecting_brackets(text):
        pair = pair.strip()
        if ':' in pair:
            k, v = pair.split(':', 1)
            result[k.strip()] = clean_value(v.strip())
    return result


def split_respecting_brackets(text: str) -> List[str]:
    """Split on commas but respect brackets and quotes."""
    items = []
    depth = 0
    current = []
    in_quote = False
    quote_char = None

    for ch in text:
        if ch in ('"', "'") and not in_quote:
            in_quote = True
            quote_char = ch
            current.append(ch)
        elif ch == quote_char and in_quote:
            in_quote = False
            current.append(ch)
        elif ch in ('(', '[', '{') and not in_quote:
            depth += 1
            current.append(ch)
        elif ch in (')', ']', '}') and not in_quote:
            depth -= 1
            current.append(ch)
        elif ch == ',' and depth == 0 and not in_quote:
            items.append(''.join(current))
            current = []
        else:
            current.append(ch)

    if current:
        items.append(''.join(current))
    return items


def set_nested(result: dict, key: str, value: Any, indent: int,
               stack: list) -> None:
    """Set a value in nested dict based on indentation."""
    # Pop stack entries deeper than or equal to current indent
    while stack and stack[-1][0] >= indent:
        stack.pop()

    if stack:
        parent_dict = stack[-1][1]
        if isinstance(parent_dict, dict):
            parent_dict[key] = value
    else:
        result[key] = value

    if isinstance(value, dict):
        stack.append((indent, value, key))


def append_to_parent(result: dict, item: Any, indent: int,
                     stack: list) -> None:
    """Append a list item to the appropriate parent."""
    # Find the right parent — look for the most recent dict value at lower indent
    target = None
    for i in range(len(stack) - 1, -1, -1):
        _, container, key = stack[i]
        if isinstance(container, dict):
            # Find the key whose value should be a list
            for k, v in container.items():
                if isinstance(v, list):
                    target = v
                    break
                elif isinstance(v, dict):
                    for kk, vv in v.items():
                        if isinstance(vv, list):
                            target = vv
                            break
            if target:
                break

    if target is not None:
        target.append(item)
    else:
        # Fall back: find the 'value' key in the spec section
        if 'value' in result.get('spec', {}):
            val = result['spec']['value']
            if isinstance(val, list):
                val.append(item)
            elif val == {} or val is None:
                result['spec']['value'] = [item]


def resolve_ref(defs: Dict[str, Any], ref_path: str) -> Optional[str]:
    """Resolve a dotted reference path against the DEF store.

    Examples:
        resolve_ref(defs, "AvatarMap.Commander.platform")
        resolve_ref(defs, "PlatformBudget.value")
        resolve_ref(defs, "ChainNames")
    """
    parts = ref_path.split('.')
    if not parts:
        return None

    def_name = parts[0]
    if def_name not in defs:
        return None

    current = defs[def_name]

    # Navigate the path
    for part in parts[1:]:
        if isinstance(current, dict):
            # Try direct key
            if part in current:
                current = current[part]
            # Try in spec.value
            elif 'spec' in current and isinstance(current['spec'], dict):
                if 'value' in current['spec']:
                    val = current['spec']['value']
                    if isinstance(val, dict) and part in val:
                        current = val[part]
                    else:
                        return None
                elif part in current['spec']:
                    current = current['spec'][part]
                else:
                    return None
            elif 'value' in current and isinstance(current['value'], dict):
                if part in current['value']:
                    current = current['value'][part]
                else:
                    return None
            else:
                return None
        elif isinstance(current, list):
            # Try numeric index
            try:
                idx = int(part)
                current = current[idx]
            except (ValueError, IndexError):
                return None
        else:
            return None

    # Format the resolved value
    if isinstance(current, dict):
        # For dicts, return the whole DEF block if at top level
        if len(parts) == 1:
            return format_def_summary(current)
        return format_dict(current)
    elif isinstance(current, list):
        return ', '.join(str(item) for item in current)
    elif current is None:
        return 'null'
    else:
        return str(current)


def format_def_summary(def_block: Dict[str, Any]) -> str:
    """Format a full DEF block as a concise summary."""
    sutra = def_block.get('sutra', '')
    if sutra:
        return sutra
    gloss = def_block.get('gloss', '')
    if gloss:
        return gloss.strip()
    return str(def_block)


def format_dict(d: Dict[str, Any]) -> str:
    """Format a dict as a readable string."""
    parts = []
    for k, v in d.items():
        if v is not None:
            parts.append(f"{k}: {v}")
    return ', '.join(parts)


def expand_text(text: str, defs: Dict[str, Any]) -> Tuple[str, int, List[str]]:
    """Expand all ${...} references in text.

    Returns: (expanded_text, num_expanded, list_of_unresolved)
    """
    expanded_count = 0
    unresolved = []

    def replacer(match):
        nonlocal expanded_count
        ref_path = match.group(1)
        resolved = resolve_ref(defs, ref_path)
        if resolved is not None:
            expanded_count += 1
            return resolved
        else:
            unresolved.append(ref_path)
            return match.group(0)  # Leave unresolved refs as-is

    result = REF_PATTERN.sub(replacer, text)
    return result, expanded_count, unresolved


def process_file(filepath: Path, defs: Dict[str, Any], dry_run: bool = False,
                 check_only: bool = False) -> Tuple[int, List[str]]:
    """Process a single file, expanding DEF references."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except (UnicodeDecodeError, PermissionError) as e:
        print(f"  Skipping {filepath}: {e}", file=sys.stderr)
        return 0, []

    refs = REF_PATTERN.findall(content)
    if not refs:
        return 0, []

    expanded, count, unresolved = expand_text(content, defs)

    if check_only:
        if refs:
            print(f"  {filepath}: {len(refs)} refs ({count} resolvable, {len(unresolved)} unresolved)")
            for u in unresolved:
                print(f"    UNRESOLVED: ${{{u}}}")
        return count, unresolved

    if dry_run:
        print(f"\n--- {filepath} ---")
        for ref in refs:
            resolved = resolve_ref(defs, ref)
            status = f"→ {resolved}" if resolved else "UNRESOLVED"
            print(f"  ${{{ref}}} {status}")
        return count, unresolved

    if count > 0:
        filepath.write_text(expanded, encoding='utf-8')
        print(f"  {filepath}: {count} refs expanded")

    return count, unresolved


def list_defs(defs: Dict[str, Any]) -> None:
    """Print all available DEF names and their top-level structure."""
    print("Available DEF blocks:\n")
    for name, block in sorted(defs.items()):
        sutra = block.get('sutra', '(no sutra)')
        print(f"  {name}: {sutra}")

        # Show navigable paths
        spec = block.get('spec', {})
        value = spec.get('value', {}) if isinstance(spec, dict) else None
        if isinstance(value, dict):
            for key in value:
                print(f"    .{key}")
                if isinstance(value[key], dict):
                    for subkey in value[key]:
                        print(f"      .{key}.{subkey}")
        elif isinstance(value, list) and value:
            sample = value[0]
            if isinstance(sample, dict):
                for key in sample:
                    print(f"    [n].{key}")
        print()


def main():
    args = sys.argv[1:]

    if not args:
        print(__doc__)
        sys.exit(0)

    dry_run = '--dry-run' in args
    check_only = '--check' in args
    list_mode = '--list-defs' in args

    # Remove flags from args
    args = [a for a in args if not a.startswith('--')]

    # Load DEF blocks
    if not DEF_PATH.exists():
        print(f"Error: DEF file not found at {DEF_PATH}", file=sys.stderr)
        sys.exit(1)

    defs = parse_def_blocks(DEF_PATH.read_text(encoding='utf-8'))
    print(f"Loaded {len(defs)} DEF blocks from {DEF_PATH.name}")

    if list_mode:
        list_defs(defs)
        return

    if not args:
        print("Error: No file or directory specified", file=sys.stderr)
        sys.exit(1)

    target = args[0]
    total_expanded = 0
    all_unresolved = []

    if target == '-':
        # Stdin mode
        content = sys.stdin.read()
        expanded, count, unresolved = expand_text(content, defs)
        print(expanded)
        return

    target_path = Path(target)
    if not target_path.exists():
        # Try relative to repo root
        target_path = REPO_ROOT / target
        if not target_path.exists():
            print(f"Error: {target} not found", file=sys.stderr)
            sys.exit(1)

    if target_path.is_file():
        count, unresolved = process_file(target_path, defs, dry_run, check_only)
        total_expanded += count
        all_unresolved.extend(unresolved)
    elif target_path.is_dir():
        for filepath in sorted(target_path.rglob('*.md')):
            count, unresolved = process_file(filepath, defs, dry_run, check_only)
            total_expanded += count
            all_unresolved.extend(unresolved)
    else:
        print(f"Error: {target} is not a file or directory", file=sys.stderr)
        sys.exit(1)

    # Summary
    print(f"\nTotal: {total_expanded} refs expanded", end='')
    if all_unresolved:
        unique_unresolved = sorted(set(all_unresolved))
        print(f", {len(unique_unresolved)} unique unresolved refs:")
        for u in unique_unresolved:
            print(f"  ${{{u}}}")
    else:
        print()


if __name__ == '__main__':
    main()
