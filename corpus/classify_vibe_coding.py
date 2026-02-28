#!/usr/bin/env python3
"""Classify vibe-coding/ files — only 6-8% are actual vibe coding."""
import os
import json
import csv
import shutil
from collections import Counter

os.chdir('/Users/system/syncrescendence/corpus')
SRC = "vibe-coding"

def extract_content(filepath):
    try:
        with open(filepath, 'r', errors='replace') as f:
            if filepath.endswith('.jsonl'):
                contents = []
                for i, line in enumerate(f):
                    if i >= 8: break
                    try:
                        obj = json.loads(line.strip())
                        c = obj.get('content', '') or ''
                        if not c and 'payload' in obj:
                            c = obj['payload'].get('content', '') if isinstance(obj['payload'], dict) else ''
                        contents.append(c)
                    except: contents.append(line)
                return ' '.join(contents)
            elif filepath.endswith('.log'):
                return f.read(500)
            else:
                return f.read(2000)
    except:
        return ''

RULES = [
    # Operational/system files first
    (["Cycle complete", "EXEC_TIMEOUT", "completed", "Objective received"], "syncrescendence-operations"),
    (["DYN-BATCH", "schema_version", "generated_at", "atoms_extracted"], "syncrescendence-operations"),
    (["CONFIRM-", "RESULT-", "TASK-", "dispatch", "siege", "handoff"], "syncrescendence-operations"),
    (["canon/", "praxis/", "certescence", "ascertescence", "clarescence"], "syncrescendence-certescence"),
    (["syncrescendence", "constellation", "orchestration/"], "syncrescendence-operations"),

    # Clear non-coding topics
    (["biotech", "drug", "pharma", "clinical trial", "GLP-1", "FDA", "therapeutic"], "ai-biotech"),
    (["geopolit", "military", "defense", "DoD", "national security", "warfare", "Iran", "sanctions"], "geopolitics-grand-strategy"),
    (["Peterson", "sermon", "biblical", "theology", "spiritual", "esoteric", "mysticism", "Kabbalah"], "philosophy-esoterica"),
    (["meaning", "existential", "purpose", "Nietzsche", "human flourishing", "civiliz", "entropy", "telos"], "meaning-civilization"),
    (["philosophy", "metaphysic", "epistemolog", "ontolog", "phenomenolog", "Heidegger"], "philosophy-esoterica"),
    (["health", "psychology", "mental health", "therapy", "neuroscien", "brain", "meditation", "sleep", "nutrition", "longevity", "Bryan Johnson"], "health-psychology"),
    (["leadership", "management", "executive", "org structure", "team building"], "leadership-management"),
    (["startup", "venture capital", "VC ", "Series A", "seed round", "YC ", "fundrais"], "startup-vc"),
    (["Alex Hormozi", "Acquisition.com", "business model", "SaaS", "revenue model", "B2B", "go-to-market"], "product-business"),

    # AI sub-domains that aren't coding
    (["alignment", "safety", "AI risk", "existential risk", "x-risk", "constitutional AI", "RLHF", "red team", "guardrail"], "ai-safety"),
    (["video generat", "VFX", "Sora", "text-to-video", "Runway", "Kling", "Veo"], "ai-video-vfx"),
    (["memory", "retrieval", "RAG", "vector database", "embedding", "knowledge graph", "Graphiti", "long-term memory"], "ai-memory-retrieval"),
    (["multi-agent", "agent coordination", "agent swarm", "agent orchestrat", "PAI framework"], "multi-agent-systems"),
    (["AGI", "superintelligen", "ASI", "singularity", "scaling law", "emergence"], "ai-capability-futures"),

    # Media/news about AI (not coding)
    (["Elon Musk", "Sam Altman", "Dario Amodei", "Jensen", "Satya", "Zuckerberg", "Cathie Wood", "ARK"], "ai-models"),
    (["GPT-5", "Gemini", "Llama", "Grok", "o1", "o3", "benchmark", "MMLU", "leaderboard"], "ai-models"),
    (["open source", "open-source", "Hugging Face", "democratiz", "commoditiz"], "ai-models"),
    (["model release", "announced", "launched", "new model"], "ai-models"),

    # Career/productivity (not coding methodology)
    (["career", "job displace", "skill tree", "hiring", "resume", "workforce", "employment", "layoff", "reskill"], "productivity-pkm"),
    (["productiv", "PKM", "second brain", "note-taking", "workflow", "time management"], "productivity-pkm"),
    (["education", "learning", "certification", "university", "student", "teach"], "productivity-pkm"),

    # Creative/design
    (["writing", "creator economy", "content creation", "storytelling", "narrative", "copywriting"], "writing-creation"),
    (["design", "taste", "aesthetic", "typography", "UX", "UI design", "visual"], "design-taste"),
    (["auteur", "film", "cinema", "documentary", "movie"], "design-taste"),

    # Business/economics
    (["adoption", "ROI", "enterprise AI", "market", "stock", "invest", "billion", "trillion", "revenue"], "product-business"),
    (["China", "Europe", "regulation", "policy", "government", "law", "legislat"], "geopolitics-grand-strategy"),

    # Infrastructure
    (["GPU", "H100", "NVIDIA", "data center", "energy", "thermodynamic", "TSU", "hardware", "chip", "semiconductor"], "infrastructure"),
    (["photonic", "quantum computing", "optical", "laser"], "infrastructure"),
    (["cybersecurity", "malware", "ransomware", "encryption"], "infrastructure"),

    # OpenClaw specific
    (["openclaw", "OpenClaw", "SOUL.md", "HEARTBEAT"], "openclaw"),

    # Prompt engineering (distinct from coding)
    (["prompt engineer", "system prompt", "chain of thought", "few-shot", "prompt template"], "prompt-engineering"),

    # ACTUAL vibe coding / AI-assisted coding — these stay
    (["vibe cod", "vibe-cod", "vibecod"], "vibe-coding"),
    (["claude code", "Claude Code", "claude-code", "cursor", "copilot", "windsurf", "cline", "aider", "codex cli", "Codex CLI"], "claude-code"),
    (["AI coding", "code generation", "code scaffold", "AI-assisted coding", "coding agent", "AI code", "code review"], "vibe-coding"),
    (["coding tool", "IDE", "code editor", "developer tool", "dev tool", "programming tool"], "vibe-coding"),
    (["API", "SDK", "developer", "framework", "library", "programming", "software engineer"], "vibe-coding"),
    (["context engineer", "context window", "token", "inference"], "vibe-coding"),

    # Remaining catch-alls
    (["disruption", "transformation", "future of work", "automation", "replace", "obsolete"], "ai-capability-futures"),
    (["intelligence", "reasoning", "thinking", "problem solving", "decision", "cognit"], "ai-capability-futures"),
    (["agent", "autonomous", "self-organiz", "tool use", "function call"], "multi-agent-systems"),
    (["cost", "price", "compute", "expensive", "cheap"], "ai-models"),
]

def classify(fname, content):
    # Log files
    if fname.endswith('.log'):
        return 'syncrescendence-operations'
    # XML files likely operational
    if fname.endswith('.xml'):
        return 'syncrescendence-operations'
    # Images
    if fname.endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
        return 'design-taste'

    content_lower = content.lower()
    for keywords, dest in RULES:
        for kw in keywords:
            if kw.lower() in content_lower:
                return dest
    return "vibe-coding"  # If nothing else matches, keep in vibe-coding


def main():
    files = sorted(os.listdir(SRC))
    files = [f for f in files if os.path.isfile(os.path.join(SRC, f)) and f != '.DS_Store']

    results = []
    for fname in files:
        fpath = os.path.join(SRC, fname)
        content = extract_content(fpath)
        dest = classify(fname, content)
        results.append((fname, dest))

    # Write TSV
    with open('CLASSIFY-VIBE-CODING.tsv', 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['filename', 'destination'])
        for fname, dest in results:
            w.writerow([fname, dest])

    counts = Counter(dest for _, dest in results)
    print(f"\nTotal files: {len(results)}")
    print(f"\nDestination distribution:")
    for dest, count in counts.most_common():
        print(f"  {dest}: {count}")
    staying = counts.get('vibe-coding', 0)
    print(f"\nStaying in vibe-coding: {staying} ({staying*100/len(results):.1f}%)")

    # Execute moves (only files NOT staying in vibe-coding)
    if '--move' in os.sys.argv:
        moved = 0
        errors = []
        for fname, dest in results:
            if dest == 'vibe-coding':
                continue  # Already here
            src = os.path.join(SRC, fname)
            os.makedirs(dest, exist_ok=True)
            dst = os.path.join(dest, fname)
            if os.path.exists(dst):
                errors.append(f"COLLISION: {fname} in {dest}/")
            elif os.path.exists(src):
                shutil.move(src, dst)
                moved += 1
        print(f"\nMoved: {moved}, Errors: {len(errors)}")
        for e in errors[:10]: print(f"  {e}")
        remaining = [f for f in os.listdir(SRC) if os.path.isfile(os.path.join(SRC, f)) and f != '.DS_Store']
        print(f"Remaining in vibe-coding/: {len(remaining)}")


if __name__ == '__main__':
    main()
