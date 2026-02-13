# PRAC: Multi-Account Coordination

**Scope**: CLAUDE_CONFIG_DIR, known bugs, isolation patterns, rate limit handling

---

## The Problem

Single account hits rate limits. Need multiple accounts for continuous work. But account switching on same device has documented bugs.

---

## Naive Approach (Buggy)

```bash
# Aliases for account switching
alias claude-acc1="CLAUDE_CONFIG_DIR=~/.claude-acc1 claude"
alias claude-acc2="CLAUDE_CONFIG_DIR=~/.claude-acc2 claude"
alias claude-acc3="CLAUDE_CONFIG_DIR=~/.claude-acc3 claude"
```

**Known Issues**:
- GitHub #5001: Buggy rate limit enforcement across accounts
- GitHub #12786: Account collision on same device
- Credentials leak between directories
- Rate limits not properly isolated

---

## Recommended: Separate Environments

### Separate Machines
```
Machine 1: Account 1 (Primary)
Machine 2: Account 2 (Backup)
Machine 3: Account 3 (Overflow)
```

**Best isolation**. No credential collision possible.

### Separate VMs
```bash
# Create VM per account
multipass launch -n claude-acc1
multipass launch -n claude-acc2
multipass launch -n claude-acc3

# Each VM has own Claude installation
multipass exec claude-acc1 -- claude
```

### Docker Containers
```dockerfile
FROM ubuntu:22.04
RUN curl -fsSL https://install.anthropic.com | sh
COPY .claude-acc1/ /root/.claude/
WORKDIR /workspace
```

```bash
docker run -v $(pwd):/workspace claude-acc1
docker run -v $(pwd):/workspace claude-acc2
```

**Note**: Each container needs own API credentials.

---

## Context Portability

With file-based context, any account can access strategic state:

```bash
# Account 1 creates handoff
git add 00-ORCHESTRATION/oracle_contexts/handoffs/
git commit -m "docs: Oracle handoff"
git push

# Account 2 picks up
git pull
# Now has equivalent context via CLAUDE.md + handoff docs
```

**Key**: Memory lives in repo, not in account.

---

## Rate Limit Handling

```
PROC RateLimitFailover:
    1: "Account 1 hits rate limit"

    2: "Check task type"
        - If implementation → Switch to Account 2
        - If large-context analysis → Route to Gemini
        - If simple lookup → Route to Haiku

    3: "Create handoff before switching"
        - Commit current state
        - Push to repo

    4: "Account 2 loads context"
        - git pull
        - Read handoff docs
        - Continue work

    5: "Account 1 recovers"
        - Available again after cooldown
        - Can resume or take new tasks
end
```

---

## Worktree Integration

Combine with git worktrees for full isolation:

```bash
# Machine 1 (Account 1)
cd project-alpha  # Worktree for zone alpha

# Machine 2 (Account 2)
cd project-beta   # Worktree for zone beta

# Machine 3 (Account 3)
cd project-gamma  # Worktree for zone gamma
```

Each machine has:
- Own account
- Own worktree
- Zone-specific files
- No possible collision

---

## Configuration Per Environment

Each environment needs:

```
~/.claude/
├── CLAUDE.md          # Account-specific preferences
├── credentials.json   # Account credentials
└── settings.json      # Account settings
```

**Never share**:
- credentials.json
- session tokens
- API keys

**Do share** (via repo):
- CLAUDE.md (project context)
- Handoff documents
- Zone ledgers

---

## Monitoring

Track which account is working where:

```markdown
# In handoff document

## Session Info
- Account: Account 2
- Zone: Beta
- Rate limit status: Fresh (reset 14:00 UTC)
```

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Same-device switching | Documented bugs | Separate machines/VMs |
| Sharing credentials | Security risk | Isolated credential stores |
| No handoff before switch | Lost context | Always commit before failover |
| Relying on memory export | Unreliable | Use file-based context |

---

## Quick Reference

1. **Don't** use CLAUDE_CONFIG_DIR on same device
2. **Do** use separate machines/VMs/containers
3. **Always** commit handoff before switching
4. **Route** large-context to Gemini when rate-limited
5. **Combine** with worktrees for full isolation

---

## Cross-References

- [[SYNTHESIS-cross_platform_patterns]] → Multi-account architecture
- [[MECH-git_worktree_coordination]] → Worktree setup
- [[PRAC-oracle_to_executor_handoff]] → Context portability
