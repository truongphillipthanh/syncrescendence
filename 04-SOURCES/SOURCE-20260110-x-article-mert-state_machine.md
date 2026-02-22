---
id: SOURCE-20260110-x-article-mert-state_machine
date_published: "2026-01-10"
platform: x
format: article
creator: mert
title: state machine
status: triaged
url: https://x.com/mert/status/2009986072953126935
original_filename: "state_machine-@mert.md"
signal_tier: tactical
topics:
  - "claude-code"
  - "vibe-coding"
  - "best-practices"
teleology: extract
notebooklm_category: claude-code
aliases:
  - "Mert - State Machine Diagrams Tip"
synopsis: "Quick tip: ask Claude to generate state machine diagrams of existing components before modifying them. This forces the model to map all paths rather than being lazy, and helps the developer verify correctness of the model understanding."
key_insights:
  - "Asking Claude to make state machine diagrams of existing components forces it to map out all paths rather than defaulting to lazy partial analysis"
  - "State machine diagrams serve dual purpose: verifying the model correctly understands the component and revealing paths the developer may have forgotten"
  - "This is a quick verification technique that prevents Claude from making changes based on incomplete understanding of existing code"
---
a quick opus 4.5 vibecoding tip

ask claude to make state machine diagrams of existing components

this causes it to map out all paths (which, it will default to being lazy otherwise) but also helps you verify if it's doing things correctly at a systems level