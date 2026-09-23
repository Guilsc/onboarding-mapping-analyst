---
name: Canonical Mapping Analysis
description: >
  Decide which evidence-backed objects, fields, rules, conditions, and behaviors
  belong in a reusable Master Mapping and which should remain variants, exceptions,
  legacy behavior, conflicts, or unknowns.
task_intents:
  - analyze
  - update
  - discover
---

# Canonical Mapping Analysis

## Purpose

Determine what should become part of the reusable Master Mapping model.

## Use this skill when

- discovery has produced candidate reusable rules;
- a Master is being designed;
- new evidence may change canonical behavior;
- the team needs to separate reusable rules from implementation/partner variants;
- canonical readiness must be assessed.

## Do not use this skill when

- the user only wants a simple comparison or explanation;
- the task is request-specific generation with no proposed canonical change;
- source discovery is not mature enough to support reusable conclusions.

## Inputs

Use whichever are available:
- reconciled field/object findings;
- Mapping Family findings;
- Salesforce/Workfront analysis;
- approved rules/decisions;
- gaps/conflicts/clarifications;
- production evidence.

## Analysis guidance

For every proposed object/field/rule ask:

1. Is it reusable?
2. Is evidence sufficient?
3. Would it remain valid without partner/reseller identity?
4. Is it conditional?
5. Is the condition reusable and explicit?
6. Does it conflict with approved knowledge?
7. Is it legacy or implementation-specific?

Classify as:
- CANONICAL;
- CONDITIONAL CANONICAL;
- IMPLEMENTATION VARIANT;
- PARTNER-SPECIFIC;
- LEGACY;
- CONFLICT;
- UNKNOWN.

## Expected output

As needed:
- proposed canonical rule set;
- conditional rules;
- excluded rules;
- rationale/evidence;
- clarifications;
- readiness for Master generation/update.

## Quality gates

Before concluding:
- do not promote weak evidence to canonical;
- do not treat partner identity as a reusable rule without a reusable business condition;
- do not hide conflicts;
- preserve legitimate variants and conditions;
- ensure canonical conclusions remain explainable from evidence.
