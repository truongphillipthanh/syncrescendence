# Drift Mapping: Legacy & Stale References
## Path Casing Drift
- **Issue**: References to `outgoing/` (lowercase) vs `-OUTGOING/` (uppercase/prefixed).
- **Count**: ~49 instances identified in previous survey; validation suggests these persist in `02-OPERATIONAL` scripts.

## Configuration Drift
- **Issue**: Stale `config/coordination` references.
- **Location**: Primarily in `CLAUDE.md` and legacy `00-ORCHESTRATION` drafts.
- **Count**: ~25 instances.

## Marker Drift
- **Issue**: Legacy `===AUDIZABLE===` markers.
- **Status**: Being replaced by fenced code blocks or specific metadata headers, but ~12 files still contain the legacy string.
