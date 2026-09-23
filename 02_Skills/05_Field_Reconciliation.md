---
name: Field Reconciliation
description: >
  Reconcile field-level mapping evidence across sources that belong to the same
  candidate or approved mapping family. Use when sources disagree about field
  source, requiredness, population owner, transformations, defaults, conditions,
  or version/implementation behavior.
task_intents:
  - analyze
  - update
  - discover
---

# Field Reconciliation

## Purpose

Determine which field-level behaviors agree, differ legitimately, conflict, or remain unknown across evidence for the same mapping family.

## Use this skill when

- multiple sources describe the same target field differently;
- field source/path differs across files;
- requiredness, owner, default, transformation, or condition is inconsistent;
- a Master is being discovered or updated;
- the user asks why two mappings differ at field level.

## Do not use this skill when

- only one authoritative field rule exists and no comparison is needed;
- the question is purely object-level and has no field-level uncertainty;
- the user only wants a simple lookup.

## Inputs

Use whichever are available:
- field-level mappings;
- Salesforce object findings;
- payload/API paths;
- Workfront mappings when relevant;
- Approved Master/decisions;
- version history and production evidence.

## Analysis guidance

For each logical target field compare:
- source/path;
- required behavior;
- population owner;
- transformations/defaults;
- conditions;
- version differences;
- partner-specific differences;
- supporting evidence.

Classify as:
- CONFIRMED REUSABLE;
- CONDITIONAL REUSABLE;
- IMPLEMENTATION VARIANT;
- PARTNER-SPECIFIC;
- LEGACY;
- MISSING;
- CONFLICTING;
- UNKNOWN.

Do not use majority occurrence alone as proof.

Do not simplify away legitimate conditional behavior.

## Expected output

Return only what the parent task needs, such as:
- reconciled field rule;
- evidence comparison;
- condition/variant classification;
- conflicts;
- missing information;
- clarification questions.

## Quality gates

Before concluding:
- distinguish absence of evidence from evidence of absence;
- do not convert frequency into canonicality;
- preserve reusable conditions;
- keep partner-specific behavior out of reusable rules unless evidence supports it;
- surface unresolved conflicts explicitly.
