# Harness Capability Registry CC79 External Overrides

**Class**: capability override layer  
**Purpose**: apply post-registry external verification evidence without rewriting raw CC79 ingest outputs

## Precedence Rule

When a command appears in both:

1. [HARNESS-CAPABILITY-REGISTRY-CC79.md](/Users/system/syncrescendence/orchestration/state/impl/HARNESS-CAPABILITY-REGISTRY-CC79.md)
2. this override layer

the override layer is authoritative because it is derived from later runtime receipts.

## Sources

- [RESPONSE-AJNA-cc79-openclaw-command-verification.md](/Users/system/syncrescendence/communications/responses/RESPONSE-AJNA-cc79-openclaw-command-verification.md)
- [RESPONSE-MANUS-cc79-harness-command-verification.md](/Users/system/syncrescendence/communications/responses/RESPONSE-MANUS-cc79-harness-command-verification.md)
- [RESPONSE-COMMANDER-cc79-openclaw-command-verification.md](/Users/system/syncrescendence/communications/responses/RESPONSE-COMMANDER-cc79-openclaw-command-verification.md)
- [RESPONSE-COMMANDER-cc79-codex-command-verification.md](/Users/system/syncrescendence/communications/responses/RESPONSE-COMMANDER-cc79-codex-command-verification.md)
- [HARNESS-CAPABILITY-REGISTRY-CC79-EXTERNAL-OVERRIDES.json](/Users/system/syncrescendence/orchestration/state/HARNESS-CAPABILITY-REGISTRY-CC79-EXTERNAL-OVERRIDES.json)

## Effective Updates

### OpenClaw

- `openclaw test-skill --help` -> `binary_present_subcommand_unverified` (`T2`)
- `openclaw skills purge --untrusted --help` -> `binary_present_subcommand_unverified` (`T2`)
- `openclaw telemetry export --prom --help` -> `binary_present_subcommand_unverified` (`T2`)
- `openclaw doctor --restore --help` -> `binary_present_subcommand_unverified` (`T2`)

### Aider (Manus sandbox)

- `aider --help` -> `binary_missing` (`T3`)
- `aider --yes --message "noop verification"` -> `binary_missing` (`T3`)

### OpenHands (Manus sandbox)

- `python3 -m openhands.sdk --help` -> `module_missing` (`T3`)
- `python3 -m openhands.sdk --condenser ... --help` -> `module_missing` (`T3`)
- `python3 -m openhands.sdk --workspace docker ... --help` -> `module_missing` (`T3`)

### Codex (local shell)

- `codex --telemetry` -> `command_claim_mismatch` (`T3`)
- `codex apply --patch harness.md.patch` -> `command_claim_mismatch` (`T3`)
- `codex --help` -> `probe_pass` (`T1`)
- `codex apply --help` -> `probe_pass` (`T1`)
