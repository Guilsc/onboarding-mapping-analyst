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

This Skill owns the OMA **Promote to Knowledge** action.

## Use this skill when

- the user asks to **Promote to Knowledge**;
- OMA identifies a validated discussion outcome that may be useful beyond the current conversation and asks whether it should be promoted;
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

For Promote to Knowledge, use this sequence:

Discussion  
→ Distill  
→ Classify  
→ Validate  
→ Persist

Determine:
1. what durable conclusion actually emerged;
2. whether it is validated enough to persist;
3. why the conclusion matters;
4. evidence and source references;
5. affected families/objects/fields;
6. the correct governed destination;
7. whether a registry update is required;
8. whether a Skill/Agent Core improvement is required;
9. whether there is Master version impact.

Do not treat exploratory reasoning, abandoned options, or unvalidated assumptions as durable knowledge.

Knowledge types:
- Mapping Decision;
- Domain Rule;
- Taxonomy Decision;
- Exception;
- Clarification Resolution;
- Agent Error;
- Skill Improvement;
- Governance Improvement.

## Expected output

As needed:
- Discussion Outcome / Knowledge Candidate;
- Learning Candidate;
- registry update recommendation;
- linked Decision/Rule/Exception/Clarification updates;
- Skill/Agent Core improvement recommendation;
- Master Change Candidate.

## Quality gates

Before persisting:
- persist the distilled outcome rather than the full raw chat by default;
- preserve rationale and source/evidence traceability;
- use an existing governed destination before creating a new artifact type;
- only validated learning becomes shared canonical knowledge;
- preserve evidence/decision traceability;
- do not learn from frequency alone;
- do not let one chat silently rewrite governed knowledge;
- keep request-specific behavior separate unless explicitly approved as reusable.
