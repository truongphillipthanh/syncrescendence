---
id: SOURCE-20260116-x-article-paulsolt-if_youre_new_to_codex_here_are_7_beginner_tips
date_published: "2026-01-16"
platform: x
format: article
creator: paulsolt
title: if youre new to codex here are 7 beginner tips
status: triaged
url: https://x.com/PaulSolt/status/2012010080414081188
original_filename: "if_youre_new_to_codex_here_are_7_beginner_tips-@paulsolt.md"
signal_tier: tactical
topics:
  - "vibe-coding"
  - "developer-tools"
  - "tutorial"
teleology: implement
notebooklm_category: coding-tools
aliases:
  - "PaulSolt - Codex Beginner Tips"
synopsis: "Seven beginner tips for OpenAI Codex: start with GPT-5.2-Codex high, use clear prompts, leverage the queue feature, and other practical getting-started advice for new Codex users."
key_insights:
  - "Start with GPT-5.2-Codex high reasoning effort as the default for balanced speed and quality"
  - "Clear concise prompts with specific context produce better results than verbose instructions"
  - "The queue feature enables batching multiple tasks for continuous agent execution"
---
1. Start with:

GPT-5.2-Codex high

That is high reasoning. It is enough. Don't be tempted with xhigh unless working on something really tricky. It uses more tokens and will be slower to finish.

2. Sometimes more reasoning may not help. You may need to give your agents better docs that are up to date. I prefer to have my agents create Markdown docs from DocSet that are local, instead of web scraping.

I use DocSetQuery to create docs from Dash DocSet bundles. https://github.com/PaulSolt/DocSetQuery…

3. Read 
@steipete
 post to get started.

Bookmark his blog and follow him. Read his post, it's gold, and so are his other workflow posts.

https://steipete.me/posts/2025/shipping-at-inference-speed…

4. Copy aspects from Peter's agents .md file and make it your own. There's thousands of hours of learnings in his open source projects.

https://github.com/steipete/agent-scripts…

Use the scripts too, things like committer for atomic commits are super powerful when multiple agents work in one folder.

5. Just talk to codex. You don't need complex rules. You don't need to create huge Plan .md  files. 

You can get really good results by just working on one aspect of a feature at a time, handing it off, and then letting Codex do it. 

If you get bored waiting start up another project while you wait. Ask it to do something and then go back to the original one. Most likely it will be done unless you're doing a huge refactor. 

6. You can always ask your agent to copy something from another project. Peter does this all the time and has agents leveraging work they've already done for new projects.

I ask my agents to create Makefiles to build and run my apps. For new projects I have them copy the structure. See my workflow video: How I use Codex GPT 5.2 with Xcode (My Complete Workflow)
https://youtu.be/o4iKnSYlhBQ

7. Ask it to do things … and most likely you're going to need YOLO (danger mode) to get anything done without constant nagging.