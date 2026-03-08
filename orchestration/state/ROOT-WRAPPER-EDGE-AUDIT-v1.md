# Root Wrapper Edge Audit v1

**Date**: `2026-03-08`  
**Status**: `bounded local edge audit`  
**Subject**: `external caller truth for finalize_cowork_relay_job.py`

## 1. Scope

This audit searched bounded local roots under `/Users/system` for references to:

- `/Users/system/syncrescendence/finalize_cowork_relay_job.py`

The goal was to determine whether live edge automation still invokes the root compatibility wrapper outside the repo.

## 2. Search Roots

Searched roots:

- `/Users/system/syncrescendence`
- `/Users/system/.codex`
- `/Users/system/.config`
- `/Users/system/.local/bin`
- `/Users/system/.zshrc`
- `/Users/system/.zprofile`
- `/Users/system/.bashrc`
- `/Users/system/Library/LaunchAgents`
- `/Users/system/Library/Application Support`
- `/Users/system/Desktop/syncrescendence_pre_schematic_design`
- `/Users/system/Documents`

Hazel-specific inspection also covered:

- `/Users/system/Library/Application Support/Hazel/16777231-58660320.hazelrules`
- `/Users/system/Library/Application Support/Hazel/16777231-58660320.hazellocalrulesdb`
- `/Users/system/Library/Application Support/Hazel/16777231-58660320.hazeldb`
- `/Users/system/Library/Application Support/Hazel/16777231-58660309.hazelrules`
- `/Users/system/Library/Application Support/Hazel/16777231-58660309.hazellocalrulesdb`
- `/Users/system/Library/Application Support/Hazel/16777231-58660309.hazeldb`
- `/Users/system/Library/Preferences/com.noodlesoft.Hazel.plist`

## 3. Confirmed Active Caller Evidence

### 3.1 Active Hazel deployment still points at the root wrapper

Confirmed evidence:

- [com.noodlesoft.Hazel.plist](/Users/system/Library/Preferences/com.noodlesoft.Hazel.plist) lists deployed folder id `16777231-58660320` and `RunState => true`.
- The same preference payload records folder id `16777231-58660320` as Hazel folder `~/syncrescendence/00-ORCHESTRATION/relay/cowork-v1/artifacts/outgoing`.
- [16777231-58660320.hazellocalrulesdb](/Users/system/Library/Application%20Support/Hazel/16777231-58660320.hazellocalrulesdb) records rule id `D3411323-174E-480F-A20D-6596B7366EB8` with `active => true`.
- The same rule database reports `lastSyncTime` corresponding to `2026-03-02T21:01:52.086222+00:00`.
- [16777231-58660320.hazelrules](/Users/system/Library/Application%20Support/Hazel/16777231-58660320.hazelrules) contains the exact shell command:
  - `/usr/bin/env python3 /Users/system/syncrescendence/finalize_cowork_relay_job.py --status-file "$1" --project-ontology`
- [16777231-58660320.hazeldb](/Users/system/Library/Application%20Support/Hazel/16777231-58660320.hazeldb) records:
  - `Last Poll Time` = `2026-03-08T21:37:15Z`
  - `Last Execution Error Time` = `2026-03-08T21:37:15Z` for:
    - `perplexity-20260302-211119-728920-perplexity-relay-prototype.status.json`
    - `perplexity-20260303-012357-608498-cowork-sandbox-smoke-job.status.json`

Assessment:

- This is not merely historical documentation. It is live machine configuration with an enabled rule, a deployed folder, and polling/error timestamps on `2026-03-08`.
- The stored Hazel display path is legacy `00-ORCHESTRATION`, but the current repo still contains matching runtime files under [orchestration/relay/cowork-v1/artifacts/outgoing](/Users/system/syncrescendence/orchestration/relay/cowork-v1/artifacts/outgoing), which is consistent with Hazel following a moved folder via bookmark metadata rather than plain path text.
- Result: the root wrapper retirement is still blocked by confirmed local Hazel automation.

### 3.2 The live Hazel caller is also stale in argument shape

Additional evidence:

- The active Hazel shell command still appends `--project-ontology`.
- [operators/cli-web-gap/finalize_cowork_relay_job.py](/Users/system/syncrescendence/operators/cli-web-gap/finalize_cowork_relay_job.py) currently accepts `--job`, `--status-file`, `--result`, `--note`, and `--citation-count`, but not `--project-ontology`.
- In-repo guidance is split:
  - [orchestration/relay/cowork-v1/HAZEL-RULES.md](/Users/system/syncrescendence/orchestration/relay/cowork-v1/HAZEL-RULES.md) points to the operator path without `--project-ontology`
  - [validated-patterns/cli-web-gap/HAZEL-RULES.md](/Users/system/syncrescendence/validated-patterns/cli-web-gap/HAZEL-RULES.md) points to the operator path but still includes `--project-ontology`

Assessment:

- Even after repointing away from the root wrapper, the live Hazel rule should not be copied forward verbatim.
- The external caller needs both:
  1. path cutover from root wrapper to operator path
  2. argument cutover away from unsupported `--project-ontology`

## 4. Stale Historical Or Non-Caller References

These hits were found but do not constitute live external callers:

- Repo planning, assessment, handoff, and response files under `/Users/system/syncrescendence`
  - these are documentation or prior-wave lineage
- [storage.json](/Users/system/Library/Application%20Support/Antigravity/User/globalStorage/storage.json)
  - contains the wrapper path under `openRecentFile`
  - this is editor/recent-file state, not an automation entrypoint
- Claude local session logs under `/Users/system/Library/Application Support/Claude/local-agent-mode-sessions`
  - contain copied text and prior relay instructions
  - these are session transcripts, not active automation
- Codex state and archived sessions under `/Users/system/.codex`
  - contain prior prompt text and archived output
  - these are historical session artifacts, not edge callers
- Duplicated corpus files under `/Users/system/Desktop/syncrescendence_pre_schematic_design`
  - these are historical/reference documents, not runtime automations

## 5. No-Hit Search Areas

No wrapper references were found in these bounded roots:

- `/Users/system/.config`
- `/Users/system/.local/bin`
- `/Users/system/.zshrc`
- `/Users/system/.zprofile`
- `/Users/system/.bashrc`
- `/Users/system/Library/LaunchAgents`

Also, no additional direct caller surfaces were found in the searched portions of `/Users/system/Library/Application Support` beyond:

- Hazel rule storage
- editor/session-history artifacts

## 6. Recommendation

Wrapper retirement is **still blocked**.

Reason:

- a confirmed live Hazel edge rule still invokes `/Users/system/syncrescendence/finalize_cowork_relay_job.py`
- Hazel polled and attempted that rule on `2026-03-08`
- the same caller is stale enough that it also still passes unsupported `--project-ontology`

Safe next-wave retirement conditions:

1. update the live Hazel rule to call `/Users/system/syncrescendence/operators/cli-web-gap/finalize_cowork_relay_job.py`
2. remove unsupported `--project-ontology` from that live rule unless the operator regains support for it
3. verify one successful Hazel-triggered finalization after the cutover
4. only then delete [finalize_cowork_relay_job.py](/Users/system/syncrescendence/finalize_cowork_relay_job.py) and remove the transitional allowlist entries

## 7. Final Classification

- Confirmed active caller candidates:
  - Hazel deployed folder/rule set `16777231-58660320` for Cowork outgoing status files
- Stale historical references:
  - repo docs, session archives, editor recent-file state, pre-schematic corpus duplicates
- No-hit search areas:
  - shell dotfiles searched, local bin/config roots searched, LaunchAgents searched

## 8. Outcome

- `complete`
