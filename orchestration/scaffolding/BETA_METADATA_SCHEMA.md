# BETA METADATA SCHEMA SPECIFICATION
## YAML Frontmatter Standard for Syncrescendence

**Generated**: 2025-12-30
**Agent**: Claude Opus 4.5 (Stream Beta)
**Directive**: DIRECTIVE-017 (Holistic Reconception)
**Status**: SPECIFICATION COMPLETE

---

## Executive Summary

Every document in the Syncrescendence corpus requires YAML frontmatter that:
1. Makes the document self-describing
2. Enables programmatic navigation
3. Supports manifest auto-generation
4. Preserves version history without filename changes

---

## Part I: Schema Definition

### Required Fields

```yaml
---
id: string              # Unique identifier (e.g., "CANON-31141")
name: string            # Human-readable name (e.g., "Five Account Architecture")
identity: string        # SCREAMING_CASE identifier (e.g., "FIVE_ACCOUNT")
tier: enum              # GENESIS | CANON | OPERATIONAL | QUEUE | EXEMPLA
type: enum              # cosmos | core | lattice | chain | planetary | lunar | satellite | comet | asteroid | ring | meta
version: string         # Semantic version (e.g., "2.0.0")
status: enum            # canonical | draft | deprecated
created: string         # ISO 8601 date (e.g., "2025-10-17")
updated: string         # ISO 8601 date (e.g., "2025-12-30")
---
```

### Conditional Fields (Chain Documents)

```yaml
chain: string           # INTELLIGENCE | INFORMATION | INSIGHT | EXPERTISE | KNOWLEDGE | WISDOM
parent: string | null   # Parent document ID (e.g., "CANON-31140")
planetary: string       # Planet name if applicable (e.g., "ACUMEN")
lunar: string           # Moon name if applicable (e.g., "IIC_CONSTELLATION")
```

### Optional Fields

```yaml
supersedes: string      # ID of document this replaces (e.g., "CANON-17")
deprecated: boolean     # Whether this document is deprecated
change_velocity: enum   # eternal | quarterly | monthly | weekly
dependencies: list      # IDs of required documents
synopsis: string        # One-paragraph summary (≤300 chars)
aliases: list           # Alternative names for reference
---
```

---

## Part II: Field Specifications

### id

**Type**: String
**Format**: `[TIER]-[NUMBER]` or `[TIER]-[NUMBER]-[SUBTIER]`
**Examples**:
- `CANON-00000`
- `CANON-31141`
- `GENESIS-000`
- `QUEUE-36000`

**Validation**: Must match pattern `^(CANON|GENESIS|OPERATIONAL|QUEUE|EXEMPLA)-[0-9]{3,5}$`

### name

**Type**: String
**Format**: Human-readable title case
**Examples**:
- "Syncrescendent Schema"
- "Five Account Architecture"
- "The Founding Moment"

**Validation**: 3-100 characters, no special characters except spaces and hyphens

### identity

**Type**: String
**Format**: SCREAMING_SNAKE_CASE, ≤25 characters
**Examples**:
- `SCHEMA`
- `FIVE_ACCOUNT`
- `ORIGIN`

**Validation**: Must match pattern `^[A-Z][A-Z0-9_]{1,24}$`

### tier

**Type**: Enum
**Values**: `GENESIS` | `CANON` | `OPERATIONAL` | `QUEUE` | `EXEMPLA`
**Description**:
- `GENESIS`: Foundational narrative layer
- `CANON`: Constitutional architecture
- `OPERATIONAL`: Living work documents
- `QUEUE`: Pending canonization or deletion
- `EXEMPLA`: Demonstrations and examples

### type

**Type**: Enum
**Values**: `cosmos` | `core` | `lattice` | `chain` | `planetary` | `lunar` | `satellite` | `comet` | `asteroid` | `ring` | `meta`
**Description**:
- `cosmos`: Universal principles (00xxx)
- `core`: Central celestial body (1xxxx)
- `lattice`: Cross-cutting structures (2xxxx)
- `chain`: Chain-level documents (3x000)
- `planetary`: Major bodies (3x100)
- `lunar`: Moons (3x1x0)
- `satellite`: Small bodies around moons (3x1xx)
- `comet`: Eccentric supplements (3x0xx)
- `asteroid`: Fragments (3x0xx sublevels)
- `ring`: Ring structures (Transcendence)
- `meta`: Archival/special (99xxx)

### chain

**Type**: Enum (conditional)
**Values**: `INTELLIGENCE` | `INFORMATION` | `INSIGHT` | `EXPERTISE` | `KNOWLEDGE` | `WISDOM`
**Required**: When tier=CANON and type in {chain, planetary, lunar, satellite, comet, asteroid, ring}

### version

**Type**: String
**Format**: Semantic versioning `MAJOR.MINOR.PATCH`
**Examples**: `2.0.0`, `1.1.0`, `2.3.0`
**Rules**:
- MAJOR: Reconception or breaking changes
- MINOR: Significant additions or modifications
- PATCH: Typo fixes, clarifications

### status

**Type**: Enum
**Values**: `canonical` | `draft` | `deprecated`
**Description**:
- `canonical`: Active, authoritative
- `draft`: Work in progress
- `deprecated`: Superseded, kept for reference

### created / updated

**Type**: String
**Format**: ISO 8601 date (`YYYY-MM-DD`)
**Examples**: `2025-10-17`, `2025-12-30`

### parent

**Type**: String | null
**Format**: Parent document ID
**Examples**: `CANON-31140`, `CANON-35100`, `null`
**Description**: Direct parent in celestial hierarchy

### change_velocity

**Type**: Enum
**Values**: `eternal` | `quarterly` | `monthly` | `weekly`
**Description**:
- `eternal`: Never changes after canonization
- `quarterly`: Reviewed/updated quarterly
- `monthly`: Monthly updates expected
- `weekly`: Rapidly evolving

### synopsis

**Type**: String
**Format**: Plain text, ≤300 characters
**Description**: One-paragraph summary for manifest and navigation

---

## Part III: Tier-Specific Templates

### GENESIS Template

```yaml
---
id: GENESIS-000
name: The Founding Moment
identity: ORIGIN
tier: GENESIS
type: null
version: 1.0.0
status: canonical
created: 2025-12-30
updated: 2025-12-30
synopsis: Why Syncrescendence exists - the convergence crisis, founding decisions, and aspiration.
---
```

### CANON Cosmos Template

```yaml
---
id: CANON-00000
name: Syncrescendent Schema
identity: SCHEMA
tier: CANON
type: cosmos
version: 2.0.0
status: canonical
created: 2025-10-01
updated: 2025-12-30
change_velocity: quarterly
synopsis: Master structural schema defining document hierarchy, numbering, and relationships.
---
```

### CANON Chain Template

```yaml
---
id: CANON-31000
name: Information Chain
identity: INFORMATION
tier: CANON
type: chain
chain: INFORMATION
parent: null
version: 2.0.0
status: canonical
created: 2025-10-01
updated: 2025-12-30
synopsis: The sensing and perception chain - atmospheric awareness enabling all other processing.
---
```

### CANON Planetary Template

```yaml
---
id: CANON-31100
name: Acumen
identity: ACUMEN
tier: CANON
type: planetary
chain: INFORMATION
parent: CANON-31000
planetary: ACUMEN
version: 2.3.0
status: canonical
created: 2025-10-01
updated: 2025-12-30
synopsis: The Information chain's primary planet - perceptual discrimination and atmospheric sensing.
---
```

### CANON Lunar Template

```yaml
---
id: CANON-31140
name: IIC Constellation
identity: IIC
tier: CANON
type: lunar
chain: INFORMATION
parent: CANON-31100
planetary: ACUMEN
lunar: IIC_CONSTELLATION
version: 1.0.0
status: canonical
created: 2025-10-15
updated: 2025-12-30
synopsis: Integrated Information Curation - the constellation of content sensing and distribution practices.
---
```

### CANON Satellite Template

```yaml
---
id: CANON-31141
name: Five Account Architecture
identity: FIVE_ACCOUNT
tier: CANON
type: satellite
chain: INFORMATION
parent: CANON-31140
planetary: ACUMEN
lunar: IIC_CONSTELLATION
version: 1.0.0
status: canonical
created: 2025-10-20
updated: 2025-12-30
synopsis: The five-account social media architecture for multi-platform identity coherence.
---
```

### QUEUE Template

```yaml
---
id: QUEUE-36000
name: Philosophical Foundations
identity: PHIL_FOUNDATIONS
tier: QUEUE
type: null
target: CANON-36xxx
version: 1.0.0
status: draft
created: 2025-12-30
updated: 2025-12-30
expiration: 2 cycles
synopsis: Metahumanism synthesis extraction pending canonization or deletion.
---
```

---

## Part IV: Implementation Process

### Step 1: Pilot Documents (5)

Apply frontmatter to:
1. `CANON-00000-SCHEMA-cosmos.md`
2. `CANON-00001-SYNCRESCENDENCE-cosmos.md`
3. `CANON-31141-FIVE_ACCOUNT-satellite-IIC-lunar-ACUMEN-planetary-INFORMATION.md`
4. `GENESIS-000-ORIGIN.md`
5. `QUEUE-36000-philosophical-foundations.md`

### Step 2: Validate Pilot

Check:
- [ ] All required fields present
- [ ] Field values match schema
- [ ] IDs are unique
- [ ] Parent references resolve
- [ ] Synopsis under 300 chars

### Step 3: Full Rollout

Apply to all 58 CANON files + 4 GENESIS files + 5 QUEUE files.

### Step 4: Auto-Generation

Create manifest generation script that reads frontmatter and produces CANON-00002.

---

## Part V: Validation Script

```bash
#!/bin/bash
# validate_frontmatter.sh - Validate YAML frontmatter

validate_file() {
    local file="$1"
    local errors=0

    # Extract frontmatter
    frontmatter=$(sed -n '/^---$/,/^---$/p' "$file" | sed '1d;$d')

    # Check required fields
    for field in id name identity tier type version status created updated; do
        if ! echo "$frontmatter" | grep -q "^$field:"; then
            echo "MISSING: $field in $file"
            ((errors++))
        fi
    done

    # Validate id format
    id=$(echo "$frontmatter" | grep "^id:" | cut -d: -f2 | tr -d ' ')
    if ! [[ "$id" =~ ^(CANON|GENESIS|OPERATIONAL|QUEUE|EXEMPLA)-[0-9]{3,5}$ ]]; then
        echo "INVALID ID: $id in $file"
        ((errors++))
    fi

    # Validate version format
    version=$(echo "$frontmatter" | grep "^version:" | cut -d: -f2 | tr -d ' ')
    if ! [[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        echo "INVALID VERSION: $version in $file"
        ((errors++))
    fi

    if [[ $errors -eq 0 ]]; then
        echo "VALID: $file"
    fi

    return $errors
}

# Validate all markdown files
for file in CANON/**/*.md GENESIS/*.md QUEUE/*.md; do
    if [[ -f "$file" ]]; then
        validate_file "$file"
    fi
done
```

---

## Part VI: Manifest Generation Script

```bash
#!/bin/bash
# generate_manifest.sh - Auto-generate CANON-00002 from frontmatter

OUTPUT="CANON/cosmos/CANON-00002-CORPUS-cosmos.md"

cat > "$OUTPUT" << 'HEADER'
---
id: CANON-00002
name: Syncrescendent Corpus
identity: CORPUS
tier: CANON
type: cosmos
version: 2.0.0
status: canonical
created: 2025-10-01
updated: $(date +%Y-%m-%d)
change_velocity: weekly
synopsis: Auto-generated manifest of all canonical documents.
---

# SYNCRESCENDENT CORPUS MANIFEST
## Auto-Generated Document Registry

**Generated**: $(date)
**Source**: YAML frontmatter extraction

---

## GENESIS Layer

| ID | Name | Identity | Status |
|----|------|----------|--------|
HEADER

# Extract GENESIS entries
for file in GENESIS/*.md; do
    if [[ -f "$file" ]]; then
        id=$(grep "^id:" "$file" | head -1 | cut -d: -f2 | tr -d ' ')
        name=$(grep "^name:" "$file" | head -1 | cut -d: -f2-)
        identity=$(grep "^identity:" "$file" | head -1 | cut -d: -f2 | tr -d ' ')
        status=$(grep "^status:" "$file" | head -1 | cut -d: -f2 | tr -d ' ')
        echo "| $id | $name | $identity | $status |" >> "$OUTPUT"
    fi
done

cat >> "$OUTPUT" << 'COSMOS'

## CANON Cosmos (00xxx)

| ID | Name | Identity | Status |
|----|------|----------|--------|
COSMOS

# Extract cosmos entries
for file in CANON/cosmos/*.md; do
    if [[ -f "$file" ]]; then
        id=$(grep "^id:" "$file" | head -1 | cut -d: -f2 | tr -d ' ')
        name=$(grep "^name:" "$file" | head -1 | cut -d: -f2-)
        identity=$(grep "^identity:" "$file" | head -1 | cut -d: -f2 | tr -d ' ')
        status=$(grep "^status:" "$file" | head -1 | cut -d: -f2 | tr -d ' ')
        echo "| $id | $name | $identity | $status |" >> "$OUTPUT"
    fi
done

# Continue for core, lattice, chains...

echo "Manifest generated: $OUTPUT"
```

---

## Part VII: Pilot Implementation

### GENESIS-000-ORIGIN.md Frontmatter

```yaml
---
id: GENESIS-000
name: The Founding Moment
identity: ORIGIN
tier: GENESIS
type: null
version: 1.0.0
status: canonical
created: 2025-12-30
updated: 2025-12-30
synopsis: Why Syncrescendence exists - the convergence crisis, founding decisions, and aspiration across individual, civilizational, and evolutionary scales.
---
```

### CANON-00000-SCHEMA-cosmos.md Frontmatter

```yaml
---
id: CANON-00000
name: Syncrescendent Schema
identity: SCHEMA
tier: CANON
type: cosmos
version: 2.0.0
status: canonical
created: 2025-10-01
updated: 2025-12-30
change_velocity: quarterly
synopsis: Master structural schema defining document hierarchy, numbering conventions, celestial metaphor, and navigational grammar.
---
```

### CANON-31141 Frontmatter

```yaml
---
id: CANON-31141
name: Five Account Architecture
identity: FIVE_ACCOUNT
tier: CANON
type: satellite
chain: INFORMATION
parent: CANON-31140
planetary: ACUMEN
lunar: IIC_CONSTELLATION
version: 1.0.0
status: canonical
created: 2025-10-20
updated: 2025-12-30
synopsis: The five-account social media architecture enabling multi-platform identity coherence and content distribution.
---
```

---

## Status

**Specification**: COMPLETE
**Pilot Implementation**: READY
**Full Rollout**: PENDING (after nomenclature reform)

---

*Self-describing documents enable self-navigating systems.*
