# Extraction: SOURCE-undated-001

**Source**: `SOURCE-20260220-website-article-agents-agents_md_simple_open_format_guiding.md`
**Atoms extracted**: 17
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (7)

### ATOM-SOURCE-undated-001-0002
**Lines**: 3-3
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> AGENTS.md is used by over 60,000 open-source projects.

### ATOM-SOURCE-undated-001-0004
**Lines**: 20-22
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> AGENTS.md complements README.md by containing detailed context specifically for coding agents, such as build steps, tests, and conventions, which might otherwise clutter a README or be irrelevant to human contributors.

### ATOM-SOURCE-undated-001-0006
**Lines**: 33-60
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> AGENTS.md is compatible with a growing ecosystem of AI coding agents and tools, including Gemini CLI, Autopilot & Coded Agents, Semgrep, Factory, RooCode, Jules, Devin, Codex, Zed, goose, Warp, Cursor, Aider, Ona, Windsurf, opencode, Coding agent (GitHub Copilot), Kilo Code, Amp, Phoenix, and VS Code.

### ATOM-SOURCE-undated-001-0012
**Lines**: 115-116
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> AGENTS.md is standard Markdown and does not have required fields; agents parse the text provided under any headings.

### ATOM-SOURCE-undated-001-0013
**Lines**: 117-118
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> If instructions conflict, the AGENTS.md file closest to the edited file takes precedence, and explicit user chat prompts override everything.

### ATOM-SOURCE-undated-001-0015
**Lines**: 119-120
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.60, actionability=0.60, epistemic_stability=0.80

> If testing commands are listed in AGENTS.md, agents will attempt to execute relevant programmatic checks and fix failures before completing a task.

### ATOM-SOURCE-undated-001-0016
**Lines**: 121-121
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.90

> AGENTS.md should be treated as living documentation and can be updated later.

## Concept (2)

### ATOM-SOURCE-undated-001-0001
**Lines**: 3-6
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> AGENTS.md is an open format designed to guide coding agents, serving as a 'README for agents' by providing context and instructions for AI coding agents to work on a project.

### ATOM-SOURCE-undated-001-0003
**Lines**: 19-19
**Context**: consensus / claim
**Tension**: novelty=0.00, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.00, actionability=0.10, epistemic_stability=0.90

> README.md files are intended for human users, providing quick starts, project descriptions, and contribution guidelines.

## Framework (1)

### ATOM-SOURCE-undated-001-0005
**Lines**: 24-27
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.60, actionability=0.60, epistemic_stability=0.80

> The AGENTS.md format is intentionally separated from README.md to provide agents with a clear, predictable instruction location, keep READMEs concise for human contributors, and offer precise, agent-focused guidance that complements existing documentation.

## Praxis Hook (7)

### ATOM-SOURCE-undated-001-0007
**Lines**: 95-102
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To use AGENTS.md, create an AGENTS.md file at the root of the repository, add sections covering project overview, build/test commands, code style, testing instructions, and security considerations, and include extra instructions like commit messages or PR guidelines.

### ATOM-SOURCE-undated-001-0008
**Lines**: 103-105
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> For large monorepos, use nested AGENTS.md files for subprojects; agents automatically read the nearest file in the directory tree, giving precedence to the closest one.

### ATOM-SOURCE-undated-001-0009
**Lines**: 103-104
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To resolve conflicting instructions, the AGENTS.md file closest to the edited file takes precedence, and explicit user chat prompts override all other instructions.

### ATOM-SOURCE-undated-001-0010
**Lines**: 106-107
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.60, actionability=0.90, epistemic_stability=0.80

> Agents will automatically run testing commands listed in AGENTS.md, attempting to execute relevant programmatic checks and fix failures before completing a task.

### ATOM-SOURCE-undated-001-0011
**Lines**: 112-113
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To migrate existing documentation to AGENTS.md, rename the existing file to AGENTS.md and create a symbolic link for backward compatibility using the command: `mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md`.

### ATOM-SOURCE-undated-001-0014
**Lines**: 117-118
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To configure Aider to use AGENTS.md, add `read: AGENTS.md` to the `.aider.conf.yml` file.

### ATOM-SOURCE-undated-001-0017
**Lines**: 121-122
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To configure Gemini CLI to use AGENTS.md, set `"contextFileName": "AGENTS.md"` in the `.gemini/settings.json` file.
