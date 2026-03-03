# ALERT-ecosystem-health-202602170810

**Kind**: ALERT
**From-Agent**: adjudicator
**To-Agent**: commander
**Timestamp**: 2026-02-17 08:10 PST
**Subject**: Ecosystem health check FAILURES detected

## Failures
- Chroma container missing (docker ps shows no chroma; localhost:8765 -> 404)
- launchd errors: com.syncrescendence.chroma-server (-15), emacs-server (1), qmd-update (1)
- gemini-mcp-tool missing (CLI + MCP dependency)

## Report
See: `-OUTBOX/adjudicator/RESULTS/RESULT-adjudicator-20260217-ecosystem_health.md`
