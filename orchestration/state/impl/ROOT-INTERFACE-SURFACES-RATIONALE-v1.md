# Root Interface Surfaces Rationale v1

## Purpose

Explain why the successor shell keeps certain root dotfiles and harness-facing config surfaces instead of forcing every interface concern into deeper lanes.

This is derived from predecessor roots such as:

- [syncrescendence-pre-syncrephoenix](/Users/system/Desktop/syncrescendence-pre-syncrephoenix)
- [syncrescendence-before-full](/Users/system/Desktop/syncrescendence-before-full)

Those roots carried two distinct classes of surfaces:

1. **Operator cockpit files**
   - `BOOT.md`
   - `WORK-LOOP.md`
   - `INTER-AGENT.md`
   - `CONTINUOUS-IMPROVEMENT.md`
2. **Root interface adapters**
   - `.claude/`
   - `.gemini/`
   - `.obsidian/`
   - `.github/`
   - `.gitignore`
   - `.gitattributes`
   - root harness veneers such as `CLAUDE.md` and `GEMINI.md`

## Design Rule

Root interface surfaces are allowed only when they satisfy at least one of these:

1. they are required by a native harness or platform
2. they keep the shell self-addressable from the top level
3. they expose local interface state without claiming constitutional authority
4. they reduce operator friction without creating a second truth plane

## Live Root Interface Set

The successor shell now recognizes these root interface classes:

- tracked harness veneers:
  - [CLAUDE.md](/Users/system/syncrescendence/CLAUDE.md)
  - [GEMINI.md](/Users/system/syncrescendence/GEMINI.md)
- tracked harness adapter directories:
  - [.claude](/Users/system/syncrescendence/.claude)
  - [.gemini](/Users/system/syncrescendence/.gemini)
- tracked repo configuration:
  - [.github](/Users/system/syncrescendence/.github)
  - [.gitignore](/Users/system/syncrescendence/.gitignore)
  - [.gitattributes](/Users/system/syncrescendence/.gitattributes)
- optional local interface state:
  - `.obsidian/`

## Local-State Rule

`.obsidian/` is intentionally different from `.claude/` and `.gemini/`.

- `.claude/` and `.gemini/` are thin tracked adapters because they participate directly in harness loading.
- `.obsidian/` is local interface state. It may exist at the root, but it must not be treated as canonical output or repo truth.
- if `.obsidian/` exists, it should remain gitignored except for an explicit future decision to version a minimal stable subset.

## What Does Not Return

The predecessor root also carried:

- `CLAUDE-EXT.md`
- `OPENCLAW-EXT.md`
- `GROK-EXT.md`
- `GEMINI-EXT.md`

Those do not return as independent root authorities.
Their proper successors are:

- playbooks
- validated patterns
- generated harness veneers
- operator and communication lineage

## Connection to the Config -> Ontology Cascade

The original compounding line of questioning remains the right cascade:

- scaffold consensus -> lane and shell structure
- memory architecture -> durable state, office memory, compaction
- config consensus -> constitutional source plus harness veneers
- live ledger -> communications, receipts, runtime evidence, ontology projection

Root interface surfaces exist so that cascade stays operable from native harnesses without relapsing into root clutter.
