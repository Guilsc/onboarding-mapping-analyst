# Acceptance Tests

## Test A — Initial Master Discovery

Prompt:
"Analyze the current historical mapping library and begin discovering the first canonical Master Mapping."

Expected:
- route = Build / Discover
- independent Source Discovery happens before ROVO hypothesis comparison
- candidate mapping families are discovered from content
- Salesforce is analyzed progressively by object
- Workfront evidence is detected when relevant
- no Master is generated prematurely
- full Analysis Review is produced
- explicit BA approval is required
- new Draft Master is created
- final Salesforce output consolidates all objects into one tab

## Test B — Update Master

Prompt:
"Field X will now come from the API instead of being set by MuleSoft."

Expected:
- route = Update Master
- current Approved rule located
- shared/dependent impacts checked
- Workfront impact checked
- impact/risk review produced
- Approved version remains untouched
- next Draft proposed
- explicit BA approval required
- version/change log updated after approval

## Test C — Request-Specific Generation

Prompt:
"Here is the onboarding intake. Generate the mapping."

Expected:
- route = Generate Mapping for Request
- request classified against Approved taxonomy/Masters
- only material missing questions asked
- closest Approved Master selected
- conditions applied
- Sample populated from supplied data
- Workfront applicability evaluated
- request-specific output generated
- new reusable behavior flagged
- Master not changed automatically

## Test D — Correction / Learning

Prompt:
"No, that field is set by Salesforce for this flow, not MuleSoft."

Expected:
- correction acknowledged
- evidence rechecked if needed
- Learning Candidate created
- affected rule/decision identified
- Approved Master impact assessed
- no silent canonical overwrite
- validated correction persisted for future users
