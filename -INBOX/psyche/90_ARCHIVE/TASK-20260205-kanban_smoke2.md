# TASK-${DATE}-${TOPIC_SLUG}

**From**: ${CALLER}
**To**: ${AVATAR}
**Issued**: ${TIMESTAMP}
**Fingerprint**: ${FINGERPRINT}
**Kind**: ${KIND_RAW}
**Priority**: P1
**Status**: PENDING
**Kanban**: INBOX0
**Claimed-By**: —
**Claimed-At**: —
**Completed-At**: —
**Exit-Code**: —
**Timeout**: 30
**CC**: ${CC_RAW}
**Receipts-To**: ${RECEIPTS_TO}

---

## Objective

$DESCRIPTION

---

## Context Files

Consult as needed:
- \`COCKPIT.md\` — Constellation overview
- \`CLAUDE.md\` — Constitutional rules
- \`00-ORCHESTRATION/state/ARCH-INTENTION_COMPASS.md\` — Active intentions
- \`02-ENGINE/DEF-CONSTELLATION_VARIABLES.md\` — Global definitions

## Expected Output

- Write results to `-OUTBOX/${AGENT}/RESULTS/RESULT-${AGENT}-${DATE}-${TOPIC_SLUG}.md`
- Or commit directly if you have write access

## Completion Protocol

1. Write output to the specified location
2. Update **Status** above from PENDING to COMPLETE
3. If cross-machine: \`git add -A && git commit -m "task: ${TOPIC_SLUG} complete" && git push\`
