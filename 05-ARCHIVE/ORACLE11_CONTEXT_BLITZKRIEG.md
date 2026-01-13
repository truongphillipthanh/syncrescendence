# ORACLE 11 COMPREHENSIVE CONTEXT
## Blitzkrieg Deployment Package
**Date**: 2026-01-09
**Status**: ACTIVE DIRECTIVE PACKAGE
**Scope**: Full backlog execution across all available execution instances

---

## EXECUTIVE SUMMARY

Oracle 11 inherits a clean, well-organized repository from Oracle 10. Two major initiatives are complete:
- **PROJ-001**: Transcript Ingestion (43 sources processed, pattern proven)
- **PROJ-011**: Automation Infrastructure (CLAUDE.md, Makefile, coordination.yaml, MCP config)

**Immediate priorities** (all unblocked, ready for parallel execution):
1. **PROJ-002**: IIC Configuration (5 AI accounts across platforms)
2. **PROJ-012**: Multi-CLI Integration (Gemini CLI onboarding)
3. **PROJ-014**: Multi-Account Sync (Claude 2/3 web app utilization)
4. **System Prompt Correction**: 4 files need replacement from authoritative sources
5. **Queue Triage**: 03-QUEUE disposition execution
6. **PROJ-016**: Skills Conversion (new project, scaffolding only)

---

## REPOSITORY STATE

### Directory Structure (7 numbered directories)
```
00-ORCHESTRATION/    Strategic coordination (directives, logs, state, oracle_contexts)
01-CANON/            Verified canonical knowledge (65+ files, PROTECTED)
02-OPERATIONAL/      Functions (20 XML), prompts, model profiles
03-QUEUE/            Pending items by modal (modal1/, modal2/)
04-SOURCES/          Source documents (raw/, processed/)
05-ARCHIVE/          Historical preservation
06-EXEMPLA/          Templates and examples
```

### Ledger State (Ground Truth)
| Ledger | Records | Status |
|--------|---------|--------|
| projects.csv | 11 projects | CURRENT |
| tasks.csv | 47 tasks | CURRENT |
| sources.csv | 184 sources | CURRENT |
| sprints.csv | 1 sprint | CURRENT |

### Project Status Summary
| Project | Status | Priority | Oracle |
|---------|--------|----------|--------|
| PROJ-001 | complete | P1 | Oracle10 |
| PROJ-002 | not_started | P1 | Oracle11 |
| PROJ-003 | not_started | P2 | Oracle11 |
| PROJ-008 | not_started | P2 | TBD |
| PROJ-010 | not_started | P2 | Oracle10+ |
| PROJ-011 | complete | P0 | Oracle10 |
| PROJ-004 | blocked | P2 | Oracle12 |
| PROJ-005 | blocked | P3 | Oracle13 |
| PROJ-006 | blocked | P1 | Oracle14 |
| PROJ-007 | blocked | P3 | Oracle15 |
| PROJ-009 | not_started | P3 | TBD |

---

## CRITICAL FINDINGS

### 1. System Prompt Authoritative Source Discrepancy

**Issue**: Repository's unified-prompt files do NOT match authoritative synthesis files from system_prompts.zip

| File | Authoritative (zip) | Repository | Action |
|------|---------------------|------------|--------|
| Claude prompt | synthesis-claude.md (14.5KB, XML) | Claude-unified-prompt.md (9KB, prose) | REPLACE |
| ChatGPT prompt | synthesis-chatgpt.md (25KB) | ChatGPT-unified-prompt.md (15KB) | REPLACE |
| Gemini prompt | synthesis-gemini.md (2.5KB) | Gemini-unified-prompt.md | REPLACE |
| Grok prompt | synthesis-grok.md (3.5KB) | Grok-unified-prompt.md | REPLACE |

**Evidence**: Synthesis files use established XML architecture (`<system_prompt>`, `<core_identity>`, `<cognitive_profile>` with `<reasoning>` tags). Repository files are markdown prose with different structure.

### 2. Gemini CLI Integration Opportunity

**Gemini CLI** (google-gemini/gemini-cli) is a fully parallel execution environment to Claude Code:
- **GEMINI.md**: Context files (analogous to CLAUDE.md)
- **MCP Support**: Via ~/.gemini/settings.json
- **Free Tier**: 60 requests/min, 1,000 requests/day with personal Google account
- **Model Access**: Gemini 2.5 Pro (1M context), Gemini 3 Pro, Gemini 3 Flash
- **Headless Mode**: `gemini -p "prompt" --output-format json` for scripting

**Key Capability Mapping**:
| Claude Code | Gemini CLI | Notes |
|-------------|------------|-------|
| CLAUDE.md | GEMINI.md | Hierarchical loading from ~/.gemini/ + project root |
| .claude/settings.json | ~/.gemini/settings.json | MCP server configuration |
| worktrees | Same git worktrees | Shared repository access |
| /compact | /chat compress | Token management |

### 3. IIC Architecture Ready for Deployment

Per CANON-31140 and CANON-31141, the Intelligence Integration Constellation requires:

**Five Accounts** (one per chain):
1. **Acumen** → Information Chain (Sensing/Reconnaissance)
2. **Coherence** → Insight Chain (Synthesis/Frameworks)
3. **Efficacy** → Expertise Chain (Operations/Execution)
4. **Mastery** → Knowledge Chain (Teaching/Curriculum)
5. **Transcendence** → Wisdom Chain (Meta-coordination)

**Per-Account Configuration**:
- Dedicated email address
- Platform accounts (YouTube, Twitter/X, Substack, LinkedIn)
- Claude Project with chain-specific system prompt
- Feed curation (Priority Band qualification)
- AI assistance templates

---

## AVAILABLE EXECUTION INSTANCES

### Claude Instances (Confirmed)
| Instance | Location | Status | Zone |
|----------|----------|--------|------|
| Oracle | Claude.ai Web (Account 1) | Active | Strategic synthesis |
| Claude Code 1 | iTerm Alpha | Available | Stream A |
| Claude Code 2 | iTerm Beta | Available | Stream B |
| Claude Code 3 | iTerm Gamma | Available | Stream C |

### Gemini Instance (Available, Untested)
| Instance | Location | Status | Notes |
|----------|----------|--------|-------|
| Gemini CLI | iTerm | Installed, untested | Requires validation |

### Idle Accounts (Potential)
- Claude.ai Account 2 (web app)
- Claude.ai Account 3 (web app)
- ChatGPT (web app + potential Codex)

---

## BLITZKRIEG EXECUTION STREAMS

### Stream A: IIC Foundation (Claude Code 1)
**Directive**: DIRECTIVE-042A
**Scope**: Acumen + Coherence IIC configuration
**Deliverables**:
- IIC-Acumen-config.md (complete account specification)
- IIC-Coherence-config.md (complete account specification)
- IIC-shared-protocols.md (cross-IIC communication standards)

### Stream B: Multi-CLI Integration (Claude Code 2)
**Directive**: DIRECTIVE-042B
**Scope**: Gemini CLI onboarding + system prompt correction
**Deliverables**:
- GEMINI.md (Syncrescendence-adapted context file)
- gemini-settings.json (MCP configuration template)
- MULTI_CLI_COORDINATION.md (operational protocol)
- Corrected unified-prompt files in 02-OPERATIONAL/prompts/unified/

### Stream C: Operational Hygiene (Claude Code 3)
**Directive**: DIRECTIVE-042C
**Scope**: Queue triage + ledger updates + new project scaffolding
**Deliverables**:
- Queue disposition execution (move/merge files)
- Updated tasks.csv with new tasks
- Updated projects.csv with PROJ-016 (Skills Conversion)
- Updated DYN-BACKLOG.md

### Stream D: Gemini Validation (Gemini CLI)
**Directive**: DIRECTIVE-042D (test directive)
**Scope**: Validate Gemini CLI operational capability
**Deliverables**:
- Repository structure verification
- GEMINI.md context loading confirmation
- Basic file operations test
- Comparative capability assessment

---

## SUCCESS METRICS

| Metric | Target | Measurement |
|--------|--------|-------------|
| IIC accounts specified | ≥2 complete | Config files created |
| System prompts corrected | 4 files | diff verification |
| Gemini CLI validated | Yes/No | Test directive completion |
| Queue triage complete | 7 files moved | Directory state |
| PROJ-016 created | 1 project | projects.csv entry |
| New tasks created | ≥8 tasks | tasks.csv entries |
| PROJ-002 status | IN_PROGRESS | Ledger updated |

---

## CONSTITUTIONAL REMINDERS

### Absolute Rules
1. **FLAT PRINCIPLE**: No subdirectories. Use prefixes.
2. **DISTILLATION ≠ ORGANIZATION**: Metabolism = READ → EXTRACT → COMPRESS → DELETE
3. **LEDGER GROUND TRUTH**: tasks.csv is authoritative. Verify, don't trust reports.

### Operational Rules
1. All outputs to /mnt/user-data/outputs/ for download
2. Verify before claiming completion
3. Commit frequently with semantic prefixes

### 18-Lens Evaluation Reminder
Critical lenses for this Blitzkrieg:
- **Lens #2 (Bitter Lesson)**: Does this scale with compute? (IIC + multi-CLI = yes)
- **Lens #9 (Agentify)**: Can this self-activate? (Skills, MCP = yes)
- **Lens #12 (Industrial Engineering)**: Reduces Principal bottleneck? (Parallel execution = yes)
- **Lens #14 (Permaculture)**: Self-sustaining? (Automation infrastructure = yes)

---

## HANDOFF PROTOCOL

Each execution instance receives:
1. This Oracle Context artifact
2. Specific directive (DIRECTIVE-042A/B/C/D)
3. Access to shared repository

Each instance produces:
1. Deliverables to /mnt/user-data/outputs/
2. Execution log per standard template
3. Ledger updates (append-only for shared CSVs)

Principal action:
1. Download all outputs from all streams
2. Integrate to repository
3. Commit with semantic messages
4. Push to remote

---

*This context provides complete strategic orientation for all execution instances. Each directive below provides tactical specifics.*
