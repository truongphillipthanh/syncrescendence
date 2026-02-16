# Claude Code Guide Validation and Upgrade: Comprehensive Research Report

This five-phase research program validates the baseline Claude Code Definitive Guide against first-party official documentation, revealing **12 claims requiring correction**, **7 claims fully verified**, and **9 high-priority gaps** where official documentation is silent. The most significant finding: extended thinking triggers ("ultrathink," etc.) underwent an **architectural change in January 2026** that makes previous guidance obsolete—keywords no longer allocate tokens, as thinking is now enabled by default at maximum budget.

---

## A. Verified Claude Code Reference: Architecture, Configuration, and Interaction

### Architecture Map (Validated January 2026)

Claude Code operates as an **agentic coding tool** executing in three primary contexts: terminal CLI, VS Code extension (beta), and web interface (claude.ai/code). The architecture comprises these verified components:

| Component | Official Description | Boundary Surface |
|-----------|---------------------|------------------|
| **CLI Core** | Primary terminal interface, npm-distributed | Local execution, API calls to Anthropic |
| **Agent SDK** | Extensible framework for custom agents | Programmatic interface, TypeScript/Python |
| **MCP Gateway** | Model Context Protocol server integration | Stdio/HTTP/SSE transports, tool discovery |
| **Checkpoint System** | Automatic code state preservation | Git-like rewind, OS-level storage |
| **Sandbox** | Bubblewrap (Linux) / Seatbelt (macOS) isolation | Network, filesystem restrictions |

**Dataflow (verified):** User prompt → System prompt (~10% context) + CLAUDE.md memory → API inference → Tool execution (Bash/Edit/Read/Write/WebFetch/MCP) → Permission check → Result display → Optional compaction.

### Configuration Surface Map (Validated)

**CLAUDE.md Hierarchy (REFINED from baseline claim):**

The baseline guide claimed a **5-level hierarchy** (Enterprise → User → Project → Modular rules → Local). Official documentation confirms a **4-level hierarchy** with different precedence:

```
1. ~/.claude/CLAUDE.md (user-level, applies globally)
2. Parent directories (recursive upward from cwd to /)
3. ./CLAUDE.md or ./.claude/CLAUDE.md (working directory)
4. Child directories (loaded ON-DEMAND when working in subtrees)
```

**Critical correction:** Files load **upward** from working directory, NOT downward. Child directory CLAUDE.md files are loaded on-demand, not at startup.

**Settings.json Precedence (VERIFIED):**
```
Managed (highest) → Local → Project → User (lowest)
```

Official documentation states programmatic options "always override filesystem settings."

| Config File | Location | Committed to Git | Purpose |
|-------------|----------|------------------|---------|
| settings.json | ~/.claude/ | N/A (user-level) | Global user preferences |
| settings.json | .claude/ | Yes | Project defaults |
| settings.local.json | .claude/ | No (.gitignore) | Local overrides, secrets |
| managed-settings.json | /etc/claude-code/ | Enterprise policy | Cannot be overridden |

**Permissions Schema (VERIFIED):**
```json
{
  "permissions": {
    "allow": ["Bash(npm run:*)", "Read(~/.zshrc)", "mcp__github__*"],
    "deny": ["Bash(curl:*)", "Read(./.env)", "Read(./secrets/**)"],
    "ask": ["Bash(git push:*)"]
  }
}
```
Rule evaluation order: Deny rules checked first → Allow rules → Ask rules → Unmatched = approval required.

**Hooks System (VERIFIED):**
| Hook Event | Trigger Point | Supports Matchers |
|------------|---------------|-------------------|
| PreToolUse | Before tool execution | Yes |
| PostToolUse | After tool completion | Yes |
| PermissionRequest | Permission dialog shown | Yes |
| SessionStart | Session begins | Yes (source: startup/resume/clear) |
| Stop | Main agent finishes | No |
| SubagentStop | Subagent completes | No |
| PreCompact | Before compaction | Yes (trigger: manual/auto) |
| Notification | Notification sent | Yes |
| UserPromptSubmit | User submits prompt | No |
| Setup | --init flags | No |

### Interaction Paradigm Map (Validated)

**Plan Mode (VERIFIED with clarification):**
- Activation: **Shift+Tab cycles modes** (Normal → Auto-Accept → Plan)
- Alternative: `/plan` command directly enables Plan Mode
- Behavior: Claude describes intended actions and waits for approval before modifications
- Official characterization: "Perfect for exploring codebases, planning complex changes, or reviewing code safely"

**Extended Thinking Triggers (MAJOR CORRECTION):**

The baseline guide claims specific token allocations: "think" (~4K), "think hard" (~10K), "ultrathink" (~32K). This is **OUTDATED**.

| Time Period | Behavior | Official Source |
|-------------|----------|-----------------|
| **Pre-2026 (v1.x)** | Keywords mapped directly to token budgets | Best Practices blog (April 2025) |
| **Post-January 2026 (v2.x)** | Extended thinking **enabled by default at 31,999 tokens**; keywords are cosmetic | Common Workflows docs |

**Current mechanism:** Thinking budget controlled exclusively by:
1. Tab toggle (on/off)
2. `MAX_THINKING_TOKENS` environment variable
3. API `thinking.budget_tokens` parameter

**Context Window Behavior (PARTIALLY VERIFIED):**
- **200K context window** with ~10% consumed by system prompt, tools, memory
- **Auto-compaction** triggers at ~98% context usage (bug fix noted: previously triggered incorrectly at ~65%)
- **Compaction is lossy** (summarization-based), but algorithms are NOT documented
- `/compact` accepts custom instructions: "/compact Focus on code samples" tells Claude what to preserve

**UNVERIFIED Claims from Baseline:**
- "Quality begins to decline well before 200K limit" — NOT officially documented
- "~150-200 instructions reliably; system prompt uses ~50" — NO official documentation found

---

## B. Community Reality Section: Patterns, Antipatterns, and Reconciliation

### Practice vs. Spec Matrix

| Area | Official Spec | Community Practice | Divergence Level |
|------|--------------|-------------------|------------------|
| Thinking triggers | Auto-enabled, keywords cosmetic | Still using "ultrathink" | HIGH |
| Plan Mode | Optional feature | Treated as essential for complex work | MEDIUM |
| CLAUDE.md size | "Keep concise" | 13-25KB for serious repos | MEDIUM |
| Permissions | Conservative defaults | Two camps: auto-accept vs. careful | LOW |
| Context management | Auto-compact available | Manual control + `/clear` preferred | MEDIUM |
| Custom subagents | Recommended for context isolation | Criticized for "gatekeeping context" | HIGH |
| `/compact` command | Available for summarization | Avoided as "opaque, error-prone" | HIGH |

### Verified Effective Patterns (3+ Independent Practitioners)

**1. Handoff Document Pattern:**
Before hitting context limits, practitioners ask Claude to write a structured handoff document:
> "Put the rest of the plan in folder X. Explain what you have tried, what worked, what didn't work, so the next agent with fresh context can finish it."

This pattern appears in Boris Cherny's workflow, Shrivu Shankar's enterprise guide, and ykdojo's tips repository.

**2. Git Worktree Isolation:**
Multiple practitioners (Steinberger, Nx blog, community guides) use worktrees for parallel Claude instances:
```
project/
├── main/           ← main checkout
├── feature-auth/   ← worktree (Claude instance 1)
├── bugfix-api/     ← worktree (Claude instance 2)
```
Each agent operates in isolated directory with shared Git history.

**3. Block-at-Commit, Not Block-at-Write:**
Enterprise users (Shrivu Shankar) prefer PreToolUse hooks on `git commit` rather than `Edit`, allowing agents to complete full plans before validation runs.

**4. "Constitution" CLAUDE.md Structure:**
Effective CLAUDE.md files observed across professional repositories include:
- Bash commands with exact syntax
- Code style directives with good/bad examples (✅/❌)
- Workflow rules ("typecheck when done", "prefer single tests")
- Anti-patterns section ("never uncomment tests to make them pass")
- Gotchas and project-specific warnings

### Documented Antipatterns (Recurring Failures)

**1. "Penelope Problem"** (Zvi Mowshowitz):
Claude gets partway through good work, then announces "I'm thinking about this all wrong!" and deletes progress.

**2. "Hydra Problem":**
Fixing one bug creates two more, especially in unfamiliar codebases.

**3. "Mock-Happy Behavior":**
Claude defaults to mocking tests instead of fixing underlying issues. Practitioners interrupt when Claude says "I'll update test to use mocks."

**4. Context Exhaustion:**
Trusting Claude too much as codebase grows; not clearing context frequently enough.

**5. uv Package Manager Confusion:**
Multiple reports that Claude "CANNOT for the life of it figure out how to use uv correctly."

### Reconciliation Proposals

| Divergence | Why It Exists | Proposed Reconciliation |
|------------|--------------|------------------------|
| Large CLAUDE.md files | Complex projects need comprehensive context | Official guidance should acknowledge "concise" varies by project complexity; provide tiered examples |
| Ultrathink keywords | Outdated blog post; community muscle memory | Update Best Practices blog with deprecation notice; add CLI warning when keyword detected |
| /compact avoidance | Users report lossy, unpredictable results | Document compaction algorithm; provide "what gets preserved" guidance |
| Custom subagent criticism | "Gatekeeps context" from main agent | Document Master-Clone pattern as alternative to Lead-Specialist |
| YOLO mode on bare metal | Container friction too high | Improve backup/snapshot integration; document hourly Arq snapshot pattern |

---

## C. Novel Research Paths Section (≥7 Hypotheses)

### Research Path 1: Speculative Multi-Action Execution

**Hypothesis:** If we implement speculative execution predicting likely next tool calls using faster models (Haiku), we achieve **30%+ latency reduction** while maintaining lossless output quality.

**Evidence basis:** arXiv paper "Speculative Actions" (2510.04371) reports 40-55% speculation hit rates on agentic workflows.

**Experiment:** Instrument Claude Code sessions measuring sequential API call latency; implement speculation layer; measure wall-clock time across refactoring, debugging, feature implementation tasks.

**Expected tradeoffs:** Additional inference cost for speculative calls; wasted computation on speculation misses; requires safety envelopes for idempotent operations.

**Guide sections upgraded:** Performance optimization, Cost management, Autonomous workflows.

### Research Path 2: State Machine Formalization for Recovery

**Hypothesis:** If we model Claude Code workflows as explicit state machines (exploration → planning → coding → testing → committing) with checkpoint/recovery paths, we reduce **task abandonment by 40%** and enable reliable "resume from failure."

**Evidence basis:** AutoRocq agentic proving system and VeriMaAS multi-agent verification frameworks demonstrate formal state representation improves reliability.

**Experiment:** Annotate 1000+ sessions with state transitions and failure points; build state machine model; implement checkpoint/restore; measure recovery success vs. current "start over" approach.

**Expected tradeoffs:** State serialization overhead; complexity with non-deterministic outputs; potential context inflation.

**Guide sections upgraded:** Session management, Long-running tasks, Error recovery.

### Research Path 3: AST-Based Hallucination Detection

**Hypothesis:** A deterministic AST post-processing layer validating generated code against library signature Knowledge Bases can detect **100% of API-level hallucinations** and auto-correct **77%+** without additional LLM calls.

**Evidence basis:** arXiv "Detecting and Correcting Hallucinations in LLM-Generated Code" (2601.19106) demonstrates AST-based detection taxonomy with 19 intent-conflicting types identified.

**Experiment:** Build Knowledge Base for top 50 Python packages; run detection on 500+ generated samples; measure precision/recall vs. manual annotation.

**Expected tradeoffs:** KB maintenance for evolving libraries; cannot detect semantic/logic hallucinations; language-specific parsers required.

**Guide sections upgraded:** Code quality verification, Trust calibration, Hooks for validation.

### Research Path 4: Hierarchical Context Summarization

**Hypothesis:** Hierarchical summarization preserving critical information at attention-favored positions (start/end) while compressing low-value content maintains **>90% task performance at 2x effective context utilization**.

**Evidence basis:** NoLiMa benchmark shows 11/12 models dropped below 50% performance at 32K tokens; "Lost-in-the-middle" effect confirmed across studies.

**Experiment:** Implement importance scoring for context segments; apply progressive summarization; track "context health" metrics; A/B test on real sessions.

**Expected tradeoffs:** Information loss from summarization; scoring overhead; risk of discarding unexpectedly relevant context.

**Guide sections upgraded:** Context management, Compaction strategies, Session duration optimization.

### Research Path 5: Git Worktree-Native Parallel Orchestration

**Hypothesis:** Native git worktree integration with automated workspace isolation enables **3-5x parallel task throughput** while eliminating inter-agent file conflicts.

**Evidence basis:** Nx blog, Steinberger workflow documentation, and community guides demonstrate successful parallel patterns using manual worktree setup.

**Experiment:** Implement worktree creation/management commands; measure parallel throughput vs. sequential; track merge conflict rates.

**Expected tradeoffs:** Disk space overhead; coordination complexity for overlapping changes; divergent branches requiring reconciliation.

**Guide sections upgraded:** Multi-agent patterns, Parallel development, Branch discipline.

### Research Path 6: TiCoder Test-as-Specification Verification

**Hypothesis:** Generating and validating test cases before code generation improves **code correctness by 15%+** while reducing cognitive load during evaluation.

**Evidence basis:** UPenn TiCoder study demonstrates users with test-first workflow significantly more likely to correctly evaluate AI code with no increase in completion time.

**Experiment:** Implement test generation as first-class feature; user study comparing test-first vs. code-first; track correctness on private test suites.

**Expected tradeoffs:** Additional inference cost; test execution overhead; may slow trivial tasks.

**Guide sections upgraded:** TDD workflows, Verification loops, Code review integration.

### Research Path 7: Multi-Agent Maker-Checker Pattern

**Hypothesis:** Dual-agent workflow where one Claude generates code and another validates/critiques catches **30%+ more defects** before human review while maintaining generation speed.

**Evidence basis:** Microsoft Azure AI Agent Design Patterns documents maker-checker as production-proven pattern; Semantic Kernel orchestration demonstrates implementation.

**Experiment:** Implement dual-agent workflow with separate prompts; compare defect detection vs. single-agent; measure token cost vs. quality improvement.

**Expected tradeoffs:** 2x+ token cost; potential infinite loops; latency increase from multi-turn verification.

**Guide sections upgraded:** Code review, Quality gates, Multi-agent orchestration.

### Research Path 8: Secrets Exposure Prevention Pipeline

**Hypothesis:** Mandatory secrets scanning, prompt sanitization, and output filtering reduce **secrets exposure by 90%** without impacting productivity.

**Evidence basis:** Apiiro research documents 40% increase in secrets exposure with AI assistants; 39 million leaked secrets on GitHub in 2024.

**Experiment:** Integrate trufflehog/gitleaks scanning; track blocked patterns; measure false positive rates and workflow impact.

**Expected tradeoffs:** Scanning latency; false positives; pattern database maintenance.

**Guide sections upgraded:** Security hardening, Permissions configuration, Enterprise deployment.

### Research Path 9: Prompt Drift Regression Framework

**Hypothesis:** Continuous regression testing with versioned prompts, golden datasets, and automated quality gates catches performance degradation **within 24 hours** of model updates while reducing eval maintenance by **60%**.

**Evidence basis:** Anthropic "Demystifying Evals" emphasizes teams without evals get "bogged down in reactive loops"; capability evals with high pass rates can "graduate" to regression suites.

**Experiment:** Build regression suite from production traces; implement CI/CD integration; track eval coverage and time-to-regression-detection.

**Expected tradeoffs:** Eval maintenance overhead; LLM-as-judge non-determinism; cost of comprehensive suites.

**Guide sections upgraded:** Prompt engineering, Model upgrade handling, Quality assurance.

### Research Path 10: Cognitive Load-Adaptive Role Configuration

**Hypothesis:** Dynamically adjusting AI autonomy based on developer experience and task complexity optimizes cognitive load distribution and increases code quality.

**Evidence basis:** Springer "Impact of AI-assisted Pair Programming" shows effectiveness depends on task complexity × developer experience interaction.

**Experiment:** Implement role-switching commands; track productivity across configurations; correlate experience with optimal settings.

**Expected tradeoffs:** Role-switching overhead; miscalibrated autonomy risk; skill profiling required.

**Guide sections upgraded:** Workflow modes, Team configuration, Onboarding patterns.

---

## D. Guide Upgrade Plan: Section-by-Section Deltas

### Sections to Rewrite with Verified Information

| Section | Current Claim | Verified Correction | Priority |
|---------|---------------|---------------------|----------|
| **CLAUDE.md Hierarchy** | 5-level (Enterprise → User → Project → Modular → Local) | 4-level (User → Parent dirs → Working dir → Child on-demand) | CRITICAL |
| **Extended Thinking Triggers** | "think" (~4K), "ultrathink" (~32K) | Keywords now cosmetic; thinking auto-enabled at 31,999 tokens | CRITICAL |
| **Context Degradation** | "Quality declines well before 200K" | UNVERIFIED; remove or mark as hypothesis | HIGH |
| **Instruction Limits** | "~150-200 instructions reliably; system prompt uses ~50" | UNVERIFIED; remove or mark as community wisdom | HIGH |
| **Plan Mode Activation** | "Shift+Tab twice" | Correct, but add: /plan command also works | MEDIUM |
| **Settings Precedence** | May be incomplete | Add: Managed → Local → Project → User; programmatic overrides all | MEDIUM |

### New Sections to Add

**1. Extended Thinking Architecture (v2.x):**
- Document the January 2026 change: thinking enabled by default
- Explain Tab toggle mechanism
- Document MAX_THINKING_TOKENS env var
- Deprecation notice for keyword-based triggers

**2. MCP Security Model:**
- Trust model (Anthropic does not audit MCP servers)
- Permission syntax: `mcp__server__tool`, `mcp__server__*`
- Tool Search dynamic loading (>10% context threshold)
- mcpServers configuration schema with transport types

**3. Enterprise Configuration:**
- managed-settings.json location and precedence
- Policy-based MCP allowlists/denylists
- Cannot-be-overridden settings

**4. Checkpoint System:**
- Automatic state saving before each change
- Esc-Esc or /rewind command
- Restore options: code only, conversation only, both
- Limitation: applies to Claude's edits only, not user edits or bash commands

**5. Community Patterns Section:**
- Handoff document pattern
- Git worktree isolation
- Block-at-commit hooks strategy
- Master-Clone vs. Lead-Specialist agent patterns

### Sections to Demote to "Unverified/Community Wisdom"

| Section | Reason |
|---------|--------|
| Context degradation at specific percentages | No official documentation; community observation only |
| Instruction count limits | No official documentation found |
| Specific thinking token allocations (4K/10K/32K) | Outdated; mechanism changed |
| Custom subagent performance claims | Community reports mixed; official guidance minimal |

### Sections to Remove or Archive

- **"Ultrathink" as active mechanism** — replace with historical note
- **5-level hierarchy diagram** — replace with correct 4-level hierarchy
- **Token allocation tables for thinking keywords** — replace with v2.x mechanism

---

## E. Config Pack Upgrade Plan

### Hierarchy Corrections

**Current (incorrect):**
```
├── Enterprise Settings
│   └── User Settings
│       └── Project Settings
│           └── Modular Rules
│               └── Local Settings
```

**Corrected (verified):**
```
Precedence: Managed > Local > Project > User

Files:
├── /etc/claude-code/managed-settings.json    [Enterprise - highest]
├── .claude/settings.local.json               [Local - not committed]
├── .claude/settings.json                     [Project - committed]
└── ~/.claude/settings.json                   [User - lowest]

CLAUDE.md Loading:
├── ~/.claude/CLAUDE.md                       [User-level, always loaded]
├── ../../CLAUDE.md                           [Recursive upward from cwd]
├── ../CLAUDE.md                              
├── ./CLAUDE.md                               [Working directory]
└── ./subdir/CLAUDE.md                        [Loaded ON-DEMAND when working in subdir]
```

### Settings.json Template Upgrade

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run:*)",
      "Bash(git status)",
      "Bash(git diff:*)",
      "Read(src/**)",
      "Edit(src/**)"
    ],
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(~/.ssh/**)",
      "Read(~/.aws/**)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(rm -rf:*)"
    ],
    "ask": [
      "Bash(git push:*)",
      "Bash(npm publish:*)",
      "Write(**)"
    ]
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Bash command: $CC_TOOL_INPUT' >> /tmp/claude-audit.log"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command", 
            "command": "npm run lint -- --fix $CC_TOOL_INPUT_FILE 2>/dev/null || true"
          }
        ]
      }
    ]
  },
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  },
  "env": {
    "MAX_THINKING_TOKENS": "31999",
    "CLAUDE_CODE_ENABLE_TELEMETRY": "0"
  }
}
```

### CLAUDE.md Template Upgrade

```markdown
# Project: [Name]

## Quick Commands
- `npm run dev` — Start development server
- `npm run test` — Run test suite  
- `npm run lint` — Check linting
- `npm run typecheck` — TypeScript validation

## Code Style
- Use TypeScript strict mode (we've had production bugs from implicit any)
- Prefer named exports over default exports
- Use async/await over .then() chains
- Destructure imports: `import { useState } from 'react'`

## Testing
- Run tests after any code change: `npm run test`
- Write unit tests for new functions
- DO NOT mock implementations to make tests pass
- DO NOT uncomment failing tests

## Gotchas
❌ Bad: `import React from 'react'` (we use named imports)
✅ Good: `import { useState, useEffect } from 'react'`

❌ Bad: Deleting tests that fail
✅ Good: Fixing the code to make tests pass

## Environment
- Node 20+
- pnpm (not npm or yarn)
- PostgreSQL for database

## When Done
1. Run `npm run typecheck`
2. Run `npm run test`
3. Run `npm run lint`
4. Commit in logical chunks with conventional commit messages
```

---

## F. Open Questions List

### Critical Unknowns (High Risk if Ambiguous)

| Question | Why It Matters | Proposed Confirmation Method |
|----------|----------------|------------------------------|
| **Exact compaction algorithm** | Users report lossy/unpredictable behavior | Request official documentation; instrument compaction to measure information loss |
| **Context degradation curve** | Guides claim quality drops before 200K; unverified | Controlled experiment: run identical tasks at 25%/50%/75%/95% context fill |
| **Thinking keyword residual effects** | Community reports "ultrathink still helps" despite deprecation | A/B test with/without keywords on complex tasks; measure output quality |
| **Child CLAUDE.md loading semantics** | "On-demand" is vague; what triggers loading? | Test: create nested CLAUDE.md, observe when contents appear in context |
| **Tool Search activation threshold** | Documented as ">10% context" but unclear measurement | Instrument tool loading; test with varying MCP tool counts |

### Medium-Priority Unknowns

| Question | Why It Matters | Proposed Confirmation Method |
|----------|----------------|------------------------------|
| Custom agent vs. Task tool performance | Community divided on effectiveness | Benchmark identical tasks with both patterns |
| .claudeignore reliability | Reports of files being read despite ignore rules | Security audit with honeypot files |
| Managed settings Windows location | Linux/macOS documented, Windows unclear | Test on Windows; request official docs |
| Hook timeout behavior | What happens if hook command hangs? | Test with sleep 60 in hook |
| Subagent context inheritance | Do subagents inherit full parent context? | Instrument subagent token usage |

### Lower-Priority Unknowns

| Question | Why It Matters | Proposed Confirmation Method |
|----------|----------------|------------------------------|
| Exact system prompt token count | Optimization opportunity | Use verbose mode; count tokens |
| MCP server timeout defaults | Reliability engineering | Test with slow-responding servers |
| Checkpoint storage location/format | Backup/restore strategy | Examine filesystem after checkpoint creation |
| Plugin marketplace moderation | Security trust model | Review marketplace policies |

### Risks if Left Ambiguous

**Compaction uncertainty:** Teams may experience data loss mid-session without warning; recommend implementing custom PreCompact hooks to log what gets summarized.

**Thinking keyword confusion:** Developers may waste effort crafting "ultrathink" prompts believing they affect behavior; update all training materials.

**Context degradation claims:** Teams may prematurely reset sessions, losing valuable context; or conversely, trust context too long and experience quality issues.

**Security gaps:** .env auto-loading and .claudeignore reliability issues mean sensitive data may be exposed to model; implement deny rules as defense-in-depth.

---

## Appendix: Source Citations and Access Dates

### Official Anthropic Sources (Verified January 29, 2026)

| Source | URL | Type |
|--------|-----|------|
| Memory Documentation | docs.anthropic.com/en/docs/claude-code/memory | Stable docs |
| Settings Documentation | docs.anthropic.com/en/docs/claude-code/settings | Stable docs |
| Hooks Reference | docs.anthropic.com/en/docs/claude-code/hooks | Stable docs |
| Best Practices | anthropic.com/engineering/claude-code-best-practices | Blog (April 2025) |
| Common Workflows | code.claude.com/docs/en/common-workflows | Stable docs |
| Extended Thinking | docs.anthropic.com/en/docs/build-with-claude/extended-thinking | Stable docs |
| Claude 4 Launch | anthropic.com/news/claude-4 | Announcement (May 2025) |
| Autonomous Work Update | anthropic.com/news/enabling-claude-code-to-work-more-autonomously | Announcement (Sep 2025) |
| $1B Milestone | anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone | Announcement (Dec 2025) |

### GitHub Repositories (Verified January 29, 2026)

| Repository | Purpose | Stars |
|------------|---------|-------|
| anthropics/claude-code | Official issue tracker, plugins | ~42.4k |
| anthropics/skills | Agent Skills examples | ~40.2k |
| agentskills/agentskills | Skills specification | 69 |
| anthropics/claude-code-action | GitHub Actions integration | Official |

### Community Sources (Ephemeral Discussions)

| Source | Author | Date | Credibility |
|--------|--------|------|-------------|
| lucumr.pocoo.org | Armin Ronacher (Flask creator) | Dec 2025 | High |
| blog.sshh.io | Shrivu Shankar (Enterprise lead) | Jan 2026 | High |
| steipete.me | Peter Steinberger (PSPDFKit) | Oct 2025 | High |
| thezvi.substack.com | Zvi Mowshowitz | Jan 2026 | Medium-High |
| r/ClaudeAI, r/ClaudeCode | Community | Ongoing | Medium |
| ykdojo/claude-code-tips | Community guide | Jan 2026 | Medium |

---

## Conclusion: The Verified Operating Model

Based on this five-phase validation, the recommended Claude Code operating model for serious engineering repositories:

**Default stance:** Conservative permissions (explicit allow/deny), Plan Mode for architectural work, manual context management via `/clear` + handoff documents, PreToolUse hooks for commit-time validation.

**Key dials:**
1. **Autonomy level:** Normal (default) → Auto-Accept (trusted tasks) → YOLO (sandboxed only)
2. **Thinking:** Enabled by default; use Tab toggle if cost-constrained
3. **Context strategy:** Clear after each logical task; preserve via handoff documents
4. **Parallel work:** Git worktrees for true isolation; multiple terminal sessions

**Mode transitions:**
- New feature → Plan Mode → approve plan → Normal Mode → implement
- Bug fix → Normal Mode → Edit + Test → commit
- Exploration → Plan Mode throughout → no modifications
- Batch refactoring → YOLO in container → review diffs

The most significant correction to existing guides: **Extended thinking keywords are now cosmetic**. All documentation referencing "ultrathink" as a mechanism should be updated to reflect the January 2026 architecture change where thinking is enabled by default at maximum budget (31,999 tokens).

This research validates Claude Code as a production-ready agentic coding tool with well-documented configuration surfaces, while identifying nine critical gaps where official documentation remains silent and community practices have diverged to fill the void.