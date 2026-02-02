# Syncrescendence Makefile
# Standard targets for repository operations

.PHONY: verify sync update-ledgers tree clean help token token-json token-full sync-drive sync-all sync-checkpoint

# Default target
help:
	@echo "Syncrescendence Repository Commands"
	@echo ""
	@echo "  make verify         - Run all verification checks"
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

# Comprehensive verification
verify:
	@echo "=== Structure Verification ==="
	@echo -n "Unexpected subdirectories: "
	@find . -mindepth 2 -type d -name "scaffolding" 2>/dev/null | wc -l
	@echo -n "Root .md files: "
	@ls *.md 2>/dev/null | wc -l || echo "0"
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
	@echo "  Total rows: $$(wc -l < 04-SOURCES/DYN-SOURCES.csv)"
	@echo "  Processed: $$(grep -c ',processed,' 04-SOURCES/DYN-SOURCES.csv || echo 0)"

# Generate directory tree (stdout)
tree:
	@tree -L 2 -I 'node_modules|.git|__pycache__|*.pyc'

# Clean temporary files
clean:
	@echo "Cleaning temporary files..."
	@find . -name "*.tmp" -delete
	@find . -name "*.bak.*" -mtime +7 -delete
	@find . -name ".DS_Store" -delete
	@echo "Clean complete."

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

# Quick sync checkpoint (no file generation, just output)
sync-checkpoint:
	@echo "SYNC-CHECKPOINT: $$(date -u +"%Y-%m-%dT%H:%M:%SZ")" && \
	echo "COMMIT: $$(git rev-parse --short HEAD)" && \
	echo "BRANCH: $$(git rev-parse --abbrev-ref HEAD)"
