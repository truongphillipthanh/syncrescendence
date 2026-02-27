# WATCHDOG ESCALATION: Service restart loop detected

**Time**: 2026-02-11 21:31:16
**Restarts in last hour**: 21

## Recent restart log
2026-02-11 20:46:16 kickstart chroma-server
2026-02-11 20:46:16 bootstrap webhook-receiver
2026-02-11 20:46:16 kickstart webhook-receiver
2026-02-11 20:46:16 bootstrap watch-psyche
2026-02-11 20:46:16 kickstart watch-psyche
2026-02-11 20:46:16 bootstrap watch-adjudicator
2026-02-11 20:46:16 kickstart watch-adjudicator
2026-02-11 20:46:20 http-restart Chroma status=000
2026-02-11 20:46:20 http-restart Webhook status=000
2026-02-11 20:47:26 bootstrap watch-cartographer

## Action Required
Check logs at /tmp/syncrescendence-*.log for root cause.
Services affected: Chroma (8765), Webhook (8888), watchers.
