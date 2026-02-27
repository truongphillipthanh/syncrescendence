# obsidian + claude code 101

(Description: A monochromatic engraving-style illustration featuring a minimalist desk workspace. Central focus shows an Apple laptop with the Apple logo visible. Surrounding items include antique navigation instruments: a brass compass, a detailed astrolabe with intricate geometric patterns, globes at various angles, and hanging pendulum-like instruments. Books are stacked nearby. The artistic style uses fine cross-hatching and line work typical of classical scientific illustration, rendered in grayscale with a wooden surface and brick wall background.)

I've spent the last year building an operating system for thinking with ai. Claude Code runs my Obsidian vaults.

It extracts the key concepts, connects them to what you already figured out, and builds a living representation of your thinking.

I find myself only working in the vault now.

The markdown files know everything I've discovered, nicely structured and with automatic situational context injection for in-context learning.

I use a vault index that helps the agent decide what notes to pull in, same pattern as how Claude Code decides which skills to load.

(If you think about it, every note is basically a skill in some sense... highly curated knowledge that gets injected when relevant)

The deeper thing is that a vault encodes how you think, not just what you thought about. The methodology becomes part of the system. It's all just markdown files, you own it completely. This is AI as thinking partner, not as a writing assistant.

## knowledge = code?

I realized: knowledge bases and codebases have a lot in common.

They're both folders of text files with relationships between them, they both have conventions and patterns, and they both benefit from agents that can navigate and operate them.

Vibe coding changed how we write software by letting AI handle implementation while you focus on direction, and the same shift applies to knowledge work.

You don't take notes anymore. You operate a system that takes notes.

## what is a vault?

A vault is a folder of markdown files that link to each other:
```markdown
my-vault/
├── 00_inbox/              # capture zone, zero friction
├── 01_thinking/           # your notes and synthesis
│   └── notes/             # individual thinking notes
├── 02_reference/          # external knowledge
│   ├── tools/             # tool documentation
│   ├── approaches/        # methods and patterns
│   └── sources/           # external knowledge
├── 03_creating/           # content in progress
│   └── drafts/
├── 04_published/          # finished work archive
├── 05_archive/            # inactive content
├── 06_system/             # templates and scripts
├── CLAUDE.md              # teaches the ai your system
└── attachments/           # images and files
```

Files connect using `[[wiki links]]` which build a network of ideas.

When you write `[[quality is the hard part]]` in one note, it creates a clickable link to another note with that title.

The agent can follow these links to jump between related ideas, discovering connections you forgot existed.

## how to write good notes

How you write those links matters.

Most people put references at the bottom like footnotes. Instead, weave links into your sentences.

Don't write "this relates to quality, see: quality-note". Write "because [[quality is the hard part]] we need to focus on curation".

The link becomes part of your thought, and the agent can follow your reasoning by following the links.

Also write notes that stand alone and are composable.

If someone lands on a note from a link, they shouldn't need to read five other notes first to understand it.

Think of notes like lego blocks.

Each one is complete on its own, but they connect to build bigger structures.

When your notes work this way, the network itself becomes valuable.

The thing is, AI doesn't automatically understand your philosophy. You have to teach it.

Watching an AI completely disrespect my philosophies taught me this the hard way.

When you need to teach Claude how you think, you realize how much implicit knowledge you carry around. Suddenly you have to textualize everything.

My CLAUDE.md is around 2000 lines now because I keep refining what works and what doesn't.

## every vault needs its own philosophy

Here's what most guides get wrong. They give you a system and say follow this but every vault serves a different purpose and needs different principles.

Same as codebases really.

You wouldn't use the same folder structure for a CLI tool and a web app.

I run multiple vaults. One is for thinking about AI and knowledge management, which is the example I'll share.

Another is for work, which tracks projects and clients with completely different rules. The philosophy changes based on purpose.

Same underlying pattern, different rules. The pattern is:

- Markdown files with links that any AI can read
- A CLAUDE.md file that teaches the agent your specific system
- Structure that lets the agent orient quickly
- Conventions written as instructions so the AI stays consistent

What goes in those instructions depends entirely on your purpose.

## what this could be

A work vault might emphasize:

- Capture first, structure later
- Project folders with meetings and outputs
- Client context for AI consumption

A research vault might emphasize:

- Source tracking and citations
- Literature notes
- Claim verification

A creative vault might emphasize:

- Idea capture and incubation
- Draft progression
- Reference organization

## the thinking vault example

The vault I'm sharing focuses on developing understanding. The philosophy comes from the CLAUDE.md file:

I can feel the difference when the vault is well maintained versus full of noise. Depth matters more than breadth.

Here is a snippet from the CLAUDE.md to emphasize on this:
```markdown
depth over breadth. quality over speed. tokens are free. this is not about efficiency. this is about excellence. when you pick a task, you are committing to understanding it completely and leaving behind work that future agents can build on.
```

## how claude finds things

When Claude starts a session it needs to understand what exists without reading every file.

That's impossible with thousands of notes. So my system has layers that let the agent orient quickly:
```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "tree -L 3 -a -I '.git|.obsidian' --noreport"
          }
        ]
      }
    ]
  }
}
```

1. Claude sees the folder structure. A hook automatically shows what folders and files exist at session start.

2. An index file that lists every note with a one sentence description. Claude can scan 50 notes in seconds without opening them.

3. Topic pages (MOCs) that link to related notes. These act like tables of contents for each subject. They also contain notes that Claude leaves for itself about what it learned while traversing the graph, leaving breadcrumbs for future sessions.

The AI starts broad, narrows to what's relevant, then follows links to build understanding.

## core principles

These are the rules that work for my thinking vault. Other vault types might need different ones:

1. Can this note be linked from elsewhere and still make sense? If linking to it forces you to explain three other things first, split it up. That's composability.

2. I stopped naming notes like topics and started naming them like claims. Instead of "thoughts on AI slop" you write "quality is the hard part". When you link to it, the title becomes part of your sentence naturally. (This also forces Claude to think differently when building sentences, which I believe is beneficial because it requires understanding)

3. Insight that individual notes matter less than their relationships. A note with many incoming links is more valuable than an isolated note because every link creates a new reading path. The network is the knowledge.

## how the agent operates

Every task starts with orientation. Claude scans the structure, checks the index for relevant notes, reads the topic page before making changes.

It follows links to build understanding and makes no changes without context.

When Claude discovers something useful about navigating a topic, it records that in the topic page.

Future sessions read those notes and learn from past navigation. This is how the vault remembers how to think through itself.

Sometimes two notes interact in interesting ways. Claude creates a new note capturing the insight that emerges from combining them.

Every new capture triggers a search for related notes. Claude adds links with context.

## folder architecture
```markdown
vault/
├── 00_inbox/           # capture zone
├── 01_thinking/        # your notes and topic pages
│   ├── knowledge-work.md  # example topic page
│   └── notes/          # individual notes
├── 02_reference/       # stuff from others
├── 03_creating/        # drafts in progress
├── 04_published/       # finished work
├── 05_archive/         # old stuff
└── 06_system/          # templates and config
```

This structure works for a personal thinking vault. A work vault might have projects and clients.

The point isn't the specific folders but that folder location tells you what something is.

Markdown is the system. Tools like Obsidian are just windows into it. The vault could survive any app disappearing.

Everything is plain text that any editor can read and any AI can process. You own your data completely.

## how to start

1. Create a folder with subfolders that match your purpose. Think about what you actually need to organize.

2. Write a CLAUDE.md that explains your system. Start simple and evolve it as you learn what works.

3. Let Claude operate. Capture something and ask Claude to find connections. Let it navigate and discover relationships and suggest where things belong.

ALWAYS review what it produces and edit for quality.

You're not taking notes anymore but directing a system that takes notes. Your job becomes judgment, which means deciding what matters.

The human role evolves from writer to editor and from creator to curator.

## tldr

- Vibe coding changed how we write software. Vibe note taking changes how we think.
- A vault is just markdown files that link to each other.
- LLMs have no memory, so vaults give them one.
- CLAUDE.md teaches the AI how your system works.
- Every vault needs its own philosophy based on purpose.
- What stays constant: markdown, links, AI operates while you provide judgment.

If you want to see how this evolves, follow along. I'm open sourcing my notes soon.

---

heinrich