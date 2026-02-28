#!/usr/bin/env python3
"""Classify and move files from syncrescendence-other/ and uncategorized/."""
import os
import json
import csv
import shutil

os.chdir('/Users/system/syncrescendence/corpus')

def extract_content(filepath):
    try:
        with open(filepath, 'r', errors='replace') as f:
            if filepath.endswith('.jsonl'):
                lines = []
                for i, line in enumerate(f):
                    if i >= 5: break
                    try:
                        obj = json.loads(line.strip())
                        lines.append(obj.get('content', '') or str(obj.get('payload', {}).get('content', '')))
                    except: lines.append(line)
                return ' '.join(lines)
            else:
                return f.read(2000)
    except:
        return ''

# ---- UNCATEGORIZED: mostly scripts/plists ----
def classify_uncategorized(fname, content):
    ext = os.path.splitext(fname)[1]
    if ext in ('.sh', '.py', '.plist', '.applescript', '.yaml', '.yml'):
        content_lower = content.lower()
        # Check for syncrescendence-specific scripts
        if any(kw in content_lower for kw in ['dispatch', 'cockpit', 'ledger', 'pedigree', 'session', 'ingest', 'auto_ingest', 'handoff']):
            return 'syncrescendence-operations'
        if any(kw in content_lower for kw in ['memsync', 'extraction', 'mining', 'quality_gate', 'atom_cluster', 'protease', 'graphiti']):
            return 'syncrescendence-architecture'
        if any(kw in content_lower for kw in ['config', 'triage', 'glossary', 'notation']):
            return 'syncrescendence-config'
        if any(kw in content_lower for kw in ['memory', 'journal', 'state_vector', 'snapshot']):
            return 'productivity-pkm'
        return 'infrastructure'
    if ext == '.md':
        content_lower = content.lower()
        if any(kw in content_lower for kw in ['syncrescendence', 'constellation', 'certescence']):
            return 'syncrescendence-operations'
        return 'infrastructure'
    return 'infrastructure'

# ---- SYNCRESCENDENCE-OTHER ----
def classify_sn_other(fname, content):
    content_lower = content.lower()
    ext = os.path.splitext(fname)[1]

    # Config files
    if ext in ('.yaml', '.yml', '.db', '.db-shm', '.db-wal', '.breaker'):
        return 'syncrescendence-config'
    if ext == '.mmd':
        return 'syncrescendence-architecture'

    # By content
    if any(kw in content_lower for kw in ['confirm-', 'result-', 'task state', 'execution', 'siege', 'clarescence session', 'dispatch']):
        return 'syncrescendence-operations'
    if any(kw in content_lower for kw in ['oauth', 'setup', 'hazel', 'automation rule', 'launchd', 'config']):
        return 'syncrescendence-config'
    if any(kw in content_lower for kw in ['transcript', 'batch', 'url recovery', 'source', 'extraction', 'digest', 'mapping']):
        return 'syncrescendence-extraction'
    if any(kw in content_lower for kw in ['convergence', 'architecture', 'synthesis', 'system design', 'vision']):
        return 'syncrescendence-architecture'
    if any(kw in content_lower for kw in ['council', 'certescence', 'ascertescence', 'governance']):
        return 'syncrescendence-certescence'
    if any(kw in content_lower for kw in ['multi-agent', 'orchestrat', 'agent']):
        return 'multi-agent-systems'
    if any(kw in content_lower for kw in ['model', 'AI ', 'capability', 'alignment', 'safety']):
        return 'ai-models'
    if any(kw in content_lower for kw in ['memory', 'retrieval', 'knowledge graph']):
        return 'ai-memory-retrieval'

    return 'syncrescendence-operations'  # Default for sn-other


def process_folder(folder, classifier):
    files = sorted(os.listdir(folder))
    files = [f for f in files if os.path.isfile(os.path.join(folder, f)) and f != '.DS_Store']

    results = []
    for fname in files:
        fpath = os.path.join(folder, fname)
        content = extract_content(fpath)
        dest = classifier(fname, content)
        results.append((fname, dest))

    return results


def move_files(folder, results):
    moved = 0
    errors = []
    for fname, dest in results:
        src = os.path.join(folder, fname)
        os.makedirs(dest, exist_ok=True)
        dst = os.path.join(dest, fname)
        if os.path.exists(dst):
            errors.append(f"COLLISION: {fname} in {dest}/")
        elif os.path.exists(src):
            shutil.move(src, dst)
            moved += 1
        else:
            errors.append(f"MISSING: {src}")
    return moved, errors


# Process uncategorized
print("=== UNCATEGORIZED ===")
uc_results = process_folder('uncategorized', classify_uncategorized)
from collections import Counter
uc_counts = Counter(d for _, d in uc_results)
for dest, count in uc_counts.most_common():
    print(f"  {dest}: {count}")
uc_moved, uc_errors = move_files('uncategorized', uc_results)
print(f"Moved: {uc_moved}, Errors: {len(uc_errors)}")
for e in uc_errors[:5]: print(f"  {e}")

# Process syncrescendence-other
print("\n=== SYNCRESCENDENCE-OTHER ===")
so_results = process_folder('syncrescendence-other', classify_sn_other)
so_counts = Counter(d for _, d in so_results)
for dest, count in so_counts.most_common():
    print(f"  {dest}: {count}")
so_moved, so_errors = move_files('syncrescendence-other', so_results)
print(f"Moved: {so_moved}, Errors: {len(so_errors)}")
for e in so_errors[:5]: print(f"  {e}")

# Check remainders
for folder in ['uncategorized', 'syncrescendence-other']:
    remaining = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and f != '.DS_Store']
    print(f"\n{folder}/ remaining: {len(remaining)}")
