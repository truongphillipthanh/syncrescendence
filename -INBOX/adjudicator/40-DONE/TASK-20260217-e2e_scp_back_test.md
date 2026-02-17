# TASK: End-to-end Neural Bridge SCP-back verification test

**Status**: PENDING
**Priority**: P0
**Reply-To**: commander
**CC**: commander
**To**: adjudicator
**Timeout**: 300

## Objective

Prove the full CONFIRM SCP-back chain works end-to-end. This is the final verification that the Neural Bridge is truly operational.

## Test 1: Verify env vars in running auto_ingest_loop

```bash
tail -3 ~/Desktop/syncrescendence/-INBOX/adjudicator/auto_ingest.log
```
Must show `Neural Bridge env:` line with `AJNA=macbook-air`.

## Test 2: Simulate CONFIRM SCP-back

Create a test CONFIRM file and SCP it to MBA (simulating what auto_ingest_loop does):

```bash
# Create test CONFIRM
echo "# TEST-CONFIRM-SCP-BACK
**Kind**: TEST
**From-Agent**: adjudicator
**To-Agent**: commander
**Status**: TEST-PASS
**Completed-At**: $(date -u '+%Y-%m-%dT%H:%M:%SZ')
This is a test of the Neural Bridge CONFIRM SCP-back mechanism." > /tmp/TEST-CONFIRM-scp-back.md

# SCP it to MBA commander inbox (same path auto_ingest uses)
scp -o BatchMode=yes -o ConnectTimeout=5 /tmp/TEST-CONFIRM-scp-back.md macbook-air:~/Desktop/syncrescendence/-INBOX/commander/00-INBOX0/TEST-CONFIRM-scp-back.md

# Check exit code
echo "SCP exit code: $?"
```

Expected: exit code 0.

## Test 3: Verify file arrived on MBA

```bash
ssh -o ConnectTimeout=5 macbook-air "ls -la ~/Desktop/syncrescendence/-INBOX/commander/00-INBOX0/TEST-CONFIRM-scp-back.md && cat ~/Desktop/syncrescendence/-INBOX/commander/00-INBOX0/TEST-CONFIRM-scp-back.md"
```

Expected: file exists with correct content.

## Test 4: Verify reverse path (MBA → Mac mini)

```bash
ssh -o ConnectTimeout=5 macbook-air "echo 'TEST-REVERSE-PATH' > /tmp/test-reverse.md && scp -o BatchMode=yes -o ConnectTimeout=5 /tmp/test-reverse.md mini:~/Desktop/syncrescendence/-INBOX/adjudicator/00-INBOX0/TEST-REVERSE-PATH.md && echo 'REVERSE SCP OK' || echo 'REVERSE SCP FAILED'"

# Check if it arrived locally
ls -la ~/Desktop/syncrescendence/-INBOX/adjudicator/00-INBOX0/TEST-REVERSE-PATH.md 2>/dev/null && echo "REVERSE FILE ARRIVED" || echo "REVERSE FILE MISSING"
```

## Test 5: Clean up test files

```bash
rm -f /tmp/TEST-CONFIRM-scp-back.md /tmp/test-reverse.md
ssh macbook-air "rm -f ~/Desktop/syncrescendence/-INBOX/commander/00-INBOX0/TEST-CONFIRM-scp-back.md" 2>/dev/null
rm -f ~/Desktop/syncrescendence/-INBOX/adjudicator/00-INBOX0/TEST-REVERSE-PATH.md 2>/dev/null
```

## Verdict

Write RESULT with:
```
NEURAL BRIDGE END-TO-END TEST:
- Test 1 (env vars in process): PASS/FAIL
- Test 2 (SCP to MBA): PASS/FAIL  
- Test 3 (file verification): PASS/FAIL
- Test 4 (reverse path): PASS/FAIL
- OVERALL: PASS/FAIL
```

**Reply-To**: commander
**CC**: commander
