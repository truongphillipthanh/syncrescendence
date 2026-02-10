# Skills Pipeline Map
## Capability-to-Stage Mapping for the Syncrescendence Constellation

**Document Type**: REFERENCE (Living Document)
**Last Updated**: 2026-02-09
**Source**: Deep Audit — Skills Pipeline Mapping

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
| -INBOX/ filesystem kanban | All | protocol |
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

## Identified Gaps
- **Deployment/Ops**: No skills for deployment, CI/CD, containerization
- **Database**: No database management skills
- **Frontend**: No UI/UX skills (not currently needed)
- **Notification**: No desktop notification system for agent completion

---

*Generated from Deep Audit 2026-02-09 | Maintained as living reference*
