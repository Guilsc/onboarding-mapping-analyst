---
name: Workfront Mapping Analysis
description: >
  Determine whether Adobe Workfront applies to an onboarding mapping and analyze
  the project/template, Salesforce-to-Workfront lineage, field mappings, conditions,
  defaults, and exceptions. Use when Workfront behavior may be standard,
  conditional, exceptional, or unclear.
task_intents:
  - analyze
  - generate
  - update
  - discover
---

# Workfront Mapping Analysis

## Purpose

Determine whether and how Adobe Workfront project mapping applies to the current mapping task.

## Use this skill when

- Workfront files/evidence are present;
- the intake may require a Workfront project;
- a Master needs Workfront applicability classified;
- Workfront template/field behavior differs across implementations;
- a change may affect Salesforce-to-Workfront mapping.

## Do not use this skill when

- the mapping family is confirmed to have no Workfront behavior;
- the user's question is unrelated to Workfront;
- the task can be answered entirely from a known Salesforce rule.

## Inputs

Use whichever are available:
- Workfront mappings;
- Salesforce mappings/fields;
- intake/request information;
- current Approved Master;
- production examples;
- integration behavior/evidence.

## Analysis guidance

Classify applicability as:
- STANDARD;
- CONDITIONAL;
- EXCEPTION;
- NOT OBSERVED;
- UNKNOWN.

Frequency alone does not make Workfront canonical.

Analyze:
- whether project creation/update occurs;
- creation/update condition;
- project template selection;
- Salesforce source object/field;
- Workfront target fields;
- integration-set/default values;
- transformations;
- required behavior;
- reusable vs partner-specific differences;
- supporting evidence and strength.

### Request-generation rule

Generate Workfront when:
1. intake explicitly requires it; OR
2. Approved Master says STANDARD; OR
3. Approved Master says CONDITIONAL and the condition is met.

## Expected output

As needed:
- Workfront applicability;
- template/project behavior;
- reusable field mapping;
- conditions/exceptions;
- conflicts/clarifications;
- recommendation on whether Master/request output needs a Workfront tab.

## Quality gates

Before concluding:
- do not treat frequency as proof;
- preserve explicit conditional behavior;
- verify Salesforce-to-Workfront lineage where possible;
- distinguish reusable behavior from partner-specific exceptions;
- do not create an empty Workfront tab when Workfront does not apply.
