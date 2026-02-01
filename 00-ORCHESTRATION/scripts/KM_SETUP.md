# Keyboard Maestro Setup Instructions

**Version**: 1.0.0
**Generated**: 2026-01-23
**Prerequisites**: Keyboard Maestro 11.x (macOS automation app)

---

## Installation

1. Open Keyboard Maestro Editor
2. Create new macro group "Syncrescendence"
3. Set availability: All Applications
4. Create macros matching the specifications in `km_macros.yaml`

---

## Macro Group: Syncrescendence

### Group Settings
- **Name**: Syncrescendence
- **Available in**: All Applications (or specify: Terminal, VS Code, Claude.ai, ChatGPT)
- **Palette**: Optional (can create palette for quick access)

---

## Macros to Create

### Category 1: Handoff Macros

#### Macro: ChatGPT Handoff
- **Trigger**: `⌘⇧H`
- **Actions**:
  1. Get Clipboard → Variable `original_content`
  2. Set Clipboard to Text:
     ```
     ## HANDOFF FROM CLAUDE

     %Variable%original_content%

     ---
     Build upon this. Expand with ideas I wouldn't consider.
     ```
  3. Display Notification: "Content formatted for ChatGPT handoff"

#### Macro: Gemini Handoff
- **Trigger**: `⌘⇧G`
- **Actions**:
  1. Get Clipboard → Variable `original_content`
  2. Set Clipboard to Text:
     ```
     ## HANDOFF FOR ORACLE SENSING

     %Variable%original_content%

     ---
     Ingest fully. Identify patterns across corpus.
     ```
  3. Display Notification: "Content formatted for Gemini handoff"

#### Macro: Create Directive Template
- **Trigger**: `⌘⇧D`
- **Actions**:
  1. Prompt for User Input → Variable `directive_code`
     - Prompt: "Directive code (e.g., INFRASTRUCTURE-STABILIZATION):"
  2. Set Variable `today` to `%ICUDateTime%yyyy-MM-dd%`
  3. Set Variable `date_code` to `%ICUDateTime%yyyyMMdd%`
  4. Set Clipboard to Text:
     ```
     # DIRECTIVE: %Variable%directive_code%
     ## DIR-%Variable%date_code%-%Variable%directive_code%

     **Date**: %Variable%today%
     **From**: [ROLE]
     **To**: [ROLE]
     **Phase**: [PHASE]

     ---

     ## CONTEXT

     ## EXECUTION

     ## SUCCESS CRITERIA

     - [ ] [Criterion 1]

     ---

     ## HANDOFF TOKEN

     \`\`\`
     HANDOFF-%Variable%date_code%-[FROM]-TO-[TO]
     Directive: DIR-%Variable%date_code%-%Variable%directive_code%
     \`\`\`
     ```

---

### Category 2: Insertion Macros

#### Macro: Insert CANON Reference
- **Trigger**: Text Trigger `;canon`
- **Actions**:
  1. Prompt for User Input → Variable `canon_id`
     - Prompt: "CANON ID (5 digits):"
  2. Execute Shell Script:
     ```bash
     cd ~/Desktop/syncrescendence
     find 01-CANON -name "CANON-%Variable%canon_id%-*.md" | head -1 | xargs basename .md
     ```
     → Variable `canon_filename`
  3. Insert Text by Typing: `[[%Variable%canon_filename%]]`

#### Macro: Insert Timestamp
- **Trigger**: Text Trigger `;now`
- **Actions**:
  1. Insert Text by Typing: `%ICUDateTime%yyyy-MM-dd'T'HH:mm:ss%`

---

### Category 3: Navigation Macros

#### Macro: Open Terminal at Repo
- **Trigger**: `⌘⇧T`
- **Actions**:
  1. Activate Application "Terminal"
  2. Execute AppleScript:
     ```applescript
     tell application "Terminal"
         do script "cd ~/Desktop/syncrescendence && clear"
         activate
     end tell
     ```

#### Macro: Open Active Directive
- **Trigger**: `⌘⇧A`
- **Actions**:
  1. Execute Shell Script:
     ```bash
     cd ~/Desktop/syncrescendence
     ls -t 00-ORCHESTRATION/directives/DIRECTIVE-04*.md | head -1
     ```
     → Variable `latest_directive`
  2. Open File: `%Variable%latest_directive%`

#### Macro: Open Dashboard
- **Trigger**: `⌘⇧B`
- **Actions**:
  1. Open File: `~/Desktop/syncrescendence/00-ORCHESTRATION/state/DYN-DASHBOARD.md`

---

### Category 4: Git Macros

#### Macro: Git Status
- **Trigger**: `⌘⇧S`
- **Actions**:
  1. Activate Application "Terminal"
  2. Type Text: `cd ~/Desktop/syncrescendence && git status`
  3. Press Return

#### Macro: Git Pull
- **Trigger**: `⌘⇧P`
- **Actions**:
  1. Activate Application "Terminal"
  2. Type Text: `cd ~/Desktop/syncrescendence && git pull`
  3. Press Return

---

### Category 5: Analysis Macros

#### Macro: Count CANON Files
- **Trigger**: `⌃⌘C`
- **Actions**:
  1. Execute Shell Script:
     ```bash
     cd ~/Desktop/syncrescendence
     find 01-CANON -name "CANON-*.md" | wc -l | tr -d ' '
     ```
     → Variable `count`
  2. Display Text Large: "CANON files: %Variable%count%"

#### Macro: Pending Tasks Count
- **Trigger**: `⌃⌘T`
- **Actions**:
  1. Execute Shell Script:
     ```bash
     cd ~/Desktop/syncrescendence
     grep -c ",pending," 00-ORCHESTRATION/state/DYN-TASKS.csv || echo "0"
     ```
     → Variable `pending`
  2. Display Notification: "Pending tasks: %Variable%pending%"

---

## Keyboard Shortcut Reference

Quick reference card:

| Shortcut | Action | Category |
|----------|--------|----------|
| `⌘⇧H` | ChatGPT Handoff | Handoff |
| `⌘⇧G` | Gemini Handoff | Handoff |
| `⌘⇧D` | Directive Template | Handoff |
| `;canon` | Insert CANON Ref | Insertion |
| `;now` | Insert Timestamp | Insertion |
| `⌘⇧T` | Open Terminal | Navigation |
| `⌘⇧A` | Active Directive | Navigation |
| `⌘⇧B` | Dashboard | Navigation |
| `⌘⇧S` | Git Status | Git |
| `⌘⇧P` | Git Pull | Git |
| `⌃⌘C` | Count CANON | Analysis |
| `⌃⌘T` | Pending Tasks | Analysis |

---

## Testing

Test each macro after creation:

### Test Handoffs
1. Copy some text
2. Press `⌘⇧H`
3. Paste somewhere
4. Verify format includes "## HANDOFF FROM CLAUDE"

### Test Text Triggers
1. In any text field, type `;now`
2. Verify timestamp appears

### Test Git Macros
1. Press `⌘⇧S`
2. Verify Terminal opens and runs git status

---

## Troubleshooting

### Shortcuts Not Working

**Check**:
1. Keyboard Maestro Engine is running (menubar icon)
2. Macro group is enabled
3. No shortcut conflicts (System Preferences > Keyboard > Shortcuts)
4. Application is in "Available in" list

### Shell Scripts Failing

**Check**:
1. Path to syncrescendence is correct (`~/Desktop/syncrescendence`)
2. Execute permissions on scripts
3. Keyboard Maestro has Full Disk Access (System Preferences > Security)

### Variables Not Substituting

**Solution**: Ensure variable names match exactly (case-sensitive)

---

## Customization

Adjust shortcuts to avoid conflicts:

| Default | Alternative | Reason |
|---------|-------------|--------|
| `⌘⇧T` | `⌘⇧R` | If Terminal has conflict |
| `⌘⇧S` | `⌃⌘S` | If app uses Save As |
| `;canon` | `,canon` | If semicolon used elsewhere |

---

## Advanced: Macro Palettes

Create a palette for quick access without memorizing shortcuts:

1. Macro Group → Enable "Show a palette..."
2. Configure trigger: `⌘⇧Space` or `F1`
3. Palette appears on trigger, shows all macros
4. Click or type number to execute

---

## Export/Backup

Backup your macros:

1. File → Export Macros...
2. Select "Syncrescendence" group
3. Save to: `-OUTGOING/` or safe location
4. Filename: `Syncrescendence-KM-Macros-YYYYMMDD.kmmacros`

---

## Future: XML Generation

Planned improvement: Generate `.kmmacros` XML file for direct import from `km_macros.yaml`.

For now: **Manual macro creation** following these specs.

---

**Status**: Manual setup guide for Keyboard Maestro automation. XML generation planned for future release.
