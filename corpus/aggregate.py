#!/usr/bin/env python3
"""
NUCLEOSYNTHESIS — AGGREGATE phase
Move corpus files into semantic topic folders based on WHAT THEY ARE ABOUT.
No deletions. Bottom-up: topics come from content analysis, not file type.
"""
import os, csv, shutil
from pathlib import Path

CORPUS = Path("/Users/system/syncrescendence/corpus")

# === SEMANTIC TOPIC MAPPING ===
# Map raw TSV topics → semantic folder names (WHAT IT'S ABOUT, not format)
TOPIC_MAP = {
    # --- External knowledge (what the content is about) ---
    "claude-code": "claude-code",
    "openclaw": "openclaw",
    "ai-agents": "multi-agent-systems",
    "ai-general": "ai-general",
    "ai-models": "ai-models",
    "ai-business": "product-business",
    "ai-video": "ai-video-vfx",
    "ai-image": "ai-video-vfx",
    "ai-coding": "vibe-coding",
    "ai-memory": "ai-memory-retrieval",
    "ai-safety": "ai-safety",
    "chatgpt": "ai-models",
    "codex": "ai-models",
    "gemini": "ai-models",
    "cursor": "ai-models",
    "mcp": "multi-agent-systems",
    "content-creation": "writing-creation",
    "design": "design-taste",
    "software-engineering": "vibe-coding",
    "economics-startups": "startup-vc",
    "economics-investing": "product-business",
    "economics-macro": "meaning-civilization",
    "business-organization": "leadership-management",
    "biology-neuroscience": "health-psychology",
    "biology-evolution": "philosophy-esoterica",
    "history": "meaning-civilization",
    "philosophy-consciousness": "philosophy-esoterica",
    "philosophy-epistemology": "philosophy-esoterica",
    "physics-cosmology": "philosophy-esoterica",
    "geopolitics-us-china": "meaning-civilization",
    "geopolitics-russia": "meaning-civilization",
    "geopolitics-europe": "meaning-civilization",
    "infrastructure": "infrastructure",
    "other-ai-tool": "multi-agent-systems",
    "prompt-engineering": "prompt-engineering",
    "self-improvement": "productivity-pkm",
    # --- Syncrescendence internal (still by TOPIC not format) ---
    "sn-architecture": "syncrescendence-architecture",
    "sn-canon": "syncrescendence-canon",
    "sn-certescence": "syncrescendence-certescence",
    "sn-rosetta": "syncrescendence-certescence",
    "sn-atom": "syncrescendence-extraction",
    "sn-pipeline": "syncrescendence-extraction",
    "sn-config": "syncrescendence-config",
    "sn-script": "syncrescendence-operations",
    "sn-prompt": "syncrescendence-operations",
    "sn-system-prompt": "syncrescendence-operations",
    "sn-watchdog": "syncrescendence-operations",
    "sn-task": "syncrescendence-operations",
    "sn-result": "syncrescendence-operations",
    "sn-confirm": "syncrescendence-operations",
    "sn-handoff": "syncrescendence-operations",
    "sn-other": "syncrescendence-other",
}

def load_all_tsvs():
    """Load ALL cluster map TSVs → {filename: topic}"""
    mapping = {}
    # Merge all available TSVs
    tsv_files = [
        "CLUSTER-MAP-CARTOGRAPHER.tsv",
        "CLUSTER-MAP-ADJUDICATOR.tsv",
        "CLUSTER-MAP-08001-09000.tsv",
        "CLUSTER-MAP-09001-10000.tsv",
        "CLUSTER-MAP-10001-11000.tsv",
        "CLUSTER-MAP-11001-11712.tsv",
        "CLUSTER-MAP-FULL.tsv",
    ]
    for tsv_name in tsv_files:
        tsv_path = CORPUS / tsv_name
        if not tsv_path.exists():
            continue
        with open(tsv_path, "r") as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) >= 2:
                    fn = parts[0].strip()
                    topic = parts[1].strip()
                    if fn and topic and topic != "topic":  # skip header
                        # Don't overwrite with less specific
                        if fn not in mapping:
                            mapping[fn] = topic
    return mapping

# Files/patterns to skip (meta-artifacts of this operation)
SKIP_PREFIXES = ("BOTTOMUP-", "CLUSTER-MAP-", "SUBCLUSTER-", "NEARDUPES-", "SEMANTIC-CLUSTERS")
SKIP_EXACT = {
    "aggregate.py", "classifier.py", "adjudicator_classifier.py",
    "strip_filenames.py", "UNDO-NUCLEOSYNTHESIS.sh",
    "CLASSIFICATION_REPORT.txt", "RECLASSIFICATION-VALIDATION.txt",
}

def should_skip(filename):
    if filename in SKIP_EXACT:
        return True
    for prefix in SKIP_PREFIXES:
        if filename.startswith(prefix):
            return True
    return False

def main():
    tsv_map = load_all_tsvs()
    print(f"Loaded {len(tsv_map)} topic entries from TSVs")

    # Collect files in corpus root only
    all_files = [
        f for f in os.listdir(CORPUS)
        if (CORPUS / f).is_file() and not should_skip(f)
    ]
    print(f"Found {len(all_files)} files to aggregate")

    # Classify
    moves = {}  # folder → [files]
    unmapped = []
    for f in all_files:
        topic = tsv_map.get(f)
        if topic:
            folder = TOPIC_MAP.get(topic, topic)
        else:
            folder = "uncategorized"
            unmapped.append(f)
        moves.setdefault(folder, []).append(f)

    # Print plan
    print(f"\n{'Folder':<35} {'Count':>6}")
    print("-" * 43)
    for folder in sorted(moves.keys()):
        print(f"{folder:<35} {len(moves[folder]):>6}")
    print("-" * 43)
    total = sum(len(v) for v in moves.values())
    print(f"{'TOTAL':<35} {total:>6}")
    print(f"\nUnmapped files: {len(unmapped)}")
    if unmapped:
        # Show extension breakdown of unmapped
        from collections import Counter
        ext_counts = Counter(Path(f).suffix for f in unmapped)
        print("Unmapped by extension:")
        for ext, count in ext_counts.most_common(10):
            print(f"  {ext or '(none)'}: {count}")

    # Execute moves
    moved = 0
    errors = 0
    for folder, files in moves.items():
        dest = CORPUS / folder
        dest.mkdir(exist_ok=True)
        for f in files:
            src = CORPUS / f
            dst = dest / f
            if dst.exists():
                print(f"SKIP (exists): {f} → {folder}/")
                continue
            try:
                shutil.move(str(src), str(dst))
                moved += 1
            except Exception as e:
                print(f"ERROR: {f} → {folder}/: {e}")
                errors += 1

    print(f"\nMoved {moved} files into {len(moves)} folders. Errors: {errors}")

if __name__ == "__main__":
    main()
