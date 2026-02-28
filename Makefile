# Syncrescendence Makefile
# Standard targets for repository operations

.PHONY: configs sync clean sync-checkpoint tree help

# ──────────────────────────────────────────────────────────────
# Config Generation — Single-source build from AGENTS.md master
# ──────────────────────────────────────────────────────────────
# AGENTS.md is the single source of truth for all operational law.
# Platform-specific extensions (*-EXT.md) add only platform-native deltas.
# Generated files (CLAUDE.md, GEMINI.md) are what each CLI auto-loads.
# Edit AGENTS.md or *-EXT.md, then run: make configs

configs: AGENTS.md CLAUDE-EXT.md GEMINI-EXT.md OPENCLAW-EXT.md
	@cat AGENTS.md CLAUDE-EXT.md > CLAUDE.md
	@cat AGENTS.md GEMINI-EXT.md > GEMINI.md
	@echo "✓ CLAUDE.md generated (AGENTS.md + CLAUDE-EXT.md)"
	@echo "✓ GEMINI.md generated (AGENTS.md + GEMINI-EXT.md)"
	@echo "✓ Configs regenerated from single source"

# Default target
help:
	@echo "Syncrescendence Repository Commands"
	@echo ""
	@echo "  make configs          - Regenerate CLAUDE.md + GEMINI.md from sources"
	@echo "  make sync             - Pull, rebase, push"
	@echo "  make sync-checkpoint  - Quick sync checkpoint (git state)"
	@echo "  make tree             - Generate current directory tree"
	@echo "  make clean            - Remove temporary files"

# Git sync with rebase
sync:
	@echo "Pulling latest..."
	git pull --rebase
	@echo "Pushing changes..."
	git push
	@echo "Sync complete."

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

# Quick sync checkpoint (no file generation, just output)
sync-checkpoint:
	@echo "SYNC-CHECKPOINT: $$(date -u +"%Y-%m-%dT%H:%M:%SZ")" && \
	echo "COMMIT: $$(git rev-parse --short HEAD)" && \
	echo "BRANCH: $$(git rev-parse --abbrev-ref HEAD)"
