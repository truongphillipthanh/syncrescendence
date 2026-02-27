# WATCHDOG ESCALATION: Service restart loop detected

**Time**: 2026-02-09 11:25:45
**Restarts in last hour**: 24

## Recent restart log
2026-02-09 11:04:50 kickstart corpus-health
2026-02-09 11:04:50 kickstart qmd-update
2026-02-09 11:09:52 kickstart corpus-health
2026-02-09 11:09:52 kickstart qmd-update
2026-02-09 11:15:14 kickstart corpus-health
2026-02-09 11:15:14 kickstart qmd-update
2026-02-09 11:20:30 kickstart corpus-health
2026-02-09 11:20:30 kickstart qmd-update
2026-02-09 11:25:45 kickstart corpus-health
2026-02-09 11:25:45 kickstart qmd-update

## Action Required
Check logs at /tmp/syncrescendence-*.log for root cause.
Services affected: Chroma (8765), Webhook (8888), watchers.
