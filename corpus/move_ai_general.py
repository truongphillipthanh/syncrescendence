#!/usr/bin/env python3
"""Move ai-general files to their classified destinations."""
import csv
import os
import shutil

os.chdir('/Users/system/syncrescendence/corpus')

# Read classification
moves = {}
with open('CLASSIFY-AI-GENERAL.tsv') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        moves[row['filename']] = row['destination']

# Create new folders if needed
for dest in set(moves.values()):
    os.makedirs(dest, exist_ok=True)

# Execute moves
moved = 0
errors = []
for fname, dest in moves.items():
    src = os.path.join('ai-general', fname)
    dst = os.path.join(dest, fname)
    if os.path.exists(src):
        if os.path.exists(dst):
            errors.append(f"COLLISION: {fname} already exists in {dest}/")
        else:
            shutil.move(src, dst)
            moved += 1
    else:
        errors.append(f"MISSING: {src}")

print(f"Moved: {moved}")
print(f"Errors: {len(errors)}")
for e in errors[:20]:
    print(f"  {e}")

# Check what's left
remaining = os.listdir('ai-general')
remaining = [f for f in remaining if os.path.isfile(os.path.join('ai-general', f))]
print(f"\nFiles remaining in ai-general/: {len(remaining)}")
