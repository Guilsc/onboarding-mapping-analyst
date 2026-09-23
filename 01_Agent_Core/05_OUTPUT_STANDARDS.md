# Output Standards

## Analysis Review

Before first Master generation or a material version change, provide a BA-reviewable summary including when relevant:
- Executive Summary
- Sources Analyzed
- Mapping Families / Taxonomy
- Source-to-Family Classification
- Salesforce Object Coverage
- Object Cardinality
- Field Coverage
- Population Ownership
- Reusable Conditions
- Workfront Applicability
- Partner/Reseller-Specific Exclusions
- Missing Mappings
- Confirmed Gaps
- Conflicts
- Clarifications
- Assumptions
- Prior Hypothesis Validation
- Proposed Workbook Structure
- Readiness
- GO / GO WITH CLARIFICATIONS / NO-GO

## Canonical Master Mapping

### Required
`Salesforce Mapping`

All Salesforce objects belong in ONE consolidated mapping tab, grouped/ordered by object.

Minimum concepts:
- Salesforce Object
- Field Label
- Field API Name
- Source
- Source Field / JSON Path
- Required?
- Population Owner
- Mapping / Transformation
- Default / Fixed Value
- Condition
- Notes
- Sample

Preserve useful historical mapping columns where practical.

### Conditional
`Workfront Project Mapping`

Only when Workfront applies.

### Optional
`Analysis & Assumptions`

Only when important context must remain with the artifact.

### Version-change tab
`Change Log`

Primarily for V2+ or any changed canonical version.

The Change Log records business-significant mapping changes between logical OMA versions. It does not replace Google native file version history and should not attempt to record every working edit made while a Draft is being developed.

Do not create empty tabs.
