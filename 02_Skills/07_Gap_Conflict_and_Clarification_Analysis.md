---
name: Gap Conflict and Clarification Analysis
description: >
  Distinguish missing mappings, confirmed gaps, true conflicts, observed differences,
  and unresolved questions. Use when evidence is incomplete, inconsistent, or may be
  explained by lifecycle/automation rather than an actual defect in the mapping model.
task_intents:
  - analyze
  - update
  - discover
---

# Gap, Conflict and Clarification Analysis

## Purpose

Classify uncertainty accurately so the agent does not turn incomplete or contradictory evidence into false rules or false gaps.

## Use this skill when

- expected behavior cannot be found;
- two credible sources disagree;
- production/example state differs from documented behavior;
- lifecycle/automation may explain a difference;
- a decision cannot safely be made from available evidence;
- an Analysis Review needs clear open questions.

## Do not use this skill when

- evidence is already clear and consistent;
- the user only asks for a straightforward lookup;
- no uncertainty or discrepancy exists.

## Inputs

Use whichever are relevant:
- expected/canonical behavior;
- observed/example behavior;
- source evidence;
- version/lifecycle context;
- Salesforce/Workfront findings;
- approved decisions/rules.

## Analysis guidance

Use these definitions:

### Missing Mapping
Reliable evidence shows a mapping should exist but it cannot be found.

### Confirmed Gap
Evidence demonstrates expected behavior is missing or incorrect.

### Conflict
Credible sources define incompatible behavior under the same conditions.

### Observed Difference
Actual/example state differs, but lifecycle/automation may explain it.

### Clarification Required
Evidence cannot safely establish the correct behavior.

For each issue state:
- expected behavior;
- observed/documented behavior;
- evidence;
- impact;
- possible lifecycle explanation;
- classification;
- precise question when needed.

## Expected output

Return only relevant issues, including:
- classification;
- evidence;
- impact;
- clarification question;
- recommended owner/SME when useful.

## Quality gates

Before concluding:
- never convert uncertainty into a Confirmed Gap;
- distinguish conflicting rules from conditional behavior;
- consider lifecycle/automation explanations;
- ask precise questions rather than generic requests for clarification.
