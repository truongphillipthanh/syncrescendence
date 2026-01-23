# Hazel Setup Instructions

**Version**: 1.0.0
**Generated**: 2026-01-23
**Prerequisites**: Hazel 5.x (macOS automation app)

---

## Installation

1. Open Hazel preferences
2. Add folders to watch (see below)
3. Create rules matching the specifications in `hazel_rules.yaml`
4. Test with sample files before enabling auto-move rules

---

## Folders to Watch

Add these folders in Hazel:

| Folder | Purpose |
|--------|---------|
| `~/Downloads` | Intake point for all Syncrescendence files |
| `~/Desktop/syncrescendence/-INBOX` | Sorting and triage staging |
| `~/Desktop/syncrescendence/00-ORCHESTRATION/execution_logs` | Auto-archive old logs |
| `~/Desktop/syncrescendence/00-ORCHESTRATION/directives` | Auto-archive old directives (optional) |
| `~/Desktop/syncrescendence` (root) | Cleanup rules (.DS_Store, temp files) |

---

## Rules to Create

### 1. ~/Downloads Folder

#### Rule: Intake Markdown
- **Conditions**: Extension is `md`
- **Actions**: Move to `~/Desktop/syncrescendence/-INBOX/`
- **Note**: Will capture all .md files—adjust if needed

####  Rule: Intake Text (Transcripts)
- **Conditions**: Extension is `txt` AND (Name contains "transcript" OR "youtube" OR "SOURCE")
- **Actions**: Move to `~/Desktop/syncrescendence/-INBOX/`

#### Rule: Intake CSV
- **Conditions**: Extension is `csv` AND Name contains "syncrescendence"
- **Actions**: Move to `~/Desktop/syncrescendence/-INBOX/`

#### Rule: Intake PDF
- **Conditions**: Extension is `pdf` AND Name contains "syncrescendence"
- **Actions**: Move to `~/Desktop/syncrescendence/-INBOX/`

---

### 2. ~/Desktop/syncrescendence/-INBOX Folder

#### Rule: Sort to Sources (DISABLED BY DEFAULT)
- **Conditions**: Name contains "transcript" OR "SOURCE"
- **Actions**: Move to `~/Desktop/syncrescendence/04-SOURCES/raw/`
- **⚠️ Enable only after testing**: Auto-filing skips triage

#### Rule: Alert on CANON Files
- **Conditions**: Name starts with "CANON"
- **Actions**:
  - Show notification: "CANON file in INBOX - MANUAL REVIEW REQUIRED"
  - Add tag "protected"
- **Note**: Alert only, no auto-move (CANON is PROTECTED)

---

### 3. ~/Desktop/syncrescendence/00-ORCHESTRATION/execution_logs

#### Rule: Archive Old Logs
- **Conditions**:
  - Date Last Modified is not in the last 30 days
  - Name matches "EXECUTION_LOG-*"
- **Actions**: Move to `~/Desktop/syncrescendence/05-ARCHIVE/execution-logs/`

---

### 4. ~/Desktop/syncrescendence (Root)

#### Rule: Remove .DS_Store
- **Conditions**: Name is `.DS_Store`
- **Actions**: Move to Trash (or Delete Immediately)
- **Recursive**: Yes (apply to all subfolders)

#### Rule: Clean Temp Files
- **Conditions**:
  - Extension is `tmp`, `temp`, or `bak`
  - Date Last Modified is not in the last 1 day
- **Actions**: Move to Trash
- **Recursive**: Yes

#### Rule: Alert on Large Files
- **Conditions**: Size is greater than 5 MB
- **Actions**:
  - Show notification: "Large file added - consider offload"
  - Add tag "large-file"
- **Recursive**: Yes
- **Note**: Monitoring only, no auto-action

---

## Verification

After setup, test each rule:

### Test 1: Intake
1. Save a test `.md` file to `~/Downloads` named `test-syncrescendence.md`
2. Verify it appears in `-INBOX` within 5 seconds
3. Check Hazel log for any errors

### Test 2: Cleanup
1. Create a `.DS_Store` file somewhere in the repo
2. Verify Hazel removes it within 1 minute
3. Check Hazel log

### Test 3: Archiving
1. Check existing execution logs
2. Manually trigger archive rule (right-click in Hazel)
3. Verify logs move to `05-ARCHIVE/execution-logs/`

---

## Troubleshooting

### Rules Not Triggering

**Check**:
1. Folder is added to Hazel and monitored
2. Rule conditions are correct (case-sensitive!)
3. Hazel has Disk Access permissions (System Preferences > Security)
4. Hazel menubar icon shows "Active"

### Files Not Moving

**Check**:
1. Destination folder exists
2. No permission issues (try moving manually first)
3. File isn't locked or in use
4. Check Hazel log for specific error

### Too Many False Positives

**Solution**: Add more specific conditions
- Example: Instead of "Extension is md", use "Extension is md AND Name contains syncrescendence"

---

## Safety Notes

- ⚠️ Rules marked `DISABLED BY DEFAULT` should remain disabled until thoroughly tested
- ⚠️ CANON and directive rules require manual review—never auto-file
- ⚠️ Always verify moves before emptying trash
- ⚠️ Keep Hazel logs enabled for 30 days for audit trail

---

## Customization

Adjust these values based on your workflow:

| Setting | Default | Adjust To |
|---------|---------|-----------|
| Archive timing (logs) | 30 days | 60 days (if you want longer retention) |
| Archive timing (directives) | 60 days | Never (keep all directives active) |
| File size threshold | 5MB | 10MB (if you work with larger files) |
| Temp file cleanup | 1 day | 7 days (if you use temps longer) |

---

## Advanced: Hazel Rule Export

Future improvement: Generate `.hazelrules` file for direct import from `hazel_rules.yaml`.

For now: **Manual rule creation** following these specs.

---

## Monitoring

Check Hazel activity:
1. Open Hazel preferences
2. Click folder name
3. View "Info" tab → Recent activity log
4. Verify rules are firing as expected

---

**Status**: Manual setup guide for Hazel automation. Import automation planned for future release.
