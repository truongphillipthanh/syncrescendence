# 06-ORCHESTRATION/state/

## Structure

| Directory | Purpose | Mutability |
|-----------|---------|------------|
| `dynamic/` | Real-time operational state | High (updates frequently) |
| `ledgers/` | CSV mechanical tracking | Medium (task/sprint updates) |
| `reference/` | Stable protocols and schemas | Low (deliberate updates only) |
| `archaeology/` | Historical decisions and characteristics | Frozen (append-only) |

## Oracle Contexts

Oracle context documents are in `06-ORCHESTRATION/oracle_contexts/` with directives and execution logs as peer directories. Oracle contexts are the strategic synthesis layer—the "why" above the "what" (directives) and "how" (execution logs).
