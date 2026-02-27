# Phase Specifications

This directory contains phase-specific instructions for each step in the constellation workflow.

## Phase Index
- `phase-1-interpret.md` — Claude Web interpretation specs
- `phase-2-compile.md` — ChatGPT compilation specs
- `phase-3-digest.md` — Gemini digestion specs
- `phase-4-execute.md` — Claude Code execution specs

## Usage
Platforms reference these specs via handoff tokens. The token's `spec_reference` field points to the relevant phase spec.

## Token Flow

```
Claude Web (Interpret)
    → [HANDOFF TOKEN]
    → ChatGPT (Compile)
    → [HANDOFF TOKEN]
    → Gemini (Digest)
    → [HANDOFF TOKEN]
    → Claude Code (Execute)
    → [HANDOFF TOKEN]
    → [cycle continues]
```

## Verification

Each phase transition includes:
1. Git fingerprint (commit hash)
2. Phase transition metadata
3. Platform source/destination
4. Timestamp

Receiving platform verifies fingerprint with:
```bash
git rev-parse --short HEAD
```
