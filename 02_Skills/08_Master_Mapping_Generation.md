---
name: Master Mapping Generation
description: >
  Generate a new or next-version Master Mapping artifact from validated canonical
  analysis. Use only when analysis is sufficiently complete and the required human
  authorization to generate the Draft/approved artifact has been provided.
task_intents:
  - update
  - discover
---

# Master Mapping Generation

## Purpose

Create the governed Master Mapping artifact after analysis has established the reusable model.

## Use this skill when

- Analysis Review supports Master generation;
- the BA/authorized owner has approved generation of a new Master Draft;
- a validated canonical change requires a next-version Draft.

## Do not use this skill when

- source analysis is still incomplete;
- material conflicts/clarifications block reliable generation;
- the user only wants a comparison/explanation;
- the task is request-specific generation;
- approval/authorization required by governance has not been provided.

## Inputs

Use:
- validated canonical rule set;
- Salesforce Objects Analysis;
- Workfront analysis when applicable;
- field reconciliation;
- resolved clarifications/approved assumptions;
- current Master/version when creating Vn+1.

## Analysis guidance

### Initial Master

Create a NEW artifact.

Never modify a historical source file.

### Workbook structure

Required:
- Salesforce Mapping

Conditional:
- Workfront Project Mapping

Optional:
- Analysis & Assumptions
- Change Log

Do not create empty tabs.

### Salesforce rule

All Salesforce objects are consolidated into one Salesforce Mapping tab, grouped/ordered by object.

### Version rule

- first approved canonical Master = V1;
- Approved versions are immutable;
- changed canonical content creates a new Draft version;
- never overwrite an Approved Master.

## Expected output

A Master Mapping Draft matching the approved mapping/output standards.

## Quality gates

Before delivery:
- verify only validated canonical/conditional rules are included;
- keep implementation/partner exceptions out unless explicitly represented as governed conditions;
- preserve traceability;
- include Workfront only when applicable;
- do not mark a generated file Approved without explicit authorization.
