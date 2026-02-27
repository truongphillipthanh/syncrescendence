# WATCHDOG ESCALATION: Service restart loop detected

**Time**: 2026-02-09 10:19:45
**Restarts in last hour**: 6

## Recent restart log
2026-02-09 10:09:44 kickstart corpus-health
2026-02-09 10:09:44 kickstart qmd-update
2026-02-09 10:14:45 kickstart corpus-health
2026-02-09 10:14:45 kickstart qmd-update
2026-02-09 10:19:45 kickstart corpus-health
2026-02-09 10:19:45 kickstart qmd-update

## Action Required
Check logs at /tmp/syncrescendence-*.log for root cause.
Services affected: Chroma (8765), Webhook (8888), watchers.
