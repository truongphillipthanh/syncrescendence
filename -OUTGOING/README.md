# -OUTGOING: Web Relay Prompt Staging

**Purpose**: CLI agents create **PROMPT-*** files here for the Sovereign to dispatch to web app platforms (Vizier, Vanguard, Diviner, Oracle, Augur).

**IO Model**: v2.0 (2026-02-06)

---

## Scope (Strictly PROMPT-* Only)

As of IO Model v2, `-OUTGOING/` is **exclusively** for web relay prompts. Agent-to-agent results go directly to the destination agent's `-INBOX/{agent}/` folder.

```
WHAT GOES HERE:           WHAT DOES NOT:
  PROMPT-VIZIER-*.md        RESULT-* files (→ -INBOX/{agent}/)
  PROMPT-VANGUARD-*.md      REPORT-* files (→ 04-SOURCES/ or archive/)
  PROMPT-DIVINER-*.md       Evidence packs (→ -INBOX/{agent}/)
  PROMPT-ORACLE-*.md        Task files (→ -INBOX/{agent}/)
  PROMPT-AUGUR-*.md
```

## Architecture

```
CLI Agent completes work requiring web app follow-up
     │
     ▼
Writes PROMPT-{TARGET}-{DATE}-{TOPIC}.md to -OUTGOING/
     │
     ▼
Sovereign picks up prompt, pastes into target web app
     │
     ▼
Web app processes, Sovereign captures result to -INBOX/{originator}/
```

## Prompt File Format

```markdown
# PROMPT-{TARGET}-{YYYY-MM-DD}-{TOPIC}

**From**: {originating CLI agent}
**To**: {target web app avatar}
**Status**: PENDING | DISPATCHED | COMPLETE

## Prompt
{The actual prompt text to paste into the web app}

## Context Files
{List any files the web app should reference}

## Expected Return
{What the Sovereign should capture back}
```

## Target Avatars

| Target | Avatar | Platform | When To Use |
|--------|--------|----------|-------------|
| VIZIER | Vizier | Claude Web | Synthesis, ideation, interpretation |
| VANGUARD | Vanguard | ChatGPT Web | Compilation, formatting, Canvas work |
| DIVINER | Diviner | Gemini Web | Multimodal digestion, TTS, Drive sync |
| ORACLE | Oracle | Grok Web | Cultural sensing, X firehose, red-teaming |
| AUGUR | Augur | Perplexity | Fact-checking, citation-backed research |

## Why Not Bypass -OUTGOING?

We **do** bypass it for agent-to-agent delivery (direct inbox writes). We **keep** it for web relay because:
- Web apps lack filesystem watchers — the Sovereign must manually relay
- PROMPT-* naming convention enables automated triage (`triage_outgoing.sh`)
- Once Linear/Slack/MCP integrations are live, this folder becomes the automation surface

## Flow

```
Agent-to-Agent:  Ajna → -INBOX/psyche/     (DIRECT, no -OUTGOING)
Agent-to-Web:    Commander → -OUTGOING/     (PROMPT-* for Sovereign relay)
Web-to-Agent:    Sovereign → -INBOX/{agent}/ (captures web app output)
```
