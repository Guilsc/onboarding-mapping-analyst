---
name: Learning and Knowledge Curation
description: >
  Convert validated corrections, decisions, resolved clarifications, approved
  version changes, and agent mistakes into durable governed knowledge so future
  mapping analysis improves without treating chat history or unvalidated findings
  as canonical truth.
task_intents:
  - analyze
  - generate
  - update
  - discover
---

# Learning and Knowledge Curation

## Purpose

Persist only validated learning that should influence future mapping reasoning.

## Use this skill when

- a BA/authorized owner corrects the agent;
- a clarification is resolved;
- a taxonomy decision is approved/rejected;
- a canonical rule is approved/rejected;
- new evidence is validated;
- an AI mistake is confirmed;
- an approved version change creates durable new knowledge.

## Do not use this skill when

- a finding is still hypothetical;
- evidence is unresolved/conflicting;
- a one-off request-specific difference should not become canonical;
- the conversation contains speculation that has not been validated.

## Inputs

Use whichever apply:
- correction/decision;
- supporting evidence;
- affected mapping family/object/field;
- current registries;
- Master version information;
- relevant Skill/Agent Core behavior.

## Analysis guidance

Determine:
1. previous interpretation;
2. corrected/approved interpretation;
3. why the earlier interpretation was wrong/incomplete;
4. evidence;
5. affected families/objects/fields;
6. registry updates required;
7. Skill/Agent Core improvement required?;
8. Master version impact?

Learning types:
- Domain Rule;
- Taxonomy Decision;
- Exception;
- Clarification Resolution;
- Agent Error;
- Skill Improvement;
- Governance Improvement.

## Expected output

As needed:
- Learning Candidate;
- registry update recommendation;
- linked Decision/Rule/Exception/Clarification updates;
- Skill/Agent Core improvement recommendation;
- Master Change Candidate.

## Quality gates

Before persisting:
- only validated learning becomes shared canonical knowledge;
- preserve evidence/decision traceability;
- do not learn from frequency alone;
- do not let one chat silently rewrite governed knowledge;
- keep request-specific behavior separate unless explicitly approved as reusable.
