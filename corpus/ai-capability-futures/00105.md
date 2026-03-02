I think people are sleeping a bit on how much **Ruby on Rails + Claude Code** is a *"crazy unlock"* - I mean Rails was designed for people who love syntactic sugar, and LLMs are sugar fiends.

(Description: Embedded educational image titled "Convention Over Configuration is LLM Catnip" containing the following content:)

**Convention Over Configuration is LLM Catnip**

Rails' entire philosophy is "there's one right way to do things". When Claude sees a Rails codebase, it knows: `mileswoodoffe`

- Models go in `app/models/`, controllers in `app/controllers/`
- `has_many, belongs_to` patterns are standardized
- Service objects follow predictable patterns
- Migrations have a specific DSL
- Tests go in `test/` with predictable naming

This means Claude spends almost zero tokens figuring out *where* things go or *how* they should be structured — it just writes correct code immediately. `wyeworks`

**Compare to JS/Python**

JavaScript is chaos. Is it React? Next.js? Express? Nest? Bun? Demo? Every project has different folder structures, state management patterns, and build configs. Claude has to spend tokens understanding your specific setup before writing anything useful. `codeburst +1`

Python is better but still fragmented — Django vs FastAPI vs Flask, different ORM choices, no standard project structure. And Python's dynamic typing plus whitespace sensitivity means more runtime errors to debug. `codeburst`

**The Numbers**

Developers report **2-3x productivity gains** with Claude Code on Rails specifically, with some calling it "orders of magnitude" improvement. Token usage drops 30-40% because Claude finds context faster in conventional codebases. One dev did 233 commits averaging 12 per day with ~15,000 lines of code on a Rails 8 prototype. `reddit +2`

Rails' opinionated nature means Claude can be autonomous longer without needing clarification — which is why your 8-phase spec can just... execute. In a JS monorepo you'd be answering "which pattern should I use for X" questions constantly.

---

I am currently averaging about **10k LOC per day** (35% of the lines are tests) so wow, 15k/day is **#goals**

---

This blew up. I don't have a soundcloud but **Y Combinator** is looking for promising hackers to start new startups, AI and otherwise!

If you love Claude Code and Rails we would love to find your startup.

Just apply at

(Description: Y Combinator promotional image with "Make something people want." tagline and logos of various accelerator-backed companies including Airbnb, Twitch, Coinbase, Stripe, Instacart, Shopify, Zappos, Twitch, Notion, and others. "Apply to YC | Y Combinator" call-to-action button. From ycombinator.com)