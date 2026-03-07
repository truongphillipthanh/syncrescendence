# Response

**Response ID**: `RSP-20260306-codex-swarm-wave-2-lane-01-knowledge-compatibility`
**Surface**: `codex_parallel_session`
**Date received**: `2026-03-06`
**Dispatch packet**: `PKT-20260306-codex-swarm-wave-2-lane-01-knowledge-compatibility`
**Result state**: `complete`

## 1. Exact Docs That Must Change Now

The smallest live-facing write set that stops the repo from presenting bare `knowledge/references/` as the sovereign secondary lane is:

1. `README.md`
2. `knowledge/README.md`
3. `knowledge/feedstock/README.md`
4. `knowledge/references/README.md`

These four surfaces are sufficient because they are the live-facing readmes that still either:

- omit `knowledge/sigma/` where the lane hierarchy is introduced,
- route promotion directly into bare `knowledge/references/`,
- or describe `knowledge/references/` as its own lane rather than as compatibility housing.

No change is required now to:

- `orchestration/state/impl/KNOWLEDGE-LANE-LAW-v1.md`
- `knowledge/sigma/README.md`

Those two files already ratify Sigma correctly and already preserve compatibility semantics without treating bare `references/` as enduring lane sovereignty.

## 2. Patch-Ready Diffs

### `README.md`

```diff
--- a/README.md
+++ b/README.md
@@
- - [knowledge](/Users/system/syncrescendence/knowledge): distilled references, domain canon, and incoming feedstock
+ - [knowledge](/Users/system/syncrescendence/knowledge): Sigma-tier doctrine, housed reference substrates, domain canon, and incoming feedstock
@@
- - [knowledge/references/neocorpus](/Users/system/syncrescendence/knowledge/references/neocorpus): internalized distilled research substrate from the predecessor shell
+ - [knowledge/sigma](/Users/system/syncrescendence/knowledge/sigma): live secondary knowledge tier below canon
+ - [knowledge/references/neocorpus](/Users/system/syncrescendence/knowledge/references/neocorpus): compatibility-housed Sigma reference substrate presently treated semantically as `knowledge/sigma/references/neocorpus/`
```

### `knowledge/README.md`

```diff
--- a/knowledge/README.md
+++ b/knowledge/README.md
@@
 Use it for:
 
- - distilled reference substrates
+ - Sigma-tier secondary doctrine
+ - housed reference substrates
 - promoted domain canon
 - incoming research feedstock
@@
 Start here:
 
 - [CHARTER.md](/Users/system/syncrescendence/knowledge/CHARTER.md)
- - [references](/Users/system/syncrescendence/knowledge/references)
+ - [sigma](/Users/system/syncrescendence/knowledge/sigma)
+ - [references](/Users/system/syncrescendence/knowledge/references) (compatibility housing for `knowledge/sigma/references/`)
 - [canon](/Users/system/syncrescendence/knowledge/canon)
 - [feedstock](/Users/system/syncrescendence/knowledge/feedstock)
```

### `knowledge/feedstock/README.md`

```diff
--- a/knowledge/feedstock/README.md
+++ b/knowledge/feedstock/README.md
@@
 Artifacts here should eventually be:
 
- - compacted into `knowledge/references/`
+ - compacted into `knowledge/sigma/references/`
+ - elevated into `knowledge/sigma/` when they become repeated-use secondary doctrine
 - promoted into `knowledge/canon/`
 - distilled into `playbooks/`
 - or retired as low-value noise
+
+During staged compatibility, the current physical `knowledge/references/` tree remains readable as housed Sigma reference material rather than as an independent lane.
```

### `knowledge/references/README.md`

```diff
--- a/knowledge/references/README.md
+++ b/knowledge/references/README.md
@@
 # References
 
-This lane holds distilled reference substrates that the current shell actively consults.
+This surface is the compatibility housing for `knowledge/sigma/references/`.
+
+It holds distilled reference substrates that the current shell actively consults, but they should be interpreted as Sigma reference material rather than as an independent top-level knowledge lane.
 
 Current occupant:
@@
 - [NEOCORPUS-CATEGORY-INDEX-v1.md](/Users/system/syncrescendence/knowledge/references/NEOCORPUS-CATEGORY-INDEX-v1.md)
 - [NEOCORPUS-INTERNALIZATION-v1.md](/Users/system/syncrescendence/knowledge/references/NEOCORPUS-INTERNALIZATION-v1.md)
+
+New documentation and classification decisions should name `knowledge/sigma/references/` as the enduring semantic destination while this compatibility path remains in place.
```

## 3. Compatibility Wording To Reuse

Use this sentence wherever a concise bridge is needed:

`knowledge/references/` remains live as the compatibility housing for `knowledge/sigma/references/`; it should stay readable and citable, but it should not be described as the sovereign secondary lane name.

Short form for bullets and link labels:

`knowledge/references/` (compatibility housing for `knowledge/sigma/references/`)

This wording preserves readability because it keeps the current path visible, while still making the Sigma semantic contract explicit.

## 4. Top Failure Modes If Skipped

1. Root and lane-entry docs continue teaching the wrong ontology, so new contributors will keep classifying secondary doctrine under bare `references/` instead of Sigma.
2. `knowledge/feedstock/README.md` continues routing compaction into the compatibility path as if it were the real destination, which reopens the very lane-contract drift Sigma ratification closed.
3. `knowledge/references/README.md` continues presenting itself as an independent lane, which dilutes the law and makes later subtree rehousing look like a semantic rename rather than a physical compatibility cleanup.
4. The repo keeps carrying contradictory public instructions: law says Sigma, but first-touch readmes still teach pre-ratification behavior.
5. Future path cleanup gets harder because more artifacts, prompts, and README prose will accumulate on the false assumption that `knowledge/references/` is permanent lane identity.

## 5. Status

`complete`

The minimal live-facing cleanup set is fully drafted above. The binding law already reflects Sigma correctly, so the required action now is only to update the four readme surfaces listed in Section 1.
