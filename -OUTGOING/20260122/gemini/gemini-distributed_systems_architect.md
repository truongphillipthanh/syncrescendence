# Distributed Systems Evidence Pack: Syncrescendence Corpus

**Date:** 2026-01-22
**Auditor:** Gemini CLI (Distributed Systems Architect)
**Target:** Syncrescendence Repository

---

## 1. State Inventory

The system state is explicitly partitioned into Mutable, Immutable, Derived, and Replicated tiers.

### Mutable State (The "Hot" Path)
*   **Operational Directives:** `00-ORCHESTRATION/directives/*.md` (Append-only log of intent)
*   **Execution Logs:** `00-ORCHESTRATION/execution_logs/*.md` (Append-only log of action)
*   **Dynamic Ledgers:** `00-ORCHESTRATION/state/DYN-*.csv` (e.g., `DYN-TASKS.csv`, `DYN-BURNDOWN.csv`) - *High contention risk*
*   **Inbox/Outbox:** `-INBOX/`, `-OUTGOING/` (Transient I/O buffers)
*   **Handoff Tokens:** `.constellation/tokens/active.json` (Critical coordination atom)
*   **Queue:** `03-QUEUE` (Synthesis Inbox)

### Immutable State (The "Cold" Store)
*   **Canon:** `01-CANON/*.md` (Constitutional artifacts, versioned via Git)
*   **Archive:** `05-MEMORY/` (Superseded state, 30-day implicit TTL)
*   **Wisdom Layer:** `06-EXEMPLA/` (Aphorisms, Proverbs - effective constants once written)
*   **Source Truth:** `.git/` (The only true persistent store)

### Derived State (Computed Views)
*   **Corpus Index:** `00-ORCHESTRATION/state/DYN-CORPUS_INDEX.md` (Generated from file tree)
*   **Dashboards:** `00-ORCHESTRATION/state/DYN-DASHBOARD.md` (Aggregated status)
*   **System State:** `.constellation/state/current.yaml` (Snapshot of consensus)

### Replicated State (The "Constellation")
*   **Agent Contexts:** Claude, ChatGPT, Gemini, and Grok maintain private, eventually-consistent caches of the repo state.
*   **Synchronization:** Achieved via "Sensing" (reading repo) and "Handoffs" (receiving token).

---

## 2. Consistency Model Analysis

**Assumed Model:** **Sequential Consistency** for the Repository; **Eventual Consistency** for the Agents.

*   **Repository (Ground Truth):** Acts as a **Linearizable** store. All writes must be serialized via Git commits.
*   **Agents (Constellation):** Operate on **Stale Snapshots**. An agent's "read" of the system is only valid at the time of context loading.
*   **Invariant Violation:**
    *   **File:** `00-ORCHESTRATION/state/DYN-TASKS.csv` vs `00-ORCHESTRATION/state/tasks.csv.bak`
    *   **Violation:** Divergence in timestamps (Jan 11 vs Jan 9) suggests a potential "Lost Update" or "Dirty Write" if the backup mechanism isn't atomic.
    *   **Risk:** An agent reads `tasks.csv.bak` thinking it's current, while another writes to `DYN-TASKS.csv`.

---

## 3. Consensus Protocol

**Mechanism:** **Token Passing** (Handoff Protocol).

*   **Token:** `.constellation/tokens/active.json`
*   **Protocol:**
    1.  Agent A holds token (Active).
    2.  Agent A commits work to Repo.
    3.  Agent A generates new Token (targeting Agent B or Principal).
    4.  Agent A releases Token.
    5.  Agent B acquires Token.
*   **Leader:** The **Principal** is the eternal Leader (Paxos Proposer). Agents are Learners/Acceptors who can temporarily become Proposers via Directives.
*   **Partition Behavior:** If the "Web" agents cannot write to the repo, the "CLI" agent (or Principal) acts as the bridge.

---

## 4. Race Condition Detection

### Scenario A: The "Double-Brain" Split
*   **Condition:** Claude Web and Gemini CLI both attempt to execute a Directive simultaneously.
*   **Mechanism:** Both read `DYN-TASKS.csv`, see `TASK-001` as `TODO`. Both mark `IN_PROGRESS`.
*   **Result:** **Write Skew**. Two branches diverge. Git merge conflict ensures detection, but operational energy is wasted.
*   **Probability:** Moderate (High during "Blitz" mode).

### Scenario B: The "Stale Handoff"
*   **Condition:** Agent A generates a handoff token but fails to push the commit containing it to GitHub.
*   **Mechanism:** Agent B is notified (via chat) but cannot see the token file in the repo.
*   **Result:** **Deadlock**. Agent B waits for a token that exists only in Agent A's local state.
*   **Recovery:** Principal intervention (manual push or token regeneration).

---

## 5. Partition Tolerance & CAP Analysis

**System Classification:** **CP (Consistent + Partition Tolerant)**

*   **Consistency:** The system prioritizes correctness (Canonical Truth) over availability (Agents can always chat, but they cannot *act* without the Token/Repo access).
*   **Partition Tolerance:** The system survives network partitions between Agents and Repo by defaulting to "ReadOnly" mode for the Agents.

**Failure Modes:**
*   **Web App Disconnect:** If Claude Web cannot access GitHub, it falls back to its internal context window (High Drift Risk).
*   **CLI Disconnect:** If CLI cannot pull `main`, it refuses to execute Directives (Safety Fail-safe).

---

## 6. Event Sourcing Schema

The system is evolving towards a robust Event Sourcing model.

**Current Events:**
*   `routing_decision`: `{timestamp, task_type, decision, rationale}` (Found in `events.jsonl`)
*   `system_init`: `{timestamp, event, actor}`
*   `execution_complete`: `{timestamp, actor, plan_id, status}`

**Proposed Event Schema (Formalized):**
```json
{
  "event_id": "UUID",
  "type": "DIRECTIVE_ISSUED | TASK_STARTED | TASK_COMPLETED | STATE_CHANGED",
  "timestamp": "ISO8601",
  "actor": "AGENT_ID",
  "payload": {
    "directive_id": "DIR-...",
    "affected_files": ["..."],
    "before_hash": "SHA1",
    "after_hash": "SHA1"
  },
  "causality": {
    "parent_event_id": "UUID",
    "handoff_token_id": "HO-..."
  }
}
```

---

## 7. State Machine Specification

**Entity:** Artifact (e.g., a claim, a document)

```
[VOID] --(Capture)--> [CAPTURED]
[CAPTURED] --(Interpret)--> [INTERPRETED]
[INTERPRETED] --(Compile)--> [COMPILED]
[COMPILED] --(Digest)--> [DIGESTED] --(Sense)--> [SENSED]
[SENSED] --(Verify)--> [VERIFIED]
[VERIFIED] --(Stage)--> [STAGED]
[STAGED] --(Commit)--> [COMMITTED] --(Archive)--> [ARCHIVED]
```

**Illegal Transitions:**
*   `[CAPTURED] -> [COMMITTED]` (Bypassing verification/synthesis)
*   `[ARCHIVED] -> [COMMITTED]` (Zombie state; must go back to `[STAGED]` first)

---

## 8. Refactoring Recommendations

1.  **Atomic State Updates:** Deprecate CSVs for state. Use `events.jsonl` as the *only* source of truth for tasks/projects, and derive the CSVs as read-only views. This eliminates the `tasks.csv` vs `tasks.csv.bak` consistency issue.
2.  **Token Leasing:** Implement a "Time-to-Live" (TTL) in the Handoff Token. If a token isn't used within X minutes, it expires, allowing the Principal to reclaim control without manual cleanup.
3.  **Merkle Proofs:** Agents should include the `git commit hash` of the state they read when generating an output. This allows the Verifier to detect if an output was generated from stale state ("Phantom Read").

