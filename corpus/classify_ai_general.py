#!/usr/bin/env python3
"""
Bottom-up classifier for ai-general/ files.
Reads each file, extracts key content, assigns to a destination folder.
"""
import os
import json
import re
import csv
import sys

SRC = "ai-general"

# Destination mapping - based on bottom-up analysis of 200 sampled files
# Each entry: (keywords_in_content, destination_folder)
RULES = [
    # Specific domains first (narrowest matches)
    (["biotech", "drug", "pharma", "clinical trial", "GLP-1", "protein folding", "Eroom", "FDA", "therapeutic", "genomic"], "ai-biotech"),
    (["geopolit", "military", "defense", "DoD", "national security", "warfare", "NATO", "deterrence", "sanctions", "Iran", "IRGC"], "geopolitics-grand-strategy"),
    (["cybersecurity", "malware", "ransomware", "zero-day", "post-quantum", "encryption"], "infrastructure"),

    # Syncrescendence-specific
    (["syncrescendence", "constellation", "certescence", "ascertescence", "clarescence", "protease", "canon/", "praxis/", "orchestration/"], "syncrescendence-operations"),
    (["openclaw", "OpenClaw", "SOUL.md", "HEARTBEAT"], "openclaw"),

    # AI sub-domains
    (["multi-agent", "agent coordination", "agent swarm", "agent orchestrat", "MAS ", "constellation agent", "PAI framework", "Mission Control"], "multi-agent-systems"),
    (["claude code", "Claude Code", "claude-code", "cursor", "copilot", "windsurf", "cline", "aider", "codex cli", "Codex CLI"], "claude-code"),
    (["vibe cod", "vibe-cod", "vibecod", "AI coding", "code generation", "code scaffold", "AI-assisted coding", "coding agent"], "vibe-coding"),
    (["memory", "retrieval", "RAG", "vector database", "embedding", "knowledge graph", "Graphiti", "long-term memory", "context window"], "ai-memory-retrieval"),
    (["alignment", "safety", "AI risk", "existential risk", "x-risk", "alignment tax", "constitutional AI", "RLHF", "red team"], "ai-safety"),
    (["video generat", "VFX", "Sora", "text-to-video", "Runway", "Kling", "Veo", "Luma"], "ai-video-vfx"),
    (["prompt engineer", "system prompt", "chain of thought", "few-shot", "prompt template", "jailbreak"], "prompt-engineering"),

    # Business/career
    (["startup", "venture capital", "VC ", "Series A", "seed round", "YC ", "Y Combinator", "fundrais", "valuation"], "startup-vc"),
    (["Alex Hormozi", "Acquisition.com", "Skool.com", "entrepreneur", "business model", "SaaS", "revenue model", "B2B", "go-to-market"], "product-business"),
    (["career", "job displace", "skill tree", "hiring", "resume", "interview", "workforce", "employment", "layoff", "reskill"], "productivity-pkm"),
    (["productiv", "PKM", "second brain", "note-taking", "Obsidian", "Notion", "workflow", "time management", "GTD"], "productivity-pkm"),

    # Philosophy/meaning
    (["meaning", "existential", "purpose", "Nietzsche", "philosophy of work", "human flourishing", "civiliz", "entropy", "telos"], "meaning-civilization"),
    (["philosophy", "metaphysic", "epistemolog", "ontolog", "phenomenolog", "Heidegger", "Wittgenstein", "esoteric", "occult", "mysticism", "Kabbalah", "hermeticism"], "philosophy-esoterica"),
    (["Peterson", "sermon", "biblical", "religious", "theology", "spiritual"], "philosophy-esoterica"),

    # Creative/design
    (["writing", "creator economy", "content creation", "storytelling", "narrative", "copywriting", "publishing"], "writing-creation"),
    (["design", "taste", "aesthetic", "typography", "UX", "UI design", "visual"], "design-taste"),
    (["leadership", "management", "executive", "org structure", "team building", "delegation"], "leadership-management"),

    # Health
    (["health", "psychology", "mental health", "therapy", "cogniti", "neuroscien", "brain", "meditation", "mindfulness", "sleep", "exercise", "nutrition", "longevity", "Bryan Johnson"], "health-psychology"),

    # Infrastructure/hardware
    (["GPU", "H100", "NVIDIA", "data center", "energy", "terawatt", "gigawatt", "thermodynamic", "TSU", "hardware", "chip", "semiconductor", "TSMC"], "infrastructure"),

    # Broader AI topics - these catch remaining files
    (["model release", "announced", "launched", "new model", "benchmark", "MMLU", "leaderboard", "Gemini", "GPT-5", "Claude", "Llama", "Grok", "o1", "o3"], "ai-models"),
    (["AGI", "superintelligen", "ASI", "capability", "scaling law", "emergence", "paradigm shift", "singularity", "timeline"], "ai-capability-futures"),
    (["open source", "open-source", "Hugging Face", "democratiz", "moat", "commoditiz"], "ai-models"),
    (["Elon Musk", "Sam Altman", "Dario Amodei", "Sundar", "Jensen", "Satya", "Zuckerberg", "Cathie Wood", "ARK"], "ai-models"),
    (["adoption", "ROI", "enterprise AI", "AI transformation", "digital transform"], "product-business"),

    # Remainder catch rules (from bottom-up inspection of 137 unclassified)
    (["Langlands", "set theory", "computability", "mathematical proof", "conjecture", "category theory", "topology", "algebraic geometry", "theorem", "axiom"], "philosophy-esoterica"),
    (["hallucination", "failure mode", "robustness", "guardrail", "trustworth", "reliability"], "ai-safety"),
    (["renaissance", "cultural shift", "liberation", "post-labor", "printing press", "industrial revolution", "enlightenment", "societal impact"], "meaning-civilization"),
    (["photonic", "quantum computing", "optical", "laser", "material science"], "infrastructure"),
    (["disruption", "transformation", "future of work", "automation", "replace", "obsolete"], "ai-capability-futures"),
    (["education", "learning", "certification", "university", "student", "teach", "classroom", "school"], "productivity-pkm"),
    (["market", "stock", "invest", "portfolio", "financial", "billion", "trillion", "revenue", "profit"], "product-business"),
    (["agent", "autonomous", "self-organiz", "loop", "tool use", "function call"], "multi-agent-systems"),
    (["intelligence", "reasoning", "thinking", "problem solving", "decision", "cognit"], "ai-capability-futures"),
    (["API", "SDK", "developer", "integration", "platform", "framework", "library", "tool"], "vibe-coding"),
    (["China", "US ", "Europe", "regulation", "policy", "government", "law", "legislat"], "geopolitics-grand-strategy"),
    (["cost", "price", "token", "compute", "inference cost", "expensive", "cheap"], "ai-models"),
]

# File-type overrides for operational files
LOG_DEST = "syncrescendence-operations"
# System JSONL = has these keys AND does NOT have content/payload (content atoms have both)
SYSTEM_JSONL_KEYS = {"generated_at", "session_id", "atoms_extracted", "result", "state", "signal", "energy_audit_status"}
CONTENT_ATOM_KEYS = {"content", "payload", "atom_id", "category"}


def extract_content(filepath):
    """Extract searchable content from a file."""
    try:
        with open(filepath, 'r', errors='replace') as f:
            if filepath.endswith('.jsonl'):
                lines = []
                contents = []
                for i, line in enumerate(f):
                    if i >= 8:
                        break
                    lines.append(line.strip())
                    try:
                        obj = json.loads(line.strip())
                        # For content atoms, extract content field
                        if 'content' in obj:
                            contents.append(obj['content'])
                        # For system records, include the raw JSON keys
                        elif 'payload' in obj and isinstance(obj['payload'], dict):
                            contents.append(obj['payload'].get('content', ''))
                    except json.JSONDecodeError:
                        contents.append(line)
                # Return raw first line + extracted content for dual classification
                raw = lines[0] if lines else ''
                return raw + '\n' + ' '.join(contents)
            elif filepath.endswith('.log'):
                return f.read(500)
            else:
                return f.read(1500)
    except Exception as e:
        return ''


def classify(filepath, content):
    """Classify content into a destination folder."""
    # Log files → operations
    if filepath.endswith('.log'):
        return LOG_DEST
    # System JSONL (batch reports, state snapshots, not content atoms)
    if filepath.endswith('.jsonl'):
        try:
            first_line = content.split('\n')[0] if content else ''
            obj = json.loads(first_line) if first_line.strip() else {}
            has_system = any(k in obj for k in SYSTEM_JSONL_KEYS)
            has_content = any(k in obj for k in CONTENT_ATOM_KEYS)
            if has_system and not has_content:
                return LOG_DEST
        except (json.JSONDecodeError, Exception):
            pass
    content_lower = content.lower()
    for keywords, dest in RULES:
        for kw in keywords:
            if kw.lower() in content_lower:
                return dest
    return "ai-general-remainder"


# Manual overrides for files that slip through keyword rules
MANUAL = {
    "00716.md": "syncrescendence-operations",
    "01270.jsonl": "ai-models", "01271.jsonl": "ai-models",
    "01312.jsonl": "product-business", "01313.jsonl": "product-business",
    "01546.jsonl": "meaning-civilization", "01547.jsonl": "meaning-civilization",
    "01660.jsonl": "claude-code", "01661.jsonl": "claude-code",
    "01903.jsonl": "ai-capability-futures", "01904.jsonl": "ai-capability-futures",
    "02044.jsonl": "ai-models", "02045.jsonl": "ai-models",
    "02047.jsonl": "ai-models", "02048.jsonl": "ai-models",
    "02119.jsonl": "ai-models", "02120.jsonl": "ai-models",
    "02185.jsonl": "ai-models", "02186.jsonl": "ai-models",
    "02377.jsonl": "vibe-coding", "02378.jsonl": "vibe-coding",
    "02953.jsonl": "philosophy-esoterica", "02954.jsonl": "philosophy-esoterica",
    "02989.jsonl": "ai-models", "02990.jsonl": "ai-models",
    "03157.jsonl": "geopolitics-grand-strategy", "03158.jsonl": "geopolitics-grand-strategy",
    "03163.jsonl": "meaning-civilization", "03164.jsonl": "meaning-civilization",
    "03265.jsonl": "ai-models", "03266.jsonl": "ai-models",
    "03943.jsonl": "ai-models", "03944.jsonl": "ai-models",
    "01570.jsonl": "product-business", "01571.jsonl": "product-business",
    "10001.md": "product-business",  # All-In predictions = business/VC
    "10083.md": "vibe-coding",  # Theo t3.gg = dev content
    "10150.md": "ai-safety",  # Signal privacy
    "10346.md": "productivity-pkm",  # AI feature ranking
    "10724.md": "productivity-pkm",  # AI user outcomes
}


def main():
    results = []
    files = sorted(os.listdir(SRC))
    files = [f for f in files if os.path.isfile(os.path.join(SRC, f))]

    for fname in files:
        if fname in MANUAL:
            results.append((fname, MANUAL[fname]))
            continue
        fpath = os.path.join(SRC, fname)
        content = extract_content(fpath)
        dest = classify(fpath, content)
        results.append((fname, dest))

    # Write TSV
    with open('CLASSIFY-AI-GENERAL.tsv', 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['filename', 'destination'])
        for fname, dest in results:
            w.writerow([fname, dest])

    # Summary
    from collections import Counter
    counts = Counter(dest for _, dest in results)
    print(f"\nTotal files: {len(results)}")
    print(f"\nDestination distribution:")
    for dest, count in counts.most_common():
        print(f"  {dest}: {count}")

    remainder = counts.get('ai-general-remainder', 0)
    print(f"\nUnclassified remainder: {remainder} ({remainder*100/len(results):.1f}%)")


if __name__ == '__main__':
    os.chdir('/Users/system/syncrescendence/corpus')
    main()
