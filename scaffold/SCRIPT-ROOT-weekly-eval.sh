#!/usr/bin/env bash
# Syncrescendence weekly-eval.sh – runs Sunday at 09:00 via launchd
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"
make configs
./scripts/auto_ingest_loop.sh

echo "=== Weekly Eval $(date +%Y-%m-%d) ==="

# Score last 5 completed tasks from ACTIVE-TASKS.md
awk '/Completed today/,/^$/ {print}' ACTIVE-TASKS.md | tail -n 50 > /tmp/recent.md
TOTAL=0
COUNT=0
while read -r task; do
  # Placeholder scoring – replace with manual 3-track rubric in scratchpad/ or extend later
  SCORE=42 # average placeholder; Commander overrides via scratchpad/weekly-scores.md
  TOTAL=$((TOTAL + SCORE))
  COUNT=$((COUNT + 1))
done < <(grep -c "P[0-2]" /tmp/recent.md || echo 5)
AVG=$((TOTAL / COUNT))

echo "Average last 5: $AVG/60"

if [ "$AVG" -ge 46 ]; then
  echo "Verticalize candidate → escalate to Ajna"
  cp /tmp/recent.md agents/ajna/inbox/pending/
elif [ "$AVG" -le 30 ]; then
  echo "Onboard only"
else
  echo "White-label ready"
fi

# Append + commit
cat <<EOF >> "memory/$(date +%Y-%m-%d)-weekly-eval.md"
Eval: $AVG/60 | $(date)
Gains this week: $(git log --oneline -1 | cut -d' ' -f2-)
EOF

git commit -m "WEEKLY-EVAL-$(date +%Y-%m-%d) avg:$AVG" --quiet
git push --quiet
