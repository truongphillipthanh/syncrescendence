# CLARESCENCE: Doom Emacs Org-Mode Configuration Sprint
**Date**: 2026-02-09
**Author**: Commander
**Scope**: Doom Emacs as Constellation Observation Layer
**Status**: ACTIVE — Sprint items below

---

## Pass 1: Truth Surface (IS vs SHOULD-BE)

### Binary & Installation

| Aspect | IS | SHOULD-BE | Gap |
|--------|----|-----------|-----|
| Emacs variant | `emacs-plus@30` (29.4 dev) | `emacs-plus@30` (keep) | NONE — emacs-mac migration (DEC-LIFESTYLE-002) is CANCELLED. emacs-mac has native-comp freeze issues on Tahoe. emacs-plus@30 is stable. |
| Native compilation | MISSING (doom doctor warns) | Enabled via `--with-native-compilation` | CRITICAL — significant perf hit |
| Doom framework | `~/.config/emacs/` (3.0.0-pre) | Same | NONE |
| User config | `~/.config/doom/{init,config,packages}.el` | Same | NONE |
| Package count | 140 (straight.el) | ~150 after sprint additions | MINOR |

### Module Configuration (init.el)

| Module | IS | SHOULD-BE | Gap |
|--------|----|-----------|-----|
| org +roam | v1 (EOL, unmaintained) | +roam2 (v2, active) | CRITICAL — v1 is dead |
| org +journal | MISSING | ENABLED | MEDIUM — no daily notes system |
| org +pretty | Enabled | Keep | NONE |
| org +present | Enabled | Keep | NONE |
| org +dragndrop | MISSING | ENABLED | LOW — image drag-n-drop |
| org-habit | MISSING from org-modules | Add via `(add-to-list 'org-modules 'org-habit t)` | MEDIUM — no habit tracking |
| :checkers | EMPTY section | Add `syntax` | LOW |

### Config Quality (config.el)

| Aspect | IS | SHOULD-BE | Gap |
|--------|----|-----------|-----|
| API tokens | PLAINTEXT in config.el | `auth-source` (.authinfo.gpg) or env vars | SECURITY — exposed credentials |
| Frame alpha | 70% transparency | Match updated Ghostty (70%) | NONE |
| Frame padding | 8px internal-border | 4px (match Ghostty update) | COSMETIC |
| org-agenda-files | Only `orchestration/state/` | Add `-INBOX/*/00-INBOX0/` for capture.org files | MEDIUM — captured tasks invisible in agenda |
| org-roam flag | +roam (v1) | +roam2 (v2) — config.el roam settings need update for v2 API | CRITICAL |
| org-habit | Not loaded | `(add-to-list 'org-modules 'org-habit t)` | MEDIUM |
| org-journal | Not configured | Set `org-journal-dir`, date format, file type | MEDIUM |

### Launch & Integration

| Aspect | IS | SHOULD-BE | Gap |
|--------|----|-----------|-----|
| Launch location | Cartographer's nvim pane (wrong) | Own Ghostty window, Moom-tiled | CRITICAL — UX broken |
| Emacs server | On-demand (after-init-hook) | launchd plist (always-on) | MEDIUM — startup delay on emacsclient |
| EDITOR env var | `code --wait` (VS Code) | `emacsclient -nw` or leave as-is | LOW — VS Code is fine for git commits |
| Doom CLI in PATH | YES (`~/.config/emacs/bin`) | Keep | NONE |
| Dashboard alias | NONE | `doom-dash` alias → `emacsclient -nw -c` or `emacs -nw` | MEDIUM |

---

## Pass 2: Lifecycle Semantics

### Role in Cockpit

Doom Emacs is **Layer 7** of the Sovereign Cockpit — the **Observation Layer**. It is NOT a code editor. Its job:

1. **Org Agenda dashboard** — grouped view of all tasks across T0-T3
2. **Org Capture** — quick task/intention capture from any terminal
3. **Linear/ClickUp API views** — SaaS task boards in org buffers
4. **State file viewer** — read-only observation of orchestration state
5. **org-roam knowledge graph** — Syncrescendence corpus as networked notes

### Window Placement

Doom Emacs should run as:
- **Its own Ghostty window** (NOT inside the cockpit tmux session)
- Moom Classic tiles it alongside the cockpit and browser
- Launched via `emacsclient -nw -c` (terminal mode) or `emacs -nw`
- The launchd plist ensures the server is always ready

### Interaction Pattern

```
Sovereign sees notification → Ctrl+Space (Moom) → select Emacs tile
  → SPC d a (agenda) → review → SPC d s (cockpit state) → back to work
Quick capture: any terminal → emacsclient -e '(org-capture)' → template → done
```

---

## Pass 3: Decision Atoms

### DEC-EMACS-001: Cancel emacs-mac migration
- **Decision**: Keep `emacs-plus@30`, do NOT migrate to emacs-mac
- **Rationale**: emacs-mac has native-compilation freeze issues on macOS Tahoe (Doom issue #8554). emacs-plus@30 is stable and supports all needed features.
- **Reversibility**: HIGH — just `brew install emacs-mac` later if fixed
- **Action**: Reinstall emacs-plus@30 WITH native-compilation flag

### DEC-EMACS-002: org-roam v1 → v2
- **Decision**: Switch from `+roam` to `+roam2` in init.el
- **Rationale**: v1 is EOL, unmaintained, growing feature disparity
- **Reversibility**: MEDIUM — v2 has different DB schema, migration required
- **Action**: Change init.el, run `doom sync`, rebuild roam DB

### DEC-EMACS-003: API token security
- **Decision**: Move tokens to `~/.authinfo` (auth-source)
- **Rationale**: Plaintext tokens in config.el are visible to any process reading the file
- **Reversibility**: HIGH — can always put them back
- **Action**: Create `~/.authinfo`, update config.el to use `auth-source-search`

### DEC-EMACS-004: Emacs as independent window
- **Decision**: Emacs runs in its own Ghostty window, NOT inside cockpit tmux
- **Rationale**: The cockpit is a watch station. Emacs is a dashboard. Different windows, Moom-tiled.
- **Reversibility**: HIGH
- **Action**: Remove emacs from cockpit.sh panes, add launch alias, add launchd plist for server

### DEC-EMACS-005: Enable org-journal + org-habit
- **Decision**: Add +journal flag and org-habit module
- **Rationale**: Daily notes and habit tracking are core GTD primitives
- **Reversibility**: HIGH
- **Action**: Update init.el, add journal config to config.el

---

## Sprint Items

### S1: Reinstall emacs-plus@30 with native-compilation [DEC-EMACS-001]
```bash
brew uninstall emacs-plus@30
brew install emacs-plus@30 --with-native-compilation --with-modern-icon
doom sync
```
**Verification**: `doom doctor` shows no native-comp warning

### S2: Fix init.el modules [DEC-EMACS-002, DEC-EMACS-005]
Update `~/.config/doom/init.el`:
- Change `+roam` → `+roam2`
- Add `+journal` and `+dragndrop` to org flags
- Add `syntax` to `:checkers`

### S3: Update packages.el
Add:
- `(package! org-journal)` — if not pulled by +journal flag
- Any other needed packages

### S4: Comprehensive config.el rewrite [DEC-EMACS-003, DEC-EMACS-005]
- Move API tokens to `~/.authinfo` + auth-source
- Add org-habit to org-modules
- Configure org-journal (dir, date format, file type)
- Update frame padding to match Ghostty (4px)
- Add org-agenda custom commands with org-ql
- Update org-agenda-files to include inbox capture files
- Fix org-roam config for v2 API (different variable names)
- Add org-roam-ui package for graph visualization

### S5: Create launchd plist for emacs server [DEC-EMACS-004]
```xml
~/Library/LaunchAgents/com.syncrescendence.emacs-server.plist
```
- Launches `emacs --daemon` at login
- Ensures emacsclient is always instant

### S6: Shell integration [DEC-EMACS-004]
- Add `doom-dash` alias to `~/.zshrc`: `emacsclient -nw -c`
- Add `ec` alias: `emacsclient -nw`
- Add `org-capture` alias: `emacsclient -e '(org-capture)'`

### S7: Run doom sync + verify
```bash
doom sync
doom doctor
```
**Verification**: All modules load, no warnings, server starts clean

### S8: Remove emacs from cockpit nvim panes
- cockpit.sh already doesn't launch emacs (nvim panes launch nvim)
- Verify no leftover emacs processes in tmux

---

## Falsifiers

1. If `doom doctor` still warns about native-comp after S1 → reinstall failed
2. If org-roam DB doesn't build after S2 → v2 migration failed
3. If `emacsclient -nw` hangs → server plist not working
4. If agenda shows no items → agenda-files misconfigured
5. If org-capture fails → capture template paths wrong

---

**END CLARESCENCE**
