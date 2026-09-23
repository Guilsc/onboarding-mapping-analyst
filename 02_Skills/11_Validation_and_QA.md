---
name: Validation and QA
description: >
  Validate mapping analysis or generated artifacts for structural consistency,
  traceability, object/field integrity, canonicalization quality, Workfront
  applicability, and governance compliance before delivery or approval.
task_intents:
  - analyze
  - generate
  - update
  - discover
---

# Validation and QA

## Purpose

Check that a mapping analysis or artifact is internally consistent, traceable, and compliant with the solution's mapping/governance rules.

## Use this skill when

- a request-specific mapping is ready for delivery;
- a Master Draft is ready for review;
- an Analysis Review needs validation;
- material mapping changes have been applied;
- the parent workflow requires a quality gate.

## Do not use this skill when

- the user only wants a trivial lookup with no artifact/output to validate;
- there is not yet enough analysis to evaluate quality meaningfully.

## Inputs

Use the artifact/analysis being validated plus relevant:
- Approved Master/rules;
- source evidence;
- Salesforce/Workfront findings;
- version/governance metadata.

## Analysis guidance

### Salesforce
Check:
- duplicate targets;
- inconsistent API names;
- contradictory mappings without conditions;
- required targets without source/default/derivation;
- inconsistent cardinality/dependencies;
- population-owner inconsistencies;
- conflicting defaults/transformations;
- assumptions shown as facts.

### Canonicalization
Check:
- partner-specific leakage;
- legacy behavior treated as current;
- frequency mistaken for proof;
- inconsistent family boundaries.

### Workfront
Check:
- applicability rule;
- template behavior;
- Salesforce-to-Workfront lineage;
- Workfront tab created only when applicable.

### Governance
Check:
- traceability;
- visible conflicts;
- correct version metadata;
- no overwrite of Approved artifacts;
- correct separation between request-specific and canonical behavior.

## Expected output

Return:
- PASS;
- PASS WITH ISSUES; or
- FAIL.

Include concise findings and remediation only where relevant.

## Quality gates

A FAIL blocks an approval recommendation or final governed delivery until material issues are resolved.

Do not inflate minor presentation issues into FAIL when mapping correctness is unaffected.
