---
kind: clarescence
id: CLARESCENCE-2026-02-11-mba-commander-init
title: "MBA Commander Initialization: MCP + Cockpit + Memory"
date: 2026-02-11
status: executed
fidelity: tactical
agent: commander
passes: 3
decision_atoms: 4
linear: SYN-35
predecessors:
  - CLARESCENCE-2026-02-09-mba-ajna-setup.md
  - RESULT-mba-commander-20260211.md
---

# CLARESCENCE: MBA Commander Initialization

**Date**: 2026-02-11
**Fidelity**: Tactical (Passes 0–3)
**Agent**: Commander (Mac mini, dispatching to MBA)
**IntentionLink**: INT-1504, INT-P015, SYN-35

---

## PASS 0: Orient & Situate

### Ground Truth
- Machine: M1-Mac-mini.local (dispatching, not target)
- Target: Lisas-MacBook-Air (MBA, user: lisa)
- Fingerprint: `cc4ebed`
- Working tree: 3 modified files (cockpit.sh, current.yaml, ledger)
- Commander inbox: empty (all processed)

### Prior Work
- CLARESCENCE-2026-02-09-mba-ajna-setup: 10-pass strategic clarescence for Ajna/OpenClaw on MBA. Status: EXECUTED.
- RESULT-mba-commander-20260211: Claude Code installed (8/8 PASS). Missing: MCP, cockpit, memory.

### Tier
- **T1a** (repo-operational). Affects SYN-35 (MBA setup).

### Dependencies
- Blocks: INT-1603 (JIT HighCommand), INT-P015 (dual-machine paradigm)
- Blocked by: Nothing (Ajna setup complete, Commander installed)

### Affected Agents
- Commander (MBA instance)
- Ajna (co-resident on MBA)

---

## PASS 1: Triumvirate Calibration

- **Destination**: INT-1504 (cascade deployment Mac mini → MBA), INT-P015 (dual-machine: Mac mini=macro, MBA=micro)
- **Current state**: Commander installed on MBA but unconfigured. No MCP servers, no cockpit, no persistent memory. Essentially a Claude Code binary with skills and hooks but no integration layer.
- **Fit verdict**: CLOSES THE GAP. MBA becomes fully dual-engine (Ajna+Commander). This is the last step before SYN-35 can be marked Done.

---

## PASS 2: Lens Sweep (abbreviated for Tactical)

| # | Lens | P/F | Note |
|---|------|-----|------|
| 1 | Sovereignty | PASS | MBA retains full autonomy, no Mac mini dependency for core ops |
| 2 | Portability | PASS | Scripts are in repo, sync via git |
| 3 | Durability | PASS | Config persists across sessions |
| 4 | Reversibility | PASS | Delete MCP entries from ~/.claude.json to revert |
| 5 | Atomicity | PASS | Single init script, single commit |
| 6 | Verifiability | PASS | Script has 6-step verification |
| 7 | Delegability | PASS | Sovereign runs script on MBA; no CLI ambiguity |
| 8 | Composability | PASS | mba-cockpit.sh parallels cockpit.sh pattern |
| 9 | Observability | PASS | Script outputs status for every step |
| 10 | Token economy | PASS | Lightweight MCP set (5 servers vs Mac mini's 12) |
| 11 | Energy sustainability | PASS | One-time script, no ongoing maintenance |
| 12 | Coupling risk | PASS | Per-machine config in ~/.claude.json, not shared |
| 13 | Semantic clarity | PASS | "mba-cockpit" vs "cockpit" avoids confusion |
| 14 | Canon alignment | N/A | No CANON changes |
| 15 | Tier coherence | PASS | T1a work, SYN-35 tracked |
| 16 | Agent compatibility | PASS | Ajna+Commander co-resident, no port conflicts |
| 17 | Automation potential | PASS | Init script is fully automatable |
| 18 | Narrative fit | PASS | MBA = kinetic cockpit, micro-ops |

**Score: 17/17 (1 N/A) — PASS**

---

## PASS 3: CANON Coherence

- COCKPIT.md correctly lists Ajna as MBA remote. After this init, Commander also operates on MBA.
- No CANON contradiction — COCKPIT.md describes the Mac mini cockpit; MBA has its own variant (mba-cockpit.sh).
- MBA Commander is a **deployment cascade** (INT-1504), not a replacement. Mac mini Commander remains the primary instance.

---

## Decision Atoms

| ID | Decision | Surface | Reversibility |
|----|----------|---------|---------------|
| DA-01 | MBA MCP = 5 servers (obsidian, filesystem, gemini-mcp, linear, clickup) | ~/.claude.json on MBA | Delete mcpServers key |
| DA-02 | No Graphiti/Qdrant on MBA (Docker services stay on Mac mini) | mba-commander-init.sh | Add servers later if Docker deployed |
| DA-03 | 2-pane cockpit (Ajna left, Commander right) | mba-cockpit.sh | Kill session, modify script |
| DA-04 | MBA Commander memory in ~/.claude/projects/-Users-lisa-Desktop-syncrescendence/memory/ | MEMORY.md | Delete file |

---

## Artifacts Produced

1. `00-ORCHESTRATION/scripts/mba-cockpit.sh` — 2-pane tmux cockpit
2. `00-ORCHESTRATION/scripts/mba-commander-init.sh` — one-shot MCP + config setup
3. This clarescence record

---

## Sovereign Action Required

On MBA, run:
```bash
cd ~/Desktop/syncrescendence
git pull
bash 00-ORCHESTRATION/scripts/mba-commander-init.sh
source ~/.zshrc
mba-cockpit --launch
```

---

## Falsifier

If MBA Commander's ~/.claude.json already has project-scoped MCP servers under `/Users/lisa/Desktop/syncrescendence`, the init script will overwrite them. Check first with:
```bash
python3 -c "import json; c=json.load(open('$HOME/.claude.json')); print(json.dumps(c.get('projects',{}).get('$HOME/Desktop/syncrescendence',{}).get('mcpServers',{}), indent=2))"
```

**Confidence**: High (90%). Commander is installed and verified. Init script is straightforward JSON manipulation.

---

**End of Clarescence**
