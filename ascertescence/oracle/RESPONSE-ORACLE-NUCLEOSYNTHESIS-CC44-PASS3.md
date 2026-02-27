## Edge Case 1: Scaffold Singletons

PORTAL-CHAT-AGENTS.md  
Decision: Move to agents/coordination/portal-chat-agents.md  
Rationale: Centers on inter-agent communication protocols, aligning with coordination rather than broad deployment infrastructure.

FLEET-COMMANDERS-HANDBOOK.md  
Decision: Move to agents/coordination/fleet-commanders-handbook.md  
Rationale: Operational handbook for fleet commanders emphasizes agent orchestration, better suited to coordination than deployment.

DEPLOYMENT-PLAYBOOK.md  
Decision: Retain in infrastructure/deployment/deployment-playbook.md  
Rationale: Explicitly details deployment procedures, reinforcing Pass 2's infrastructure focus without need for shift.

CONTINUOUS-IMPROVEMENT.md  
Decision: Move to agents/coordination/continuous-improvement.md  
Rationale: Procedural documentation for ongoing enhancements fits agent workflow coordination over static deployment.

WORK-LOOP.md  
Decision: Move to agents/coordination/work-loop.md  
Rationale: Operational playbook describing iterative loops aligns with agent coordination mechanisms.

INTER-AGENT.md  
Decision: Move to agents/coordination/inter-agent.md  
Rationale: Directly addresses inter-agent protocols, core to coordination subdirectory.

BOOT.md  
Decision: Retain in infrastructure/deployment/boot.md  
Rationale: Bootstrap procedures are foundational deployment steps, consistent with Pass 2 routing.

README.md  
Decision: Retain in infrastructure/deployment/readme.md  
Rationale: Directory index serves as entry point for deployment context, no strong case for relocation.

## Edge Case 2: Sources Singletons

FRONTMATTER_TEMPLATE.md  
Decision: Move to ontology/knowledge/frontmatter-template.md  
Rationale: Metadata template for sources supports knowledge structuring, fitting ontology over feedcraft.

DYN-SOURCES.csv  
Decision: Move to ontology/knowledge/dyn-sources.csv  
Rationale: Dynamic registry of sources aids knowledge management, better in ontology than uncategorized.

TRANSCRIPT_RECONCILIATION.md  
Decision: Move to knowledge/uncategorized/transcript-reconciliation.md  
Rationale: Post-processing artifact lacks clear topic, defaults to uncategorized knowledge pending review.

README.md  
Decision: Move to ontology/knowledge/readme.md  
Rationale: Directory index explains sources system, integrating with knowledge ontology.

index.md  
Decision: Move to ontology/knowledge/index.md  
Rationale: Source index provides metastructural overview, aligning with ontology/knowledge.

## Edge Case 3: Structural Voids

engine/02-ENGINE/certescence/  
Decision: Script deletes after confirming contents relocated to ascertescence/.  
Rationale: Empty shell post-flattening; deletion prevents orphaned structures without loss of data.

orchestration/00-ORCHESTRATION/state/  
Decision: Script deletes after archiving logs to agents/orchestration-legacy/.  
Rationale: Near-empty with only logs; preserve logs in legacy but remove shell for clean taxonomy.

## Edge Case 4: Root-Level Constitutional Files

AGENTS.md  
Decision: Retain at root/agents.md  
Rationale: Constitutional source of truth demands maximum accessibility, overriding taxonomic moves.

CLAUDE.md  
Decision: Retain at root/claude.md  
Rationale: Generated config from AGENTS.md inherits root-level priority for agent readability.

GEMINI.md  
Decision: Retain at root/gemini.md  
Rationale: Generated config parallels CLAUDE.md, maintaining root accessibility.

Makefile  
Decision: Retain at root/makefile  
Rationale: Build orchestration is repo-wide entry point, best at root for universal access.

README.md  
Decision: Retain at root/readme.md  
Rationale: Repo entry point serves all users, not confined to infrastructure or ontology.

.env.graphiti  
Decision: Retain at root/.env.graphiti  
Rationale: Environment config for Graphiti is system-wide, prioritizing root-level visibility.

## Edge Case 5: Ascertescence Sequential Numbering

Decision: Script skips ascertescence/ entirely, no moves or renames.  
Rationale: Chronological ledger organization already optimal; restructuring risks breaking sequential integrity.

## Edge Case 6: ENGINE- Subtype Ambiguity

ENGINE-REF-ROSETTA*  
Decision: Confirm to ontology/rosetta/  
Rationale: Rosetta Stone as reference for conceptual mappings embodies ontological alignment tools.

ENGINE-REF-AUDIZER*  
Decision: Change to infrastructure/cli/audizer-ref/  
Rationale: Tool reference for usage instructions fits CLI infrastructure over general skills.

ENGINE-REF-FLEET*  
Decision: Change to agents/coordination/fleet-ref/  
Rationale: Fleet handbook as operational policy governs agent interactions, suiting coordination.

ENGINE-CAP-*  
Decision: Change to consciousness/capabilities/  
Rationale: CAP likely denotes capabilities within consciousness framework, refining Pass 2's placement.

ENGINE-IIC-*  
Decision: Confirm to ontology/  
Rationale: IIC (possibly Integrated Inference Chains) supports ontological structures through reasoning models.

ENGINE-SURVEY-*  
Decision: Confirm to sovereignty/  
Rationale: Surveys assessing system or agent states align with sovereignty's oversight functions.

ENGINE-WF-*  
Decision: Change to agents/coordination/workflows/  
Rationale: WF as workflows better coordinates agent operations than feedcraft's data ingestion focus.

## Edge Case 7: Canon Internal Structure

Decision: Script excludes canon/ and canon/sn/ from walk loop entirely.  
Rationale: Protected canon requires Sovereign approval for changes; skipping preserves integrity.