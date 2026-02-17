# PRAC — Ontology Dataview Queries
## Ready-to-Use Obsidian Dataview Queries for CANON Ontology

**Version**: 1.0.0
**Created**: 2026-02-05
**Authority**: Commander (Claude Code Opus)
**Prerequisite**: Obsidian Dataview plugin installed; CANON files have extended frontmatter (`operational_status`, `entities_defined`, `depends_on`, `last_verified`)
**Coverage**: 10/79 CANON files have extended frontmatter (pilot batch). Remaining 69 files need extension.

---

## OPERATIONAL STATUS QUERIES

### All Theoretical CANON Files (What Needs Operationalization)
```dataview
TABLE operational_status, chain, type
FROM "01-CANON"
WHERE operational_status = "theoretical"
SORT id ASC
```

### All Operational CANON Files (What's Running)
```dataview
TABLE operational_status, chain, type
FROM "01-CANON"
WHERE operational_status = "operational"
SORT id ASC
```

### All Partial CANON Files (In Progress)
```dataview
TABLE operational_status, chain, type
FROM "01-CANON"
WHERE operational_status = "partial"
SORT id ASC
```

### Operational Status Summary (Counts)
```dataview
TABLE length(rows) AS "Count"
FROM "01-CANON"
WHERE operational_status
GROUP BY operational_status
```

### Stale Files (Not Verified Recently)
```dataview
TABLE operational_status, last_verified, chain
FROM "01-CANON"
WHERE last_verified < date("2026-01-01")
SORT last_verified ASC
```

---

## CHAIN-BASED QUERIES

### All Files in a Specific Chain
```dataview
TABLE type, operational_status, name
FROM "01-CANON"
WHERE chain = "WISDOM"
SORT id ASC
```
*(Replace "WISDOM" with: INTELLIGENCE, INFORMATION, INSIGHT, EXPERTISE, KNOWLEDGE)*

### Chain Operational Status Matrix
```dataview
TABLE chain, operational_status, type
FROM "01-CANON"
WHERE chain
SORT chain ASC, id ASC
```

### Theoretical Files by Chain (What Each Chain Needs)
```dataview
TABLE chain, name, type
FROM "01-CANON"
WHERE operational_status = "theoretical" AND chain
GROUP BY chain
```

---

## DEPENDENCY QUERIES

### Files That Depend on a Specific CANON
```dataview
TABLE name, operational_status, chain
FROM "01-CANON"
WHERE contains(depends_on, "CANON-00000")
SORT id ASC
```
*(Replace "CANON-00000" with any CANON ID to find its dependents)*

### Files With No Dependencies (Root Documents)
```dataview
TABLE name, operational_status, chain, type
FROM "01-CANON"
WHERE length(depends_on) = 0
SORT id ASC
```

### Dependency Count (Most Depended-Upon Files)
```dataview
TABLE name, length(depends_on) AS "Dependency Count", operational_status
FROM "01-CANON"
WHERE depends_on
SORT length(depends_on) DESC
```

---

## ENTITY QUERIES

### Files Defining Specific Entity Types
```dataview
TABLE name, entities_defined
FROM "01-CANON"
WHERE any(entities_defined, (e) => contains(e, "CAP"))
SORT id ASC
```
*(Replace "CAP" with: CON, STR, WF, AGT, NOT, MET, ART, PROTO)*

### All Defined Entities (Flattened)
```dataview
TABLE name, entities_defined
FROM "01-CANON"
WHERE entities_defined
SORT id ASC
```

---

## TIER QUERIES

### Files by Cosmological Tier
```dataview
TABLE name, chain, operational_status
FROM "01-CANON"
WHERE type = "cosmos"
SORT id ASC
```
*(Replace "cosmos" with: core, lattice, chain, planetary, lunar, satellite, comet, asteroid)*

### Tier Distribution
```dataview
TABLE length(rows) AS "Count"
FROM "01-CANON"
WHERE type
GROUP BY type
```

---

## MODIFICATION TRACKING

### Recently Modified CANON Files
```dataview
TABLE name, updated, operational_status
FROM "01-CANON"
SORT file.mtime DESC
LIMIT 10
```

### CANON Files Modified This Month
```dataview
TABLE name, chain, operational_status
FROM "01-CANON"
WHERE file.mtime > date("2026-02-01")
SORT file.mtime DESC
```

---

## COMBINED / STRATEGIC QUERIES

### Path to Gaian Field Node (Dependency Chain)
```dataview
TABLE name, operational_status, depends_on
FROM "01-CANON"
WHERE contains(id, "35") OR contains(depends_on, "CANON-35")
SORT id ASC
```

### Ontology Progress Dashboard
```dataview
TABLE
  length(filter(rows, (r) => r.operational_status = "operational")) AS "Operational",
  length(filter(rows, (r) => r.operational_status = "partial")) AS "Partial",
  length(filter(rows, (r) => r.operational_status = "theoretical")) AS "Theoretical",
  length(filter(rows, (r) => !r.operational_status)) AS "Unclassified"
FROM "01-CANON"
```

### Missing Frontmatter (Files Needing Extension)
```dataview
TABLE name, type, chain
FROM "01-CANON"
WHERE !operational_status
SORT id ASC
```

---

## USAGE NOTES

1. **Dataview plugin required**: Install from Obsidian Community Plugins
2. **Queries are live**: Results update as you modify CANON frontmatter
3. **Coverage tracking**: Use "Missing Frontmatter" query to track extension progress (currently 10/79)
4. **Copy-paste ready**: Each query block can be pasted directly into any Obsidian note
5. **Juggl complement**: For visual graph queries, install Juggl plugin and use typed links based on `depends_on` and `entities_defined`

---

## VERSION HISTORY

**v1.0.0** (2026-02-05): Genesis
- 20+ queries across 7 categories
- Operational status, chain, dependency, entity, tier, modification, strategic queries
- Pilot coverage: 10/79 CANON files
- Authority: Commander (Claude Code Opus)
