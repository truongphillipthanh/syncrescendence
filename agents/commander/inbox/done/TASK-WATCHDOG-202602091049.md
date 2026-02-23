---
Status: PENDING
Priority: P0
Reply-To: watchdog
CC: commander
---
# WATCHDOG ESCALATION: Service restart loop detected

**Time**: 2026-02-09 10:49:49
**Restarts in last hour**: 18

## Recent restart log
2026-02-09 10:29:46 kickstart corpus-health
2026-02-09 10:29:46 kickstart qmd-update
2026-02-09 10:34:47 kickstart corpus-health
2026-02-09 10:34:47 kickstart qmd-update
2026-02-09 10:39:48 kickstart corpus-health
2026-02-09 10:39:48 kickstart qmd-update
2026-02-09 10:44:48 kickstart corpus-health
2026-02-09 10:44:48 kickstart qmd-update
2026-02-09 10:49:49 kickstart corpus-health
2026-02-09 10:49:49 kickstart qmd-update

## Action Required
Check logs at /tmp/syncrescendence-*.log for root cause.
Services affected: Chroma (8765), Webhook (8888), watchers.
