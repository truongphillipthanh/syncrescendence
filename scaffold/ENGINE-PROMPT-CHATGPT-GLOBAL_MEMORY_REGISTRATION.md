---
id: chatgpt-global-memory-registration
kind: memory_registration
scope: global
target: chatgpt
owner: Vanguard
---

# ChatGPT Global Memory Registration

Paste this into ChatGPT to register global preferences in Saved Memory.

---

Remember these global preferences for me across all chats:

1. Always trifurcate substantive responses into:
   * Inline readable content (normal markdown prose, no label)
   * Final transcript block (a single fenced code block at the very end—plain text, no markdown, no language tag, nothing after it)
   * Directive Pack only when executing (Context, Pedigree, Directives A/B/C)

2. The transcript block must always be last. Never output anything after the closing fence. No labels like "Readable version" or "Audizable version" anywhere.

3. In this workflow, "Blitzkrieg" means: produce Context, Pedigree, and Directives for lanes A/B/C with toolchain+model+success criteria+verification commands, intended for external executors.

4. Treat the repository as ground truth: use -INBOX for intake and -OUTGOING for exports/handoffs; avoid legacy outgoing/OUTGOING semantics.

After saving, tell me what you stored as saved memories in one concise paragraph.
