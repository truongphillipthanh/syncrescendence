---
url: https://x.com/tomcrawshaw01/status/2020866308230009189
author: Tom (@tomcrawshaw01)
captured_date: 2026-02-09
---

# Claude Code Told Me Everything I'm Doing Wrong. Then It Built Three Agents To Fix It.

(Description: Terminal window screenshot with orange pixelated retro-style text reading "CLAUDE CODE" on two lines, followed by white monospace text "/insights" below on a dark background with macOS-style window controls at top)

I typed /insights and watched it process 2,555 messages across 318 sessions. It told me things about my workflow I didn't even realize.

## I Typed One Command And Got A Full Performance Review Of My AI Workflow

I wasn't expecting much.

I typed /insights into Claude Code, hit enter, and walked away to grab coffee. When I came back, it had processed 2,555 messages across 318 sessions and generated a full diagnostic report on how I've been using it for the past 30 days.

Not a summary. Not a dashboard. A report that told me what I'm doing well, where I'm bleeding time, and what to do about it.

It even designed three autonomous agents based on the patterns it found in my specific workflow. Not generic templates. Agents built from my actual usage data.

Here's what it looked like.

## Most People Using AI Tools Have Zero Feedback Loop

Think about this for a second.

You open Claude Code (or ChatGPT, or Cursor, or whatever you're using) every single day. You type prompts, get outputs, close the window. Repeat tomorrow.

But if someone asked you right now, "What are your patterns? Where do you lose time? What's your most common task?"... you'd be guessing.

There's no mirror. No replay. No scoreboard.

You're running a system every day without a single metric on how well that system is actually performing. It's like driving a car with the dashboard lights off and hoping you don't run out of gas.

That's what /insights fixes.

## Here's What The Report Actually Spits Out (Section By Section)

The /insights report isn't one giant wall of text. It breaks down into specific sections, and each one reads like a different lens on your workflow.

Here's the structure it generated for me:

**At A Glance** gives you a high-level snapshot. What's working, what's creating friction, quick wins you can install immediately, and ambitious workflows on the horizon.

**What You Work On** breaks your sessions into categories. Mine showed 95 sessions on content creation, 75 on brand voice analysis, 65 on API integrations, 50 on Python automation, and 33 on documentation.

**How You Use Claude Code** is where it gets interesting. It analyzes your communication style, your delegation patterns, how long you typically wait between messages, and whether you micromanage or let the agent run.

Then it goes deeper: Impressive Things You Did, Where Things Go Wrong, Features to Try, New Usage Patterns, and On the Horizon.

Each section pulls from your actual conversation data. Not hypothetical. Not templated. Your data.

## It Told Me I've Been Building A Skills Library Without Realizing It Had A Name

The first section that caught my eye was "Impressive Things You Did."

It flagged three patterns I hadn't consciously connected.

**Pattern one:** I'd installed 26 custom skills over 30 days. Things like an X/Twitter research skill, a copywriting principles framework, and a brand voice analyzer. Each one extending what Claude Code can do for my specific work. The report called it "building a personal skills library" and noted it as a compounding advantage.

**Pattern two:** I'd fed Claude 14 of my top-performing posts and had it extract a comprehensive voice profile document. Tone patterns, sentence structures, engagement hooks, common phrases. The report flagged this as "data-driven brand voice extraction" and pointed out that most people describe their voice in abstract terms, while I grounded mine in actual performance data.

**Pattern three:** 7,776 Bash commands in a single month. 182 commits. The report called it a "Bash-heavy automation pipeline" and noted my tool usage showed Bash at nearly 4x the rate of file edits. Meaning I'm letting Claude run complex operations independently instead of hand-editing files myself.

None of these felt "impressive" in the moment. Each one was just me working. But the report connected the dots and showed me a system I'd been building without a blueprint.

## It Also Told Me Where I'm Bleeding Time (And It Was Right)

This is the section that stings a little. But that's the point.

The report flagged three friction patterns:

**Ambiguous project references.** I'd say something like "add this to the skill" and Claude would sprint confidently toward the wrong project. One session, I asked it to add copywriting principles to a content creation skill. Claude headed straight for my n8n automation project instead. I had to stop it and redirect. The report noted this as my most common source of wasted back-and-forth.

**The "mostly done" pattern.** Out of 90 analyzed sessions, 82 landed at "mostly achieved." Only 8 hit "fully achieved." That's a 91% almost-but-not-quite rate. The report pointed out that I wasn't being explicit enough about what "done" actually looks like for each task. Claude was completing the technical work but missing the polish or secondary steps I expected.

**Exploration overhead.** That 7,776 Bash commands number? It's a double-edged sword. The report noted my Bash-to-Edit ratio was unusually high, suggesting Claude was spending significant time exploring my codebase (running find, ls, and cat commands) before it could confidently make changes. I wasn't giving it enough upfront context about where things live.

Reading this section felt like watching game film after a loss. Uncomfortable, but you can't fix what you can't see.

## The Quick Wins It Suggested Take Minutes To Install

The report didn't just diagnose problems. It generated specific fixes I could copy and paste directly into Claude Code.

**Fix one: CLAUDE.md additions.** Three lines of context I could add to my project file so Claude always checks the right directories first. No more "wrong project" confusion. One of them was literally: "This project focuses on content creation, copywriting skills, and social media workflows. Key directories: .claude/skills/ for Claude skills, content-creation/ for templates and guides."

That's it. Three sentences. And it eliminates the most common friction point in my entire workflow.

**Fix two: Custom slash commands.** The report suggested turning my most repeated workflows (voice analysis, skill installation, documentation creation) into reusable /commands. Instead of explaining what I want every session, I type one command and the whole process runs with the right context baked in.

**Fix three: MCP server connections.** It noticed I was burning time on manual API setup for social media platforms and suggested connecting an MCP server for Twitter to eliminate the key juggling entirely.

Each fix addresses a specific pattern the report identified. Not generic productivity advice. Targeted solutions built from 30 days of my actual usage data.

## Then It Designed Three Autonomous Agents Based On My Workflow Patterns

This is where the report shifted from looking backward to looking forward.

Based on everything /insights analyzed about my patterns, it designed three autonomous agents tailored to my specific work. Not theoretical concepts. Agents with step-by-step implementation instructions I could paste directly into Claude Code.

### Agent One: An Autonomous Content Voice Research Pipeline

Right now, my brand voice extraction process is manual. I feed Claude a batch of posts, it analyzes them, and it spits out a voice profile document. It works well, but I have to initiate it every time.

The agent /insights designed would run this autonomously on a weekly schedule.

It reads my current brand voice profile, pulls my latest 20 posts from social platforms, identifies which ones outperformed average engagement, extracts the linguistic patterns unique to those top performers, and writes a "Voice Evolution Report" comparing new findings against my existing profile.

If significant patterns emerge, it proposes specific updates with before-and-after examples. All of this happens without me initiating a single prompt.

The voice profile that took me dozens of sessions to build manually would now update itself in the background while I'm focused on actually creating content.

### Agent Two: Self-Improving Skills Through Test Iteration

I've installed 26 skills in 30 days. Each one required me to test it, evaluate the output, tweak the prompts, and test again. That loop is where most of my "mostly achieved" sessions live.

The second agent automates the entire improvement cycle.

It reads the current skill, generates five diverse test scenarios, runs the skill against each test, evaluates outputs against my copywriting principles, identifies specific weaknesses in anything scoring below an 8 out of 10, edits the skill's prompts to address those weaknesses, and re-runs the tests.

It doesn't stop until all five scenarios pass. Then it commits the improved skill with a changelog explaining exactly what it fixed and why.

The skills I build would get better while I sleep. Every morning I'd wake up to a tighter, more effective toolkit than the one I left the night before.

### Agent Three: Parallel Documentation Workers That Merge Their Own Output

56 of my sessions over 30 days were documentation creation. Guides, reference materials, principles documents, knowledge base entries. It's important work but it's a time sink.

The third agent spawns parallel Claude instances that each document a different skill or API endpoint simultaneously.

A coordinator agent assigns the work, each worker reads the skill code, fetches any external API docs it references, and writes complete documentation including purpose, inputs, outputs, examples, and edge cases. After documenting each skill, it updates a master index. Then it reviews all new docs for voice consistency against my brand voice profile and harmonizes any outliers.

What used to take 56 individual sessions could run as a single coordinated operation in the background.

## What Changes When You Actually Have A Mirror On Your AI Workflow

Before I ran /insights, I thought I was using Claude Code efficiently. I was building skills. I was automating. I was shipping.

But I had no idea that 91% of my sessions were landing at "mostly done" instead of "fully done." I didn't realize my most common friction point was three missing sentences in a config file. I couldn't see that my exploration overhead was inflating every single session.

The difference between using an AI tool and operating an AI system is feedback.

In 2026, the people who are going to pull ahead aren't the ones using the most AI tools. They're the ones who know how their AI tools are actually performing, where the friction lives, and what to do about it.

One command. That's all it takes to find out.

Type /insights.

---

**Promotional note:** If you want more breakdowns like this, the tools, workflows, and implementation methods are sent out weekly in The AI Operator's Playbook. Subscribe at https://learnn8nautomation.com/newsletter for 15 production-ready n8n workflows and 6 implementation playbooks from 8 years of building automations.

**Post metadata:** Published 6:24 AM · Feb 9, 2026 | 31.6K Views | 13 Replies | 24 Reposts | 298 Likes | 609 Bookmarks