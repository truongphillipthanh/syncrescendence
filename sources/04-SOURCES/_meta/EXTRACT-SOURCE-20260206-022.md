# Extraction: SOURCE-20260206-022

**Source**: `SOURCE-20260206-x-article-voxyz_ai-i_built_an_ai_company_with_openclaw_vercel_supabase_two_weeks_later_they_run_it_themselves.md`
**Atoms extracted**: 32
**Categories**: claim, concept, framework, praxis_hook, prediction

---

## Claim (9)

### ATOM-SOURCE-20260206-022-0001
**Lines**: 4-4
**Context**: anecdote / claim
**Tension**: novelty=0.20, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.60, epistemic_stability=0.50

> Building an autonomous AI agent system capable of running a website end-to-end from initial agent communication capabilities took two weeks.

### ATOM-SOURCE-20260206-022-0022
**Lines**: 286-287
**Context**: anecdote / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> The core closed loop of an autonomous system (propose → execute → feedback → re-trigger) can be wired up in approximately one week, excluding pre-existing infrastructure.

### ATOM-SOURCE-20260206-022-0023
**Lines**: 291-291
**Context**: anecdote / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> The described system, with 6 agents, autonomously operates voxyz.space daily.

### ATOM-SOURCE-20260206-022-0024
**Lines**: 293-294
**Context**: consensus / limitation
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.60

> Inter-agent collaboration in the described system is still basic, and 'free will' is mostly simulated through probability-based non-determinism.

### ATOM-SOURCE-20260206-022-0025
**Lines**: 294-294
**Context**: anecdote / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> The system genuinely runs and does not require constant human monitoring.

### ATOM-SOURCE-20260206-022-0027
**Lines**: 311-311
**Context**: anecdote / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.50

> The core closed loop of an autonomous agent system (propose → execute → feedback → re-trigger) can be wired up in approximately one week, excluding pre-existing infrastructure.

### ATOM-SOURCE-20260206-022-0028
**Lines**: 315-315
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> Six autonomous agents are currently operating voxyz.space daily.

### ATOM-SOURCE-20260206-022-0029
**Lines**: 318-318
**Context**: anecdote / limitation
**Tension**: novelty=0.40, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.30, actionability=0.50, epistemic_stability=0.40

> The inter-agent collaboration in the described autonomous system is still basic, and 'free will' is primarily simulated through probability-based non-determinism.

### ATOM-SOURCE-20260206-022-0030
**Lines**: 319-319
**Context**: anecdote / claim
**Tension**: novelty=0.30, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> The autonomous agent system genuinely runs without requiring constant human oversight.

## Concept (2)

### ATOM-SOURCE-20260206-022-0004
**Lines**: 37-46
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.60

> A 'closed loop' in an unattended agent system involves a cycle of agent proposal, auto-approval, mission creation, worker execution, event emission, and triggering of new reactions, returning to the proposal stage.

### ATOM-SOURCE-20260206-022-0013
**Lines**: 195-196
**Context**: hypothesis / claim
**Tension**: novelty=0.80, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.40, actionability=0.30, epistemic_stability=0.40

> Introducing probability into inter-agent reactions, rather than 100% determinism, can make a system feel more like a 'real team' where responses are not always guaranteed.

## Framework (6)

### ATOM-SOURCE-20260206-022-0002
**Lines**: 16-20
**Context**: method / evidence
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> The VoxYZ Agent World uses OpenClaw for agent intelligence, Next.js + Vercel for the website frontend and API, and Supabase as the single source of truth for all state.

### ATOM-SOURCE-20260206-022-0003
**Lines**: 22-23
**Context**: method / evidence
**Tension**: novelty=0.40, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.50

> The VoxYZ Agent World assigns six distinct roles to AI agents: Minion (decisions), Sage (strategy analysis), Scout (intel gathering), Quill (content writing), Xalt (social media management), and Observer (quality checks).

### ATOM-SOURCE-20260206-022-0008
**Lines**: 111-115
**Context**: method / evidence
**Tension**: novelty=0.60, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> A gate system for AI agent proposals can include specific checks for different step kinds, such as `checkWriteContentGate` for daily content caps, `checkPostTweetGate` for tweet quotas, and `checkDeployGate` for deployment policies.

### ATOM-SOURCE-20260206-022-0010
**Lines**: 160-161
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> A system can use built-in triggers to detect conditions and return proposal templates, which are then handed to a proposal service, with cap gates and auto-approve logic applied automatically.

### ATOM-SOURCE-20260206-022-0012
**Lines**: 176-177
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.50

> A 'reaction matrix' can define spontaneous inter-agent interactions based on patterns, such as a source, tags, target agent, action type, probability, and cooldown.

### ATOM-SOURCE-20260206-022-0016
**Lines**: 220-223
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> A three-layer architecture for an autonomous system can consist of OpenClaw (VPS) for thinking and execution, Vercel for approval and monitoring, and Supabase for all state management.

## Praxis Hook (13)

### ATOM-SOURCE-20260206-022-0005
**Lines**: 56-58
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> To avoid race conditions and conflicting task execution in an AI agent system, designate a single executor (e.g., a VPS) for tasks, while a lightweight control plane (e.g., Vercel) handles triggers, reaction queues, and task recovery.

### ATOM-SOURCE-20260206-022-0006
**Lines**: 80-82
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> To ensure consistent proposal processing and prevent triggers from bypassing approval flows, centralize all proposal creation through a single shared function (`createProposalAndMaybeAutoApprove`) that handles checks, insertion, event emission, and auto-approval.

### ATOM-SOURCE-20260206-022-0007
**Lines**: 106-108
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Implement 'Cap Gates' at the proposal entry point to reject proposals immediately if quotas or policies are not met, preventing the buildup of unexecutable tasks in the queue. Rejected proposals should be recorded for auditing.

### ATOM-SOURCE-20260206-022-0009
**Lines**: 149-150
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Implement a 'reject at the gate' principle for system proposals, where rejected proposals are recorded for auditing rather than silently dropped, preventing unbounded queue growth.

### ATOM-SOURCE-20260206-022-0011
**Lines**: 171-172
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Implement cooldown periods for triggers to prevent excessive activation from a single event, ensuring system stability and efficiency.

### ATOM-SOURCE-20260206-022-0014
**Lines**: 200-201
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Implement a self-healing mechanism in a system's heartbeat to recover stale steps by marking them as failed after a defined threshold (e.g., 30 minutes without progress) and then checking if the mission should be finalized.

### ATOM-SOURCE-20260206-022-0015
**Lines**: 215-216
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> When finalizing a mission, check all its steps; the entire mission fails if any step fails, and succeeds only if all steps are completed, preventing partial successes from marking the whole mission as successful.

### ATOM-SOURCE-20260206-022-0017
**Lines**: 232-242
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> For a minimum viable closed-loop system, essential database tables include `ops_mission_proposals`, `ops_missions`, `ops_mission_steps`, `ops_agent_events`, `ops_policy`, `ops_trigger_rules`, `ops_agent_reactions`, and `ops_action_runs`.

### ATOM-SOURCE-20260206-022-0018
**Lines**: 244-246
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Consolidate proposal creation, cap gates, auto-approve, and mission creation into a single function (Proposal Service) that all sources (API, triggers, reactions) call, making it the central hub of the system loop.

### ATOM-SOURCE-20260206-022-0019
**Lines**: 248-249
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Store all system behavior toggles and limits in a policy-driven configuration table (e.g., `ops_policy`) to allow adjustments without code redeployment.

### ATOM-SOURCE-20260206-022-0020
**Lines**: 264-266
**Context**: method / claim
**Tension**: novelty=0.50, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Implement a system heartbeat as an API route (e.g., `/api/ops/heartbeat`) called by a crontab line every few minutes, which runs trigger evaluation, reaction queue processing, insight promotion, and stale task cleanup.

### ATOM-SOURCE-20260206-022-0021
**Lines**: 268-270
**Context**: method / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Ensure that after completing a step, a worker calls `maybeFinalizeMissionIfDone` to check the entire mission's status, rather than marking the mission as succeeded based on a single step's completion.

### ATOM-SOURCE-20260206-022-0032
**Lines**: 324-325
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.70

> Indie developers building agent systems with OpenClaw should compare notes with others to avoid common pitfalls.

## Prediction (2)

### ATOM-SOURCE-20260206-022-0026
**Lines**: 296-298
**Context**: speculation / claim
**Tension**: novelty=0.70, consensus_pressure=0.20, contradiction_load=0.10, speculation_risk=0.80, actionability=0.30, epistemic_stability=0.40

> Future work will cover how agents 'argue' and 'persuade' each other, including roundtable voting and Sage's memory consolidation, to foster team cognition among independent Claude instances.

### ATOM-SOURCE-20260206-022-0031
**Lines**: 321-322
**Context**: speculation / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.70, actionability=0.20, epistemic_stability=0.30

> A future article will detail how agents 'argue' and 'persuade' each other, and how roundtable voting and Sage's memory consolidation contribute to team cognition among independent Claude instances.
