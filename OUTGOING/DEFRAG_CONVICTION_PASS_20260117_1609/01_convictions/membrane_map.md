# Membrane Map
## Boundaries, Crossings, and Required Receipts
**Generated**: 2026-01-17

---

## I. WHAT MEMBRANES ARE

Membranes are boundaries between different domains of the system. Each membrane has:
- **What can cross**: Permitted flows
- **What cannot cross**: Prohibited flows
- **Required receipts**: Artifacts that must be created when crossing

Membranes protect system integrity by controlling information flow.

---

## II. THE FIVE MEMBRANES

### Membrane 1: Surface ↔ Repo

**Domain A**: Conversational surfaces (Claude Web, ChatGPT, Gemini, etc.)
**Domain B**: Repository (ground truth)

```
┌─────────────────┐          ┌─────────────────┐
│    SURFACE      │          │      REPO       │
│                 │          │                 │
│  Claude Web     │◀────────▶│  00-ORCHESTRATION│
│  ChatGPT        │ Membrane │  01-CANON       │
│  Gemini         │    1     │  02-OPERATIONAL │
│  Claude Code    │          │  ...            │
└─────────────────┘          └─────────────────┘
```

| What Can Cross | Direction | Receipt Required |
|----------------|-----------|------------------|
| Directives | Surface → Repo | Commit |
| Execution results | Surface → Repo | EXE packet, commit |
| Context for session | Repo → Surface | None (read) |
| Artifacts | Surface → Repo | CONT packet |
| Plans | Surface → Repo | PLN packet |
| Research findings | Surface → Repo | EVD packet |

| What Cannot Cross | Why |
|-------------------|-----|
| Unexternalized state | Creates implicit database |
| Uncommitted changes | Not durable |
| Platform-specific memory | Non-portable |

---

### Membrane 2: Tool ↔ Context

**Domain A**: Tool execution (MCP servers, Bash, sub-agents)
**Domain B**: Main conversation context

```
┌─────────────────┐          ┌─────────────────┐
│      TOOL       │          │     CONTEXT     │
│                 │          │                 │
│  MCP servers    │◀────────▶│  Main thread    │
│  Bash commands  │ Membrane │  Coordinator    │
│  Sub-agents     │    2     │  Working memory │
└─────────────────┘          └─────────────────┘
```

| What Can Cross | Direction | Receipt Required |
|----------------|-----------|------------------|
| Tool results (summarized) | Tool → Context | None (inline) |
| Task delegation | Context → Tool | Context packet |
| File reads | Tool → Context | None |
| File writes | Tool → Repo | Commit (via Membrane 1) |

| What Cannot Cross | Why |
|-------------------|-----|
| Full tool output (verbose) | Bloats context |
| Tool schemas (all at once) | Token budget exceeded |
| Other agents' full context | Creates confusion |

**Key Pattern**: Sub-agents return summaries, not full traces.

---

### Membrane 3: Agent ↔ Agent

**Domain A**: One agent (e.g., Claude Code Alpha)
**Domain B**: Another agent (e.g., Claude Code Beta, ChatGPT)

```
┌─────────────────┐          ┌─────────────────┐
│    AGENT A      │          │    AGENT B      │
│                 │          │                 │
│  Claude Code    │◀────────▶│  ChatGPT        │
│  (Executor)     │ Membrane │  (Deviser)      │
│                 │    3     │                 │
└─────────────────┘          └─────────────────┘
```

| What Can Cross | Direction | Receipt Required |
|----------------|-----------|------------------|
| Plan packets | B → A | PLN packet in repo |
| Execution packets | A → B | EXE packet in repo |
| Evidence packets | Oracle → Deviser | EVD packet in repo |
| Audit packets | Auditor → Repo | AUD packet in repo |

| What Cannot Cross | Why |
|-------------------|-----|
| Conversation context | Non-portable |
| Platform-specific state | Incompatible |
| Implicit assumptions | Not verified |

**Key Pattern**: All inter-agent communication goes through repo (blackboard).

---

### Membrane 4: Account ↔ Account

**Domain A**: One account (e.g., Personal iCloud)
**Domain B**: Another account (e.g., Hybrid Gmail)

```
┌─────────────────┐          ┌─────────────────┐
│   ACCOUNT A     │          │   ACCOUNT B     │
│                 │          │                 │
│  Personal       │◀────────▶│  Hybrid         │
│  (iCloud)       │ Membrane │  (Gmail)        │
│                 │    4     │                 │
└─────────────────┘          └─────────────────┘
```

| What Can Cross | Direction | Receipt Required |
|----------------|-----------|------------------|
| Public artifacts | A ↔ B | Via repo |
| Non-sensitive documents | A ↔ B | Via repo |
| Research findings | B → A | Via repo |

| What Cannot Cross | Why |
|-------------------|-----|
| API keys | Security |
| Credentials | Security |
| Personal PII | Privacy |
| Client confidential data | Privacy |
| Private repo contents (to Gemini) | IP exposure (training) |

**Key Pattern**: Repo is the neutral zone; accounts touch repo, not each other directly.

---

### Membrane 5: Canon ↔ Ops

**Domain A**: Canonical knowledge (01-CANON/)
**Domain B**: Operational state (00-ORCHESTRATION/, 02-OPERATIONAL/)

```
┌─────────────────┐          ┌─────────────────┐
│     CANON       │          │      OPS        │
│                 │          │                 │
│  01-CANON/      │◀────────▶│  00-ORCHESTRATION│
│  Constitutional │ Membrane │  02-OPERATIONAL │
│  Protected      │    5     │  Working        │
└─────────────────┘          └─────────────────┘
```

| What Can Cross | Direction | Receipt Required |
|----------------|-----------|------------------|
| Validated insights | Ops → Canon | Integration commit |
| Reference (read) | Canon → Ops | None |
| Schema updates | Ops → Canon | Principal approval |
| Protocol changes | Ops → Canon | 18-lens evaluation |

| What Cannot Cross | Why |
|-------------------|-----|
| Unvalidated content | Canon is verified |
| Temporal/current-state info | Canon is durable |
| Operational detritus | Canon is clean |

**Key Pattern**: Canon is append-friendly, edit-hostile. Changes require justification.

---

## III. MEMBRANE CROSSING RECEIPTS SUMMARY

| Membrane | Crossing Type | Required Receipt |
|----------|---------------|------------------|
| 1 (Surface↔Repo) | Externalization | EVD/PLN/EXE/AUD/CONT + commit |
| 2 (Tool↔Context) | Delegation | Context packet to sub-agent |
| 3 (Agent↔Agent) | Handoff | Blackboard packet |
| 4 (Account↔Account) | Transfer | Via repo (neutral zone) |
| 5 (Canon↔Ops) | Promotion | Integration commit + Principal approval |

---

## IV. MEMBRANE VIOLATION DETECTION

### Membrane 1 Violation Signs
- State discussed but not in repo
- "We decided X" with no recorded decision
- Session ends without artifacts

### Membrane 2 Violation Signs
- Context window filling unexpectedly
- Tool output included verbatim (not summarized)
- All MCP schemas loaded at once

### Membrane 3 Violation Signs
- Agent claims to know what another agent did without packet
- "Continue from where [other agent] left off" without handoff
- Implicit assumptions about shared state

### Membrane 4 Violation Signs
- Credentials in conversation
- PII crossing to cloud AI
- Sensitive data in prompts

### Membrane 5 Violation Signs
- CANON edited without Principal approval
- Temporal content in CANON
- Unvalidated content promoted to CANON

---

## V. ENFORCEMENT MECHANISMS

| Membrane | Enforcement Mechanism |
|----------|----------------------|
| 1 | Closure Gate (requires receipts) |
| 2 | Sub-agent summary requirement |
| 3 | Blackboard protocol (packets required) |
| 4 | Data classification rules |
| 5 | Protected zone permissions |

---

## VI. MEMBRANE VISUALIZATION

```
                    ┌─────────────────────────────────────┐
                    │           ACCOUNTS                   │
                    │  ┌─────────┐   ┌─────────┐          │
                    │  │ Personal│◀─▶│ Hybrid  │          │
                    │  │ (iCloud)│ M4│ (Gmail) │          │
                    │  └────┬────┘   └────┬────┘          │
                    │       │             │                │
                    │       └──────┬──────┘                │
                    │              │                       │
                    └──────────────┼───────────────────────┘
                                   │
                    ┌──────────────┼───────────────────────┐
                    │              ▼                       │
                    │         SURFACES           M1        │
                    │  ┌─────┐ ┌─────┐ ┌─────┐ ◀─────────▶ │
                    │  │Claude│ │Chat │ │Gemini│           │
                    │  │ Web  │ │GPT  │ │     │            │
                    │  └──┬───┘ └──┬──┘ └──┬──┘            │
                    │     │       │       │                │
                    │     └───────┼───────┘                │
                    │             │ M3 (Agent↔Agent)       │
                    └─────────────┼────────────────────────┘
                                  │
                    ┌─────────────┼────────────────────────┐
                    │             ▼                        │
                    │        REPOSITORY                    │
                    │  ┌──────────────────────────────┐    │
                    │  │        00-ORCHESTRATION       │    │
                    │  │   ┌────────┐  ┌────────┐     │    │
                    │  │   │blackboard│  │ state │     │    │
                    │  │   └────────┘  └────────┘     │    │
                    │  └──────────────────────────────┘    │
                    │            │                         │
                    │            │ M5 (Canon↔Ops)          │
                    │            ▼                         │
                    │  ┌──────────────────────────────┐    │
                    │  │         01-CANON              │    │
                    │  │       (PROTECTED)             │    │
                    │  └──────────────────────────────┘    │
                    │                                      │
                    │  ┌───────────────────────────────┐   │
                    │  │ TOOLS (M2: Tool↔Context)      │   │
                    │  │  MCP servers, sub-agents      │   │
                    │  └───────────────────────────────┘   │
                    │                                      │
                    └──────────────────────────────────────┘
```

---

**Membranes protect coherence. Cross them properly, with receipts.**
