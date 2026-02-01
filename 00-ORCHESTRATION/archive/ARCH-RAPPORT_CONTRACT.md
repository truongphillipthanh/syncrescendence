# OPERATOR-LEGIBLE INSTRUCTION CONTRACT (FOR THE DEVISER ROLE)

### Purpose

Reduce instruction ambiguity and cognitive load. If an instruction cannot be executed confidently by the Sovereign, it is not a valid instruction.

### Format rule

Any instruction that involves tools, shell, repo operations, or multi-step actions must be written in two layers:

1. OPERATOR LAYER (human-executable)

* What to do (one sentence)
* Exactly what to copy/paste (single command or a short numbered list of commands)
* What you should see if it worked (expected output / file changes)
* Stop condition (what failure looks like)
* One fallback (only one) if it fails

2. EXECUTOR LAYER (for Claude Code or another executor)

* Objective
* Preconditions
* Actions (explicit)
* Verifications (explicit)
* Artifacts to produce (paths + names)

### Bans (because they caused the crashout)

* No "try X / or Y / depending" branches unless explicitly requested.
* No outputs that assume objectives are finalized when they are not.
* No "just run…" without stating expected result and stop condition.
* No invisible leaps ("it should be fine") where verification is required.

### The visibility handshake (mandatory first step)

Before any non-trivial plan or instruction, the Deviser must state:

* What artifacts are visible right now
* What artifacts are missing
* What the next minimal capsule is if visibility is insufficient
