# Apple MCP Server Release for Xcode 26.3 - Thread Discussion

## Post 1 - Feb 3, 2026 (10:40 AM)

Apple has released an MCP server as part of Xcode 26.3!

It extends the IDE and requires the IDE to be running and your project open. It can:

- Browse + search the Xcode project structure (ls/glob/grep)
- Read/write/edit/move/delete files and create groups/dirs
- Build the project and pull structured errors + full build logs
- List Xcode Issue Navigator issues + per-file diagnostics
- Discover tests, run all or targeted tests, with pass/fail summaries
- Render SwiftUI previews to a snapshot and run small Swift snippets

Looks really nice and has some really useful tools, but somewhat limited. It extends the Xcode IDE rather than using the Xcode Command Line tools, so it uses the schema, build config, and project you have open in the IDE. You need to have the IDE open and running in the background.

I don't think this replaces XcodeBuildMCP, which doesn't require the IDE to be running and has more capabilities like UI-automation and debugging support.

It might be possible to utilise Xcode MCP via JSON-RPC with XcodeBuildMCP to add the IDE specific-capabilities if running, will look into this.

Good to see Apple making progress in that area!

XcodeBuildMCP is safe for now!

---

## Post 2 - Feb 3, 2026

Disappointing to see Apple pass on improving the toolchain for agentic coding and instead ship a closed-source MCP that depends on a closed Xcode build pipeline and IDE. The command line tools are still crippled compared to the IDE, and xcodebuild, lacking proper incremental build,s is a sad state of affairs. The OSS community is stuck building on top of these limitations. Apple had a real opportunity to modernise the foundation in a way that would benefit both the ecosystem and its own stack.

---

## Post 3 - Feb 4, 2026

I don't think it really changes anything tbh. It's an MCP for an IDE. XcodeBuildMCP is an MCP for headless iOS and macOS development. What I'll probably look at doing is proxying some of the Xcode MCP tools (when available) to XcodeBuildMCP.

---

## Post 4 - Feb 4, 2026

So the MCP essentially exposes the IDE's features to external coding agents. Xcode IDE has its own build diagnostics and build pipeline and of course project file format. Until now this has been unavailable to external applications. But this MCP is designed for users who primarily work in Xcode and want to occasionally drop down to a 3rd party coding harness like Claude Code.

---

## Post 5 - Feb 4, 2026

Yep that's a nice capability for sure.