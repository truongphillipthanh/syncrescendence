# WATCHDOG ESCALATION: Service restart loop detected

**Time**: 2026-02-12 16:03:02
**Restarts in last hour**: 4

## Recent restart log
2026-02-12 16:01:21 tmux-recreate constellation
2026-02-12 16:01:37 http-restart Chroma status=000
2026-02-12 16:02:51 kickstart chroma-server
2026-02-12 16:03:02 http-restart Chroma status=000

## Action Required
Check logs at /tmp/syncrescendence-*.log for root cause.
Services affected: Chroma (8765), Webhook (8888), watchers.
