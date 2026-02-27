# TASK-20260207-highcommand-reflect-phase5-dailynotes

**From**: Commander (self-dispatch)
**To**: Commander (Claude Code Opus)
**Issued**: 2026-02-07
**Kind**: TASK
**Priority**: P0
**Exit-Code**: 0
**Completed-At**: 2026-02-07T18:00:34Z
**Claimed-At**: 2026-02-07T18:00:34Z
**Claimed-By**: commander-M1-Mac-mini
**Kanban**: DONE
**Status**: COMPLETE
**Reply-To**: commander
**CC**: commander
**Timeout**: 120
**Receipts-To**: -INBOX/commander/00-INBOX0

---

## Objective

Implement the **Daily Notes View** in HighCommand, cloning Reflect's core temporal feed primitive. This is the #1 critical gap identified in the Reflect gap analysis (RESULT-commander-20260207-highcommand-saner-reflect-archaeology.md).

---

## Required Actions

1. **Create DailyNotesView.swift** — New view replacing the read-only NavigateView as the default landing surface for the "Daily notes" sidebar selection.

2. **Infinite temporal scroll** — ScrollView with LazyVStack, dates stretching infinitely forward/backward. Today auto-scrolled to center. Each day rendered as a card with:
   - Date heading (e.g., "Sat, February 7th, 2026") with **left purple/orange accent bar** (thin vertical rule)
   - Bullet-point TextEditor as default input mode — immediate cursor focus, zero chrome
   - Generous whitespace between day cards
   - Subtle container boundary (not visible borders — background color shift)

3. **Right sidebar context** — When Daily Notes is active, right sidebar shows:
   - Monthly mini-calendar widget (matching Reflect's style — grid with today highlighted)
   - Note actions: Pin this note, Share with private link, Show history

4. **SwiftData integration** — Create `DailyNote` model (or extend Intention) with:
   - `date: Date` (unique per day)
   - `content: String` (bullet-point markdown body)
   - `isPinned: Bool`
   - Auto-create today's entry on launch if absent

5. **Wire into navigation** — Add `.dailyNotes` case to SidebarSelection. Update ContentRouter. This should be the **default landing view** when app launches (matching Reflect behavior).

---

## Acceptance Checks

- [ ] Infinite scroll works in both temporal directions
- [ ] Today's note is auto-focused with cursor ready
- [ ] Left accent bar visible on today's date heading
- [ ] Mini-calendar in right sidebar with today highlighted
- [ ] Note actions (Pin, Share, History) visible in right sidebar
- [ ] DailyNote persists across app restarts (SwiftData)
- [ ] BUILD SUCCEEDS with zero errors

---

## Context Files

- `/Users/home/Desktop/HighCommand/HighCommand-resarch/reflect_exegesis.md` (Section II.1: The Daily Note)
- `/Users/home/Desktop/HighCommand/HighCommand-references/reflect/relflect-3.png` (Daily Notes screenshot)
- `/Users/home/Desktop/HighCommand/HighCommand-references/reflect/relflect-4.png` (Daily Notes screenshot 2)
- `/Users/home/Desktop/HighCommand/HighCommand/Views/NavigateView.swift` (existing temporal view to reference)
- `/Users/home/Desktop/HighCommand/HighCommand/Models/DomainModels.swift` (existing models)
- `/Users/home/Desktop/syncrescendence/-INBOX/commander/90_ARCHIVE/RESULT-commander-20260207-highcommand-saner-reflect-archaeology.md` (gap analysis)

---

## Expected Output

- New file: `HighCommand/Views/DailyNotesView.swift`
- New/modified model in `DomainModels.swift` (DailyNote @Model)
- Modified: `AppNavigationState.swift` (add .dailyNotes)
- Modified: `ContentView.swift` (wire ContentRouter)
- Modified: `SidebarView.swift` (default selection)
- RESULT file: `-INBOX/commander/00-INBOX0/RESULT-commander-YYYYMMDD-highcommand-reflect-phase5.md`
