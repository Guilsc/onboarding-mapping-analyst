# Agent Architecture

The Onboarding Mapping Analyst is easiest to understand as four user-visible architecture blocks, with adaptive reasoning and governance operating inside the core behavior.

![Onboarding Mapping Analyst architecture](../docs/assets/architecture.svg)

## 1. Personal Execution Surfaces

Each user works in their own environment:
- Gemini / Onboarding Mapping Analyst Gem
- Gemini in Google Drive
- NotebookLM

These are execution surfaces, not shared systems of record.

A user's chat or NotebookLM notebook does not need to be shared with other users. NotebookLM is a personal analysis workspace that can consume selected shared Drive files as sources.

## 2. OMA Core Behavior

OMA provides the common specialist behavior across supported surfaces.

Core components:
- Senior Data Systems Analyst identity
- Task Router
- Execution Policy
- Governance
- Output Standards
- 12 modular Mapping Skills
- Doppelganger Policy

High-level decision flow:

Task Intent  
→ Mapping Workspace  
→ Complexity / Consequence  
→ Relevant Skills  
→ Doppelganger (optional)  
→ Governance

Task Intents:
- Analyze / Compare / Explain
- Generate Mapping from Intake
- Update Existing Mapping
- Discover / Build New Mapping

### Adaptive execution

Use the lowest sufficient reasoning tier for the current step.

Preserve valid prior work for small follow-up changes. Retry only the necessary delta unless a change materially invalidates earlier conclusions.

Escalate reasoning depth, source scope, or execution surface only when required by ambiguity, evidence conflict, validation failure, cross-system complexity, or write consequence.

## 3. Shared Governed Drive

The shared layer is the files and governed outputs, not the user's execution environment.

### Shared Mapping Workspace

Contains durable mapping knowledge and working artifacts such as:
- Source Library
- Production Evidence
- Master Mappings
  - Approved
  - Drafts
- Registries
- Analysis Reviews
- Current Approved Master Index
- Request Outputs

### Shared Personalization Library

Contains reusable Doppelganger assets:
- Shared Lenses
  - Business Analyst
  - Operations
  - QA
  - Developer / Integration
  - PM / DM
- Shared Profiles
  - Samples
  - Users

A Personal Profile may remain private. A real profile appears in the shared library only when the user intentionally shares it.

## 4. Default Output Behavior

OMA resolves the default output destination from the active Mapping Workspace.

### Recommended Shared Workspace

Default:

`Shared Workspace → Request Outputs/`

### Custom Mapping Workspace

Default:

`Custom Workspace → <Custom Workspace>/Outputs/`

The user may override the destination when supported.

If the current execution surface cannot persist directly to the resolved destination, return the artifact and preserve the intended destination so it can be written without changing the analysis.

## Source Connection Model

**Behavior comes from OMA instructions. Evidence comes from sources selected in the current execution surface.**

Do not assume the OMA Gem, Gemini in Drive, or NotebookLM automatically has the entire Shared Mapping Workspace in context.

Use only the source controls available in the current surface.

## Doppelganger

Doppelganger is optional.

It may use:
- zero or one Role Lens;
- zero or one Personal Analysis Profile.

The task may determine the best-fit Lens. The Personal Profile represents user preferences.

Skills provide analytical capability. Doppelganger changes perspective and presentation only.

It never changes:
- mapping evidence;
- Approved Master selection;
- canonical rules;
- validation;
- governance.

## Operating boundary

Personal execution surfaces may come and go.

The durable solution is the combination of:
- OMA operating behavior;
- governed shared Drive sources;
- governed shared outputs;
- optional shared personalization assets.

The model itself, a user's chat, and a user's NotebookLM notebook are not permanent organizational memory.
