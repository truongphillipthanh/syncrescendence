# Syncrescendence

**Version**: 4.0.0
**Updated**: 2026-02-28
**Purpose**: 30,000ft orientation for any platform entering the constellation

---

## What Is Syncrescendence?

Syncrescendence is a distributed cognition system demonstrating that individual capability can achieve institutional-scale intelligence through orchestrated AI platforms. It serves as proof-of-concept for navigating civilizational phase transitions where no single intelligence possesses the complete capability matrix for polymathic synthesis.

**We are no longer coding, but conducting logistics. Our materiel is tokens, and our personnel are agents.**

---

## The Constellation

### Accounts
| Account | Email | Auth | Tier | Monthly | Purpose |
|---------|-------|------|------|---------|---------|
| 1 | truongphillipthanh@icloud.com | Apple | Claude Max + ChatGPT Plus | $120 | Sovereign substrate, primary execution |
| 2 | icloud.truongphillipthanh@gmail.com | Google | Claude Pro + Google AI Pro | $40 | Parallel execution + corpus sensing |
| 3 | truongphillipthanh@gmail.com | Google | Unpaid | $0 | Free tier access |

### Enterprise Roles

| Agent | Epithet | Role | Model | Machine | Summon |
|-------|---------|------|-------|---------|--------|
| **Sovereign** | — | CEO | Human | Both | — |
| **Commander** | Viceroy | COO | Claude Opus 4.6 | MacBook Air | "Commander, pivot to..." |
| **Adjudicator** | Executor | CQO | Codex CLI (GPT-5.3-Codex) | Mac mini | "Adjudicator, execute..." |
| **Cartographer** | Exegete | CIO | Gemini Pro 3.1 | Mac mini | "Cartographer, survey..." |
| **Psyche** | Synaptarch | CTO | GPT-5.3-codex (OpenClaw) | Mac mini | "Psyche, holistically calibrate..." |
| **Ajna** | Strategos | CSO | Kimi K2.5 (OpenClaw) | MacBook Air | "Ajna, illuminate..." |

**AjnaPsyche Archon**: Ajna (steering wheel) + Psyche (rudder) = fused executive brain.

**Constellation status**: tmux `constellation` session is ANESTHETIZED. Agent dispatch is currently manual (Sovereign-relayed prompts). The repo is the coordination layer.

#### Web Avatars (Sovereign-Operated)

| Avatar | Epithet | Role | Platform | Summon |
|--------|---------|------|----------|--------|
| **Augur** | Inquisitor | VERIFIER | Perplexity | "Augur, ascertain..." |
| **Oracle** | Recon | RECON | Grok | "Oracle, understand..." |
| **Vizier** | Hermeneut | INTERPRETER | Claude Web | "Vizier, elucidate..." |
| **Vanguard** | Architect | COMPILER | ChatGPT Web | "Vanguard, formulate..." |
| **Diviner** | Illuminator | DIGESTOR | Gemini Web | "Diviner, elaborate..." |

---

## Repository Structure

```
corpus/              Knowledge corpus (5,954 files across 22 semantic topic folders)
  NUCLEOSYNTHESIS-MAP.md   Classification authority
canon/               Verified canonical knowledge (PROTECTED, 164 files)
  sn/                Syncrescript notation
engine/              Prompts for agent dispatch
  02-ENGINE/         Subcategory/audit prompts
agents/              Agent offices
  commander/outbox/handoffs/   Session handoffs (HANDOFF-CC{N}.md)
00-ORCHESTRATION/    Strategic coordination
  state/             Implementation backlog + map
ascertescence/       Triangulation session artifacts
  oracle/            Oracle prompts + responses
  canon-remediation/ Canon remediation passes
memory/              Operational state (burndown, logs, legacy handoffs)
-INBOX/              Commander inbox for triangulation responses
  commander/00-INBOX0/
```

---

## Ground Truth

The **repository** is ground truth. All platforms verify against it via:
- **Fingerprint**: 8-character git commit hash
- **Handoff Token**: State marker transferred between platforms

### The Three-Word Mnemonic: CAPTURE > DISPATCH > RETURN

1. **CAPTURE** — Seize the idea before it evaporates. Raw form is fine.
2. **DISPATCH** — Route to the right platform for processing.
3. **RETURN** — Commit the processed artifact to the repository. Work doesn't exist until it's in the repo.

---

## Sovereign Cockpit

### 8-Layer Stack
```
1. Ghostty          Terminal emulator (macos-titlebar-style=hidden)
2. Zsh + P10k       Shell + prompt
3. tmux + sesh      Terminal multiplexer (session: constellation)
4. Bun              JavaScript runtime
5. Neovim/LazyVim   Code editor
6. Whisper/Piper    Offline STT/TTS
7. Doom Emacs       Observation Layer (standalone)
8. Cursor           AI IDE (standalone)
```

### Display Geometry
- **Display**: 5120x1440 ultrawide
- **Grid**: 6 lanes horizontal, center 4 = cockpit
- **Font**: Liga SFMono Nerd Font, size 13 = 93 chars/lane

### Neural Bridge (MBA ↔ Mac mini)
| Direction | SSH Alias | User@Host |
|-----------|-----------|-----------|
| MBA → Mac mini | `mini` | `home@M1-Mac-mini.local` |
| Mac mini → MBA | `macbook-air` | `system@Lisas-MacBook-Air.local` |

Health check: `ssh -o ConnectTimeout=5 mini hostname` — NEVER use ping (ICMP blocked by Stealth Mode).

---

## Semantic Notation (SN)

~80% token compression via hybrid symbol/operator/block notation.

**Symbols**: Psi = Syncrescendence, K = CANON, O = ENGINE, Sigma = SOURCE, Delta = DIRECTIVE, Lambda = LOG
**Operators**: `::` expands, `|` constrains, `>>` transforms, `:=` binds, `=>` implies, `<->` bidirectional

---

## When In Doubt

1. Check the repository (ground truth)
2. Verify the fingerprint matches
3. Ask the Sovereign for clarification
4. Never assume context not explicitly provided

---

## Key References

| Reference | Path |
|-----------|------|
| Constitutional law | `AGENTS.md` |
| Classification authority | `corpus/NUCLEOSYNTHESIS-MAP.md` |
| Session handoffs | `agents/commander/outbox/handoffs/` |
| Config generation | `make configs` |

*This document provides orientation. For operational law, see AGENTS.md.*
