#!/usr/bin/env bash
set -euo pipefail

echo "=== DEFRAG POST-APPLY VERIFICATION ==="
echo "Run at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"

fail=0
warn=0

check() {
  if eval "$1"; then
    echo "PASS: $2"
  else
    echo "FAIL: $2"
    fail=$((fail + 1))
  fi
}

warn_check() {
  if eval "$1"; then
    echo "PASS: $2"
  else
    echo "WARN: $2"
    warn=$((warn + 1))
  fi
}

check '[ $(ls *.md 2>/dev/null | rg -v "^CLAUDE.md$" | wc -l) -eq 0 ]' "No orphan .md at root"
check '[ $(ls -d */ 2>/dev/null | rg -v "^(0[0-6]|OUTGOING|outgoing|config|\.)" | wc -l) -eq 0 ]' "No orphan dirs at root"
check '[ $(find . -name ".DS_Store" | wc -l) -eq 0 ]' "No .DS_Store files"
check '[ $(ls DIRECTIVE*.md 2>/dev/null | wc -l) -eq 0 ]' "No directives at root"
check '[ $(ls ORACLE*.md 2>/dev/null | wc -l) -eq 0 ]' "No oracle contexts at root"

warn_check '[ $(ls 05-ARCHIVE/ARCH-*.md 2>/dev/null | wc -l) -ge 9 ]' "Archive files created"
warn_check '[ $(ls 00-ORCHESTRATION/directives/DIRECTIVE*.md 2>/dev/null | wc -l) -ge 10 ]' "Directives in place"

# Link integrity (simple pass)
if rg -n '\]\([^)]+\.md\)' -g '*.md' >/tmp/defrag_md_links.txt; then
  echo "Link scan complete: /tmp/defrag_md_links.txt"
else
  echo "Link scan: no markdown links found"
fi

if [[ $fail -gt 0 ]]; then
  echo "FAILURES: $fail"
  exit 1
fi

echo "WARNINGS: $warn"
echo "Verification complete"
