# CC28 Intention Pruning Draft — Recon Only

**Date**: 2026-02-24
**Agent**: Commander (Claude Opus 4.6)
**Session**: CC28 Task 2
**Source**: ARCH-INTENTION_COMPASS.md v3.5.0 (97 intentions counted)
**Authority**: Sovereign approves all cuts. This is recon only.

---

## Summary Counts

| Verdict | Count |
|---------|-------|
| DONE | 38 |
| STALE | 14 |
| MERGED | 10 |
| ACTIVE | 35 |
| **Total** | **97** |

**Net result**: 38 DONE + 14 STALE + 10 MERGED = **62 removable** → leaves **35 ACTIVE** (within 30-40 target).

---

## DONE — Already Accomplished

| INT-ID | Title | Verdict | Evidence |
|--------|-------|---------|----------|
| INT-2301 | Fix Docker on Mac mini | DONE | DC-100 DONE. Neo4j 5.26.0 + Graphiti 0.22.0 healthy. Phase 0 complete. |
| INT-2302 | Agent fleet audit | DONE | DC-101 DONE. Fleet audited, SSH bridge verified. Phase 0 complete. |
| INT-2303 | Memory Phase 1 — memsync + JSONL | DONE | DC-110–113 all DONE. E2E write path verified. Safe build point `5a26d8f8`. |
| INT-2304 | Antifragile scaffold scripts | DONE | DC-120+121 DONE. scaffold_validate.sh + scaffold_heal.sh installed. `127ace0b`. |
| INT-1204 | Update CANON-25100 with Oracle Pedigree | DONE | Status already "resolved" in compass. CANON-25100 v2.1.0. |
| INT-1205 | Unified intention compass | DONE | Status already "resolved". This document IS the deliverable. |
| INT-1101 | Multi-CLI integration validation | DONE | Status already "resolved". DIRECTIVE-042B. |
| INT-1210 | Canonize Model Manual/Prompting | DONE | Status already "resolved". DIRECTIVE-044B audit. |
| INT-1211 | Canonize Platform Features | DONE | Status already "resolved". 77 CANON files. |
| INT-1212 | Canonize Model Qualities | DONE | Status already "resolved". 73 CANON files. |
| INT-1213 | Blitzkrieg model specification | DONE | Status already "resolved". CLAUDE.md v2.1.0. |
| INT-1502 | Inscribe narrative DNA | DONE | Status already "resolved". memory/narrative-dna.md. |
| INT-1507 | Appropriate martial/legal terminology | DONE | Status already "resolved". REF-ROSETTA_STONE.md v2.3.0. |
| INT-1508 | Track Yegge Gas Town + Anthropic Hivemind | DONE | Status already "resolved". memory/narrative-dna.md. |
| INT-1509 | launchd over cron | DONE | Status already "resolved". DEC-SOV-006, plists deployed. |
| INT-2201 | Complete repo rearchitecture | DONE | Status already "resolved". Agent offices deployed, collab/ created. |
| INT-2203 | Collaboration directory design | DONE | Status already "resolved". collab/ with anti-proliferation policy. |
| INT-0001 | Civilizational sensing infrastructure | DONE | Core framing established and operational. Status "resolved". |
| INT-0101 | Consumer/prosumer focus | DONE | Status "resolved". Ecosystem cartography scoped. |
| INT-0201 | Flat + symlink architecture | DONE | Status "resolved". Decision 2.1. |
| INT-0301 | Orchestration infrastructure pattern | DONE | Status "resolved". THE MODEL established. |
| INT-0302 | Reception Calibration vs Archetype Engineering | DONE | Status "resolved". Three-layer architecture decided. |
| INT-0401 | Canonize or delete | DONE | Status "superseded". Too aggressive — nuanced approach adopted. |
| INT-0402 | 79% file reduction | DONE | Status "resolved". Defrag completed. |
| INT-0403 | Nine evaluative lenses | DONE | Status "resolved". Extended to 18. |
| INT-0501 | Orchestration is protected infrastructure | DONE | Status "resolved". Constitutional rule. |
| INT-0502 | Genesis layer creation | DONE | Status "resolved". CANON-0000x series. |
| INT-0601 | Extended nine lenses to 18 | DONE | Status "resolved". STANDARDS.md. |
| INT-0602 | Bifurcation: filesystem vs Obsidian | DONE | Status "resolved". Decision 6.2. |
| INT-0701 | Review every conversation | DONE | Status "resolved". Forensic audit completed. |
| INT-0801 | Complete PROJ-001 transcript ingestion | DONE | Status "resolved". 43 sources processed. |
| INT-0901 | Directory restructuring to 00-06 | DONE | Status "resolved". Numbered scheme deployed. |
| INT-1001 | PROJ-011 automation infrastructure | DONE | Status "resolved". CLAUDE.md + Makefile. |
| INT-1002 | Multi-Claude coordination | DONE | Status "resolved". coordination.yaml. |
| INT-1101 (O11) | Parallel stream execution | DONE | Status "resolved". 4 streams completed. |
| INT-1102 (O11) | IIC configuration reconnaissance | DONE | Status "resolved". 14500+ lines reviewed. |
| INT-1103 | Gemini CLI validation | DONE | Status "resolved". APPROVED. |
| INT-1204 (O12) | Oracle Pedigree protocol | DONE | Status "resolved". CANON-25100 update. |

---

## STALE — No Activity in 5+ Sessions, No Blocking Dependency

| INT-ID | Title | Verdict | Evidence |
|--------|-------|---------|----------|
| INT-1201 | Accounts self-sustaining by month end | STALE | Status "failed". Jan 31 deadline missed. No reset target set. Last touched Oracle 12 (pre-Council 22). |
| INT-1207 | Manus before Perplexity | STALE | P3 deferred since Oracle 12. No activity. Platform prioritization obsolete. |
| INT-1208 | Promos for Perplexity + Gemini account | STALE | P3 deferred since Oracle 12. Cost optimization future. No activity. |
| INT-0802 | Modal 2 visual capabilities | STALE | P3 deferred. PROJ-009. No activity since Oracle 8. |
| INT-1102 (skills) | Skills conversion for top 5 functions | STALE | P3 deferred since Oracle 11. No activity. Superseded by INT-2404 skills audit. |
| INT-0701 (backlog) | Browser automation for account cloning | STALE | P3 deferred since Oracle 7. No activity. |
| INT-1214 | Deep Research: Claude Code + Anthropic | STALE | P2 deferred since Oracle 12. Prompt prepared but never executed. |
| INT-1215 | Deep Research: OpenAI Codex | STALE | P3 deferred since Oracle 12. Never started. |
| INT-1216 | Deep Research: Google Jules + Gemini CLI | STALE | P3 deferred since Oracle 12. Never started. |
| INT-1217 | Plan Mode as Oracle replacement | STALE | P3 deferred since Oracle 12. Obsolete — triangulation playbook supersedes. |
| INT-1218 | Permission fatigue mitigation | STALE | P3 deferred since Oracle 12. `skipDangerousModePermissionPrompt` is already set. |
| INT-1618 | Celestial alignment synchronization | STALE | P3 deferred. Poetic/cathartic. No operational dependency. |
| INT-0801 (backlog) | Tech Lunar 306K specs to CANON | STALE | P2 deferred since Oracle 8. PROJ-008. No activity. |
| INT-1901 | Avatarize Grok Build | STALE | P2 deferred. Blocked by Grok Build not publicly released. Still no release as of 2026-02-24. |

---

## MERGED — Subsumed by Another Intention

| INT-ID | Title | Verdict | Evidence |
|--------|-------|---------|----------|
| INT-2306 | Rename praxis sigma container | MERGED | Subsumed by DC-122 (Sovereign decision pending). Same scope. |
| INT-2307 | Numbered→semantic dir rename is Phase 4 | MERGED | Subsumed by DC-146 (SUPERSEDED per deferred commitments — sanctify numbered layers per DC-204T). |
| INT-1710 | Constellation pattern validated | MERGED | Subsumed by INT-P022 (same pattern observation). Status is meta-validation, not actionable work. |
| INT-1711 | Agent Vault = Human-Agent Shared Knowledge Graph | MERGED | Subsumed by INT-1707 (Three-Layer Memory Architecture). Same concept, INT-1707 is broader. |
| INT-1712 | Security perimeter is capability not network | MERGED | Subsumed by INT-1709 (Security is existential) + INT-P019 (Security as Binding Constraint). |
| INT-2410 | Constellation avatarization thesis | MERGED | Subsumed by INT-2411 (Psyche/Ajna recharacterization). INT-2410 is the theory, INT-2411 is the execution. Combine into one. |
| INT-C009 | Celestial alignment (capture) | MERGED | Duplicate of INT-1618. |
| INT-C008 | Notion/Airtable LifeOS discussion | MERGED | Subsumed by INT-1616 (LifeOS/PKM convergence) + INT-2408 (Exocortex integration). |
| INT-C010 | Notion/Airtable/PKM (capture) | MERGED | Duplicate of INT-C008, both subsumed by INT-1616 + INT-2408. |
| INT-C005 | Learn tmux | MERGED | tmux is operational. Subsumed by general constellation operations. |

---

## ACTIVE — Still Relevant, Has Open Work

| INT-ID | Title | Verdict | Evidence |
|--------|-------|---------|----------|
| INT-1202 | Capitalize on heavy machinery | ACTIVE | Ongoing velocity mandate. Evergreen. |
| INT-1203 | Design for 3 Claude + 1 Gemini + 1 ChatGPT | ACTIVE | Constellation architecture still evolving. Model registry updates ongoing. |
| INT-1206 | Complete IIC configs | ACTIVE | PROJ-002. Unfinished. |
| INT-1501 | Maximize Claude Code autonomy | ACTIVE | Autonomy ledger now at L1/200. Active progression. |
| INT-1503 | Close 30% fiduciary gap | ACTIVE | Linked to autonomy ledger. Active. |
| INT-1504 | Cascade deployment MBA↔Mac mini | ACTIVE | Mac mini offline. Relevant when it comes back. |
| INT-1506 | Neo-organization thesis | ACTIVE | Evergreen strategic framing. |
| INT-1601 | Syncrescript | ACTIVE | Sovereign interest confirmed CC27 (Ruby/Elixir sensibilities). |
| INT-1602 | IIC ingestion pipeline + feedcraft | ACTIVE | Blocked by account restructure. Still relevant. |
| INT-1603 | JIT-software HighCommand | ACTIVE | Dashboard design unbuilt. |
| INT-1604 | Web app memory audit + RAG strategy | ACTIVE | Unfinished. |
| INT-1612 | Begin ALL automations | ACTIVE | DC-130 DONE but DC-131/132/133 open. Partially done. |
| INT-1614 | Student + apprentice FDE modules | ACTIVE | P1. Personal domain integration. |
| INT-1616 | LifeOS/PKM convergence | ACTIVE | P1. Major strategic intention. |
| INT-1701 | Progressive Disclosure context loading | ACTIVE | Pattern identified, not yet implemented. |
| INT-1707 | Three-Layer Memory Architecture | ACTIVE | Phase 1 done but layers 2-3 (graph query, tacit knowledge) unbuilt. |
| INT-1709 | Security is existential | ACTIVE | DC-140 done (audit). DC-141 open (key rotation). Ongoing concern. |
| INT-1801 | Token Economics Dispatch | ACTIVE | No budget-aware routing built yet. |
| INT-1802 | Model Role Specialization | ACTIVE | Partially addressed by model_router.py. More to do. |
| INT-1803 | Open Model Onboarding (Cline + OpenCode) | ACTIVE | Cline installed, OpenCode not. Integration incomplete. |
| INT-2101 | Dual-stream architecture | ACTIVE | Major unbuilt pipeline. 0% automated intelligence stream. |
| INT-2104 | Feedcrafting algorithm | ACTIVE | Blocked by INT-2101. Core pipeline. |
| INT-2202 | MBA single-cockpit consolidation | ACTIVE | P1. Mac mini role evolving. |
| INT-2204 | Platform-native accommodation | ACTIVE | P1. Three sub-problems identified. |
| INT-2305 | Phase gate rule | ACTIVE | Constitutional. Evergreen enforcement. |
| INT-2401 | OpenClaw architecture harmonization | ACTIVE | Blocked by DC-208 research. |
| INT-2402 | CLI agent heterogeneity strategy | ACTIVE | Subsumes INT-2204(b). |
| INT-2404 | Skills audit + bleeding-edge shopping | ACTIVE | Blocked by DC-P16. |
| INT-2408 | Exocortex integration | ACTIVE | Major next-phase work. 19 files unprocessed. |
| INT-2412 | Recanonize after research | ACTIVE | Blocked by Phase 2C+2D. |
| INT-P004 | Globe before trees | ACTIVE | Evergreen design principle. |
| INT-P017 | File-First, Always | ACTIVE | Evergreen pattern. Operationally validated. |
| INT-P028 | Architecture without execution is decoration | ACTIVE | Seared lesson. Keep. |
| INT-P034 | Feedback loops > memory engineering | ACTIVE | From corpus synthesis. Novel insight. |
| INT-P035 | Security is Phase 0 | ACTIVE | Escalated from Phase 5. Active enforcement. |

---

## Borderline / Notes for Sovereign

1. **INT-1505 (Deep syncretization sci-fi narratives)** — Could be STALE (last active Session 15, Cartographer task). Currently classified ACTIVE above but a Sovereign call. Left out of ACTIVE list above — net effect is it should be STALE if Sovereign agrees. That would bring ACTIVE to 34.

2. **INT-1209 (Temporal intelligence refresh)** — DC-134 DONE (ledger_refresh.sh), but the broader vision (Live Ledger Phases 2-4) remains. Recommend DONE for the original intention, with remaining work tracked as DCs.

3. **Patterns INT-P006, P007, P009–P013, P014–P016, P018–P027, P029–P033, P036–P037** — 27 patterns total. Most are evergreen meta-observations. Recommend: keep the 5 most operationally relevant (P017, P028, P034, P035, P004), archive the rest as "RESOLVED — institutionalized" since they are now embedded in constitutional rules, AGENTS.md, or operational practice. This would remove ~22 more items but patterns are a different class than actionable intentions.

4. **Captures INT-C002, C003, C006, C007, C011, C012** — 6 pending captures never triaged. Recommend: C002 (STALE), C003 (STALE — revenue target never reset), C006 (MERGED into INT-MI19), C007 (DONE — tmux + parallel sessions operational), C011 (MERGED into INT-1803), C012 (MERGED into INT-1901).

---

## Recommended Final State

If Sovereign approves all verdicts above plus the borderline calls:

| Category | Count |
|----------|-------|
| Removed (DONE + STALE + MERGED) | ~62 |
| Remaining ACTIVE | ~35 |
| Patterns (archive candidates) | ~22 (separate decision) |

The 35 remaining ACTIVE intentions cluster around 5 themes:
1. **Pipeline/Feedcraft** (INT-2101, 2104, 1602, 1708) — the unbuilt intelligence pipeline
2. **Infrastructure** (INT-1612, 1801, 1803, 1804) — automations + sensing gaps
3. **Architecture** (INT-2202, 2204, 2401, 2402, 2408) — constellation design
4. **Content** (INT-2412, 1616, 1707) — knowledge enrichment
5. **Security/Hardening** (INT-1709, P035) — ongoing concern

---

*This file is a recon artifact. No changes have been made to ARCH-INTENTION_COMPASS.md. Sovereign reviews and approves cuts before any modifications.*
