# Extraction: SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr

**Source**: `SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr.md`
**Atoms extracted**: 16
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (9)

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0001
**Lines**: 8-12
**Context**: anecdote / evidence
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.80

> YOLO mode, which grants an agent all permissions, did not work well with Claude Code's plan mode initially because plan mode did not inherit all tool permissions and frequently requested approval.

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0003
**Lines**: 22-25
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.10, epistemic_stability=0.70

> Mario's 'pi' agent does not feature a plan mode, and Amp is in the process of removing theirs, suggesting a trend away from this feature in some agent implementations.

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0005
**Lines**: 40-45
**Context**: method / evidence
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Claude Code's plan mode includes recurring prompts to remind the agent it is in read-only mode, even though file writing tools remain available, and the agent seemingly edits its own plan file using the edit file tool.

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0006
**Lines**: 49-51
**Context**: method / evidence
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Entering plan mode in Claude Code injects a custom prompt to encourage the agent to write the plan file, but there is no other enforcement mechanism.

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0007
**Lines**: 53-55
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> Upon exiting plan mode, Claude Code reads the plan file from disk and then proceeds to execute based on that plan, meaning the specification path always involves the file system.

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0011
**Lines**: 102-105
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.80

> The behavior of tools in Claude Code's plan mode is primarily influenced by prompt reinforcement, rather than the tools themselves becoming read-only.

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0013
**Lines**: 110-111
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.70

> The Claude plan mode system prompt is essentially the same as a regular prompt, with additional verbiage and UX elements.

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0014
**Lines**: 115-118
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.20, speculation_risk=0.40, actionability=0.20, epistemic_stability=0.50

> The author's limited testing suggests no significant difference in how plan mode invokes tools compared to regular execution, possibly due to their prompting styles.

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0016
**Lines**: 127-129
**Context**: anecdote / claim
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.30, actionability=0.20, epistemic_stability=0.50

> The author finds Claude's plan mode unnatural because it requires switching UI modes instead of allowing direct planning with the model.

## Concept (2)

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0004
**Lines**: 35-38
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.10, actionability=0.10, epistemic_stability=0.90

> In Claude Code, a 'plan' is defined as a markdown file written by Claude into its 'plans' folder while in plan mode, lacking any structure beyond plain text.

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0015
**Lines**: 123-125
**Context**: hypothesis / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.50, actionability=0.20, epistemic_stability=0.60

> A key question in agentic tools is whether user experience should be enforced by the system harness or emerge naturally from the model.

## Framework (1)

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0008
**Lines**: 80-100
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.70

> Claude Code's plan mode workflow is structured into four phases: Phase 1 (Initial Understanding) for comprehending the request and code, Phase 2 (Design) for developing an implementation approach, Phase 3 (Review) for aligning plans with user intentions, and Phase 4 (Final Plan) for writing the concise, detailed plan to the plan file.

## Praxis Hook (4)

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0002
**Lines**: 14-20
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> An alternative approach to agent plan mode involves iterating with the agent to create a handoff in a markdown file, where the agent asks clarifying questions, which are then answered in an editor through multiple iterations.

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0009
**Lines**: 90-96
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To use the planning tool, first write your plan to the specified plan file, then use the tool to signal completion for user review and approval.

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0010
**Lines**: 100-103
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Only use the planning tool for tasks requiring planning implementation steps for code writing; do not use it for research, information gathering, or file operations.

### ATOM-SOURCE-20250217-website-article-unknown-what_actually_is_claude_code_s_plan_mode_lucumr-0012
**Lines**: 107-108
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> Before using the planning tool, ensure your plan is clear and unambiguous, addressing any multiple valid approaches or unclear requirements.
