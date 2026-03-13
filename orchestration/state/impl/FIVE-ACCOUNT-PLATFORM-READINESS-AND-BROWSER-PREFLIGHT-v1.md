# Five-Account Platform Readiness And Browser Preflight v1

**Status**: staged
**Class**: bounded readiness law
**Purpose**: make the browser-bound execution frontier precise for the five chain emails already available in Keychain without treating live platform state as repo-local law

## Compact Rule

- the five chain emails being available in Keychain establishes only local identity availability
- platform-account existence on YouTube, X, Pinterest, and later surfaces is an external-bound fact that must be observed, not declared by repo text
- platform session readiness is narrower than account existence and requires identity-confirmed, isolated browser state
- capture readiness is narrower than session readiness and exists only when read-only evidence can be gathered without account creation or social mutation
- actual account creation, onboarding completion, follow/subscription/save/board mutation, and any other live platform write remain out of scope
- ambiguity, session contamination, or forced mutation stops execution immediately

## 1. Lawful Inputs

This readiness law is derivative of:

1. [CODEX-CAMPAIGN-13-ACUMEN-CC92-CONSTELLATION-LAW-IMPORT-AND-ENFORCEMENT-v1.md](/Users/system/syncrescendence/orchestration/state/impl/CODEX-CAMPAIGN-13-ACUMEN-CC92-CONSTELLATION-LAW-IMPORT-AND-ENFORCEMENT-v1.md)
2. [CAMPAIGN-12-ACUMEN-CC91-INBOUND-FEED-CONSTELLATION-AND-PRODUCTIZATION-SYNTHESIS-v1.md](/Users/system/syncrescendence/orchestration/state/impl/CAMPAIGN-12-ACUMEN-CC91-INBOUND-FEED-CONSTELLATION-AND-PRODUCTIZATION-SYNTHESIS-v1.md)
3. [EXOCORTEX-ACCOUNT-IDENTITY-MATRIX-CC76.md](/Users/system/syncrescendence/orchestration/state/impl/EXOCORTEX-ACCOUNT-IDENTITY-MATRIX-CC76.md)
4. [LOCAL-SURFACE-STATUS.md](/Users/system/syncrescendence/orchestration/state/LOCAL-SURFACE-STATUS.md)
5. [CANON-25220-ACCOUNT_FEED_ARCH-satellite-CONSTELLATION_ARCH-lattice.md](/Users/system/Desktop/canon/CANON-25220-ACCOUNT_FEED_ARCH-satellite-CONSTELLATION_ARCH-lattice.md)

No browser tab, remembered login, suggested account switcher, or platform-local draft may outrank repo law.
At the same time, repo law may not pretend that an external platform account exists when that existence has not yet been observed.

## 2. The Four Distinctions

The frontier must remain split into four non-equivalent states.

### 2.1 Already-Available Email / Keychain Identity

This means:

- a chain email exists
- local access material or pointer is present in Keychain
- the intended identity slot can be named before browser work begins

This does **not** mean:

- a YouTube channel exists
- an X account exists
- a Pinterest account exists
- any browser session is currently authenticated

### 2.2 Platform Account Existence

This means a human has externally observed that the target platform already has an account, channel, or profile bound to the intended identity.

Allowed outcomes:

- `observed_exists`
- `observed_absent`
- `unconfirmed`

This state is external-bound.
The repo may record the observation result, but it may not invent it.

### 2.3 Platform Session Readiness

This means:

- the browser context is isolated to one chain identity
- the platform shows the intended logged-in identity or platform handle
- the session is stable enough to navigate the required read-only surfaces

Allowed outcomes:

- `session_ready`
- `session_blocked`
- `session_contaminated`
- `session_unconfirmed`

An existing account without an isolated correct session is not ready.

### 2.4 Capture Readiness

This means:

- the relevant read-only surface is visible
- the operator can inspect or capture evidence without creating an account
- no follow, subscribe, board creation, or onboarding action is required to proceed

Allowed outcomes:

- `capture_ready`
- `capture_blocked`
- `capture_requires_mutation`
- `capture_unconfirmed`

## 3. External-Bound Execution Rule

Repo-local law may define:

- the order of operations
- required evidence classes
- isolation discipline
- stop conditions
- checklist structure

Repo-local law may **not** do any of the following by declaration alone:

- create a platform account
- assert that a platform account exists when it has not been observed
- ratify a platform-local follow graph
- treat a live browser session as durable truth

If a platform offers only a create-account path, interest-picker flow, or profile-completion wizard, the lawful repo outcome is `observed_absent` or `capture_requires_mutation`, not a forced continuation.

## 4. Identity Confirmation

Before any browser work:

1. identify the intended chain slot as `CHAIN-01` through `CHAIN-05`
2. confirm the corresponding email identity from Keychain without copying secrets into repo artifacts
3. bind one browser profile or container to that chain slot for the duration of the check
4. confirm that the browser-visible email, handle, avatar, or account switcher state matches the intended slot

If the operator cannot answer "which exact chain identity is this browser context using?" execution stops.

## 5. Session Isolation

Isolation requirements:

- one dedicated browser profile, container, or equivalent isolated context per chain slot
- no mixed-login state for multiple chain identities inside the same active context
- no reliance on a generic default browser profile
- no simultaneous cross-slot execution in a single profile
- one platform is checked at a time inside the active isolated context

If a context auto-switches identities, exposes multiple plausible logged-in identities, or inherits another slot's remembered session, mark the result `session_contaminated` and stop that branch.

## 6. Capture Order

The lawful order is:

1. confirm the intended Keychain-backed chain identity
2. establish isolated browser context for that chain identity
3. check platform-account existence
4. check platform session readiness
5. check capture readiness
6. record result or blocker before moving to the next platform

Platform order for this wave:

1. YouTube
2. X
3. Pinterest
4. other later surfaces only after the first three have been classified for the active chain slot

This order is chosen because YouTube compatibility is already the leading registry concern in the campaign law, X and Pinterest are the next explicitly named outward surfaces, and later surfaces should not blur the first proof boundary.

## 7. Stop Conditions

Execution stops immediately for the active chain slot and platform if any of the following occurs:

- intended chain identity cannot be confirmed from Keychain-backed local evidence
- browser context shows the wrong email, wrong handle, or ambiguous switcher state
- the platform requires account creation to continue
- the platform requires onboarding, interest selection, channel setup, board setup, or profile completion to reach the target surface
- the operator would need to follow, subscribe, save, pin, or otherwise mutate live platform state to continue
- MFA or recovery challenge cannot be completed safely in the current window
- the session cannot be isolated cleanly from another chain slot
- the read-only capture surface cannot be reached without mutation

The correct action after a stop is to record the blocker precisely, not to improvise around it.

## 8. Allowed Repo Outputs

This preflight may lawfully produce only:

- readiness classifications
- blocker notes
- capture-order decisions
- isolation decisions
- evidence pointers or operator notes that avoid secret leakage

It may not produce:

- hidden platform writes
- silent account creation
- live follow/subscription mutations
- claims that a later surface is ready because a different surface was ready

## 9. Completion Definition For This Wave

This wave is complete when, for each of the five chain identities and for each currently in-scope platform, the repo can distinguish:

- whether the email/keychain identity is available
- whether a platform account already exists
- whether an isolated session is ready
- whether read-only capture is ready
- which exact stop condition blocks progress if any of the above is false

That is sufficient to make the next browser-bound execution frontier precise.
It is intentionally insufficient to justify live platform mutation.
