# Google AI Studio Playbook

**Status**: stage0-v1  
**Class**: model-surface playbook  
**Authority chain**: constitution -> executive intention -> program -> playbook -> model checkpoint bridge / reconciliation / ontology  
**Primary sources**:
- [EXOCORTEX-SURFACE-TAXONOMY-CC75.md](/Users/system/syncrescendence/orchestration/state/impl/EXOCORTEX-SURFACE-TAXONOMY-CC75.md)
- [EXOCORTEX-ACCOUNT-IDENTITY-MATRIX-CC76.md](/Users/system/syncrescendence/orchestration/state/impl/EXOCORTEX-ACCOUNT-IDENTITY-MATRIX-CC76.md)
- [TOOL-STACK-ADDENDUM-POST-CC75.md](/Users/system/syncrescendence/orchestration/state/impl/TOOL-STACK-ADDENDUM-POST-CC75.md)
- [operators/exocortex/google_model_bridge.py](/Users/system/syncrescendence/operators/exocortex/google_model_bridge.py)

## 0. What This Surface Is For

Google AI Studio is a Google model execution surface for rapid model-side experimentation and prompt/runtime evaluation.

## 1. Surface Separation Rule

Treat these as distinct surfaces:
- `google_ai_studio` (interactive model experimentation)
- `gemini_api` (programmatic model invocation)
- `vertex_ai` (projected production infra/model surface)
- `notebooklm_surface` (source-bounded synthesis surface)

Do not collapse them into one "Google" bucket.

## 2. Native Grain

AI Studio is strongest for:
- quick model behavior checks
- prompt evaluation before automation hardening
- comparative tests before API/operator promotion

## 3. Return Path

When model execution is adopted into durable pipeline, emit a checkpoint:

```bash
python3 operators/exocortex/google_model_bridge.py \
  --model "<model>" \
  --request-kind "<kind>" \
  --provider-surface google_ai_studio \
  --summary "<summary>" \
  --project-ontology \
  --ontology-url domain
```

## 4. Guardrails

- AI Studio output is evidence, not constitutional truth
- cost and quota constraints must be explicit before scale-up
- only promote patterns that survive replay in operatorized/API form
