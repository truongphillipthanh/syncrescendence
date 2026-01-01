#!/bin/bash
# rename_canon.sh - Execute nomenclature reform
# Generated: 2025-12-30
# Directive: DIRECTIVE-017
#
# WARNING: This script performs destructive file renames.
# Execute only after Principal approval and backup verification.
#
# Usage: ./rename_canon.sh [--dry-run]
#   --dry-run: Show what would be renamed without executing

set -e

DRY_RUN=false
if [[ "$1" == "--dry-run" ]]; then
    DRY_RUN=true
    echo "=== DRY RUN MODE - No files will be renamed ==="
fi

CANON_DIR="/Users/system/Desktop/syncrescendence/CANON"

rename_file() {
    local old="$1"
    local new="$2"

    if [[ "$DRY_RUN" == true ]]; then
        echo "WOULD RENAME:"
        echo "  FROM: $old"
        echo "  TO:   $new"
        echo ""
    else
        if [[ -f "$old" ]]; then
            mv "$old" "$new"
            echo "RENAMED: $(basename "$old") -> $(basename "$new")"
        else
            echo "WARNING: File not found: $old"
        fi
    fi
}

echo "=== Syncrescendence Nomenclature Reform ==="
echo "=== Postpositive Synaptic Naming System ==="
echo ""

# cosmos tier
echo "--- COSMOS TIER ---"
rename_file "$CANON_DIR/cosmos/CANON-00000-cosmos-SYNCRESCENDENT_SCHEMA.md" "$CANON_DIR/cosmos/CANON-00000-SCHEMA-cosmos.md"
rename_file "$CANON_DIR/cosmos/CANON-00001-cosmos-SYNCRESCENDENCE-v2_3.md" "$CANON_DIR/cosmos/CANON-00001-SYNCRESCENDENCE-cosmos.md"
rename_file "$CANON_DIR/cosmos/CANON-00002-cosmos-SYNCRESCENDENT_CORPUS-v2_3.md" "$CANON_DIR/cosmos/CANON-00002-CORPUS-cosmos.md"
rename_file "$CANON_DIR/cosmos/CANON-00003-cosmos-SYNCRESCENDENCE_EVALUATION-v2_3.md" "$CANON_DIR/cosmos/CANON-00003-EVALUATION-cosmos.md"
rename_file "$CANON_DIR/cosmos/CANON-00004-cosmos-SYNCRESCENDENT_RESOLUTIONS-v2_3.md" "$CANON_DIR/cosmos/CANON-00004-RESOLUTIONS-cosmos.md"
rename_file "$CANON_DIR/cosmos/CANON-00005-cosmos-SYNCRESCENDENT_STRATEGY-v2_3.md" "$CANON_DIR/cosmos/CANON-00005-STRATEGY-cosmos.md"
rename_file "$CANON_DIR/cosmos/CANON-00006-cosmos-SYNCRESCENDENT_OPERATIONS_v2_3.md" "$CANON_DIR/cosmos/CANON-00006-OPERATIONS-cosmos.md"
rename_file "$CANON_DIR/cosmos/CANON-00007-cosmos-ARTIFACT_PRODUCTION_PROTOCOL.md" "$CANON_DIR/cosmos/CANON-00007-ARTIFACT_PROTOCOL-cosmos.md"
rename_file "$CANON_DIR/cosmos/CANON-00008-cosmos-MODAL_SEQUENCE_ARCHITECTURE.md" "$CANON_DIR/cosmos/CANON-00008-MODAL_SEQUENCE-cosmos.md"
rename_file "$CANON_DIR/cosmos/CANON-00009-cosmos-SYNCRESCENDENT_QUICKSTART-v2_3.md" "$CANON_DIR/cosmos/CANON-00009-QUICKSTART-cosmos.md"
rename_file "$CANON_DIR/cosmos/CANON-00010-cosmos-CONTENT_PRODUCTION_PROTOCOL.md" "$CANON_DIR/cosmos/CANON-00010-CONTENT_PROTOCOL-cosmos.md"

# core tier
echo ""
echo "--- CORE TIER ---"
rename_file "$CANON_DIR/core/CANON-10000-core-SYNCRESCENDENT_CELESTIAL_BODY-v1_1.md" "$CANON_DIR/core/CANON-10000-CELESTIAL_BODY-core.md"
rename_file "$CANON_DIR/core/CANON-11000-core-SYNCRESCENDENT_FACETS.md" "$CANON_DIR/core/CANON-11000-FACETS-core.md"

# lattice tier
echo ""
echo "--- LATTICE TIER ---"
rename_file "$CANON_DIR/lattice/CANON-20000-lattice-COGNITIVE_PALACE.md" "$CANON_DIR/lattice/CANON-20000-PALACE-lattice.md"
rename_file "$CANON_DIR/lattice/CANON-21000-lattice-CHAIN_INTERDEPENDENCY_MATRIX-v1_0.md" "$CANON_DIR/lattice/CANON-21000-CHAIN_MATRIX-lattice.md"
rename_file "$CANON_DIR/lattice/CANON-21100-lattice-TRI_HELICAL_TIMELINE_VISUALIZATION-v1_0.md" "$CANON_DIR/lattice/CANON-21100-TRI_HELIX-lattice.md"
rename_file "$CANON_DIR/lattice/CANON-22000-lattice-INTERFERENCE_PATTERN-v2.2.md" "$CANON_DIR/lattice/CANON-22000-INTERFERENCE-lattice.md"
rename_file "$CANON_DIR/lattice/CANON-23000-lattice-LUNAR_NAVIGATION-V1.md" "$CANON_DIR/lattice/CANON-23000-LUNAR_NAV-lattice.md"
rename_file "$CANON_DIR/lattice/CANON-24000-lattice-PRIORITY-5-OMNI-QUALITY.md" "$CANON_DIR/lattice/CANON-24000-OMNI_QUALITY-lattice.md"
rename_file "$CANON_DIR/lattice/CANON-25000-lattice-MEMORY_ARCHITECTURE-v1_0.md" "$CANON_DIR/lattice/CANON-25000-MEMORY_ARCH-lattice.md"
rename_file "$CANON_DIR/lattice/CANON-25100-lattice-CONTEXT_TRANSITION_PROTOCOL-v1_1.md" "$CANON_DIR/lattice/CANON-25100-CONTEXT_TRANS-lattice.md"

# chains tier - INTELLIGENCE (30xxx)
echo ""
echo "--- INTELLIGENCE CHAIN (30xxx) ---"
rename_file "$CANON_DIR/chains/CANON-30000-chain-INTELLIGENCE-v1_1.md" "$CANON_DIR/chains/CANON-30000-INTELLIGENCE-chain.md"
rename_file "$CANON_DIR/chains/CANON-30100-chain-INTELLIGENCE-comet-ASA_MODEL.md" "$CANON_DIR/chains/CANON-30100-ASA-comet-INTELLIGENCE.md"
rename_file "$CANON_DIR/chains/CANON-30200-chain-INTELLIGENCE-comet-STRATEGIC_POSITIONING_SUPPLEMENT.md" "$CANON_DIR/chains/CANON-30200-POSITIONING-comet-INTELLIGENCE.md"
rename_file "$CANON_DIR/chains/CANON-30300-chain-INTELLIGENCE-comet-TECHNOLOGY_STACK_DATABASE.md" "$CANON_DIR/chains/CANON-30300-TECH_STACK-comet-INTELLIGENCE.md"
rename_file "$CANON_DIR/chains/CANON-30310-chain-INTELLIGENCE-comet-TECHNOLOGY_STACK_DATABASE-asteroid-COMPLETE_MIGRATION.md" "$CANON_DIR/chains/CANON-30310-MIGRATION-asteroid-TECH_STACK-comet-INTELLIGENCE.md"
rename_file "$CANON_DIR/chains/CANON-30320-chain-INTELLIGENCE-comet-TECHNOLOGY_STACK_DATABASE-asteroid-WORKFLOW-INTELLIGENCE_FRAMEWORK.md" "$CANON_DIR/chains/CANON-30320-WORKFLOW_INTEL-asteroid-TECH_STACK-comet-INTELLIGENCE.md"

# chains tier - INFORMATION (31xxx)
echo ""
echo "--- INFORMATION CHAIN (31xxx) ---"
rename_file "$CANON_DIR/chains/CANON-31000-chain-INFORMATION.md" "$CANON_DIR/chains/CANON-31000-INFORMATION-chain.md"
rename_file "$CANON_DIR/chains/CANON-31100-chain-INFORMATION-planetary-ACUMEN-v2_3.md" "$CANON_DIR/chains/CANON-31100-ACUMEN-planetary-INFORMATION.md"
rename_file "$CANON_DIR/chains/CANON-31110-chain-INFORMATION-planetary-ACUMEN-lunar-FEEDCRAFT.md" "$CANON_DIR/chains/CANON-31110-FEEDCRAFT-lunar-ACUMEN-planetary-INFORMATION.md"
rename_file "$CANON_DIR/chains/CANON-31115-chain-INFORMATION-planetary-ACUMEN-lunar-IIC_IMPLEMENTATION.md" "$CANON_DIR/chains/CANON-31115-IIC_IMPL-lunar-ACUMEN-planetary-INFORMATION.md"
rename_file "$CANON_DIR/chains/CANON-31120-chain-INFORMATION-planetary-ACUMEN-lunar-TONE_LIBRARY_ARCHITECTURE.md" "$CANON_DIR/chains/CANON-31120-TONE_LIBRARY-lunar-ACUMEN-planetary-INFORMATION.md"
rename_file "$CANON_DIR/chains/CANON-31121-chain-INFORMATION-planetary-ACUMEN-lunar-TONE_LIBRARY_ARCHITECTURE-satellite-TONE_LIBRARY_TAXONOMY.md" "$CANON_DIR/chains/CANON-31121-TONE_TAXONOMY-satellite-TONE_LIBRARY-lunar-ACUMEN-planetary-INFORMATION.md"
rename_file "$CANON_DIR/chains/CANON-31122-chain-INFORMATION-planetary-ACUMEN-lunar-TONE_LIBRARY_ARCHITECTURE-satellite-RHETORICAL_CALIBRATION.md" "$CANON_DIR/chains/CANON-31122-RHETORICAL-satellite-TONE_LIBRARY-lunar-ACUMEN-planetary-INFORMATION.md"
rename_file "$CANON_DIR/chains/CANON-31130-chain-INFORMATION-planetary-ACUMEN-lunar-SEVEN_LAYER_STACK-v1_0.md" "$CANON_DIR/chains/CANON-31130-SEVEN_LAYER-lunar-ACUMEN-planetary-INFORMATION.md"
rename_file "$CANON_DIR/chains/CANON-31140-chain-INFORMATION-planetary-ACUMEN-lunar-IIC_CONSTELLATION-v1_0.md" "$CANON_DIR/chains/CANON-31140-IIC-lunar-ACUMEN-planetary-INFORMATION.md"
rename_file "$CANON_DIR/chains/CANON-31141-chain-INFORMATION-planetary-ACUMEN-lunar-IIC_CONSTELLATION-satellite-FIVE_ACCOUNT_ARCHITECTURE-v1_0.md" "$CANON_DIR/chains/CANON-31141-FIVE_ACCOUNT-satellite-IIC-lunar-ACUMEN-planetary-INFORMATION.md"
rename_file "$CANON_DIR/chains/CANON-31142-chain-INFORMATION-planetary-ACUMEN-lunar-IIC_CONSTELLATION-satellite-PLATFORM_GRAMMAR-v1_0.md" "$CANON_DIR/chains/CANON-31142-PLATFORM_GRAMMAR-satellite-IIC-lunar-ACUMEN-planetary-INFORMATION.md"
rename_file "$CANON_DIR/chains/CANON-31143-chain-INFORMATION-planetary-ACUMEN-lunar-IIC_CONSTELLATION-satellite-FEED_CURATION-v1_0.md" "$CANON_DIR/chains/CANON-31143-FEED_CURATION-satellite-IIC-lunar-ACUMEN-planetary-INFORMATION.md"

# chains tier - INSIGHT (32xxx)
echo ""
echo "--- INSIGHT CHAIN (32xxx) ---"
rename_file "$CANON_DIR/chains/CANON-32000-chain-INSIGHT.md" "$CANON_DIR/chains/CANON-32000-INSIGHT-chain.md"
rename_file "$CANON_DIR/chains/CANON-32100-chain-INSIGHT-planetary-COHERENCE.md" "$CANON_DIR/chains/CANON-32100-COHERENCE-planetary-INSIGHT.md"
rename_file "$CANON_DIR/chains/CANON-32110-chain-INSIGHT-planetary-COHERENCE-lunar-SYSTEM-v2_2.md" "$CANON_DIR/chains/CANON-32110-COHERENCE_SYS-lunar-COHERENCE-planetary-INSIGHT.md"
rename_file "$CANON_DIR/chains/CANON-32120-chain-INSIGHT-planetary-COHERENCE-lunar-META_ANALYTICAL_FRAMEWORK-v1_0.md" "$CANON_DIR/chains/CANON-32120-META_ANALYSIS-lunar-COHERENCE-planetary-INSIGHT.md"

# chains tier - EXPERTISE (33xxx)
echo ""
echo "--- EXPERTISE CHAIN (33xxx) ---"
rename_file "$CANON_DIR/chains/CANON-33000-chain-EXPERTISE.md" "$CANON_DIR/chains/CANON-33000-EXPERTISE-chain.md"
rename_file "$CANON_DIR/chains/CANON-33100-chain-EXPERTISE-planetary-EFFICACY.md" "$CANON_DIR/chains/CANON-33100-EFFICACY-planetary-EXPERTISE.md"
rename_file "$CANON_DIR/chains/CANON-33110-chain-EXPERTISE-planetary-EFFICACY-lunar-BUSINESS_OPERATION_BACKBONE-v2_2.md" "$CANON_DIR/chains/CANON-33110-BIZ_BACKBONE-lunar-EFFICACY-planetary-EXPERTISE.md"
rename_file "$CANON_DIR/chains/CANON-33111-chain-EXPERTISE-planetary-EFFICACY-lunar-BUSINESS_OPERATION_BACKBONE-satellite-BUSINESS_OPERATIONS_v1_2_ENHANCEMENTS.md" "$CANON_DIR/chains/CANON-33111-BIZ_ENHANCE-satellite-BIZ_BACKBONE-lunar-EFFICACY-planetary-EXPERTISE.md"
rename_file "$CANON_DIR/chains/CANON-33112-chain-EXPERTISE-planetary-EFFICACY-lunar-BUSINESS_OPERATION_BACKBONE-satellite-REVENUE_MODEL_RECONCILIATION-v1_0.md" "$CANON_DIR/chains/CANON-33112-REVENUE_MODEL-satellite-BIZ_BACKBONE-lunar-EFFICACY-planetary-EXPERTISE.md"

# chains tier - KNOWLEDGE (34xxx)
echo ""
echo "--- KNOWLEDGE CHAIN (34xxx) ---"
rename_file "$CANON_DIR/chains/CANON-34000-chain-KNOWLEDGE.md" "$CANON_DIR/chains/CANON-34000-KNOWLEDGE-chain.md"
rename_file "$CANON_DIR/chains/CANON-34100-chain-KNOWLEDGE-planetary-MASTERY.md" "$CANON_DIR/chains/CANON-34100-MASTERY-planetary-KNOWLEDGE.md"
rename_file "$CANON_DIR/chains/CANON-34110-chain-KNOWLEDGE-planetary-MASTERY-lunar-CURRICULUM-v1_1.md" "$CANON_DIR/chains/CANON-34110-CURRICULUM-lunar-MASTERY-planetary-KNOWLEDGE.md"
rename_file "$CANON_DIR/chains/CANON-34120-chain-KNOWLEDGE-planetary-MASTERY-lunar-SYLLABUS-v1_1.md" "$CANON_DIR/chains/CANON-34120-SYLLABUS-lunar-MASTERY-planetary-KNOWLEDGE.md"

# chains tier - WISDOM (35xxx)
echo ""
echo "--- WISDOM CHAIN (35xxx) ---"
rename_file "$CANON_DIR/chains/CANON-35000-chain-WISDOM.md" "$CANON_DIR/chains/CANON-35000-WISDOM-chain.md"
rename_file "$CANON_DIR/chains/CANON-35100-chain-WISDOM-ring-TRANSCENDENCE.md" "$CANON_DIR/chains/CANON-35100-TRANSCENDENCE-ring-WISDOM.md"
rename_file "$CANON_DIR/chains/CANON-35110-chain-WISDOM-ring-TRANSCENDENCE-lunar-SYSTEM-v2_2.md" "$CANON_DIR/chains/CANON-35110-TRANS_SYSTEM-lunar-TRANSCENDENCE-ring-WISDOM.md"
rename_file "$CANON_DIR/chains/CANON-35120-chain-WISDOM-ring-TRANSCENDENCE-lunar-NEURODIVERGENT_PRACTICE_ADAPTATIONS-v1_0.md" "$CANON_DIR/chains/CANON-35120-NEURODIVERGENT-lunar-TRANSCENDENCE-ring-WISDOM.md"
rename_file "$CANON_DIR/chains/CANON-35200-chain-WISDOM-ring-TRANSCENDENCE-lunar-GAIAN_FIELD_NODE-v1_0.md" "$CANON_DIR/chains/CANON-35200-GAIAN_NODE-lunar-TRANSCENDENCE-ring-WISDOM.md"

# meta tier
echo ""
echo "--- META TIER ---"
rename_file "$CANON_DIR/CANON-99000-meta-HISTORICAL_ARCHIVE.md" "$CANON_DIR/CANON-99000-HISTORICAL-meta.md"

echo ""
echo "=== NOMENCLATURE REFORM COMPLETE ==="
echo ""

if [[ "$DRY_RUN" == true ]]; then
    echo "This was a DRY RUN. No files were actually renamed."
    echo "Run without --dry-run to execute the renames."
else
    echo "All files renamed. Next steps:"
    echo "1. Update cross-references in all documents"
    echo "2. Validate with: grep -rn 'CANON-[0-9]' CANON/"
    echo "3. Commit changes"
fi
