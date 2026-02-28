# WATCHDOG ESCALATION: Service restart loop detected

**Time**: 2026-02-09 12:21:57
**Restarts in last hour**: 24

## Recent restart log
2026-02-09 12:01:55 kickstart corpus-health
2026-02-09 12:01:55 kickstart qmd-update
2026-02-09 12:06:55 kickstart corpus-health
2026-02-09 12:06:55 kickstart qmd-update
2026-02-09 12:11:56 kickstart corpus-health
2026-02-09 12:11:56 kickstart qmd-update
2026-02-09 12:16:56 kickstart corpus-health
2026-02-09 12:16:56 kickstart qmd-update
2026-02-09 12:21:57 kickstart corpus-health
2026-02-09 12:21:57 kickstart qmd-update

## Action Required
Check logs at /tmp/syncrescendence-*.log for root cause.
Services affected: Chroma (8765), Webhook (8888), watchers.
