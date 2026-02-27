#!/bin/bash
set -e

# Syncrephoenix Migration — CC43
# Collapses 9+ top-level dirs → 4 (sources, logs, scaffold, canon) + root files
# Every git mv is explicit. No || true silencing. Failures are signals.
#
# SAFE BUILD POINT: Take one before running.
#   git add -A && git commit -m "chore: pre-migration snapshot CC43"

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_ROOT"

echo ""
echo "================================================"
echo "  SYNCREPHOENIX MIGRATION — CC43"
echo "  Repo: $REPO_ROOT"
echo "  HEAD: $(git rev-parse --short HEAD)"
echo "================================================"
echo ""

# ============================================================
# PHASE 0: Create destination structure
# ============================================================
echo "=== Phase 0: Create destinations ==="

mkdir -p logs/state
mkdir -p logs/archive
mkdir -p logs/inbox
mkdir -p logs/outbox
mkdir -p logs/handoffs
mkdir -p logs/sovereign
mkdir -p logs/memory

mkdir -p scaffold/agents
mkdir -p scaffold/engine
mkdir -p scaffold/praxis
mkdir -p scaffold/scripts
mkdir -p scaffold/templates
mkdir -p scaffold/configs
mkdir -p scaffold/collab

echo "  Destinations created."

# ============================================================
# PHASE 1: Kill duplicates first (lowest risk — these are redundant)
# ============================================================
echo ""
echo "=== Phase 1: Eliminate duplicates ==="

# Root-level 00-ORCHESTRATION/ is a stub (2 files + impl/) that duplicates orchestration/00-ORCHESTRATION/
# Move its unique files into orchestration/00-ORCHESTRATION/state/ then delete
if [ -d "00-ORCHESTRATION" ]; then
  for f in 00-ORCHESTRATION/state/IMPLEMENTATION-BACKLOG.md 00-ORCHESTRATION/state/IMPLEMENTATION-MAP.md; do
    if [ -f "$f" ]; then
      target="orchestration/00-ORCHESTRATION/state/$(basename "$f")"
      if [ ! -f "$target" ]; then
        git mv "$f" "$target"
        echo "  Merged: $f → $target"
      else
        git rm "$f"
        echo "  Duplicate removed: $f (already exists at $target)"
      fi
    fi
  done
  # Remove the stub dir
  git rm -rf 00-ORCHESTRATION/ 2>/dev/null && echo "  Removed: 00-ORCHESTRATION/ (stub)" || true
fi

# orchestration/orchestration/ is triple-nested redundancy (2 files)
if [ -d "orchestration/orchestration" ]; then
  # Move any unique files up
  for f in orchestration/orchestration/state/.orchestrator_last_run orchestration/orchestration/state/DYN-CONSTELLATION_STATE.md; do
    if [ -f "$f" ]; then
      target="orchestration/state/$(basename "$f")"
      if [ ! -f "$target" ]; then
        git mv "$f" "$target"
        echo "  Merged up: $f → $target"
      else
        git rm "$f"
        echo "  Duplicate removed: $f"
      fi
    fi
  done
  git rm -rf orchestration/orchestration/ 2>/dev/null && echo "  Removed: orchestration/orchestration/ (triple-nest)" || true
fi

# Empty dirs at sources root: sources/research/, sources/research-notebooks/, sources/_config/
for d in sources/research sources/research-notebooks sources/_config; do
  if [ -d "$d" ]; then
    find "$d" -name ".DS_Store" -delete 2>/dev/null
    rmdir "$d" 2>/dev/null && echo "  Removed empty: $d" || echo "  Not empty, keeping: $d"
  fi
done

# sovereign/ (lowercase) — empty inbox/memory structure, no real files
if [ -d "sovereign" ]; then
  find sovereign/ -name ".DS_Store" -delete 2>/dev/null
  find sovereign/ -type d -empty -delete 2>/dev/null
  rmdir sovereign 2>/dev/null && echo "  Removed empty: sovereign/" || echo "  sovereign/ not empty, keeping"
fi

echo "  Duplicates eliminated."

# ============================================================
# PHASE 2: Move logs (append-only temporal records)
# ============================================================
echo ""
echo "=== Phase 2: Move logs ==="

# -SOVEREIGN/ → logs/sovereign/ (decision queue, pedigrees, syncrephoenix passes)
if [ -d "-SOVEREIGN" ]; then
  git mv -- "-SOVEREIGN" logs/sovereign/
  echo "  -SOVEREIGN/ → logs/sovereign/"
fi

# -INBOX/ → logs/inbox/
if [ -d "-INBOX" ]; then
  git mv -- "-INBOX" logs/inbox/
  echo "  -INBOX/ → logs/inbox/"
fi

# -OUTBOX/ → logs/outbox/
if [ -d "-OUTBOX" ]; then
  git mv -- "-OUTBOX" logs/outbox/
  echo "  -OUTBOX/ → logs/outbox/"
fi

# orchestration/00-ORCHESTRATION/state/ → logs/state/ (146 files — the canonical state)
if [ -d "orchestration/00-ORCHESTRATION/state" ]; then
  git mv orchestration/00-ORCHESTRATION/state logs/state/canonical
  echo "  orchestration/00-ORCHESTRATION/state/ → logs/state/canonical/"
fi

# orchestration/state/ → logs/state/vestigial (45 files — alternate state location)
if [ -d "orchestration/state" ]; then
  git mv orchestration/state logs/state/vestigial
  echo "  orchestration/state/ → logs/state/vestigial/"
fi

# orchestration/00-ORCHESTRATION/archive/ → logs/archive/
if [ -d "orchestration/00-ORCHESTRATION/archive" ]; then
  git mv orchestration/00-ORCHESTRATION/archive logs/archive/
  echo "  orchestration/00-ORCHESTRATION/archive/ → logs/archive/"
fi

# memory/ → logs/memory/ (ingest logs, burndown state)
if [ -d "memory" ]; then
  git mv memory logs/memory/
  echo "  memory/ → logs/memory/"
fi

# ..bfg-report/ → DELETE (git cleanup artifact, not tracked)
if [ -d "..bfg-report" ]; then
  rm -rf "..bfg-report"
  echo "  Deleted: ..bfg-report/ (untracked cleanup artifact)"
fi

echo "  Logs moved."

# ============================================================
# PHASE 3: Move scaffold (operational living core)
# ============================================================
echo ""
echo "=== Phase 3: Move scaffold ==="

# agents/ → scaffold/agents/
if [ -d "agents" ]; then
  git mv agents scaffold/agents/
  echo "  agents/ → scaffold/agents/"
fi

# engine/ → scaffold/engine/
if [ -d "engine" ]; then
  git mv engine scaffold/engine/
  echo "  engine/ → scaffold/engine/"
fi

# praxis/ → scaffold/praxis/
if [ -d "praxis" ]; then
  git mv praxis scaffold/praxis/
  echo "  praxis/ → scaffold/praxis/"
fi

# orchestration/00-ORCHESTRATION/scripts/ → scaffold/scripts/
if [ -d "orchestration/00-ORCHESTRATION/scripts" ]; then
  git mv orchestration/00-ORCHESTRATION/scripts scaffold/scripts/orchestration
  echo "  orchestration/00-ORCHESTRATION/scripts/ → scaffold/scripts/orchestration/"
fi

# orchestration/scripts/ → scaffold/scripts/legacy (4 files)
if [ -d "orchestration/scripts" ]; then
  git mv orchestration/scripts scaffold/scripts/legacy
  echo "  orchestration/scripts/ → scaffold/scripts/legacy/"
fi

# scripts/ (root) → scaffold/scripts/root (2 files: auto_ingest_loop.sh, weekly-eval.sh)
if [ -d "scripts" ]; then
  git mv scripts scaffold/scripts/root
  echo "  scripts/ → scaffold/scripts/root/"
fi

# orchestration/00-ORCHESTRATION/templates/ → scaffold/templates/
if [ -d "orchestration/00-ORCHESTRATION/templates" ]; then
  git mv orchestration/00-ORCHESTRATION/templates scaffold/templates/
  echo "  orchestration/00-ORCHESTRATION/templates/ → scaffold/templates/"
fi

# orchestration/00-ORCHESTRATION/launchd/ → scaffold/configs/launchd/
if [ -d "orchestration/00-ORCHESTRATION/launchd" ]; then
  mkdir -p scaffold/configs/launchd
  git mv orchestration/00-ORCHESTRATION/launchd scaffold/configs/launchd/
  echo "  orchestration/00-ORCHESTRATION/launchd/ → scaffold/configs/launchd/"
fi

# collab/ → scaffold/collab/
if [ -d "collab" ]; then
  git mv collab scaffold/collab/
  echo "  collab/ → scaffold/collab/"
fi

# openclaw/ → scaffold/openclaw/
if [ -d "openclaw" ]; then
  git mv openclaw scaffold/openclaw/
  echo "  openclaw/ → scaffold/openclaw/"
fi

# .constellation/ → scaffold/constellation/
if [ -d ".constellation" ]; then
  git mv .constellation scaffold/constellation
  echo "  .constellation/ → scaffold/constellation/"
fi

# *-EXT.md config deltas → scaffold/configs/
for f in CLAUDE-EXT.md GEMINI-EXT.md GROK-EXT.md OPENCLAW-EXT.md; do
  if [ -f "$f" ]; then
    git mv "$f" scaffold/configs/
    echo "  $f → scaffold/configs/"
  fi
done

# Operational root .md files → scaffold/
for f in BOOT.md WORK-LOOP.md INTER-AGENT.md CONTINUOUS-IMPROVEMENT.md; do
  if [ -f "$f" ]; then
    git mv "$f" scaffold/
    echo "  $f → scaffold/"
  fi
done

# ACTIVE-TASKS.md → logs/ (dynamic ledger)
if [ -f "ACTIVE-TASKS.md" ]; then
  git mv ACTIVE-TASKS.md logs/
  echo "  ACTIVE-TASKS.md → logs/"
fi

# .agents/ skills → scaffold/configs/
if [ -d ".agents" ]; then
  git mv .agents scaffold/configs/agents-skills
  echo "  .agents/ → scaffold/configs/agents-skills/"
fi

echo "  Scaffold moved."

# ============================================================
# PHASE 4: Flatten canon (protected — careful)
# ============================================================
echo ""
echo "=== Phase 4: Flatten canon ==="

# canon/01-CANON/* → canon/ (merge up, remove numbered prefix wrapper)
if [ -d "canon/01-CANON" ]; then
  # Move contents up
  for item in canon/01-CANON/*; do
    if [ -e "$item" ]; then
      git mv "$item" canon/
      echo "  $(basename "$item") → canon/"
    fi
  done
  rmdir canon/01-CANON 2>/dev/null && echo "  Removed: canon/01-CANON/" || true
fi

echo "  Canon flattened."

# ============================================================
# PHASE 5: Flatten sources (bulk — largest volume)
# ============================================================
echo ""
echo "=== Phase 5: Flatten sources ==="

# sources/04-SOURCES/* → sources/ (merge up)
if [ -d "sources/04-SOURCES" ]; then
  for item in sources/04-SOURCES/*; do
    if [ -e "$item" ]; then
      git mv "$item" sources/
      echo "  $(basename "$item") → sources/"
    fi
  done
  rmdir sources/04-SOURCES 2>/dev/null && echo "  Removed: sources/04-SOURCES/" || true
fi

# sources/_meta/ has 1 file (source_index.db) — keep at sources root
echo "  Sources flattened."

# ============================================================
# PHASE 6: Clean up empties and vestigial
# ============================================================
echo ""
echo "=== Phase 6: Cleanup ==="

# Remove whatever remains of orchestration/ (should be empty or near-empty)
if [ -d "orchestration" ]; then
  remaining=$(find orchestration/ -type f -not -name ".DS_Store" 2>/dev/null | wc -l | tr -d ' ')
  if [ "$remaining" = "0" ]; then
    rm -rf orchestration/
    echo "  Removed empty: orchestration/"
  else
    echo "  WARNING: orchestration/ still has $remaining files. Listing:"
    find orchestration/ -type f -not -name ".DS_Store"
  fi
fi

# Clean empty dirs repo-wide
find . -type d -empty -not -path './.git/*' -delete 2>/dev/null
echo "  Empty directories cleaned."

# Remove .DS_Store files
find . -name ".DS_Store" -not -path './.git/*' -delete 2>/dev/null
echo "  .DS_Store files cleaned."

# ============================================================
# PHASE 7: Verify
# ============================================================
echo ""
echo "=== Phase 7: Verify ==="

echo ""
echo "Top-level structure:"
find . -maxdepth 1 -not -name '.' -not -name '.git' -not -name '.gitignore' -not -name '.gitattributes' -not -name '.env.graphiti' -not -name '.claude' -not -name '.gemini' -not -name '.obsidian' -not -name '.cursor' -not -name '.windsurf' -not -name '.agent' | sort

echo ""
echo "Orphan empty dirs:"
find . -type d -empty -not -path './.git/*' 2>/dev/null || echo "  None"

echo ""
echo "File counts per top-level:"
for d in sources logs scaffold canon; do
  count=$(find "$d" -type f 2>/dev/null | wc -l | tr -d ' ')
  echo "  $d/: $count files"
done

echo ""
echo "================================================"
echo "  Migration complete. Review with: git status"
echo "  Then: update AGENTS.md paths + make configs"
echo "  Then: git add -A && git commit"
echo "================================================"
