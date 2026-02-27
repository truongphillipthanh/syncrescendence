# Commander Directive: HighCommand Reflect Implementation

## Context

HighCommand (née Agendizer) is at `/Users/home/Desktop/HighCommand`. It is a macOS 26 SwiftUI app (Swift 6.0, SwiftData, XcodeGen) that implements the Syncrescendence ontology as a native GUI substrate (INT-MI19).

The Agendizer Blitzkrieg (Phases 0-4) is COMPLETE. The Saner.AI feature swarm is COMPLETE (BUILD SUCCEEDED — Command Palette, Inbox Triage, AI Conversation, Right Panels, Enhanced Sidebar, Conversational Daily Brief all operational).

A Reflect gap analysis identified 2 critical + 5 major gaps. Four TASK files are staged in your inbox for Phases 5-8.

## Directive

Execute the HighCommand Reflect implementation. Your inbox contains 4 PENDING tasks:

1. **TASK-20260207-highcommand-reflect-phase5-dailynotes.md** (P0) — Daily Notes View: editable infinite-scroll temporal feed, left accent bar, mini-calendar sidebar, note actions
2. **TASK-20260207-highcommand-reflect-phase6-allnotes-table.md** (P0) — All Notes Table: sortable columns (Subject/Snippet/Tags/Updated), type-tab filters, New Note CTA
3. **TASK-20260207-highcommand-reflect-phase7-slash-backlinks.md** (P1) — Slash Command Menu (`/`) + Backlink Inline System (`[[` autocomplete, purple rendering, incoming backlinks, suggested backlinks)
4. **TASK-20260207-highcommand-reflect-phase8-entities-pinned-tasks.md** (P1) — Entity Templates (/person, /company), Pinned Notes sidebar section, Dedicated Tasks View

## Execution Strategy

Phases 5 and 6 are independent — dispatch as parallel swarm if feasible. Phase 7 depends on Phase 5 (slash commands attach to DailyNotesView editor). Phase 8 depends on Phases 6+7 (entity tags render in AllNotesView, /person /company use SlashCommandMenu).

**Dependency graph:**
```
Phase 5 (Daily Notes) ──┐
                         ├──► Phase 7 (Slash + Backlinks)──► Phase 8 (Entities + Pinned + Tasks)
Phase 6 (All Notes)  ───┘
```

## Key References

- **Gap analysis**: `-INBOX/commander/90_ARCHIVE/RESULT-commander-20260207-highcommand-saner-reflect-archaeology.md`
- **Reflect exegesis**: `/Users/home/Desktop/HighCommand/HighCommand-resarch/reflect_exegesis.md`
- **Reflect screenshots**: `/Users/home/Desktop/HighCommand/HighCommand-references/reflect/` (7 PNGs)
- **Domain models**: `/Users/home/Desktop/HighCommand/HighCommand/Models/DomainModels.swift`
- **Existing views**: `/Users/home/Desktop/HighCommand/HighCommand/Views/` (all .swift files)
- **Project config**: `/Users/home/Desktop/HighCommand/project.yml` (XcodeGen — `xcodegen generate` after adding new files)

## Hard Constraints

- macOS 26 Tahoe target, Swift 6.0, SwiftUI only (no AppKit)
- Brand color: `Color(hex: 0xD87001)` (burnt orange) — NOT Reflect's purple
- Dark-mode-first palette (deep navy-charcoal background)
- Progressive disclosure depth stack (L0-L4), NavigationSplitView at app level
- All models use SwiftData `@Model` with `private(set)` on computed/derived properties
- `.glassEffect()` for Liquid Glass surfaces where appropriate
- Every phase must BUILD SUCCEED before marking complete

## Receipt Protocol

After each phase, write RESULT file to `-INBOX/commander/00-INBOX0/RESULT-commander-YYYYMMDD-highcommand-reflect-phaseN.md` and update TASK status to COMPLETE. Update `DYN-EXECUTION_STAGING.md` with behavioral log.

Begin.
