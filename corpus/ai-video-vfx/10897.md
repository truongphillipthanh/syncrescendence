# Forget Google Docs. My OpenClaw bot and I share work through GitHub repos
(Description: A illustration showing a workflow diagram with Google Drive and GitHub logos connected by arrows through an OpenClaw mascot (orange crab-like character) and a raccoon-like assistant character. The diagram shows the flow from Drive to GitHub with repository labels displayed.)
When I started setting [this up](https://x.com/renatonitta/status/2022053849670762858), I first tried using Google Drive, since the bot already uses its own Gmail account. But it didn't feel right, so I set up a GitHub organization to share repos with my [@openclaw](https://x.com/@openclaw) bot instead.
Let me show you a quick demo first, and I'll elaborate more in a minute.
(Description: Embedded video showing a demo of the GitHub interface with the shared_workspace repository open, displaying a draft document titled "The Daily Journal (Nikki)" in a Google Doc-like interface embedded in the GitHub workflow.)
## Create an organization
You can use an existing one, but I created a new organization to hold all the repos for this partnership.
Since the bot has its own GitHub account, it behaves like any collaborator: it can create new repos, manage existing ones, send commits, push changes, and everything.
I asked the bot to create the following repos:
(Description: A GitHub interface screenshot showing a list of 4 repositories: shared_workspace (with 0 watchers, 0 stars), tanuki-nikki (with 0 watchers, 0 stars), tanuki-scripts marked with Python language (with 0 watchers, 0 stars), and tanuki-ops (with 0 watchers, 0 stars).)
- **shared_workspace** — our "drive"
- **tanuki-nikki** — its daily journal
- **tanuki-scripts** — automation scripts we rely on
- **tanuki-ops** — operational rules, behavior guidelines, procedures
## Your agent's work needs to survive tomorrow
I needed a place where the agent's work would persist. Where can I find it tomorrow? Next week. Next month. Where every change is tracked, and every file lives in a predictable place.
I also didn't want to leave critical files on the local disk. If something happens to the machine where the bot is installed, do I lose everything?
No. The important things are pushed to GitHub.
I also asked it to create a recovery kit, with a daily routine to keep it updated. If anything goes south, I can rebuild the bot without depending on the local disk.
(Description: A GitHub file browser showing a recovery folder structure with files including README.md, bootstrap_checklist.md, personas.md, repos.md, routines.md, and rules.md, alongside a popup titled "Tanuki-kun recovery kit" explaining it is a disaster recovery kit for rehydrating Tanuki-kun on a fresh OpenClaw install, with the goal that if the machine dies, Nikki-san can rebuild the assistant without losing personality, rules, and routines.)
## The shared workspace
We have other repos, but I'll focus on the "drive-like" one.
It will grow like any normal drive. Right now, it already includes:
(Description: A GitHub interface showing the shared_workspace repository structure with folders including outbound, projects, writing, archived, drafts, and personal. A file preview panel shows a document "Peter (OpenClaw's creator) joins OpenAI — quick note" with content discussing OpenClaw's approach and mentioning real tools, workflows, durable artifacts, and operational safety.)
- a **writing** folder (with the draft from the demo)
- **drafts**, **published**, and **archived** states
- a **project_ideas** folder
- an **x_metrics** folder (where it saves summaries of my X activity)
- a **personal** folder where I told the bot to store whatever it wants
## Why Git is better than you'd expect for this
Everything is version-controlled. Every change the agent makes is a commit, with a timestamp and a diff I can review.
Everything is searchable. I can grep the entire workspace.
Commits create accountability. Every file has a history: when it was created, when it changed, and exactly what changed.
If something looks wrong, I can roll it back in seconds.
## The takeaway
If you're building with OpenClaw, you need a persistence layer that isn't a chat window.
GitHub gives you:
- **Durability** — files survive restarts.
- **Auditability** — every change is a commit.
- **Structure** — folders enforce rules.
It's not flashy.
It's just Git.
And it's the foundation that makes everything else work.