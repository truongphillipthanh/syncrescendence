# DIRECTIVE: DIR-20260120-EXECUTION-LOG-INFRASTRUCTURE

## Context
The constellation infrastructure (DIR-20260120-CONSTELLATION-INFRASTRUCTURE) completed successfully but the execution evidence remained trapped in Claude Code's session context. This breaks the principle: **every execution produces repository-legible evidence**.

This directive closes that gap and buttons up infrastructure that's definitively ready for canon.

## Objective
1. Create execution log infrastructure with portable output format
2. Update Makefile with `log` target
3. Create directive template that enforces log persistence
4. Move confirmed infrastructure documents from -INBOX to appropriate homes

## Constraints
- All paths relative to repository root
- Flat directory structure (no nesting beyond stated)
- Execution logs are Markdown (human-legible) with YAML frontmatter (machine-parseable)
- Templates use placeholders, not example data

---

## Deliverable 1: Execution Log Template

Create `06-EXEMPLA/TEMPLATE-EXECUTION_LOG.md`:

```markdown
---
directive_id: DIR-YYYYMMDD-NAME
executed_by: [claude-code|codex|gemini-cli]
started_at: YYYY-MM-DDTHH:MM:SSZ
completed_at: YYYY-MM-DDTHH:MM:SSZ
status: [COMPLETE|PARTIAL|FAILED|BLOCKED]
commit: [git short hash or "uncommitted"]
---

# Execution Log: DIR-YYYYMMDD-NAME

## Directive Summary
[One sentence describing what was requested]

## Deliverables

| Item | Status | Notes |
|------|--------|-------|
| [deliverable 1] | ✅/⚠️/❌ | [any relevant detail] |
| [deliverable 2] | ✅/⚠️/❌ | |

## Verification Results

| Check | Result | Evidence |
|-------|--------|----------|
| [check 1] | PASS/FAIL | [command output or observation] |

## Decisions Made During Execution
[Document any ambiguities resolved, judgment calls, or deviations from directive]

## Artifacts Created
- `path/to/file1.ext` — [description]
- `path/to/file2.ext` — [description]

## Continuation Vector
[What should happen next, if anything]

## Raw Output
<details>
<summary>Terminal output (collapsed)</summary>

```
[paste relevant terminal output here]
```

</details>
```

---

## Deliverable 2: Makefile Updates

Append to existing `Makefile`:

```make
# Execution logging
LOG_DIR := 00-ORCHESTRATION/execution_logs
DIRECTIVE ?= UNNAMED

.PHONY: log log-init

log-init:
	@mkdir -p $(LOG_DIR)
	@TIMESTAMP=$$(date -u +"%Y-%m-%dT%H:%M:%SZ") && \
	DIRECTIVE_FILE="$(LOG_DIR)/DIR-$$(date +%Y%m%d)-$(DIRECTIVE).md" && \
	if [ ! -f "$$DIRECTIVE_FILE" ]; then \
		echo "---" > "$$DIRECTIVE_FILE" && \
		echo "directive_id: DIR-$$(date +%Y%m%d)-$(DIRECTIVE)" >> "$$DIRECTIVE_FILE" && \
		echo "executed_by: claude-code" >> "$$DIRECTIVE_FILE" && \
		echo "started_at: $$TIMESTAMP" >> "$$DIRECTIVE_FILE" && \
		echo "completed_at: " >> "$$DIRECTIVE_FILE" && \
		echo "status: IN_PROGRESS" >> "$$DIRECTIVE_FILE" && \
		echo "commit: $$(git rev-parse --short HEAD 2>/dev/null || echo 'uncommitted')" >> "$$DIRECTIVE_FILE" && \
		echo "---" >> "$$DIRECTIVE_FILE" && \
		echo "" >> "$$DIRECTIVE_FILE" && \
		echo "# Execution Log: DIR-$$(date +%Y%m%d)-$(DIRECTIVE)" >> "$$DIRECTIVE_FILE" && \
		echo "Initialized: $$DIRECTIVE_FILE"; \
	else \
		echo "Log exists: $$DIRECTIVE_FILE"; \
	fi

log:
	@TIMESTAMP=$$(date -u +"%Y-%m-%dT%H:%M:%SZ") && \
	DIRECTIVE_FILE="$(LOG_DIR)/DIR-$$(date +%Y%m%d)-$(DIRECTIVE).md" && \
	if [ -f "$$DIRECTIVE_FILE" ]; then \
		sed -i '' "s/^completed_at:.*/completed_at: $$TIMESTAMP/" "$$DIRECTIVE_FILE" && \
		sed -i '' "s/^status:.*/status: $(STATUS)/" "$$DIRECTIVE_FILE" && \
		echo "Updated: $$DIRECTIVE_FILE with status $(STATUS)"; \
	else \
		echo "ERROR: No log found. Run 'make log-init DIRECTIVE=$(DIRECTIVE)' first"; \
	fi
```

Usage:
```bash
# At directive start
make log-init DIRECTIVE=EXECUTION-LOG-INFRASTRUCTURE

# At directive end
make log STATUS=COMPLETE DIRECTIVE=EXECUTION-LOG-INFRASTRUCTURE
```

---

## Deliverable 3: Directive Envelope Template

Create `06-EXEMPLA/TEMPLATE-DIRECTIVE.md`:

```markdown
# DIRECTIVE: DIR-YYYYMMDD-NAME

## Preamble
```bash
# Run immediately upon receiving this directive:
make log-init DIRECTIVE=NAME
```

## Context
[Why this directive exists—link to Oracle decision or preceding work]

## Objective
[What success looks like]

## Constraints
[Hard boundaries that must not be violated]

## Deliverables
- [ ] Item 1
- [ ] Item 2

## Verification
```bash
# Commands to prove completion
```

## Postamble
```bash
# Run after all deliverables complete:
make log STATUS=COMPLETE DIRECTIVE=NAME
git add 00-ORCHESTRATION/execution_logs/
git commit -m "log(DIR-YYYYMMDD-NAME): [summary]"
```

Append execution evidence to log file before committing.
```

---

## Deliverable 4: -INBOX Triage (Confirmed Moves Only)

These files are infrastructure-complete and should move:

| Source | Destination | Rationale |
|--------|-------------|-----------|
| `-INBOX/constellation-teleology.md` | `01-CANON/CANON-constellation-teleology.md` | Defines the architectural why; referenced by all agents |
| `-INBOX/memory-architecture-teleology.md` | `01-CANON/CANON-memory-architecture-teleology.md` | Same |
| `-INBOX/CHATGPT_COMPILER_HANDOFF.md` | `02-OPERATIONAL/prompts/canonical/CHATGPT_COMPILER_HANDOFF.md` | Active operational document |
| `-INBOX/constellation-architecture.jsx` | `05-ARCHIVE/ARCH-constellation-architecture-v1.jsx` | Superseded by implementation; keep for reference |
| `-INBOX/COCKPIT.md` | Evaluate after sensing sweep | May duplicate root COCKPIT.md |

**Do NOT move** (requires sensing sweep first):
- `accounts.csv`, `platforms.csv`, `roles.csv` — May belong in `02-OPERATIONAL/registries/` or need consolidation
- `CONFIGURATION_REGISTRY.md` — Unclear if current
- `INTERACTION_DYNAMICS_SPECIFICATION.md` — May be scaffold
- `grok-red-team-instructions.md` — Unclear status

Execute moves:
```bash
# Confirmed canonical
mv -INBOX/constellation-teleology.md 01-CANON/CANON-constellation-teleology.md
mv -INBOX/memory-architecture-teleology.md 01-CANON/CANON-memory-architecture-teleology.md

# Confirmed operational
mkdir -p 02-OPERATIONAL/prompts/canonical
mv -INBOX/CHATGPT_COMPILER_HANDOFF.md 02-OPERATIONAL/prompts/canonical/

# Archive (superseded)
mv -INBOX/constellation-architecture.jsx 05-ARCHIVE/ARCH-constellation-architecture-v1.jsx

git add -A
git commit -m "triage(-INBOX): canonize teleology docs, operationalize compiler handoff, archive jsx"
```

---

## Deliverable 5: Retroactive Log for Previous Directive

Create `00-ORCHESTRATION/execution_logs/DIR-20260120-CONSTELLATION-INFRASTRUCTURE.md`:

```markdown
---
directive_id: DIR-20260120-CONSTELLATION-INFRASTRUCTURE
executed_by: claude-code
started_at: 2026-01-21T03:20:00Z
completed_at: 2026-01-21T03:24:30Z
status: COMPLETE
commit: 37f1f52
---

# Execution Log: DIR-20260120-CONSTELLATION-INFRASTRUCTURE

## Directive Summary
Create constellation infrastructure: .dispatch/ watch folder architecture, state management directories, Makefile automation, and git hooks.

## Deliverables

| Item | Status | Notes |
|------|--------|-------|
| .constellation/tokens/ | ✅ | Created |
| .constellation/state/ | ✅ | Created |
| .dispatch/claude-lead/{pending,processing,complete}/ | ✅ | Created |
| .dispatch/claude-parallel/{pending,processing,complete}/ | ✅ | Created |
| .dispatch/codex/pending/ | ✅ | Created |
| .dispatch/gemini/pending/ | ✅ | Created |
| .constellation/tokens/active.json | ✅ | JSON token state |
| .constellation/tokens/active.txt | ✅ | Human-readable token |
| .constellation/state/current.yaml | ✅ | Git state snapshot |
| Makefile (token, sync-drive, sync-all) | ✅ | Updated |
| .git/hooks/post-commit | ✅ | Auto-updates state on commit |
| 00-ORCHESTRATION/scripts/corpus-survey.sh | ✅ | Gemini CLI wrapper |
| AGENTS.md | ✅ | Codex configuration |

## Verification Results

| Check | Result | Evidence |
|-------|--------|----------|
| Directories exist | PASS | ls confirmed all paths |
| make token works | PASS | Token generated to clipboard |
| Git hook fires on commit | PASS | current.yaml updated |
| current.yaml updated | PASS | Contains commit 37f1f52 |
| Clipboard has token | PASS | pbpaste confirmed |

## Artifacts Created
- `.constellation/` directory tree (10 directories)
- 7 infrastructure files
- Makefile targets: token, sync-drive, sync-all

## Continuation Vector
Execution log infrastructure needed (this directive addresses that gap).
```

---

## Verification

```bash
# Template exists
cat 06-EXEMPLA/TEMPLATE-EXECUTION_LOG.md | head -20

# Makefile targets work
make log-init DIRECTIVE=TEST
cat 00-ORCHESTRATION/execution_logs/DIR-*-TEST.md
make log STATUS=COMPLETE DIRECTIVE=TEST

# Retroactive log exists
cat 00-ORCHESTRATION/execution_logs/DIR-20260120-CONSTELLATION-INFRASTRUCTURE.md

# Triage completed
ls 01-CANON/CANON-*-teleology.md
ls 02-OPERATIONAL/prompts/canonical/CHATGPT_COMPILER_HANDOFF.md
```

---

## Postamble

```bash
make log STATUS=COMPLETE DIRECTIVE=EXECUTION-LOG-INFRASTRUCTURE
git add -A
git commit -m "feat(infra): execution log infrastructure, templates, -INBOX triage"
```
