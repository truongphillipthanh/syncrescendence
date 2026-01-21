# Cognitive Core Nucleus Proposal
The following 7 files constitute the 'Cognitive Core' of Syncrescendence:

1. **COCKPIT.md**
   - **Role**: Operational nerve center and entry point.
   - **Replaces**: Various 'README' files in subdirectories.
   - **Points To**: `Makefile`, `00-ORCHESTRATION/`.
   - **Loss**: Specific task history.

2. **CLAUDE.md**
   - **Role**: Agentic persona and protocol definition.
   - **Replaces**: Scattered `.claude.json` or instruction snippets.
   - **Points To**: `REF-STANDARDS.md`.
   - **Loss**: Model-specific prompt tweaks.

3. **00-ORCHESTRATION/state/REF-STANDARDS.md**
   - **Role**: The 18 Lenses; the 'Constitution'.
   - **Replaces**: `18_lenses.md`, `DECISION_LOG.md`.
   - **Points To**: Internal logic.
   - **Loss**: Historical versions of the lenses.

4. **00-ORCHESTRATION/state/DYN-TREE.md**
   - **Role**: Structural blueprint.
   - **Replaces**: Manual directory listings.
   - **Points To**: The filesystem itself.
   - **Loss**: Granular file-level descriptions.

5. **01-CANON/CANON-00015-MACROSCOPIC_NARRATIVES-cosmos.md**
   - **Role**: Narrative and philosophical alignment (Lenses 19-30).
   - **Replaces**: Various 'Philosophy' drafts.
   - **Points To**: External philosophical authorities.
   - **Loss**: Raw, unrefined 'stream of consciousness' notes.

6. **TOPOLOGY_MAP.md**
   - **Role**: Real-time state of the repository.
   - **Replaces**: `SURVEY_REPORT.md`.
   - **Points To**: `DYN-TREE.md`.
   - **Loss**: Temporal drift history.

7. **Makefile**
   - **Role**: The 'Engine' of the system.
   - **Replaces**: Manual shell commands.
   - **Points To**: `02-OPERATIONAL/`.
   - **Loss**: Complex, one-off command strings.
