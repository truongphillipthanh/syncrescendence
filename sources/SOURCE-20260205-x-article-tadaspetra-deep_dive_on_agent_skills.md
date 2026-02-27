---
url: https://x.com/tadaspetra/status/2019204136982532407
author: "Tadas Petra (@tadaspetra)"
captured_date: 2026-02-04
id: SOURCE-20260205-017
original_filename: "20260205-x_article-deep_dive_on_agent_skills-@tadaspetra.md"
status: triaged
platform: x
format: article
creator: tadaspetra
signal_tier: tactical
topics:
  - ai-agents
  - context-management
  - testing
  - cursor
teleology: implement
notebooklm_category: ai-agents
aliases:
  - "Deep Dive on Agent Skills"
synopsis: "Deep Dive on Agent Skills I spent the last few weeks building elevenlabs/skills, which got 500+ installs in the first 24 hours. Here's everything I've learned about how to use and build Agent Skills. Agent Skills are folders containing context (mostly Markdown files) on a specific topic to increase the coding agent's likelihood of accomplishing a related task."
key_insights:
  - "Each of these folders must have a file named `SKILL.md` in the root of that folder."
  - "Progressive Disclosure The reason skills have become a go-to approach for developers is due to the way they manage context efficiently."
  - "How to Use Skills Once you have the skills in the appropriate location, in theory, the LLM should just be able to find them and use them when it is deemed useful."
---
# Deep Dive on Agent Skills

I spent the last few weeks building elevenlabs/skills, which got 500+ installs in the first 24 hours.

Here's everything I've learned about how to use and build Agent Skills.

(Description: Hero image showing "SKILLS" text with a person holding a microphone against a dark background, with folder structure visualization displaying agents, references, and other configuration files)

## What is an Agent?

Agent Skills are folders containing context (mostly Markdown files) on a specific topic to increase the coding agent's likelihood of accomplishing a related task.

These files live in a hidden folder that's currently different for each coding agents:

- `.claude/skills/` for Claude Code
- `.cursor/skills/` for Cursor
- `.opencode/skills/` for Open Code

(Description: File explorer visualization showing folder hierarchy with .agents, .claude, .codex, and .cursor folders displayed in a dark-themed interface)

If you only use one tool, that is a non-issue, but if you use multiple or like to test different ones time to time, it is a bit annoying. I recommend using [skills.sh](//skills.sh) tool from @vercel for managing skills. This uses a command to store all skills in a .agents/skills/ folder and then symlink them to all other folders, thus creating one source of truth.

It seems like many tools are updating to support the `.agents/` folder, so I expect not needing to symlink in the near future.

Each of these folders must have a file named `SKILL.md` in the root of that folder. This file needs to have at minimum `name` and a `description` defined in the frontmatter.

You can have nested folders within the skills folder containing additional information, which can be referenced by the `SKILL.md` file:

1. `scripts/` - Executable code that agents can run.
2. `references/` - More markdown files that can be used as additional documentation, when needed.
3. `assets/` - Static resources the agent can use.

## Progressive Disclosure

The reason skills have become a go-to approach for developers is due to the way they manage context efficiently. When you start your AI agent, it only loads the `name` and `description` into the context, so your LLM is aware of the type of skills it has access to.

When you make a request, the LLM can check if any of the skills apply to this request. If so, it retrieves only the `SKILL.md` file from the skills. Then it will use the skill, and only if the LLM decides it needs more information, it will load in the appropriate context from the `scripts/`, `references/`, or `assets/` folder.

## How to Use Skills

Once you have the skills in the appropriate location, in theory, the LLM should just be able to find them and use them when it is deemed useful.

However, LLMs are not perfect, so if I know that I have a skill and want to make sure it is used, I simply tell the LLM to use it.
```plaintext
Use the text-to-speech skill to create an audio file from the text within the input box.
```

These skills can also be installed on a per-project basis or per-user, so you have access to them across all projects. Project-based installation will have a `.claude/` folder within your project, and user-based installation will have it in the root of your user.

## How to Develop Skills

Again, these are just markdown files mostly. But there are some conventions and best practices that should be followed: https://agentskills.io/specification

The only MUST is that you have to have a `SKILL.md` file with a `name` and `description` front matter.

The actual content of that file can be anything, but it is recommended to be under 500 lines to keep the context at a reasonable size.

The main goal of this file is to give the LLM information about how to do the specific thing and what options are available for it. Here are some examples of things I added for the text-to-speech skill:

1. Quickstart
2. Available Models
3. Voice IDs
4. Voice Settings
5. Language Enforcement
6. Streaming
7. Error Handling

There is also a meta skill called skill-creator developed by anthropic that is used to help you write better skills: https://skills.sh/anthropics/skills/skill-creator.

I definitely recommend using this skill and even reading through the skill content to become a better reference/docs writer. And lastly, you can use @tessl_io to validate how good your skills are.

## How to Launch Skills

Once again, these are just files, so to launch them all you need to do is share the files. You can email them or send them any other way, but if you want them to be discoverable, make a GitHub repository with your skills and make it public.

They can be discovered on [skills.sh](//skills.sh), as long as they follow the format. This site crawls all public GitHub repos and looks for `SKILL.md` files. And when it finds them, it gets added to the directory automatically. This can take anywhere from a few hours to a few days.

(Description: Screenshot of skills.sh directory interface showing a table with SKILL names, descriptions, and installs count. Visible entries include: "text-to-speech" (283 installs), "speech-to-text" (95 installs), "agents" (80 installs), "setup-api-key" (67 installs), "sound-effects" (64 installs), and "music" (56 installs))

But even before it is listed, anybody can install your skills by running
```bash
npx skills add <owner/repo>
```

This command will start a easy to use terminal installer to help you install skills in the appropriate location and link them to the correct coding agents and projects.

That's all I got. If I missed something and you still have questions, leave a comment. And if you want to see an example of skills, you can find the repo here: https://github.com/elevenlabs/skills

---

**Engagement Stats:** 5 replies, 45 reposts, 452 likes, 792 bookmarks, 39.1K views  
**Published:** 4:19 PM · February 4, 2026