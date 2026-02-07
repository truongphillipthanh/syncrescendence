#!/bin/bash
# watch_dispatch.sh — Watch for dispatch files in an agent's Inbox0 folder (filesystem-kanban)
# Usage: bash watch_dispatch.sh [AGENT_NAME]
# Requires: fswatch (brew install fswatch) or uses polling fallback
#
# Filesystem Kanban:
#   - Watches:  -INBOX/<agent>/00-INBOX0/
#   - Claims:   atomic mv -> 10-IN_PROGRESS/
#   - Completes: mv -> 40-DONE/ or 50_FAILED/
#
# Guards:
#   - Ignore RECEIPT-* files
#   - Only execute files addressed to this agent (**To** guard)
#   - Never execute completed tasks (Completed-At/Exit-Code guard)
#
# Receipts:
#   - Deterministically write RESULT to the path in **Receipts-To** (default -OUTBOX/<agent>/RESULTS)
#   - Best-effort CC piping: copy finalized TASK into -INBOX/<cc>/RECEIPTS and (if ssh alias exists) scp it.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [ -z "$REPO_ROOT" ]; then
  REPO_ROOT="$HOME/Desktop/syncrescendence"
fi

AGENT="${1:-psyche}"
HOSTNAME_SHORT=$(hostname -s 2>/dev/null || echo "local")
SCRIPTS_DIR="$REPO_ROOT/00-ORCHESTRATION/scripts"

INBOX_ROOT="$REPO_ROOT/-INBOX/$AGENT"
INBOX0_DIR="$INBOX_ROOT/00-INBOX0"
INPROG_DIR="$INBOX_ROOT/10-IN_PROGRESS"
DONE_DIR="$INBOX_ROOT/40-DONE"
FAILED_DIR="$INBOX_ROOT/50_FAILED"
BLOCKED_DIR="$INBOX_ROOT/30-BLOCKED"
RECEIPTS_DIR="$INBOX_ROOT/RECEIPTS"

mkdir -p "$INBOX0_DIR" "$INPROG_DIR" "$BLOCKED_DIR" "$DONE_DIR" "$FAILED_DIR" "$RECEIPTS_DIR"

WATCH_DIR="$INBOX0_DIR"
POLL_INTERVAL=10

log() { echo "[Watch] $*"; }

log "Watching -INBOX/$AGENT/00-INBOX0/ for dispatch files"
log "Directory: $WATCH_DIR"
log "Poll interval: ${POLL_INTERVAL}s"
log "Claim tag: ${AGENT}-${HOSTNAME_SHORT}"
log "Press Ctrl+C to stop"
log ""

parse_header_field() {
  local file="$1"; local field="$2"
  python3 - "$file" "$field" <<'PY'
import re, sys
path, field = sys.argv[1], sys.argv[2]
text=open(path,'r',encoding='utf-8').read()
m=re.search(r'^\*\*'+re.escape(field)+r'\*\*:\s*(.+)\s*$', text, flags=re.M)
print(m.group(1).strip() if m else '')
PY
}

header_to_matches_agent() {
  local file="$1"
  python3 - "$file" "$AGENT" <<'PY'
import re, sys
path, agent = sys.argv[1], sys.argv[2]
text=open(path,'r',encoding='utf-8').read()
m=re.search(r'^\*\*To\*\*:\s*(.+)$', text, flags=re.M)
if not m:
    sys.exit(1)
to=m.group(1).strip().lower()
a=agent.strip().lower()
if re.search(r'\b'+re.escape(a)+r'\b', to):
    sys.exit(0)
sys.exit(1)
PY
}

header_is_already_completed() {
  local file="$1"
  python3 - "$file" <<'PY'
import re, sys
text=open(sys.argv[1],'r',encoding='utf-8').read()
ca=re.search(r'^\*\*Completed-At\*\*:\s*(.+)$', text, flags=re.M)
ec=re.search(r'^\*\*Exit-Code\*\*:\s*(.+)$', text, flags=re.M)
completed=(ca and ca.group(1).strip() not in ('—','-',''))
exitc=(ec and ec.group(1).strip() not in ('—','-',''))
# treat either as completed
sys.exit(0 if (completed or exitc) else 1)
PY
}

set_fields() {
  local file="$1"; shift
  python3 - "$file" "$@" <<'PY'
import sys
path=sys.argv[1]
# args pairs: field value
pairs=sys.argv[2:]
lines=open(path,'r',encoding='utf-8').read().splitlines(True)

def set_field(name,value):
    key=f"**{name}**:"
    for i,line in enumerate(lines):
        if line.startswith(key):
            lines[i]=f"{key} {value}\n"; return
    # insert near top after Priority/Fingerprint/Issued
    insert_after=None
    for marker in ("**Priority**:","**Fingerprint**:","**Issued**:"):
        for i,line in enumerate(lines):
            if line.startswith(marker):
                insert_after=i; break
        if insert_after is not None:
            break
    if insert_after is None:
        insert_after=0
    lines.insert(insert_after+1, f"{key} {value}\n")

for i in range(0,len(pairs),2):
    set_field(pairs[i], pairs[i+1])

open(path,'w',encoding='utf-8').write(''.join(lines))
PY
}

write_result_receipt() {
  local task_file="$1"; local exit_code="$2"; local output_file="$3"

  local receipts_to
  receipts_to=$(parse_header_field "$task_file" "Receipts-To")
  if [ -z "$receipts_to" ]; then
    receipts_to="-OUTBOX/${AGENT}/RESULTS"
  fi

  mkdir -p "$REPO_ROOT/$receipts_to" 2>/dev/null || true

  local task_base
  task_base=$(basename "$task_file")
  local date
  date=$(date '+%Y%m%d')
  local slug
  slug=$(echo "$task_base" | sed -E 's/^TASK-[0-9]{8}-//; s/\.md$//')
  if [ -z "$slug" ] || [ "$slug" = "$task_base" ]; then
    slug=$(echo "$task_base" | sed -E 's/\.md$//')
  fi

  local result_path="$REPO_ROOT/$receipts_to/RESULT-${AGENT}-${date}-${slug}.md"

  {
    echo "# RESULT-${AGENT}-${date}-${slug}"
    echo
    echo "**Task**: $task_base"
    echo "**Agent**: $AGENT"
    echo "**Exit-Code**: $exit_code"
    echo "**Completed-At**: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
    echo
    echo "---"
    echo
    echo "## Output"
    echo
    cat "$output_file"
    echo
  } > "$result_path"

  echo "$result_path"
}

pipe_to_cc() {
  local finalized_task="$1"; local cc_list="$2"; local result_path_abs="${3:-}"
  [ -z "$cc_list" ] && return 0

  IFS=',' read -r -a ccs <<< "$cc_list"
  for cc in "${ccs[@]}"; do
    cc=$(echo "$cc" | xargs)
    [ -z "$cc" ] && continue

    mkdir -p "$REPO_ROOT/-INBOX/$cc/RECEIPTS" 2>/dev/null || true
    cp -f "$finalized_task" "$REPO_ROOT/-INBOX/$cc/RECEIPTS/RECEIPT-${AGENT}-$(basename "$finalized_task")" 2>/dev/null || true

    # best-effort remote pipe: ssh alias == cc
    if ssh -o BatchMode=yes -o ConnectTimeout=3 "$cc" "test -d ~/Desktop/syncrescendence/-INBOX/$cc" 2>/dev/null; then
      scp -q -o BatchMode=yes -o ConnectTimeout=5 "$finalized_task" \
        "$cc:~/Desktop/syncrescendence/-INBOX/$cc/RECEIPTS/RECEIPT-${AGENT}-$(basename "$finalized_task")" \
        2>/dev/null || true

      if [ -n "$result_path_abs" ] && [ -f "$result_path_abs" ]; then
        scp -q -o BatchMode=yes -o ConnectTimeout=5 "$result_path_abs" \
          "$cc:~/Desktop/syncrescendence/-INBOX/$cc/$(basename "$result_path_abs")" \
          2>/dev/null || true
      fi
    fi
  done
}

EXEC_EXIT=0

parse_timeout_seconds() {
  local file="$1"
  local t
  t=$(parse_header_field "$file" "Timeout" || true)

  # Default: 600s (10m)
  if [ -z "$t" ] || [ "$t" = "—" ] || [ "$t" = "-" ]; then
    echo 600
    return 0
  fi

  # If it's an integer <= 240, interpret as minutes (legacy tasks use 30)
  if echo "$t" | rg -q '^[0-9]+$'; then
    if [ "$t" -le 240 ]; then
      echo $((t * 60))
      return 0
    fi
    echo "$t"
    return 0
  fi

  # Fallback
  echo 600
}

run_executor() {
  local task_file="$1"
  local tmp_out
  tmp_out=$(mktemp "/tmp/syncrescendence-${AGENT}-taskout.XXXXXX")

  local task_content
  task_content="$(cat "$task_file")"

  local timeout_s
  timeout_s=$(parse_timeout_seconds "$task_file")

  # Build command + run with a hard wall-clock timeout using python (portable on macOS)
  local cmd_json
  local stdin_mode="none"
  local stdin_text=""

  case "$AGENT" in
    commander)
      cmd_json=$(printf '%s' "$task_content" | python3 -c 'import json,sys; print(json.dumps(["claude","-p",sys.stdin.read()]))')
      ;;
    adjudicator)
      cmd_json=$(printf '%s' "$task_content" | python3 -c 'import json,sys; print(json.dumps(["codex","exec",sys.stdin.read()]))')
      ;;
    cartographer)
      cmd_json=$(python3 -c 'import json; print(json.dumps(["gemini","-p","You are responding to a task dispatch. Do NOT use any tools. Simply read the objective and respond with text only."]))')
      stdin_mode="text"
      stdin_text="$task_content"
      ;;
    psyche|ajna)
      # align internal openclaw timeout with wall clock (best-effort)
      local inner
      inner=$timeout_s
      if [ "$inner" -gt 600 ]; then inner=600; fi
      cmd_json=$(printf '%s' "$task_content" | python3 -c 'import json,sys; t=sys.argv[1]; print(json.dumps(["openclaw","agent","--agent","main","--message",sys.stdin.read(),"--timeout",t]))' "$inner")
      ;;
    *)
      echo "[Watch] No CLI handler configured for agent: $AGENT" >"$tmp_out" 2>&1
      EXEC_EXIT=127
      echo "$tmp_out"
      return 0
      ;;
  esac

  set +e
  python3 - "$cmd_json" "$timeout_s" "$stdin_mode" >"$tmp_out" 2>&1 <<'PY'
import json, subprocess, sys, time
try:
    cmd=json.loads(sys.argv[1])
except (json.JSONDecodeError, IndexError) as e:
    sys.stdout.write(f"[Watch] EXEC_ERROR: failed to parse command JSON: {e}\n")
    sys.exit(126)
timeout=float(sys.argv[2])
stdin_mode=sys.argv[3]
stdin_data=None
if stdin_mode == "text":
    stdin_data=sys.stdin.read()

start=time.time()
try:
    p = subprocess.run(cmd, input=stdin_data, text=True, capture_output=True, timeout=timeout)
    sys.stdout.write(p.stdout)
    if p.stderr:
        sys.stdout.write("\n" + p.stderr)
    sys.exit(p.returncode)
except subprocess.TimeoutExpired as e:
    elapsed=time.time()-start
    sys.stdout.write(f"[Watch] EXEC_TIMEOUT after {elapsed:.1f}s (limit {timeout:.0f}s)\n")
    sys.exit(124)
except FileNotFoundError:
    sys.stdout.write("[Watch] EXEC_ERROR: command not found\n")
    sys.exit(127)
PY
  EXEC_EXIT=$?
  set -e

  echo "$tmp_out"
}

handle_file() {
  local file="$1"
  local base
  base=$(basename "$file")

  # Ignore receipts and non-md
  [[ "$base" == RECEIPT-* ]] && return 0
  [[ "$base" != *.md ]] && return 0

  # Only TASK/SURVEY/PATCH etc are allowed, but we enforce by To/Completed guards
  if ! header_to_matches_agent "$file"; then
    log "$(date '+%H:%M:%S') Skipping not addressed to $AGENT: $base" >&2
    return 0
  fi

  if header_is_already_completed "$file"; then
    log "$(date '+%H:%M:%S') Skipping already completed task: $base" >&2
    return 0
  fi

  # Only claim if Status says PENDING (Inbox0 invariant)
  if ! grep -q "Status.*PENDING" "$file" 2>/dev/null; then
    return 0
  fi

  # Atomic claim by moving Inbox0 -> InProgress
  local claimed="$INPROG_DIR/$base"
  if ! mv "$file" "$claimed" 2>/dev/null; then
    return 0
  fi

  local now
  now=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
  local claim_tag="${AGENT}-${HOSTNAME_SHORT}"

  set_fields "$claimed" \
    Status IN_PROGRESS \
    Kanban IN_PROGRESS \
    Claimed-By "$claim_tag" \
    Claimed-At "$now"

  log "$(date '+%H:%M:%S') Claimed: $base" >&2
  if [ -x "$SCRIPTS_DIR/append_ledger.sh" ]; then
    bash "$SCRIPTS_DIR/append_ledger.sh" CLAIM "$AGENT" "$AGENT" "$base" >/dev/null 2>&1 || true
  fi

  log "$(date '+%H:%M:%S') Processing: $base"

  local cc_list
  cc_list=$(parse_header_field "$claimed" "CC")

  local out_file
  out_file=$(run_executor "$claimed")
  local exit_code=$EXEC_EXIT

  local done_now
  done_now=$(date -u '+%Y-%m-%dT%H:%M:%SZ')

  local status_val
  local kanban_val
  if [ $exit_code -eq 0 ]; then
    status_val=COMPLETE
    kanban_val=DONE
  elif [ $exit_code -eq 124 ]; then
    status_val=BLOCKED
    kanban_val=BLOCKED
  else
    status_val=FAILED
    kanban_val=FAILED
  fi

  set_fields "$claimed" \
    Status "$status_val" \
    Kanban "$kanban_val" \
    Completed-At "$done_now" \
    Exit-Code "$exit_code"

  local final_path
  if [ $exit_code -eq 0 ]; then
    final_path="$DONE_DIR/$base"
  elif [ $exit_code -eq 124 ]; then
    final_path="$BLOCKED_DIR/$base"
  else
    final_path="$FAILED_DIR/$base"
  fi
  mv "$claimed" "$final_path" 2>/dev/null || true

  # Write deterministic result receipt
  local result_abs
  result_abs=$(write_result_receipt "$final_path" "$exit_code" "$out_file")

  # Pipe receipts to CC
  if [ -n "$cc_list" ] && [ "$cc_list" != "—" ]; then
    pipe_to_cc "$final_path" "$cc_list" "$result_abs"
  fi

  if [ -x "$SCRIPTS_DIR/append_ledger.sh" ]; then
    if [ $exit_code -eq 0 ]; then
      bash "$SCRIPTS_DIR/append_ledger.sh" COMPLETE "$AGENT" "—" "$base" >/dev/null 2>&1 || true
    elif [ $exit_code -eq 124 ]; then
      bash "$SCRIPTS_DIR/append_ledger.sh" BLOCKED "$AGENT" "—" "$base" >/dev/null 2>&1 || true
    else
      bash "$SCRIPTS_DIR/append_ledger.sh" FAILED "$AGENT" "—" "$base" >/dev/null 2>&1 || true
    fi
  fi

  rm -f "$out_file" 2>/dev/null || true
}

if command -v fswatch &>/dev/null; then
  log "Using fswatch (event-driven, low overhead)"
  log ""
  fswatch -0 "$WATCH_DIR" | while IFS= read -r -d '' changed; do
    # fswatch returns the directory too; we only handle files
    [ -f "$changed" ] || continue
    handle_file "$changed"
  done
else
  log "fswatch not found. Using polling fallback (${POLL_INTERVAL}s interval)"
  log "Install fswatch for event-driven watching: brew install fswatch"
  log ""
  while true; do
    for f in "$WATCH_DIR"/*.md; do
      [ -f "$f" ] || continue
      handle_file "$f"
    done
    sleep "$POLL_INTERVAL"
  done
fi
