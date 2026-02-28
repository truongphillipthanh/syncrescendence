import csv
import json
import os
import re
from collections import Counter, defaultdict


ROOT = "/Users/system/syncrescendence/corpus"
OUT_PATH = os.path.join(ROOT, "CLUSTER-MAP-ADJUDICATOR.tsv")
START = 4001
END = 8000


ALLOWED_TOPICS = {
    "claude-code",
    "openclaw",
    "codex",
    "gemini",
    "chatgpt",
    "cursor",
    "other-ai-tool",
    "ai-agents",
    "ai-coding",
    "prompt-engineering",
    "ai-memory",
    "ai-safety",
    "ai-models",
    "ai-business",
    "mcp",
    "ai-video",
    "ai-image",
    "ai-general",
    "geopolitics-us-china",
    "geopolitics-iran",
    "geopolitics-russia",
    "geopolitics-grand-strategy",
    "geopolitics-other",
    "economics-macro",
    "economics-investing",
    "economics-startups",
    "physics-cosmology",
    "biology-evolution",
    "biology-neuroscience",
    "philosophy-consciousness",
    "philosophy-epistemology",
    "history",
    "self-improvement",
    "content-creation",
    "design",
    "infrastructure",
    "software-engineering",
    "sn-handoff",
    "sn-task",
    "sn-confirm",
    "sn-result",
    "sn-prompt",
    "sn-certescence",
    "sn-config",
    "sn-script",
    "sn-watchdog",
    "sn-canon",
    "sn-rosetta",
    "sn-system-prompt",
    "sn-architecture",
    "sn-pipeline",
    "sn-atom",
    "sn-other",
}


INTERNAL_EXACT = {
    "04471.md": ("sn-pipeline", "", "Data quality fixes across SOURCE frontmatter and metadata"),
    "04472.md": ("sn-pipeline", "", "Final verification census for the Source Anneal corpus"),
    "04473.md": ("sn-architecture", "", "Operating handbook for the Syncrescendence constellation cockpit"),
    "04474.md": ("sn-pipeline", "sn-config", "Canonical frontmatter template for processed source files"),
    "04475.md": ("sn-system-prompt", "ai-agents", "Function capability index for model-facing agent workflows"),
    "04476.xml": ("prompt-engineering", "sn-system-prompt", "Prompt for extracting and consolidating insights across document versions"),
    "04477.xml": ("prompt-engineering", "", "Prompt for synthesis and unification of discrete materials"),
    "04478.xml": ("prompt-engineering", "", "Prompt for high-fidelity semantic amplification of source text"),
    "04479.xml": ("sn-system-prompt", "prompt-engineering", "Claude Projects metaprompt for comprehensive artifact annealment"),
    "04480.md": ("prompt-engineering", "", "Minimal prompt for converting text into TTS-optimized audio scripts"),
    "04481.md": ("prompt-engineering", "", "System identity and rules for TTS-friendly transcription output"),
    "04482.md": ("prompt-engineering", "", "Comprehensive reference for TTS transcription edge cases and fidelity rules"),
    "04483.xml": ("sn-pipeline", "prompt-engineering", "Workflow prompt for archiving Medium articles into markdown"),
    "04484.xml": ("sn-pipeline", "prompt-engineering", "Workflow prompt for archiving general web pages into markdown"),
    "04485.xml": ("sn-pipeline", "prompt-engineering", "Workflow prompt for archiving X long-form articles"),
    "04486.xml": ("sn-pipeline", "prompt-engineering", "Workflow prompt for archiving dense X threads"),
    "04487.xml": ("prompt-engineering", "", "Prompt for semantically preserving and coalescing multiple iterations"),
    "04488.xml": ("prompt-engineering", "sn-system-prompt", "Claude prompt compilation and optimization template"),
    "04489.xml": ("prompt-engineering", "sn-pipeline", "Metaprompt for canon identification and artifact consolidation"),
    "04490.xml": ("prompt-engineering", "sn-system-prompt", "Claude Projects prompt optimization from existing attachments"),
    "04491.xml": ("prompt-engineering", "ai-models", "Prompt for synthesizing outputs from multiple frontier AI models"),
    "04492.md": ("prompt-engineering", "", "Prompt for integrating disparate source materials into unified output"),
    "04493.md": ("prompt-engineering", "", "Prompt for improving listenability while preserving source meaning"),
    "04494.xml": ("prompt-engineering", "self-improvement", "Prompt for high-intensity cognitive offload and structured thinking"),
    "04495.xml": ("prompt-engineering", "", "Claude-oriented prompt optimization and intent interpretation framework"),
    "04496.xml": ("prompt-engineering", "", "Prompt for building foundation-first primers on unfamiliar topics"),
    "04497.md": ("prompt-engineering", "", "Prompt for improving readability while preserving source meaning"),
    "04498.xml": ("prompt-engineering", "philosophy-epistemology", "Prompt for philosophical transformation of concepts through staged reimagining"),
    "04499.xml": ("sn-pipeline", "prompt-engineering", "Prompt for transforming panel transcripts into coherent narratives"),
    "04500.xml": ("sn-pipeline", "prompt-engineering", "Prompt for transforming YouTube transcripts into readable articles"),
    "04501.xml": ("sn-pipeline", "prompt-engineering", "Prompt for transforming interviews and podcasts into cleaned narratives"),
    "04502.xml": ("prompt-engineering", "sn-system-prompt", "Claude translation prompt with adaptive versioning"),
    "04503.md": ("sn-result", "software-engineering", "Gate review for Agendizer phase 0 foundation work"),
    "04504.md": ("sn-result", "software-engineering", "Gate review for Agendizer phase 1 interpretation work"),
    "04505.md": ("sn-result", "software-engineering", "Gate review for Agendizer phase 2 navigation work"),
    "04506.md": ("sn-result", "software-engineering", "Gate review for Agendizer phase 3 ledger work"),
    "04507.md": ("sn-result", "software-engineering", "Gate review for Agendizer phase 4 graph connectivity work"),
    "04508.md": ("sn-result", "software-engineering", "Gate review for Agendizer phase 5 dispatch work"),
    "04509.md": ("sn-result", "software-engineering", "Gate review for Agendizer phase 6 polish work"),
    "04510.md": ("gemini", "sn-config", "Gemini CLI extensions appended into the agent instruction set"),
    "04511.md": ("gemini", "sn-script", "Runbook for the Gemini refinement automation script"),
    "04512.md": ("other-ai-tool", "sn-system-prompt", "Grok CLI extension prompt and behavior rules"),
    "04513.md": ("mcp", "claude-code", "Guide for authenticating MCP servers for Claude Code"),
    "04514.md": ("sn-handoff", "", "Session handoff summarizing source anneal completion and next architecture work"),
    "04515.md": ("sn-handoff", "", "Handoff for continuing live ledger and scaffold elucidation work"),
    "04516.md": ("sn-handoff", "", "Unified commander handoff with pre-made execution plan"),
    "04517.md": ("sn-handoff", "", "Commander Council 26 terminal handoff for ascertescence protocol work"),
    "04518.md": ("sn-handoff", "", "Commander Council 26 auto-compaction handoff"),
    "04519.md": ("sn-handoff", "", "Commander Council 27 auto-compaction handoff"),
    "04520.md": ("sn-handoff", "", "Commander Council 27 terminal handoff summarizing completed builds"),
    "04521.md": ("sn-handoff", "", "CC28 session terminal handoff covering siege progress"),
    "04522.md": ("sn-handoff", "", "Commander Council 29 auto-compaction handoff"),
    "04523.md": ("sn-handoff", "", "Second Commander Council 29 auto-compaction handoff"),
    "04524.md": ("sn-handoff", "sn-canon", "Commander Council 29 terminal handoff and constitutional synthesis"),
    "04525.md": ("sn-handoff", "sn-canon", "Emergency-mode handoff carrying sovereign directive and operating constraints"),
    "04526.md": ("sn-handoff", "sn-canon", "Emergency-mode culmination handoff with verbatim sovereign directive"),
    "04527.md": ("sn-canon", "sn-handoff", "Standalone emergency sovereign directive to propagate across outputs"),
    "04528.md": ("sn-handoff", "", "Commander Council 32 auto-compaction handoff"),
    "04529.md": ("sn-canon", "sn-handoff", "Emergency sovereign directive with updated progress markers"),
    "04530.md": ("sn-canon", "sn-handoff", "Emergency sovereign directive with gated atom promotion status"),
    "04531.md": ("ai-models", "sn-canon", "Frontier model behavioral profiles and triangulation playbook"),
    "04532.md": ("sn-canon", "sn-handoff", "Emergency sovereign directive for persistent operational framing"),
    "04533.md": ("sn-canon", "sn-handoff", "Emergency sovereign directive for persistent operational framing"),
    "04534.md": ("sn-handoff", "", "Commander Council 33 session handoff"),
    "04535.md": ("sn-handoff", "", "Commander Council 34 session handoff"),
    "04536.md": ("sn-handoff", "", "Commander Council 35 session handoff"),
    "04537.md": ("sn-handoff", "", "Commander Council 36 session handoff"),
    "04538.md": ("sn-handoff", "", "Commander Council 37 session handoff"),
    "04539.md": ("sn-handoff", "", "Commander Council 38 session handoff"),
    "04540.md": ("sn-handoff", "", "Commander Council 39 session handoff"),
    "04541.md": ("sn-handoff", "", "Commander Council 40 session handoff"),
    "04542.md": ("sn-handoff", "", "Commander Council 41 session handoff"),
    "04543.md": ("sn-handoff", "", "Commander Council 42 session handoff"),
    "04544.md": ("sn-handoff", "", "Commander Council 44 session handoff"),
    "04545.md": ("sn-handoff", "sn-architecture", "Session handoff for deep architectural audit"),
    "04546.md": ("sn-handoff", "sn-pipeline", "Session handoff for DC-208 pipeline execution"),
    "04547.md": ("sn-handoff", "sn-pipeline", "Session handoff after mining pipeline engineering completion"),
    "04548.md": ("sn-handoff", "", "Additional Commander Council 32 auto-compaction handoff"),
    "04549.md": ("sn-handoff", "sn-script", "Session terminal handoff for phases 3-5 tooling completion"),
    "04550.md": ("sn-canon", "", "Heritage map tracing conceptual lineage across canon ranges"),
    "04551.md": ("sn-canon", "", "Second part of the heritage map across canon clusters"),
    "04552.md": ("sn-canon", "", "Merged heritage map of canon concepts and their lineage"),
    "04553.md": ("sn-config", "sn-architecture", "Configuration for the Acumen identity-intelligence complex"),
    "04554.md": ("sn-config", "sn-architecture", "Configuration for the Coherence identity-intelligence complex"),
    "04555.md": ("sn-config", "sn-architecture", "Configuration for the Efficacy identity-intelligence complex"),
    "04556.md": ("sn-config", "sn-architecture", "Configuration for the Mastery identity-intelligence complex"),
    "04557.md": ("sn-config", "sn-architecture", "Configuration for the Transcendence identity-intelligence complex"),
    "04558.md": ("sn-architecture", "sn-config", "Protocols for communication across the IIC constellation"),
    "04559.md": ("infrastructure", "sn-architecture", "Implementation plan for bidirectional SSH between constellation machines"),
    "04560.md": ("sn-task", "sn-architecture", "Normalized implementation backlog ready for Linear execution"),
    "04561.md": ("sn-task", "sn-architecture", "Implementation map linking canon directives to deliverables"),
    "04562.md": ("sn-pipeline", "", "Auto-generated source index grouped by creator"),
    "04563.md": ("sn-pipeline", "", "Auto-generated source index grouped by platform"),
    "04564.md": ("sn-pipeline", "", "Auto-generated source index grouped by signal tier"),
    "04565.md": ("sn-pipeline", "", "Auto-generated source index grouped by teleology"),
    "04566.md": ("sn-pipeline", "", "Auto-generated source index grouped by topic"),
    "04567.md": ("sn-pipeline", "", "Auto-generated source index grouped by transcript status"),
    "04568.md": ("sn-pipeline", "", "Auto-generated source index ordered chronologically"),
    "04569.md": ("sn-pipeline", "", "Auto-generated source index grouped by NotebookLM category"),
    "04570.md": ("sn-handoff", "sn-result", "Siege index summarizing prompts and results from CC28"),
    "04571.md": ("sn-handoff", "sn-result", "Index of triangulation response files awaiting metabolization"),
    "04572.md": ("sn-canon", "sn-handoff", "Emergency sovereign directive for all downstream outputs"),
    "04573.md": ("sn-architecture", "sn-config", "Audit of incumbent SaaS integrations across the workspace"),
    "04574.md": ("sn-architecture", "", "Constellation routing rules and cross-machine handoff bridge"),
    "04575.md": ("sn-architecture", "software-engineering", "Analysis of tooling conflicts and architectural overlaps"),
    "04576.md": ("sn-rosetta", "sn-canon", "Forensic reconciliation of drift in the clarescence lens system"),
    "04577.lock": ("sn-watchdog", "", "Lockfile for a background coordination process"),
    "04578.lock": ("sn-watchdog", "", "Lockfile for a background coordination process"),
    "04579.lock": ("sn-watchdog", "", "Lockfile for a background coordination process"),
    "04580.lock": ("sn-watchdog", "", "Lockfile for a background coordination process"),
    "04581.md": ("sn-pipeline", "", "Manifest of sources staged for NotebookLM"),
    "04582.md": ("claude-code", "prompt-engineering", "Mechanics note on context compaction and token pressure"),
    "04583.md": ("prompt-engineering", "ai-models", "Mechanics note on triggering extended reasoning modes across models"),
    "04584.md": ("infrastructure", "ai-agents", "Mechanics note on git worktree isolation for parallel agent work"),
    "04585.md": ("claude-code", "sn-script", "Mechanics note on Claude Code headless mode automation"),
    "04586.md": ("claude-code", "ai-safety", "Mechanics note on hook lifecycle automation and guardrails"),
    "04587.md": ("mcp", "sn-architecture", "Mechanics note on MCP server architecture and patterns"),
    "04588.md": ("prompt-engineering", "", "Mechanics note on prompt engineering patterns"),
    "04589.md": ("claude-code", "sn-architecture", "Mechanics note on the skill system architecture"),
    "04590.md": ("sn-pipeline", "sn-architecture", "Blueprint for the source anneal ingestion and enrichment pipeline"),
    "04591.md": ("claude-code", "ai-agents", "Mechanics note on sub-agent delegation and isolated contexts"),
    "04592.md": ("claude-code", "ai-agents", "Mechanics note on the task orchestration system"),
    "04593.md": ("sn-pipeline", "", "Superseded research on YouTube ingestion pipeline architecture"),
    "04594.md": ("sn-canon", "sn-handoff", "Emergency sovereign directive for all downstream outputs"),
    "04595.md": ("content-creation", "self-improvement", "Framework for developing auteur-level personal content style"),
    "04596.md": ("sn-pipeline", "", "Research on architecture for a YouTube ingestion pipeline"),
    "04597.md": ("sn-pipeline", "", "Operation record for the Great Source Anneal corpus unification"),
    "04598.md": ("sn-result", "sn-pipeline", "Autofix log for data gap repairs across source files"),
    "04599.md": ("sn-pipeline", "", "Catalog tracking X bookmark transcription completion"),
    "04600.md": ("sn-pipeline", "", "Census report for pool A research files"),
    "04601.csv": ("sn-pipeline", "", "CSV inventory of pool A research files and metadata"),
    "04602.md": ("sn-pipeline", "", "Census report for pool B source files"),
    "04603.csv": ("sn-pipeline", "", "CSV inventory of pool B files and source flags"),
    "04604.md": ("sn-pipeline", "", "Census report for pool C NotebookLM source files"),
    "04605.csv": ("sn-pipeline", "", "CSV inventory of NotebookLM pool C source files"),
    "04606.csv": ("sn-pipeline", "", "CSV classification of sources and suspected duplicates across pools"),
    "04607.md": ("sn-pipeline", "", "Unified census report across all source pools"),
    "04608.md": ("sn-pipeline", "", "Data gaps quality gate report for SOURCE frontmatter"),
    "04609.md": ("sn-pipeline", "sn-result", "Deletion log for deduplication pass of the Source Anneal"),
    "04610.csv": ("sn-pipeline", "", "Duplicate cluster manifest across source pools"),
    "04611.md": ("sn-pipeline", "", "Deduplication manifest for the Source Anneal"),
    "04612.jsonl": ("sn-atom", "sn-pipeline", "Clustered atom records with representative previews"),
    "04613.md": ("sn-atom", "", "Summary of atom clustering results and score bands"),
    "04614.jsonl": ("sn-atom", "", "Atom scoring records with cluster assignments"),
    "04615.jsonl": ("sn-atom", "", "Atom scoring breakdowns with component contributions"),
    "04616.jsonl": ("sn-pipeline", "sn-atom", "Batch extraction status records for source atomization"),
    "04617.json": ("sn-pipeline", "", "Batch plan for processing source atom extraction"),
    "04618.md": ("sn-pipeline", "sn-atom", "Dynamic batch report for atom extraction throughput"),
    "04619.jsonl": ("sn-atom", "", "Atoms annotated with cluster labels and terms"),
    "04620.md": ("sn-atom", "", "Summary of cluster analysis across extracted atoms"),
    "04621.md": ("sn-atom", "sn-result", "Quality gate results across extracted atoms"),
    "04622.jsonl": ("sn-atom", "", "Per-atom quality and consistency metrics"),
    "04623.csv": ("sn-pipeline", "", "Master registry of sources with metadata, categories, and synopses"),
    "04624.json": ("sn-pipeline", "", "Parsed metadata dictionary for source files"),
    "04625.json": ("sn-pipeline", "", "Source graph data with nodes and edges"),
    "04626.mmd": ("sn-pipeline", "", "Mermaid graph of source relationships"),
    "04627.json": ("sn-pipeline", "", "Ranked source records with scoring outputs"),
    "04628.md": ("sn-pipeline", "", "Gap-fill report for frontmatter classification fields"),
    "04629.md": ("sn-pipeline", "", "Remainder enrichment report for source metadata"),
    "04630.md": ("sn-pipeline", "", "Batch enrichment report across SOURCE files"),
}


TOPIC_PATTERNS = {
    "claude-code": [
        (r"\bclaude code\b", 10),
        (r"\bclaude\.md\b", 8),
        (r"\bclaude cowork\b", 6),
        (r"\bopus 4\.6\b", 3),
    ],
    "openclaw": [
        (r"\bopenclaw\b", 10),
        (r"\bclawdbot\b", 10),
        (r"\bclawhub\b", 6),
        (r"\bmoltbot\b", 6),
        (r"\bmoltbook\b", 6),
        (r"\bclawd\b", 5),
    ],
    "codex": [
        (r"\bcodex\b", 10),
        (r"\bgpt-5(?:\.\d+)?-codex\b", 8),
        (r"\bcodex cli\b", 8),
    ],
    "gemini": [
        (r"\bgemini\b", 8),
        (r"\bantigravity\b", 5),
        (r"\bdeepmind\b", 3),
        (r"\bdemis\b", 3),
    ],
    "chatgpt": [
        (r"\bchatgpt\b", 10),
        (r"\bgpt-4o\b", 6),
        (r"\bgpt-4\b", 4),
    ],
    "cursor": [
        (r"\bcursor\b", 10),
    ],
    "other-ai-tool": [
        (r"\bdevin\b", 8),
        (r"\bmanus\b", 8),
        (r"\bqmd\b", 8),
        (r"\bopeneditor\b", 8),
        (r"\blovable\b", 8),
        (r"\bv0\b", 8),
        (r"\bbolt\.new\b", 8),
        (r"\breplit agent\b", 8),
        (r"\bwindsurf\b", 8),
        (r"\bnotebooklm\b", 7),
        (r"\bgrok\b", 7),
        (r"\baihero\b", 7),
        (r"\bagno\b", 7),
        (r"\bsuperwhisper\b", 7),
        (r"\bmidjourney\b", 7),
        (r"\bvoice cloning\b", 8),
        (r"\bvoice synthesis\b", 8),
        (r"\belevenlabs\b", 8),
        (r"\bvoicebox\b", 8),
    ],
    "ai-agents": [
        (r"\bai agents?\b", 7),
        (r"\bagentic\b", 7),
        (r"\bmulti-agent\b", 9),
        (r"\bsubagents?\b", 8),
        (r"\bsub-agent\b", 8),
        (r"\bagents?\b", 2),
        (r"\borchestration\b", 6),
        (r"\bmission control\b", 6),
        (r"\bfleet of ai agents\b", 8),
        (r"\bautonomous agent", 7),
    ],
    "ai-coding": [
        (r"\bai engineering\b", 8),
        (r"\bai engineer\b", 7),
        (r"\bai-assisted coding\b", 8),
        (r"\bvibe coding\b", 8),
        (r"\bdeveloper tools?\b", 5),
        (r"\bcoding workflow\b", 6),
        (r"\bautonomous coding\b", 7),
        (r"\bcode review\b", 5),
        (r"\bdebugging\b", 5),
        (r"\btesting\b", 5),
        (r"\bdeployment\b", 5),
        (r"\btoken management\b", 4),
        (r"\bsoftware development\b", 6),
        (r"\bgithub pushes?\b", 5),
        (r"\bpr reviews?\b", 5),
        (r"\bship things?\b", 5),
        (r"\bengineers?\b", 2),
    ],
    "prompt-engineering": [
        (r"\bprompt engineering\b", 10),
        (r"\bprompt design\b", 8),
        (r"\bsystem prompt\b", 8),
        (r"\bmetaprompt\b", 7),
        (r"\bprompt optimization\b", 8),
        (r"\bcontext engineering\b", 7),
        (r"\bprompting\b", 6),
        (r"\bprompt library\b", 9),
        (r"\bthousands of prompts\b", 8),
    ],
    "ai-memory": [
        (r"\brag\b", 10),
        (r"\bvector stores?\b", 8),
        (r"\bembeddings?\b", 8),
        (r"\bpersistent memory\b", 8),
        (r"\bmemory management\b", 7),
        (r"\bmemory\b", 4),
        (r"\bobsidian\b", 6),
        (r"\bhybrid search\b", 6),
    ],
    "ai-safety": [
        (r"\bai safety\b", 10),
        (r"\balignment\b", 8),
        (r"\bguardrails?\b", 8),
        (r"\bred teaming\b", 8),
        (r"\bjailbreak\b", 8),
        (r"\bai risks?\b", 7),
        (r"\bgovernance\b", 5),
        (r"\bunsafe\b", 5),
    ],
    "ai-models": [
        (r"\bfrontier model", 8),
        (r"\bbenchmarks?\b", 7),
        (r"\bscaling\b", 6),
        (r"\bmodel comparisons?\b", 8),
        (r"\bjagged intelligence\b", 8),
        (r"\bagi\b", 5),
        (r"\breasoning\b", 4),
        (r"\bwhich ai to use\b", 7),
        (r"\bstate of ai\b", 6),
        (r"\bmodel\b", 2),
    ],
    "ai-business": [
        (r"\bvaluation\b", 8),
        (r"\brun-rate\b", 8),
        (r"\bipo\b", 8),
        (r"\bpricing\b", 7),
        (r"\bcosts?\b", 6),
        (r"\btokens per engineer\b", 8),
        (r"\bmarket\b", 5),
        (r"\bcompany\b", 3),
        (r"\bstartup\b", 5),
        (r"\beconomics\b", 5),
        (r"\blabor\b", 5),
        (r"\bjob description\b", 7),
        (r"\bknowledge work\b", 6),
        (r"\bcontext layer\b", 6),
        (r"\bfinancial analysis\b", 6),
        (r"\bmarket dynamics\b", 7),
        (r"\bces\b", 5),
        (r"\bnvidia\b", 5),
        (r"\bamd\b", 4),
        (r"\bproduct categories\b", 5),
        (r"\bsell-off\b", 7),
        (r"\bprice of ai\b", 7),
    ],
    "mcp": [
        (r"\bmodel context protocol\b", 10),
        (r"\bmcp\b", 8),
        (r"\bmcp servers?\b", 9),
        (r"\bfunction calling\b", 6),
        (r"\btool use\b", 5),
    ],
    "ai-video": [
        (r"\bai video\b", 9),
        (r"\bvideo generation\b", 10),
        (r"\bseedance\b", 8),
        (r"\bsora\b", 8),
        (r"\brunway\b", 7),
        (r"\bpika\b", 7),
        (r"\bvfx\b", 7),
    ],
    "ai-image": [
        (r"\bimage generation\b", 10),
        (r"\bstable diffusion\b", 8),
        (r"\bdall-e\b", 8),
        (r"\bmidjourney\b", 8),
        (r"\bflux\b", 7),
    ],
    "geopolitics-us-china": [
        (r"\bus[- ]china\b", 10),
        (r"\btaiwan\b", 7),
        (r"\bxi jinping\b", 8),
        (r"\bsemiconductor ban\b", 8),
        (r"\bchina\b", 3),
    ],
    "geopolitics-iran": [
        (r"\biran\b", 10),
        (r"\bgaza\b", 8),
        (r"\bpalestin", 8),
        (r"\bhezbollah\b", 8),
        (r"\bhamas\b", 8),
        (r"\bisrael\b", 5),
        (r"\bmiddle east\b", 6),
    ],
    "geopolitics-russia": [
        (r"\brussia\b", 10),
        (r"\bukraine\b", 10),
        (r"\bputin\b", 8),
        (r"\bkyiv\b", 8),
        (r"\bnato\b", 4),
    ],
    "geopolitics-grand-strategy": [
        (r"\bgrand strategy\b", 10),
        (r"\bworld order\b", 8),
        (r"\bhegemony\b", 7),
        (r"\bmilitary theory\b", 8),
        (r"\bgeopolitics\b", 5),
    ],
    "geopolitics-other": [
        (r"\bgeopolitical\b", 7),
        (r"\bindia\b", 4),
        (r"\beurope\b", 4),
        (r"\bafrica\b", 4),
        (r"\bwar\b", 4),
    ],
    "economics-macro": [
        (r"\binflation\b", 9),
        (r"\binterest rates?\b", 8),
        (r"\bfederal reserve\b", 9),
        (r"\bmonetary policy\b", 9),
        (r"\bgdp\b", 6),
        (r"\bmacro(?:economics)?\b", 8),
    ],
    "economics-investing": [
        (r"\binvesting\b", 10),
        (r"\bportfolio\b", 8),
        (r"\btrading\b", 8),
        (r"\bstocks?\b", 7),
        (r"\bequities\b", 7),
        (r"\bbonds?\b", 7),
    ],
    "economics-startups": [
        (r"\bventure capital\b", 10),
        (r"\bentrepreneurship\b", 9),
        (r"\bseries a\b", 8),
        (r"\bseed funding\b", 8),
        (r"\bstartup\b", 7),
        (r"\bceo\b", 4),
    ],
    "physics-cosmology": [
        (r"\bquantum\b", 9),
        (r"\bphysics\b", 8),
        (r"\bcosmology\b", 10),
        (r"\bastrophysics\b", 10),
        (r"\brelativity\b", 8),
        (r"\bblack holes?\b", 8),
        (r"\bmath\b", 4),
    ],
    "biology-evolution": [
        (r"\bevolution\b", 9),
        (r"\bgenetics?\b", 9),
        (r"\bdarwin\b", 8),
        (r"\borganisms?\b", 8),
        (r"\bnatural selection\b", 10),
        (r"\blife\b", 3),
    ],
    "biology-neuroscience": [
        (r"\bneuroscience\b", 10),
        (r"\bneuron", 8),
        (r"\bcortex\b", 8),
        (r"\bcerebell", 8),
        (r"\bbrain\b", 6),
        (r"\bsynapse\b", 8),
    ],
    "philosophy-consciousness": [
        (r"\bconsciousness\b", 10),
        (r"\bqualia\b", 10),
        (r"\bpanpsych", 10),
        (r"\bintegrated information theory\b", 10),
        (r"\biit\b", 8),
        (r"\bphenomenology\b", 8),
        (r"\bvedanta\b", 8),
        (r"\bmetaphysics\b", 7),
        (r"\binterface theory of perception\b", 10),
    ],
    "philosophy-epistemology": [
        (r"\bepistemology\b", 10),
        (r"\bontology\b", 8),
        (r"\btruth\b", 6),
        (r"\bknowledge\b", 5),
        (r"\bworldview\b", 6),
        (r"\breasoning\b", 4),
        (r"\bparadigm\b", 5),
        (r"\bthinking\b", 4),
    ],
    "history": [
        (r"\bhistory\b", 10),
        (r"\bhistorical\b", 8),
        (r"\bancient\b", 8),
        (r"\bcivilization\b", 6),
        (r"\brome\b", 6),
        (r"\bworld war\b", 8),
    ],
    "self-improvement": [
        (r"\bfocus\b", 8),
        (r"\bdiscipline\b", 8),
        (r"\blearn\b", 6),
        (r"\bhabit\b", 8),
        (r"\bproductivity\b", 8),
        (r"\bcareer\b", 6),
        (r"\b100x engineer\b", 8),
        (r"\blearn anything\b", 8),
    ],
    "content-creation": [
        (r"\bcontent creation\b", 10),
        (r"\bcontent strategy\b", 10),
        (r"\bpersonal brand", 9),
        (r"\bcreator economy\b", 9),
        (r"\byoutube channel\b", 8),
        (r"\bbrand strategy\b", 8),
        (r"\bauteur\b", 8),
    ],
    "design": [
        (r"\bdesign systems?\b", 10),
        (r"\bui\/ux\b", 10),
        (r"\bfigma\b", 8),
        (r"\btypography\b", 8),
        (r"\bvisual design\b", 8),
        (r"\btaste\b", 5),
        (r"\bdesign\b", 4),
    ],
    "infrastructure": [
        (r"\bssh\b", 10),
        (r"\bnetworking\b", 9),
        (r"\blaunchd\b", 9),
        (r"\bserver\b", 5),
        (r"\bdevops\b", 8),
        (r"\bnginx\b", 8),
        (r"\bdocker\b", 8),
        (r"\bkubernetes\b", 8),
        (r"\baws\b", 6),
        (r"\bcloud\b", 5),
        (r"\bworktree\b", 6),
    ],
    "software-engineering": [
        (r"\bsoftware architecture\b", 9),
        (r"\bsystems design\b", 9),
        (r"\bapi design\b", 8),
        (r"\bdatabase schema\b", 8),
        (r"\brefactoring\b", 8),
        (r"\bswiftui\b", 6),
        (r"\bxcodebuild\b", 5),
        (r"\bprogramming\b", 5),
        (r"\bengineering\b", 3),
        (r"\bchips?\b", 2),
    ],
}


TOKEN_MAP = {
    "claude-code": ("claude-code", 8),
    "openclaw": ("openclaw", 8),
    "clawdbot": ("openclaw", 8),
    "codex": ("codex", 8),
    "gemini": ("gemini", 7),
    "chatgpt": ("chatgpt", 8),
    "cursor": ("cursor", 8),
    "mcp": ("mcp", 8),
    "ai-agents": ("ai-agents", 8),
    "agents-orchestration": ("ai-agents", 7),
    "agentic-development": ("ai-agents", 6),
    "ai-engineering": ("ai-coding", 8),
    "vibe-coding": ("ai-coding", 8),
    "ai-workflow": ("ai-coding", 6),
    "coding": ("ai-coding", 4),
    "developer-tools": ("ai-coding", 5),
    "cli-tools": ("ai-coding", 5),
    "testing": ("ai-coding", 4),
    "debugging": ("ai-coding", 4),
    "deployment": ("ai-coding", 4),
    "token-management": ("ai-coding", 4),
    "context-management": ("ai-memory", 6),
    "memory-management": ("ai-memory", 7),
    "rag": ("ai-memory", 8),
    "obsidian": ("ai-memory", 7),
    "prompt-engineering": ("prompt-engineering", 8),
    "prompting": ("prompt-engineering", 6),
    "extended-thinking": ("prompt-engineering", 5),
    "architecture": ("software-engineering", 3),
    "framework": ("philosophy-epistemology", 2),
    "philosophy": ("philosophy-epistemology", 6),
    "consciousness": ("philosophy-consciousness", 8),
    "brain": ("biology-neuroscience", 7),
    "history": ("history", 7),
    "design": ("design", 7),
    "content-creation": ("content-creation", 8),
    "career": ("self-improvement", 6),
    "education": ("self-improvement", 5),
    "economics": ("ai-business", 5),
    "business": ("ai-business", 5),
    "entrepreneurship": ("economics-startups", 7),
    "startup": ("economics-startups", 6),
    "video": ("ai-video", 6),
    "security": ("software-engineering", 3),
    "infrastructure": ("infrastructure", 7),
    "software": ("software-engineering", 3),
    "benchmarks": ("ai-models", 6),
    "models": ("ai-models", 5),
    "agi": ("ai-models", 5),
    "research": ("ai-general", 2),
    "economics-startups": ("economics-startups", 8),
}


CATEGORY_MAP = {
    "claude-code": ("claude-code", 8),
    "ai-agents": ("ai-agents", 8),
    "agents-orchestration": ("ai-agents", 8),
    "ai-engineering": ("ai-coding", 8),
    "coding-tools": ("ai-coding", 5),
    "vibe-coding": ("ai-coding", 8),
    "prompt-engineering": ("prompt-engineering", 8),
    "career-growth": ("self-improvement", 8),
    "philosophy-paradigm": ("philosophy-epistemology", 4),
    "ai-creative-media": ("ai-video", 6),
    "general": ("ai-general", 2),
}


TOOL_TOPICS = {
    "claude-code",
    "openclaw",
    "codex",
    "gemini",
    "chatgpt",
    "cursor",
    "other-ai-tool",
}


SPECIFIC_TOOL_WORDS = {
    "claude",
    "openclaw",
    "clawdbot",
    "codex",
    "gemini",
    "chatgpt",
    "cursor",
    "grok",
    "manus",
    "devin",
    "notebooklm",
    "voicebox",
}


def clean_space(text):
    text = text.replace("\t", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def read_text(path, limit=12000):
    with open(path, encoding="utf-8", errors="ignore") as handle:
        return handle.read(limit)


def load_target_files():
    files = []
    for name in os.listdir(ROOT):
        match = re.match(r"^(\d{5})\.", name)
        if not match:
            continue
        number = int(match.group(1))
        if START <= number <= END:
            files.append((number, name))
    files.sort()
    return files


def summarize_from_text(text, fallback):
    for raw in text.splitlines():
        line = clean_space(raw)
        if not line:
            continue
        if line.startswith("{") or line.startswith("["):
            continue
        if len(line) < 12:
            continue
        return line[:160]
    return fallback[:160]


def parse_json_line(line):
    try:
        return json.loads(line)
    except Exception:
        return None


def extract_source_id_from_obj(obj):
    if not isinstance(obj, dict):
        return ""
    for path in (
        ("source_id",),
        ("payload", "source_id"),
        ("provenance", "source_id"),
    ):
        cur = obj
        ok = True
        for key in path:
            if isinstance(cur, dict) and key in cur:
                cur = cur[key]
            else:
                ok = False
                break
        if ok and isinstance(cur, str):
            return cur
    return ""


def extract_content_from_obj(obj):
    if not isinstance(obj, dict):
        return ""
    for path in (
        ("content",),
        ("payload", "content"),
        ("representative_preview",),
        ("content_preview",),
        ("title",),
        ("name",),
    ):
        cur = obj
        ok = True
        for key in path:
            if isinstance(cur, dict) and key in cur:
                cur = cur[key]
            else:
                ok = False
                break
        if ok and isinstance(cur, str) and cur.strip():
            return cur
    return ""


def load_metadata():
    rows = {}
    with open(os.path.join(ROOT, "04623.csv"), encoding="utf-8", errors="ignore") as handle:
        for row in csv.DictReader(handle):
            rows[row["id"]] = row
    return rows


def build_source_groups(target_files, metadata_rows):
    groups = []
    pending = []

    def finalize_pending():
        nonlocal pending
        if not pending:
            return
        source_id = ""
        source_filenames = []
        snippets = []
        empty_files = []
        files = []
        for item in pending:
            files.append(item["name"])
            if item.get("source_id") and not source_id:
                source_id = item["source_id"]
            source_filenames.extend(item.get("source_filenames", []))
            snippets.extend(item.get("snippets", []))
            if item.get("empty"):
                empty_files.append(item["name"])
        group = {
            "group_id": files[-1],
            "source_id": source_id,
            "files": files,
            "snippets": snippets[:12],
            "source_filenames": source_filenames,
            "empty_files": empty_files,
        }
        if source_id and source_id in metadata_rows:
            group["metadata"] = metadata_rows[source_id]
        groups.append(group)
        pending = []

    for _, name in target_files:
        path = os.path.join(ROOT, name)
        if name in INTERNAL_EXACT:
            finalize_pending()
            continue

        if name.endswith(".md"):
            text = read_text(path, 12000)
            if "# Extraction:" not in text[:120]:
                finalize_pending()
                continue
            sid_match = re.search(r"# Extraction:\s*([^\n]+)", text)
            source_match = re.search(r"\*\*Source\*\*:\s*`([^`]+)`", text)
            quoted = [clean_space(snippet) for snippet in re.findall(r"^>\s*(.+)$", text, flags=re.MULTILINE)]
            pending.append(
                {
                    "name": name,
                    "source_id": sid_match.group(1).strip() if sid_match else "",
                    "source_filenames": [source_match.group(1).strip()] if source_match else [],
                    "snippets": quoted[:4] if quoted else [summarize_from_text(text, "Extraction summary")],
                    "empty": False,
                }
            )
            finalize_pending()
            continue

        if name.endswith(".jsonl"):
            if os.path.getsize(path) == 0:
                pending.append(
                    {
                        "name": name,
                        "source_id": "",
                        "source_filenames": [],
                        "snippets": [],
                        "empty": True,
                    }
                )
                continue

            with open(path, encoding="utf-8", errors="ignore") as handle:
                lines = []
                for _ in range(4):
                    line = handle.readline()
                    if not line:
                        break
                    lines.append(line.rstrip("\n"))

            sid = ""
            snippets = []
            for line in lines:
                obj = parse_json_line(line)
                if not obj:
                    continue
                sid = sid or extract_source_id_from_obj(obj)
                content = extract_content_from_obj(obj)
                if content:
                    snippets.append(clean_space(content))

            pending.append(
                {
                    "name": name,
                    "source_id": sid,
                    "source_filenames": [],
                    "snippets": snippets[:4],
                    "empty": False,
                }
            )

    finalize_pending()
    return groups


def add_score(scores, topic, amount):
    if topic in ALLOWED_TOPICS:
        scores[topic] += amount


def make_profile_text(profile, include_metadata):
    parts = []
    row = profile.get("metadata")
    if include_metadata and row:
        for field in ("title", "notebooklm_category", "topics", "synopsis", "creator", "filename"):
            value = row.get(field)
            if value:
                parts.append(value)
    parts.extend(profile.get("source_filenames", []))
    parts.extend(profile.get("snippets", [])[:8])
    return clean_space(" | ".join(parts))


def tokenize_keywords(text):
    text = text.lower()
    return {
        token
        for token in re.findall(r"[a-z0-9][a-z0-9\-\+\.]{2,}", text)
        if token not in {
            "the",
            "and",
            "for",
            "with",
            "that",
            "this",
            "from",
            "into",
            "your",
            "have",
            "will",
            "what",
            "when",
            "where",
            "about",
            "their",
            "there",
            "they",
            "just",
            "more",
            "than",
            "here",
            "over",
            "some",
            "like",
            "using",
            "used",
        }
    }


def metadata_is_trustworthy(profile):
    row = profile.get("metadata") or {}
    if not row:
        return False
    source_names = " ".join(profile.get("source_filenames", []))
    if row.get("filename") and source_names and row["filename"] in source_names:
        return True

    snippet_text = " ".join(profile.get("snippets", [])[:6])
    if not snippet_text:
        return bool(row.get("title"))

    metadata_text = " ".join(
        value for value in (row.get("title", ""), row.get("synopsis", ""), row.get("filename", "")) if value
    )
    snippet_tools = tokenize_keywords(snippet_text) & SPECIFIC_TOOL_WORDS
    metadata_tools = tokenize_keywords(metadata_text) & SPECIFIC_TOOL_WORDS
    if snippet_tools and metadata_tools and not (snippet_tools & metadata_tools):
        return False

    snippet_tokens = tokenize_keywords(snippet_text)
    title_tokens = tokenize_keywords(row.get("title", ""))
    synopsis_tokens = tokenize_keywords(row.get("synopsis", ""))
    filename_tokens = tokenize_keywords(row.get("filename", ""))

    if title_tokens and len(snippet_tokens & title_tokens) >= 2:
        return True
    if synopsis_tokens and len(snippet_tokens & synopsis_tokens) >= (5 if not row.get("title") else 3):
        return True
    if filename_tokens and len(snippet_tokens & filename_tokens) >= 2:
        return True
    return False


def score_source_profile(profile):
    trusted_metadata = metadata_is_trustworthy(profile)
    text = make_profile_text(profile, include_metadata=trusted_metadata)
    lower = text.lower()
    scores = Counter()
    notes = []

    row = profile.get("metadata") or {}
    if trusted_metadata:
        category = row.get("notebooklm_category", "").strip().lower()
        if category in CATEGORY_MAP:
            topic, weight = CATEGORY_MAP[category]
            add_score(scores, topic, weight)

        topic_tokens = [clean_space(tok.lower()) for tok in row.get("topics", "").split(";") if tok.strip()]
        for token in topic_tokens:
            if token in TOKEN_MAP:
                topic, weight = TOKEN_MAP[token]
                add_score(scores, topic, weight)
                notes.append(token)

    for topic, patterns in TOPIC_PATTERNS.items():
        for pattern, weight in patterns:
            matches = len(re.findall(pattern, lower))
            if matches:
                add_score(scores, topic, matches * weight)

    source_names = " ".join(profile.get("source_filenames", [])).lower()
    if source_names:
        for topic, patterns in TOPIC_PATTERNS.items():
            for pattern, weight in patterns:
                matches = len(re.findall(pattern, source_names))
                if matches:
                    add_score(scores, topic, matches * (weight + 2))

    if sum(scores[t] for t in TOOL_TOPICS) >= 12 and sum(scores[t] for t in ("ai-agents", "ai-coding", "prompt-engineering")) >= 8:
        for topic in ("ai-agents", "ai-coding", "prompt-engineering"):
            scores[topic] += 2

    if scores["philosophy-consciousness"] and scores["biology-neuroscience"]:
        if "brain" in lower or "neuron" in lower or "cerebell" in lower:
            scores["biology-neuroscience"] += 2
        if "qualia" in lower or "panpsych" in lower or "iit" in lower:
            scores["philosophy-consciousness"] += 3

    if scores["ai-business"] and ("pricing" in lower or "cost" in lower or "valuation" in lower):
        scores["ai-business"] += 3

    if scores["ai-models"] and ("benchmark" in lower or "frontier" in lower or "model" in lower):
        scores["ai-models"] += 2

    if scores["ai-video"] and "image" in lower:
        scores["ai-image"] += 2

    if scores["other-ai-tool"] and any(tag in lower for tag in ("openclaw", "claude code", "cursor", "codex", "gemini", "chatgpt")):
        scores["other-ai-tool"] -= 2

    if trusted_metadata and row.get("title"):
        title = row["title"].lower()
        if "state of ai" in title or "which ai to use" in title or "jagged" in title:
            scores["ai-models"] += 4
        if "workflow" in title or "setup" in title or "ship" in title:
            scores["ai-coding"] += 2
        if "cost" in title or "pricing" in title or "run-rate" in title:
            scores["ai-business"] += 3
        if "prompt library" in title:
            scores["prompt-engineering"] += 5
        if "voice" in title and ("clone" in title or "synthesis" in title):
            scores["other-ai-tool"] += 6

    if "prompt library" in lower:
        scores["prompt-engineering"] += 4
    if "knowledge work" in lower or "financial analysis" in lower:
        scores["ai-business"] += 3
    if "excel" in lower or "powerpoint" in lower:
        scores["ai-coding"] += 2
    if "ces" in lower and ("nvidia" in lower or "samsung" in lower or "amd" in lower or "amazon" in lower):
        scores["ai-business"] += 4
        scores["ai-models"] += 2
    if "voice cloning" in lower or "voice synthesis" in lower:
        scores["other-ai-tool"] += 5

    if not scores:
        if "ai" in lower or "llm" in lower or "model" in lower or "agent" in lower:
            scores["ai-general"] = 1
        else:
            scores["philosophy-epistemology"] = 1

    ranked = [topic for topic, _ in scores.most_common() if scores[topic] > 0]
    primary = ranked[0]

    if primary in TOOL_TOPICS:
        non_tool = max((scores[t] for t in scores if t not in TOOL_TOPICS), default=0)
        if non_tool > scores[primary] * 1.45:
            primary = max(
                (t for t in scores if t not in TOOL_TOPICS),
                key=lambda t: scores[t],
            )

    secondary = ""
    for topic in ranked:
        if topic == primary:
            continue
        if scores[topic] >= max(5, int(scores[primary] * 0.35)):
            secondary = topic
            break

    summary = ""
    if trusted_metadata and row.get("title") and row.get("synopsis"):
        summary = clean_space(row["synopsis"])
    elif trusted_metadata and row.get("title"):
        summary = clean_space(row["title"])
    elif profile.get("snippets"):
        summary = clean_space(profile["snippets"][0])
    elif profile.get("source_filenames"):
        summary = clean_space(profile["source_filenames"][0])
    else:
        summary = profile["source_id"]

    return primary, secondary, summary[:180], scores


def classify_orphan_file(name, text):
    lower = text.lower()
    if name.endswith(".jsonl") and os.path.getsize(os.path.join(ROOT, name)) == 0:
        return "sn-other", "", "Empty JSONL artifact with no recoverable source metadata"
    if name.endswith(".jsonl") and "source_id" in lower:
        obj = parse_json_line(text.splitlines()[0]) if text.splitlines() else None
        content = extract_content_from_obj(obj) if obj else ""
        summary = clean_space(content or "Source-linked JSONL artifact")
        return "ai-general", "", summary[:180]
    if name.endswith(".xml"):
        return "prompt-engineering", "", summarize_from_text(text, "Prompt definition")
    if name.endswith(".csv") or name.endswith(".json") or name.endswith(".mmd"):
        return "sn-pipeline", "", summarize_from_text(text, "Pipeline artifact")
    if name.endswith(".lock"):
        return "sn-watchdog", "", "Lockfile for a background coordination process"
    return "sn-other", "", summarize_from_text(text, name)


def main():
    metadata_rows = load_metadata()
    target_files = load_target_files()
    groups = build_source_groups(target_files, metadata_rows)

    file_rows = []
    group_to_result = {}
    file_to_group = {}
    for group in groups:
        primary, secondary, summary, _scores = score_source_profile(group)
        group_to_result[group["group_id"]] = (primary, secondary, summary)
        for name in group["files"]:
            file_to_group[name] = group["group_id"]

    for _, name in target_files:
        if name in INTERNAL_EXACT:
            primary, secondary, summary = INTERNAL_EXACT[name]
            file_rows.append((name, primary, secondary, summary))
            continue

        group_id = file_to_group.get(name)
        if group_id and group_id in group_to_result:
            primary, secondary, summary = group_to_result[group_id]
            file_rows.append((name, primary, secondary, summary))
            continue

        text = read_text(os.path.join(ROOT, name), 8000) if os.path.getsize(os.path.join(ROOT, name)) else ""
        primary, secondary, summary = classify_orphan_file(name, text)
        file_rows.append((name, primary, secondary, summary))

    file_rows.sort(key=lambda row: int(row[0][:5]))

    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        for name, primary, secondary, summary in file_rows:
            if primary not in ALLOWED_TOPICS:
                raise ValueError(f"Invalid primary topic for {name}: {primary}")
            if secondary and secondary not in ALLOWED_TOPICS:
                raise ValueError(f"Invalid secondary topic for {name}: {secondary}")
            handle.write(
                f"{name}\t{primary}\t{secondary}\t{clean_space(summary)}\n"
            )


if __name__ == "__main__":
    main()
