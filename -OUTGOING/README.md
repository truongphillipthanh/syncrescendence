# -OUTGOING: CLI-to-WebApp Prompt Staging

**Purpose**: CLI agents create prompt files here for the Sovereign to dispatch to web app platforms (Vizier, Vanguard, Diviner, Oracle, Augur).

---

## Architecture

```
CLI Agent completes work
     │
     ▼
Writes PROMPT-{TARGET}-{date}-{topic}.md to -OUTGOING/
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

| Target | Platform | When To Use |
|--------|----------|-------------|
| VIZIER | Claude Web | Synthesis, ideation, interpretation |
| VANGUARD | ChatGPT Web | Compilation, formatting, Canvas work |
| DIVINER | Gemini Web | Multimodal digestion, TTS, Drive sync |
| ORACLE | Grok Web | Cultural sensing, X firehose, red-teaming |
| AUGUR | Perplexity | Fact-checking, citation-backed research |

## Flow

This is the **reverse** of -INBOX:
- **-INBOX**: tasks flow INTO CLI agents
- **-OUTGOING**: prompts flow OUT to web apps via the Sovereign

Once Linear and Slack are onboarded, this manual relay becomes automated via MCP integrations.
