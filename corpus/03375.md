# Extraction: SOURCE-20260202-006

**Source**: `SOURCE-20260202-x-article-ryancarson-how_to_setup_your_agent_to_do_daily_testing_file_bugs.md`
**Atoms extracted**: 36
**Categories**: claim, concept, praxis_hook

---

## Claim (2)

### ATOM-SOURCE-20260202-006-0021
**Lines**: 240-242
**Context**: consensus / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.50, epistemic_stability=0.90

> The pre-signed Chrome debug profile, while essential for unattended testing, is a significant security liability because it contains live session cookies and OAuth tokens that bypass MFA.

### ATOM-SOURCE-20260202-006-0036
**Lines**: 313-314
**Context**: consensus / claim
**Tension**: novelty=0.40, consensus_pressure=0.50, contradiction_load=0.00, speculation_risk=0.20, actionability=0.80, epistemic_stability=0.70

> Autonomous QA can be achieved by providing an AI agent with a script, a schedule, and an issue tracker API, leveraging its existing knowledge of app interaction.

## Concept (1)

### ATOM-SOURCE-20260202-006-0003
**Lines**: 29-34
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.30, contradiction_load=0.20, speculation_risk=0.10, actionability=0.70, epistemic_stability=0.60

> Agent-Driven E2E testing differs from Traditional E2E by using accessibility tree snapshots to adapt to semantic changes, running daily to catch regressions, and providing 'real user journey' confidence, rather than relying on brittle CSS selectors and hardcoded sequences for PR gating.

## Praxis Hook (33)

### ATOM-SOURCE-20260202-006-0001
**Lines**: 3-5
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Implement a daily end-to-end (E2E) testing script that runs every morning to test signup and onboarding flows, including all agent tools, and automatically files bugs if issues are detected.

### ATOM-SOURCE-20260202-006-0002
**Lines**: 18-25
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To set up daily E2E testing, use a script scheduled via macOS launchd (or CI equivalent), ensure a fresh user is created for each run by deleting previous data from the database, auth provider, and payment provider, configure unattended Google OAuth using a pre-signed Chrome debug profile, and enable automatic bug filing with error details upon test failure.

### ATOM-SOURCE-20260202-006-0004
**Lines**: 37-42
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.60

> Use Agent-Driven E2E testing when your application has AI/chat flows with adaptive responses, you need to test actual user journeys, you prioritize a 'daily safety net' over PR gating, or you have OAuth flows that are difficult to mock.

### ATOM-SOURCE-20260202-006-0005
**Lines**: 45-49
**Context**: method / limitation
**Tension**: novelty=0.50, consensus_pressure=0.40, contradiction_load=0.10, speculation_risk=0.10, actionability=0.80, epistemic_stability=0.60

> Avoid Agent-Driven E2E testing if you require deterministic CI gating (use Playwright with mocked auth), cannot tolerate any flakiness, or lack a dedicated machine for the Chrome profile.

### ATOM-SOURCE-20260202-006-0006
**Lines**: 72-77
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> The daily E2E test script (`daily-e2e-test.sh`) should execute in four phases: Setup (kill Chrome, clear cookies, delete test user), Signup (open signup, click OAuth, handle consent), Onboarding (read AI message, pattern-match, respond), and Feature Tests (send tool prompts, verify responses, take screenshots).

### ATOM-SOURCE-20260202-006-0007
**Lines**: 79-79
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Upon test failure, the E2E script should automatically generate a report and file a bug in the issue tracker.

### ATOM-SOURCE-20260202-006-0008
**Lines**: 92-92
**Context**: method / claim
**Tension**: novelty=0.80, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To achieve unattended Google OAuth in E2E tests, launch Chrome with a debug profile that has been pre-signed into your test Google account.

### ATOM-SOURCE-20260202-006-0009
**Lines**: 109-116
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To handle both Google OAuth flows (account picker vs. direct consent), check the snapshot for 'choose an account' to click the test email, otherwise click 'Continue' on the consent page.

### ATOM-SOURCE-20260202-006-0010
**Lines**: 120-142
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Before each E2E test run, ensure a clean slate by deleting the test user from the database (which should cascade to related records), canceling subscriptions and deleting the customer from the payment provider, and deleting the user from the authentication provider.

### ATOM-SOURCE-20260202-006-0011
**Lines**: 145-150
**Context**: method / claim
**Tension**: novelty=0.70, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> When using `dotenv` for environment variables, use the `-o` flag to ensure production environment variables override local ones, preventing unintended use of development credentials.

### ATOM-SOURCE-20260202-006-0012
**Lines**: 153-170
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Implement an automatic bug filing function that, upon test failure, constructs a title and body including error details, log file paths, and screenshot directories, then sends a POST request to the issue tracker's API.

### ATOM-SOURCE-20260202-006-0013
**Lines**: 180-183
**Context**: method / claim
**Tension**: novelty=0.60, consensus_pressure=0.30, contradiction_load=0.10, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> To control noise from daily E2E tests and auto-filed bugs, implement retries for transient failures.

### ATOM-SOURCE-20260202-006-0014
**Lines**: 200-200
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To adapt bug reporting for GitHub Issues, use the `POST /repos/{owner}/{repo}/issues` endpoint.

### ATOM-SOURCE-20260202-006-0015
**Lines**: 201-201
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To adapt bug reporting for Linear, use the `POST /graphql` endpoint with an `issueCreate` mutation.

### ATOM-SOURCE-20260202-006-0016
**Lines**: 202-202
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To adapt bug reporting for Jira, use the `POST /rest/api/3/issue` endpoint.

### ATOM-SOURCE-20260202-006-0017
**Lines**: 211-223
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Implement a retry mechanism for transient failures by attempting an operation a maximum of 2 times with a 5-second sleep between attempts.

### ATOM-SOURCE-20260202-006-0018
**Lines**: 227-228
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Before filing a new bug, check for similar existing bugs created within the last 24 hours and comment on them instead of creating duplicates.

### ATOM-SOURCE-20260202-006-0019
**Lines**: 231-231
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Retain logs and screenshots for the last 7 days and automatically delete older runs to manage artifact storage.

### ATOM-SOURCE-20260202-006-0020
**Lines**: 234-234
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.70

> Configure alerting to page on-call personnel only after 2 or more consecutive failures, while single failures should generate a ticket without an immediate alert.

### ATOM-SOURCE-20260202-006-0022
**Lines**: 244-247
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Treat the `$HOME/chrome-debug-profile` directory with the same security level as production SSH keys, never running it on a shared machine and ensuring cleanup scripts invalidate Google sessions to limit the blast radius of a potential leak.

### ATOM-SOURCE-20260202-006-0023
**Lines**: 250-250
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Use a dedicated Google account for testing, not a personal one.

### ATOM-SOURCE-20260202-006-0024
**Lines**: 251-251
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Run automated tests on a locked-down machine, such as a Mac mini or a dedicated runner.

### ATOM-SOURCE-20260202-006-0025
**Lines**: 252-252
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Store tokens in a keychain or secret manager instead of plain `.env` files.

### ATOM-SOURCE-20260202-006-0026
**Lines**: 253-253
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Ensure test user data contains no real Personally Identifiable Information (PII).

### ATOM-SOURCE-20260202-006-0027
**Lines**: 254-254
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Sanitize screenshots by blurring sensitive areas before attaching them to tickets.

### ATOM-SOURCE-20260202-006-0028
**Lines**: 255-255
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Do not reuse your personal Chrome profile for automated testing.

### ATOM-SOURCE-20260202-006-0029
**Lines**: 256-256
**Context**: method / claim
**Tension**: novelty=0.10, consensus_pressure=0.80, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.90

> Do not run automated tests on shared developer laptops.

### ATOM-SOURCE-20260202-006-0030
**Lines**: 260-298
**Context**: method / claim
**Tension**: novelty=0.20, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> To schedule a daily E2E test script (`daily-e2e-test.sh`) at 9:00 AM on macOS, use a `launchd` plist configuration with `StartCalendarInterval` set to `Hour: 9` and `Minute: 0`.

### ATOM-SOURCE-20260202-006-0031
**Lines**: 302-304
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.70, contradiction_load=0.00, speculation_risk=0.10, actionability=0.90, epistemic_stability=0.80

> For CI environments (e.g., GitHub Actions, CircleCI), persist authentication using Playwright's `storageState` or use service accounts with API-based authentication instead of OAuth.

### ATOM-SOURCE-20260202-006-0032
**Lines**: 308-308
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Extend autonomous QA to payment testing using Stripe test cards.

### ATOM-SOURCE-20260202-006-0033
**Lines**: 309-309
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Extend autonomous QA to email verification using a controlled real inbox (e.g., Resend + webhook).

### ATOM-SOURCE-20260202-006-0034
**Lines**: 310-310
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Extend autonomous QA to multi-user scenarios by spawning multiple browser sessions.

### ATOM-SOURCE-20260202-006-0035
**Lines**: 311-311
**Context**: method / claim
**Tension**: novelty=0.30, consensus_pressure=0.60, contradiction_load=0.00, speculation_risk=0.20, actionability=0.90, epistemic_stability=0.70

> Extend autonomous QA to API integrations by triggering webhooks and verifying database state.
