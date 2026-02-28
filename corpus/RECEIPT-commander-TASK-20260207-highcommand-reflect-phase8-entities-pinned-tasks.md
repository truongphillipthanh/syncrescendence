# TASK-20260207-highcommand-reflect-phase8-entities-pinned-tasks

**From**: Commander (self-dispatch)
**To**: Commander (Claude Code Opus)
**Issued**: 2026-02-07
**Kind**: TASK
**Priority**: P1
**Exit-Code**: 0
**Completed-At**: 2026-02-07T18:01:24Z
**Claimed-At**: 2026-02-07T18:01:23Z
**Claimed-By**: commander-M1-Mac-mini
**Kanban**: DONE
**Status**: COMPLETE
**Reply-To**: commander
**CC**: commander
**Timeout**: 120
**Receipts-To**: -INBOX/commander/00-INBOX0

---

## Objective

Implement **Entity Templates**, **Pinned Notes**, and **Dedicated Tasks View** — the remaining Major-severity gaps from the Reflect analysis.

---

## Required Actions

### Part A: Entity Templates

1. Extend `OntologyClass` or create entity subtypes for **Person** and **Company** with structured metadata fields:
   - Person: Title, Company (backlink), Type (#person), Emails, Phone, Location
   - Company: Type (#company), Domain
2. Slash commands `/person` and `/company` create typed Intentions with pre-populated field templates at the top of the note body.
3. Entity tag rendering: `#person` and `#company` tags render as colored pills in AllNotesView and inline.

### Part B: Pinned Notes Sidebar

1. Add `isPinned: Bool` to Intention model (or DailyNote if Phase 5 exists).
2. Add "Pinned notes" section in SidebarView below navigation items, above the existing sections.
3. Pin/unpin via Note Actions in right sidebar, or right-click context menu on sidebar items.
4. Pinned notes appear as simple text rows (matching Reflect's style: no icons, just titles).

### Part C: Dedicated Tasks View

1. **Create TasksView.swift** — Standalone view for the "Tasks" sidebar selection:
   - Search bar at top
   - "Task filters" dropdown button (filter by stage, project, ontology class)
   - "Current" section (starred/high-priority tasks — ledgered + connected stages)
   - "+ Add" button to create a new task-typed Intention
   - Each task row shows: checkbox, title, project badge, due hint if present
2. Wire to sidebar navigation as a primary route (matching Reflect's 4 top-level nav: Daily notes, All notes, Tasks, Map).

---

## Acceptance Checks

- [ ] `/person` creates Person-typed Intention with structured fields
- [ ] `/company` creates Company-typed Intention with structured fields
- [ ] #person and #company render as colored tag pills
- [ ] "Pinned notes" section visible in sidebar
- [ ] Pin/unpin works from right sidebar Note Actions
- [ ] TasksView renders with search, filters, Current section, + Add
- [ ] Tasks can be checked off (transitions to dispatched stage)
- [ ] BUILD SUCCEEDS with zero errors

---

## Context Files

- `/Users/home/Desktop/HighCommand/HighCommand-references/reflect/reflect-1.png` (Tasks view)
- `/Users/home/Desktop/HighCommand/HighCommand-references/reflect/relflect-5.png` (All Notes with entity tags)
- `/Users/home/Desktop/HighCommand/HighCommand-resarch/reflect_exegesis.md` (Section II.3: Entity Notes, Section II.5: Command Surface)
- `/Users/home/Desktop/HighCommand/HighCommand/Models/DomainModels.swift`
- `/Users/home/Desktop/HighCommand/HighCommand/Views/SidebarView.swift`

---

## Expected Output

- New file: `HighCommand/Views/TasksView.swift`
- Modified: `DomainModels.swift` (isPinned, entity metadata)
- Modified: `SidebarView.swift` (Pinned notes section, Tasks nav)
- Modified: `SlashCommandMenu.swift` (if Phase 7 complete, add /person /company)
- Modified: `ContentView.swift` (wire TasksView route)
- RESULT file with build verification
