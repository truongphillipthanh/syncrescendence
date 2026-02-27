---
id: SOURCE-undated-x-article-kr0der-codex_has_a_hidden_spec_mode_one_word_unlocks_it
platform: x
format: article
creator: kr0der
title: codex has a hidden spec mode one word unlocks it
status: triaged
original_filename: "codex_has_a_hidden_spec_mode_one_word_unlocks_it-@kr0der.md"
signal_tier: tactical
topics: ""
teleology: implement
notebooklm_category: coding-tools
aliases: ""
synopsis: ""
key_insights: ""
---
Codex planning felt underwhelming.
"Make a plan" gave me 6-7 bullet points. This was fine for small tasks but made it hard to review plans for long tasks.
But then I randomly wrote "make a spec" in one of my prompts, and this changed everything.
Here are my 2 prompts:
- add a column in between "In Progress" and "Done" called "In Review”. Make a plan, don’t code yet.
- add a column in between "In Progress" and "Done" called "In Review". Make a spec, don't code yet.
Now you can see literally the only difference is that I used "spec" instead of "plan" on the right.
The left side is fine for quick stuff, but I can't trust a 6-line plan when Codex is about to run for 15 minutes or more.
The right side gives me actual sections - Goal, Backend, UI/UX, Acceptance, Open questions. The Acceptance part is huge, I can see exactly what Codex is aiming for before it starts.
Try it yourself.
Take your next task, run both versions, and compare.
You'll stop using "plan" after that.