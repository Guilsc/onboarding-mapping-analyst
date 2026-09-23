# Router

Infer the user's **Task Intent** from natural language. The user does not need to know Skill names, model tiers, or the best Google AI surface.

Use this decision order:

Task Intent  
→ Mapping Workspace  
→ Complexity / Consequence  
→ Relevant Skills  
→ Doppelganger (optional)  
→ Governance level.

## Step 1 — Understand Task Intent

### A. Analyze / Compare / Explain

Use for:
- filename/source lookup;
- simple or complex file comparison;
- field lineage;
- "why is this logic different?";
- onboarding-type differences;
- object behavior questions;
- version comparison;
- impact questions where no change is requested.

Default to read-only analysis.

Do not invoke a Master lifecycle for a small question.

### B. Generate Mapping from Intake

Use when intake/request data is supplied or the user asks for a request-specific mapping.

Sequence:
interpret intake  
→ resolve Mapping Workspace  
→ classify mapping family  
→ resolve Current Approved Master  
→ apply conditions/rules  
→ populate Sample/request values  
→ determine Workfront applicability  
→ validate  
→ generate request-specific output.

The user does not need to choose the Master manually.

### C. Update Existing Mapping

Use when the user wants a mapping changed or versioned.

Change input may be:
- explicit A/B/C/D changes;
- meeting notes;
- SME comments;
- email/Jira/request text;
- another mapping file;
- implementation findings.

Sequence:
resolve Mapping Workspace + Current Approved Master  
→ translate input into Proposed Mapping Changes  
→ compare current vs proposed behavior  
→ Change & Impact Analysis  
→ supporting Salesforce/Workfront/Field analysis  
→ Vn+1 Draft  
→ Validation / Analysis Review as required  
→ READY_FOR_APPROVAL  
→ file approval event  
→ new Approved version.

If the user says or asks anything that would constitute approval in the AI conversation, always display:

> Approval intent recorded. Final governed approval must still be completed in the mapping file. The file approval is the authoritative trigger for promotion and the downstream approval workflow.

Then record the approval intent when appropriate, prepare/point to the approval artifact, and keep the mapping in READY_FOR_APPROVAL. Do not promote the Master until the file approval event is confirmed.

Never edit an Approved Master in place.

### D. Discover / Build New Mapping

Use when:
- no Approved Master exists;
- the source set does not reasonably fit an existing mapping family;
- taxonomy/mapping families are unknown;
- the user explicitly wants a new Master.

Sequence:
Source Discovery  
→ Mapping Family Discovery  
→ Salesforce Objects Analysis  
→ Workfront Mapping Analysis when relevant  
→ Field Reconciliation  
→ Canonical Mapping Analysis  
→ Gap/Conflict/Clarification Analysis  
→ Validation  
→ Analysis Review  
→ V1 Draft  
→ READY_FOR_APPROVAL  
→ file approval event  
→ V1 Approved.

## Step 2 — Resolve Mapping Workspace

1. explicit user-provided mapping files/folder → Custom Mapping Workspace;
2. otherwise use the Recommended Shared Workspace when configured and accessible;
3. if neither is available and the task requires mapping sources, ask for one;
4. validate that the source set is mapping-related.

Never merge a Custom Workspace into the Recommended Shared Workspace automatically.

## Step 3 — Assess Complexity and Consequence

Consider:
- corpus size;
- ambiguity;
- reasoning complexity;
- cross-object/system scope;
- evidence conflict;
- read vs write intent;
- canonical impact;
- current environment capability.

Use the Execution Policy.

## Step 4 — Apply Relevant Skills

Skills are analytical lenses and quality gates.

Use `02_Skills/00_SKILL_CATALOG.md` as the compact routing index:
1. compare the Task Intent and analytical need against Skill metadata/descriptions;
2. select the smallest relevant Skill set;
3. load/use the full Skill instructions only for selected Skills.

A simple comparison may need no full workflow.

## Step 5 — Resolve Doppelganger

Doppelganger is optional.

Supported modes:
- No Personalization;
- Private Profile;
- Import from Shared Personalization Path.

Use at most one Personal Profile and one Role Lens by default.

### Resolve the Role Lens

1. explicit user-selected/requested Lens wins;
2. otherwise, if the task strongly and unambiguously matches one available Shared Lens, use it;
3. otherwise, for a neutral task, use the Personal Profile's optional default Role Lens;
4. otherwise use a unique configured role/title default when available;
5. otherwise use no Lens.

Examples:
- regression/test scenarios → QA Lens, when available;
- manual/operational impact → Operations Lens, when available;
- source path/transformation/integration dependencies → Developer / Integration Lens, when available.

If multiple perspectives are explicitly requested, run them separately and combine findings. Do not blend Lens instructions.

### Resolve the Personal Profile

Use one when:
1. explicitly selected by the user; or
2. explicitly bound/configured for that user.

Do not auto-select another person's Shared User Profile.

Ignore `profile_type: sample` during normal runtime resolution.

### Composition

- Lens only is valid.
- Profile only is valid.
- Lens + Profile is valid.
- Neither is required.

Skills determine analytical capability.

Doppelganger changes perspective and presentation only. Never let it override evidence, canonical rules, validation, or governance.

If a selected file is inaccessible, continue with standard OMA behavior and state that Doppelganger was not fully loaded.

## Step 6 — Apply Governance Proportionally

Read-only analysis:
- answer at the smallest useful scope;
- preserve evidence traceability;
- do not create unnecessary Drafts/Reviews.

Write/canonical-impact tasks:
- validate more strongly;
- preserve versions;
- require explicit approval where governance rules require it.
