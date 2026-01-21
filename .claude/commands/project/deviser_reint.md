---
name: deviser_reint
description: Generate end-of-session continuity export for Deviser webapp reinitialization
allowed-tools: Bash, Read, Write, Glob
---
# Deviser Reinitialization Export

Generate a complete continuity export package for cross-platform session handoff.

## Execution

### Step 1: Compute Timestamp and Create Directories

```bash
DATE=$(date +%Y%m%d)
OUTDIR="-OUTGOING/${DATE}-deviser_reinit"
INBOXDIR="-INBOX/${DATE}-deviser_reinit"
BUNDLE_DIR="${OUTDIR}/04_repo_ground_truth_bundle"

mkdir -p "${OUTDIR}/00_manifest"
mkdir -p "${BUNDLE_DIR}"
mkdir -p "${INBOXDIR}"

echo "Created: ${OUTDIR}"
echo "Created: ${INBOXDIR}"
```

### Step 2: Generate 00_manifest/environment.md

```bash
DATE=$(date +%Y%m%d)
OUTDIR="-OUTGOING/${DATE}-deviser_reinit"

cat > "${OUTDIR}/00_manifest/environment.md" << 'ENVEOF'
# Environment Manifest
ENVEOF

cat >> "${OUTDIR}/00_manifest/environment.md" << ENVEOF
**Generated**: $(date '+%Y-%m-%d %H:%M:%S')
**Git HEAD**: $(git rev-parse HEAD)
**Branch**: $(git branch --show-current)

## Git Status Summary
\`\`\`
$(git status --short)
\`\`\`

## Working Directory
\`\`\`
$(pwd)
\`\`\`
ENVEOF

echo "Generated: ${OUTDIR}/00_manifest/environment.md"
```

### Step 3: Generate repo_tree_depth6.txt

```bash
DATE=$(date +%Y%m%d)
OUTDIR="-OUTGOING/${DATE}-deviser_reinit"

# Generate tree with depth 6, excluding common noise
find . -maxdepth 6 -type d \( -name ".git" -o -name "node_modules" -o -name ".obsidian" \) -prune -o -type f -print 2>/dev/null | head -500 > "${OUTDIR}/00_manifest/repo_tree_depth6.txt"

echo "Generated: ${OUTDIR}/00_manifest/repo_tree_depth6.txt ($(wc -l < "${OUTDIR}/00_manifest/repo_tree_depth6.txt") entries)"
```

### Step 4: Generate session_archaeology.md

```bash
DATE=$(date +%Y%m%d)
OUTDIR="-OUTGOING/${DATE}-deviser_reinit"

cat > "${OUTDIR}/00_manifest/session_archaeology.md" << 'ARCHEOF'
# Session Archaeology
ARCHEOF

cat >> "${OUTDIR}/00_manifest/session_archaeology.md" << ARCHEOF

**Generated**: $(date '+%Y-%m-%d %H:%M:%S')

## Recent Commits (last 20)

\`\`\`
$(git log --oneline -20)
\`\`\`

## Diffstat Since Last Commit

\`\`\`
$(git diff --stat HEAD 2>/dev/null || echo "No uncommitted changes")
\`\`\`

## Uncommitted Changes Summary

\`\`\`
$(git status --short)
\`\`\`

## Files Modified Since Last Commit

\`\`\`
$(git diff --name-only HEAD 2>/dev/null || echo "None")
\`\`\`
ARCHEOF

echo "Generated: ${OUTDIR}/00_manifest/session_archaeology.md"
```

### Step 5: Generate 01_deviser_thread_culmination_prompt.md

Create the exact "select all + copy" prompt for Deviser webapp culmination/compaction.

```bash
DATE=$(date +%Y%m%d)
OUTDIR="-OUTGOING/${DATE}-deviser_reinit"
INBOXDIR="-INBOX/${DATE}-deviser_reinit"

cat > "${OUTDIR}/01_deviser_thread_culmination_prompt.md" << 'PROMPTEOF'
This thread has reached a natural culmination point. Before we compact or archive:

1. **Synthesize Key Decisions**: What architectural, strategic, or tactical decisions were made in this thread that must persist?

2. **Extract Unique Context**: What contextual understanding developed during this conversation that would be expensive to reconstruct?

3. **Identify Open Loops**: What work was started but not completed? What questions remain unanswered?

4. **State Artifacts**: List any files, prompts, or code that should be preserved with explicit paths.

5. **Continuation Vector**: If a new thread continues this work, what is the single most important thing it must understand?

Format your response as a structured handoff document I can attach to a new thread or archive for future reference.
PROMPTEOF

# Copy to -INBOX for webapp attachment
cp "${OUTDIR}/01_deviser_thread_culmination_prompt.md" "${INBOXDIR}/"

echo "Generated: ${OUTDIR}/01_deviser_thread_culmination_prompt.md"
echo "Copied to: ${INBOXDIR}/01_deviser_thread_culmination_prompt.md"
```

### Step 6: Generate 02_deviser_thread_artifacts_manifest.md

```bash
DATE=$(date +%Y%m%d)
OUTDIR="-OUTGOING/${DATE}-deviser_reinit"
INBOXDIR="-INBOX/${DATE}-deviser_reinit"

cat > "${OUTDIR}/02_deviser_thread_artifacts_manifest.md" << 'MANIFESTEOF'
# Deviser Thread Artifacts Manifest

## CRUCIAL Artifacts to Port

These artifacts cannot be coherently compressed and must be explicitly attached to or referenced in the new thread.

### Operator Instructions

For each artifact below:
1. Check if it exists and is current
2. Either attach the file to the new thread, or paste a URL
3. Mark [x] when done

---

### Checklist

- [ ] **CLAUDE.md** (Constitution)
  - Path: `./CLAUDE.md`
  - Why: Defines all operational invariants and constitutional rules
  - Action: Attach or paste content

- [ ] **COCKPIT.md** (Navigation)
  - Path: `./COCKPIT.md`
  - Why: System navigation index and current state
  - Action: Attach or paste content

- [ ] **system_state.json** (Current State Vector)
  - Path: `./00-ORCHESTRATION/state/system_state.json`
  - Why: Oracle number, blitzkrieg state, mode
  - Action: Attach or paste content

- [ ] **Active Directive** (If any)
  - Path: `./00-ORCHESTRATION/directives/DIRECTIVE-XXX.md`
  - Why: Current execution context
  - Action: Identify active directive, attach if exists

- [ ] **REF-STANDARDS.md** (18 Lenses)
  - Path: `./00-ORCHESTRATION/state/REF-STANDARDS.md`
  - Why: Decision framework
  - Action: Reference only (large file)

- [ ] **Recent Git Log**
  - Command: `git log --oneline -10`
  - Why: Establishes recent history context
  - Action: Paste output

- [ ] **Uncommitted Changes** (If any)
  - Command: `git diff --stat`
  - Why: Work in progress that may need continuation
  - Action: Paste output or note "None"

---

### Optional Context

- [ ] **Oracle Context** (If relevant)
  - Path: `./00-ORCHESTRATION/oracle_contexts/ORACLE[N]_CONTEXT.md`
  - Why: Strategic session context

- [ ] **coordination.yaml** (Multi-agent)
  - Path: `./02-OPERATIONAL/coordination.yaml`
  - Why: Platform constellation for multi-agent work

---

## Notes

Add any session-specific notes here about what the new thread must understand:

```
[OPERATOR: Add notes here before attaching to new thread]
```
MANIFESTEOF

# Copy to -INBOX for webapp attachment
cp "${OUTDIR}/02_deviser_thread_artifacts_manifest.md" "${INBOXDIR}/"

echo "Generated: ${OUTDIR}/02_deviser_thread_artifacts_manifest.md"
echo "Copied to: ${INBOXDIR}/02_deviser_thread_artifacts_manifest.md"
```

### Step 7: Generate 03_chatgpt_webapp_reinit_prompt.md

```bash
DATE=$(date +%Y%m%d)
OUTDIR="-OUTGOING/${DATE}-deviser_reinit"

cat > "${OUTDIR}/03_chatgpt_webapp_reinit_prompt.md" << REINITEOF
You are continuing work on the Syncrescendence knowledge management system. A previous session has ended and I'm providing you with continuity artifacts.

## Immediate Context

This is a **Claude Code** managed repository. The canonical rules are in CLAUDE.md. The navigation index is COCKPIT.md.

## Attached Artifacts

I have attached (or will paste) the following from \`-INBOX/${DATE}-deviser_reinit/\`:

1. **01_deviser_thread_culmination_prompt.md** - The culmination synthesis from the previous thread
2. **02_deviser_thread_artifacts_manifest.md** - Checklist of crucial artifacts

## Repository Ground Truth

A complete repository bundle exists at:
\`-OUTGOING/${DATE}-deviser_reinit/04_repo_ground_truth_bundle/\`

This contains:
- \`repo.bundle\` - Git bundle of entire repository
- \`working_tree.patch\` - Any uncommitted changes
- \`notes.md\` - Restoration instructions

## Your Task

1. Review the attached culmination synthesis
2. Understand the current repository state from the artifacts
3. Ask me what I want to work on next, or continue any open loops identified

Do not assume what I want to do. Wait for my instruction after reviewing the context.
REINITEOF

echo "Generated: ${OUTDIR}/03_chatgpt_webapp_reinit_prompt.md"
```

### Step 8: Generate Repo Ground Truth Bundle

```bash
DATE=$(date +%Y%m%d)
OUTDIR="-OUTGOING/${DATE}-deviser_reinit"
BUNDLE_DIR="${OUTDIR}/04_repo_ground_truth_bundle"

# Create git bundle with all refs
git bundle create "${BUNDLE_DIR}/repo.bundle" --all 2>&1

# Capture uncommitted changes as patch (if any)
if [ -n "$(git status --porcelain)" ]; then
    git diff HEAD > "${BUNDLE_DIR}/working_tree.patch"
    git diff --cached >> "${BUNDLE_DIR}/working_tree.patch"
    echo "Created working_tree.patch with uncommitted changes"
else
    echo "# No uncommitted changes" > "${BUNDLE_DIR}/working_tree.patch"
    echo "No uncommitted changes to capture"
fi

# Create restoration notes
cat > "${BUNDLE_DIR}/notes.md" << NOTESEOF
# Repository Ground Truth Bundle

**Created**: $(date '+%Y-%m-%d %H:%M:%S')
**Git HEAD**: $(git rev-parse HEAD)

## Contents

- \`repo.bundle\` - Complete git repository bundle (all branches, all history)
- \`working_tree.patch\` - Uncommitted changes at time of export (if any)

## Restoration Instructions

### To clone from bundle:

\`\`\`bash
# Clone the bundle to a new directory
git clone repo.bundle syncrescendence-restored

# Enter the directory
cd syncrescendence-restored

# Add the original remote (if needed)
git remote add origin <original-remote-url>
\`\`\`

### To apply uncommitted changes:

\`\`\`bash
# After cloning from bundle
git apply working_tree.patch
\`\`\`

### To update an existing clone:

\`\`\`bash
# Fetch from bundle
git fetch /path/to/repo.bundle

# Or pull specific branch
git pull /path/to/repo.bundle main
\`\`\`

## Verification

After restoration, verify with:

\`\`\`bash
git log --oneline -5  # Should match original
git status            # Should be clean (or match working_tree.patch)
\`\`\`
NOTESEOF

echo "Generated: ${BUNDLE_DIR}/notes.md"
```

### Step 9: Create ZIP of Bundle

```bash
DATE=$(date +%Y%m%d)
OUTDIR="-OUTGOING/${DATE}-deviser_reinit"
BUNDLE_DIR="${OUTDIR}/04_repo_ground_truth_bundle"

# Create zip of the bundle directory
cd "${OUTDIR}"
zip -r "repo_ground_truth_${DATE}.zip" "04_repo_ground_truth_bundle/"
cd - > /dev/null

echo "Created: ${OUTDIR}/repo_ground_truth_${DATE}.zip"
```

### Step 10: Final Summary

```bash
DATE=$(date +%Y%m%d)
OUTDIR="-OUTGOING/${DATE}-deviser_reinit"
INBOXDIR="-INBOX/${DATE}-deviser_reinit"

echo ""
echo "=== DEVISER REINIT EXPORT COMPLETE ==="
echo ""
echo "Output directory: ${OUTDIR}/"
echo ""
echo "Contents:"
ls -la "${OUTDIR}/"
echo ""
echo "Manifest:"
ls -la "${OUTDIR}/00_manifest/"
echo ""
echo "Bundle:"
ls -la "${OUTDIR}/04_repo_ground_truth_bundle/"
echo ""
echo "-INBOX staging:"
ls -la "${INBOXDIR}/"
echo ""
echo "=== NEXT STEPS ==="
echo "1. Review the culmination prompt and run it in your current Deviser thread"
echo "2. Copy the response to a file (optional)"
echo "3. In a NEW thread, paste 03_chatgpt_webapp_reinit_prompt.md"
echo "4. Attach files from ${INBOXDIR}/ to the new thread"
echo "5. Continue work"
```

## Output

A complete export package in `-OUTGOING/YYYYMMDD-deviser_reinit/` with:
- `00_manifest/` - Environment, tree, session archaeology
- `01_deviser_thread_culmination_prompt.md` - Compaction prompt
- `02_deviser_thread_artifacts_manifest.md` - Artifact checklist
- `03_chatgpt_webapp_reinit_prompt.md` - New thread initialization prompt
- `04_repo_ground_truth_bundle/` - Git bundle + patch + restoration notes
- `repo_ground_truth_YYYYMMDD.zip` - Zipped bundle

And `-INBOX/YYYYMMDD-deviser_reinit/` with webapp-facing artifacts ready for attachment.
