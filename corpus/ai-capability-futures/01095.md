# Extraction: SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned

**Source**: `SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned.md`
**Atoms extracted**: 15
**Categories**: claim, praxis_hook

---

## Claim (1)

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0005
**Lines**: 36-38
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.70

> Claude can be used for codebase onboarding by allowing engineers to ask 'why does this work this way?' and having it search git history and code for answers, significantly reducing onboarding time.

## Praxis Hook (14)

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0001
**Lines**: 15-17
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Use simple markdown files (CLAUDE.md) to provide Claude with project context, including bash commands, code style, and testing patterns, as Claude loads them automatically.

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0002
**Lines**: 20-23
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Employ an 'explore-plan-code' workflow where Claude first reads files, then creates a plan (using 'think' for deeper reasoning), and only then implements the code, as this significantly improves quality.

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0003
**Lines**: 26-28
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Utilize test-driven development (TDD) with Claude by writing and committing tests, then letting Claude implement the code until all tests pass, which helps maintain its focus.

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0004
**Lines**: 31-33
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Use ESC to interrupt Claude and double ESC to edit previous prompts, saving time when Claude is going in the wrong direction.

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0006
**Lines**: 41-45
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> For automation, use Claude's headless mode (claude -p) for tasks like PR labeling and subjective code review, or use --dangerously-skip-permissions within an isolated container for linting or boilerplate generation.

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0007
**Lines**: 48-50
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Implement a multi-Claude workflow where one Claude writes code and another reviews it, or use git worktrees for parallel Claude sessions on different features.

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0008
**Lines**: 53-55
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Seed every repository with a tuned CLAUDE.md file, which Claude pulls into every prompt; use '#' in-session to append live notes, add 'IMPORTANT / YOU MUST' for stronger adherence, and run '/init' to scaffold one instantly.

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0009
**Lines**: 56-57
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Escalate Claude's reasoning on demand by inserting 'think' → 'think hard' → 'think harder' → 'ultrathink' to unlock larger thinking budgets before it acts.

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0010
**Lines**: 58-59
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Stop or rewind Claude in one keystroke: Esc halts any phase without losing context, and double-Esc allows editing an earlier prompt to branch a new path.

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0011
**Lines**: 60-61
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.30, actionability=0.90, epistemic_stability=0.70

> Achieve bullet-proof autonomy with Safe YOLO by running 'claude dangerously-skip-permissions' only inside an isolated container (without internet access) to allow Claude to mass-fix lint errors or boilerplate unattended.

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0012
**Lines**: 62-63
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Utilize CLAUDE.md hierarchy, supporting root, parent, child, or ~/.claude locations, so monorepos automatically inherit both global and per-package guidance.

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0013
**Lines**: 64-65
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Use one-word tool whitelisting, such as '/allowed-tools Edit Bash(git commit:*)', to remove future permission prompts for trusted actions.

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0014
**Lines**: 66-67
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.60

> Turbo-charge context with images by pasting screenshots or providing file paths, allowing Claude to visually compare mockups vs. output and iterate UI until pixels match.

### ATOM-SOURCE-20250421-x-thread-alexalbert-we_wrote_up_what_weve_learned-0015
**Lines**: 68-68
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Use the gh CLI as a super-power, as Claude speaks gh fluently and can draft PRs, fix review comments, triage issues, and write commit messages that cite history.
