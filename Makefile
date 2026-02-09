# Syncrescendence Makefile
# Standard targets for repository operations

.PHONY: verify verify-full lint triage sync update-ledgers tree clean help token token-json token-full sync-drive sync-all sync-checkpoint regenerate-canon model-db model-query model-cost model-routing

# Default target
help:
	@echo "Syncrescendence Repository Commands"
	@echo ""
	@echo "  make verify         - Run all verification checks (Makefile)"
	@echo "  make verify-full    - Run comprehensive verification suite"
	@echo "  make lint           - Lint 02-ENGINE artifacts (frontmatter)"
	@echo "  make triage         - Show pending packets across all pipes"
	@echo "  make sync           - Pull, rebase, push"
	@echo "  make update-ledgers - Validate and report ledger status"
	@echo "  make tree           - Generate current directory tree"
	@echo "  make clean          - Remove temporary files"
	@echo "  make token PHASE=... NEXT=...  - Generate handoff token"
	@echo "  make sync-all                  - Generate token and copy to clipboard"
	@echo "  make token-json               - Generate JSON format token"
	@echo "  make token-full               - Generate both formats + archive"
	@echo "  make sync-checkpoint           - Quick sync checkpoint (no files)"
	@echo ""
	@echo "Intelligence:"
	@echo "  make regenerate-canon          - Regenerate all CANON templates from data"
	@echo "  make model-db                  - Initialize model intelligence database"
	@echo "  make model-cost                - Show constellation cost analysis"
	@echo "  make model-routing             - Show task routing matrix"
	@echo "  make model-query SQL=\"...\"     - Run custom SQL against model DB"
	@echo ""

# Comprehensive verification
verify:
	@echo "=== Structure Verification ==="
	@echo -n "Unexpected subdirectories: "
	@find . -mindepth 2 -type d -name "scaffolding" 2>/dev/null | wc -l
	@echo "Root .md files (expected: CLAUDE.md, COCKPIT.md, README.md):"
	@for f in CLAUDE.md COCKPIT.md README.md; do \
		if [ -f "$$f" ]; then echo "  ✓ $$f"; else echo "  ✗ $$f MISSING"; fi; \
	done
	@EXTRA=$$(ls *.md 2>/dev/null | grep -v -E '^(CLAUDE|COCKPIT|README)\.md$$' | head -5); \
	if [ -n "$$EXTRA" ]; then echo "  ⚠ Unexpected: $$EXTRA"; fi
	@echo ""
	@echo "=== Ledger Verification ==="
	@echo -n "tasks.csv rows: "
	@wc -l < 00-ORCHESTRATION/state/DYN-TASKS.csv
	@echo -n "projects.csv rows: "
	@wc -l < 00-ORCHESTRATION/state/DYN-PROJECTS.csv
	@echo ""
	@echo "=== Content Verification ==="
	@echo -n "Processed sources: "
	@ls 04-SOURCES/processed/*.md 2>/dev/null | wc -l || echo "0"
	@echo -n "CANON with integrations: "
	@grep -l "SOURCE-" 01-CANON/*.md 2>/dev/null | wc -l || echo "0"
	@echo ""
	@echo "=== Git Status ==="
	@git status --short
	@echo ""
	@echo "=== Verification Complete ==="

# Git sync with rebase
sync:
	@echo "Pulling latest..."
	git pull --rebase
	@echo "Pushing changes..."
	git push
	@echo "Sync complete."

# Ledger status report
update-ledgers:
	@echo "=== Ledger Status ==="
	@echo ""
	@echo "tasks.csv:"
	@head -1 00-ORCHESTRATION/state/DYN-TASKS.csv
	@echo "  Total rows: $$(wc -l < 00-ORCHESTRATION/state/DYN-TASKS.csv)"
	@echo "  Done: $$(grep -c ',done,' 00-ORCHESTRATION/state/DYN-TASKS.csv || echo 0)"
	@echo "  In Progress: $$(grep -c ',in_progress,' 00-ORCHESTRATION/state/DYN-TASKS.csv || echo 0)"
	@echo ""
	@echo "projects.csv:"
	@head -1 00-ORCHESTRATION/state/DYN-PROJECTS.csv
	@echo "  Total rows: $$(wc -l < 00-ORCHESTRATION/state/DYN-PROJECTS.csv)"
	@echo "  Complete: $$(grep -c ',complete,' 00-ORCHESTRATION/state/DYN-PROJECTS.csv || echo 0)"
	@echo "  In Progress: $$(grep -c ',in_progress,' 00-ORCHESTRATION/state/DYN-PROJECTS.csv || echo 0)"
	@echo ""
	@echo "sources.csv:"
	@if [ -f 04-SOURCES/DYN-SOURCES.csv ]; then \
		echo "  Total rows: $$(wc -l < 04-SOURCES/DYN-SOURCES.csv)"; \
		echo "  Processed: $$(grep -c ',processed,' 04-SOURCES/DYN-SOURCES.csv || echo 0)"; \
	else \
		echo "  (file not found)"; \
	fi

# Generate directory tree (stdout)
tree:
	@if command -v tree >/dev/null 2>&1; then \
		tree -L 2 -I 'node_modules|.git|__pycache__|*.pyc'; \
	else \
		echo "tree not installed (brew install tree). Falling back to find:"; \
		find . -maxdepth 2 -not -path './.git/*' -not -name '.DS_Store' | sort; \
	fi

# Clean temporary files
clean:
	@echo "Cleaning temporary files..."
	@find . -name "*.tmp" -not -path './.git/*' -delete 2>/dev/null; true
	@find . -name "*.bak.*" -mtime +7 -not -path './.git/*' -delete 2>/dev/null; true
	@find . -name ".DS_Store" -not -path './.git/*' -delete 2>/dev/null; true
	@echo "Clean complete."

# Comprehensive verification (scripts)
verify-full:
	@bash 00-ORCHESTRATION/scripts/verify_all.sh

# Lint operational artifacts
lint:
	@bash 00-ORCHESTRATION/scripts/ops_lint.sh

# Triage pending packets
triage:
	@bash 00-ORCHESTRATION/scripts/triage_outgoing.sh

# ============================================
# HANDOFF TOKEN SYSTEM
# ============================================

PHASE ?= unspecified
NEXT ?= unspecified
FROM_PLATFORM ?= unknown
TO_PLATFORM ?= unknown

# Usage: make token PHASE=current NEXT=next FROM_PLATFORM=source TO_PLATFORM=dest
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
	echo "Phase: $(PHASE) -> $(NEXT)" && \
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
	echo "Phase: $(PHASE) -> $(NEXT)" >> .constellation/tokens/active.txt && \
	echo "From: $(FROM_PLATFORM)" >> .constellation/tokens/active.txt && \
	echo "To: $(TO_PLATFORM)" >> .constellation/tokens/active.txt && \
	echo "When: $$TIMESTAMP" >> .constellation/tokens/active.txt && \
	echo "" >> .constellation/tokens/active.txt && \
	echo "VERIFY: git rev-parse --short HEAD should return: $$FINGERPRINT" >> .constellation/tokens/active.txt && \
	echo "" >> .constellation/tokens/active.txt && \
	echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >> .constellation/tokens/active.txt && \
	cat .constellation/tokens/active.txt | pbcopy && \
	echo "-> Token copied to clipboard"

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

# Sync to Google Drive (placeholder for future rclone integration)
sync-drive: token
	@echo "Drive sync not yet configured. Token generated."
	@cat .constellation/tokens/active.txt

# Generate token and copy to clipboard
sync-all: token
	@cat .constellation/tokens/active.txt | pbcopy
	@echo "Token copied to clipboard"

# ============================================
# INTELLIGENCE SYSTEM
# ============================================

# Regenerate CANON files from templates + data
regenerate-canon:
	@python3 00-ORCHESTRATION/scripts/regenerate_canon.py --all

# Initialize model intelligence database
model-db:
	@python3 00-ORCHESTRATION/scripts/model_db.py init

# Cost analysis
model-cost:
	@python3 00-ORCHESTRATION/scripts/model_db.py cost

# Task routing matrix
model-routing:
	@python3 00-ORCHESTRATION/scripts/model_db.py routing

# Custom SQL query (usage: make model-query SQL="SELECT * FROM models")
SQL ?= SELECT name, context_window, input_price_per_m FROM models ORDER BY name
model-query:
	@python3 00-ORCHESTRATION/scripts/model_db.py query "$(SQL)"

# Quick sync checkpoint (no file generation, just output)
sync-checkpoint:
	@echo "SYNC-CHECKPOINT: $$(date -u +"%Y-%m-%dT%H:%M:%SZ")" && \
	echo "COMMIT: $$(git rev-parse --short HEAD)" && \
	echo "BRANCH: $$(git rev-parse --abbrev-ref HEAD)"
