#!/bin/zsh
# setup-worktrees.sh
# Create git worktrees for multi-Claude coordination

set -e

REPO_ROOT=$(git rev-parse --show-toplevel)
PARENT_DIR=$(dirname "$REPO_ROOT")

echo "=== Syncrescendence Worktree Setup ==="
echo "Repository: $REPO_ROOT"
echo "Parent: $PARENT_DIR"
echo ""

# Ensure we're on develop branch
git checkout develop 2>/dev/null || git checkout -b develop

# Create worktrees
echo "Creating worktrees..."

if [ ! -d "$PARENT_DIR/syncrescendence-alpha" ]; then
    git worktree add "$PARENT_DIR/syncrescendence-alpha" -b alpha/work
    echo "  Created: syncrescendence-alpha"
else
    echo "  Exists: syncrescendence-alpha"
fi

if [ ! -d "$PARENT_DIR/syncrescendence-beta" ]; then
    git worktree add "$PARENT_DIR/syncrescendence-beta" -b beta/work
    echo "  Created: syncrescendence-beta"
else
    echo "  Exists: syncrescendence-beta"
fi

if [ ! -d "$PARENT_DIR/syncrescendence-gamma" ]; then
    git worktree add "$PARENT_DIR/syncrescendence-gamma" -b gamma/work
    echo "  Created: syncrescendence-gamma"
else
    echo "  Exists: syncrescendence-gamma"
fi

# Copy local settings template to each worktree
echo ""
echo "Copying local settings templates..."
for instance in alpha beta gamma; do
    WORKTREE="$PARENT_DIR/syncrescendence-$instance"
    if [ -d "$WORKTREE" ]; then
        mkdir -p "$WORKTREE/.claude"
        if [ -f "$REPO_ROOT/.claude/settings.local.json.template" ]; then
            cp "$REPO_ROOT/.claude/settings.local.json.template" \
               "$WORKTREE/.claude/settings.local.json"
            # Update instance name in the copy
            sed -i '' "s/\[ALPHA|BETA|GAMMA\]/$instance/g" \
                "$WORKTREE/.claude/settings.local.json"
            echo "  Configured: $instance"
        fi
    fi
done

echo ""
echo "=== Worktree Setup Complete ==="
echo ""
echo "Worktrees created:"
git worktree list
echo ""
echo "Next steps:"
echo "  1. Each Claude instance should cd to its assigned worktree"
echo "  2. Configure .claude/settings.local.json with account-specific settings"
echo "  3. Use branch prefixes for commits (alpha/, beta/, gamma/)"
