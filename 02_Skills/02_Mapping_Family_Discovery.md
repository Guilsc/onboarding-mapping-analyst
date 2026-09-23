---
name: Mapping Family Discovery
description: >
  Discover which mapping sources represent the same reusable onboarding behavior
  and where meaningful family boundaries exist. Use when taxonomy is unknown,
  sources appear related but not identical, or a new source set may represent a
  new mapping family rather than an implementation-specific variation.
task_intents:
  - analyze
  - discover
---

# Mapping Family Discovery

## Purpose

Discover reusable onboarding mapping families from evidence rather than imposing a predefined taxonomy.

## Use this skill when

- the user asks whether mapping files belong together;
- taxonomy or mapping-family boundaries are unclear;
- a new source set does not obviously fit an existing family;
- historical labels may mix channel, product, partner, service, or implementation concepts;
- a new Master Mapping may need to be discovered.

## Do not use this skill when

- a simple comparison can answer the user's question;
- the mapping family is already governed and the user only wants request generation;
- the task is only a field-level change within a known family.

## Inputs

Use whichever are available:
- classified source inventory;
- candidate mapping files;
- Salesforce object/field findings;
- Workfront findings;
- payload structures;
- approved taxonomy and Masters, when evaluating an existing workspace.

## Analysis guidance

Compare behavior across sources, including:
- Salesforce objects and Create / Update / Reference behavior;
- object relationships and cardinality;
- field sets;
- required behavior;
- conditions;
- Source / MuleSoft / Salesforce population ownership;
- transformations and defaults;
- Workfront applicability/template behavior;
- entry mechanism;
- payload structure;
- product/service;
- requestClass/business model.

### Boundary test

Ask:

**Would this behavior still make sense if the partner/reseller name were removed?**

If yes, it may represent reusable canonical behavior.

### Two-pass hypothesis validation

First derive candidate families independently from source evidence.

Only afterward compare them to prior hypothesis artifacts and classify each hypothesis as:
- Confirmed;
- Partially Confirmed;
- Refined;
- Split;
- Merged;
- Reclassified;
- Contradicted;
- Insufficient Evidence.

## Expected output

As needed:
- candidate clusters;
- proposed canonical families;
- defining characteristics;
- important differences;
- supporting sources;
- confidence/evidence strength;
- unresolved classification questions.

## Quality gates

Before concluding:
- do not force Channel + Product as the taxonomy;
- do not make Partner/Reseller a family solely because it appears frequently;
- do not use filename similarity as primary evidence;
- preserve legitimate conditional or implementation-specific differences;
- surface uncertainty rather than forcing a family decision.
