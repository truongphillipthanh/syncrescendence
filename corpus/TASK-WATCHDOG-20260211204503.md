# WATCHDOG ESCALATION: Service restart loop detected

**Time**: 2026-02-11 20:45:03
**Restarts in last hour**: 11

## Recent restart log
2026-02-11 20:44:58 bootstrap chroma-server
2026-02-11 20:44:58 kickstart chroma-server
2026-02-11 20:44:58 bootstrap webhook-receiver
2026-02-11 20:44:58 kickstart webhook-receiver
2026-02-11 20:44:58 bootstrap watch-psyche
2026-02-11 20:44:58 kickstart watch-psyche
2026-02-11 20:44:58 bootstrap watch-adjudicator
2026-02-11 20:44:58 kickstart watch-adjudicator
2026-02-11 20:45:03 http-restart Chroma status=000
2026-02-11 20:45:03 http-restart Webhook status=000

## Action Required
Check logs at /tmp/syncrescendence-*.log for root cause.
Services affected: Chroma (8765), Webhook (8888), watchers.
