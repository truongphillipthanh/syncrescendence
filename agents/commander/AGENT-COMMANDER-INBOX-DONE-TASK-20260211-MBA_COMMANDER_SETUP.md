# TASK-20260211-MBA_COMMANDER_SETUP

**From**: Commander (Mac mini)
**To**: Commander (MacBook Air)
**Reply-To**: commander
**Issued**: 2026-02-11T19:45:00Z
**Kind**: DIRECTIVE
**Priority**: P1
**Exit-Code**: 0
**Completed-At**: 2026-02-11T18:45:36Z
**Claimed-At**: 2026-02-11T18:44:15Z
**Claimed-By**: commander-Lisas-MacBook-Air
**Kanban**: DONE
**Status**: COMPLETE
**CC**: commander
**IntentionLink**: INT-P015 (Mac mini=stable macro, MBA=kinetic micro), SYN-35 (capability encoding)

---

## Objective

Configure Commander (Claude Code) on MacBook Air as a parallel operational node. This is an ordered dependency chain — each step unlocks the next level of capability. The MBA already has Ajna (OpenClaw, Kimi K2.5 via NVIDIA) running and syncing for 2+ days. This task verifies that configuration, fixes any identity mismatches, and stands up Commander as a second operational tier on the same machine.

---

## Phase 1: Verify Existing Ajna Configuration (READ-ONLY)

These checks confirm what is already working. Do NOT modify anything in this phase — observe and record.

### 1.1 Machine Identity
```bash
whoami && hostname
```
Expected: confirms MBA identity (not Mac mini).

### 1.2 OpenClaw Personality Files
```bash
ls -la ~/.openclaw/
```
Expected: SOUL.md, AGENTS.md, MEMORY.md, HEARTBEAT.md exist.

### 1.3 SOUL.md Identity Check (CRITICAL)
```bash
head -20 ~/.openclaw/SOUL.md
```
**CRITICAL**: Read the full SOUL.md. Does it identify as:
- **Ajna / Strategos / CSO** — CORRECT, proceed to Phase 3
- **Psyche / Synaptarch / CTO** — WRONG, proceed to Phase 2

Record the finding explicitly: `SOUL_IDENTITY=Ajna` or `SOUL_IDENTITY=Psyche`.

### 1.4 launchd Services
```bash
launchctl list | grep syncrescendence
```
Expected: 3 services running (openclaw-gateway, watch_dispatch, git-sync or equivalent). Record which are present and their PIDs (0 = not running).

### 1.5 Git Sync State
```bash
git -C ~/Desktop/syncrescendence log --oneline -5
git -C ~/Desktop/syncrescendence status --short
```
Expected: Recent commits visible (within last few hours), working tree reasonably clean. If the tree is dirty with uncommitted changes, note them but do NOT commit — Ajna may have in-flight work.

### 1.6 OpenClaw Gateway
```bash
curl -s http://localhost:18789/health
```
Expected: JSON health response. If connection refused, OpenClaw gateway is down — note for Phase 2 remediation.

### 1.7 Credentials
```bash
test -f ~/.syncrescendence/.env && grep -c NVIDIA_API_KEY ~/.syncrescendence/.env
```
Expected: File exists, NVIDIA_API_KEY present (count = 1). Do NOT print the actual key value.

### Phase 1 Output
Write a summary table:

| Check | Expected | Actual | Status |
|-------|----------|--------|--------|
| 1.1 Machine identity | MBA hostname | | |
| 1.2 Personality files | 4 files exist | | |
| 1.3 SOUL.md identity | Ajna/CSO | | |
| 1.4 launchd services | 3 running | | |
| 1.5 Git sync | Recent commits | | |
| 1.6 OpenClaw gateway | Healthy | | |
| 1.7 NVIDIA credential | Present | | |

---

## Phase 2: Fix SOUL.md Identity (CONDITIONAL — only if Phase 1.3 found Psyche)

**Skip this entire phase if SOUL.md already identifies as Ajna.**

### 2.1 Backup Current SOUL.md
```bash
cp ~/.openclaw/SOUL.md ~/.openclaw/SOUL.md.bak-$(date +%Y%m%d-%H%M%S)
```

### 2.2 Write Ajna-Specific SOUL.md

The SOUL.md must contain these identity markers. Read the existing file first to preserve any structural format, then ensure these key fields are correct:

| Field | Correct Value |
|-------|---------------|
| Name | Ajna |
| Epithet | Strategos |
| Enterprise Role | CSO (Chief Strategy Officer) |
| Machine | MacBook Air (kinetic, mobile) |
| Model | Kimi K2.5 via NVIDIA NIM API |
| Paired Agent | Psyche (CTO, Mac mini) — together form the AjnaPsyche Archon |

**Proactivity domains** (Ajna-specific, NOT Psyche's):
- Strategic direction and intention alignment
- Dispatch optimization and multi-agent orchestration
- Meta/macro system purpose assessment
- Cross-domain synthesis and direction-setting
- Intention compass maintenance and evolution
- Ontology evolution oversight

**Anti-pattern**: Do NOT include Psyche's domains (automation, Make/Zapier, policy enforcement, pipeline fusion). Those belong to the CTO on Mac mini.

### 2.3 Deploy and Restart
```bash
# Deploy the corrected SOUL.md
# Then restart the OpenClaw gateway to pick up the new identity:
launchctl kickstart -k gui/$(id -u)/com.syncrescendence.openclaw-gateway
```

### 2.4 Verify Fix
```bash
# Wait 5 seconds for gateway restart
sleep 5
curl -s http://localhost:18789/health
head -10 ~/.openclaw/SOUL.md
```
Confirm gateway is healthy and SOUL.md now reads Ajna/CSO.

---

## Phase 3: Commander (Claude Code) Setup on MBA

These steps establish Claude Code as a parallel operational tier alongside Ajna.

### 3a: Verify Claude Code Installation
```bash
claude --version
which claude
```
If not installed:
```bash
npm install -g @anthropic-ai/claude-code
```
If npm is not available, check for Homebrew node:
```bash
brew list node 2>/dev/null && npm install -g @anthropic-ai/claude-code
```

### 3b: MCP Configuration

Check if `~/.claude.json` exists:
```bash
test -f ~/.claude.json && echo "EXISTS" || echo "MISSING"
```

If MISSING, create `~/.claude.json` with project-scoped MCP servers appropriate for MBA operations. The MBA needs LOCAL tools only — API-heavy servers (Linear, ClickUp, Jira) stay on Mac mini where Commander-mini handles all API operations.

**Required MCP servers for MBA**:
- **Obsidian** — local vault access (`~/Desktop/syncrescendence`)
- **Filesystem** — repo file operations
- **Playwright or Chrome DevTools** — browser automation (if needed)

**Optional MCP servers** (only if Mac mini services are reachable):
- **Graphiti** — requires Neo4j on Mac mini (needs Tailscale/SSH tunnel or LAN IP)
- **Qdrant** — requires Qdrant on Mac mini (same network requirement)

**NOT needed on MBA** (Commander-mini handles these):
- Linear, ClickUp, Jira, Todoist, Airtable

To get the Mac mini MCP config as a reference:
```bash
# On MBA, if Mac mini is reachable:
ssh macmini "cat ~/.claude.json" 2>/dev/null
# Or copy from the repo if it's checked in
```

### 3c: Skills Installation

Check current skills inventory:
```bash
ls ~/.agents/skills/ 2>/dev/null | wc -l
```

If fewer than 16 skills, install the core set:
```bash
# Core operational skills
npx skills add obra/lace@commit-work -g -y
npx skills add obra/lace@dispatching-parallel-agents -g -y
npx skills add obra/lace@writing-plans -g -y
npx skills add obra/lace@executing-plans -g -y
```

Note: The full skills inventory from Mac mini (226+) is NOT required on MBA. Install only what Commander-MBA needs for its "kinetic micro" role.

### 3d: Hooks Configuration

Check if hooks directory exists:
```bash
ls ~/.claude/hooks/ 2>/dev/null
```

Set up session logging hooks equivalent to Mac mini. These hooks are critical for maintaining the constellation's audit trail:

| Hook | Event | Purpose |
|------|-------|---------|
| session_log.sh | stop | Session metadata to DYN-SESSION_LOG.md |
| ajna_pedigree.sh | stop | Decision lineage to DYN-PEDIGREE_LOG.md |
| create_execution_log.sh | stop | Execution entry to DYN-EXECUTION_STAGING.md |
| pre_compaction.sh | precompact | Warn about uncommitted state |
| intent_compass.sh | userpromptsubmit | Intention signals to DYN-INTENTIONS_QUEUE.md |

If hooks exist on Mac mini, copy them:
```bash
# From Mac mini (if reachable via SSH or shared filesystem)
scp macmini:~/.claude/hooks/*.sh ~/.claude/hooks/
```

Otherwise, create minimal stubs that write to the repo's orchestration state files.

### 3e: tmux/Terminal Configuration

The MBA operates as "kinetic micro" (INT-P015). It does NOT need the full 4-pane ultrawide cockpit. Configure a minimal 2-pane layout:

```
+----------------------------+
| Ajna (OpenClaw Kimi K2.5)  |
|         Pane 1              |
+----------------------------+
| Commander (Claude Code)     |
|         Pane 2              |
+----------------------------+
```

**Terminal**: Use Ghostty if installed (`which ghostty`), otherwise Terminal.app.
**No AeroSpace**: The tiling window manager is Mac mini ultrawide only.
**tmux session name**: `mba-cockpit` (distinct from Mac mini's `cockpit`).

```bash
# Check if tmux session already exists
tmux has-session -t mba-cockpit 2>/dev/null && echo "EXISTS" || echo "CREATE"
```

If creating:
```bash
tmux new-session -d -s mba-cockpit -n ajna
tmux split-window -v -t mba-cockpit:ajna
tmux select-pane -t mba-cockpit:ajna.0
tmux send-keys -t mba-cockpit:ajna.0 'cd ~/Desktop/syncrescendence && openclaw tui --session main' Enter
tmux select-pane -t mba-cockpit:ajna.1
tmux send-keys -t mba-cockpit:ajna.1 'cd ~/Desktop/syncrescendence && claude' Enter
```

---

## Phase 4: Verification Checklist

Run all 8 checks and record PASS/FAIL:

```bash
# 1. Machine identity
echo "=== CHECK 1: Identity ===" && whoami && hostname

# 2. SOUL.md identity
echo "=== CHECK 2: SOUL.md ===" && head -5 ~/.openclaw/SOUL.md

# 3. launchd services
echo "=== CHECK 3: launchd ===" && launchctl list | grep syncrescendence

# 4. Claude Code version
echo "=== CHECK 4: Claude Code ===" && claude --version 2>&1

# 5. Git working tree
echo "=== CHECK 5: Git ===" && git -C ~/Desktop/syncrescendence status --short

# 6. OpenClaw gateway
echo "=== CHECK 6: OpenClaw ===" && curl -s http://localhost:18789/health

# 7. Skills count
echo "=== CHECK 7: Skills ===" && ls ~/.agents/skills/ 2>/dev/null | wc -l

# 8. NVIDIA credential
echo "=== CHECK 8: Credential ===" && grep -c NVIDIA_API_KEY ~/.syncrescendence/.env 2>/dev/null
```

**Pass criteria**:
| # | Check | PASS if |
|---|-------|---------|
| 1 | Machine identity | hostname is MBA (not Mac mini) |
| 2 | SOUL.md identity | First lines mention Ajna/CSO/Strategos |
| 3 | launchd services | At least 2 services listed with non-negative PIDs |
| 4 | Claude Code | Version string returned (any version) |
| 5 | Git working tree | Clean or only expected modifications |
| 6 | OpenClaw gateway | HTTP 200 or JSON health response |
| 7 | Skills | Count >= 4 (core set installed) |
| 8 | NVIDIA credential | Count = 1 |

**Minimum viable**: Checks 1, 2, 4, 5 must PASS. Checks 3, 6, 7, 8 are degraded-but-operational if they fail.

---

## Completion Protocol

### On SUCCESS (6+ checks PASS, all 4 required checks PASS):

1. Write verification results to:
   ```
   -INBOX/commander/00-INBOX0/RESULT-mba-commander-20260211.md
   ```
   Include the full verification table with PASS/FAIL for each check, plus any remediation actions taken.

2. Commit:
   ```bash
   git add -A && git commit -m "feat(SYN-35): MBA Commander setup verified — dual-tier operational"
   ```

3. If SOUL.md was fixed from Psyche to Ajna, note this explicitly in the RESULT file with before/after.

4. Push to ensure Mac mini Commander can see the results:
   ```bash
   git push origin main
   ```

### On PARTIAL (some checks FAIL but required checks PASS):

1. Write results to the same RESULT file path
2. Commit with: `chore(SYN-35): MBA Commander partial setup — N/8 checks passed`
3. List what needs Sovereign intervention (e.g., missing credentials, services down)

### On FAILURE (any required check FAILS):

1. Write diagnostic report to RESULT file
2. Commit with: `fix(SYN-35): MBA Commander setup diagnostics — blocked on X`
3. Do NOT attempt destructive remediation — report back and wait for guidance

---

## Context for Commander-MBA

When you (Commander on MBA) are operational, your role differs from Commander on Mac mini:

- **Mac mini Commander**: Primary operational node. Handles all API-heavy work (Linear, ClickUp, Jira, Todoist, Airtable). Runs the full 4-pane cockpit. Dispatches to Adjudicator and Cartographer.
- **MBA Commander**: Secondary/kinetic node. Handles local-first work (vault operations, ontology editing, strategic analysis support for Ajna). Lightweight 2-pane setup. Does NOT duplicate API operations.

The MBA is the "steering wheel" machine (Ajna = CSO). Commander-MBA supports Ajna's strategic work. Commander-mini is the "rudder" machine (Psyche = CTO) where the heavy operational machinery runs.

**Anti-pattern**: Do NOT try to replicate the full Mac mini infrastructure on MBA. The dual-machine paradigm (INT-P015) is intentional — each machine has a distinct role.
