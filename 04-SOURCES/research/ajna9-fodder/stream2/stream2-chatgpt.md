# Claude Code: Validated Architecture, Configuration, and Interaction

## Architecture Map

-   **Agentic Loop (LLM + Tools):** Claude Code runs as a local CLI that
    orchestrates an *agentic loop* powered by remote Claude models and
    local tools. User prompts (with project code context) go through the
    Claude LLM (cloud) for reasoning, and the CLI executes the model's
    recommended actions (file edits, shell commands, searches, etc.)
    locally. "The agentic loop is powered by two components: models that
    reason and tools that act. Claude Code serves as the agentic harness
    around Claude: it provides the tools, context management, and
    execution environment that turn a language model into a capable
    coding
    agent."[\[1\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=autonomously%20but%20stays%20responsive%20to,into%20a%20capable%20coding%20agent).
    In practice, Claude Code uses *Claude* language models to process
    code/tasks
    (remote)[\[2\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20uses%20Claude%20models,the%20model%20doing%20the%20reasoning)
    while running tools (file I/O, shell, git, code search, etc.) on the
    user's
    machine[\[3\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Tools).
-   **Models:** Multiple Claude models are supported. By default
    **Claude Sonnet** is used for most coding tasks and **Claude Opus**
    for complex reasoning, but the CLI allows switching (e.g.
    `claude --model <name>` or
    `/model`)[\[2\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20uses%20Claude%20models,the%20model%20doing%20the%20reasoning).
    Models run in the cloud (Anthropic servers); nothing about the LLM
    runs locally.
-   **Tools and Extensions:** Built-in *tools* (file read/write, shell,
    search, web fetch, code intelligence, etc.) execute
    locally[\[3\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Tools).
    Extensions such as **Skills** (custom prompts), **Hooks**
    (event-triggered scripts), **MCP servers** (external API
    connectors), and **subagents** (forked Claude Code sessions) layer
    on top of the core
    loop[\[4\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Each%20tool%20use%20gives%20Claude,right%20extension%20for%20your%20needs).
    Skills and hooks are defined by user files and run locally (the
    model reads their instructions); MCP servers contact external
    services; subagents spawn additional local processes with isolated
    context[\[5\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Manage%20context%20with%20skills%20and,subagents).
-   **Context & Memory:** Claude Code maintains a *session context*
    (conversation + relevant files) that is stored locally. Project
    files, `CLAUDE.md`, and open buffers are all part of this
    context[\[6\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=This%20guide%20focuses%20on%20the,Claude%20Code%20gains%20access%20to)[\[7\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%E2%80%99s%20context%20window%20holds%20your,to%20see%20what%E2%80%99s%20using%20space).
    Older tool outputs and conversation are auto-summarized
    ("compacted") by Claude Code when the context window
    fills[\[8\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20manages%20context%20automatically,server%20costs).
    The system also uses *checkpoints*: before any file edit, Claude
    Code snapshots the file so changes can be undone
    locally[\[9\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Undo%20changes%20with%20checkpoints).
    Context and session data reside on the local machine (not in the
    cloud); Claude Code explicitly has "no persistent memory between
    sessions" -- each `claude` invocation starts fresh (though sessions
    can be
    saved/resumed)[\[10\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20saves%20your%20conversation,md).
-   **Data Flows (Local vs Remote):** In sum, **user↔CLI↔Claude**: the
    CLI reads project code/CLAUDE.md (local), sends it to Claude
    (remote) along with tool definitions, then runs the returned tool
    commands
    locally[\[2\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20uses%20Claude%20models,the%20model%20doing%20the%20reasoning)[\[3\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Tools).
    Results (command outputs, file diffs) feed back into the local
    context, completing the loop. Subagents run the same loop in
    parallel but with their own fresh context, returning summaries to
    the main
    session[\[5\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Manage%20context%20with%20skills%20and,subagents).

**Baseline claims evaluation (Architecture):** The baseline's high-level
notions (agentic loop, tools vs model, local vs cloud) are **Verified**
by official
docs[\[1\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=autonomously%20but%20stays%20responsive%20to,into%20a%20capable%20coding%20agent)[\[2\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20uses%20Claude%20models,the%20model%20doing%20the%20reasoning).
Specific baseline assertions (e.g. "single-threaded master loop," or
details about which model is used in which mode) are not explicitly
documented and thus **Refined/Unverified**. For example, the claim that
*Plan Mode always uses Opus by default* is **Unverified** (official docs
simply say models can be switched
manually)[\[2\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20uses%20Claude%20models,the%20model%20doing%20the%20reasoning).
Similarly, any baselined "Enterprise/Unix philosophy architecture" is
not spelled out in official docs (though the CLI's behavior aligns with
Unix principles); such stylistic claims are **Unverified**.

## Configuration Surface Map

-   `settings.json` **(hierarchical JSON):** The primary config file is
    `settings.json` in JSON format. It is supported at multiple scopes:
    **User** (`~/.claude/settings.json`), **Project**
    (`.claude/settings.json`), and **Local**
    (`.claude/settings.local.json`, which is
    `.gitignore`-d)[\[11\]](https://code.claude.com/docs/en/settings#:~:text=,that%20need%20centralized%20control%2C%20Claude).
    An organization can enforce a **managed-settings.json** (and
    **managed-mcp.json**) in system directories
    (`/Library/Application Support/ClaudeCode/` on macOS,
    `/etc/claude-code/` on Linux, or `C:\Program Files\ClaudeCode\` on
    Windows)[\[12\]](https://code.claude.com/docs/en/settings#:~:text=ignore%20,code%2F%60%20%2A%20Windows%3A%20%60C%3A%5CProgram%20Files%5CClaudeCode).
    Settings from these files are merged with the following precedence
    (highest to lowest): *Managed policies* \> *Command-line flags* \>
    *Local* \> *Project* \>
    *User*[\[13\]](https://code.claude.com/docs/en/settings#:~:text=How%20scopes%20interact).
    (For example, a setting in `settings.local.json` overrides one in
    `.claude/settings.json`, and CLI arguments override both.)
-   **Managed Settings:** In managed mode, admins can deploy
    `managed-settings.json` and `managed-mcp.json` to system
    locations[\[12\]](https://code.claude.com/docs/en/settings#:~:text=ignore%20,code%2F%60%20%2A%20Windows%3A%20%60C%3A%5CProgram%20Files%5CClaudeCode).
    These provide org-wide defaults or allowlists (e.g. forcing certain
    permission rules or MCP servers). Managed config merges in at the
    top of the
    hierarchy[\[13\]](https://code.claude.com/docs/en/settings#:~:text=How%20scopes%20interact).
-   **Other JSON Configs:**
-   `~/.claude.json`**:** This user-level JSON file (in the home CLAUDE
    directory) holds session state and preferences (OAuth credentials,
    UI prefs, notification settings, etc.), allowed tools, and
    *user-scoped* MCP server
    configurations[\[14\]](https://code.claude.com/docs/en/settings#:~:text=,mcp.json).
    Users generally do not edit this manually.
-   `.mcp.json`**:** A project-level file defining MCP (Model Context
    Protocol) servers. It lives in the project root (`.mcp.json`) and
    declares additional external services/tools for this repo. These
    server entries must be approved (via settings or CLI). User-level
    MCP config is in
    `~/.claude.json`[\[14\]](https://code.claude.com/docs/en/settings#:~:text=,mcp.json).
-   **Subagent configs:** Under `~/.claude/agents/` and
    `.claude/agents/` (project), users can define custom *subagents*.
    Each subagent is a folder with a `AGENT.md` workflow. (Official docs
    list these directories as the places for agent
    definitions.)[\[15\]](https://code.claude.com/docs/en/settings#:~:text=Feature%20User%20location%20Project%20location,project)
-   **Memory and Rules Files:**
-   `CLAUDE.md`**:** A Markdown "constitution" file loaded every session
    for durable project-wide rules and
    context[\[7\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%E2%80%99s%20context%20window%20holds%20your,to%20see%20what%E2%80%99s%20using%20space)[\[6\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=This%20guide%20focuses%20on%20the,Claude%20Code%20gains%20access%20to).
    It is searched in multiple places: first, a *managed* system
    CLAUDE.md (if provided, e.g. `/Library/.../CLAUDE.md` on
    macOS)[\[16\]](https://code.claude.com/docs/en/memory#:~:text=Memory%20Type%20Location%20Purpose%20Use,Team%20members%20via%20source%20control);
    then the user home CLAUDE.md (`~/.claude/CLAUDE.md`); then
    `./CLAUDE.md` or `./.claude/CLAUDE.md` in the project; and finally a
    local override file `./CLAUDE.local.md` in the project
    root[\[17\]](https://code.claude.com/docs/en/memory#:~:text=Memory%20Type%20Location%20Purpose%20Use,specific%20project%20instructions).
    These load in that priority order.
-   `.claude/rules/*.md`**:** Project-specific rule files under
    `.claude/rules/` are also loaded into memory as part of CLAUDE.md
    (e.g. `.claude/rules/code-style.md`,
    etc.)[\[18\]](https://code.claude.com/docs/en/memory#:~:text=instructions%20managed%20by%20IT%2FDevOps%20Company,Team%20members%20via%20source%20control).
-   `CLAUDE.local.md`**:** A local, gitignored override (e.g.
    credentials, personal notes) in the project
    root[\[19\]](https://code.claude.com/docs/en/memory#:~:text=%E2%80%A2%20Windows%3A%20%60C%3A%5CProgram%20Files%5CClaudeCode%5CCLAUDE.md%20%60Organization,specific%20project%20instructions).
-   **Skills and Commands:**
-   **Legacy slash commands:** Older custom commands can be added as
    Markdown under `.claude/commands/*.md`. These work exactly like
    skills (each file with
    frontmatter)[\[20\]](https://code.claude.com/docs/en/skills#:~:text=For%20built,Claude%20invokes%20them%2C%20and%20the).
-   **Skills:** Stored as directories named after the slash command,
    containing a `SKILL.md` file with YAML frontmatter. Skills can
    reside in three places: per-user
    (`~/.claude/skills/<skill>/SKILL.md` for all projects), per-project
    (`.claude/skills/<skill>/SKILL.md`), or bundled in a plugin
    (`<plugin>/skills/<skill>/SKILL.md`)[\[21\]](https://code.claude.com/docs/en/skills#:~:text=match%20at%20L187%20Personal%60~%2F.claude%2Fskills%2F%3Cskill,name%3E%2FSKILL.md%20%60Where%20plugin%20is%20enabled).
    Each `SKILL.md` uses YAML frontmatter (between `---`) to configure
    triggers and permissions, followed by markdown
    instructions[\[22\]](https://code.claude.com/docs/en/skills#:~:text=Every%20skill%20needs%20a%20,helps%20Claude%20decide%20when%20to).
-   **Formats and Schemas:** All settings files are in JSON. (Official
    docs note a JSON schema exists for `settings.json`---for example on
    schemastore---but it is not yet explicitly documented in user
    guides[\[23\]](https://github.com/anthropics/claude-code/issues/11795#:~:text=Problem%20Statement).)
    Skills use a YAML+Markdown format in
    `SKILL.md`[\[22\]](https://code.claude.com/docs/en/skills#:~:text=Every%20skill%20needs%20a%20,helps%20Claude%20decide%20when%20to).
    Configuration precedence and merging rules follow the hierarchy
    above[\[13\]](https://code.claude.com/docs/en/settings#:~:text=How%20scopes%20interact).
-   **Environment Variables:** Claude Code recognizes many environment
    variables (e.g. `ANTHROPIC_API_KEY` or `CLAUDE_CODE_*`) to override
    settings. Users can also define `env` in `settings.json` to set
    session environment
    variables[\[24\]](https://code.claude.com/docs/en/settings#:~:text=Variable%20Purpose%20,See%20%2032).
    For example, `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` makes
    the CLI load `CLAUDE.md` from any extra directories passed with
    `--add-dir`[\[25\]](https://code.claude.com/docs/en/settings#:~:text=,client%20certificate%20file%20for%20mTLS).
    (A full list of supported env vars is in official
    docs[\[24\]](https://code.claude.com/docs/en/settings#:~:text=Variable%20Purpose%20,See%20%2032)[\[25\]](https://code.claude.com/docs/en/settings#:~:text=,client%20certificate%20file%20for%20mTLS).)
-   **CLI Flags:** The `claude` command accepts many flags that override
    or initiate behaviors. Notable ones include `--model <name>` (to
    pick the model at
    startup)[\[2\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20uses%20Claude%20models,the%20model%20doing%20the%20reasoning),
    `--continue` or `--resume` (to continue a saved
    session)[\[26\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=When%20you%20resume%20a%20session,session%60%20flag),
    `--fork-session` (to fork the conversation), and `--clear` (to start
    fresh). CLI flags have higher precedence than file-based
    settings[\[13\]](https://code.claude.com/docs/en/settings#:~:text=How%20scopes%20interact).

**Baseline claims evaluation (Configuration):** Many baseline-file
claims map to real settings. For example, the hierarchy of settings
files in the config suite (user vs project vs local) **Matches
Official** \[58†L178-L187\]\[8†L140-L149\]. However, some baseline
specifics require refinement: e.g., the example `$schema` URL in
settings is *not officially documented* (though a schema does
exist)[\[23\]](https://github.com/anthropics/claude-code/issues/11795#:~:text=Problem%20Statement),
so citing it without doc support is **Unverified/Refined**. The
suggested "profiles/" folder is **Unverified** (official docs have no
built-in "profiles" feature). Using a YAML frontmatter-based `SKILL.md`
is *exactly* how skills
work[\[22\]](https://code.claude.com/docs/en/skills#:~:text=Every%20skill%20needs%20a%20,helps%20Claude%20decide%20when%20to)
(Verified), and legacy `.claude/commands/*.md` are still
supported[\[20\]](https://code.claude.com/docs/en/skills#:~:text=For%20built,Claude%20invokes%20them%2C%20and%20the).
The baseline's `defaultMode: "plan"` in JSON is a valid setting, but
note that the official default is
`"acceptEdits"`[\[27\]](https://code.claude.com/docs/en/settings#:~:text=files%20from%20Claude%20Code%20access,to%20prevent%20%60bypassPermissions),
so treating "plan" as default is a **Refinement**. Overall, official
docs largely confirm the config file locations and merging rules
(Verified), but custom-suggested structures (profiles, etc.) are not in
official docs (Unverified).

## Interaction Paradigm Map

-   **Permission/Approval Modes:** Claude Code supports three main modes
    (toggled with **Shift+Tab** or the `--bypass-permissions` flag):
    *Default* (ask before any file edit or external command),
    *Auto-Accept Edits* (file edits auto-approved, but commands still
    require approval), and *Plan Mode* (no edits until a plan is
    approved)[\[28\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Press%20,permission%20modes).
    Official docs describe: "Plan mode: Claude uses read-only tools
    only, creating a plan you can approve before
    execution"[\[28\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Press%20,permission%20modes).
    Permissions can also be managed via `permissions` in settings (with
    ordered allow/deny lists) and even disabled for automation (the
    `--dangerously-skip-permissions` bypass). Managed policies can
    disable bypassing for
    security[\[27\]](https://code.claude.com/docs/en/settings#:~:text=files%20from%20Claude%20Code%20access,to%20prevent%20%60bypassPermissions).
-   **Plan Mode Semantics:** When entered (e.g. by pressing Shift+Tab to
    cycle into it, or using the `/plan` command), Claude enters a
    *planning* phase. It uses only non-destructive tools and produces a
    strategy or "plan.md" for user
    review[\[28\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Press%20,permission%20modes).
    Only after the user approves the plan does Claude execute actions.
    (This matches the documented "read-only plan"
    behavior[\[28\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Press%20,permission%20modes).)
    Plan Mode is entirely opt-in; there is no hidden "magical" mode --
    it simply changes the permission mode.
-   **Context Compaction & Reset:** As conversation history grows,
    Claude Code *auto-compacts* to stay within token
    limits[\[8\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20manages%20context%20automatically,server%20costs).
    It will clear older tool outputs first, then summarize the dialogue
    if
    needed[\[8\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20manages%20context%20automatically,server%20costs).
    Users can manually run `/compact [directives]` to compress context
    with focus (officially
    documented)[\[8\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20manages%20context%20automatically,server%20costs).
    Conversely, `/clear` wipes the current context completely (starting
    a fresh
    session)[\[29\]](https://code.claude.com/docs/en/interactive-mode#built-in-commands#:~:text=,usage%20as%20a%20colored%20grid).
    Persistent, important instructions should be put in `CLAUDE.md`
    (which is reloaded after compaction/reset) rather than relying on
    conversation
    memory[\[8\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20manages%20context%20automatically,server%20costs).
    The docs explicitly note: *"Claude Code manages context
    automatically... key code snippets are preserved; detailed
    instructions from early in the conversation may be lost. Put
    persistent rules in
    CLAUDE.md."*[\[8\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20manages%20context%20automatically,server%20costs).
-   **Session Management:** Each `claude` invocation creates a session
    ID tied to the working directory. Sessions are saved locally, so you
    can resume or fork them. Using `claude --continue` or
    `claude --resume` reloads a past session (restoring its
    history)[\[26\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=When%20you%20resume%20a%20session,session%60%20flag).
    (Forking with `--fork-session` or `--fork` starts a parallel branch
    of the same
    conversation[\[26\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=When%20you%20resume%20a%20session,session%60%20flag).)
    By default there is no long-term memory: *"Claude Code has no
    persistent memory between sessions. Each new session starts
    fresh"*[\[10\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20saves%20your%20conversation,md).
    To carry info across sessions, users rely on CLAUDE.md, task lists,
    or external notes.
-   **Slash Commands & Skills:** Claude Code uses a "slash" (`/`) prefix
    to invoke built-in commands (e.g. `/help`, `/context`, `/agent`,
    etc.) or custom **Skills**. Skills are triggered by slash commands
    (the skill's `name` field becomes the
    `/command`)[\[22\]](https://code.claude.com/docs/en/skills#:~:text=Every%20skill%20needs%20a%20,helps%20Claude%20decide%20when%20to).
    In fact, legacy custom slash commands (`.claude/commands/*.md`) have
    been unified with the Skill
    system[\[20\]](https://code.claude.com/docs/en/skills#:~:text=For%20built,Claude%20invokes%20them%2C%20and%20the).
    Each skill's frontmatter can restrict whether the user must type the
    slash or Claude can auto-invoke it when relevant. Slash commands
    thus serve two roles: interactive prompts for built-in utilities and
    entry points for user-defined skills.
-   **Hooks:** Hooks are scripts triggered by events. Official docs
    define: *"Claude Code hooks are user-defined shell commands that
    execute at various points in Claude Code's lifecycle. Hooks provide
    deterministic control... ensuring certain actions always happen
    rather than relying on the
    LLM."*[\[30\]](https://code.claude.com/docs/en/hooks-guide#:~:text=Claude%20Code%20hooks%20are%20user,to%20choose%20to%20run%20them).
    Hooks can run **before/after** each tool use (e.g. logging), or at
    session start/end. They are configured via the `hooks` section in
    settings (with keys for each
    event)[\[30\]](https://code.claude.com/docs/en/hooks-guide#:~:text=Claude%20Code%20hooks%20are%20user,to%20choose%20to%20run%20them).
    Their role is to allow customized automation (e.g. enforcing code
    format on save).
-   **Other Interaction Notes:** Claude Code is fundamentally
    conversational and interactive. Users can interrupt the model, steer
    it, or provide additional instructions at any
    time[\[31\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=refactor%20might%20involve%20extensive%20verification,into%20a%20capable%20coding%20agent).
    Features like `/agents` or `/doctor` commands assist configuration.
    All built-in slash commands and features (like `/compact`, `/clear`,
    `/context`, `/status`, etc.) are documented in the interactive mode
    reference[\[29\]](https://code.claude.com/docs/en/interactive-mode#built-in-commands#:~:text=,usage%20as%20a%20colored%20grid)[\[32\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Ask%20Claude%20Code%20for%20help).

**Baseline claims evaluation (Interaction):** Many baseline descriptions
match the docs. For example, the permission modes **match exactly**:
default/auto-accept/plan are
documented[\[28\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Press%20,permission%20modes)
(Verified). The idea that users should review the plan before execution
is the documented intention of Plan
Mode[\[28\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Press%20,permission%20modes).
The auto-compaction behavior is also
confirmed[\[8\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20manages%20context%20automatically,server%20costs).
However, some baseline statements need refinement or lack support. For
instance, the baseline's claim that *Plan Mode "uses Opus for deep
reasoning"* is **Unverified** (official docs allow model choice but do
not mandate which model is used in Plan
Mode)[\[2\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20uses%20Claude%20models,the%20model%20doing%20the%20reasoning).
The shortcut "press Shift+Tab twice" to enter Plan Mode is an
oversimplification: **Shift+Tab toggles among modes**, and Plan Mode is
one of
them[\[28\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Press%20,permission%20modes)
(Verified that Shift+Tab switches modes, but "twice" is not documented).
The baseline's description of "dangerously skip permissions" is also not
in the guides (although the CLI flag exists, the docs actually show how
to disable it for policy via
`disableBypassPermissionsMode`[\[27\]](https://code.claude.com/docs/en/settings#:~:text=files%20from%20Claude%20Code%20access,to%20prevent%20%60bypassPermissions)),
so that claim is **Refined**: in practice one can bypass or disable
bypass, but it's an advanced escape hatch. Finally, the baseline's focus
on tasks (parallel subagents and task lists) is only partially covered
officially (there is a task-sharing feature via
`CLAUDE_CODE_TASK_LIST_ID`[\[33\]](https://code.claude.com/docs/en/settings#:~:text=should%20handle%20hostname%20resolution%20,on%20Unix%2FmacOS)),
but the detailed "Tasks" system described by the baseline is mostly
external or prescriptive. In short, official docs confirm the core
interaction modes (Verified), while speculative workflows or
model-specific claims are Unverified or need reframing.

## Summary of Baseline Claims

-   **Verified:** Baseline claims that directly match official docs,
    e.g. hierarchical config file locations, permission modes
    (Default/Auto/Plan), CLAUDE.md loading rules, use of skills/hooks,
    etc. (Cited above in each section.)
-   **Refined:** Baseline claims that overlap but need adjustment: e.g.
    default model or mode values ("plan" is a valid mode but not the
    default)[\[28\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Press%20,permission%20modes)[\[27\]](https://code.claude.com/docs/en/settings#:~:text=files%20from%20Claude%20Code%20access,to%20prevent%20%60bypassPermissions);
    `--dangerously-skip-permissions` (docs show how to disable
    it)[\[27\]](https://code.claude.com/docs/en/settings#:~:text=files%20from%20Claude%20Code%20access,to%20prevent%20%60bypassPermissions);
    context auto-compaction exists, but many baseline strategies around
    it are user tips rather than spec.
-   **Unverified:** Claims without official support: e.g. specifics
    about which model is used in Plan Mode, claims about internal
    concurrency, or any overspecification (like "Plan Mode requires two
    Shift+Tab presses"), or custom conventions (like "profiles" folders,
    special task systems) not documented. These would require testing or
    more info.

Overall, the **official documentation and source code confirm the core
architecture, file/config layout, and interaction semantics of Claude
Code**. Where the baseline guide adds extra patterns or heuristics,
those are largely advisory and go beyond what's codified; we mark them
as refined or unverified, suggesting caution. All official details above
are cited from Anthropic's current docs and repos (as of Jan 28,
2025)[\[1\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=autonomously%20but%20stays%20responsive%20to,into%20a%20capable%20coding%20agent)[\[28\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Press%20,permission%20modes)[\[11\]](https://code.claude.com/docs/en/settings#:~:text=,that%20need%20centralized%20control%2C%20Claude)[\[17\]](https://code.claude.com/docs/en/memory#:~:text=Memory%20Type%20Location%20Purpose%20Use,specific%20project%20instructions).

[\[1\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=autonomously%20but%20stays%20responsive%20to,into%20a%20capable%20coding%20agent)
[\[2\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20uses%20Claude%20models,the%20model%20doing%20the%20reasoning)
[\[3\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Tools)
[\[4\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Each%20tool%20use%20gives%20Claude,right%20extension%20for%20your%20needs)
[\[5\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Manage%20context%20with%20skills%20and,subagents)
[\[6\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=This%20guide%20focuses%20on%20the,Claude%20Code%20gains%20access%20to)
[\[7\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%E2%80%99s%20context%20window%20holds%20your,to%20see%20what%E2%80%99s%20using%20space)
[\[8\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20manages%20context%20automatically,server%20costs)
[\[9\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Undo%20changes%20with%20checkpoints)
[\[10\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Claude%20Code%20saves%20your%20conversation,md)
[\[26\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=When%20you%20resume%20a%20session,session%60%20flag)
[\[28\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Press%20,permission%20modes)
[\[31\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=refactor%20might%20involve%20extensive%20verification,into%20a%20capable%20coding%20agent)
[\[32\]](https://code.claude.com/docs/en/how-claude-code-works#:~:text=Ask%20Claude%20Code%20for%20help)
How Claude Code works - Claude Code Docs

<https://code.claude.com/docs/en/how-claude-code-works>

[\[11\]](https://code.claude.com/docs/en/settings#:~:text=,that%20need%20centralized%20control%2C%20Claude)
[\[12\]](https://code.claude.com/docs/en/settings#:~:text=ignore%20,code%2F%60%20%2A%20Windows%3A%20%60C%3A%5CProgram%20Files%5CClaudeCode)
[\[13\]](https://code.claude.com/docs/en/settings#:~:text=How%20scopes%20interact)
[\[14\]](https://code.claude.com/docs/en/settings#:~:text=,mcp.json)
[\[15\]](https://code.claude.com/docs/en/settings#:~:text=Feature%20User%20location%20Project%20location,project)
[\[24\]](https://code.claude.com/docs/en/settings#:~:text=Variable%20Purpose%20,See%20%2032)
[\[25\]](https://code.claude.com/docs/en/settings#:~:text=,client%20certificate%20file%20for%20mTLS)
[\[27\]](https://code.claude.com/docs/en/settings#:~:text=files%20from%20Claude%20Code%20access,to%20prevent%20%60bypassPermissions)
[\[33\]](https://code.claude.com/docs/en/settings#:~:text=should%20handle%20hostname%20resolution%20,on%20Unix%2FmacOS)
Claude Code settings - Claude Code Docs

<https://code.claude.com/docs/en/settings>

[\[16\]](https://code.claude.com/docs/en/memory#:~:text=Memory%20Type%20Location%20Purpose%20Use,Team%20members%20via%20source%20control)
[\[17\]](https://code.claude.com/docs/en/memory#:~:text=Memory%20Type%20Location%20Purpose%20Use,specific%20project%20instructions)
[\[18\]](https://code.claude.com/docs/en/memory#:~:text=instructions%20managed%20by%20IT%2FDevOps%20Company,Team%20members%20via%20source%20control)
[\[19\]](https://code.claude.com/docs/en/memory#:~:text=%E2%80%A2%20Windows%3A%20%60C%3A%5CProgram%20Files%5CClaudeCode%5CCLAUDE.md%20%60Organization,specific%20project%20instructions)
Manage Claude\'s memory - Claude Code Docs

<https://code.claude.com/docs/en/memory>

[\[20\]](https://code.claude.com/docs/en/skills#:~:text=For%20built,Claude%20invokes%20them%2C%20and%20the)
[\[21\]](https://code.claude.com/docs/en/skills#:~:text=match%20at%20L187%20Personal%60~%2F.claude%2Fskills%2F%3Cskill,name%3E%2FSKILL.md%20%60Where%20plugin%20is%20enabled)
[\[22\]](https://code.claude.com/docs/en/skills#:~:text=Every%20skill%20needs%20a%20,helps%20Claude%20decide%20when%20to)
Extend Claude with skills - Claude Code Docs

<https://code.claude.com/docs/en/skills>

[\[23\]](https://github.com/anthropics/claude-code/issues/11795#:~:text=Problem%20Statement)
Link to JSON Schema for settings.json in the official docs · Issue
#11795 · anthropics/claude-code · GitHub

<https://github.com/anthropics/claude-code/issues/11795>

[\[29\]](https://code.claude.com/docs/en/interactive-mode#built-in-commands#:~:text=,usage%20as%20a%20colored%20grid)
Interactive mode - Claude Code Docs

<https://code.claude.com/docs/en/interactive-mode>

[\[30\]](https://code.claude.com/docs/en/hooks-guide#:~:text=Claude%20Code%20hooks%20are%20user,to%20choose%20to%20run%20them)
Get started with Claude Code hooks - Claude Code Docs

<https://code.claude.com/docs/en/hooks-guide>
