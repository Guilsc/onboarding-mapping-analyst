---
name: Change and Impact Analysis
description: >
  Translate requested mapping changes into structured proposed changes and assess
  their downstream impact across fields, Salesforce objects, Workfront, conditions,
  mapping families, request-generation behavior, and versioned artifacts.
task_intents:
  - update
  - analyze
---

# Change and Impact Analysis

## Purpose

Understand a proposed change to an existing mapping before creating the next version.

## Use this skill when

- the user asks to modify an existing Master Mapping;
- changes arrive through meeting notes, SME comments, email, Jira/request text, or another mapping file;
- a new requirement may affect several fields/objects;
- the user asks what a proposed mapping change would impact.

## Do not use this skill when

- no mapping change is requested;
- the task is only a read-only explanation with no impact assessment;
- no existing mapping/model exists and discovery is required instead.

## Inputs

Use whichever are available:
- Current Approved Master;
- requested change input;
- meeting notes/ticket/email/comments;
- new mapping/evidence;
- approved decisions/rules;
- Salesforce/Workfront mappings.

## Analysis guidance

### First structure the requested change

Before editing anything, translate unstructured inputs into **Proposed Mapping Changes**.

For each proposed change capture, when relevant:
- target mapping family;
- domain/object;
- target field/rule;
- current behavior;
- proposed behavior;
- source of change;
- condition;
- rationale/evidence;
- unresolved ambiguity.

### Trace impact

Trace:

changed requirement  
→ affected fields  
→ affected Salesforce objects  
→ affected Workfront fields/templates  
→ affected canonical rules  
→ mapping families  
→ dependent conditions  
→ request-generation behavior  
→ backward impact.

Compare:
- Current Rule;
- Proposed Rule;
- Reason;
- Evidence;
- Impact;
- Risk.

## Expected output

As needed:
- structured Proposed Mapping Changes;
- impact analysis;
- affected artifacts/rules;
- Workfront impact;
- risks/conflicts/clarifications;
- proposed next-version changes.

## Quality gates

Before concluding:
- do not edit an Approved version in place;
- do not treat meeting notes as unambiguous requirements when wording is unclear;
- surface cross-object and request-generation impact;
- preserve unaffected behavior;
- identify when a change actually represents a new mapping family rather than a version update.
