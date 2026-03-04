# Harness Capability Registry CC79 Effective

**Class**: effective capability registry
**Method**: base registry with external override precedence

## Counts

- records: 138
- overrides applied: 13
- T0: 5
- T1: 2
- T2: 110
- T3: 21

## Status Distribution

- `binary_alias_missing_use_python3`: 2
- `binary_missing`: 8
- `binary_present_subcommand_unverified`: 20
- `command_claim_mismatch`: 2
- `module_missing`: 3
- `probe_pass`: 7
- `probe_timeout`: 27
- `quarantined_segment_not_probed`: 8
- `runtime_or_complex_shell_command_unprobed`: 61

## Applied Overrides

- `aider` | `aider --help` -> `binary_missing` `T3`
- `aider` | `aider --yes --message "noop verification"` -> `binary_missing` `T3`
- `codex` | `codex --help` -> `probe_pass` `T1`
- `codex` | `codex --telemetry` -> `command_claim_mismatch` `T3`
- `codex` | `codex apply --help` -> `probe_pass` `T1`
- `codex` | `codex apply --patch harness.md.patch` -> `command_claim_mismatch` `T3`
- `openclaw` | `openclaw doctor --restore --help` -> `binary_present_subcommand_unverified` `T2`
- `openclaw` | `openclaw skills purge --untrusted --help` -> `binary_present_subcommand_unverified` `T2`
- `openclaw` | `openclaw telemetry export --prom --help` -> `binary_present_subcommand_unverified` `T2`
- `openclaw` | `openclaw test-skill --help` -> `binary_present_subcommand_unverified` `T2`
- `openhands` | `python3 -m openhands.sdk --condenser llm --max-size 80 --keep-first 3 --help` -> `module_missing` `T3`
- `openhands` | `python3 -m openhands.sdk --help` -> `module_missing` `T3`
- `openhands` | `python3 -m openhands.sdk --workspace docker --security-level high --inject-failure trace.json --help` -> `module_missing` `T3`

## Effective Registry

| Harness | Tier | Status | Command | Source | Detail |
|---|---|---|---|---|---|
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/add` | `report-grok-aider.md` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/ask` | `report-grok-aider.md` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/code` | `report-grok-aider.md` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/drop` | `report-grok-aider.md` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/image <screenshot.png>` | `report-grok-aider.md` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/read` | `report-grok-aider.md` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/read CONVENTIONS.md` | `report-grok-aider.md` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/undo` | `report-grok-aider.md` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/voice` | `report-grok-aider.md` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/web https://…` | `report-grok-aider.md` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `git blame --line-porcelain \| grep ^author \| cut -d' ' -f2- \| sort \| uniq -c` | `report-grok-aider.md` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `git log --author=Aider --since=1m \| wc -l` | `report-grok-aider.md` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `git log --since=1day --oneline \| wc -l` | `report-grok-aider.md` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T3 | binary_missing | `aider --help` | `RESPONSE-MANUS-cc79-harness-command-verification.md` | command not found in Manus sandbox |
| aider | T3 | binary_missing | `aider --message "implement the attached design" --image design.png --yes` | `report-grok-aider.md` | binary not present on this machine |
| aider | T3 | binary_missing | `aider --yes --message "execute plan"` | `report-grok-aider.md` | binary not present on this machine |
| aider | T3 | binary_missing | `aider --yes --message "noop verification"` | `RESPONSE-MANUS-cc79-harness-command-verification.md` | command not found in Manus sandbox |
| codex | T1 | probe_pass | `codex --help` | `RESPONSE-COMMANDER-cc79-codex-command-verification.md` | top-level help command verified locally |
| codex | T1 | probe_pass | `codex apply --help` | `RESPONSE-COMMANDER-cc79-codex-command-verification.md` | subcommand help verified locally |
| codex | T2 | binary_present_subcommand_unverified | `codex fine-tune --base gpt-5.3-codex --dataset telemetry-skill.jsonl --private` | `report-grok-codex.md` | Codex CLI |
| codex | T2 | binary_present_subcommand_unverified | `codex fork-thread --role=reviewer` | `report-grok-codex.md` | Codex CLI |
| codex | T2 | binary_present_subcommand_unverified | `codex pr create` | `report-grok-codex.md` | Codex CLI |
| codex | T2 | binary_present_subcommand_unverified | `codex rebaseline --global-harness` | `report-grok-codex.md` | Codex CLI |
| codex | T2 | binary_present_subcommand_unverified | `codex redteam --surface all --sandbox read-only --audit otel` | `report-grok-codex.md` | Codex CLI |
| codex | T2 | binary_present_subcommand_unverified | `codex start "refactor auth" --multi-agent` | `report-grok-codex.md` | Codex CLI |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `$setup; $start "task"; /self-reflect` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `$skill-creator` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `$skill-creator "telemetry dashboard" → generates SKILL.md + yaml → invoke in AGENTS.md` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `$start "epic refactor" --topology hierarchical-mesh` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `$start "refactor auth"` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `/compact` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `/self-reflect` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `/self-reflect --target codex-cli --output harness.md.patch` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `codex compact; codex prime --keywords PLANS.md AGENTS.md; spawn_agents_on_csv` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `codex export-history --format jsonl --metrics velocity,errors > roi.jsonl` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `codex export-history --format jsonl --since 7d > velocity.jsonl` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `codex export-history --format jsonl > dashboard.jsonl` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `curl -sSL https://raw.githubusercontent.com/dsifry/metaswarm/main/.codex/install.sh \| bash` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `jq '.[] \| "Tasks: \(.tasks) \| $ saved: \(.hours*150)"' roi.jsonl` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `jq '.[] \| select(.error_type=="logic")' dashboard.jsonl \| wc -l` | `report-grok-codex.md` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T3 | binary_missing | `skills.sh export telemetry-skill --format dataset` | `report-grok-codex.md` | binary not present on this machine |
| codex | T3 | binary_missing | `skills.sh publish --registry public` | `report-grok-codex.md` | binary not present on this machine |
| codex | T3 | command_claim_mismatch | `codex --telemetry` | `RESPONSE-COMMANDER-cc79-codex-command-verification.md` | unexpected argument '--telemetry' on live codex CLI |
| codex | T3 | command_claim_mismatch | `codex apply --patch harness.md.patch` | `RESPONSE-COMMANDER-cc79-codex-command-verification.md` | unexpected argument '--patch'; codex apply expects TASK_ID |
| openclaw | T2 | binary_present_subcommand_unverified | `git rollback` | `report-grok-openclaw.md` | git: 'rollback' is not a git command. See 'git --help'. |
| openclaw | T2 | binary_present_subcommand_unverified | `openclaw doctor --restore --help` | `RESPONSE-COMMANDER-cc79-openclaw-command-verification.md` | doctor command exists but --restore flag absent |
| openclaw | T2 | binary_present_subcommand_unverified | `openclaw skills purge --untrusted --help` | `RESPONSE-COMMANDER-cc79-openclaw-command-verification.md` | skills purge not present in observed command tree |
| openclaw | T2 | binary_present_subcommand_unverified | `openclaw telemetry export --prom --help` | `RESPONSE-COMMANDER-cc79-openclaw-command-verification.md` | telemetry command not present in observed command tree |
| openclaw | T2 | binary_present_subcommand_unverified | `openclaw test-skill --help` | `RESPONSE-COMMANDER-cc79-openclaw-command-verification.md` | top-level help returned; subcommand not confirmed |
| openclaw | T2 | probe_timeout | `openclaw daemon stop` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw debug ledger --sync-test` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw doctor --blue-green-test` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw doctor --restore` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw gateway --port 18789` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw memory compact` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw node describe --all` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw node kill --id pi-01` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw promote` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw reset --logs` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw skills purge --untrusted` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw skills purge --vt-fail` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw swarm scale --down` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw telemetry export --prom` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw test-skill` | `report-grok-openclaw.md` | probe timeout |
| openclaw | T2 | runtime_or_complex_shell_command_unprobed | `openclaw replay --session <id>` | `report-grok-openclaw.md` | slash-command or complex shell syntax; kept as operational pattern only |
| openclaw | T3 | quarantined_segment_not_probed | `codex "Run $skill-creator: new skill for test coverage"` | `report-grok-openclaw.md` | segment quarantined |
| openclaw | T3 | quarantined_segment_not_probed | `codex "Self-reflect on last failure and edit AGENTS.md"` | `report-grok-openclaw.md` | segment quarantined |
| openclaw | T3 | quarantined_segment_not_probed | `codex --cd . "List active instruction sources"` | `report-grok-openclaw.md` | segment quarantined |
| openclaw | T3 | quarantined_segment_not_probed | `codex --features multi_agent=true "Fork sub-agents for frontend/backend"` | `report-grok-openclaw.md` | segment quarantined |
| openclaw | T3 | quarantined_segment_not_probed | `codex debug clear-memories` | `report-grok-openclaw.md` | segment quarantined |
| openclaw | T3 | quarantined_segment_not_probed | `codex mcp-server` | `report-grok-openclaw.md` | segment quarantined |
| openclaw | T3 | quarantined_segment_not_probed | `codex mcp-server --port 8080 # recursive orchestration` | `report-grok-openclaw.md` | segment quarantined |
| openclaw | T3 | quarantined_segment_not_probed | `codex status` | `report-grok-openclaw.md` | segment quarantined |
| opencode | T0 | probe_pass | `git clone https://github.com/anomalyco/opencode` | `report-grok-opencode.md` | GIT-CLONE(1)                      Git Manual                      GIT-CLONE(1) |
| opencode | T0 | probe_pass | `git clone https://github.com/opencode-ai/opencode` | `report-grok-opencode.md` | GIT-CLONE(1)                      Git Manual                      GIT-CLONE(1) |
| opencode | T0 | probe_pass | `git restore AGENTS.md` | `report-grok-opencode.md` | GIT-RESTORE(1)                    Git Manual                    GIT-RESTORE(1) |
| opencode | T0 | probe_pass | `npm install -g opencode-swarm opencode-agent-memory` | `report-grok-opencode.md` | Install a package |
| opencode | T0 | probe_pass | `opencode serve` | `report-grok-opencode.md` | opencode serve |
| opencode | T2 | binary_present_subcommand_unverified | `go build` | `report-grok-opencode.md` | usage: go build [-o output] [build flags] [packages] |
| opencode | T2 | binary_present_subcommand_unverified | `go build -ldflags="-s -w" -o opencode-custom ./cmd/opencode` | `report-grok-opencode.md` | usage: go build [-o output] [build flags] [packages] |
| opencode | T2 | binary_present_subcommand_unverified | `opencode /connect` | `report-grok-opencode.md` | [0m▄[0m |
| opencode | T2 | binary_present_subcommand_unverified | `opencode /connect --local` | `report-grok-opencode.md` | [0m▄[0m |
| opencode | T2 | binary_present_subcommand_unverified | `opencode /init` | `report-grok-opencode.md` | [0m▄[0m |
| opencode | T2 | binary_present_subcommand_unverified | `opencode /reload-plugins` | `report-grok-opencode.md` | [0m▄[0m |
| opencode | T2 | binary_present_subcommand_unverified | `opencode bench` | `report-grok-opencode.md` | [0m▄[0m |
| opencode | T2 | binary_present_subcommand_unverified | `opencode export-session` | `report-grok-opencode.md` | [0m▄[0m |
| opencode | T2 | binary_present_subcommand_unverified | `opencode export-trace --format mermaid` | `report-grok-opencode.md` | [0m▄[0m |
| opencode | T2 | probe_timeout | `git reset --hard` | `report-grok-opencode.md` | probe timeout |
| opencode | T2 | probe_timeout | `opencode --agent-inspect-persona @successor` | `report-grok-opencode.md` | probe timeout |
| opencode | T2 | probe_timeout | `opencode --local` | `report-grok-opencode.md` | probe timeout |
| opencode | T2 | probe_timeout | `opencode --profile` | `report-grok-opencode.md` | probe timeout |
| opencode | T2 | probe_timeout | `opencode --trace` | `report-grok-opencode.md` | probe timeout |
| opencode | T2 | probe_timeout | `opencode debug config` | `report-grok-opencode.md` | probe timeout |
| opencode | T2 | probe_timeout | `opencode debug config --validate` | `report-grok-opencode.md` | probe timeout |
| opencode | T2 | probe_timeout | `opencode debug paths` | `report-grok-opencode.md` | probe timeout |
| opencode | T2 | probe_timeout | `opencode plugin add code-yeongyu/oh-my-opencode joshuadavidthomas/opencode-agent-memory zaxbysauce/opencode-swarm` | `report-grok-opencode.md` | probe timeout |
| opencode | T2 | probe_timeout | `opencode plugin add joshuadavidthomas/opencode-agent-memory` | `report-grok-opencode.md` | probe timeout |
| opencode | T2 | probe_timeout | `opencode plugin pin` | `report-grok-opencode.md` | probe timeout |
| opencode | T2 | probe_timeout | `opencode ultrawork` | `report-grok-opencode.md` | probe timeout |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `/connect` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `/redo` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `/share` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `/ulw-loop` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `/undo` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `curl -fsSL https://opencode.ai/install \| bash` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `curl -fsSL https://raw.githubusercontent.com/code-yeongyu/oh-my-opencode/main/install \| bash` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `git clone ... && go build -o /usr/local/bin/opencode-custom && opencode-custom --version` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `git clone https://github.com/anomalyco/opencode && cd opencode && go run . serve --daemon && opencode --daemon-status` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `git clone https://github.com/anomalyco/opencode && go run . /init && opencode --debug \| grep lsp` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `git clone https://github.com/joshuadavidthomas/opencode-agent-memory && opencode /init && echo '{"plugin":["./opencode-agent-memory"]}' > opencode.json && opencode --debug \| grep memory` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `git reset --hard origin/main && go build` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `npm install -g opencode-swarm && opencode serve --background` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode --local && opencode serve` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode --trace --new-session && opencode export-session` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /connect --local && opencode debug config \| grep -E 'permission\|mcp'` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && cp AGENTS.md ~/.continue/rules.md && code --install-extension continue.continue` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && echo '{"lsp":{"pyright":{"disabled":false}},"small_model":"ollama/llama3.2"}' > opencode.json && opencode --debug` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && echo '{"permission":{"junior":{"edit":"ask"}}}' >> opencode.json` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && memory_set persona "self-editing meta-agent"` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && opencode --debug` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && opencode --debug && cat ~/.config/opencode/opencode.json \| grep -E 'small_model\|autoCompact'` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && opencode --debug \| grep lsp` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && opencode plugin add joshuadavidthomas/opencode-agent-memory && opencode memory-evolve --dry-run` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode debug config --remove-plugin myplugin && rm -rf .opencode/plugins/myplugin` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode debug config \| grep mcp` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode debug config; journal_read; /undo` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode export-persistent-state --format json > backup.json && opencode import-session backup.json` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode export-session --format json \| jq '.summary' > reset.md && opencode --new-session` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode serve --background && opencode ultrawork "ship production feature X unsupervised"` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode serve --background && opencode ultrawork "ship production feature X"` | `report-grok-opencode.md` | slash-command or complex shell syntax; kept as operational pattern only |
| openhands | T2 | binary_alias_missing_use_python3 | `python -m openhands.sdk --condenser llm --max-size 80 --keep-first 3` | `report-grok-openhands.md` | python missing; python3 is present on this machine |
| openhands | T2 | binary_alias_missing_use_python3 | `python -m openhands.sdk --workspace docker --security-level high --inject-failure trace.json` | `report-grok-openhands.md` | python missing; python3 is present on this machine |
| openhands | T2 | runtime_or_complex_shell_command_unprobed | `git add .openhands/skills && git commit -m "self-refine"` | `report-grok-openhands.md` | slash-command or complex shell syntax; kept as operational pattern only |
| openhands | T3 | binary_missing | `helm upgrade --set autoscaling.enabled=true --set prometheus.trigger=latency` | `report-grok-openhands.md` | binary not present on this machine |
| openhands | T3 | binary_missing | `openhands --airgap --rbac team-x` | `report-grok-openhands.md` | binary not present on this machine |
| openhands | T3 | module_missing | `python3 -m openhands.sdk --condenser llm --max-size 80 --keep-first 3 --help` | `RESPONSE-MANUS-cc79-harness-command-verification.md` | No module named 'openhands' in Manus sandbox |
| openhands | T3 | module_missing | `python3 -m openhands.sdk --help` | `RESPONSE-MANUS-cc79-harness-command-verification.md` | No module named 'openhands' in Manus sandbox |
| openhands | T3 | module_missing | `python3 -m openhands.sdk --workspace docker --security-level high --inject-failure trace.json --help` | `RESPONSE-MANUS-cc79-harness-command-verification.md` | No module named 'openhands' in Manus sandbox |
