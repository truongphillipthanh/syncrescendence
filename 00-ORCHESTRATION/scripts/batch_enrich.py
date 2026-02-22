#!/usr/bin/env python3
"""
Batch heuristic enrichment for raw SOURCE-*.md files.
NO API calls — pure pattern matching on title/creator/content.
"""

import os
import re
import sys
import time
from pathlib import Path
from datetime import datetime

SOURCES_DIR = Path("/Users/system/Desktop/syncrescendence/04-SOURCES")
REPORT_PATH = SOURCES_DIR / "_meta" / "ENRICHMENT_BATCH_REPORT.md"

# ── Pattern banks ──────────────────────────────────────────────────────

PARADIGM_PATTERNS = re.compile(
    r'consciousness|intelligence theory|agi\b|artificial general|fundamental|paradigm|philosophy of|physics of|'
    r'theory of mind|emergence|sentien|first principles|ontolog|epistemolog|phenomenolog|metaphysic|'
    r'superintelligen|alignment problem|existential risk|singularity',
    re.IGNORECASE
)
STRATEGIC_PATTERNS = re.compile(
    r'future of|state of|prediction|industry|market|economy|leadership|'
    r'landscape|ecosystem|roadmap|vision for|where.*heading|year in review|'
    r'trillion|billion|geopolitic|macro|strategy|competitive|moat',
    re.IGNORECASE
)
TACTICAL_PATTERNS = re.compile(
    r'tutorial|how to|guide|setup|configure|tips|tricks|workflow|walkthrough|step.by.step|'
    r'getting started|crash course|in \d+ minutes|beginner|hands.on|demo|quickstart',
    re.IGNORECASE
)

TELEOLOGY_IMPLEMENT = re.compile(
    r'tutorial|how to|walkthrough|setup|install|build|deploy|configur|hands.on|demo|'
    r'step.by.step|getting started|crash course|beginner|quickstart',
    re.IGNORECASE
)
TELEOLOGY_STRATEGIZE = re.compile(
    r'prediction|industry|state of|future of|landscape|roadmap|year in review|trend|forecast|'
    r'where.*heading|market|strategy|competitive',
    re.IGNORECASE
)
TELEOLOGY_SYNTHESIZE = re.compile(
    r'interview|panel|discussion|conversation|debate|roundtable|fireside|chat with|talks with|'
    r'podcast|dialogue|q\s*&\s*a',
    re.IGNORECASE
)
TELEOLOGY_CONTEXTUALIZE = re.compile(
    r'history|background|explain|origins|evolution of|story of|how.*became|rise of|fall of|'
    r'timeline|retrospective',
    re.IGNORECASE
)
TELEOLOGY_INSPIRE = re.compile(
    r'motivat|vision|inspir|creative|dream|manifesto|keynote|commencement|ted\s*talk|'
    r'why i|my journey|life lesson',
    re.IGNORECASE
)
TELEOLOGY_REFERENCE = re.compile(
    r'documentation|spec|announcement|release|changelog|what\'s new|update|launch|'
    r'official|paper|whitepaper|arxiv',
    re.IGNORECASE
)

# notebooklm_category patterns
CAT_CLAUDE = re.compile(r'claude|anthropic|claude.code|sonnet|opus|haiku', re.IGNORECASE)
CAT_CODING_TOOLS = re.compile(r'codex|cursor|windsurf|vscode|vs.code|ide\b|developer tool|copilot|cline|aider|bolt', re.IGNORECASE)
CAT_AI_ENG = re.compile(r'\bmodel\b|training|fine.tun|architecture|neural|transformer|llm|gpt|gemini|llama|mistral|token|embedding|inference|benchmark|eval', re.IGNORECASE)
CAT_AGENTS = re.compile(r'\bagent|swarm|orchestrat|multi.agent|mcp\b|tool.use|function.call|langchain|langgraph|autogen|crew.?ai|a2a\b', re.IGNORECASE)
CAT_PHILOSOPHY = re.compile(r'consciousness|intelligence\b|philosophy|physics|quantum|epistemolog|ontolog|metaphysic|hermetic|esoteric|occult|alchemy|mysticism|spiritual', re.IGNORECASE)
CAT_CAREER = re.compile(r'career|startup|founder|business|entrepreneur|freelanc|interview prep|salary|hiring|job|resume|portfolio', re.IGNORECASE)
CAT_VIBE = re.compile(r'vibe.cod|v0\b|design|ui\b|ux\b|frontend|tailwind|css|figma|shadcn|next\.?js|react|svelte|web.dev', re.IGNORECASE)
CAT_PROMPT = re.compile(r'prompt|prompting|system prompt|chain.of.thought|few.shot|zero.shot|jailbreak', re.IGNORECASE)
CAT_CREATIVE = re.compile(r'video gen|vfx|image gen|creative ai|sora\b|midjourney|dall.e|stable diffusion|comfyui|runway|pika|kling|hailuo|flux', re.IGNORECASE)


def parse_duration_minutes(duration_str):
    """Parse '1h 3m 43s' or '35m 58s' to minutes."""
    if not duration_str:
        return 0
    h = re.search(r'(\d+)h', duration_str)
    m = re.search(r'(\d+)m', duration_str)
    total = 0
    if h:
        total += int(h.group(1)) * 60
    if m:
        total += int(m.group(1))
    return total


def classify_signal_tier(title, content, duration_min):
    text = f"{title} {content}"
    if PARADIGM_PATTERNS.search(text):
        return "paradigm"
    if STRATEGIC_PATTERNS.search(text):
        return "strategic"
    if TACTICAL_PATTERNS.search(text):
        return "tactical"
    return "tactical" if duration_min < 20 else "strategic"


def classify_teleology(title, content, fmt):
    text = f"{title} {content}"
    if TELEOLOGY_IMPLEMENT.search(text):
        return "implement"
    if TELEOLOGY_STRATEGIZE.search(text):
        return "strategize"
    if TELEOLOGY_SYNTHESIZE.search(text):
        return "synthesize"
    if TELEOLOGY_CONTEXTUALIZE.search(text):
        return "contextualize"
    if TELEOLOGY_INSPIRE.search(text):
        return "inspire"
    if TELEOLOGY_REFERENCE.search(text):
        return "reference"
    # Defaults based on format
    if fmt in ("interview", "panel"):
        return "synthesize"
    if fmt in ("tutorial",):
        return "extract"
    return "strategize"


def classify_category(title, creator):
    text = f"{title} {creator}"
    if CAT_CLAUDE.search(text):
        return "claude-code"
    if CAT_CODING_TOOLS.search(text):
        return "coding-tools"
    if CAT_AGENTS.search(text):
        return "agents-orchestration"
    if CAT_PROMPT.search(text):
        return "prompt-engineering"
    if CAT_CREATIVE.search(text):
        return "ai-creative-media"
    if CAT_VIBE.search(text):
        return "vibe-coding"
    if CAT_PHILOSOPHY.search(text):
        return "philosophy-paradigm"
    if CAT_CAREER.search(text):
        return "career-growth"
    if CAT_AI_ENG.search(text):
        return "ai-engineering"
    return "ai-engineering"


def extract_topics(title):
    """Extract 3-5 topic tags from title."""
    # Remove common filler words
    stop = {'the','a','an','of','in','on','for','to','and','or','is','are','was','with','by','at','from','how','what','why','when','this','that','it','its','i','my','your','we','our','do','does','did','can','could','will','would','should','has','have','had','be','been','being','not','no','all','every','each','you','they','them','he','she','his','her','about'}
    # Clean title
    clean = re.sub(r'[^\w\s]', ' ', title.lower())
    words = [w for w in clean.split() if w not in stop and len(w) > 2]
    # Take first 5 unique
    seen = []
    for w in words:
        if w not in seen:
            seen.append(w)
        if len(seen) >= 5:
            break
    return seen


def generate_synopsis(title, creator, topics, fmt):
    fmt_label = {
        "interview": "interview", "panel": "panel discussion", "lecture": "lecture",
        "tutorial": "tutorial", "solo_presentation": "presentation",
        "essay": "essay", "article": "article", "paper": "paper",
    }.get(fmt, "video")
    topic_str = ", ".join(topics[:3]) if topics else "various topics"
    return f"{title} by {creator}. A {fmt_label} covering {topic_str}."


def generate_aliases(title):
    """Generate 1-2 short aliases from title."""
    aliases = []
    # Truncated version
    words = title.split()
    if len(words) > 4:
        aliases.append(" ".join(words[:4]))
    if len(words) > 2:
        aliases.append(" ".join(words[:min(len(words), 6)]))
    else:
        aliases.append(title)
    return aliases[:2]


def enrich_file(filepath):
    """Read, classify, and rewrite frontmatter for a single file. Returns True if modified."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Parse frontmatter
    fm_match = re.match(r'^---\n(.*?\n)---\n', content, re.DOTALL)
    if not fm_match:
        return False

    fm_text = fm_match.group(1)
    body = content[fm_match.end():]

    # Check if already enriched
    st_match = re.search(r'^signal_tier:\s*(.*?)$', fm_text, re.MULTILINE)
    syn_match = re.search(r'^synopsis:\s*(.*?)$', fm_text, re.MULTILINE)
    if not st_match or not syn_match:
        return False
    st_val = st_match.group(1).strip().strip('"')
    syn_val = syn_match.group(1).strip().strip('"')
    if st_val not in ('null', '') or syn_val not in ('null', ''):
        return False

    # Extract fields
    title = ""
    t = re.search(r'^title:\s*"?(.+?)"?\s*$', fm_text, re.MULTILINE)
    if t:
        title = t.group(1)

    creator = ""
    c = re.search(r'^creator:\s*"?(.+?)"?\s*$', fm_text, re.MULTILINE)
    if c:
        creator = c.group(1)

    fmt = ""
    f = re.search(r'^format:\s*(\S+)', fm_text, re.MULTILINE)
    if f:
        fmt = f.group(1)

    duration_str = ""
    d = re.search(r'^duration:\s*"?(.+?)"?\s*$', fm_text, re.MULTILINE)
    if d:
        duration_str = d.group(1)

    duration_min = parse_duration_minutes(duration_str)
    # Use first 2000 chars of body for classification
    snippet = body[:2000]
    text_for_classify = f"{title} {snippet}"

    # Classify
    signal_tier = classify_signal_tier(title, snippet, duration_min)
    teleology = classify_teleology(title, snippet, fmt)
    category = classify_category(title, creator)
    topics = extract_topics(title)
    synopsis = generate_synopsis(title, creator, topics, fmt)
    aliases = generate_aliases(title)

    # Build new frontmatter
    new_fm = fm_text

    # Replace signal_tier
    new_fm = re.sub(r'^(signal_tier:\s*).*$', f'\\1{signal_tier}', new_fm, flags=re.MULTILINE)

    # Replace synopsis
    new_fm = re.sub(r'^(synopsis:\s*).*$', f'\\1"{synopsis}"', new_fm, flags=re.MULTILINE)

    # Replace topics
    if topics:
        topics_yaml = "\n".join(f'  - "{t}"' for t in topics)
        new_fm = re.sub(r'^topics:\s*\[\]', f'topics:\n{topics_yaml}', new_fm, flags=re.MULTILINE)

    # Add new fields if missing (before the closing ---)
    has_teleology = 'teleology:' in fm_text
    has_category = 'notebooklm_category:' in fm_text
    has_aliases = 'aliases:' in fm_text

    additions = ""
    if not has_teleology:
        additions += f"teleology: {teleology}\n"
    if not has_category:
        additions += f"notebooklm_category: {category}\n"
    if not has_aliases:
        aliases_yaml = "\n".join(f'  - "{a}"' for a in aliases)
        additions += f"aliases:\n{aliases_yaml}\n"

    # If fields exist but are null, replace them
    if has_teleology:
        new_fm = re.sub(r'^(teleology:\s*).*$', f'\\1{teleology}', new_fm, flags=re.MULTILINE)
    if has_category:
        new_fm = re.sub(r'^(notebooklm_category:\s*).*$', f'\\1{category}', new_fm, flags=re.MULTILINE)

    new_content = f"---\n{new_fm}{additions}---\n{body}"

    with open(filepath, 'w', encoding='utf-8') as fout:
        fout.write(new_content)

    return True


def main():
    start = time.time()
    files = sorted(SOURCES_DIR.glob("SOURCE-*.md"))
    print(f"Found {len(files)} SOURCE files")

    enriched = 0
    skipped = 0
    errors = []
    category_counts = {}
    tier_counts = {}
    teleology_counts = {}

    for i, fp in enumerate(files):
        try:
            # Quick check before full parse
            with open(fp, 'r', encoding='utf-8', errors='replace') as f:
                head = f.read(2000)
            st = re.search(r'signal_tier:\s*(null|"null"|\s*$)', head)
            syn = re.search(r'synopsis:\s*(null|"null"|\s*$)', head)
            if not (st and syn):
                skipped += 1
                continue

            if enrich_file(fp):
                enriched += 1
                # Track stats from what we just wrote
                with open(fp, 'r', encoding='utf-8', errors='replace') as f:
                    new_head = f.read(2000)
                for field, counts in [('signal_tier', tier_counts), ('teleology', teleology_counts), ('notebooklm_category', category_counts)]:
                    m = re.search(rf'^{field}:\s*(\S+)', new_head, re.MULTILINE)
                    if m:
                        v = m.group(1)
                        counts[v] = counts.get(v, 0) + 1
            else:
                skipped += 1
        except Exception as e:
            errors.append((fp.name, str(e)))

        if (i + 1) % 100 == 0:
            elapsed = time.time() - start
            print(f"  [{i+1}/{len(files)}] enriched={enriched} skipped={skipped} errors={len(errors)} ({elapsed:.1f}s)")

    elapsed = time.time() - start
    print(f"\nDone: {enriched} enriched, {skipped} skipped, {len(errors)} errors in {elapsed:.1f}s")

    # Write report
    report = f"""# Enrichment Batch Report

**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Duration**: {elapsed:.1f}s
**Total SOURCE files scanned**: {len(files)}
**Enriched**: {enriched}
**Skipped (already enriched)**: {skipped}
**Errors**: {len(errors)}

## Signal Tier Distribution

| Tier | Count |
|------|-------|
"""
    for k in sorted(tier_counts, key=tier_counts.get, reverse=True):
        report += f"| {k} | {tier_counts[k]} |\n"

    report += f"""
## Teleology Distribution

| Teleology | Count |
|-----------|-------|
"""
    for k in sorted(teleology_counts, key=teleology_counts.get, reverse=True):
        report += f"| {k} | {teleology_counts[k]} |\n"

    report += f"""
## NotebookLM Category Distribution

| Category | Count |
|----------|-------|
"""
    for k in sorted(category_counts, key=category_counts.get, reverse=True):
        report += f"| {k} | {category_counts[k]} |\n"

    if errors:
        report += "\n## Errors\n\n"
        for name, err in errors[:50]:
            report += f"- `{name}`: {err}\n"

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_PATH, 'w') as f:
        f.write(report)
    print(f"Report written to {REPORT_PATH}")


if __name__ == "__main__":
    main()
