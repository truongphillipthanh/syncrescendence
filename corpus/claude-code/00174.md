# CodeMode MCPs Thread

**Post 1 — Feb 5, 2026 at 9:17 PM**

i'm telling you, y'all are sleeping on codemode mcps - the agent just wrote this code to find exactly what it wanted w/ no context pollution

(Description: Code snippet showing a command-line interface execution with async function that retrieves specific methods from runtime and processes them with interrupt handlers and memory/stack limit management. Contains variables for `runtimeBase`, `interruptIdx`, `memLimitIdx`, `stackSizeIdx`, and `executeJobIdx` extracted via `findIndexCL`, followed by return statement joining formatted interrupt handler and memory limit data with newline characters.)
```javascript
@opensrc_execute [code=async () => {
  // Get specific methods from runtime
  const runtimeBase = await opensrc.read("rquickjs", "core/src/runtime/base.rs");

  // Extract interrupt handler and memory/stack limit sections
  const lines = runtimeBase.split('\\n');
  const interruptIdx = lines.findIndexCL => l.includes('set_interrupt_handler'));
  const memLimitIdx = lines.findIndexCL => l.includes('set_memory_limit'));
  const stackSizeIdx = lines.findIndexCL => l.includes('set_max_stack_size'));
  const executeJobIdx = lines.findIndexCL => l.includes('execute_pending_job'));

  return {
    interruptHandler: lines.slice(Math.max(0, interruptIdx - 5), interruptIdx + 25).join('\\n'),
    memoryLimit: lines.slice(Math.max(0, memLimitIdx - 3), memLimitIdx + 15).join('\\n'),
    stackSize: lines.slice(Math.max(0, stackSizeIdx - 3), stackSizeIdx + 15).join('\\n'),
    executeJob: lines.slice(Math.max(0, executeJobIdx - 5), executeJobIdx + 20).join('\\n')
  }
}]
```

**Post 2 — Feb 5, 2026**

(Description: Code snippet continuing the execution pattern with async function looking for serde_json conversion. Contains opensrc.grep call searching for "serde_json" with sources array including "rquickjs" and file include patterns for "*.rs" files. Conditional logic checks if results exist, reads the file content, and attempts conversion. Otherwise includes fallback check for convert module with opensrc.files call and mapping function.)
```javascript
@opensrc_execute [code=async () => {
  // Look for serde_json conversion
  const results = await opensrc.grep("serde_json", {
    sources: ["rquickjs"],
    include: "*.rs"
  });

  if (results.length > 0) {
    const file = results.file;
    return await opensrc.read("rquickjs", file);
  }

  // Otherwise check for convert module
  const convertFiles = await opensrc.files("rquickjs", "core/src/value/convert/*.rs");
  return { found: results.length > 0, files: convertFiles.map(f => f.path) };
}]
```

**Post 3 — Feb 5, 2026**

(Description: Code snippet showing another async execution pattern retrieving content from GitHub repository. Uses opensrc.get() method to fetch source code from "DelSkayn/rquickjs" repository. Contains logic that reads the source name and core/src/context/ctx.rs file, splits content by newlines, and iterates through lines checking for EvalOptions flag using JS_EVAL test. Relevant lines are pushed to an array with formatting, finally returning the relevant matches joined with newline characters.)
```javascript
@opensrc_execute [code=async () => {
  const source = opensrc.get("github.com/DelSkayn/rquickjs");
  const content = await opensrc.read(source.name, "core/src/context/ctx.rs");
  const lines = content.split("\\n");
  const relevant = [];
  for (let i = 0; i < lines.length; i++) {
    if (/EvalOptions|to_flag|JS_EVAL/.test(lines)) {
      relevant.push(`${i+1}: ${lines}`);
    }
  }
  return relevant.join('\\n');
}]
```