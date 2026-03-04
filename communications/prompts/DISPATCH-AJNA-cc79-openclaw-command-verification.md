# DISPATCH-AJNA-cc79-openclaw-command-verification

**Surface**: `ajna_openclaw_runtime`  
**Packet type**: `verification_dispatch`  
**Purpose**: verify OpenClaw commands that timed out in local CC79 command probes

## Commands To Verify

1. `openclaw test-skill --help`
2. `openclaw skills purge --untrusted --help`
3. `openclaw telemetry export --prom --help`
4. `openclaw doctor --restore --help`

## Return Format

For each command:

- command
- exit_code
- first_20_lines_output
- verdict: `exists_and_behaves` / `exists_but_changed` / `missing`

## Output Artifact

Write result as:

- `/Users/system/syncrescendence/communications/responses/RESPONSE-AJNA-cc79-openclaw-command-verification.md`
