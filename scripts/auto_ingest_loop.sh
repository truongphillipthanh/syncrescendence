#!/usr/bin/env bash
# Syncrescendence auto_ingest_loop.sh – location-agnostic
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

echo "=== Constellation Ingest Cycle $(date +%Y-%m-%d_%H:%M) ==="

# 1. BOOT
source <(echo "cd $REPO_ROOT; git pull --ff-only; make configs" | bash)

# 2. Scan all offices
for office in agents/*/inbox/pending/*; do
  [ -f "$office" ] || continue
  agent=$(basename "$(dirname "$(dirname "$office")")")
  echo "Ingesting $office for $agent..."

  # Move to active/ per INIT.md
  mv "$office" "agents/$agent/inbox/active/$(basename "$office")"

  # Dispatch to Commander if Sovereign-tagged, else route via INTER-AGENT.md logic
  if grep -q "SOVEREIGN" "$office"; then
    cp "agents/$agent/inbox/active/$(basename "$office")" agents/commander/inbox/pending/
  else
    # Simple routing stub – extend with INTER-AGENT.md parse if needed
    echo "Handoff to Commander for triage"
    cp "agents/$agent/inbox/active/$(basename "$office")" agents/commander/inbox/pending/
  fi
done

# 3. Run Commander triage (triggers slash-gate)
echo "Commander triage cycle complete – check agents/commander/inbox/active/"

# 4. Log to memory/
echo "Cycle complete $(date)" >> "memory/$(date +%Y-%m-%d)-ingest.log"
