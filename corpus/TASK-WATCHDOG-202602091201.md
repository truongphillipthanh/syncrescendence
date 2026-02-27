# WATCHDOG ESCALATION: Service restart loop detected

**Time**: 2026-02-09 12:01:55
**Restarts in last hour**: 24

## Recent restart log
2026-02-09 11:40:46 kickstart corpus-health
2026-02-09 11:40:46 kickstart qmd-update
2026-02-09 11:45:47 kickstart corpus-health
2026-02-09 11:45:47 kickstart qmd-update
2026-02-09 11:51:12 kickstart corpus-health
2026-02-09 11:51:12 kickstart qmd-update
2026-02-09 11:56:39 kickstart corpus-health
2026-02-09 11:56:39 kickstart qmd-update
2026-02-09 12:01:55 kickstart corpus-health
2026-02-09 12:01:55 kickstart qmd-update

## Action Required
Check logs at /tmp/syncrescendence-*.log for root cause.
Services affected: Chroma (8765), Webhook (8888), watchers.
