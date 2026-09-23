---
name: Salesforce Objects Analysis
description: >
  Analyze Salesforce objects, relationships, field mappings, population ownership,
  cardinality, creation/update behavior, and conditions represented by onboarding
  evidence. Use when the task requires understanding Salesforce behavior rather
  than only locating or comparing an obvious field.
task_intents:
  - analyze
  - update
  - discover
---

# Salesforce Objects Analysis

## Purpose

Understand the complete Salesforce object model represented by the mapping evidence.

The Skill may analyze objects progressively, but it owns the full Salesforce analysis needed by the parent task.

## Use this skill when

- object creation/update/reference behavior must be understood;
- mappings disagree about Salesforce behavior;
- field ownership, dependencies, or cardinality are unclear;
- a Master Mapping is being discovered or materially changed;
- analysis spans multiple Salesforce objects;
- an onboarding difference may be caused by Salesforce automation or lifecycle behavior.

## Do not use this skill when

- the user only wants a filename or simple field location;
- one obvious field comparison can be answered directly;
- the task does not involve Salesforce behavior.

## Inputs

Use whichever are relevant:
- mapping sources;
- Salesforce examples/snapshots;
- payload or integration mappings;
- current Approved Master, when applicable;
- approved decisions/rules;
- production evidence.

## Analysis guidance

Reason about the evidence first. Do not force a predefined object order.

### Discover objects

For each object determine, when supported:
- Created / Updated / Referenced / Conditional / Not Created / Unknown;
- Required?;
- Expected Count / Scope;
- cardinality basis;
- creation/update conditions;
- dependencies and relationships;
- evidence;
- confidence/evidence strength.

Do not infer object creation merely because fields appear in a mapping.

### Analyze fields

For each relevant field determine:
- Field Label;
- Field API Name;
- Source;
- Source Field / JSON Path;
- Required / Optional / Conditional;
- Population Owner;
- Mapping / Transformation;
- Default / Fixed Value;
- Condition;
- Notes;
- Sample evidence;
- family differences;
- partner-specific differences;
- legacy behavior;
- missing/conflict/unknown status.

### Reconcile across objects

Validate:
- dependencies;
- cardinality;
- shared conditions;
- cross-object logic;
- lifecycle/automation explanations for observed state.

## Expected output

Return only the detail needed by the parent task, which may include:
- Salesforce Object Coverage;
- object behavior findings;
- field coverage;
- common/reusable rules;
- conditional rules;
- exclusions;
- gaps/conflicts/clarifications;
- evidence strength.

## Quality gates

Before concluding:
- verify object behavior is evidence-backed;
- distinguish immediate onboarding state from later automation where relevant;
- do not infer creation from field presence;
- do not hide cross-object dependencies;
- surface conflicts instead of silently reconciling them;
- final Master output uses one consolidated Salesforce Mapping tab, not one tab per object.
