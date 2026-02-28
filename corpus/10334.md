# Claude Code: CLAUDE.md Loading Behavior

**@bcherny · Jan 27, 2026**

In case it's not clear in the docs:

- **Ancestor** `CLAUDE.md`'s are loaded into context automatically on startup
- **Descendent** `CLAUDE.md`'s are loaded *lazily* only when Claude reads/writes files in a folder the `CLAUDE.md` is in. Think of it as a special kind of skill.

We designed it this way for monorepos and other big repos, tends to work pretty well in practice.

---

**@bcherny · Jan 27, 2026**
```
CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 claude
```