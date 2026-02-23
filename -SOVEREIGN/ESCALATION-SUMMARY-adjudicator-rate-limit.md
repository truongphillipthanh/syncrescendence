# ESCALATION SUMMARY: Adjudicator Rate-Limit Failures

**Consolidated**: 2026-02-22 by Commander
**Root Cause**: Codex model quota exhausted — all deferred_dc_* followup tasks hit RATE_LIMIT after 3 retries
**Affected Tasks**: deferred_dc_002, dc_003, dc_004, dc_013 (followups)
**Date Range**: 2026-02-20 through 2026-02-22
**Original Escalation Count**: 9 (collapsed into this summary)

## Additional Adjudicator Failures

| Task | Failure | Date |
|---|---|---|
| watchdog_recovery | EXEC_TIMEOUT (1800s) | 2026-02-17 |
| scp_sling_verify | EXEC_TIMEOUT (1800s) | 2026-02-19 |

## Psyche Failure

| Task | Failure | Date |
|---|---|---|
| infrastructure_audit | STALE_TIMEOUT | 2026-02-21 |

## Resolution

Adjudicator (Codex CLI) needs either:
1. Model quota reset / upgrade
2. Model swap to a non-rate-limited alternative
3. Tasks reassigned to Commander or another agent

**Status**: OPEN — deferred to Sovereign decision queue
