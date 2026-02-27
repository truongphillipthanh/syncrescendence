# CLAWDBOT Security Hardening: Top 10 Vulnerabilities and Their Fixes

As a Security / 98% AI YOLO Maximalist with Guardrails guy, I'm asking you to please listen to this.

Here are some of the top security issues with [clawd.bot](https://clawd.bot) that you all should be avoiding. Don't avoid the project. It's great. But please be safe with it!

## Vulnerabilities vs. Fixes

(Description: A two-column visual guide displayed with red skull/warning icons on the left for vulnerabilities and green shield checkmarks on the right for fixes. The vulnerabilities are listed in red text on the left, with corresponding remediation steps in green text on the right.)

### Vulnerabilities

1. Gateway exposed on 0.0.0.0:18789
2. DM policy allows all users
3. Sandbox disabled by default
4. Credentials in plaintext oauth.json
5. Prompt injection via web content
6. Dangerous commands unlocked
7. No network isolation
8. Elevated tool access granted
9. No audit logging enabled
10. Weak/default pairing codes

### Fixes

1. Set gateway.auth.token in environment
2. Set dm_policy to allowlist with explicit users
3. Enable sandbox=all + docker.network=none
4. Use env vars + chmod 600 permissions
5. Wrap untrusted content in untrusted tags
6. Block rm -rf, curl pipes, git push --force
7. Use Docker network isolation
8. Restrict MCP tools to minimum needed
9. Enable comprehensive session logging
10. Use cryptographic random codes + rate limiting

---

**Engagement Metrics:**
- Posted: 11:12 AM · Jan 26, 2026
- Views: 262.1K
- Replies: 93
- Reposts: 391
- Likes: 2.7K
- Bookmarks: 4.8K