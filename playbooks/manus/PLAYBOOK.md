# Manus Playbook

**Status**: stage0-v1  
**Class**: execution-surface playbook  
**Authority chain**: constitution -> executive intention -> program -> playbook -> checkpoint bridge / reconciliation / ontology  
**Primary sources**:
- [MANUS-FIRST-DISPATCH-CC73.md](/Users/system/syncrescendence/orchestration/state/impl/MANUS-FIRST-DISPATCH-CC73.md)
- [EXOCORTEX-ACCOUNT-IDENTITY-MATRIX-CC76.md](/Users/system/syncrescendence/orchestration/state/impl/EXOCORTEX-ACCOUNT-IDENTITY-MATRIX-CC76.md)
- [operators/exocortex/manus_checkpoint_bridge.py](/Users/system/syncrescendence/operators/exocortex/manus_checkpoint_bridge.py)

## 0. What This Surface Is For

Manus is the bounded autonomous backend execution surface.

It is used for:
- delegated external runs that are too slow, brittle, or cumbersome for direct local execution
- returning structured checkpoints into repo truth
- increasing execution bandwidth without introducing hidden authority

## 1. Native Grain

Manus performs best when work is framed as:
- narrow objective
- explicit assumptions and constraints
- explicit return shape (commands, files, blockers, verification)
- bounded scope with checkpoint discipline

## 2. Guardrails

Manus must not:
- become a second source of truth
- invent policy, governance, or architecture authority
- hold secrets in repo artifacts
- bypass event/reconciliation/ontology projection

## 3. Required Return Path

Every Manus result should be normalized via checkpoint bridge:

```bash
python3 operators/exocortex/manus_checkpoint_bridge.py \
  --workflow "<workflow_id>" \
  --status "<status>" \
  --summary "<summary>" \
  --repo-paths <paths...> \
  --project-ontology \
  --ontology-url domain
```

## 4. Promotion Rule

- keep Manus as an execution surface, not a planning sovereign
- promote repeated successful dispatch/receipt loops into operators and templates
- never ratify Manus output directly without repo-side assessment
