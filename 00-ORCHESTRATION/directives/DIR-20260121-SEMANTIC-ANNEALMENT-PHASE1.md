# DIRECTIVE: DIR-20260121-SEMANTIC-ANNEALMENT-PHASE1

---
## DECISION ENVELOPE
handoff_id: HO-20260121-043000-ajna4
origin_platform: claude-web-acc1
origin_session: Ajna4 (Syncrescendence Interpreter)
destination_platform: claude-code
decision_timestamp: 2026-01-21T04:30:00Z

### Decision Context
trigger: Constellation infrastructure complete (DIR-20260120-CONSTELLATION-INFRASTRUCTURE), corpus sensing report received from Gemini CLI, handoff protocol design requires implementation
alternatives_considered:
  - Incremental directives (small bites): Rejected—creates expensive coherence reconstruction cycles, violates "Principal is bottleneck" principle
  - Full corpus annealment in one pass: Rejected—too risky; token economics issues in CANON require careful handling
  - Infrastructure-only pass (no canonization): Rejected—sensing report shows "Shadow Canon" in -INBOX blocking downstream work
selected_approach: Phased comprehensive directive addressing infrastructure + critical canonization + nomenclature in single execution cycle
selection_rationale: |
  The lens analysis (25/25 pass) confirms the integrated approach. The sensing report identifies clear triage decisions (teleology docs → CANON, fingerprint solution → OPERATIONAL). Executing these together creates compounding value: infrastructure enables better handoffs, canonization stabilizes definitions, nomenclature fixes prevent future drift. Splitting would require 3+ relay cycles with context loss at each boundary.

### Assumptions
- Repository is at commit 37f1f52 or later (post-constellation-infrastructure)
- The sensing report accurately reflects current corpus state
- Token economics warnings (100KB+ files) are flagged but NOT addressed this pass (Type 1 decision requiring more analysis)
- Flat Principle violations in -OUTGOING are tolerated (historical artifacts, not active infrastructure)

### Constraints Inherited
- Flat Principle: All new directories must be flat (no nesting beyond one level)
- Metadata prefixes: ARCH-, CANON-, REF-, DYN-, DIR-, TEMPLATE-
- Execution logs must persist to 00-ORCHESTRATION/execution_logs/
- Principal checkpoints are real gates, not rubber stamps

### Dependencies
- prior_handoff: DIR-20260120-CONSTELLATION-INFRASTRUCTURE (COMPLETE)
- requires_completion_of: Gemini corpus sensing sweep (COMPLETE - report attached)
- blocks: Corpus annealment Phase 2 (token economics), YouTube processing pipeline

### Principal Checkpoints
- [ ] Reviewed lens analysis (25/25 pass)
- [ ] Confirmed assumptions still valid
- [ ] Approved for execution
---

## PREAMBLE

```bash
# Run immediately upon receiving this directive:
cd ~/Desktop/syncrescendence  # or your repo path
git pull origin main
make log-init DIRECTIVE=SEMANTIC-ANNEALMENT-PHASE1
```

If `make log-init` fails (target doesn't exist yet), this directive creates it.

---

## OBJECTIVE

Complete the first phase of semantic annealment:
1. **Handoff Infrastructure**: Implement State Fingerprint Solution with Decision Envelope integration
2. **Execution Log System**: Create templates and Makefile automation for persistent logging
3. **Critical Canonization**: Move confirmed -INBOX documents to appropriate homes
4. **Nomenclature Normalization**: Fix lowercase violations in critical operational files
5. **Prompt Operationalization**: Install Gemini sensing prompt for future sweeps

Success state: A repository where handoffs are verifiable, execution is logged, and the "Shadow Canon" is resolved.

---

## CONSTRAINTS

- All file operations are reversible via git (Type 2 decisions)
- Do NOT modify files >50KB without explicit Principal approval
- Do NOT delete any files—archive instead
- Do NOT flatten -OUTGOING historical bundles (tolerated violation)
- Preserve all git history

---

## PHASE 1: Execution Log Infrastructure

### 1.1 Create Execution Log Template

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

## Verification Results

| Check | Result | Evidence |
|-------|--------|----------|
| [check 1] | PASS/FAIL | [command output or observation] |

## Decisions Made During Execution
[Document any ambiguities resolved, judgment calls, or deviations from directive]

## Artifacts Created
- `path/to/file1.ext` — [description]

## Continuation Vector
[What should happen next, if anything]
```

### 1.2 Create Directive Envelope Template

Create `06-EXEMPLA/TEMPLATE-DIRECTIVE.md`:

```markdown
# DIRECTIVE: DIR-YYYYMMDD-NAME

---
## DECISION ENVELOPE
handoff_id: HO-YYYYMMDD-HHMMSS-[source]
origin_platform: [claude-web|chatgpt|gemini|claude-code]
origin_session: [thread name or ID]
destination_platform: [target platform]
decision_timestamp: YYYY-MM-DDTHH:MM:SSZ

### Decision Context
trigger: [What prompted this work]
alternatives_considered:
  - [Option A]: [why rejected]
selected_approach: [Chosen option]
selection_rationale: |
  [2-5 sentences explaining WHY]

### Assumptions
- [Assumption that could invalidate directive if wrong]

### Constraints Inherited
- [Constraint from prior decisions]

### Dependencies
- prior_handoff: [HO-ID or "none"]
- requires_completion_of: [prerequisites]
- blocks: [downstream work]

### Principal Checkpoints
- [ ] Reviewed decision rationale
- [ ] Confirmed assumptions still valid
- [ ] Approved for execution
---

## PREAMBLE
\`\`\`bash
make log-init DIRECTIVE=NAME
\`\`\`

## OBJECTIVE
[What success looks like]

## CONSTRAINTS
[Hard boundaries]

## DELIVERABLES
- [ ] Item 1
- [ ] Item 2

## VERIFICATION
\`\`\`bash
# Commands to prove completion
\`\`\`

## POSTAMBLE
\`\`\`bash
make log STATUS=COMPLETE DIRECTIVE=NAME
git add -A
git commit -m "feat(DIR-YYYYMMDD-NAME): [summary]"
\`\`\`
```

### 1.3 Update Makefile with Log Targets

Append to existing `Makefile`:

```make
# ============================================
# EXECUTION LOGGING
# ============================================

LOG_DIR := 00-ORCHESTRATION/execution_logs
DIRECTIVE ?= UNNAMED
STATUS ?= IN_PROGRESS

.PHONY: log-init log log-view

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
		echo "" >> "$$DIRECTIVE_FILE" && \
		echo "## Deliverables" >> "$$DIRECTIVE_FILE" && \
		echo "" >> "$$DIRECTIVE_FILE" && \
		echo "| Item | Status | Notes |" >> "$$DIRECTIVE_FILE" && \
		echo "|------|--------|-------|" >> "$$DIRECTIVE_FILE" && \
		echo "| | | |" >> "$$DIRECTIVE_FILE" && \
		echo "" >> "$$DIRECTIVE_FILE" && \
		echo "## Verification Results" >> "$$DIRECTIVE_FILE" && \
		echo "" >> "$$DIRECTIVE_FILE" && \
		echo "| Check | Result | Evidence |" >> "$$DIRECTIVE_FILE" && \
		echo "|-------|--------|----------|" >> "$$DIRECTIVE_FILE" && \
		echo "| | | |" >> "$$DIRECTIVE_FILE" && \
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
		echo "Updated: $$DIRECTIVE_FILE → status: $(STATUS)"; \
	else \
		echo "ERROR: No log found. Run 'make log-init DIRECTIVE=$(DIRECTIVE)' first"; \
		exit 1; \
	fi

log-view:
	@ls -la $(LOG_DIR)/*.md 2>/dev/null | tail -5 || echo "No logs found"
```

---

## PHASE 2: State Fingerprint System

### 2.1 Enhance Token Generation

Update `.constellation/tokens/` with enhanced token format.

Create `.constellation/phase-specs/README.md`:

```markdown
# Phase Specifications

This directory contains phase-specific instructions for each step in the constellation workflow.

## Phase Index
- `phase-1-interpret.md` — Claude Web interpretation specs
- `phase-2-compile.md` — ChatGPT compilation specs  
- `phase-3-digest.md` — Gemini digestion specs
- `phase-4-execute.md` — Claude Code execution specs

## Usage
Platforms reference these specs via handoff tokens. The token's `spec_reference` field points to the relevant phase spec.
```

### 2.2 Update Makefile Token Target

Replace existing `token` target with enhanced version:

```make
# ============================================
# HANDOFF TOKEN SYSTEM
# ============================================

PHASE ?= unspecified
NEXT ?= unspecified
FROM_PLATFORM ?= unknown
TO_PLATFORM ?= unknown

.PHONY: token token-json token-full state-broadcast

token:
	@FINGERPRINT=$$(git rev-parse --short HEAD) && \
	TIMESTAMP=$$(date -u +"%Y-%m-%dT%H:%M:%SZ") && \
	TOKEN_ID="HANDOFF-$$(date +%Y%m%d)-$$(date +%H%M%S)-$(PHASE)-to-$(NEXT)" && \
	echo "" && \
	echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" && \
	echo "HANDOFF TOKEN: $$TOKEN_ID" && \
	echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" && \
	echo "" && \
	echo "Fingerprint: $$FINGERPRINT" && \
	echo "Phase: $(PHASE) → $(NEXT)" && \
	echo "From: $(FROM_PLATFORM)" && \
	echo "To: $(TO_PLATFORM)" && \
	echo "When: $$TIMESTAMP" && \
	echo "" && \
	echo "VERIFY: git rev-parse --short HEAD should return: $$FINGERPRINT" && \
	echo "" && \
	echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" && \
	echo "" > .constellation/tokens/active.txt && \
	echo "HANDOFF TOKEN: $$TOKEN_ID" >> .constellation/tokens/active.txt && \
	echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >> .constellation/tokens/active.txt && \
	echo "" >> .constellation/tokens/active.txt && \
	echo "Fingerprint: $$FINGERPRINT" >> .constellation/tokens/active.txt && \
	echo "Phase: $(PHASE) → $(NEXT)" >> .constellation/tokens/active.txt && \
	echo "From: $(FROM_PLATFORM)" >> .constellation/tokens/active.txt && \
	echo "To: $(TO_PLATFORM)" >> .constellation/tokens/active.txt && \
	echo "When: $$TIMESTAMP" >> .constellation/tokens/active.txt && \
	echo "" >> .constellation/tokens/active.txt && \
	echo "VERIFY: git rev-parse --short HEAD should return: $$FINGERPRINT" >> .constellation/tokens/active.txt && \
	echo "" >> .constellation/tokens/active.txt && \
	echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >> .constellation/tokens/active.txt && \
	cat .constellation/tokens/active.txt | pbcopy && \
	echo "→ Token copied to clipboard"

token-json:
	@FINGERPRINT=$$(git rev-parse --short HEAD) && \
	FULL_HASH=$$(git rev-parse HEAD) && \
	TIMESTAMP=$$(date -u +"%Y-%m-%dT%H:%M:%SZ") && \
	TOKEN_ID="HANDOFF-$$(date +%Y%m%d)-$$(date +%H%M%S)-$(PHASE)-to-$(NEXT)" && \
	BRANCH=$$(git rev-parse --abbrev-ref HEAD) && \
	echo "{" > .constellation/tokens/active.json && \
	echo "  \"token_id\": \"$$TOKEN_ID\"," >> .constellation/tokens/active.json && \
	echo "  \"fingerprint\": \"$$FINGERPRINT\"," >> .constellation/tokens/active.json && \
	echo "  \"timestamp\": \"$$TIMESTAMP\"," >> .constellation/tokens/active.json && \
	echo "  \"phase\": {" >> .constellation/tokens/active.json && \
	echo "    \"current\": \"$(PHASE)\"," >> .constellation/tokens/active.json && \
	echo "    \"next\": \"$(NEXT)\"" >> .constellation/tokens/active.json && \
	echo "  }," >> .constellation/tokens/active.json && \
	echo "  \"from_platform\": \"$(FROM_PLATFORM)\"," >> .constellation/tokens/active.json && \
	echo "  \"to_platform\": \"$(TO_PLATFORM)\"," >> .constellation/tokens/active.json && \
	echo "  \"verification\": {" >> .constellation/tokens/active.json && \
	echo "    \"git_commit\": \"$$FULL_HASH\"," >> .constellation/tokens/active.json && \
	echo "    \"branch\": \"$$BRANCH\"" >> .constellation/tokens/active.json && \
	echo "  }" >> .constellation/tokens/active.json && \
	echo "}" >> .constellation/tokens/active.json && \
	echo "Written: .constellation/tokens/active.json"

token-full: token token-json
	@mkdir -p .constellation/tokens/archive && \
	TIMESTAMP=$$(date +%Y%m%d-%H%M%S) && \
	cp .constellation/tokens/active.json ".constellation/tokens/archive/$$TIMESTAMP.json" && \
	echo "Archived: .constellation/tokens/archive/$$TIMESTAMP.json"
```

### 2.3 Create Token Archive Directory

```bash
mkdir -p .constellation/tokens/archive
mkdir -p .constellation/phase-specs
```

---

## PHASE 3: Critical Canonization

Based on sensing report, these moves are confirmed (High Confidence):

### 3.1 Teleology Documents → CANON

```bash
# Constellation teleology - foundational architecture
mv -INBOX/constellation-teleology.md 01-CANON/CANON-25210-CONSTELLATION_TELEOLOGY-lattice.md

# Memory architecture teleology - foundational architecture  
mv -INBOX/memory-architecture-teleology.md 01-CANON/CANON-25010-MEMORY_TELEOLOGY-lattice.md
```

### 3.2 Operational Documents → OPERATIONAL

```bash
# State fingerprint solution - active protocol (not archived)
mkdir -p 02-ENGINE/protocols
mv -INBOX/state-fingerprint-solution.md 02-ENGINE/protocols/REF-STATE_FINGERPRINT_PROTOCOL.md

# Compiler handoff (if still in -INBOX)
mkdir -p 02-ENGINE/prompts/canonical
# mv -INBOX/CHATGPT_COMPILER_HANDOFF.md 02-ENGINE/prompts/canonical/ (if exists)

# Configuration registry
mkdir -p 02-ENGINE/registries
mv -INBOX/CONFIGURATION_REGISTRY.md 02-ENGINE/registries/REF-CONFIGURATION_REGISTRY.md

# Memory architecture matrix (operational rules, not philosophy)
mv -INBOX/memory-architecture-matrix.md 02-ENGINE/memory/REF-MEMORY_ARCHITECTURE_MATRIX.md
```

### 3.3 JSX/Diagrams → ARCHIVE or EXEMPLA

```bash
# Architecture diagram (superseded by implementation)
mv -INBOX/constellation-architecture.jsx 05-MEMORY/ARCH-constellation-architecture-v1.jsx
mv -INBOX/constellation-bifurcated-architecture.jsx 05-MEMORY/ARCH-constellation-bifurcated-architecture.jsx

# Process flow diagram (may be useful as example)
# mv -INBOX/constellation-process-flow.jsx 06-EXEMPLA/EXAMPLE-constellation-process-flow.jsx
```

### 3.4 CSV Files → OPERATIONAL/registries

```bash
# Account/platform registries
mv -INBOX/accounts.csv 02-ENGINE/registries/DYN-ACCOUNTS.csv
mv -INBOX/platforms.csv 02-ENGINE/registries/DYN-PLATFORMS.csv
mv -INBOX/roles.csv 02-ENGINE/registries/DYN-ROLES.csv
```

### 3.5 COCKPIT.md Resolution

```bash
# Check if -INBOX/COCKPIT.md differs from root
diff COCKPIT.md -INBOX/COCKPIT.md 2>/dev/null
# If identical: rm -INBOX/COCKPIT.md
# If different: mv -INBOX/COCKPIT.md to root (overwrite) OR archive older version
```

### 3.6 Interaction Dynamics → CANON

```bash
# High-value spec (40KB) - definitional document
mv -INBOX/INTERACTION_DYNAMICS_SPECIFICATION.md 01-CANON/CANON-30460-INTERACTION_DYNAMICS-comet.md
```

---

## PHASE 4: Nomenclature Normalization

Fix lowercase violations in critical files:

```bash
# State directory files
cd 00-ORCHESTRATION/state/
mv burndown.csv DYN-BURNDOWN.csv 2>/dev/null || true
mv projects.csv DYN-PROJECTS.csv 2>/dev/null || true
mv tasks.csv DYN-TASKS.csv 2>/dev/null || true
cd ../..

# Sources directory
cd 04-SOURCES/
mv creator_bios.md REF-CREATOR_BIOS.md 2>/dev/null || true
mv filename_mapping.csv REF-FILENAME_MAPPING.csv 2>/dev/null || true
mv sources.csv DYN-SOURCES.csv 2>/dev/null || true
cd ..

# Root orphans
mv AGENTS.md 02-ENGINE/registries/REF-AGENTS.md 2>/dev/null || true
```

---

## PHASE 5: Prompt Installation

### 5.1 Install Gemini Sensing Prompt

Create `00-ORCHESTRATION/scripts/GEMINI-CORPUS-SENSING-PROMPT.md`:

[Insert full content from the GEMINI-CORPUS-SENSING-PROMPT.md artifact created earlier]

### 5.2 Update corpus-survey.sh

Ensure `00-ORCHESTRATION/scripts/corpus-survey.sh` references the prompt:

```bash
#!/bin/bash
# Corpus Survey - Gemini CLI Wrapper
# Usage: ./corpus-survey.sh [output-dir]

OUTPUT_DIR="${1:-"-OUTGOING/$(date +%Y%m%d)-corpus-survey"}"
PROMPT_FILE="00-ORCHESTRATION/scripts/GEMINI-CORPUS-SENSING-PROMPT.md"

mkdir -p "$OUTPUT_DIR"

echo "Running Gemini corpus sensing sweep..."
echo "Output directory: $OUTPUT_DIR"

# Generate file inventory
find . -type f \( -name "*.md" -o -name "*.txt" -o -name "*.csv" -o -name "*.yaml" -o -name "*.json" \) \
  ! -path "./.git/*" ! -path "./node_modules/*" \
  -exec wc -c {} \; | sort -rn > "$OUTPUT_DIR/file_inventory.txt"

echo "File inventory generated: $OUTPUT_DIR/file_inventory.txt"
echo ""
echo "To run Gemini analysis:"
echo "  gemini -p \"\$(cat $PROMPT_FILE)\" > \"$OUTPUT_DIR/SENSING_REPORT.md\""
```

---

## PHASE 6: Retroactive Logging

### 6.1 Log Previous Directive

Move the uploaded execution log to proper location:

```bash
# If DIR-20260120-CONSTELLATION-INFRASTRUCTURE.md is in -INBOX or uploads
mv [source]/DIR-20260120-CONSTELLATION-INFRASTRUCTURE.md 00-ORCHESTRATION/execution_logs/
```

### 6.2 Archive Sensing Report

```bash
# Move corpus survey results to -OUTGOING
mv [source]/20260119-corpus-annealment-survey/ -OUTGOING/
```

---

## VERIFICATION

```bash
echo "=== Phase 1: Execution Log Infrastructure ==="
cat 06-EXEMPLA/TEMPLATE-EXECUTION_LOG.md | head -10
cat 06-EXEMPLA/TEMPLATE-DIRECTIVE.md | head -10
make log-init DIRECTIVE=TEST && make log STATUS=COMPLETE DIRECTIVE=TEST
cat 00-ORCHESTRATION/execution_logs/DIR-*-TEST.md

echo ""
echo "=== Phase 2: State Fingerprint System ==="
make token PHASE=test NEXT=verify FROM_PLATFORM=claude-code TO_PLATFORM=verification
make token-json
cat .constellation/tokens/active.json
ls .constellation/phase-specs/

echo ""
echo "=== Phase 3: Canonization ==="
ls 01-CANON/CANON-252*.md
ls 01-CANON/CANON-250*.md
ls 01-CANON/CANON-304*.md
ls 02-ENGINE/protocols/
ls 02-ENGINE/registries/

echo ""
echo "=== Phase 4: Nomenclature ==="
ls 00-ORCHESTRATION/state/DYN-*.csv
ls 04-SOURCES/REF-*.md 04-SOURCES/DYN-*.csv

echo ""
echo "=== Phase 5: Prompts ==="
ls 00-ORCHESTRATION/scripts/GEMINI-*.md
cat 00-ORCHESTRATION/scripts/corpus-survey.sh | head -15

echo ""
echo "=== Phase 6: Logging ==="
ls 00-ORCHESTRATION/execution_logs/DIR-202601*.md
```

---

## POSTAMBLE

```bash
# Update execution log with results
make log STATUS=COMPLETE DIRECTIVE=SEMANTIC-ANNEALMENT-PHASE1

# Commit all changes
git add -A
git commit -m "feat(semantic-annealment): Phase 1 complete - infrastructure, canonization, nomenclature

- Execution log system with templates and Makefile targets
- Enhanced handoff token generation with JSON format
- Canonized teleology docs (CANON-25010, CANON-25210)
- Operationalized protocols and registries
- Fixed nomenclature violations (DYN-, REF- prefixes)
- Installed Gemini sensing prompt

Resolves: Shadow Canon in -INBOX
Addresses: Sensing report priorities 1-3
Blocks: Phase 2 token economics, YouTube pipeline"

# Generate handoff token for next phase
make token-full PHASE=annealment-p1 NEXT=annealment-p2 FROM_PLATFORM=claude-code TO_PLATFORM=claude-web
```

---

## CONTINUATION VECTOR

After this directive completes:

1. **Token Economics Pass** (Phase 2): Address 100KB+ files in CANON (CANON-00005, CANON-31141, CANON-31143) — requires Principal decision on split strategy
2. **Flat Principle Sweep**: Clean up nested directories in 04-SOURCES/raw/claudecode (3 levels) — may require restructuring raw source organization
3. **Hidden Intentions Audit**: Surface unpaid debts from Archive (Oracle9 transcript processing, Claude Web utilization)
4. **YouTube Pipeline**: Now unblocked by handoff infrastructure — design ingestion flow

---

## APPENDIX: Files Affected

### Created
- `06-EXEMPLA/TEMPLATE-EXECUTION_LOG.md`
- `06-EXEMPLA/TEMPLATE-DIRECTIVE.md`
- `.constellation/tokens/archive/` (directory)
- `.constellation/phase-specs/README.md`
- `00-ORCHESTRATION/scripts/GEMINI-CORPUS-SENSING-PROMPT.md`
- `02-ENGINE/protocols/` (directory)

### Moved (Canonized)
- `-INBOX/constellation-teleology.md` → `01-CANON/CANON-25210-CONSTELLATION_TELEOLOGY-lattice.md`
- `-INBOX/memory-architecture-teleology.md` → `01-CANON/CANON-25010-MEMORY_TELEOLOGY-lattice.md`
- `-INBOX/INTERACTION_DYNAMICS_SPECIFICATION.md` → `01-CANON/CANON-30460-INTERACTION_DYNAMICS-comet.md`

### Moved (Operationalized)
- `-INBOX/state-fingerprint-solution.md` → `02-ENGINE/protocols/REF-STATE_FINGERPRINT_PROTOCOL.md`
- `-INBOX/CONFIGURATION_REGISTRY.md` → `02-ENGINE/registries/REF-CONFIGURATION_REGISTRY.md`
- `-INBOX/memory-architecture-matrix.md` → `02-ENGINE/memory/REF-MEMORY_ARCHITECTURE_MATRIX.md`
- `-INBOX/accounts.csv` → `02-ENGINE/registries/DYN-ACCOUNTS.csv`
- `-INBOX/platforms.csv` → `02-ENGINE/registries/DYN-PLATFORMS.csv`
- `-INBOX/roles.csv` → `02-ENGINE/registries/DYN-ROLES.csv`

### Moved (Archived)
- `-INBOX/constellation-architecture.jsx` → `05-MEMORY/ARCH-constellation-architecture-v1.jsx`
- `-INBOX/constellation-bifurcated-architecture.jsx` → `05-MEMORY/ARCH-constellation-bifurcated-architecture.jsx`

### Renamed (Nomenclature)
- `00-ORCHESTRATION/state/burndown.csv` → `DYN-BURNDOWN.csv`
- `00-ORCHESTRATION/state/projects.csv` → `DYN-PROJECTS.csv`
- `00-ORCHESTRATION/state/tasks.csv` → `DYN-TASKS.csv`
- `04-SOURCES/creator_bios.md` → `REF-CREATOR_BIOS.md`
- `04-SOURCES/filename_mapping.csv` → `REF-FILENAME_MAPPING.csv`
- `04-SOURCES/sources.csv` → `DYN-SOURCES.csv`
- `AGENTS.md` → `02-ENGINE/registries/REF-AGENTS.md`

### Modified
- `Makefile` (added log-init, log, log-view, enhanced token targets)
- `00-ORCHESTRATION/scripts/corpus-survey.sh` (if exists)

---

**END DIRECTIVE**

*This directive was produced by Claude Web (Ajna4 thread) following 25/25 lens analysis. Decision envelope attached. Principal checkpoint required before execution.*
