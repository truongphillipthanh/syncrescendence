---
url: https://x.com/saranormous/status/2018801883222253737
author: "sarah guo (@saranormous)"
captured_date: 2026-02-03
id: SOURCE-20260203-023
original_filename: "20260203-x_article-software_abundance-@saranormous.md"
status: triaged
platform: x
format: article
creator: saranormous
signal_tier: paradigm
topics:
  - context-management
  - rag
  - rust
teleology: synthesize
notebooklm_category: philosophy-paradigm
aliases:
  - "Software Abundance"
synopsis: "Software Abundance When code is cheap, judgment becomes the work For most of software history, execution was scarce. Writing code was slow, expensive, and constrained by human throughput. The hard part was getting software to exist at all. AI coding agents invert that world. Code can now be produced quickly, cheaply, and in enormous volume."
key_insights:
  - "The best and most respected engineers have historically been closest to the code—reading it deeply, writing it carefully, understanding systems by touching them directly."
  - "At times, I felt stupid—like I was making mistakes I shouldn't be making."
  - "It pointed to parts of the system I understood tacitly but had never articulated."
---
# Software Abundance

(Description: A vibrant digital illustration featuring a futuristic purple and neon-pink cyberpunk cityscape. White sans-serif text reads "SOFTWARE ABUNDANCE" with the subtitle "WHEN CODE IS CHEAP, JUDGMENT BECOMES THE WORK". The scene includes flying vehicles, glowing planets, a sun-like sphere with warm orange glow, and stylized city towers against a star-filled sky with neon accents.)

## When code is cheap, judgment becomes the work

For most of software history, execution was scarce. Writing code was slow, expensive, and constrained by human throughput. The hard part was getting software to exist at all.

AI coding agents invert that world. Code can now be produced quickly, cheaply, and in enormous volume. Execution is no longer the limiting factor—especially for teams operating near the frontier, where outcomes are shaped less by typing speed and more by coordination and judgment.

A useful gut check is the question people now ask half-jokingly: could ten people build DocuSign today? In terms of raw code, the answer is probably yes. The more interesting question is how those ten people would spend their time. It wouldn't be typing. It would be debating edge cases, compliance, trust guarantees, auditability, error semantics, UX, and what it actually means to "sign" something across legal contexts.

That work is about intent.

As software becomes abundant, the ability to make intent clear becomes scarce. This is sometimes described as a win for ideas over execution. That framing misses the point. Most of the intent that matters in real systems is deeply technical: accumulated context, system knowledge, and judgment about tradeoffs. The work hasn't disappeared. It has moved.

This shift is unintuitive because it cuts against how engineering excellence has long been defined. The best and most respected engineers have historically been closest to the code—reading it deeply, writing it carefully, understanding systems by touching them directly. That still matters. But as software becomes abundant, it is no longer where the bottleneck sits, or where leverage consistently accumulates.

## From Intent to Code (and Where It Breaks)

When you tell an experienced engineer "make this faster," they don't hear a literal instruction. They infer context: whether latency or throughput matters, what "fast enough" means here, which tradeoffs are acceptable, and when to push back on the premise itself.

Coding agents don't share that background. You either under-specify and get something plausible but wrong, or over-specify and spend more time writing instructions than writing code.

Software abundance makes this gap visible. Executing the wrong intent is cheap, which means misalignment shows up quickly.

I've run into this myself: spending as much time steering or correcting an agent as I would have spent writing the code directly. At times, I felt stupid—like I was making mistakes I shouldn't be making. That reaction turned out to be informative. It pointed to parts of the system I understood tacitly but had never articulated. The work shifted from typing to clarifying judgment.

## What "Unacceptable Code" Means

As agents improve, the dominant failure mode changes. The problem is rarely broken code.

Unacceptable code runs, passes tests, and looks reasonable, but violates the system's implicit contract. In practice, this often means breaking invisible invariants: assumptions about idempotency, ordering, failure semantics, data integrity, or legacy coupling that were never written down because they were learned through experience.

This code might cross boundaries it shouldn't, optimize the wrong dimension, introduce fragile abstractions, mishandle edge cases, or quietly remove future options. A human engineer rejects it not because it is incorrect, but because they would not want to own it.

The gap between correctness and acceptability is where engineering intent becomes consequential.

Much of this comes down to taste: knowing when something is technically right but still the wrong shape for the system you are building.

## Path Dependence, Made Explicit

We've seen this at fast-growing companies with hundreds of engineers, where early systems were built quickly by teams that were still developing senior judgment. The code worked, scaled enough to ship, and became the foundation for everything that followed.

As AI coding tools became more capable and more pervasive in daily work, they reproduced those early patterns faithfully. Provisional decisions became defaults and were repeated across the codebase. Over time, it became clear which architectural choices had been accidental, which assumptions had gone unexamined, and which decisions were carrying far more weight than anyone had intended.

In some cases this led to rearchitecting high-I/O systems. That work was driven less by failure than by clarity. Once assumptions were visible, teams could decide which ones to formalize, which to revise, and which to discard.

Automation scales whatever structure already exists. When that structure is implicit, the scaling makes it legible.

## Not All Code Is Equally Spec-able

Agents work best where intent is explicit and stable, and struggle where it is implicit and judgment-heavy:

- **Very well-spec'd:** databases, compilers, protocols — Intent is formal and checkable
- **Operationally spec'd:** CI, ETL, CRUD services — Scope control dominates
- **Test-anchored:** business logic, bug fixes — Partial intent capture
- **Taste-heavy:** refactors, APIs, abstractions — Norms and judgment
- **Human-centric:** product logic, UX, naming — Intent evolves
- **Hard to spec:** architecture, strategy — Intent lives outside code

As you move down this spectrum, failures stop looking like bugs and start looking like code you don't trust.

## From Individual Skill to Organizational Capability

We now see companies doing well over $100M in ARR, growing quickly, that plan to stay under roughly 100 engineers—each operating at the limits of parallelized expression of intent.

The strongest users do not write better prompts. They manage intent better. They specify outcomes rather than steps, surface assumptions early, keep diffs small and reviewable, push for simpler solutions, and treat agent output like an untrusted PR.

Among fast-growing startups, senior engineers increasingly rely on tests and live systems rather than close reading of code. One engineer I know once kept pull requests tiny by letting himself eat an M&M for each one. Today, the M&Ms come whenever the system confirms the constraint—after a canary holds, a rollback works, or invariants fire when they should—and he'd need a bigger bowl.

I think of this as **judgment engineering**: the work of translating accumulated experience into explicit constraints, tests, and boundaries that systems and teams can operate against.

Done well, it makes high-quality decisions easier to repeat across people, time, and systems.

## From Software Teams to a Software-Dense World

When the cost of writing and maintaining code drops, organizations stop asking whether something **can** be automated and start deciding whether it **should** be. Software spreads into internal workflows, edge cases, and domain-specific processes that were previously too expensive or fragile to encode.

Systems like CRMs or HRISs look straightforward from the outside, but they represent many thousands of engineer-years spent encoding business logic, exceptions, and constraints that were learned the hard way. Software abundance doesn't erase that work—it changes how quickly and widely similar judgment can now be expressed.

In a software-dense world, value accrues less to individual tools and more to whoever decides which decisions get automated, and under what constraints.

As more things become software, another bottleneck becomes clearer: forming the right intent in the first place. Knowing a domain well enough to extract desired behavior from customers—to understand what they mean, not just what they say—becomes increasingly valuable. Models may help more and more with this work: surfacing inconsistencies, testing interpretations, and making assumptions explicit. How far that goes remains an open question. But everything downstream scales from whatever intent gets formed here.

## Where the Bottleneck Is Now

Software abundance forces intent into the open. As automation increases, judgment starts to behave like a type system: it defines what is allowed, what composes safely, and where failures surface. Weak judgment lets almost anything run. Strong judgment rules out entire classes of mistakes before they spread.

**Software abundance makes judgment the unit of leverage.**