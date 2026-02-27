# SIEGE CC28 — Lane 5: Proprioceptive Config Harness

**Agent**: Adjudicator (Codex)
**Repo**: `/Users/system/syncrescendence` (main branch)
**Date**: 2026-02-24
**Reply-To**: commander
**CC**: commander

---

## OBJECTIVE

Build the proprioceptive config harness — Adjudicator Spec 3. Scripts should feel their own environment and fail loudly on mismatch, not silently use stale paths.

## SPEC (from Adjudicator CC28)

### Architecture
```
Every script start:
  source config.sh
  -> sync_config_preflight --context <script>
  -> assert dirs/files/env assumptions
  -> fail closed with explicit assumption + repair hint

Standalone:
  config_health.sh --json|--md --strict
  -> used by scaffold_validate.sh
  -> used by cockpit_startup.sh

Migration:
  config_migrate.sh --dry-run|--apply --verify
  -> rewrites scripts to config imports/sourcing
  -> runs scaffold_validate gate
```

### Task 1: Extend `config.sh` (~120 LOC additions)

File: `orchestration/00-ORCHESTRATION/scripts/config.sh`

Add these functions:
- `sync_assert_dir <path> <description>` — assert directory exists, die with repair hint if not
- `sync_assert_file <path> <description>` — assert file exists, die with repair hint if not
- `sync_assert_env <varname> <description>` — assert env var is set and non-empty
- `sync_config_preflight <script_name>` — run standard assertions for the calling script's context:
  - Assert SYNCRESCENDENCE_ROOT is set
  - Assert key directories exist (orchestration, canon, engine, sources, praxis, agents)
  - Assert key state files exist (DYN-DEFERRED_COMMITMENTS.md, ARCH-INTENTION_COMPASS.md)
  - Log preflight result to stderr

### Task 2: Extend `config.py` (~90 LOC additions)

File: `orchestration/00-ORCHESTRATION/scripts/config.py`

Add:
- `validate_config(strict: bool = False) -> list[str]` — returns list of violations
- `class ConfigError(Exception)` — raised on critical violations
- Required vs optional assertions split (strict mode checks optional too)
- Path existence checks for all paths defined in config

### Task 3: Create `config_health.sh` (~140 LOC)

File: `orchestration/00-ORCHESTRATION/scripts/config_health.sh`

Standalone health check:
```bash
bash orchestration/00-ORCHESTRATION/scripts/config_health.sh --strict --json
bash orchestration/00-ORCHESTRATION/scripts/config_health.sh --md
```

Checks:
- All required directories exist
- All required state files exist
- Key env vars are set (SYNCRESCENDENCE_ROOT, machine-specific vars)
- No hardcoded `/Users/system/syncrescendence` in active scripts (scan for them)
- config.sh is sourceable without errors
- Output: JSON or Markdown report with pass/fail per check

### Task 4: Integrate in `scaffold_validate.sh` (~50 LOC)

File: `orchestration/00-ORCHESTRATION/scripts/scaffold_validate.sh`

Add config health as first-class validation section:
- Source config_health.sh results
- Config failures appear as scaffold violations
- Exit code reflects config health

### Task 5: Extend `config_migrate.sh` (~120 LOC)

File: `orchestration/00-ORCHESTRATION/scripts/config_migrate.sh`

Add:
- `--verify` flag: after migration, run `bash -n` on all .sh files and `python3 -m py_compile` on all .py files
- Dynamic inventory: scan for hardcoded paths in all scripts under orchestration/scripts/ and agents/*/
- Report: list of files with hardcoded paths, proposed replacements

### Failure Modes
- False failures on optional components → required vs optional split
- Path drift across machines → configurable root via env override
- Migration rewrites breaking code → syntax validation post-migration
- Silent pass with stale fallbacks → remove hardcoded fallback roots

## CONSTRAINTS
- Only modify files listed above (config.sh, config.py, config_health.sh, scaffold_validate.sh, config_migrate.sh)
- ~520 LOC total additions
- Commit with prefix `feat: CC28-L5 proprioceptive config harness`
- Run `config_health.sh --strict --json` and verify it passes
- Run `scaffold_validate.sh` and verify config section appears
- Do NOT modify AGENTS.md, CLAUDE.md, or any files outside your lane
