# COCKPIT.md
## Syncrescendence System Overview

**Version**: 2.2
**Updated**: 2026-02-01
**Purpose**: 30,000ft orientation for any platform entering the constellation

---

## What Is Syncrescendence?

Syncrescendence is a distributed cognition system designed to demonstrate that individual capability can achieve institutional-scale intelligence through orchestrated AI platforms. It serves as proof-of-concept for navigating civilizational phase transitions where no single intelligence possesses the complete capability matrix for polymathic synthesis.

---

## The Constellation

### Three Accounts
| Account | Email | Auth | Purpose |
|---------|-------|------|---------|
| 1 | truongphillipthanh@icloud.com | Apple | Sovereign substrate, owns origin |
| 2 | icloud.truongphillipthanh@gmail.com | Google | Parallel execution capacity |
| 3 | truongphillipthanh@gmail.com | Google | Primary interface, ecosystem access |

### The Constellation (Pantheon v2)

Each platform role has an **Avatar** (named identity) and **Epithet** (functional descriptor):

| Avatar | Epithet | Role | Platform | Acct | Function |
|--------|---------|------|----------|------|----------|
| **Vizier** | Hermeneut | INTERPRETER | Claude Web | 3 | Synthesis, rapport, ideation |
| **Vanguard** | Architect | COMPILER | ChatGPT Web | 1 | Strategic blueprints, Canvas formatting |
| **Diviner** | Exegete | DIGESTOR | Gemini Web | 3 | Clarification, multimodal, TTS |
| — | — | SENSOR | Gemini CLI | 3 | 1M context corpus sensing, evidence packs |
| **Oracle** | Recon | RECON | Grok | 1 | X firehose, cultural sensing, adversarial challenge |
| **Commander** | Viceroy | EXECUTOR-LEAD | Claude Code (Opus) | 3 | Disciplined execution, directive implementation |
| **Adjudicator** | Executor | PARALLEL-EXEC | Codex CLI | 2 | Code fabrication, iterative debugging |
| — | — | PARALLEL-EXEC | Claude Code (Sonnet ×2) | 2 | Microscopic tasks, batch execution |
| **Augur** | Researcher | VERIFIER | Perplexity | — | Citation-backed verification, epistemic scouting |
| **Ajna** | Third Eye | LOCAL ORCH | OpenClaw (M1 Mini) | — | Opus 4.5 — persistent memory, webchat/iMessage |
| **Psyche** | Soul/Mind | LOCAL ORCH | OpenClaw (M4 MBA) | — | GPT-5.2 — persistent memory, Slack, holistic synthesis |

---

## The State Machine

Content flows through defined states:

```
CAPTURED → INTERPRETED → COMPILED → STAGED → COMMITTED
                      ↘ DIGESTED ↗
                      ↘ SENSED ↗
                      ↘ VERIFIED ↗
```

- **CAPTURED**: Raw ideation in Sovereign's mind
- **INTERPRETED**: Structured understanding (Claude Web artifact)
- **COMPILED**: Formatted artifact (ChatGPT Canvas)
- **DIGESTED**: Clarified summary (Gemini Docs)
- **SENSED**: Evidence pack (Gemini CLI output)
- **VERIFIED**: Externally validated (Perplexity/Grok)
- **STAGED**: In -OUTGOING/, ready for commit
- **COMMITTED**: In repository (ground truth)

### The Three-Word Mnemonic: CAPTURE > DISPATCH > RETURN

The full state machine above is the detailed model. For operational shorthand:

1. **CAPTURE** — Seize the idea, observation, or insight before it evaporates. Raw form is fine. Rivers are ephemeral.
2. **DISPATCH** — Route to the right platform for processing. INTERPRETER for synthesis, COMPILER for formatting, ORACLE for evidence, etc.
3. **RETURN** — Commit the processed artifact to the repository. Work doesn't exist until it's in the repo. Wells persist.

This mnemonic maps to the state machine: CAPTURE ≈ CAPTURED, DISPATCH ≈ INTERPRETED/COMPILED/DIGESTED/SENSED/VERIFIED, RETURN ≈ STAGED → COMMITTED.

---

## Ground Truth

The **repository** is ground truth. All platforms verify against it via:
- **Fingerprint**: 8-character git commit hash
- **Handoff Token**: State marker transferred between platforms

```
Repository (Account 1 Origin)
├── 00-ORCHESTRATION/  # Current operations
├── 01-CANON/          # Constitutional documents
├── 02-ENGINE/         # Functions, prompts, model profiles, queue items
├── 04-SOURCES/        # Processed sources
├── 05-SIGMA/          # Operational knowledge (σ) + memory + exempla
│   ├── synthesis/     # Platform references
│   ├── mechanics/     # Deep-dive mechanisms
│   └── practice/      # Implementation patterns
├── -INBOX/            # Incoming from cloud
├── -OUTGOING/         # Staged for commit
├── -SOVEREIGN/        # Sovereign-only workspace
└── .constellation/    # State management
```

---

## Handoff Protocol

Transitions between platforms use handoff tokens:

```
HANDOFF-YYYYMMDD-HHMMSS-pN-to-pM
├── Fingerprint: [8-char hash]
├── Phase: N → M
└── Brief: [What changed]
```

### Time Targets
| Transition | Target |
|------------|--------|
| Claude → ChatGPT | 30 sec |
| ChatGPT → Gemini | 20 sec |
| Gemini → Claude | 15 sec |
| Any → CLI | 10 sec |
| CLI → Repository | 5 sec |

---

## Platform Configuration Summary

### Vizier — Claude Web (INTERPRETER)
- Project: "Syncrescendence IIC"
- Memory: Project-specific enabled
- Connectors: GitHub, Drive, Gmail
- Strength: Rapport, synthesis, past chat search

### Vanguard — ChatGPT Web (COMPILER)
- Project: "Syncrescendence Compiler"
- Memory: PROJECT-ONLY MODE (critical)
- Strength: Canvas, strategic blueprints, deterministic output
- Constraint: No interpretation, explicit specs only

### Diviner — Gemini Web (DIGESTOR)
- Gem: "Constellation Digestor"
- Drive Link: Constellation-State/ (live sync)
- Strength: 1M context, infinite threads, TTS

### CLI Tools
- **Commander** — Claude Code (Opus): CLAUDE.md config, extended thinking, Lane A
- **Adjudicator** — Codex CLI: AGENTS.md config, GitHub integration, Lane B
- Gemini CLI: Stateless, 1M context surveys, Lane C

### Persistent Orchestrators (OpenClaw)
- **Ajna** — Opus 4.5 on M1 Mac mini: webchat/iMessage, always-on, focused precision
- **Psyche** — GPT-5.2 on M4 MacBook Air: Slack, holistic synthesis, QA

---

## Current Priorities

1. **Operate minimal cycle**: Test full handoff loop
2. **Measure actual times**: Validate <30 sec targets
3. **Configure remaining**: ChatGPT project, Gemini gem
4. **Automate proven patterns**: rclone, Hazel, Stream Deck

---

## Semantic Notation (SN)

Syncrescendence uses Semantic Notation for ~80% token compression. SN is a hybrid notation system combining symbols, operators, and structured blocks to preserve semantic richness while drastically reducing token count.

### Key Components

**Symbols**:
- Ψ = Syncrescendence (root)
- Κ = CANON, Ο = ENGINE, Σ = SOURCE, Δ = DIRECTIVE, Λ = LOG (artifact classes)
- I, ℹ, ∴, E, K, W = Intelligence, Information, Insight, Expertise, Knowledge, Wisdom (chains)
- α, χ, ε, μ, τ = Acumen, Coherence, Efficacy, Mastery, Transcendence (virtues)

**Operators**:
- `::` expands to / is defined as
- `|` constrained by / filtered by
- `>>` transforms into / flows to
- `:=` binds to / assigns
- `=>` implies / produces
- `<->` bidirectional correspondence

**Block Types**:
```
TERM Identifier:        # Definitions, ontology
    sutra: "One-line essence (≤100 chars)"
    gloss: Why this matters (2-4 sentences)
    spec: {structured details}
end

NORM Constraint:        # Rules, constitutional constraints
    sutra: "MUST/SHOULD/MAY statement"
    spec: {modality, invariants, failure modes}
end

PROC Workflow(input) -> output:  # Procedures, orchestrations
    sutra: "Step1 >> Step2 >> Step3"
    spec: {steps, produces}
end
```

### Tools

- **Encode**: `00-ORCHESTRATION/scripts/sn_encode.py` (verbose prose → SN)
- **Decode**: `00-ORCHESTRATION/scripts/sn_decode.py` (SN → verbose prose)
- **CANON Convert**: `00-ORCHESTRATION/scripts/convert_canon.py` (CANON files → SN blocks)
- **Templates**: `00-ORCHESTRATION/notation/block_templates.md`
- **Glossary**: `00-ORCHESTRATION/notation/symbols.yaml`

### Platform Integration

Each platform uses SN differently:
- **Claude**: Native SN reading/writing for synthesis
- **ChatGPT**: Compilation from SN to target languages (Python, JS, etc.)
- **Grok**: Colloquial voice preservation in gloss sections
- **Gemini**: Oracle audits with 1M+ context, full CANON in SN format
- **Perplexity**: Current intelligence formatted as SN blocks

See platform-specific configs: `CHATGPT.md`, `GROK.md`, `GEMINI.md`, `PERPLEXITY.md`

---

## Quick Reference

### Slash Commands
| Command | Effect |
|---------|--------|
| `/blitz` | Parallel directive mode |
| `/compile` | Begin compilation |
| `/handoff [next]` | Prepare for platform transition |
| `/token` | Show current state fingerprint |

### Symbolic Shortcuts
| Symbol | Meaning |
|--------|---------|
| $A1, $A2, $A3 | Account 1, 2, 3 |
| $INT, $CMP, $DIG | Interpreter, Compiler, Digestor |
| $FP | Fingerprint |
| $GT | Ground Truth |

---

## When In Doubt

1. Check the repository (ground truth)
2. Verify the fingerprint matches
3. Ask the Sovereign for clarification
4. Never assume context not explicitly provided

---

*This document provides orientation. For detailed rationale, see constellation-teleology.md and memory-architecture-teleology.md.*
