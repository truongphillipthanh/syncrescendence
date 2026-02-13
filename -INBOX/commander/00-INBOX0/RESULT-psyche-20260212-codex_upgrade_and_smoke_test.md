# RESULT-psyche-20260212-codex_upgrade_and_smoke_test

(Delivered via Psyche to Commander)

**Task**: TASK-20260212-codex_upgrade_and_smoke_test.md  
**Agent**: psyche  
**Exit-Code**: 0  
**Completed-At**: 2026-02-13T02:45:55Z

---

## (1) Upgrade Codex CLI (Mac mini)
Ran per instructions:
- `brew upgrade codex`

Observed:
- `Error: Cask 'codex' is not installed.`
- Existing `codex` binary was npm-installed (`@openai/codex@0.94.0`) with `/opt/homebrew/bin/codex` as a symlink into `/opt/homebrew/lib/node_modules/...`.

To complete the upgrade via Homebrew (matching task intent):
- Backed up old npm-provided binary:
  - `/opt/homebrew/bin/codex` → `/opt/homebrew/bin/codex.npm.backup.20260213T024402Z`
- Installed Codex cask:
  - `brew install --cask codex`
- Re-ran:
  - `brew upgrade codex` → `Not upgrading codex, the latest version is already installed`

Version after:
- `codex --version` → **codex-cli 0.101.0**

---

## (2) Adjudicator model access smoke test
Command:
- `codex exec -m gpt-5.2-codex 'Reply exactly: ADJUDICATOR_MODEL_OK'`

Result:
- Final output: **ADJUDICATOR_MODEL_OK**
