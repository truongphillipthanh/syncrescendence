# Skills Pipeline Map
## Capability-to-Stage Mapping for the Syncrescendence Constellation

**Document Type**: REFERENCE (Living Document)
**Last Updated**: 2026-02-12
**Source**: Deep Audit — Skills Pipeline Mapping | DAG Upgrade — Skills Architecture Overhaul

---

## Pipeline Stages

```
ORIENT → RESEARCH → PLAN → EXECUTE → VERIFY → DISPATCH → COMMIT → REVIEW → MEMORY → OBSERVE
```

### 1. ORIENT (Situation Awareness)
| Capability | Platform | Type |
|-----------|----------|------|
| /claresce orient phase | Claude Code | skill |
| intent_compass.sh hook | Claude Code | hook |
| session_log.sh hook | Claude Code | hook |
| git status | All CLI | built-in |
| inbox triage | All CLI | protocol |

### 2. RESEARCH (Intelligence Gathering)
| Capability | Platform | Type |
|-----------|----------|------|
| web-to-markdown | Claude Code | skill |
| last30days | Claude Code | skill |
| google-ai-mode | Claude Code | skill |
| Obsidian MCP (11 tools) | Claude Code | MCP |
| Graphiti MCP (9 tools) | Claude Code | MCP |
| Qdrant MCP | Claude Code | MCP |
| qmd BM25 search | OpenClaw | tool |
| Cartographer (1M ctx) | Gemini CLI | agent |
| Chrome DevTools MCP (18+ tools) | Claude Code | MCP |
| Playwright MCP (20+ tools) | Claude Code | MCP |
| gemini-obsidian | Gemini CLI | extension |

### 3. PLAN (Strategy & Design)
| Capability | Platform | Type |
|-----------|----------|------|
| writing-plans | Claude Code | skill |
| planning-with-files | Claude Code | skill |
| Plan Mode | Claude Code | built-in |
| mermaid-diagrams | Claude Code | skill |
| Conductor | Gemini CLI | extension |
| Plan Commands | Gemini CLI | extension |

### 4. EXECUTE (Implementation)
| Capability | Platform | Type |
|-----------|----------|------|
| executing-plans | Claude Code | skill |
| subagent-driven-development | Claude Code | skill |
| dispatching-parallel-agents | Claude Code | skill |
| tmux | Claude Code | skill |
| using-git-worktrees | Claude Code | skill |
| systematic-debugging | Claude Code | skill |
| Agent Teams (Claude Code native) | Claude Code | built-in |
| Superpowers (47 sub-skills) | Claude Code | skill |
| Context Engineering Kit (61 sub-skills) | Claude Code | skill |
| AI Research Skills (79 sub-skills) | Claude Code | skill |
| Trail of Bits Security (47 sub-skills) | Claude Code | skill |
| gh-fix-ci | Codex CLI | skill |
| gh-address-comments | Codex CLI | skill |
| yeet | Codex CLI | skill |

### 5. VERIFY (Quality Assurance)
| Capability | Platform | Type |
|-----------|----------|------|
| verification-before-completion | Claude Code | skill |
| skill-judge | Claude Code | skill |
| security-best-practices | Codex CLI | skill |
| security-threat-model | Codex CLI | skill |
| security-ownership-map | Codex CLI | skill |
| code-review | Gemini CLI | extension |
| security (Google official) | Gemini CLI | extension |
| corpus-health (launchd) | System | service |
| watchdog (launchd) | System | service |

### 6. DISPATCH (Task Routing)
| Capability | Platform | Type |
|-----------|----------|------|
| dispatch.sh | All CLI | script |
| agents//inbox filesystem kanban | All | protocol |
| Ajna/CSO dispatch optimization | OpenClaw | role |
| Linear MCP (33 tools) | Claude Code | MCP |
| ClickUp MCP | Claude Code | MCP |

### 7. COMMIT (Persistence)
| Capability | Platform | Type |
|-----------|----------|------|
| commit-work | Claude Code | skill |
| changelog-generator | Codex CLI | skill |
| session-handoff | Claude Code | skill |
| create_execution_log.sh | Claude Code | hook |
| ajna_pedigree.sh | Claude Code | hook |

### 8. REVIEW (Post-Execution)
| Capability | Platform | Type |
|-----------|----------|------|
| claude-session-review (launchd) | System | cron |
| claude-linear-check (launchd) | System | cron |
| claude-corpus-insight (launchd) | System | cron |

### 9. MEMORY (Knowledge Management)
| Capability | Platform | Type |
|-----------|----------|------|
| Graphiti knowledge graph | Shared | service |
| Mem0 auto-recall/capture | OpenClaw | plugin |
| Qdrant vector store | Claude Code | MCP |
| qmd BM25 local search | OpenClaw | tool |
| MEMORY.md | Claude Code | built-in |
| conversation-memory | Claude Code | skill |
| memory-systems | Claude Code | skill |
| ensue (knowledge tree) | Claude Code | skill |

### 10. OBSERVE (Monitoring)
| Capability | Platform | Type |
|-----------|----------|------|
| Doom Emacs (observation layer) | Standalone | dormant |
| watchdog (launchd, 5min) | System | service |
| corpus-health (launchd, 6h) | System | service |
| crabwalk (companion monitor) | OpenClaw | tool |
| 4-tier self-healing | System | architecture |

---

## Coverage Summary

| Stage | Total Capabilities | Strongest Platform |
|-------|-------------------|-------------------|
| ORIENT | 5 | Claude Code |
| RESEARCH | 11 | Claude Code (MCP) |
| PLAN | 6 | Claude Code + Gemini CLI |
| EXECUTE | 14+ | Claude Code (skills + agents) |
| VERIFY | 9 | Codex CLI (security) + Gemini CLI |
| DISPATCH | 5 | Cross-platform |
| COMMIT | 5 | Claude Code |
| REVIEW | 3 | System (claudecron) |
| MEMORY | 8 | Shared infrastructure |
| OBSERVE | 5 | System services |

---

## Skill DAG — Directed Edges

| Source Skill | → | Target Skill(s) | Stage Transition | Notes |
|---|---|---|---|---|
| claresce | → | plan, execute, dispatch.sh | ORIENT → PLAN/EXECUTE/DISPATCH | Primary orientation fan-out |
| last30days / lastweek / lastday | → | plan, claresce | RESEARCH → PLAN/ORIENT | Intelligence feeds into planning or re-orientation |
| plan | → | execute, blitzkrieg_teams | PLAN → EXECUTE | Strategy materializes into implementation |
| mermaid-diagrams | → | commit-work | PLAN → COMMIT | Diagrams are committed as artifacts |
| execute / blitzkrieg | → | verification-before-completion | EXECUTE → VERIFY | All execution must pass verification gate |
| verification | → | commit-work | VERIFY → COMMIT | Verified work persists |
| skill-judge | → | update_agent_memory | VERIFY → MEMORY | Skill quality assessments update memory |
| commit-work | → | session_log.sh hook, pedigree hook | COMMIT → (hooks) | Automated metadata capture on commit |
| session-handoff | → | claresce (next session) | COMMIT → ORIENT | Handoff re-enters orientation in next session |
| update_agent_memory | → | watchdog sync | MEMORY → OBSERVE | Memory changes propagate via watchdog |
| update_universal_ledger | → | corpus-health | MEMORY → OBSERVE | Ledger changes trigger corpus health check |

---

## Named Skill Chains (Pre-defined Sequences)

### 1. INTELLIGENCE_REFRESH

**Sequence**: `lastweek` → `claresce` → `update_agent_memory` → `dispatch`

- **Purpose**: Gather ecosystem intelligence and propagate to agents
- **Entry Point**: `lastweek` (RESEARCH stage)
- **Terminal Node**: `dispatch` (DISPATCH stage — routes refreshed intelligence to relevant agents)

### 2. SOURCE_INTAKE

**Sequence**: `readize | listenize | audize` → `integrate` → `commit-work` → `update_universal_ledger`

- **Purpose**: Ingest source material into the knowledge corpus
- **Entry Point**: `readize | listenize | audize` (RESEARCH stage — media-specific intake)
- **Terminal Node**: `update_universal_ledger` (MEMORY stage — ledger records the new corpus entry)

### 3. TASK_EXECUTION

**Sequence**: `triage` → `claresce` → `plan` → `execute` → `verify` → `commit-work` → `session-handoff`

- **Purpose**: Standard operational loop for directive processing
- **Entry Point**: `triage` (DISPATCH stage — incoming task classification)
- **Terminal Node**: `session-handoff` (COMMIT stage — session boundary with continuation state)

### 4. SKILL_CREATION

**Sequence**: `find-skills` → `skillforge` → `skill-judge` → `commit-work` → `watchdog sync`

- **Purpose**: Discover, create, validate, and deploy new skills
- **Entry Point**: `find-skills` (RESEARCH stage — capability gap discovery)
- **Terminal Node**: `watchdog sync` (OBSERVE stage — deployed skill enters monitoring)

### 5. SECURITY_AUDIT

**Sequence**: `threat-modeling` → `semgrep | codeql` → `sarif-parsing` → `claresce` → `commit-work`

- **Purpose**: Comprehensive security analysis pipeline
- **Entry Point**: `threat-modeling` (VERIFY stage — threat surface enumeration)
- **Terminal Node**: `commit-work` (COMMIT stage — security findings persisted as artifacts)

---

## Entry Points and Terminal Nodes

### Entry Points
Skills that begin chains (no upstream dependency within the DAG):

| Entry Skill | Chain(s) | Stage |
|---|---|---|
| claresce | ORIENT entry, TASK_EXECUTION (via triage) | ORIENT |
| triage | TASK_EXECUTION entry | DISPATCH |
| lastweek / lastday / last30days | INTELLIGENCE_REFRESH entry | RESEARCH |
| find-skills | SKILL_CREATION entry | RESEARCH |
| threat-modeling | SECURITY_AUDIT entry | VERIFY |
| readize / listenize / audize | SOURCE_INTAKE entry | RESEARCH |

### Terminal Nodes
Skills that end chains (produce final artifacts, no downstream skill dependency):

| Terminal Skill | Chain(s) | Stage | Artifact Type |
|---|---|---|---|
| commit-work | SECURITY_AUDIT, SOURCE_INTAKE, TASK_EXECUTION | COMMIT | Git commits, persisted files |
| session-handoff | TASK_EXECUTION | COMMIT | Continuation state for next session |
| update_universal_ledger | SOURCE_INTAKE | MEMORY | Ledger CSV entries |
| update_agent_memory | INTELLIGENCE_REFRESH | MEMORY | Agent MEMORY.md updates |

---

## Identified Gaps
- **Deployment/Ops**: No skills for deployment, CI/CD, containerization
- **Database**: No database management skills
- **Frontend**: No UI/UX skills (not currently needed)
- **Notification**: No desktop notification system for agent completion
- **Anti-Shelfware**: Every active skill should appear in at least one named chain or have a non-empty wiring (hook, agent-loop, slash-command). Skills without wiring after 30-day review → dormant.

---

*Generated from Deep Audit 2026-02-09 | Maintained as living reference*
