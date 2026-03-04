# Harness Promoted Atoms Smoke

**Generated**: 2026-03-04T21:34:13Z
**Class**: promoted atom smoke verification

## Summary

- probes: 3
- passed: 3
- failed: 0

## Results

| Harness | Claim Command | Probe Command | Exit | Pass | Note |
|---|---|---|---:|---|---|
| codex | `codex --help` | `codex --help` | 0 | yes | direct promoted atom |

Expected: `Codex CLI`

Observed excerpt:
```text
Codex CLI

If no subcommand is specified, options will be forwarded to the interactive CLI.

Usage: codex [OPTIONS] [PROMPT]
       codex [OPTIONS] <COMMAND> [ARGS]

Commands:
  exec        Run Codex non-interactively [aliases: e]
  review      Run a code review non-interactively
  login       Manage login
  logout      Remove stored authentication credentials
```

| codex | `codex apply --help` | `codex apply --help` | 0 | yes | direct promoted atom |

Expected: `Usage: codex apply`

Observed excerpt:
```text
Apply the latest diff produced by Codex agent as a `git apply` to your local working tree

Usage: codex apply [OPTIONS] <TASK_ID>

Arguments:
  <TASK_ID>
          

Options:
  -c, --config <key=value>
          Override a configuration value that would otherwise be loaded from `~/.codex/config.toml`.
          Use a dotted path (`foo.bar.baz`) to override nested values. The `value` portion is parsed
```

| opencode | `opencode serve` | `opencode serve --help` | 0 | yes | safe help-form probe for long-running serve command |

Expected: `opencode serve`

Observed excerpt:
```text
opencode serve

starts a headless opencode server

Options:
  -h, --help         show help                                                             [boolean]
  -v, --version      show version number                                                   [boolean]
      --print-logs   print logs to stderr                                                  [boolean]
      --log-level    log level                  [string] [choices: "DEBUG", "INFO", "WARN", "ERROR"]
      --port         port to listen on                                         [number] [default: 0]
      --hostname     hostname to listen on                           [string] [default: "127.0.0.1"]
      --mdns         enable mDNS service discovery (defaults hostname to 0.0.0.0)
```
