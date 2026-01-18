# COCKPIT CONTRACT: Claude
## Operational Template for Claude Surfaces

**Platform**: Claude (Anthropic)
**Surfaces**: Web app (claude.ai), Claude Code CLI, Claude Desktop, API
**Version**: 1.0

---

## TELEOLOGY (Why This Platform Exists)

Claude serves **dual roles** in the Syncrescendence architecture:

**Claude Web App = ORACLE**
- Strategic synthesis sessions (numbered Oracles)
- Comprehensive directive generation
- Long-form analysis with extended thinking
- Artifact creation for download

**Claude Code CLI = EXECUTOR**
- Primary execution engine
- Filesystem sovereignty
- Sub-agent orchestration
- Verification and logging

**Not for**: Corpus-scale RAG (use Gemini), video processing (use Gemini), citation research (use Perplexity).

---

## ALLOWED ACTIONS

### Claude Web App (Oracle)
| Action | Context | Output |
|--------|---------|--------|
| Strategic synthesis | Oracle sessions | Comprehensive directives |
| Directive generation | After Oracle synthesis | DIRECTIVE-XXX.md packages |
| Long-form analysis | Complex problems | Structured analysis documents |
| Extended thinking | Architecture decisions | Deep reasoning artifacts |
| Artifact creation | For download | Files in /outputs |

### Claude Code CLI (Executor)
| Action | Context | Output |
|--------|---------|--------|
| File operations | Executing directives | Created/modified files |
| Sub-agent spawning | Parallel work | Background agents |
| Verification | Before claiming done | Command outputs |
| Git operations | Persistence | Commits |
| MCP tool usage | External systems | Tool results |

---

## FORBIDDEN ACTIONS

### Claude Web App
| Action | Why Forbidden | Alternative |
|--------|---------------|-------------|
| Claim to modify files | Web app can't touch filesystem | Use Claude Code |
| Hold execution state | Web is for synthesis | Export to Claude Code |
| Skip artifact export | State orphaned in chat | Always create artifact |

### Claude Code CLI
| Action | Why Forbidden | Alternative |
|--------|---------------|-------------|
| Claim done without verification | Unverified = unreal | Run verification commands |
| Skip commits | Unpersisted = lost | Commit after changes |
| Ignore CLAUDE.md | Constitutional violations | Always load CLAUDE.md |
| Create subdirectories | Flat Principle violation | Use naming prefixes |

---

## MEMORY POLICY

### Claude Web App (Projects)
- Project: Syncrescendence
- Project Knowledge: Load key documents
- Memory: Enabled (cross-conversation context)
- Extended Thinking: Enabled for complex analysis

### Claude Code (CLAUDE.md)
- Location: Repository root
- Content: Constitutional rules, anti-patterns, commands
- Loaded: Automatically at session start
- Updates: Via Principal approval

### Memory Hierarchy
1. Enterprise (if applicable) > 2. Project > 3. User > 4. Local CLAUDE.md

---

## PACKET POLICY

### Claude Web (Incoming)
| Packet Type | When | Content |
|-------------|------|---------|
| Evidence Packet | From Gemini sensing | Findings for synthesis |
| Audit Packet | From ChatGPT review | Issues to address |

### Claude Web (Outgoing)
| Packet Type | When | Destination |
|-------------|------|-------------|
| Oracle Context | After synthesis | Download → repo |
| Directive Package | After planning | Download → repo → Claude Code |
| Artifact | After creation | Download → repo |

### Claude Code (Incoming)
| Packet Type | When | Content |
|-------------|------|---------|
| Directive | From Oracle | Execution instructions |
| Plan Packet | From ChatGPT | Acceptance criteria |

### Claude Code (Outgoing)
| Packet Type | When | Destination |
|-------------|------|-------------|
| Execution Packet | After work | Repo (blackboard) |
| Continuation Artifact | Session end | Repo (for next session) |
| Commit | After changes | Git |

---

## INITIALIZATION BLOCK: CLAUDE WEB

Paste this at the start of Oracle sessions:

```
ROLE: ORACLE (Strategic Synthesis) in Syncrescendence architecture

CONTEXT:
- This is Oracle session #[NUMBER]
- Repository: Syncrescendence (00-ORCHESTRATION through 06-EXEMPLA)
- Principal: Human sovereign with AuDHD cognitive profile
- Previous Oracle: [SUMMARY]

CURRENT STATE:
[Paste relevant context here]

OBJECTIVE:
[State session objective here]

YOUR OUTPUTS:
- ORACLE[N]_CONTEXT.md (session context)
- DIRECTIVE-[NNN]A.md and DIRECTIVE-[NNN]B.md (parallel execution)
- Artifacts in /outputs for download

PROTOCOL:
1. Synthesize comprehensively
2. Generate directives for Claude Code execution
3. Create downloadable artifacts
4. End with graduation checklist

Begin by confirming the session objective.
```

---

## INITIALIZATION: CLAUDE CODE

Claude Code loads CLAUDE.md automatically. For continuation:

```bash
# Resume from specific session
claude --continue [session-id]

# Load context file
claude --context 00-ORCHESTRATION/ORACLE13_CONTEXT.md

# Start with specific directive
claude "Execute DIRECTIVE-046A. Read the file first, then proceed phase by phase."
```

---

## WHEN CONFUSED: ESCALATION RULE

### Claude Web
If confused, ask:
1. "What is the primary output of this Oracle session?"
2. "Should this be a directive for Claude Code, or resolved here?"
3. "What context am I missing?"

### Claude Code
If confused, ask:
1. "Should I read a file before proceeding?"
2. "What verification proves this is done?"
3. "Does this require Principal approval (protected zone)?"

**Never guess. Always ask.**

---

## SESSION END CHECKLIST

### Claude Web App
- [ ] All artifacts created in /outputs
- [ ] Artifacts ready for download
- [ ] Directives complete with success criteria
- [ ] Context document for next Oracle
- [ ] "Graduation complete" confirmed

### Claude Code
- [ ] All changes committed
- [ ] Verification commands run with evidence
- [ ] State vector updated
- [ ] Events logged
- [ ] Continuation artifact created
- [ ] "Safe to delete" or "NOT safe" stated

---

## ACCOUNT CONFIGURATION

### Claude Web App
| Setting | Value |
|---------|-------|
| Project | Syncrescendence |
| Project Knowledge | Key CANON, coordination.yaml, CLAUDE.md |
| Memory | Enabled |
| Extended Thinking | Enabled |
| Default Model | Opus for Oracle, Sonnet for routine |

### Claude Code CLI
| Setting | Value |
|---------|-------|
| CLAUDE.md | Repository root, auto-loaded |
| Model | Opus for architectural, Sonnet for execution |
| Thinking | ultrathink for complex, megathink for moderate, think for standard |
| Permissions | Use allowlists, not --dangerously-skip-permissions |

---

**Claude is the core. Web for synthesis, Code for execution. Never confuse them.**
