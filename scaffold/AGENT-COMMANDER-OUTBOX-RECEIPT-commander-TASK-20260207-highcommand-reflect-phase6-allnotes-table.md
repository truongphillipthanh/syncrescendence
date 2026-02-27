# TASK-20260207-highcommand-reflect-phase6-allnotes-table

**From**: Commander (self-dispatch)
**To**: Commander (Claude Code Opus)
**Issued**: 2026-02-07
**Kind**: TASK
**Priority**: P0
**Exit-Code**: 0
**Completed-At**: 2026-02-07T18:07:03Z
**Claimed-At**: 2026-02-07T18:00:46Z
**Claimed-By**: commander-M1-Mac-mini
**Kanban**: DONE
**Status**: COMPLETE
**Reply-To**: commander
**CC**: commander
**Timeout**: 120
**Receipts-To**: -INBOX/commander/00-INBOX0

---

## Objective

Implement the **All Notes Table View** in HighCommand, cloning Reflect's sortable, filterable notes list. This is the #2 critical gap from the Reflect gap analysis.

---

## Required Actions

1. **Create AllNotesView.swift** — Sortable table view replacing or augmenting the existing FilteredIntentionsView for the "All notes" sidebar selection.

2. **Table columns**:
   - **Subject**: Note title/summary (bold, primary text)
   - **Snippet**: First ~80 chars of body content (muted secondary text)
   - **Tags**: Inline pills rendered in accent color (#person, #company, #project, etc.) mapped from OntologyClass
   - **Updated**: Relative timestamp ("Fri", "2d ago", etc.)

3. **Tab filter bar** — Horizontal pills above the table:
   - All | Projects | Areas | Resources | People | Trash | Custom
   - Maps to OntologyClass enum values + archived state
   - Active tab highlighted with brand color underline

4. **"New note" CTA** — Button in top-right with Cmd+N shortcut. Creates a new blank Intention and navigates to its editor.

5. **Sort behavior** — Click column header to sort. Default: Updated desc. Support: Subject alpha, Updated asc/desc, Tags grouped.

6. **Row interaction** — Click row → navigate to note detail (or open in editor). Row hover state with subtle highlight.

---

## Acceptance Checks

- [ ] Table renders with 4 columns (Subject, Snippet, Tags, Updated)
- [ ] Tab filters work and filter the list by OntologyClass
- [ ] "New note" button creates Intention and navigates to it
- [ ] Column sorting works on at least Subject and Updated
- [ ] Tag pills render inline with correct colors
- [ ] Trash tab shows archived intentions
- [ ] BUILD SUCCEEDS with zero errors

---

## Context Files

- `/Users/home/Desktop/HighCommand/HighCommand-references/reflect/relflect-5.png` (All Notes screenshot)
- `/Users/home/Desktop/HighCommand/HighCommand-resarch/reflect_exegesis.md` (Section II.3: Entity Notes, tags)
- `/Users/home/Desktop/HighCommand/HighCommand/Models/DomainModels.swift` (Intention model, OntologyClass enum)
- `/Users/home/Desktop/HighCommand/HighCommand/Views/LedgerView.swift` (existing list view to reference)

---

## Expected Output

- New file: `HighCommand/Views/AllNotesView.swift`
- Modified: `AppNavigationState.swift` (add .allNotes if not present)
- Modified: `ContentView.swift` (wire ContentRouter)
- RESULT file with build verification
