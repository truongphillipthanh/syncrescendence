# TASK-20260207-highcommand-reflect-phase7-slash-backlinks

**From**: Commander (self-dispatch)
**To**: Commander (Claude Code Opus)
**Issued**: 2026-02-07
**Kind**: TASK
**Priority**: P1
**Exit-Code**: 0
**Completed-At**: 2026-02-07T18:01:05Z
**Claimed-At**: 2026-02-07T18:01:05Z
**Claimed-By**: commander-M1-Mac-mini
**Kanban**: DONE
**Status**: COMPLETE
**Reply-To**: commander
**CC**: commander
**Timeout**: 120
**Receipts-To**: -INBOX/commander/00-INBOX0

---

## Objective

Implement the **Slash Command Menu** and **Inline Backlink System** in HighCommand, cloning Reflect's two most distinctive input primitives. These are the interaction grammar that transforms HighCommand from a dashboard into a thinking tool.

---

## Required Actions

### Part A: Slash Commands

1. **SlashCommandMenu.swift** — A popup menu triggered by typing `/` in any TextEditor surface. Shows filtered list of block types:
   - Heading 1, Heading 2, Heading 3
   - Task (checkbox item)
   - Bulleted list
   - Ordered list
   - Checklist
   - Quote (blockquote)
   - Backlink (triggers `[[` flow)
   - Now (inserts current timestamp)
   - AI Palette (triggers Cmd+J flow or opens AI context)
   - Transcribe (triggers VoiceCaptureManager)

2. **Keyboard filtering** — As user types after `/`, menu filters in real-time. Arrow keys + Return to select. Esc to dismiss.

3. **Integration** — Attach to CaptureView TextEditor, DailyNotesView TextEditor (Phase 5), and any future inline editor surfaces.

### Part B: Backlink Inline System

1. **BacklinkAutocomplete.swift** — Popup triggered by typing `[[` in any TextEditor. Shows:
   - Real-time search across all Intentions (by title/summary)
   - Avatar-style icons by OntologyClass (color-coded dots)
   - Option to "Create new note" if no match
   - Inserts `[[Note Title]]` on selection

2. **Inline backlink rendering** — Text containing `[[...]]` renders the bracketed text in accent color (brand orange) as a tappable link that navigates to the referenced Intention.

3. **Incoming backlinks section** — At the bottom of any Intention detail view, show "Incoming backlinks" — all other Intentions whose content contains `[[this note's title]]`. Show snippet context.

4. **Suggested backlinks** — In right sidebar, use NLEmbedding similarity (already in ConnectView) to suggest related Intentions the user hasn't linked yet. Each with one-click "Add" action.

---

## Acceptance Checks

- [ ] `/` triggers popup menu in capture TextEditor
- [ ] Menu filters as user types
- [ ] At least 6 block types insertable (Heading, Task, Bullet, Quote, Now, Backlink)
- [ ] `[[` triggers autocomplete popup with Intention search
- [ ] Selected backlink inserts `[[Title]]` text
- [ ] `[[Title]]` renders in accent color inline
- [ ] Incoming backlinks section appears on note detail
- [ ] BUILD SUCCEEDS with zero errors

---

## Context Files

- `/Users/home/Desktop/HighCommand/HighCommand-resarch/reflect_exegesis.md` (Section II.2: Backlinks, Section II.5: Command Surface — slash commands)
- `/Users/home/Desktop/HighCommand/HighCommand/Views/CaptureView.swift` (existing TextEditor)
- `/Users/home/Desktop/HighCommand/HighCommand/Views/ConnectView.swift` (NLEmbedding similarity code)
- `/Users/home/Desktop/HighCommand/HighCommand/Models/DomainModels.swift` (Edge model)

---

## Expected Output

- New file: `HighCommand/Views/SlashCommandMenu.swift`
- New file: `HighCommand/Views/BacklinkAutocomplete.swift`
- Modified: `CaptureView.swift` (attach slash + backlink triggers)
- Modified: `DailyNotesView.swift` (if Phase 5 complete, attach triggers)
- Modified: `RightPanelView.swift` (suggested backlinks panel)
- RESULT file with build verification
