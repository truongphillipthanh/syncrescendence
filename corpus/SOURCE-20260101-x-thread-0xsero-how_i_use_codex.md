# How I use Codex

**step 1:**

- Setup **GPT-5.2-XHIGH** and tell it to read every files under what directory I want to work in
- Have it produce a map of the code, and a scope that is relevant to the big goal I want to accomplish
- Have it make a directory called /tasks where it makes 1 **task-00.md** file in a sequence

**step 2:**

- Switch to **gpt-5.2-codex-xhigh**
- Attach the scope, the rules, and the **task-00.md**
- Push the same message but change the number **task-01.md**

The scope is the big picture. What we are trying to do, what it touches, why we made certain decisions etc..

The rules file is the instructions it has to follow during development:

1. checkout new branch when starting a task
2. complete the task as described, attempt to reduce code not make more for older projects.
3. run type-check, lint, full test suite (not deleting or skipping tests), commit and push
4. update documentation

Each task will take between 15 minutes and 1 hour, you can stack them on top each other so codex only sees 1 per turn.

2-24 hour runs depending on how well you specify
all code is typically functional
improved, cleaner code,

(Description: Screenshot showing a dark-themed code editor/IDE interface with file tree on the left, code content in the center and right panels. The interface displays development environment setup with multiple file tabs and code syntax highlighting.)

---

**Jan 1, 2026 · 11:26 AM**

---

The reason I do this is so I can chain prompts to get it running for long periods

---

Codex executes
GPT plans

Codex sucks at planning it asks too many questions

---

Thanks for pointing this out

---

**Jan 2, 2026**

I haven't hit any usage limits

---

**Jan 8, 2026**

[Reference to x.com/0xsero/status/...]