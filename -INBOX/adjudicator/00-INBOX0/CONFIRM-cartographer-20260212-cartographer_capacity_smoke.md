# CONFIRM-cartographer-20260212-cartographer_capacity_smoke

**Kind**: CONFIRM
**Task**: TASK-20260212-cartographer_capacity_smoke.md
**From-Agent**: cartographer
**To-Agent**: adjudicator
**Status**: FAILED
**Exit-Code**: 1
**Completed-At**: 2026-02-12T23:53:43Z
**Finalized-Task-Path**: `/Users/home/Desktop/syncrescendence/-INBOX/cartographer/50_FAILED/TASK-20260212-cartographer_capacity_smoke.md`
**Result-Path**: `/Users/home/Desktop/syncrescendence/-OUTBOX/cartographer/RESULTS/RESULT-cartographer-20260212-cartographer_capacity_smoke.md`
**Execution-Log**: `/Users/home/Desktop/syncrescendence/-INBOX/adjudicator/00-INBOX0/EXECLOG-cartographer-20260212-cartographer_capacity_smoke.log`

---

## Execution Log Tail

```text
Server 'securityServer' supports tool updates. Listening for changes...
Server 'securityServer' supports prompt updates. Listening for changes...
Hook registry initialized with 4 hook entries
Error executing tool run_shell_command: Tool "run_shell_command" not found. Did you mean one of: "run_long_command", "self_command", "run_poc"?
Attempt 1 failed with status 429. Retrying with backoff... GaxiosError: [{
  "error": {
    "code": 429,
    "message": "No capacity available for model gemini-2.5-pro on the server",
    "errors": [
      {
        "message": "No capacity available for model gemini-2.5-pro on the server",
        "domain": "global",
        "reason": "rateLimitExceeded"
      }
    ],
    "status": "RESOURCE_EXHAUSTED",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "reason": "MODEL_CAPACITY_EXHAUSTED",
        "domain": "cloudcode-pa.googleapis.com",
        "metadata": {
          "model": "gemini-2.5-pro"
        }
      }
    ]
  }
}
]
    at Gaxios._request (/opt/homebrew/Cellar/gemini-cli/0.28.2/libexec/lib/node_modules/@google/gemini-cli/node_modules/gaxios/build/src/gaxios.js:142:23)
    at process.processTicksAndRejections (node:internal/process/task_queues:104:5)
    at async OAuth2Client.requestAsync (/opt/homebrew/Cellar/gemini-cli/0.28.2/libexec/lib/node_modules/@google/gemini-cli/node_modules/google-auth-library/build/src/auth/oauth2client.js:429:18)
    at async CodeAssistServer.requestStreamingPost (file:///opt/homebrew/Cellar/gemini-cli/0.28.2/libexec/lib/node_modules/@google/gemini-cli/node_modules/@google/gemini-cli-core/dist/src/code_assist/server.js:171:21)
    at async CodeAssistServer.generateContentStream (file:///opt/homebrew/Cellar/gemini-cli/0.28.2/libexec/lib/node_modules/@google/gemini-cli/node_modules/@google/gemini-cli-core/dist/src/code_assist/server.js:29:27)
    at async file:///opt/homebrew/Cellar/gemini-cli/0.28.2/libexec/lib/node_modules/@google/gemini-cli/node_modules/@google/gemini-cli-core/dist/src/core/loggingContentGenerator.js:138:26
    at async retryWithBackoff (file:///opt/homebrew/Cellar/gemini-cli/0.28.2/libexec/lib/node_modules/@google/gemini-cli/node_modules/@google/gemini-cli-core/dist/src/utils/retry.js:109:28)
    at async GeminiChat.makeApiCallAndProcessStream (file:///opt/homebrew/Cellar/gemini-cli/0.28.2/libexec/lib/node_modules/@google/gemini-cli/node_modules/@google/gemini-cli-core/dist/src/core/geminiChat.js:431:32)
    at async GeminiChat.streamWithRetries (file:///opt/homebrew/Cellar/gemini-cli/0.28.2/libexec/lib/node_modules/@google/gemini-cli/node_modules/@google/gemini-cli-core/dist/src/core/geminiChat.js:263:40)
    at async Turn.run (file:///opt/homebrew/Cellar/gemini-cli/0.28.2/libexec/lib/node_modules/@google/gemini-cli/node_modules/@google/gemini-cli-core/dist/src/core/turn.js:66:30) {
  config: {
    url: 'https://cloudcode-pa.googleapis.com/v1internal:streamGenerateContent?alt=sse',
    method: 'POST',
    params: { alt: 'sse' },
    headers: {
      'Content-Type': 'application/json',
      'User-Agent': 'GeminiCLI/0.28.2/gemini-2.5-pro (darwin; arm64) google-api-nodejs-client/9.15.1',
      Authorization: '<<REDACTED> - See `errorRedactor` option in `gaxios` for configuration>.',
      'x-goog-api-client': 'gl-node/25.6.1'
    },
    responseType: 'stream',
    body: '<<REDACTED> - See `errorRedactor` option in `gaxios` for configuration>.',
    signal: AbortSignal { aborted: false },
    paramsSerializer: [Function: paramsSerializer],
    validateStatus: [Function: validateStatus],
    errorRedactor: [Function: defaultErrorRedactor]
  },
  response: {
    config: {
      url: 'https://cloudcode-pa.googleapis.com/v1internal:streamGenerateContent?alt=sse',
      method: 'POST',
      params: [Object],
      headers: [Object],
      responseType: 'stream',
      body: '<<REDACTED> - See `errorRedactor` option in `gaxios` for configuration>.',
      signal: [AbortSignal],
      paramsSerializer: [Function: paramsSerializer],
      validateStatus: [Function: validateStatus],
      errorRedactor: [Function: defaultErrorRedactor]
    },
    data: '[{\n' +
      '  "error": {\n' +
      '    "code": 429,\n' +
      '    "message": "No capacity available for model gemini-2.5-pro on the server",\n' +
      '    "errors": [\n' +
      '      {\n' +
      '        "message": "No capacity available for model gemini-2.5-pro on the server",\n' +
      '        "domain": "global",\n' +
      '        "reason": "rateLimitExceeded"\n' +
      '      }\n' +
      '    ],\n' +
      '    "status": "RESOURCE_EXHAUSTED",\n' +
      '    "details": [\n' +
      '      {\n' +
      '        "@type": "type.googleapis.com/google.rpc.ErrorInfo",\n' +
      '        "reason": "MODEL_CAPACITY_EXHAUSTED",\n' +
      '        "domain": "cloudcode-pa.googleapis.com",\n' +
      '        "metadata": {\n' +
      '          "model": "gemini-2.5-pro"\n' +
      '        }\n' +
      '      }\n' +
      '    ]\n' +
      '  }\n' +
      '}\n' +
      ']',
    headers: {
      'alt-svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000',
      'content-length': '606',
      'content-type': 'application/json; charset=UTF-8',
      date: 'Thu, 12 Feb 2026 23:52:36 GMT',
      server: 'ESF',
      'server-timing': 'gfet4t7; dur=5447',
      vary: 'Origin, X-Origin, Referer',
      'x-cloudaicompanion-trace-id': '8d16f0230ea941e7',
      'x-content-type-options': 'nosniff',
      'x-frame-options': 'SAMEORIGIN',
      'x-xss-protection': '0'
    },
    status: 429,
    statusText: 'Too Many Requests',
    request: {
      responseURL: 'https://cloudcode-pa.googleapis.com/v1internal:streamGenerateContent?alt=sse'
    }
  },
  error: undefined,
  status: 429,
  Symbol(gaxios-gaxios-error): '6.7.1'
}
Error executing tool obsidian_create_note: Tool execution denied by policy.
Error executing tool run_long_command: Tool execution denied by policy.
Error executing tool self_command: Tool execution denied by policy.
```

