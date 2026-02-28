#!/usr/bin/env python3
"""Classify syncrescendence-operations/ — extract misrouted content."""
import os
import json
import csv
import shutil
from collections import Counter

os.chdir('/Users/system/syncrescendence/corpus')
SRC = "syncrescendence-operations"

def extract_content(filepath):
    try:
        with open(filepath, 'r', errors='replace') as f:
            return f.read(2000)
    except:
        return ''

# Operational patterns that should STAY
OP_PATTERNS = [
    "TASK-", "CONFIRM-", "RESULT-", "GATE REVIEW", "HANDOFF", "DISPATCH",
    "dispatch", "siege", "execution log", "session state", "inbox", "outbox",
    "WATCHDOG", "watchdog", "ESCALATION", "escalation",
    "batch_report", "DYN-BATCH", "pipeline", "convergence",
    "CLARESCENCE", "clarescence", "ASCERTESCENCE",
    "audit", "AUDIT", "triage", "TRIAGE",
    "SCAFFOLD", "scaffold", "decruft", "DECRUFT",
    "session review", "SESSION REVIEW",
    "RECLASSIFICATION", "DECOMPOSITION",
]

RULES = [
    # Content that should be elsewhere
    (["openclaw", "OpenClaw", "SOUL.md", "opencode"], "openclaw"),
    (["Claude Code", "claude-code", "Claude Skill", "cursor", "copilot", "windsurf", "cline", "aider", "Codex CLI", "codex cli"], "claude-code"),
    (["vibe cod", "AI coding", "code generation", "AI-assisted coding"], "vibe-coding"),
    (["Channel**:", "**Channel**:", "**Published**:", "**Duration**:", "**URL**: https://www.youtube.com"], "MEDIA"),  # YouTube transcripts
    (["multi-agent", "agent coordination", "agent swarm", "PAI framework"], "multi-agent-systems"),
    (["memory", "retrieval", "RAG", "vector database", "embedding", "knowledge graph", "Graphiti"], "ai-memory-retrieval"),
    (["alignment", "safety", "AI risk", "x-risk", "constitutional AI"], "ai-safety"),
    (["AGI", "superintelligen", "ASI", "singularity", "capability"], "ai-capability-futures"),
    (["GPT-5", "Gemini", "Claude Opus", "Claude Sonnet", "Llama", "Grok", "benchmark", "leaderboard"], "ai-models"),
    (["prompt engineer", "system prompt", "prompting", "Prompt Lifecycle"], "prompt-engineering"),
    (["design", "taste", "aesthetic", "typography", "UX"], "design-taste"),
    (["health", "psychology", "mental health", "therapy", "neuroscien", "brain", "GENIUS", "Schopenhauer", "DIVINE"], "health-psychology"),
    (["philosophy", "metaphysic", "esoteric", "mysticism"], "philosophy-esoterica"),
    (["meaning", "existential", "purpose", "civiliz"], "meaning-civilization"),
    (["geopolit", "military", "defense", "China", "Iran"], "geopolitics-grand-strategy"),
    (["startup", "venture capital", "VC ", "fundrais"], "startup-vc"),
    (["business model", "SaaS", "revenue", "entrepreneur", "Analyst Work"], "product-business"),
    (["career", "job", "skill", "hiring", "workforce", "employment"], "productivity-pkm"),
    (["productiv", "PKM", "workflow", "time management"], "productivity-pkm"),
    (["writing", "creator economy", "content creation", "storytelling"], "writing-creation"),
    (["leadership", "management", "executive"], "leadership-management"),
    (["GPU", "NVIDIA", "data center", "energy", "hardware", "DGX", "robotics"], "infrastructure"),
    (["video generat", "VFX", "Sora", "text-to-video"], "ai-video-vfx"),
    (["biotech", "drug", "pharma", "FDA"], "ai-biotech"),
    # Architecture/config
    (["TEMPLATE", "template", "SPECIFICATION", "specification", "format spec"], "syncrescendence-config"),
    (["architecture", "ARCH-", "integration", "convergence map", "system design"], "syncrescendence-architecture"),
    (["APP_ACTIONS", "config", "CONFIG", "ChatGPT Global Memory"], "syncrescendence-config"),
]


def classify(fname, content):
    # Non-MD files: operational by default
    ext = os.path.splitext(fname)[1]
    if ext in ('.log', '.sh', '.py', '.json', '.jsonl', '.yaml', '.yml', '.xml',
               '.plist', '.lock', '.csv', '.applescript', '.complete',
               '.watchdog_state', '.orchestrator_last_run', '.heartbeat'):
        return 'syncrescendence-operations'
    if ext == '' or 'claimed-by' in fname:
        return 'syncrescendence-operations'

    # Check if it's an operational MD
    content_upper = content[:500]
    for pat in OP_PATTERNS:
        if pat in content_upper:
            return 'syncrescendence-operations'

    # Check content rules
    content_lower = content.lower()

    # YouTube/media transcript detection
    if '**Channel**:' in content or '**Published**:' in content:
        # This is a media transcript — classify by content
        for keywords, dest in RULES:
            if dest == "MEDIA":
                continue
            for kw in keywords:
                if kw.lower() in content_lower:
                    return dest
        # Default media to ai-models if no better match
        return 'ai-models'

    for keywords, dest in RULES:
        if dest == "MEDIA":
            continue
        for kw in keywords:
            if kw.lower() in content_lower:
                return dest

    return 'syncrescendence-operations'


def main():
    files = sorted(os.listdir(SRC))
    files = [f for f in files if os.path.isfile(os.path.join(SRC, f)) and f != '.DS_Store']

    # Remove the analysis file the agent created
    analysis = os.path.join(SRC, '00000-DECOMPOSITION-ANALYSIS.md')
    if os.path.exists(analysis):
        os.remove(analysis)
        files = [f for f in files if f != '00000-DECOMPOSITION-ANALYSIS.md']

    results = []
    for fname in files:
        fpath = os.path.join(SRC, fname)
        content = extract_content(fpath)
        dest = classify(fname, content)
        results.append((fname, dest))

    counts = Counter(dest for _, dest in results)
    total = len(results)
    staying = counts.get('syncrescendence-operations', 0)
    print(f"Total files: {total}")
    print(f"Staying in syncrescendence-operations: {staying} ({staying*100/total:.1f}%)")
    print(f"\nDestination distribution:")
    for dest, count in counts.most_common():
        print(f"  {dest}: {count}")

    if '--move' in os.sys.argv:
        moved = 0
        errors = []
        for fname, dest in results:
            if dest == 'syncrescendence-operations':
                continue
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
        print(f"Remaining in syncrescendence-operations/: {len(remaining)}")


if __name__ == '__main__':
    main()
