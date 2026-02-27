---
Status: PENDING
Priority: P0
Reply-To: watchdog
CC: commander
---
# WATCHDOG ESCALATION: Service restart loop detected

**Time**: 2026-02-12 16:18:09
**Restarts in last hour**: 26

## Recent restart log
2026-02-12 16:12:28 kickstart chroma-server
2026-02-12 16:12:38 http-restart Chroma status=000
2026-02-12 16:13:51 kickstart chroma-server
2026-02-12 16:14:01 http-restart Chroma status=000
2026-02-12 16:15:14 kickstart chroma-server
2026-02-12 16:15:24 http-restart Chroma status=000
2026-02-12 16:16:36 kickstart chroma-server
2026-02-12 16:16:46 http-restart Chroma status=000
2026-02-12 16:17:59 kickstart chroma-server
2026-02-12 16:18:09 http-restart Chroma status=000

## Action Required
Check logs at /tmp/syncrescendence-*.log for root cause.
Services affected: Chroma (8765), Webhook (8888), watchers.
