---
url: https://x.com/dkundel/status/2018455598267027894
author: dominik kundel (@dkundel)
captured_date: 2026-02-14
---

# Codex App Tips and Tricks Thread

Been helping bringing the Codex app to life and at this point I've fully moved from using an IDE and the Codex Extension to working 99.9% of the time exclusively in the Codex app.

Here are some tips of what I found useful to get the most out of the app 👇

---

## 💪 Have Codex automatically become better

Add a daily task to read your past sessions in `~/.codex/sessions` and update your [AGENTS.md](http://AGENTS.md) files or update/create new skills for common tasks.

(Description: UI mockup showing "Create automation" dialog with fields for Name: "Update AGENTS.md", Projects section with "developers-website" and "Codex app" tags, Prompt field stating "Update AGENTS.md with newly discovered workflows and commands", and Constraints listing best practices for automation)

---

## 📌 Use pinned threads

Especially if you multitask across multiple projects this is a great way to quickly keep an eye on everything that's in progress.

(Description: UI mockup showing a threads panel with tasks listed: "Check bundled Codex version (4h)", "App docs (5d)", "Design modern smashburger site (2d)", "Polish app for launch prep (2d)", "Localize iOS app (6d)", followed by a Threads section showing three pinned folders: "skills", "Codex app (openai)", and "developers-website")

---

## 😴 Prevent sleeping

If your Mac auto locks but you want to keep Codex churning through tasks, you can prevent your computer from going to sleep in the settings.

(Description: UI mockup showing "Prevent sleep while running" toggle switch set to enabled, with text "Keep your computer awake while Codex is running a thread")

---

## 🔔 Notifications

I don't allow a lot of apps to send notifications but the Codex app can send you notifications for approval requests and turn completions while the app is in the background. It's great to quickly respond without switching the app into the foreground.

(Description: UI mockup showing a "Command approval" notification for curl request to developers.openai with dropdown menu options: "Approve", "Approve for session", and "Decline")

---

## 🟢 Actions in local environments

You can configure actions inside your environment settings for common tasks like starting a dev server or triggering a build. They automatically start in the integrated terminal.

That way you can start your project with the push of a button in

(Description: UI mockup showing "developers-website actions" dropdown menu with options: "▶ Run" (checkmarked), "⚙ Build", "+ Add action", "⚙ Change environment" with right arrow)

---

## 🧠 Skills + MCP

Skills will uplevel your Codex capabilities heavily, especially if you share them with your team. Most of the skills that I use (outside the ones we shipped) are checked into project repos.

We have skills to start up new versions of the app, polish the developer

(Description: Code snippet in dark theme showing YAML configuration:
```
dependencies:
  tools:
    - type: "mcp"
      value: "linear"
      description: "Linear MCP server"
      transport: "streamable_http"
      url: "https://mcp.linear.app/mcp"
```
)

---

## 🧬 Automations for boring work

My favorite use case beyond using Codex to improve skills is to have Codex keep an eye on PRs or issues.

Have Codex run every hour to check your PRs, address all the comments / fix your CI runs and $.yeet the changes back to the PR.

To quote

(Description: UI mockup of "Create automation" dialog showing Name field: "Always green PRs", Projects section showing "developers-website" tag, Prompt section with automation instructions)

The review panel is a huge reason why I rarely use an IDE. You leave line by line feedback for the output that Codex generated. Makes Codex edits faster and keeps you aligned.

(Description: Code review panel showing HTML code with green highlighting for lines 20-21 containing div elements with classes "logo">Fogline Smashburger and "nav-actions">. A dialog shows "Turn this into a separate component" with Cancel and Comment buttons. Additional code lines 22-24 visible with nav-links and menu href attributes)

---

## ⛏️ Non-coding work

There are so many useful things you can have Codex do beyond just basic coding work. I use the $.atlas skill to regularly clean up my duplicate tabs or end the day with a list of documents I still have to review or have Codex clean up my screenshot folder 😁

(Description: UI mockup showing a prompt input field with "Time to lock in. Close all my social media tabs ⊙ Atlas Control (macOS)" text and "GPT-5.2 -Codex High" model selector)

---

## 🪟 Windows support coming soon!

We will be shipping Windows soon! Wanted to get the sandbox situation on Windows right.