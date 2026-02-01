#!/usr/bin/env python3
"""
Smart CANON SN Converter
Transforms CANON documents to Semantic Notation format with structure preservation.
"""

import sys
import re
from pathlib import Path
import yaml

# Attempt to load glossary logic
try:
    SCRIPT_DIR = Path(__file__).parent
    GLOSSARY_PATH = SCRIPT_DIR.parent / "notation" / "symbols.yaml"

    def load_glossary():
        if GLOSSARY_PATH.exists():
            with open(GLOSSARY_PATH) as f:
                return yaml.safe_load(f)
        return {}

    def encode_text(text: str, glossary: dict) -> str:
        """
        Replace verbose terms with symbols based on rules + glossary.
        """
        result = text
        
        # 1. Root symbol
        result = re.sub(r'\bSyncrescendence\b', 'Ψ', result)

        # 2. Chains
        chain_map = {
            'Intelligence': 'I', 'Information': 'ℹ', 'Insight': '∴',
            'Expertise': 'E', 'Knowledge': 'K', 'Wisdom': 'W'
        }
        for name, symbol in chain_map.items():
            result = re.sub(rf'\b{name}\s+[Cc]hain\b', f'{symbol}-chain', result)

        # 3. Virtues
        virtue_map = {
            'Acumen': 'α', 'Coherence': 'χ', 'Efficacy': 'ε',
            'Mastery': 'μ', 'Transcendence': 'τ'
        }
        for name, symbol in virtue_map.items():
            result = re.sub(rf'\b{name}\b', symbol, result)

        # 4. Relations
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

        # 5. Artifact classes
        # Protect paths: Only replace CANON if not part of a path (preceded by / or -)
        result = re.sub(r'(?<![/\-\w])CANON(?![/\w])', 'Κ', result)
        result = re.sub(r'(?<![/\-\w])OPERATIONAL(?![/\w])', 'Ο', result)
        result = re.sub(r'(?<![/\-\w])SOURCE(?![/\w])', 'Σ', result)
        result = re.sub(r'(?<![/\-\w])DIRECTIVE(?![/\w])', 'Δ', result)

        # Cleanup
        result = re.sub(r'\s+::\s+', ' :: ', result)
        result = re.sub(r'\s+\|\s+', ' | ', result)
        result = re.sub(r'\s+>>\s+', ' >> ', result)

        return result

except Exception as e:
    print(f"Warning: Dependency missing: {e}")
    def load_glossary(): return {}
    def encode_text(t, g): return t

def extract_frontmatter(content: str) -> tuple:
    if not content.startswith('---'):
        return "", content
    end_idx = content.find('---', 3)
    if end_idx == -1:
        return "", content
    return content[:end_idx+3], content[end_idx+3:].lstrip('\n')

def extract_sections(content: str) -> list:
    sections = []
    # Match headers #, ##, ###
    # We treat any header as a potential block start
    # But we want to group content under the nearest header
    
    lines = content.split('\n')
    current_section = {"level": 0, "title": "Root", "content": []}
    
    for line in lines:
        header_match = re.match(r'^(#+)\s+(.+)', line)
        if header_match:
            # Save previous
            if current_section["content"] or current_section["title"] != "Root":
                 # Filter out empty sections
                 if any(l.strip() for l in current_section["content"]):
                     sections.append(current_section)
            
            level = len(header_match.group(1))
            title = header_match.group(2).strip()
            current_section = {"level": level, "title": title, "content": []}
        else:
            current_section["content"].append(line)
            
    if current_section["content"]:
        sections.append(current_section)
        
    return sections

def detect_block_type(title: str, content_lines: list) -> str:
    content = "\n".join(content_lines).lower()
    title_lower = title.lower()
    
    if any(k in title_lower for k in ['must', 'should', 'constraint', 'rule', 'norm', 'protocol']):
        return 'NORM'
    if any(k in title_lower for k in ['process', 'procedure', 'workflow', 'steps', 'how to']):
        return 'PROC'
    if any(k in title_lower for k in ['test', 'validation', 'verify']):
        return 'TEST'
    if any(k in title_lower for k in ['artifact', 'output', 'file', 'csv']):
        return 'ARTIFACT'
    if any(k in title_lower for k in ['transform', 'convert']):
        return 'PASS'
        
    return 'TERM'

def generate_sutra(content_lines: list) -> str:
    # Find first meaningful sentence
    for line in content_lines:
        clean = line.strip()
        if not clean: continue
        if clean.startswith(('-', '*', '#', '>')): continue
        if len(clean) < 10: continue # Skip short fragments/numbers
        
        # Clean markdown links/formatting
        clean = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', clean)
        clean = re.sub(r'\*\*|\*', '', clean)
        
        sentences = re.split(r'[.!?]', clean)
        if sentences:
            sutra = sentences[0].strip()
            if len(sutra) > 97:
                return sutra[:97] + "..."
            return sutra
    return "Defined as per spec."

def parse_spec(content_lines: list, glossary: dict) -> str:
    """
    Parses content into a structured spec body.
    Detects key-value pairs (bold keys), lists, etc.
    """
    spec_lines = []
    
    for line in content_lines:
        encoded = encode_text(line, glossary)
        clean = encoded.strip()
        
        if not clean:
            continue
            
        # Detect Key-Value: "**Key**: Value" or "- **Key**: Value"
        kv_match = re.match(r'^[\-\*]?\s*\*\*([^\*]+)\*\*:\s*(.+)', clean)
        if kv_match:
            key = kv_match.group(1).lower().replace(' ', '_')
            val = kv_match.group(2).strip()
            spec_lines.append(f"        {key}: {val}")
            continue
            
        # Detect List items: "- item" or "* item"
        if clean.startswith(('- ', '* ')): 
            spec_lines.append(f"        - {clean[2:].strip()}")
            continue
            
        # Detect Blockquotes as notes or invariants
        if clean.startswith('>'):
            spec_lines.append(f"        note: \"{clean[1:].strip()}\"")
            continue

        # Default: just append text (maybe commented or as a generic list item if it looks like a paragraph)
        # To avoid breaking YAML, we'll put free text as comments or under a 'desc' list if consecutive
        # For simplicity, we'll just indent it as a raw line, but that might break valid YAML.
        # Safer: Make it a comment or a list item
        spec_lines.append(f"        # {clean}")

    return "\n".join(spec_lines)

def convert_section(section: dict, glossary: dict) -> str:
    title = section['title']
    content = section['content']
    
    # Skip preamble-ish sections if they are empty
    if not any(c.strip() for c in content):
        return ""

    block_type = detect_block_type(title, content)
    
    # Create Identifier (PascalCase)
    identifier = "".join(x for x in title.title() if x.isalnum())
    
    sutra = generate_sutra(content)
    
    # Gloss: take first paragraph
    gloss = []
    capture = False
    for line in content:
        if line.strip() and not line.startswith(('#', '-', '*', '>')):
            capture = True
            gloss.append(encode_text(line.strip(), glossary))
        elif capture and not line.strip():
            break # End of paragraph
            
    gloss_text = " ".join(gloss)
    if not gloss_text:
        gloss_text = f"See spec for details on {title}."
    
    if len(gloss_text) > 300:
        gloss_text = gloss_text[:297] + "..."

    spec_body = parse_spec(content, glossary)
    
    # Fallback if spec is empty
    if not spec_body.strip():
        spec_body = "        content: |"
        for line in content:
            if line.strip():
                 spec_body += f"\n            {encode_text(line, glossary)}"

    return f"""{block_type} {identifier}:
    sutra: \"{sutra}\" 
    gloss:
        {gloss_text}
    spec:
{spec_body}
end
"""

def process_file(input_path: Path, output_path: Path, glossary: dict):
    print(f"Processing {input_path}...")
    with open(input_path, 'r', encoding='utf-8') as f:
        raw = f.read()
        
    frontmatter, body = extract_frontmatter(raw)
    sections = extract_sections(body)
    
    blocks = []
    for sec in sections:
        blk = convert_section(sec, glossary)
        if blk:
            blocks.append(blk)
            
    # Add metadata to frontmatter
    if frontmatter:
        lines = frontmatter.splitlines()
        if lines[-1] == '---':
            lines = lines[:-1]
        lines.append(f"sn_version: 1.0")
        lines.append(f"converted: 2026-01-23")
        lines.append("---")
        frontmatter = "\n".join(lines)
    else:
        frontmatter = "---\nsn_version: 1.0\nconverted: 2026-01-23\n---"

    final_output = frontmatter + "\n\n" + "\n\n".join(blocks)
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_output)

def main():
    if len(sys.argv) < 2:
        print("Usage: smart_convert.py <file_or_dir> [output_dir]")
        sys.exit(1)
        
    input_path = Path(sys.argv[1])
    glossary = load_glossary()
    
    if input_path.is_file():
        if len(sys.argv) > 2:
            out = Path(sys.argv[2])
        else:
            out = input_path.parent / "sn-converted" / input_path.name
        process_file(input_path, out, glossary)
        
    elif input_path.is_dir():
        out_dir = input_path
        if len(sys.argv) > 2:
            out_dir = Path(sys.argv[2])
        else:
            out_dir = input_path / "sn-converted"
            
        for md in input_path.glob("**/*.md"):
            # Avoid processing already converted files if output dir is inside input dir
            if "sn-converted" in str(md): continue
            
            rel_path = md.relative_to(input_path)
            dest = out_dir / rel_path
            process_file(md, dest, glossary)

if __name__ == "__main__":
    main()
