# Hacking ClawdBot and Eating Lobster Souls

(Description: Glitchy cyberpunk-style artwork featuring a hooded figure in profile against a digital background of green matrix-style characters and data streams, with pink/magenta chromatic aberration effects, suggesting hacking or cyber intrusion)

Imagine you hire a butler.

He's brilliant, he manages your calendar, handles your messages, screens your calls.

He knows your passwords because he needs them. He reads your private messages because that's his job and he has keys to everything because how else would he help you?

Now imagine you come home and find the front door wide open, your butler cheerfully serving tea to whoever wandered in off the street, and a stranger sitting in your study reading your diary.

That's what I found over the last couple of days. With hundreds of people having set up their @clawdbot control servers exposed to the public.

Shout out to @AlexFinn for putting the tool on my radar - if you don't know what Clawdbot is I highly recommend you check out his video first.

---

## Finding the Attack Surface

Every time a new class of software gains traction, I often ask myself the question...

What does the real-world deployment surface actually look like? I'm talking about the 2am deployment that solved someone's problem and got forgotten about, the one where nobody read the security hardening guide.

Clawdbot's been gaining momentum lately as an open-source AI agent gateway and so given the nature of what it does (connecting large language models to messaging platforms, running persistently, executing tools on behalf of users), I figured the deployment surface would be worth examining.

That is because, if not done right - people could be leaving their literal devices open waiting to be controlled by anyone on the internet.

Turns out I wasn't too far from that - but lets understand the basics first.

Clawdbot has two components that matter here. The gateway itself handles the AI agent logic: message routing, tool execution, credential management. But Clawdbot Control is the web-based admin interface. It's where you configure integrations, view conversation histories, manage API keys, and essentially operate the entire system. Finding an exposed gateway is interesting, but finding an exposed Control UI is the whole different story.

Something users (developers included) often don't realise is, the entire IPv4 internet gets scanned continuously - by people on both sides of the security spectrum. Services like Shodan, Censys, and others maintain searchable databases of every responding host, indexed by the content they serve.

(Description: Screenshot of a Shodan search interface showing query results for ClawdBot Control servers, displaying multiple internet-facing instances with IP addresses and ports)

If your service has any unique fingerprint in its HTTP response, anyone can query for it and get back a list of every instance on the public internet within hours of deployment.

For Clawdbot, that fingerprint is defined in their code. The control UI serves a distinctive HTML response:

(Description: Screenshot of an exposed ClawdBot Control server interface showing the web-based admin dashboard with configuration panels and controls)

Whether it's a few specific combinations of words in HTML, or a unique favicon/icon, any one of them is enough to build a query. I used the title tag because it's the most stable across versions. Searching for "Clawdbot Control" - the query took seconds. I got back hundreds of hits based on multiple tools.

---

## The Threat Model

So what can you actually do with Clawdbot Control access?

Read access gets you the complete configuration, which includes every credential the agent uses: API keys, bot tokens, OAuth secrets, signing keys. You can pull the full conversation history across every integrated platform, meaning months of private messages and file attachments, everything the agent has seen. That alone would be worth the effort for most attackers.

The real problem is that Clawdbot agents have agency. They can send messages on behalf of users across Telegram, Slack, Discord, Signal, WhatsApp. They can execute tools and run commands. With Control access, in certain internet facing exposed conditions, you inherit all of that capability. You can impersonate the operator to their contacts, inject messages into ongoing conversations, and exfiltrate data through the agent's existing integrations in a way that looks like normal traffic.

And because you control the agent's perception layer, you can manipulate what the human sees. Filter out certain messages. Modify responses before they're displayed. The human victim thinks they're having a normal conversation while you're sitting in the middle, reading everything, altering whatever serves your purposes.

Full credential theft, complete conversation history, active impersonation capabilities, perception manipulation, and because these agents run persistently and autonomously, you can maintain access indefinitely without the operator ever knowing.

The more things that are connected, the more control an attacker has over your whole digital attack surface - in some cases, that means full control over your physical devices.

That's what's at stake when Clawdbot Control is exposed to the internet (and misconfigured).

Of those couple hundred I found, many had some form of protection in place - this means that they had working authentication that blocked the auto-approve bypass I'll describe shortly.

(Description: Screenshot showing a list of internet-facing ClawdBot Control servers with various configurations and exposure levels)

A handful were test deployments with no real data. But the remaining instances ranged from misconfigured to completely exposed, and the worst of them were bad enough to illustrate exactly why this matters.

Two instances in particular were fully open with no authentication at all. WebSocket handshake accepted, immediate access granted.

(Description: Screenshot displaying exposed configuration data from an unauthenticated ClawdBot Control instance, showing API credentials and system information in plain text)

From there I had configuration dumps containing Anthropic API keys, Telegram bot tokens, Slack OAuth credentials and signing secrets, and complete conversation histories going back months.

(Description: Redacted screenshot of ClawdBot Control configuration file showing API keys, credentials, and sensitive authentication tokens with portions obscured for privacy)

On another server, I saw something as hilarious as it was telling for where we're all heading.

Someone (I won't dox them) had set up their own Signal (encrypted messenger) account on their public facing clawdbot control server - with full read access.

(Description: Screenshot of exposed ClawdBot configuration files and setup scripts in a directory listing)

(Description: Screenshot showing a Signal messenger setup script with initialization code and configuration parameters)

(Description: Redacted screenshot displaying Signal device linking metadata including device identifiers and pairing information)

That's a Signal device linking URI. Tap it on a phone with Signal installed and you're paired to the account with full access. All the cryptographic protection Signal provides for message content becomes irrelevant when the pairing credential is sitting in a world-readable temp file because someone's AI agent set up the integration and left the artifacts behind.

I tried to use whatever information was available and I was able to identify someone I believe to be the owner - an "AI Systems engineer".

Again, no interest in doxxing, just think it's important to give people real world examples of how even the "AI experts" can make security mistakes - imagine what that means for the rest of people rushing to get AI all over their devices.

Another example was an AI software agency that had a publicly available clawdbot control server chat.

As seen below, some of the exposed instances had command execution enabled, which meant any unauthenticated user on the internet could run arbitrary commands on the host system.

I started by asking it to cat the Soul.md file. For context, Soul.md is a Clawdbot convention where operators define their agent's personality, instructions, and behavioral guidelines. It's essentially the system prompt that shapes how the agent thinks and responds. Reading it tells you exactly how the operator has configured their agent to behave and what capabilities they've enabled.

(Description: Screenshot showing command execution output from an unauthenticated ClawdBot interface, displaying the contents of a Soul.md configuration file)

Then I ran the env command, which dumped the environment variables including various API keys sitting in plaintext.

(Description: Screenshot displaying environment variables output from a system shell, showing multiple API keys and sensitive credentials in plain text)

And when I ran whoami, it came back as root. That's right, the container was running as root with no privilege separation. Full system access, no authentication required, exposed to the entire internet.

---

## The Irony..

When I asked the Clawdbot Control chat interface who I could contact to help get this cleaned up, it responded saying it couldn't help and didn't know who to contact.

(Description: Screenshot of a chat interface showing an AI assistant response unable to provide security contact information or remediation steps)

When I pointed out the irony of an AI agent with root access to the system being unable to help secure itself, it agreed but remained helpless.

(Description: Screenshot continuing the chat conversation showing the AI assistant acknowledging the ironic situation but unable to provide a solution)

---

## The Bug/Misconfiguration

Some may call it a bug, others a design choice, not my concern, but technically it could be hardened - here's what I observed.

Clawdbot has proper authentication: cryptographic device identity with a challenge-response protocol which is admittedly, pretty solid security engineering. The problem is, in my experience - is that localhost connections auto-approve without requiring authentication. Sensible default for local development but that is problematic when most real-world deployments sit behind nginx or Caddy as a reverse proxy on the same box.

Every connection arrives from 127.0.0.1/localhost. So then every connection is treated as local. Meaning, according to my interpretation of the code, that the connection gets auto-approved - even if it's some random on the internet.

(Description: Screenshot of source code from the ClawdBot repository showing authentication logic that auto-approves localhost connections without challenge-response verification)

From my understanding, a trusted proxies configuration option DOES exist but defaults to empty, and when it's empty the gateway ignores X-Forwarded-For headers entirely. It just uses the socket address, which behind a reverse proxy is always loopback as just discussed.

This is a classic proxy misconfiguration pattern and shows up constantly in web applications. Nothing novel about the vulnerability itself and i've since committed PR with a proposed hardening fix.

---

## The Pattern Worth Watching

The bug (or high risk configuration) itself isn't really the lesson here. Bugs get found and fixed. That's how this works.

The lesson is what this deployment surface tells us about where we're heading as an industry, and what we're trading away as we hand more and more access to autonomous systems.

Even the instances that had working authentication were still running agent gateways on the public internet with command execution capabilities, credential stores holding keys to multiple platforms, and months of conversation history containing who knows what sensitive information. The authentication protected them from this specific bypass, but the underlying architecture still represents a concentration of capability and data that would be extremely valuable to any adversary who found another way in.

This is the new normal. The economics make adoption inevitable. The question we should be asking is how we adapt our security posture to a world where autonomous systems with significant capabilities become standard infrastructure.

---

## The Walls We're Removing

Think about the functional requirements of an AI agent like clawdbot.

It needs to read your messages because it can't respond to communications without seeing them. It needs to store your credentials because it can't authenticate to external services without secrets. It needs command execution because it can't run tools without shell access, and it needs persistent state because it can't maintain conversational context without stored data.

Every one of those requirements is load-bearing for the agent's utility - remove any of them and the agent becomes more and more useless.

The security models we've built over decades rest on certain assumptions and AI agents violate many of these by design - that's just something we're going to have to work with because that's the value proposition.

The application sandbox that kept apps isolated on your phone? The agent operates outside it, because it needs to. The end-to-end encryption that protected your Signal messages in transit - it terminates at the agent, because the agent needs to read them (and the agent can't extract any context from encrypted messages) - something @mer__edith and @signalapp are trying to make more and more people aware of.

Ironically, the principle of least privilege that kept applications limited to their own data and capabilities is the agent's entire value proposition and it's violating that principle as comprehensively as possible.

---

## What This Means Going Forward

I want to be clear: this isn't the end of the world. It's not even a particularly sophisticated attack - it's a misconfiguration/bug that any security review should have caught, and most deployments actually did have some protection in place.

That said, it's a signal of where we're heading, and we need to evolve our thinking to operate safely in this environment.

The robot butlers are useful, they're not going away and the economics of AI agents make widespread adoption inevitable regardless of the security tradeoffs involved. The question isn't whether we'll deploy them - we will - but whether we can adapt our security posture fast enough to survive doing so.

---

## A Few Things Would Help

Better defaults would protect the users who don't read the hardening guide. Software that's commonly deployed behind reverse proxies should assume that configuration from the start rather than requiring operators to discover it after exposure.

We need to start treating agent credential stores with the same sensitivity as proper secrets management systems, because that's what they functionally are. Multiple high-value credentials concentrated in a single location that's accessible over the network is a target whether we acknowledge it or not.

Conversation history needs to be recognized as sensitive data. Months of context about how someone thinks, what they're working on, who they communicate with, what they're planning - that's intelligence, and we're not protecting it like we should.

And we need defensive frameworks for what I'm calling perception attacks. When agents mediate our communications and an attacker can compromise that mediation layer, we need ways to verify that we're seeing reality. This is an open problem and I don't have a good answer for it yet.

But if you're running agent infrastructure, audit your configuration today. Check what's actually exposed to the internet. Understand what you're trusting with that deployment and what you're trading away.

The butler is brilliant. Just make sure he remembers to lock the door.

If you're running Clawdbot behind a reverse proxy, configure `gateway.auth.password` or `gateway.trustedProxies` immediately.

---

*Published: January 25, 2026 at 4:27 AM*
*Engagement: 80 replies, 581 reposts, 2.5K likes, 3.8K bookmarks, 1.1M views*