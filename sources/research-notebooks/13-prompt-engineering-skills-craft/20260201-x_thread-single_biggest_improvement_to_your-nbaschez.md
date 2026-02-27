---
url: https://x.com/nbaschez/status/2018027072720130090
author: Nathan Baschez (@nbaschez)
captured_date: 2026-02-01
---

# X Thread: Bug Testing and Agentic Development

**Post 1** — 10:22 AM · Feb 1, 2026

Single biggest improvement to your CLAUDE.md / AGENTS.md:

"When I report a bug, don't start by trying to fix it. Instead, start by writing a test that reproduces the bug. Then, have subagents try to fix the bug and prove it with a passing test."

---

**Post 2** — Feb 1

i don't have a soundcloud but if you're looking for work as an AI engineer (or to hire an AI engineer) check out ai-eng.market

---

**Post 3** — Feb 1

Ahh yes 100% I made a "UX specs" folder which is a bunch of markdown files with instructions for using the Vercel agent browser CLI, it's wildly handy as a layer one higher than regular e2e tests

---

**Post 4** — Feb 1

if you just say "write some tests" 100% agree it will do that if you say "write a test that actually reproduces this bug" much harder to fail

---

**Post 5** — Feb 1

Interesting

---

**Post 6** — Feb 1

try it! in my experience it helps to spell it out slightly more

---

**Post 7** — Feb 1

(Description: Text image titled "Bug Fixes: Prove It Pattern" with the following content:

When given a bug or error report, the first step is to spawn a subagent to write a test that reproduces the issue. Only proceed once reproduction is confirmed.

Test level hierarchy — Reproduce at the lowest level that can capture the bug:

1. Unit test — Pure logic bugs, isolated functions (lives next to the code)
2. Integration test — Component interactions, API boundaries (lives next to the code)
3. UX spec test — Full user flows, browser-dependent behavior (lives in apps/web/specs/)

For every bug fix:

1. Reproduce with subagent — Spawn a subagent to write a test that demonstrates the bug. The test should fail before the fix.
2. Fix — Implement the fix.
3. Confirm — The test now passes, proving the fix works.

If the bug is truly environment-specific or transient, document why a test isn't feasible rather than skipping silently.)

---

**Post 8** — Feb 1

here's the exact prompt

---

**Post 9** — Feb 1

Agent can edit

---

**Post 10** — Feb 1

yes

---

**Post 11** — Feb 2

Yeah true! Probably best is both - put in CLAUDE.md to use the skill, then have detailed instructions in the skill itself