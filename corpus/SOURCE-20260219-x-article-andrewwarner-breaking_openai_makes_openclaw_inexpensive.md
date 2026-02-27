# Breaking: OpenAI makes OpenClaw inexpensive
Yesterday, Claude said they'd CANCEL OpenClaw users who connect their Claude subscriptions. But OpenAI said they'd allow it! This is the step-by-step guide to using your ChatGPT subscription and eliminating API fees.
(If you just want to see how to use OpenAI, [skip to the walkthrough here](https://www.youtube.com/watch?v=7DNlQgl2Kk0&t=1s).)
## Does Claude hate OpenClaw?
Yesterday, Claude made their restrictions clear.
This is a link to their [full Legal & Compliance doc](https://code.claude.com/docs/en/legal-and-compliance#authentication-and-credential-use), but to me, the important part is this:
(Description: Screenshot of Claude Code Docs showing Legal and compliance resources section. Key text visible: "OAuth authentication (used with Free, Pro, and Max plans) is intended exclusively for Claude Code and Claude.ai. Using OAuth tokens obtained through Claude Free, Pro, or Max accounts in any other product, tool, or service — including the Agent SDK — is not permitted and constitutes a violation of the Consumer Terms of Service. Developers building products or services that interact with Claude's capabilities, including those using the Agent SDK, should use API key authentication through Claude Console or a supported cloud provider. Anthropic does not permit third-party developers to offer Claude.ai login or to route requests through Free, Pro, or Max plan credentials on behalf of their users. Anthropic reserves the right to take measures to enforce these restrictions and may do so without prior notice.")
They do NOT want you to use your $0/month, $20/month, $100/month or $200/month accounts in tools like @openclaw.
Claude seems hostile to OpenClaw.
[@steipete](https://x.com/@steipete), OpenClaw's creator, has already said that Anthropic/Claude's engagement with him is only through legal "love letters":
(Description: Screenshot of X/Twitter post from Peter Steinberger (@steipete) showing verified badges. Text: "yah they only sent love letters from legal")
And in his [@lexfridman](https://x.com/@lexfridman) interview, Peter said that after forcing him to change the name of his project, they didn't even let him redirect his old domain to make it easy for users to find his project.
## Why this sucks
The way that Claude wants us to connect to OpenClaw is **expensive**.
I'm a light user and I end up burning through $20/day, easily.
My friend [@codymclain](https://x.com/@codymclain) told me he burns $100/day.
The cost is crazy high for a project that -- let's be honest -- is still so new that most of what we're doing is using it to figure out WHAT it can do. There's no ROI for most people -- yet.
## OpenAI steps in
Yesterday, when I announced that using Claude subscriptions on OpenClaw could get your account banned, I suggested that Sam Altman and OpenAI could step in and let us use our accounts.
(Description: Screenshot of X/Twitter post from Andrew Warner (@AndrewWarner) with verified badge showing alert emoji. Text: "Breaking: Claude OAuth officially not allowed in OpenClaw. This would be a GREAT time for @sama to step in and let us use @OpenAI subscriptions with @openclaw.")
Peter replied to me immediately to tell me that OpenAI was already ahead of this:
(Description: Screenshot of X/Twitter conversation between Peter Steinberger (@steipete) showing verified badges, and Andrew Warner (@AndrewWarner). Peter's reply: "that already works, OAI publicly said that" with 95 replies, 108 reposts, 2.2K likes, 188K views. Andrew's response: "I love that! Thanks Peter." with 1 reply, 0 reposts, 61 likes, 20K views.)
What nice way to treat users. Not only did they allow it, but they communicated it clearly.
## How to do it
I recorded a clear step-by-step walk-through with [@calebhodges](https://x.com/@calebhodges) who offers concierge OpenClaw setups for clients. He's been doing this over and over because of Claude's ban.
### 📺 Watch the full video here
[Easy Video Walkthrough on YouTube](https://www.youtube.com/watch?v=7DNlQgl2Kk0&t=1s)
But for experienced users, here's the simple 2-step process.
### Step 1: Select OpenAI
```plaintext
openclaw onboard --auth-choice openai-codex
```
This will skip the **onboarding wizard**, pre-selecting **OpenAI Codex (ChatGPT OAuth)** as the authentication method. Here's what it does specifically:
**onboard**
This kicks off the setup wizard that configures your OpenClaw gateway, workspace, channels, and skills.
**--auth-choice openai-codex**
This skips the interactive prompt asking you to pick a model provider and automatically selects the **OpenAI Codex** option, which authenticates via **ChatGPT OAuth** (i.e., your existing ChatGPT/Codex subscription) rather than a raw API key.
During this flow, OpenClaw will open a browser OAuth URL for you to sign in with your ChatGPT account. Once authenticated, it sets the default model to something like openai-codex/gpt-5.x-codex and stores the OAuth credentials in your auth profile.
The main reason to choose this over an API key is that it uses your **subscription's token budget** (e.g., ChatGPT Plus/Pro) instead of pay-per-token API billing, which can be more cost-effective if OpenClaw is chatty.
### Step 2: Select 5.3 Codex
```plaintext
openclaw models set openai-codex/gpt-5.3-codex
openclaw models status --plain
```
**openclaw models set openai-codex/gpt-5.3-codex**
This sets openai-codex/gpt-5.3-codex as the **primary text model** for your agent.
Specifically, it writes agents.defaults.model.primary in your ~/.openclaw/openclaw.json config file. The model ref format is always provider/model — here openai-codex is the provider (your ChatGPT OAuth auth profile) and gpt-5.3-codex is the specific model.
Note that this writes to config but **does not automatically restart the gateway** — you'd need to run openclaw gateway restart for it to take effect on a running instance.
**openclaw models status --plain**
This shows the current model configuration and auth status. Without --, models status gives you a full overview: the resolved primary model, any configured fallbacks, the image model, and an auth summary of all providers (including OAuth expiry warnings if a token is within 24 hours of expiring). The --plain flag strips all of that context down to **just the resolved primary model name**, printed as a single line — useful for scripting or quick sanity checks that the right model is active.
So the two commands together form a common pattern: set a new default model, then verify it stuck.
## What else can you do?
### A. Cancel or downgrade your Claude account.
I'm switching from the $200/month plan to the $20/month.
### B. Spread the word about how to use OpenAI!
**1. Copy the commands above and Tweet them, as [@ryancarson](https://x.com/@ryancarson) did:**
(Description: Screenshot of X/Twitter post from Ryan Carson (@ryancarson) showing: "Here's how to use your ChatGPT account with @openclaw! openclaw onboard --auth-choice openai-codex openclaw models set openai-codex/gpt-5.3-codex openclaw models status --plain h/t @AndrewWarner @calebhodges" with 19 replies, 16 reposts, 199 likes, 14K views)
**2. Share or like this post.**
**3. Send your friends the video walkthrough that [@calebhodges](https://x.com/@calebhodges) created:** [Easy Video Walkthrough on YouTube](https://www.youtube.com/watch?v=7DNlQgl2Kk0&t=1s)
If Claude doesn't want us, we have alternatives.