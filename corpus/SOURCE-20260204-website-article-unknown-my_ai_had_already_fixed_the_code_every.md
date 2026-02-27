# My AI Had Already Fixed the Code Before I Saw It

Compounding engineering turns every pull request, bug fix, and code review into permanent lessons your development tools apply automatically

By **Kieran Klaassen**  
January 27, 2026

---

While we're on our Think Week offsite this week, we're resurfacing [Cora](https://cora.computer/) general manager [Kieran Klaassen](https://every.to/@kieran_1355)'s work on the theme of compound engineering. In this piece, Kieran lays out his definition of the term and the shift it represents: What if your AI tools learned—and autonomously applied those lessons to future work? That's what happened when his Claude Code agent incorporated three months of prior feedback without being asked. The future of development is self-improving systems, not just faster coding.— [Kate Lee](https://every.to/on-every/kate-lee-joins-every-as-editor-in-chief)

Was this newsletter forwarded to you? [Sign up](https://every.to/account) to get it in your inbox.

---

Before I opened my laptop, the code had reviewed itself.

I launched GitHub expecting to dive into my usual routine—flag poorly named [variables](https://every.to/c/compounding-engineering), trim excessive tests, and suggest simpler ways to handle errors. Instead, I found a few strong comments from [Claude Code](https://www.anthropic.com/claude-code), the AI that writes and edits in my terminal:

> "Changed variable naming to match pattern from PR [pull request] #234, removed excessive test coverage per feedback on PR #219, added error handling similar to approved approach in PR #241."

In other words, Claude had learned from three prior months of code reviews and applied those lessons without being asked. It had picked up my tastes thoroughly, the way a sharp new teammate would—and with receipts.

It [felt like cheating](https://every.to/working-overtime/ai-phobia-is-really-just-fear-that-easier-equals-cheating), but it wasn't—it was compounding. Every time we fix something, the system learns. Every time we review something, the system learns. Every time we fail in an avoidable way, the system learns. That's how we build [Cora](https://cora.computer/), Every's AI-enabled email assistant, now: Create systems that create systems, then get out of the way.

I call this **compounding engineering**: building self-improving development systems where each iteration makes the next one faster, safer, and better.

Typical AI engineering is about short-term gains. You prompt, it codes, you ship. Then you start over. Compounding engineering is about building systems with memory, where every pull request teaches the system, every bug becomes a permanent lesson, and every code review updates the defaults. AI engineering makes you faster today. Compounding engineering makes you faster tomorrow, and each day after.

Three months of compounding engineering on Cora have completely changed the way I think about code. I can't write a function anymore without thinking about whether I'm teaching the system or just solving today's problem. Every bug fix feels half-done if it doesn't prevent its entire category going forward, and code reviews without extractable lessons seem like wasted time.

When you're done reading this, you'll have the same affliction.

## The 10-minute investment that pays dividends forever

Compounding engineering asks for an upfront investment: You have to teach your tools before they can teach themselves.

Here's an example of how this works in practice: I'm building a "frustration detector" for Cora; the goal is for our AI assistant to notice when users get annoyed with the app's behavior and automatically file improvement reports. A traditional approach would be to write the detector, test it manually, tweak, and repeat. This takes significant expertise and time, a lot of which is spent context-switching.

So I start with a sample conversation where I express frustration—like repeatedly asking the same question with increasingly terse language. Then I hand it off to Claude with a simple prompt: "This conversation shows frustration. Write a test that checks if our tool catches it."

Claude writes the test. The test fails—the natural first step in [test-driven development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development). Next, I tell Claude to write the code to pass the test and then [iterate on the frustration detection prompt](https://every.to/also-true-for-humans/7-22).

Not only that—it can keep iterating. Claude adjusts the prompt and runs the test again. It reads the logs, sees why it missed a frustration signal, and adjusts again. After a few rounds, the test passes.

But AI outputs aren't deterministic—a prompt that works once might fail the next time. So I have Claude run the test 10 times. When it only identifies frustration in four out of 10 passes, we have a problem. I ask Claude to analyze why it fails and improve the prompt using [chain of thought](https://every.to/also-true-for-humans/7-22) (the step-by-step thinking Claude showed when deciding whether someone was frustrated) from each failed run and discovers a pattern:

On the next iteration, it's able to identify a frustrated user nine times out of 10. Good enough to ship as a version one—and we've created something extractable and reusable.

We codify this entire workflow—from identifying frustration patterns to iterating prompts to validating consistency across multiple runs. Now this workflow is part of our system's permanent operating procedures. Every new feature Claude builds for Cora gets stress-tested this way. When new feedback comes in about frustration detection, we feed it back into the system to improve it further.

---

*The content continues but reaches a paywall for non-subscribers. The article includes sections on the philosophy of compounding engineering and its implications for the future of development.*