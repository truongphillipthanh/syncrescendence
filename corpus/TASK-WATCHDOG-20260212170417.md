# WATCHDOG ESCALATION: Service restart loop detected

**Time**: 2026-02-12 17:04:17
**Restarts in last hour**: 29

## Recent restart log
2026-02-12 16:17:59 kickstart chroma-server
2026-02-12 16:18:09 http-restart Chroma status=000
2026-02-12 16:19:21 kickstart chroma-server
2026-02-12 16:19:31 http-restart Chroma status=000
2026-02-12 16:20:45 kickstart chroma-server
2026-02-12 16:20:55 http-restart Chroma status=000
2026-02-12 16:22:09 kickstart chroma-server
2026-02-12 16:22:19 http-restart Chroma status=000
2026-02-12 16:23:32 kickstart chroma-server
2026-02-12 16:23:43 http-restart Chroma status=000

## Action Required
Check logs at /tmp/syncrescendence-*.log for root cause.
Services affected: Chroma (8765), Webhook (8888), watchers.
