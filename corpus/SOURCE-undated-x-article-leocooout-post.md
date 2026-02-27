today I did an exploration and reduced the file search time in the TikTok codebase from nearly 8s to less than 200ms. mentioning any file in Claude is practically instantaneous now

the default configuration of fast filesystem traversal is good for smaller projects but for large-scale projects a custom indexing system is recommended

Claude lets you customize this configuration via settings.json

{
  "fileSuggestion": {
    "type": "command",
    "command": "~/.claude/file-suggestion.sh"
  }
}


my script does a quick indexing on initialization, caches it in table form, and I added some invalidation and update mechanisms in case new files are added

in summary I use FTS5 (full-text search) to do the search in the table and use the ranking system to filter relevant results for R&D