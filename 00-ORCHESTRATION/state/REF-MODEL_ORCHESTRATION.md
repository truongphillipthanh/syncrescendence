# Model Orchestration

Formal topology for Syncrescendence execution and sensing.

## Topology (high level)
Sovereign ↔ Web Apps (Claude / Gemini / ChatGPT) ↔ Repo (Codex CLI / Claude Code)

- **Sovereign**: final decision authority and intent source.
- **Claude Code**: execution lane, repo integration, structural edits.
- **Gemini**: corpus-scale sensing, ingestion, multimodal processing.
- **Codex CLI (ChatGPT)**: reasoning, synthesis, and repo edits when assigned.

Source of truth for routing and roles: `02-ENGINE/coordination.yaml` and `01-CANON/CANON-25200-CONSTELLATION_ARCH-lattice.md`.

## Role allocation (default)
- **Strategic synthesis**: Claude (Oracle thread) or ChatGPT when specified.
- **Execution**: Claude Code instances (alpha/beta).
- **Sensing/ingestion**: Gemini (2M context, multimodal).
- **Abstract reasoning**: ChatGPT (GPT-5.2 capability).

See `00-ORCHESTRATION/state/REF-BLITZKRIEG_PROTOCOL_VNEXT.md` for lane definitions.

## Kaizen loop into the corpus
1. **Sensing** (Gemini): produce evidence pack in `-OUTGOING/`.
2. **Synthesis** (Claude/ChatGPT): create decision atoms and draft changes.
3. **Integration** (Claude Code/Codex CLI): update CANON/OPERATIONAL files.
4. **Verification**: run structural and lens checks (see `00-ORCHESTRATION/state/REF-REPO_VALIDATION_PROTOCOL.md`).
5. **Retention**: keep only pointers + minimal evidence; discard transient reasoning.

This loop is the only sanctioned path for durable change.
