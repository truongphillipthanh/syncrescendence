# Extraction: SOURCE-20260128-003

**Source**: `SOURCE-20260128-x-article-theonejvo-eating_lobster_souls_part_iii_the_finale_escape_the_moltrix.md`
**Atoms extracted**: 31
**Categories**: claim, concept, framework, praxis_hook

---

## Claim (23)

### ATOM-SOURCE-20260128-003-0001
**Lines**: 13-16
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.10, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.80

> Misconfigured infrastructure in Clawdbot control servers led to the leakage of API keys, OAuth tokens, conversation histories, and Signal device pairing credentials in world-readable temp files.

### ATOM-SOURCE-20260128-003-0002
**Lines**: 20-24
**Context**: anecdote / evidence
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.60, epistemic_stability=0.70

> A major flaw in ClawdHub's supply chain allowed a simulated backdoored skill to be inflated to the #1 download spot, leading to 16 developers executing arbitrary commands on their machines within 8 hours.

### ATOM-SOURCE-20260128-003-0003
**Lines**: 28-28
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.80

> Unlike previous demonstrations requiring user interaction, this vulnerability allows compromise simply by viewing a picture.

### ATOM-SOURCE-20260128-003-0005
**Lines**: 46-47
**Context**: anecdote / evidence
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.30, actionability=0.70, epistemic_stability=0.60

> Malicious code embedded in an SVG file can execute with full access to session cookies on the main clawdhub.com domain if served directly by ClawdHub's API.

### ATOM-SOURCE-20260128-003-0006
**Lines**: 49-52
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.60, contradiction_load=0.10, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> JavaScript inside an uploaded SVG running on the same domain as ClawdHub's own code can read authentication cookies, make API requests on the user's behalf, and perform any action the logged-in user could.

### ATOM-SOURCE-20260128-003-0008
**Lines**: 66-70
**Context**: anecdote / evidence
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> ClawdHub serves all user-uploaded content from the same domain (clawdhub.com), allowing attacker code to run with the user's identity due to shared cookies and session.

### ATOM-SOURCE-20260128-003-0009
**Lines**: 74-86
**Context**: anecdote / evidence
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.20, actionability=0.70, epistemic_stability=0.60

> ClawdHub's codebase lacks validation or sanitization for uploaded file content-types and serves them exactly as uploaded, without any SVG handling, security headers, Content-Security-Policy, or separate upload domain.

### ATOM-SOURCE-20260128-003-0010
**Lines**: 94-100
**Context**: consensus / evidence
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.90

> Cross-site scripting (XSS) has been a persistent problem, listed in the OWASP Top 10 for over two decades, with well-documented consequences such as the 2018 British Airways credit card skimming incident.

### ATOM-SOURCE-20260128-003-0011
**Lines**: 105-112
**Context**: consensus / evidence
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> In December 2025, the Trust Wallet Chrome extension was compromised via a supply-chain attack using a leaked API key, leading to the theft of approximately $8.5 million in crypto assets.

### ATOM-SOURCE-20260128-003-0012
**Lines**: 115-117
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.60, epistemic_stability=0.90

> JavaScript-based attacks are not exotic; they are novel in many cases and have been successfully compromising companies for twenty years, remaining a widespread issue.

### ATOM-SOURCE-20260128-003-0013
**Lines**: 116-117
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> The `<foreignObject>` element allows embedding full XHTML inside SVG, including script tags that execute in the document context.

### ATOM-SOURCE-20260128-003-0015
**Lines**: 127-128
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.20, actionability=0.30, epistemic_stability=0.80

> A real attacker's payload would be invisible, unlike the proof of concept which shows lobsters.

### ATOM-SOURCE-20260128-003-0017
**Lines**: 134-136
**Context**: anecdote / evidence
**Tension**: novelty=0.20, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.80

> ClawdHub stores authentication tokens, including JWTs and refresh tokens, in localStorage, which malicious SVGs have full access to on the clawdhub.com origin.

### ATOM-SOURCE-20260128-003-0018
**Lines**: 136-139
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.90

> Stealing a refresh token allows an attacker to mint new JWTs even after the current session expires, potentially granting access until the token is explicitly revoked.

### ATOM-SOURCE-20260128-003-0022
**Lines**: 166-169
**Context**: speculation / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.60, actionability=0.70, epistemic_stability=0.60

> The vulnerability extends to skill icons in listings: if they load automatically, an attacker's malicious icon can compromise a user who scrolls past it without clicking.

### ATOM-SOURCE-20260128-003-0023
**Lines**: 172-174
**Context**: speculation / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.60, actionability=0.70, epistemic_stability=0.60

> Security-conscious developers reviewing skill documentation can trigger the payload if documentation images are malicious, turning carefulness into an attack vector.

### ATOM-SOURCE-20260128-003-0024
**Lines**: 176-178
**Context**: speculation / claim
**Tension**: novelty=0.30, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.60, actionability=0.70, epistemic_stability=0.60

> Direct links to ClawdHub file URLs shared in messaging apps can lead to arbitrary JavaScript execution if the user views what they believe to be architecture documents.

### ATOM-SOURCE-20260128-003-0025
**Lines**: 180-181
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.80

> The end user can be compromised by simply browsing a trusted website, without installing, running, or clicking anything.

### ATOM-SOURCE-20260128-003-0026
**Lines**: 186-187
**Context**: anecdote / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> ClawdHub lacks a Content-Security-Policy (CSP) header, which would have blocked the described SVG script execution.

### ATOM-SOURCE-20260128-003-0027
**Lines**: 189-190
**Context**: anecdote / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> ClawdHub does not use a separate upload domain, which is industry standard for sandboxing user content away from session cookies.

### ATOM-SOURCE-20260128-003-0028
**Lines**: 192-193
**Context**: anecdote / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> ClawdHub performs no SVG sanitisation, storing files exactly as uploaded, despite the existence of libraries like DOMPurify for this purpose.

### ATOM-SOURCE-20260128-003-0029
**Lines**: 195-196
**Context**: anecdote / evidence
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.90

> ClawdHub lacks content-type validation, allowing a file named `readme.txt` to be uploaded as `image/svg+xml` and execute as SVG.

### ATOM-SOURCE-20260128-003-0030
**Lines**: 209-211
**Context**: consensus / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.20, actionability=0.40, epistemic_stability=0.70

> The vulnerabilities found in ClawdHub are not due to negligence but are a result of building fast in a rapidly moving space.

## Concept (1)

### ATOM-SOURCE-20260128-003-0004
**Lines**: 37-40
**Context**: consensus / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.10, actionability=0.20, epistemic_stability=0.90

> SVG (Scalable Vector Graphics) files are code, not just images, and can contain JavaScript that browsers parse and execute.

## Framework (1)

### ATOM-SOURCE-20260128-003-0007
**Lines**: 58-62
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.90, contradiction_load=0.00, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.90

> A common security practice for user uploads is to serve content from a completely different domain (e.g., raw.githubusercontent.com, googleusercontent.com, S3 bucket domains) to enforce strict isolation between domains and sandbox malicious code.

## Praxis Hook (6)

### ATOM-SOURCE-20260128-003-0014
**Lines**: 122-129
**Context**: method / evidence
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.10, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.60

> An SVG can be constructed using the <foreignObject> element to embed full XHTML, including script tags, allowing arbitrary JavaScript execution within the document context when viewed.

### ATOM-SOURCE-20260128-003-0016
**Lines**: 130-131
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Session theft can be achieved by reading authentication cookies and sending them to an attacker-controlled server with a single line of code, completely silently.

### ATOM-SOURCE-20260128-003-0019
**Lines**: 141-143
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> With a stolen session, an attacker can call any ClawdHub API endpoint as the victim, enabling account takeover actions like listing published skills, retrieving API tokens, or accessing account settings.

### ATOM-SOURCE-20260128-003-0020
**Lines**: 145-148
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.80

> Supply chain poisoning can occur if an attacker downloads a victim's skill, injects a backdoor, and publishes a 'patch,' using the victim's reputation to distribute malware.

### ATOM-SOURCE-20260128-003-0021
**Lines**: 150-152
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Persistence can be achieved by generating a new API token with an innocuous name and storing it externally, ensuring long-term access even if the victim changes their password.

### ATOM-SOURCE-20260128-003-0031
**Lines**: 212-214
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.60, actionability=0.60, epistemic_stability=0.80

> In software development, the question is not whether vulnerabilities will exist, but how quickly one responds when they are discovered.
