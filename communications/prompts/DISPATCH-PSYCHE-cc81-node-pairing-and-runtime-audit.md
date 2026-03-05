# DISPATCH-PSYCHE-cc81-node-pairing-and-runtime-audit

## Mission

Develop Psyche's ability to execute identity-cutover support tasks from the Mac mini runtime substrate.

## Current Blocker

`openclaw nodes list --json` from Commander reports:
- `pending: []`
- `paired: []`

No remote node pairing exists yet, so Psyche cannot be invoked via `openclaw nodes` from this machine.

## Required Work

1. Establish paired-node capability between Commander machine and Psyche runtime.
2. Produce a repeatable runtime-audit command bundle for Mac mini that reports:
   - active OpenClaw identity/account bindings
   - gateway/daemon health
   - keychain pointer presence (pointer-only, no secret values)
   - tmux substrate readiness
3. Return a concise runbook for pre-cutover and post-cutover checks.

## Output Format

Provide a markdown response with:

1. `pairing_status`
2. `commands_executed`
3. `artifacts_written`
4. `remaining_blockers`
5. `next_actions`

## Constraints

1. No secrets in output.
2. Pointer-only credential evidence.
3. No hidden state changes; list every mutation.
