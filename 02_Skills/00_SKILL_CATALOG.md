# Skill Catalog

Use this catalog to select the smallest relevant Skill set before loading full Skill instructions.

Skills are **analytical lenses and quality gates**, not rigid workflow scripts.

The `name`, `description`, and `task_intents` metadata at the top of each Skill are the primary routing signals.

| # | Skill | Use when | Typical Task Intents |
|---|---|---|---|
| 01 | Source Discovery and Classification | Source purpose, relevance, completeness, or relationship is unclear; a new corpus/workspace needs inspection. | Analyze, Discover |
| 02 | Mapping Family Discovery | Taxonomy/family boundaries are unclear or sources may represent a new reusable model. | Analyze, Discover |
| 03 | Salesforce Objects Analysis | Salesforce object behavior, relationships, cardinality, ownership, fields, or conditions require investigation. | Analyze, Update, Discover |
| 04 | Workfront Mapping Analysis | Workfront applicability, template/project behavior, field lineage, or conditions require analysis. | Analyze, Generate, Update, Discover |
| 05 | Field Reconciliation | Sources disagree about source/path, requiredness, owner, transformation, default, condition, or version behavior. | Analyze, Update, Discover |
| 06 | Canonical Mapping Analysis | Evidence-backed behavior must be classified as reusable canonical, conditional, variant, exception, legacy, conflict, or unknown. | Analyze, Update, Discover |
| 07 | Gap Conflict and Clarification Analysis | Evidence is missing, inconsistent, conflicting, or may be explained by lifecycle/automation. | Analyze, Update, Discover |
| 08 | Master Mapping Generation | Validated canonical analysis is ready to become a new or next-version Master Draft. | Update, Discover |
| 09 | Change and Impact Analysis | Requested changes must be structured and traced across fields, objects, Workfront, conditions, versions, and request behavior. | Update, Analyze |
| 10 | Request Mapping Generation | Intake/request data must be mapped using the correct current Approved Master. | Generate |
| 11 | Validation and QA | A mapping analysis or artifact needs a quality gate before delivery/approval. | Analyze, Generate, Update, Discover |
| 12 | Learning and Knowledge Curation | A validated correction/decision/learning should become durable governed knowledge. | Analyze, Generate, Update, Discover |

## Selection principles

- Start from **Task Intent**, not from Skill number.
- Prefer the smallest Skill set that can answer the request reliably.
- A simple lookup/comparison may not require a full Skill workflow.
- A Skill may be invoked alone or combined with others.
- Do not select a Skill only because a keyword appears in the prompt; consider the actual analytical need.
- Do not bind Skills to a specific Google AI surface or model.
- Do not turn `task_intents` into hard restrictions. They are routing hints.
