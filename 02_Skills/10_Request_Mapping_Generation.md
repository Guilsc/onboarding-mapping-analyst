---
name: Request Mapping Generation
description: >
  Interpret onboarding intake/request information, determine the appropriate mapping
  family and Current Approved Master, apply approved conditions, populate
  request-specific/sample values, determine Workfront applicability, and generate
  the request-specific mapping without changing the canonical Master.
task_intents:
  - generate
---

# Request Mapping Generation

## Purpose

Generate a request-specific mapping from intake/request information using the correct governed Master Mapping.

## Use this skill when

- the user supplies onboarding intake/request data;
- the user asks to generate a mapping for a specific onboarding;
- request-specific values/samples need to be applied to an Approved Master.

## Do not use this skill when

- no Approved Master exists and discovery is required;
- the user is asking to change canonical behavior;
- the request is only a read-only comparison/explanation.

## Inputs

Use whichever are available:
- intake/request payload or form data;
- Mapping Workspace;
- Current Approved Master Index;
- Approved Master(s);
- approved conditions/rules;
- Workfront applicability rules.

## Analysis guidance

1. interpret the request;
2. identify the likely mapping family;
3. resolve the Current Approved Master for that family;
4. resolve evidence-based ambiguity;
5. ask only material missing questions;
6. apply approved conditions;
7. populate request-specific values;
8. populate Sample where supported;
9. flag missing required intake data;
10. determine Workfront applicability;
11. validate the output.

The user does not need to choose the Master manually.

If the request reveals potentially reusable new behavior:
- create a Learning Candidate or Master Change Candidate;
- keep request output separate from canonical knowledge.

## Expected output

A request-specific mapping using the current governed Master as baseline, with:
- populated request/sample values where supported;
- missing required data flagged;
- applicable conditions;
- Workfront mapping when required;
- request-specific exceptions clearly identified.

## Quality gates

Before delivery:
- verify the selected Master is the current Approved version;
- do not silently use a Draft;
- do not modify the Master automatically;
- separate request-specific differences from reusable canonical behavior;
- validate required data and Workfront applicability.
