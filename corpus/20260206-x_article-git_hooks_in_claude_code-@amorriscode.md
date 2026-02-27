# git hooks in Claude Code

(Description: Illustration with a cream-colored background featuring a stylized magnifying glass rendered in black lines connected to a red diamond shape with a white curved symbol inside, suggesting the intersection of search/inspection and code/programming concepts.)

Did you know you can hook into git commands with Claude Code?

The PreToolUse/PostToolHooks hooks receive the tool input as JSON on stdin, so you can check if the command is a git command. Let's go through an example.

## In .claude/settings.json:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.command' | grep -q 'git commit' && { echo 'Running pre-commit checks...'; bun run lint && bun run typecheck; }"
          }
        ]
      }
    ]
  }
}
```

## Breaking it down:

- stdin receives JSON with the tool input (e.g., `{"command": "git commit -m '...'"}`)
- Exit code 0 = allow the tool to proceed
- Exit code 2 = block the tool with the hook's stdout shown as the reason

## A more robust version that uses a bash script might look like this:
```bash
#!/bin/bash
# .claude/hooks/pre-commit.sh

COMMAND=$(jq -r '.command' < /dev/stdin)

if echo "$COMMAND" | grep -q 'git commit'; then
  echo "Running checks before commit..."
  bun run typecheck || { echo "Typecheck failed!"; exit 2; }
  bun run lint || { echo "Lint failed!"; exit 2; }
  echo "All checks passed"
  exit 0
fi

# Not a commit, allow it
exit 0
```

## Then you just reference the script in your hook settings:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/pre-commit.sh"
          }
        ]
      }
    ]
  }
}
```

Hooks are a fantastic way to get Claude to adapt to the needs of your workflow.

We have many more examples in our docs: https://code.claude.com/docs/en/hooks