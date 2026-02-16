# GitHub Connector Protocol

## Purpose
All three web applications (Claude, ChatGPT, Gemini) can sense directly into this repository via GitHub connectors. This document defines the protocol for that access.

## Capabilities

### Read Access
- All platforms can read any file in the repository
- Connector provides directory listings and file contents
- Token limits apply per-platform:
  - Claude Web: ~200K tokens/session
  - ChatGPT Web: ~128K tokens/session
  - Gemini Web: ~2M tokens/session (Flash 2.0)

### Write Access
- **Claude Web**: Read-only via connector; writes via Claude Code CLI
- **ChatGPT Web**: Read-only via connector; writes via Codex CLI or ChatGPT desktop app
- **Gemini Web**: Read-only via connector; writes via Gemini CLI (when available)

**Ground truth**: The `main` branch on GitHub is canonical. Local working directory may be ahead.

## Synchronization Protocol

### 1. Canonical State
The `main` branch on GitHub is the source of truth for cross-platform reads.

### 2. Platform Reads
All platforms read from `main` branch via GitHub connector:
- Claude uses GitHub connector (when available) or reads from local repo
- ChatGPT uses GitHub connector
- Gemini uses GitHub connector

### 3. Platform Writes

**Write path**:
1. Platform generates specification/directive
2. Appropriate CLI tool executes (Claude Code, Codex CLI, etc.)
3. Changes committed to local working directory
4. Push to `main` branch on GitHub
5. Other platforms refresh on next connector query

**Never**:
- Attempt direct writes via web interfaces
- Bypass git commit process
- Create conflicting branches

### 4. Conflict Resolution
If conflicts occur:
1. Pull latest from `main`
2. Resolve conflicts locally
3. Commit resolution
4. Push to `main`

## Token Economics

When traversing the corpus via connector, optimize token usage:

### Entry Points (Always Start Here)
1. `/CLAUDE.md` — Claude-specific instructions and context
2. `/CHATGPT.md` — ChatGPT-specific instructions (to be created)
3. `/GEMINI.md` — Gemini-specific instructions
4. `/COCKPIT.md` — Universal entry point and navigation hub

### Navigation Strategy
1. **Use README files**: Each major directory has a README.md for orientation
2. **Use grep/search**: Search for keywords rather than reading entire files
3. **Request line ranges**: Read specific sections, not full files
4. **Cache strategically**: Keep frequently-accessed documents in thread context

### Token Budget Guidelines

| Platform | Session Budget | Strategy |
|----------|---------------|----------|
| Claude Web | ~200K tokens | Read selectively; use grep; cache CANON docs |
| ChatGPT Web | ~128K tokens | Minimal reads; rely on CHATGPT.md summary; focused queries |
| Gemini Web | ~2M tokens | Can read extensively; still prefer targeted queries |

## Platform-Specific Notes

### Claude Web
- **Entry point**: `CLAUDE.md`
- **Primary focus**: Interpretation, specification, architectural decisions
- **Connector scope**: Full repository read access
- **Write method**: Handoff to Claude Code CLI
- **Strengths**: Deep reasoning, constitutional alignment, CANON fluency

### ChatGPT Web
- **Entry point**: `CHATGPT.md` (to be created)
- **Primary focus**: Ideation, compilation, code generation
- **Connector scope**: Full repository read access
- **Write method**: Handoff to Codex CLI or desktop app
- **Strengths**: Fast iteration, code generation, creative synthesis

### Gemini Web
- **Entry point**: `GEMINI.md`
- **Primary focus**: Digestion, oracle-scale sensing, massive context synthesis
- **Connector scope**: Full repository read access (can ingest full corpus)
- **Write method**: Handoff to Gemini CLI or human transcription
- **Strengths**: 2M token window, oracle-scale analysis, pattern detection across corpus

## Cross-Platform Workflows

### Workflow 1: Claude Interprets → ChatGPT Compiles
1. Claude reads user intent + relevant CANON
2. Claude dispatches task to `-INBOX/{agent}/`
3. Claude commits and pushes to `main`
4. ChatGPT reads directive via connector
5. ChatGPT generates implementation
6. ChatGPT outputs to `-OUTGOING/` for human handoff

### Workflow 2: Gemini Oracle Analysis → Claude Specification
1. Gemini ingests large corpus section (e.g., all 04-SOURCES)
2. Gemini identifies patterns and opportunities
3. Gemini writes oracle report to `-OUTGOING/`
4. Claude reads oracle report via connector
5. Claude writes directive based on oracle insights
6. Claude Code executes directive

### Workflow 3: Round-Robin Refinement
1. Claude drafts specification
2. ChatGPT reviews and suggests improvements
3. Gemini validates against full corpus coherence
4. Claude incorporates feedback and finalizes
5. Claude Code executes

## Connector Best Practices

### DO
- Start with entry point files (CLAUDE.md, CHATGPT.md, GEMINI.md)
- Use directory README files for orientation
- Search before reading full files
- Read line ranges when possible
- Cache constitutional documents (CANON) in context
- Commit frequently with semantic messages
- Push to `main` after each coherent unit of work

### DON'T
- Read entire files unnecessarily
- Read all CANON files at once (selective based on task)
- Attempt writes via connector (read-only)
- Create branches (single-branch workflow)
- Skip commit messages
- Forget to push after commits

## Security & Permissions

### Public Repository Considerations
This repository may be public. Connector access is governed by:
- GitHub OAuth tokens (user-specific)
- Repository visibility settings
- Platform-specific connector permissions

### Private Information
Never commit:
- API keys
- Passwords
- Personal identifying information
- Sensitive user data

Use environment variables and `.env` files (gitignored) for secrets.

## Troubleshooting

### "File not found" via Connector
- Verify file path (absolute from repo root)
- Check that file is committed and pushed to `main`
- Confirm connector is authenticated

### "Token limit exceeded"
- Use more selective reads (line ranges, grep)
- Clear context and restart with fresh session
- For Gemini: Increase window usage strategically

### "Stale data" (Connector showing old version)
- Verify latest commit is pushed to `main`
- Refresh connector (re-authenticate if needed)
- Check GitHub.com directly to confirm push succeeded

## Version History

- **v1.0.0** (2026-01-23): Initial protocol definition

---

**Status**: Canonical protocol for GitHub connector access across Claude/ChatGPT/Gemini web platforms.
