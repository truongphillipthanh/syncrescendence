# DIRECTIVE-044B: MODEL SPECIFICATION PROTOCOL + CLAUDE.MD UPDATE
## Stream B — Claude 3 (Sonnet 4.5)

**Issued**: 2026-01-11
**Stream**: B (Sonnet 4.5 recommended — tactical, clear instructions)
**Priority**: MODERATE
**Estimated Duration**: 30-45 minutes
**Parallel**: DIRECTIVE-044A executing simultaneously on Claude 2
**Companion**: ORACLE12_PEDIGREE.md (read first)

---

## PREAMBLE

You are Claude 3, executing Stream B of Blitzkrieg 44. This is a **minor** blitzkrieg focused on formalizing the model specification protocol and updating infrastructure files.

**Your mandate**: Formalize Blitzkrieg model specification in CLAUDE.md and update coordination.yaml with routing guidance.

---

## PHASE 1: FORMALIZE MODEL SPECIFICATION PROTOCOL (~20 minutes)

### 1.1 Read Current CLAUDE.md
```bash
cat CLAUDE.md
```

### 1.2 Add Model Specification Section

Add the following section to CLAUDE.md (find appropriate location):

```markdown
## BLITZKRIEG MODEL SPECIFICATION

When issuing Blitzkrieg directives, Oracle specifies which model to use per stream:

### Model Selection Criteria

| Model | Use When | Characteristics |
|-------|----------|-----------------|
| **Opus 4.5** | Comprehensive directives, architectural decisions, complex synthesis | Deep reasoning, better judgment, worth the cost for strategic work |
| **Sonnet 4.5** | Clear tactical instructions, well-defined tasks, execution-heavy work | Fast, capable, cost-effective when task is well-specified |

### Extended Thinking Specification

Directives may include thinking level guidance:
- `ultrathink` (~32K tokens) — Complex architectural synthesis
- `megathink` (~10K tokens) — Moderate complexity reasoning
- `think` (~4K tokens) — Standard deliberation
- *(none)* — Let model self-regulate

### Directive Header Format

Each directive should include:
```yaml
Stream: A/B
Model: Opus 4.5 / Sonnet 4.5
Thinking: ultrathink / megathink / think / default
Estimated Duration: X minutes
```

### Default Behavior

- **Oracle strategic synthesis**: Opus 4.5 (ultrathink)
- **Blitzkrieg execution**: Sonnet 4.5 unless complexity warrants Opus
- **Repository maintenance**: Sonnet 4.5 (think)
```

### 1.3 Update CLAUDE.md Header

Update version and last modified:
```markdown
**Version**: 2.1.0 (was 2.0.0)
**Last Updated**: 2026-01-11
```

---

## PHASE 2: UPDATE COORDINATION.YAML (~15 minutes)

### 2.1 Read Current coordination.yaml
```bash
cat config/coordination.yaml
```

### 2.2 Add Model Routing Section

Add or update `model_routing` section:

```yaml
model_routing:
  default: sonnet-4.5
  by_task_type:
    oracle_synthesis: opus-4.5
    architectural_decisions: opus-4.5
    complex_integration: opus-4.5
    repository_maintenance: sonnet-4.5
    ledger_updates: sonnet-4.5
    content_processing: sonnet-4.5
    verification_tasks: sonnet-4.5
  
  thinking_defaults:
    oracle_synthesis: ultrathink
    architectural_decisions: megathink
    complex_integration: megathink
    repository_maintenance: think
    ledger_updates: default
    content_processing: think
    verification_tasks: default
```

### 2.3 Add Version Update

Update coordination.yaml header:
```yaml
# coordination.yaml
# Version: 2.1.0 (was 2.0.0)
# Updated: 2026-01-11
# Change: Added model_routing section per Oracle 12 decision
```

---

## PHASE 3: LEDGER UPDATE (~5 minutes)

### 3.1 Add Tasks to tasks.csv

```csv
TASK-090,PROJ-012,Formalize model specification protocol in CLAUDE.md,task,done,P2,Claude_Code,null,0.5,null,2026-01-11,2026-01-11,Blitzkrieg 44
TASK-091,PROJ-012,Add model routing to coordination.yaml,task,done,P2,Claude_Code,TASK-090,0.5,null,2026-01-11,2026-01-11,Blitzkrieg 44
```

---

## VERIFICATION CHECKLIST

- [ ] CLAUDE.md includes BLITZKRIEG MODEL SPECIFICATION section
- [ ] CLAUDE.md version updated to 2.1.0
- [ ] coordination.yaml includes model_routing section
- [ ] coordination.yaml version updated to 2.1.0
- [ ] tasks.csv updated with TASK-090-091
- [ ] No subdirectories created (FLAT PRINCIPLE)

---

## VERIFICATION COMMANDS

```bash
# Confirm CLAUDE.md has model specification
grep -c "BLITZKRIEG MODEL SPECIFICATION" CLAUDE.md

# Confirm coordination.yaml has routing
grep -c "model_routing" config/coordination.yaml

# Confirm tasks added
grep "TASK-09[01]" 00-ORCHESTRATION/state/tasks.csv
```

---

## EXECUTION LOG TEMPLATE

Create `EXECUTION_LOG-2026-01-11-044B.md` upon completion with:
1. Phases executed
2. Files modified
3. Verification outputs
4. Duration

---

*DIRECTIVE-044B issued 2026-01-11 | Oracle 12 | Blitzkrieg 44*
