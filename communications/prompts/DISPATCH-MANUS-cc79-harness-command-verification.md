# DISPATCH-MANUS-cc79-harness-command-verification

**Surface**: `manus_api_or_runtime`  
**Packet type**: `verification_dispatch`  
**Purpose**: verify non-local harness command claims from CC79

## Commands To Verify

### Aider

1. `aider --help`
2. `aider --yes --message "noop verification"`

### OpenHands

3. `python3 -m openhands.sdk --help`
4. `python3 -m openhands.sdk --condenser llm --max-size 80 --keep-first 3 --help`
5. `python3 -m openhands.sdk --workspace docker --security-level high --inject-failure trace.json --help`

## Return Format

For each command:

- command
- exit_code
- first_20_lines_output
- verdict: `exists_and_behaves` / `exists_but_changed` / `missing`

## Output Artifact

Write result as:

- `/Users/system/syncrescendence/communications/responses/RESPONSE-MANUS-cc79-harness-command-verification.md`
