#!/usr/bin/env bash
# verify_all.sh
# Comprehensive repository verification

set -e

# Move to repo root
cd "$(git rev-parse --show-toplevel)"

echo ""
echo "========================================"
echo "   Syncrescendence Verification Suite   "
echo "========================================"
echo ""

# Structure verification
echo "-- Structure Verification ----------------"
echo -n "| Unexpected subdirectories: "
SUBDIRS=$(find . -mindepth 2 -type d -name "scaffolding" 2>/dev/null | wc -l | tr -d ' ')
if [ "$SUBDIRS" -eq 0 ]; then
    echo "+ 0"
else
    echo "x $SUBDIRS"
fi

echo "| Root .md files:"
for f in CLAUDE.md README.md AGENTS.md GEMINI.md; do
    if [ -f "$f" ]; then
        echo "|   + $f"
    else
        echo "|   x $f MISSING"
    fi
done
EXTRA=$(ls *.md 2>/dev/null | grep -v -E '^(CLAUDE|BRIDGE|AGENTS|GEMINI)\.md$' | head -5)
if [ -n "$EXTRA" ]; then
    echo "|   ! Unexpected: $EXTRA"
fi

echo -n "| Directory count: "
DIR_COUNT=$(find . -maxdepth 1 -type d -not -name '.' -not -name '.?*' 2>/dev/null | wc -l | tr -d ' ')
echo "$DIR_COUNT"
echo "------------------------------------------"
echo ""

# Orchestration hardening verification
echo "-- Orchestration Hardening ----------------"
if [ -x "00-ORCHESTRATION/scripts/verify_orchestration_hardening.sh" ]; then
    if bash "00-ORCHESTRATION/scripts/verify_orchestration_hardening.sh"; then
        echo "| + Hardened orchestration checks passed"
    else
        echo "| x Hardened orchestration checks failed"
    fi
else
    echo "| ! verify_orchestration_hardening.sh not found"
fi
echo "------------------------------------------"
echo ""

# Ledger verification
echo "-- Ledger Verification -------------------"
echo -n "| DYN-TASKS.csv: "
if [ -f "00-ORCHESTRATION/state/DYN-TASKS.csv" ]; then
    TASKS=$(wc -l < 00-ORCHESTRATION/state/DYN-TASKS.csv | tr -d ' ')
    DONE=$(grep -c ',done,' 00-ORCHESTRATION/state/DYN-TASKS.csv 2>/dev/null || echo 0)
    echo "+ $TASKS rows ($DONE done)"
else
    echo "x Not found"
fi

echo -n "| DYN-PROJECTS.csv: "
if [ -f "00-ORCHESTRATION/state/DYN-PROJECTS.csv" ]; then
    PROJECTS=$(wc -l < 00-ORCHESTRATION/state/DYN-PROJECTS.csv | tr -d ' ')
    COMPLETE=$(grep -c ',complete,' 00-ORCHESTRATION/state/DYN-PROJECTS.csv 2>/dev/null || echo 0)
    echo "+ $PROJECTS rows ($COMPLETE complete)"
else
    echo "x Not found"
fi

echo -n "| DYN-SOURCES.csv: "
if [ -f "04-SOURCES/DYN-SOURCES.csv" ]; then
    SOURCES=$(wc -l < 04-SOURCES/DYN-SOURCES.csv | tr -d ' ')
    PROCESSED=$(grep -c ',processed,' 04-SOURCES/DYN-SOURCES.csv 2>/dev/null || echo 0)
    echo "+ $SOURCES rows ($PROCESSED processed)"
else
    echo "x Not found"
fi
echo "------------------------------------------"
echo ""

# Content verification
echo "-- Content Verification ------------------"
echo -n "| CANON files: "
CANON=$(ls 01-CANON/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "$CANON"

echo -n "| Processed sources: "
PROC_SOURCES=$(ls 04-SOURCES/processed/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "$PROC_SOURCES"

echo -n "| CANON with integrations: "
INTEGRATIONS=$(grep -l "SOURCE-" 01-CANON/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "$INTEGRATIONS"

echo -n "| Function XMLs: "
FUNCTIONS=$(ls 02-ENGINE/*.xml 2>/dev/null | wc -l | tr -d ' ' || echo "0")
echo "$FUNCTIONS"
echo "------------------------------------------"
echo ""

# Git status
echo "-- Git Status ----------------------------"
CHANGES=$(git status --short | wc -l | tr -d ' ')
if [ "$CHANGES" -eq 0 ]; then
    echo "| Working tree: + Clean"
else
    echo "| Working tree: ! $CHANGES uncommitted changes"
    git status --short | head -10 | sed 's/^/|   /'
fi

BRANCH=$(git branch --show-current)
echo "| Current branch: $BRANCH"
echo "------------------------------------------"
echo ""

# Summary
echo "========================================"
echo "Verification complete: $(date '+%Y-%m-%d %H:%M:%S')"
echo "========================================"
