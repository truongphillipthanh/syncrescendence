# Syncrescendence Makefile
# Standard targets for repository operations

.PHONY: verify sync update-ledgers tree clean help pack pack-verify token sync-drive sync-all

# Default target
help:
	@echo "Syncrescendence Repository Commands"
	@echo ""
	@echo "  make verify         - Run all verification checks"
	@echo "  make sync           - Pull, rebase, push"
	@echo "  make update-ledgers - Validate and report ledger status"
	@echo "  make tree           - Generate current directory tree"
	@echo "  make clean          - Remove temporary files"
	@echo "  make pack SRC=...   - Create clean evidence pack (no macOS contamination)"
	@echo "  make pack-verify ARCHIVE=...  - Verify archive for contamination"
	@echo "  make token PHASE=... NEXT=...  - Generate handoff token"
	@echo "  make sync-all                  - Generate token and copy to clipboard"
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
	@wc -l < 00-ORCHESTRATION/state/tasks.csv
	@echo -n "projects.csv rows: "
	@wc -l < 00-ORCHESTRATION/state/projects.csv
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
	@head -1 00-ORCHESTRATION/state/tasks.csv
	@echo "  Total rows: $$(wc -l < 00-ORCHESTRATION/state/tasks.csv)"
	@echo "  Done: $$(grep -c ',done,' 00-ORCHESTRATION/state/tasks.csv || echo 0)"
	@echo "  In Progress: $$(grep -c ',in_progress,' 00-ORCHESTRATION/state/tasks.csv || echo 0)"
	@echo ""
	@echo "projects.csv:"
	@head -1 00-ORCHESTRATION/state/projects.csv
	@echo "  Total rows: $$(wc -l < 00-ORCHESTRATION/state/projects.csv)"
	@echo "  Complete: $$(grep -c ',complete,' 00-ORCHESTRATION/state/projects.csv || echo 0)"
	@echo "  In Progress: $$(grep -c ',in_progress,' 00-ORCHESTRATION/state/projects.csv || echo 0)"
	@echo ""
	@echo "sources.csv:"
	@echo "  Total rows: $$(wc -l < 04-SOURCES/sources.csv)"
	@echo "  Processed: $$(grep -c ',processed,' 04-SOURCES/sources.csv || echo 0)"

# Generate directory tree
tree:
	@echo "Generating tree..."
	@tree -L 2 -I 'node_modules|.git|__pycache__|*.pyc' > 00-ORCHESTRATION/state/DYN-ACTUAL_TREE.md
	@echo "Tree saved to 00-ORCHESTRATION/state/DYN-ACTUAL_TREE.md"

# Clean temporary files
clean:
	@echo "Cleaning temporary files..."
	@find . -name "*.tmp" -delete
	@find . -name "*.bak.*" -mtime +7 -delete
	@find . -name ".DS_Store" -delete
	@echo "Clean complete."

# Create clean evidence pack (macOS contamination-free)
# Usage: make pack SRC=path/to/directory [NAME=output_name]
pack:
	@if [ -z "$(SRC)" ]; then \
		echo "Usage: make pack SRC=<source_directory> [NAME=<output_name>]"; \
		echo ""; \
		echo "Examples:"; \
		echo "  make pack SRC=-OUTGOING/20260119-drift_cleanup"; \
		echo "  make pack SRC=-OUTGOING/20260119-drift_cleanup NAME=drift_cleanup"; \
		exit 1; \
	fi
	@bash 00-ORCHESTRATION/scripts/create_evidence_pack.sh "$(SRC)" "$(NAME)"

# Verify existing archive for contamination
# Usage: make pack-verify ARCHIVE=path/to/archive.zip
pack-verify:
	@if [ -z "$(ARCHIVE)" ]; then \
		echo "Usage: make pack-verify ARCHIVE=<path_to_archive.zip>"; \
		exit 1; \
	fi
	@bash 00-ORCHESTRATION/scripts/create_evidence_pack.sh --verify-only "$(ARCHIVE)"

# Constellation handoff token generation
# Usage: make token PHASE=current_phase NEXT=next_phase
token:
	@FINGERPRINT=$$(git rev-parse --short HEAD) && \
	TIMESTAMP=$$(date -u +"%Y-%m-%dT%H:%M:%SZ") && \
	echo "{\"fingerprint\":\"$$FINGERPRINT\",\"timestamp\":\"$$TIMESTAMP\",\"phase\":\"$(PHASE)\",\"next\":\"$(NEXT)\"}" > .constellation/tokens/active.json && \
	echo "HANDOFF TOKEN" > .constellation/tokens/active.txt && \
	echo "Fingerprint: $$FINGERPRINT" >> .constellation/tokens/active.txt && \
	echo "Phase: $(PHASE) -> $(NEXT)" >> .constellation/tokens/active.txt && \
	echo "Time: $$TIMESTAMP" >> .constellation/tokens/active.txt && \
	cat .constellation/tokens/active.txt

# Sync to Google Drive (placeholder for future rclone integration)
sync-drive: token
	@echo "Drive sync not yet configured. Token generated."
	@cat .constellation/tokens/active.txt

# Generate token and copy to clipboard
sync-all: token
	@cat .constellation/tokens/active.txt | pbcopy
	@echo "Token copied to clipboard"
