# i stopped writing better skills and started building skill architecture
(Description: Abstract visualization featuring layered horizontal bars with a gradient from purple to cyan blue against a dark background with subtle particle effects, suggesting data architecture or system layers)
most people think an ai skill is a well-written instruction file. a really good SKILL.md with examples, scoring criteria, maybe a decision tree. that's the baseline.
we built 11 marketing skills. 32,000 lines. the skills themselves were the easy part. the architecture around them is where the real gains came from.
here are 5 things we added and why each one moved the needle.
## 1. persistent memory
**the problem:** every session starts at zero. you re-explain your brand, your audience, your positioning every single time. the skill has no idea what happened yesterday.
**the fix:** a shared brand directory that every skill reads from and writes to.
- voice-profile.md ← /brand-voice owns
- positioning.md ← /positioning owns
- audience.md ← /audience-research owns
- keyword-plan.md ← /keyword-research owns
- assets.md ← all skills append
- learnings.md ← all skills append
profile files have one owner. only that skill can overwrite (with a diff and confirmation). append files never truncate. they only grow.
**the result:** session 1 builds context that session 20 uses. the skill remembers who you are and what you've done.
## 2. scored context loading
**the problem:** naive approach is to dump all brand memory into every skill. more context should mean better output. it doesn't.
we tested this. give the email skill your keyword plan, competitor analysis, creative kit, and voice profile all at once — it writes muddy emails. tries to honor everything. attention is finite.
**the fix:** a context matrix that scores what each skill receives vs what's withheld. each skill gets what sharpens it. everything else is withheld on purpose.
plus TTLs on context freshness:
- < 7 days → pass as-is
- 7-30 days → flag the age
- 30-90 days → summary only
- 90 days → don't load. it's stale.
**the result:** output went from generic to focused the moment we stopped giving skills everything and started giving them only the right things.
## 3. schema contracts between skills
**the problem:** skills work in isolation. the keyword researcher finds your topics. then you open a new conversation and re-explain everything to the content writer. data doesn't flow between skills.
**the fix:** typed interfaces. skills don't just output text. they output structured artifacts that other skills consume.
6 JSON Schema contracts. /keyword-research outputs a keyword plan. /seo-content reads that plan as input. no re-explaining. no copy-pasting between sessions.
**the result:** skills become nodes in a pipeline. the output of one becomes the input of the next. the data stays structured the whole way.
## 4. learning loops
**the problem:** the skill produces the same quality output on day 90 as day 1. no mechanism for improvement. every session is isolated.
**the fix:** after every major deliverable the system asks a simple question.
how did this perform?
- a) shipped as-is
- b) minor edits
- c) rewrote significantly
answers get logged. date-stamped. skill-tagged.
next time any skill runs it reads those learnings. the email skill stops writing question-based subject lines. the copy skill drops the polish and gets direct.
**the result:** session 1 teaches session 5. mistakes are made once. wins repeat forever. the system gets smarter the more you use it.
## 5. a shared protocol layer
**the problem:** 11 skills each implementing their own memory logic, their own freshness rules, their own feedback collection. inconsistency everywhere.
**the fix:** one protocol document that every skill follows. it defines how to read brand files, how to write them, when context is too stale to use, how to collect feedback, how to degrade when files are missing.
no runtime enforces it. the skills just follow the spec. like HTTP.
**the result:** one document. 11 skills. system-wide coherence.
## what this adds up to
the system works with zero context on day 1. no setup required. just run a skill. but over time:
**no context → useful output**
- voice → sounds like you
- positioning → uses your angle
- audience → targets real pain
- learnings → avoids past mistakes
- full kit → fully personalized
each level adds quality. none is required.
- day 1: it works.
- day 7: it works better.
- day 14: it works like it knows you.
the skill file is the starting point. the architecture around it is what makes it actually perform over time.
I've sold over 700 copies of my v1 skills. this is v2 -- this is a marketing orchestration layer. link is in the bio if you want to experience it.
oh yeah and I built an openclaw version.
---
**Engagement metrics:** 25 replies, 53 reposts, 931 likes, 2,614 bookmarks, 79.7K views