---
url: https://x.com/trq212/status/2014480496013803643
author: Thariq (@trq212)
captured_date: 2026-01-22
---

# We're turning Todos into Tasks in Claude Code

(Description: A task management interface showing a checklist with 4 done items and 6 open items, including grocery-related tasks with dependencies and blockers marked with strikethrough text)

## Introduction

Today, we're upgrading Todos in Claude Code to Tasks. Tasks are a new primitive that help Claude Code track and complete more complicated projects and collaborate on them across multiple sessions or subagents.

## Model Capabilities and Unhobbling

As model capabilities grow, one of the most important things we can do is "unhobble" Claude and allow it to use its new capabilities effectively. Compared to previous models, Opus 4.5 is able to run autonomously for longer and keep track of its state better. We found that the TodoWrite Tool was no longer necessary because Claude already knew what it needed to do for smaller tasks.

## The Need for Evolution

At the same time, we found ourselves using Claude Code to complete longer projects, sometimes across multiple subagents, context windows or sessions. But projects are more complex, tasks have dependencies and blockers and require coordination when using it across sessions.

It was clear we needed to evolve Todos to help Claude work on longer projects. This need was also emerging in the community and we took inspiration from projects like Beads by Steve Yegge.

## Tasks: The New Abstraction

Tasks are our new abstraction for coordinating many pieces of work across projects. Claude can create Tasks with dependencies on each other that are stored in the metadata, which mirrors more how projects work. Additionally, Tasks are stored in the file system so that multiple subagents or sessions can collaborate on them. When one session updates a Task, that is broadcasted to all sessions currently working on the same Task List.

## Creating and Using Tasks

You can ask Claude to create tasks right now, it's especially useful when spinning up subagents. Tasks are stored in `~/.claude/tasks`, you can use this to build additional utilities on top of tasks as well.

## Multi-Session Collaboration

To make sessions collaborate on a single Task List, you can set the TaskList as an environment variable and start Claude like so:
```
CLAUDE_CODE_TASK_LIST_ID=groceries claude
```

This also works for `claude -p` and the AgentSDK.

## Conclusion

Tasks are a key building block for allowing Claude to build more complex projects. We're looking forward to seeing how you use it.

---

**Engagement:** 308 replies, 702 reposts, 5.5K likes, 5.7K bookmarks, 1.9M views  
**Posted:** 3:29 PM · Jan 22, 2026