---
id: SOURCE-20260130-x-article-trq212-how_we_use_claude_code_in_slack
platform: x
format: article
creator: trq212
title: how we use claude code in slack
status: triaged
original_filename: "20260130-x_article-how_we_use_claude_code_in_slack-@trq212.md"
url: https://x.com/trq212/status/2017350486756888917
author: "Thariq (@trq212)"
captured_date: 2026-02-04
signal_tier: paradigm
topics:
  - claude-code
  - developer-tools
  - best-practices
  - case-study
teleology: extract
notebooklm_category: claude-code
aliases:
  - "Thariq - Claude Code in Slack at Anthropic"
synopsis: "Anthropic engineer Thariq reveals how the Claude Code team uses Claude Code inside Slack for answering codebase questions, acting on feedback, and trying out prototypes. The ultimate source of truth is the codebase itself, and Claude Code can answer questions like 'when was this feature released?' via git access."
key_insights:
  - "At Anthropic, Claude Code in Slack serves as an always-available codebase oracle — answering questions from go-to-market, support, marketing, and product teams directly from source code."
  - "The biggest difference between internal Anthropic usage and public usage is the degree of Slack-integrated collaborative workflows."
  - "Claude Code's git access enables meta-questions about the codebase itself: release timing, code ownership, and feature history."
---
# How we use Claude Code in Slack

(Description: Screenshot of a Slack conversation thread showing Claude Code APP responding with "Perfect! I have successfully updated the VS Code IDE." The message includes buttons for "View Claude Code session" and "Create PR", with metadata "Worked in payment-service - Requested by @Nate")

One of the biggest differences between how we use Claude Code at Anthropic and how the broader world uses it is how much we use it in Slack. In particular, we use it for answering questions, acting on feedback, and trying out prototypes.

## Answering Questions

When people in go-to market, customer support, marketing, product, etc. have a question about Claude Code, they ask Claude directly in Slack. While we keep our docs up to date, they don't cover every possible question. The ultimate source of truth is in the codebase.

Because it has access to git, it can answer questions like "When was this feature released?" or "who is responsible for this code?", which can help you find the right owners.

**Protip:** Go even further and add skills with access to things like your event store or analytics dashboard to answer questions about feature usage or error logs.

## Acting on Feedback

We have very active Claude Code feedback channels. When someone sends in feedback, we will very often tag @Claude to try and solve it with some guiding context. It's not always possible, but a PR can be a way of exploring or understanding how something can be done.

Every Claude in Slack instance is visible on Claude Code on the web, so my chat history in claude.ai/code is almost like my jira board, where feedback PRs are listed just waiting to be acted on.

## Building Prototypes

I don't really send memos or make mockups anymore, I just make CC prototypes. If I have an idea I might kick off the prototype via Claude in Slack and wait to see how it comes out before figuring out if it's worth investing in.

## Tips for Using Claude in Slack Well

- Investing in the configuration (e.g. Claude.MDs, hooks, verification, etc) is even more valuable, because it lets non technical people use Claude in Slack better.
- You still need to check it out, test and read the code. We're not just merging from Slack into main.
- Set a 'default repo' for a channel to make it easier for Claude in Slack to tell where it can make changes.

## Getting Started

Read the docs and get started with Claude in Slack here: https://code.claude.com/docs/en/slack

If you're already using it, give us feedback!

---

**Post metadata:** Published 1:33 PM · Jan 30, 2026 | 290.1K Views | 38 Replies | 61 Reposts | 968 Likes | 1.7K Bookmarks