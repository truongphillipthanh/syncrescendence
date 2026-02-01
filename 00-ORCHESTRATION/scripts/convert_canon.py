#!/usr/bin/env python3
"""
CANON SN Converter
Transforms CANON documents to Semantic Notation format

Usage:
    convert_canon.py <input.md> [output.md]

Examples:
    convert_canon.py 01-CANON/CANON-00002.md
    convert_canon.py 01-CANON/CANON-00007.md 01-CANON/sn-converted/CANON-00007.md
"""

import sys
import re
from pathlib import Path

# Attempt to import sn_encode
try:
    SCRIPT_DIR = Path(__file__).parent
    GLOSSARY_PATH = SCRIPT_DIR / "sn_symbols.yaml"

    import yaml

    def load_glossary():
        with open(GLOSSARY_PATH) as f:
            return yaml.safe_load(f)

    def encode_text(text: str, glossary: dict) -> str:
        """Simple encoding - replace common patterns"""
        result = text
        result = re.sub(r'\bSyncrescendence\b', 'Ψ', result)
        result = re.sub(r'\bis defined as\b', '::', result)
        result = re.sub(r'\btransforms into\b', '>>', result)
        result = re.sub(r'\bconstrained by\b', '|', result)
        result = re.sub(r'\bimplies\b', '=>', result)
        return result

except Exception as e:
    print(f"Warning: Could not load glossary: {e}")
    print("Proceeding with basic conversion...")

    def load_glossary():
        return {}

    def encode_text(text: str, glossary: dict) -> str:
        return text

def extract_frontmatter(content: str) -> tuple:
    """Extract YAML frontmatter if present"""
    if not content.startswith('---'):
        return "", content

    end_idx = content.find('---', 3)
    if end_idx == -1:
        return "", content

    frontmatter = content[:end_idx+3]
    body = content[end_idx+3:].lstrip('\n')
    return frontmatter, body

def extract_sections(content: str) -> list:
    """Extract markdown sections as conversion units"""
    sections = []
    current_section = {"level": 0, "title": "Root", "content": []}

    for line in content.split('\n'):
        if line.startswith('#'):
            # Save previous section
            if current_section["content"]:
                sections.append(current_section)

            # Start new section
            level = len(re.match(r'^#+', line).group())
            title = line.lstrip('#').strip()
            current_section = {"level": level, "title": title, "content": []}
        else:
            current_section["content"].append(line)

    # Save last section
    if current_section["content"]:
        sections.append(current_section)

    return sections

def generate_sutra(title: str, content_lines: list) -> str:
    """Generate one-line sutra from section"""
    # Find first meaningful sentence
    text = ' '.join(content_lines).strip()

    # Remove markdown formatting
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)  # Links
    text = re.sub(r'\*\*([^\*]+)\*\*', r'\1', text)  # Bold
    text = re.sub(r'\*([^\*]+)\*', r'\1', text)  # Italic
    text = re.sub(r'`([^`]+)`', r'\1', text)  # Code

    # Get first sentence
    sentences = re.split(r'[.!?]\s+', text)
    if sentences:
        sutra = sentences[0].strip()
        if len(sutra) > 100:
            sutra = sutra[:97] + "..."
        return sutra

    return title

def detect_block_type(title: str, content: str) -> str:
    """Determine appropriate SN block type"""
    title_lower = title.lower()
    content_lower = content.lower()

    # NORM indicators
    norm_keywords = ['must', 'should', 'may', 'forbidden', 'required', 'constraint', 'rule', 'principle', 'invariant']
    if any(kw in title_lower or kw in content_lower[:200] for kw in norm_keywords):
        if 'must' in content_lower[:500] or 'should' in content_lower[:500]:
            return 'NORM'

    # PROC indicators
    proc_keywords = ['process', 'procedure', 'protocol', 'workflow', 'step', 'execute']
    if any(kw in title_lower for kw in proc_keywords):
        if 'step' in content_lower or '>>' in content:
            return 'PROC'

    # TEST indicators
    if 'test' in title_lower or 'verify' in title_lower or 'validation' in title_lower:
        return 'TEST'

    # ARTIFACT indicators
    if 'artifact' in title_lower or 'output' in title_lower or 'deliverable' in title_lower:
        return 'ARTIFACT'

    # Default to TERM
    return 'TERM'

def section_to_sn_block(section: dict, glossary: dict) -> str:
    """Convert a section to SN block format"""
    title = section["title"]
    content_lines = section["content"]
    content = '\n'.join(content_lines).strip()

    if not content or len(content) < 20:
        return ""

    # Generate components
    block_type = detect_block_type(title, content)
    sutra = generate_sutra(title, content_lines)

    # Create safe identifier from title
    identifier = re.sub(r'[^a-zA-Z0-9]', '', title)
    if not identifier:
        identifier = "Unnamed"

    # Encode content for gloss (first 300 chars as summary)
    encoded_content = encode_text(content, glossary)
    gloss_text = encoded_content[:300].strip()
    if len(encoded_content) > 300:
        gloss_text += "..."

    # Build SN block
    block = f"""{block_type} {identifier}:
    sutra: "{sutra}"
    gloss:
        {gloss_text}
end
"""
    return block

def convert_canon_file(input_path: Path, output_path: Path):
    """Convert a CANON file to SN format"""
    print(f"\n{'='*60}")
    print(f"Converting: {input_path.name}")
    print(f"{'='*60}\n")

    glossary = load_glossary()

    # Read input
    with open(input_path, encoding='utf-8') as f:
        content = f.read()

    original_size = len(content)
    original_words = len(content.split())

    # Extract frontmatter
    frontmatter, body = extract_frontmatter(content)

    # Extract sections
    sections = extract_sections(body)
    print(f"Found {len(sections)} sections")

    # Convert each section to SN block
    blocks = []
    for i, section in enumerate(sections, 1):
        print(f"  Section {i}: {section['title']} ({len(section['content'])} lines)")
        block = section_to_sn_block(section, glossary)
        if block:
            blocks.append(block)

    # Assemble output
    if frontmatter:
        output = frontmatter + "\n\n"
    else:
        output = ""

    output += f"# {input_path.stem} (SN Format)\n\n"
    output += "**Note**: This is a Semantic Notation compressed version.\n"
    output += f"**Original**: {original_words:,} words, {original_size:,} characters\n\n"
    output += "---\n\n"
    output += "\n\n".join(blocks)

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)

    # Calculate metrics
    converted_size = len(output)
    converted_words = len(output.split())
    char_compression = (1 - converted_size / original_size) * 100
    word_compression = (1 - converted_words / original_words) * 100

    print(f"\n{'='*60}")
    print(f"Conversion Complete")
    print(f"{'='*60}")
    print(f"Original:   {original_size:,} chars, {original_words:,} words")
    print(f"Converted:  {converted_size:,} chars, {converted_words:,} words")
    print(f"Reduction:  {char_compression:.1f}% chars, {word_compression:.1f}% words")
    print(f"Output:     {output_path}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Error: {input_path} does not exist")
        sys.exit(1)

    # Default output path
    if len(sys.argv) > 2:
        output_path = Path(sys.argv[2])
    else:
        output_path = Path(f"01-CANON/sn-converted/{input_path.name}")

    convert_canon_file(input_path, output_path)
