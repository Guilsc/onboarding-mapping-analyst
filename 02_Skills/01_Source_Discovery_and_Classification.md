---
name: Source Discovery and Classification
description: >
  Inspect unfamiliar or newly added mapping sources to understand what they contain,
  how they relate to onboarding behavior, and which sources deserve deeper analysis.
  Use when the purpose, relevance, completeness, or mapping-family relationship of
  source files is not yet clear.
task_intents:
  - analyze
  - discover
---

# Source Discovery and Classification

## Purpose

Understand the source corpus before drawing canonical conclusions.

## Use this skill when

- historical resources are introduced for the first time;
- new mapping files or evidence arrive;
- file purpose or relevance is unclear;
- the user asks what a collection of files contains;
- a new or Custom Mapping Workspace needs an initial inventory;
- deeper analysis requires knowing which sources are trustworthy/relevant.

## Do not use this skill when

- the user only wants a simple field or filename lookup that can be answered directly;
- the correct mapping family and source are already known;
- the task is purely generating a request mapping from an existing Approved Master.

## Inputs

Use whichever are available:
- mapping files;
- payload/API mappings;
- Salesforce examples;
- Workfront mappings;
- intake examples;
- architecture/reference material;
- source metadata and folder context.

## Analysis guidance

Analyze actual content, not filename alone.

For each source determine, where relevant:
- source type;
- historical context;
- partner/reseller labels;
- concepts such as UCIF / Direct / MCIF / ECP / product / requestClass;
- Salesforce objects;
- Workfront content;
- payload/API content;
- mapping completeness;
- duplicate or legacy signals;
- potential relationship to one or more mapping families;
- evidence strength and rationale.

### Two-pass rule

During initial bootstrap or unfamiliar-source discovery:

1. independently classify the source corpus without consulting prior taxonomy/structure hypothesis artifacts;
2. only after an initial candidate model exists, compare it to prior hypotheses.

## Expected output

Return only what the parent task needs, which may include:
- Source Inventory;
- initial classification;
- duplicate/legacy candidates;
- sources recommended for deeper analysis;
- unresolved source questions;
- evidence strength.

## Quality gates

Before concluding:
- do not treat Partner as Mapping Family by default;
- do not treat filename as truth;
- allow Mixed / Unclassified when evidence is insufficient;
- do not create canonical rules in this Skill;
- do not let duplicate files artificially increase confidence.
