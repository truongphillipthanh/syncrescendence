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

task_slug_from_path() {
  local task_file="$1"
  local task_base
  task_base=$(basename "$task_file")
  local slug
  slug=$(echo "$task_base" | sed -E 's/^TASK-[0-9]{8}-//; s/\.md$//')
  if [ -z "$slug" ] || [ "$slug" = "$task_base" ]; then
    slug=$(echo "$task_base" | sed -E 's/\.md$//')
  fi
  echo "$slug"
}

resolve_reply_target() {
  # Determine which agent should receive the completion reply.
  # Priority: Reply-To header > From header (agent extraction) > commander fallback
  local task_file="$1"

  # 1. Check Reply-To header (set by dispatch.sh v2+)
  local reply_to
  reply_to=$(parse_header_field "$task_file" "Reply-To")
  if [ -n "$reply_to" ] && [ "$reply_to" != "—" ] && [ "$reply_to" != "-" ] && [ "$reply_to" != "dispatch" ]; then
    if echo "commander adjudicator cartographer psyche ajna" | grep -qw "$reply_to"; then
      echo "$reply_to"
      return 0
    fi
  fi

  # 2. Extract agent slug from From header (e.g., "Commander (Claude Code Opus)" -> "commander")
  local from_raw
  from_raw=$(parse_header_field "$task_file" "From")
  if [ -n "$from_raw" ]; then
    local from_lower
    from_lower=$(echo "$from_raw" | tr '[:upper:]' '[:lower:]')
    for candidate in commander adjudicator cartographer psyche ajna; do
      if echo "$from_lower" | grep -q "$candidate"; then
        echo "$candidate"
        return 0
      fi
    done
  fi

  # 3. Fallback: commander (hub-spoke default)
  echo "commander"
}

pipe_reply_to_sender() {
  local finalized_task="$1"; local exit_code="$2"; local output_file="$3"; local result_path_abs="${4:-}"

  local reply_target
  reply_target=$(resolve_reply_target "$finalized_task")

  # Don't reply to self
  [ "$reply_target" = "$AGENT" ] && return 0

  local target_inbox="$REPO_ROOT/-INBOX/$reply_target/00-INBOX0"
  mkdir -p "$target_inbox" 2>/dev/null || true

  local date
  date=$(date '+%Y%m%d')
  local task_base
  task_base=$(basename "$finalized_task")
  local slug
  slug=$(task_slug_from_path "$finalized_task")
  local completed_at
  completed_at=$(date -u '+%Y-%m-%dT%H:%M:%SZ')

  local status
  if [ "$exit_code" -eq 0 ]; then
    status="COMPLETE"
  elif [ "$exit_code" -eq 124 ]; then
    status="BLOCKED"
  else
    status="FAILED"
  fi

  # Copy execution log to sender's inbox
  local exec_log="$target_inbox/EXECLOG-${AGENT}-${date}-${slug}.log"
  cp -f "$output_file" "$exec_log" 2>/dev/null || true

  # Copy RESULT receipt to sender's inbox
  if [ -n "$result_path_abs" ] && [ -f "$result_path_abs" ]; then
    cp -f "$result_path_abs" "$target_inbox/$(basename "$result_path_abs")" 2>/dev/null || true
  fi

  # Write structured CONFIRM file to sender's inbox
  local confirm_file="$target_inbox/CONFIRM-${AGENT}-${date}-${slug}.md"
  {
    echo "# CONFIRM-${AGENT}-${date}-${slug}"
    echo
    echo "**Kind**: CONFIRM"
    echo "**Task**: $task_base"
    echo "**From-Agent**: $AGENT"
    echo "**To-Agent**: $reply_target"
    echo "**Status**: $status"
    echo "**Exit-Code**: $exit_code"
    echo "**Completed-At**: $completed_at"
    echo "**Finalized-Task-Path**: \`$finalized_task\`"
    if [ -n "$result_path_abs" ]; then
      echo "**Result-Path**: \`$result_path_abs\`"
    fi
    echo "**Execution-Log**: \`$exec_log\`"
    echo
    echo "---"
    echo
    echo "## Execution Log Tail"
    echo
    echo '```text'
    tail -n 120 "$output_file" 2>/dev/null || true
    echo '```'
    echo
  } > "$confirm_file"

  log "$(date '+%H:%M:%S') Reply piped to $reply_target: CONFIRM-${AGENT}-${date}-${slug}.md"

  # Best-effort remote pipe (if reply target is on another machine)
  if ssh -o BatchMode=yes -o ConnectTimeout=3 "$reply_target" "test -d ~/Desktop/syncrescendence/-INBOX/$reply_target" 2>/dev/null; then
    scp -q -o BatchMode=yes -o ConnectTimeout=5 "$confirm_file" \
      "$reply_target:~/Desktop/syncrescendence/-INBOX/$reply_target/00-INBOX0/" 2>/dev/null || true
    if [ -n "$result_path_abs" ] && [ -f "$result_path_abs" ]; then
      scp -q -o BatchMode=yes -o ConnectTimeout=5 "$result_path_abs" \
        "$reply_target:~/Desktop/syncrescendence/-INBOX/$reply_target/00-INBOX0/" 2>/dev/null || true
    fi
  fi
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
      cmd_json=$(printf '%s' "$task_content" | python3 -c 'import json,sys; print(json.dumps(["gemini","-p",sys.stdin.read()]))')
      ;;
    psyche|ajna)
      # align internal openclaw timeout with wall clock (best-effort)
      local inner
      inner=$timeout_s
      if [ "$inner" -gt 600 ]; then inner=600; fi
      if [ "$AGENT" = "psyche" ]; then
        cmd_json=$(printf '%s' "$task_content" | python3 -c 'import json,sys; t=sys.argv[1]; print(json.dumps(["openclaw","agent","--agent","main","--message",sys.stdin.read(),"--thinking","high","--timeout",t]))' "$inner")
      else
        cmd_json=$(printf '%s' "$task_content" | python3 -c 'import json,sys; t=sys.argv[1]; print(json.dumps(["openclaw","agent","--agent","main","--message",sys.stdin.read(),"--timeout",t]))' "$inner")
      fi
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

escalate_on_timeout() {
  local task_file="$1"; local exit_code="$2"; local output_file="$3"
  [ "$exit_code" -ne 124 ] && return 0

  local escalation_contact
  escalation_contact=$(parse_header_field "$task_file" "Escalation-Contact")
  [ -z "$escalation_contact" ] && return 0
  [ "$escalation_contact" = "—" ] || [ "$escalation_contact" = "-" ] && return 0
  [ "$escalation_contact" = "$AGENT" ] && return 0

  # Verify escalation contact is a known agent
  if ! echo "commander adjudicator cartographer psyche ajna" | grep -qw "$escalation_contact"; then
    return 0
  fi

  local task_base
  task_base=$(basename "$task_file")
  local date
  date=$(date '+%Y%m%d')
  local slug
  slug=$(task_slug_from_path "$task_file")
  local now
  now=$(date -u '+%Y-%m-%dT%H:%M:%SZ')

  local esc_inbox="$REPO_ROOT/-INBOX/$escalation_contact/00-INBOX0"
  mkdir -p "$esc_inbox" 2>/dev/null || true

  local esc_file="$esc_inbox/ESCALATION-${AGENT}-${date}-${slug}.md"
  {
    echo "# ESCALATION-${AGENT}-${date}-${slug}"
    echo
    echo "**Kind**: ESCALATION"
    echo "**From-Agent**: $AGENT"
    echo "**To-Agent**: $escalation_contact"
    echo "**Original-Task**: $task_base"
    echo "**Failure-Mode**: TIMEOUT (exit code 124)"
    echo "**Escalated-At**: $now"
    echo "**Status**: PENDING"
    echo
    echo "---"
    echo
    echo "## Context"
    echo
    echo "Task \`$task_base\` assigned to **$AGENT** timed out after exceeding its wall-clock limit."
    echo "The task has been moved to 30-BLOCKED. Manual intervention or re-dispatch may be required."
    echo
    echo "## Execution Log Tail"
    echo
    echo '```text'
    tail -n 60 "$output_file" 2>/dev/null || true
    echo '```'
    echo
  } > "$esc_file"

  log "$(date '+%H:%M:%S') ESCALATION sent to $escalation_contact: ESCALATION-${AGENT}-${date}-${slug}.md"

  if [ -x "$SCRIPTS_DIR/append_ledger.sh" ]; then
    bash "$SCRIPTS_DIR/append_ledger.sh" ESCALATION "$AGENT" "$escalation_contact" "$task_base" >/dev/null 2>&1 || true
  fi
}

handle_file() {
  local file="$1"
  local base
  base=$(basename "$file")

  # Ignore receipts, results, confirmations, exec logs, and non-md
  [[ "$base" == RECEIPT-* ]] && return 0
  [[ "$base" == RESULT-* ]] && return 0
  [[ "$base" == CONFIRM-* ]] && return 0
  [[ "$base" == EXECLOG-* ]] && return 0
  [[ "$base" == ESCALATION-* ]] && return 0
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

  # Output validation: CLIs sometimes exit 0 despite API failures.
  # Detect known error patterns and override exit code to FAILED.
  if [ $exit_code -eq 0 ] && [ -f "$out_file" ]; then
    if grep -qE '(model .* does not exist|RESOURCE_EXHAUSTED|MODEL_CAPACITY_EXHAUSTED|stream disconnected before completion|EXEC_ERROR)' "$out_file" 2>/dev/null; then
      # Check for substantive output beyond just error traces
      local substantive_lines
      substantive_lines=$(grep -cvE '(^$|^\[|^Reconnecting|^ERROR:|^Attempt|^Loading|^Server|^Hook|^mcp startup|at async|at Gaxios|at process|at retryWithBackoff|config:|response:|headers:|data:|error:|status:|url:|method:|params:|body:|signal:|cause:|Symbol|An unexpected)' "$out_file" 2>/dev/null || echo "0")
      if [ "$substantive_lines" -lt 5 ]; then
        log "$(date '+%H:%M:%S') Output validation: CLI exited 0 but output contains only errors. Overriding to FAILED."
        exit_code=1
      fi
    fi
  fi

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

  # Mandatory bidirectional feedback: pipe CONFIRM + RESULT + EXECLOG to the dispatching agent.
  # Uses Reply-To header (dispatch.sh v2+), falls back to From header, then to commander.
  pipe_reply_to_sender "$final_path" "$exit_code" "$out_file" "$result_abs"

  # Pipe receipts to CC
  if [ -n "$cc_list" ] && [ "$cc_list" != "—" ]; then
    pipe_to_cc "$final_path" "$cc_list" "$result_abs"
  fi

  if [ -x "$SCRIPTS_DIR/append_ledger.sh" ]; then
    if [ $exit_code -eq 0 ]; then
      bash "$SCRIPTS_DIR/append_ledger.sh" COMPLETE "$AGENT" "—" "$base" >/dev/null 2>&1 || true
    elif [ $exit_code -eq 124 ]; then
      bash "$SCRIPTS_DIR/append_ledger.sh" BLOCKED "$AGENT" "—" "$base" >/dev/null 2>&1 || true
      # Escalation: notify contact if timeout exceeded escalation delay
      escalate_on_timeout "$final_path" "$exit_code" "$out_file"
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
