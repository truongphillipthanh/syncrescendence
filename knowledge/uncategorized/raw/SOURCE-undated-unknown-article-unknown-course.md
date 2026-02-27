---
id: SOURCE-undated-unknown-article-unknown-course
platform: unknown
format: article
creator: unknown
title: course
status: triaged
original_filename: 1-GettingStarted--3-course.md
signal_tier: tactical
topics: ""
teleology: implement
notebooklm_category: claude-code
aliases: ""
synopsis: ""
key_insights: ""
---
# Getting Started

## Claude Code Basics

### Intro to Claude Code

* Claude Code is the most powerful coding agent in the world. It runs in a terminal (the command-line interface developers use).
* It runs in your terminal and can read, write, and edit files in your codebase.
* Claude Code can read, edit, and delete files. It has full control over your project.
* It can build entire apps from scratch or improve existing ones.
* Beyond coding, it works as a general-purpose agent. It can research, plan, and solve problems.
* **Tools:** Claude Code has built-in tools for searching files, running commands, browsing the web, and more.
* **Skills:** Special abilities that teach Claude Code how to do specific tasks (like setting up a database or designing a UI).
* Available through a Pro Max subscription at $200/month or via API usage.

---

## Using Claude Code Inside Vibecode

When you use Vibecode, Claude Code runs on a **virtual computer in the cloud**. This is a remote computer hosted on Vibecode's servers that you access through your browser. You never need to install anything on your own computer.

* **No setup needed:** Everything is ready to go. Just open Vibecode and start building.
* **Safe to experiment:** Your code runs in a "sandbox" (an isolated space) so nothing can affect your personal computer.
* **Servers run automatically:** The "frontend" (what users see) and "backend" (the behind-the-scenes logic) both start on their own.
* **Easy publishing:** When your app is ready, you can share it with others without dealing with complicated hosting setup.
* **Ready-to-use AI tools:** Connect to popular AI services like ChatGPT or voice generators with just a few clicks in the API tab.
* **Simple settings management:** "Environment variables" are secret settings your app needs (like passwords or API keys). Vibecode has an easy ENV tab to manage these.
* **Live preview:** Watch your app update in real-time as changes are made. No need to refresh manually.
* **See what's happening:** The Logs tab shows messages from your app, helpful for understanding what's going on or finding problems.
* **No coding experience needed:** You interact through a simple chat interface. No scary black-screen terminals required.
* **Access anywhere:** Your projects are saved in the cloud, so you can pick up where you left off from any device.

---

## Think Before You Prompt

The biggest mistake people make is typing immediately. Take a moment to think about what you actually want before asking Claude to build it.

* **Picture the end result:** Before asking for a feature, imagine what it should look like and how it should work.
* **Break it down:** Instead of "build me a social media app," think about each piece: login, posts, profiles, etc.
* **One thing at a time:** Ask for one feature, see it work, then move to the next. This gets better results than asking for everything at once.
* **The more detail, the better:** "Add a blue button" is okay. "Add a blue button in the top right that saves the form and shows a success message" is much better.

### Writing Good Prompts

Your output depends on your input. If Claude builds something you don't like, the fix is usually a better prompt.

* **Be specific:** Don't give Claude creative freedom on things you care about. It will make choices you might not like.
* **Say what you DON'T want:** "Make it simple, don't add extra features I didn't ask for" prevents over-engineering.
* **Explain why:** "I need this to be fast because users will be on slow phones" helps Claude make smarter decisions.
* **Use examples:** "Make it look like Instagram's profile page" or "Similar to how Uber shows the map" gives Claude a clear target.
* **Bad output = bad input:** If you're not happy with the result, don't blame Claude. Rethink how you asked.

> **Example: Building a contact form**
> Add a contact form to the home page with fields for name, email, and message. Put a blue submit button at the bottom. When someone submits, show a green success message that says 'Thanks! We'll be in touch.' Keep it simple, no extra fields.

---

## Keeping Conversations Fresh

Claude has a "context window," which is the amount of conversation it can remember at once. Like a whiteboard, if it gets too full, things get messy.

* **Start fresh for new features:** When you finish one thing and want to build something new, start a new conversation.
* **Quality drops over time:** Long conversations can confuse Claude. If responses start getting worse, it might be time to clear and start over.
* **One conversation per task:** Working on login? Keep that conversation just about login. Want to add payments? New conversation.
* **When in doubt, start fresh:** If Claude seems stuck or confused, a new conversation often fixes it.

### When Things Go Wrong

Sometimes Claude gets stuck or builds the wrong thing. Here's how to get back on track.

* **Start a new conversation:** This clears out any confusion from the old chat.
* **Simplify your request:** Break a big task into smaller, simpler pieces.
* **Check the Logs tab:** Error messages there can tell you (or Claude) what went wrong. If something isn't working and you don't see any logs, tell Claude to add logs so you can see what's happening.
* **Show an example:** If you can describe or show what you want more clearly, Claude can match it.
* **Don't repeat yourself:** If you've explained the same thing three times and it's still not working, try a completely different approach.

### Getting Better Over Time

The more you use Claude Code, the better you'll get at working with it. Here's how to improve faster.

* **Learn from mistakes:** When something doesn't work, think about how you could have asked differently.
* **Save good prompts:** When a prompt works really well, remember it (or write it down) for next time.
* **Don't give up:** If something doesn't work the first time, try again with a clearer prompt. Claude improves every week.
* **Think like a teacher:** Imagine you're explaining the task to a smart assistant who's never seen your project. What would they need to know?
* **Use Opus:** It's the best model available for complex tasks and produces the highest quality output.

Would you like me to analyze these instructions to identify the most critical "decision leverage" points for your first project in Vibecode?