#!/usr/bin/env bash
# verify_orchestration_hardening.sh
# Blocking verification for hardened orchestration control-plane.

set -u

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then
    echo "ERROR: must run inside repository" >&2
    exit 1
fi

INTEGRITY_GATE="${REPO_ROOT}/00-ORCHESTRATION/scripts/repo_integrity_gate.sh"
AUTO_INGEST="${REPO_ROOT}/00-ORCHESTRATION/scripts/auto_ingest_loop.sh"
ORCHESTRATOR="${REPO_ROOT}/00-ORCHESTRATION/scripts/proactive_orchestrator.sh"
WATCHDOG="${REPO_ROOT}/00-ORCHESTRATION/scripts/constellation_watchdog.sh"
SUPERVISOR="${REPO_ROOT}/00-ORCHESTRATION/scripts/auto_ingest_supervisor.sh"
DISPATCH="${REPO_ROOT}/00-ORCHESTRATION/scripts/dispatch.sh"
BREAKER_FILE="${REPO_ROOT}/00-ORCHESTRATION/state/breakers/orchestration.breaker"

failures=0

pass() {
    echo "[PASS] $*"
}

fail() {
    echo "[FAIL] $*" >&2
    failures=$((failures + 1))
}

check_exists_and_exec() {
    local file="$1"
    if [ ! -f "$file" ]; then
        fail "missing file: ${file#$REPO_ROOT/}"
        return
    fi
    if [ ! -x "$file" ]; then
        fail "not executable: ${file#$REPO_ROOT/}"
        return
    fi
    pass "executable present: ${file#$REPO_ROOT/}"
}

echo "=== Orchestration Hardening Verification ==="

check_exists_and_exec "$INTEGRITY_GATE"
check_exists_and_exec "$AUTO_INGEST"
check_exists_and_exec "$ORCHESTRATOR"
check_exists_and_exec "$WATCHDOG"
check_exists_and_exec "$SUPERVISOR"
check_exists_and_exec "$DISPATCH"

if "$INTEGRITY_GATE" --repo "$REPO_ROOT" --context verify_hardening --strict --quiet; then
    pass "strict integrity gate"
else
    fail "strict integrity gate"
fi

for script in "$AUTO_INGEST" "$ORCHESTRATOR" "$WATCHDOG" "$SUPERVISOR" "$DISPATCH"; do
    if bash -n "$script"; then
        pass "bash syntax: ${script#$REPO_ROOT/}"
    else
        fail "bash syntax: ${script#$REPO_ROOT/}"
    fi
done

if rg -n 'for t in \$tasks' "$ORCHESTRATOR" >/dev/null 2>&1; then
    fail "unsafe filename iteration pattern still present in orchestrator"
else
    pass "safe queued-task iteration in orchestrator"
fi

if [ -f "$BREAKER_FILE" ]; then
    state=$(grep '^state=' "$BREAKER_FILE" 2>/dev/null | head -1 | cut -d'=' -f2)
    case "$state" in
        OPEN|HALF_OPEN|CLOSED)
            pass "breaker state recognized: $state"
            ;;
        *)
            fail "breaker state invalid: ${state:-<empty>}"
            ;;
    esac
else
    pass "breaker file not yet created (expected before first cycle)"
fi

if [ "$failures" -gt 0 ]; then
    echo "=== Verification FAILED (${failures} checks) ===" >&2
    exit 1
fi

echo "=== Verification PASSED ==="
exit 0
