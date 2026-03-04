# CC79 Harness Capability Registry

**Class**: command capability registry
**Method**: extracted commands from sanitized harness segments + local safety probes

## Tier Counts

- `T0`: 7
- `T1`: 0
- `T2`: 106
- `T3`: 14

## Registry

| Harness | Tier | Status | Command | Probe | Detail |
|---|---|---|---|---|---|
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/add` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/ask` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/code` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/drop` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/image <screenshot.png>` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/read` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/read CONVENTIONS.md` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/undo` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/voice` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `/web https://…` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `git blame --line-porcelain \| grep ^author \| cut -d' ' -f2- \| sort \| uniq -c` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `git log --author=Aider --since=1m \| wc -l` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T2 | runtime_or_complex_shell_command_unprobed | `git log --since=1day --oneline \| wc -l` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| aider | T3 | binary_missing | `aider --message "implement the attached design" --image design.png --yes` | `aider --help` | binary not present on this machine |
| aider | T3 | binary_missing | `aider --yes --message "execute plan"` | `aider --help` | binary not present on this machine |
| codex | T0 | probe_pass | `codex --telemetry` | `codex --help` | Codex CLI |
| codex | T0 | probe_pass | `codex apply --patch harness.md.patch` | `codex apply --help` | Apply the latest diff produced by Codex agent as a `git apply` to your local working tree |
| codex | T2 | binary_present_subcommand_unverified | `codex fine-tune --base gpt-5.3-codex --dataset telemetry-skill.jsonl --private` | `codex fine-tune --help` | Codex CLI |
| codex | T2 | binary_present_subcommand_unverified | `codex fork-thread --role=reviewer` | `codex fork-thread --help` | Codex CLI |
| codex | T2 | binary_present_subcommand_unverified | `codex pr create` | `codex pr --help` | Codex CLI |
| codex | T2 | binary_present_subcommand_unverified | `codex rebaseline --global-harness` | `codex rebaseline --help` | Codex CLI |
| codex | T2 | binary_present_subcommand_unverified | `codex redteam --surface all --sandbox read-only --audit otel` | `codex redteam --help` | Codex CLI |
| codex | T2 | binary_present_subcommand_unverified | `codex start "refactor auth" --multi-agent` | `codex start --help` | Codex CLI |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `$setup; $start "task"; /self-reflect` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `$skill-creator` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `$skill-creator "telemetry dashboard" → generates SKILL.md + yaml → invoke in AGENTS.md` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `$start "epic refactor" --topology hierarchical-mesh` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `$start "refactor auth"` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `/compact` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `/self-reflect` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `/self-reflect --target codex-cli --output harness.md.patch` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `codex compact; codex prime --keywords PLANS.md AGENTS.md; spawn_agents_on_csv` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `codex export-history --format jsonl --metrics velocity,errors > roi.jsonl` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `codex export-history --format jsonl --since 7d > velocity.jsonl` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `codex export-history --format jsonl > dashboard.jsonl` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `curl -sSL https://raw.githubusercontent.com/dsifry/metaswarm/main/.codex/install.sh \| bash` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `jq '.[] \| "Tasks: \(.tasks) \| $ saved: \(.hours*150)"' roi.jsonl` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T2 | runtime_or_complex_shell_command_unprobed | `jq '.[] \| select(.error_type=="logic")' dashboard.jsonl \| wc -l` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| codex | T3 | binary_missing | `skills.sh export telemetry-skill --format dataset` | `skills.sh export --help` | binary not present on this machine |
| codex | T3 | binary_missing | `skills.sh publish --registry public` | `skills.sh publish --help` | binary not present on this machine |
| openclaw | T2 | binary_present_subcommand_unverified | `git rollback` | `git rollback --help` | git: 'rollback' is not a git command. See 'git --help'. |
| openclaw | T2 | probe_timeout | `openclaw daemon stop` | `openclaw daemon --help` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw debug ledger --sync-test` | `openclaw debug --help` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw doctor --blue-green-test` | `openclaw doctor --help` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw doctor --restore` | `openclaw doctor --help` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw gateway --port 18789` | `openclaw gateway --help` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw memory compact` | `openclaw memory --help` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw node describe --all` | `openclaw node --help` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw node kill --id pi-01` | `openclaw node --help` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw promote` | `openclaw promote --help` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw reset --logs` | `openclaw reset --help` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw skills purge --untrusted` | `openclaw skills --help` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw skills purge --vt-fail` | `openclaw skills --help` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw swarm scale --down` | `openclaw swarm --help` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw telemetry export --prom` | `openclaw telemetry --help` | probe timeout |
| openclaw | T2 | probe_timeout | `openclaw test-skill` | `openclaw test-skill --help` | probe timeout |
| openclaw | T2 | runtime_or_complex_shell_command_unprobed | `openclaw replay --session <id>` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| openclaw | T3 | quarantined_segment_not_probed | `codex "Run $skill-creator: new skill for test coverage"` | `` | segment quarantined |
| openclaw | T3 | quarantined_segment_not_probed | `codex "Self-reflect on last failure and edit AGENTS.md"` | `` | segment quarantined |
| openclaw | T3 | quarantined_segment_not_probed | `codex --cd . "List active instruction sources"` | `` | segment quarantined |
| openclaw | T3 | quarantined_segment_not_probed | `codex --features multi_agent=true "Fork sub-agents for frontend/backend"` | `` | segment quarantined |
| openclaw | T3 | quarantined_segment_not_probed | `codex debug clear-memories` | `` | segment quarantined |
| openclaw | T3 | quarantined_segment_not_probed | `codex mcp-server` | `` | segment quarantined |
| openclaw | T3 | quarantined_segment_not_probed | `codex mcp-server --port 8080 # recursive orchestration` | `` | segment quarantined |
| openclaw | T3 | quarantined_segment_not_probed | `codex status` | `` | segment quarantined |
| opencode | T0 | probe_pass | `git clone https://github.com/anomalyco/opencode` | `git clone --help` | GIT-CLONE(1)                      Git Manual                      GIT-CLONE(1) |
| opencode | T0 | probe_pass | `git clone https://github.com/opencode-ai/opencode` | `git clone --help` | GIT-CLONE(1)                      Git Manual                      GIT-CLONE(1) |
| opencode | T0 | probe_pass | `git restore AGENTS.md` | `git restore --help` | GIT-RESTORE(1)                    Git Manual                    GIT-RESTORE(1) |
| opencode | T0 | probe_pass | `npm install -g opencode-swarm opencode-agent-memory` | `npm install --help` | Install a package |
| opencode | T0 | probe_pass | `opencode serve` | `opencode serve --help` | opencode serve |
| opencode | T2 | binary_present_subcommand_unverified | `go build` | `go build --help` | usage: go build [-o output] [build flags] [packages] |
| opencode | T2 | binary_present_subcommand_unverified | `go build -ldflags="-s -w" -o opencode-custom ./cmd/opencode` | `go build --help` | usage: go build [-o output] [build flags] [packages] |
| opencode | T2 | binary_present_subcommand_unverified | `opencode /connect` | `opencode /connect --help` | [0m▄[0m |
| opencode | T2 | binary_present_subcommand_unverified | `opencode /connect --local` | `opencode /connect --help` | [0m▄[0m |
| opencode | T2 | binary_present_subcommand_unverified | `opencode /init` | `opencode /init --help` | [0m▄[0m |
| opencode | T2 | binary_present_subcommand_unverified | `opencode /reload-plugins` | `opencode /reload-plugins --help` | [0m▄[0m |
| opencode | T2 | binary_present_subcommand_unverified | `opencode bench` | `opencode bench --help` | [0m▄[0m |
| opencode | T2 | binary_present_subcommand_unverified | `opencode export-session` | `opencode export-session --help` | [0m▄[0m |
| opencode | T2 | binary_present_subcommand_unverified | `opencode export-trace --format mermaid` | `opencode export-trace --help` | [0m▄[0m |
| opencode | T2 | probe_timeout | `git reset --hard` | `git reset --help` | probe timeout |
| opencode | T2 | probe_timeout | `opencode --agent-inspect-persona @successor` | `opencode --help` | probe timeout |
| opencode | T2 | probe_timeout | `opencode --local` | `opencode --help` | probe timeout |
| opencode | T2 | probe_timeout | `opencode --profile` | `opencode --help` | probe timeout |
| opencode | T2 | probe_timeout | `opencode --trace` | `opencode --help` | probe timeout |
| opencode | T2 | probe_timeout | `opencode debug config` | `opencode debug --help` | probe timeout |
| opencode | T2 | probe_timeout | `opencode debug config --validate` | `opencode debug --help` | probe timeout |
| opencode | T2 | probe_timeout | `opencode debug paths` | `opencode debug --help` | probe timeout |
| opencode | T2 | probe_timeout | `opencode plugin add code-yeongyu/oh-my-opencode joshuadavidthomas/opencode-agent-memory zaxbysauce/opencode-swarm` | `opencode plugin --help` | probe timeout |
| opencode | T2 | probe_timeout | `opencode plugin add joshuadavidthomas/opencode-agent-memory` | `opencode plugin --help` | probe timeout |
| opencode | T2 | probe_timeout | `opencode plugin pin` | `opencode plugin --help` | probe timeout |
| opencode | T2 | probe_timeout | `opencode ultrawork` | `opencode ultrawork --help` | probe timeout |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `/connect` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `/redo` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `/share` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `/ulw-loop` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `/undo` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `curl -fsSL https://opencode.ai/install \| bash` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `curl -fsSL https://raw.githubusercontent.com/code-yeongyu/oh-my-opencode/main/install \| bash` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `git clone ... && go build -o /usr/local/bin/opencode-custom && opencode-custom --version` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `git clone https://github.com/anomalyco/opencode && cd opencode && go run . serve --daemon && opencode --daemon-status` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `git clone https://github.com/anomalyco/opencode && go run . /init && opencode --debug \| grep lsp` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `git clone https://github.com/joshuadavidthomas/opencode-agent-memory && opencode /init && echo '{"plugin":["./opencode-agent-memory"]}' > opencode.json && opencode --debug \| grep memory` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `git reset --hard origin/main && go build` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `npm install -g opencode-swarm && opencode serve --background` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode --local && opencode serve` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode --trace --new-session && opencode export-session` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /connect --local && opencode debug config \| grep -E 'permission\|mcp'` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && cp AGENTS.md ~/.continue/rules.md && code --install-extension continue.continue` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && echo '{"lsp":{"pyright":{"disabled":false}},"small_model":"ollama/llama3.2"}' > opencode.json && opencode --debug` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && echo '{"permission":{"junior":{"edit":"ask"}}}' >> opencode.json` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && memory_set persona "self-editing meta-agent"` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && opencode --debug` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && opencode --debug && cat ~/.config/opencode/opencode.json \| grep -E 'small_model\|autoCompact'` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && opencode --debug \| grep lsp` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode /init && opencode plugin add joshuadavidthomas/opencode-agent-memory && opencode memory-evolve --dry-run` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode debug config --remove-plugin myplugin && rm -rf .opencode/plugins/myplugin` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode debug config \| grep mcp` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode debug config; journal_read; /undo` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode export-persistent-state --format json > backup.json && opencode import-session backup.json` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode export-session --format json \| jq '.summary' > reset.md && opencode --new-session` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode serve --background && opencode ultrawork "ship production feature X unsupervised"` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| opencode | T2 | runtime_or_complex_shell_command_unprobed | `opencode serve --background && opencode ultrawork "ship production feature X"` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| openhands | T2 | binary_alias_missing_use_python3 | `python -m openhands.sdk --condenser llm --max-size 80 --keep-first 3` | `python --help` | python missing; python3 is present on this machine |
| openhands | T2 | binary_alias_missing_use_python3 | `python -m openhands.sdk --workspace docker --security-level high --inject-failure trace.json` | `python --help` | python missing; python3 is present on this machine |
| openhands | T2 | runtime_or_complex_shell_command_unprobed | `git add .openhands/skills && git commit -m "self-refine"` | `` | slash-command or complex shell syntax; kept as operational pattern only |
| openhands | T3 | binary_missing | `helm upgrade --set autoscaling.enabled=true --set prometheus.trigger=latency` | `helm upgrade --help` | binary not present on this machine |
| openhands | T3 | binary_missing | `openhands --airgap --rbac team-x` | `openhands --help` | binary not present on this machine |
