# Source Connection Model

The Onboarding Mapping Analyst uses the same specialist behavior across supported Google AI surfaces, while each user works in their own execution environment.

There is no requirement for a shared Gemini conversation or shared NotebookLM notebook.

## Core principle

**Behavior comes from OMA instructions. Evidence comes from the sources selected in the current surface.**

The shared component is the governed Drive content that users read from and write outputs to.

## What is personal vs shared

### Personal execution

Each user may have their own:
- Gemini session;
- OMA Gem usage;
- Gemini in Drive session;
- NotebookLM notebook;
- private Personal Profile.

### Shared governed content

The team shares:
- mapping sources;
- Approved Masters and Drafts;
- Production Evidence;
- Registries;
- Analysis Reviews;
- Shared Lenses;
- intentionally shared Personal Profiles;
- Request Outputs.

## Gemini / OMA Gem

Use the OMA Gem for specialist behavior.

The Gem provides:
- identity;
- routing;
- execution policy;
- Skills policy;
- governance;
- Doppelganger behavior.

Relevant Drive sources still need to be available/selected through the current Gemini experience.

Do not duplicate the entire Shared Mapping Workspace into Gem knowledge and do not assume the Gem automatically sees every shared file.

## Gemini in Google Drive

Gemini in Drive is the closest execution surface to the live shared files.

Recommended pattern:
1. work from the relevant Drive area;
2. use Ask Gemini / the OMA Gem when available;
3. select the relevant files, folders, or supported Drive context;
4. ask naturally;
5. write governed outputs to the resolved workspace destination when supported.

The Gem provides OMA behavior. Drive provides the live shared file context.

## NotebookLM

NotebookLM is a **personal analytical workspace**, not a shared solution layer.

Each user may create or use their own notebook and add the shared Drive files relevant to the task.

Recommended pattern:
1. create/open the user's NotebookLM notebook;
2. add the relevant mapping files from the Shared Mapping Workspace;
3. apply OMA operating guidance/instructions available to that notebook;
4. perform source-grounded analysis;
5. route durable outputs back to the active Mapping Workspace.

Do not treat NotebookLM as the organizational system of record.

Do not require users to share notebooks with one another.

A NotebookLM notebook should not be treated as a live mount of an entire Drive folder. New files in Drive are not assumed to become notebook sources automatically.

## Default output destination

For the Recommended Shared Workspace:

`Shared Workspace → Request Outputs/`

For a Custom Mapping Workspace:

`Custom Workspace → <Custom Workspace>/Outputs/`

The destination rule is part of OMA behavior and does not depend on users sharing their execution workspace.

If the current surface cannot write directly to the destination, return the generated artifact and preserve the intended destination.

## Recommended architecture

```text
        PERSONAL EXECUTION
┌─────────────────────────────┐
│ Gemini / OMA Gem            │
│ Gemini in Google Drive      │
│ NotebookLM                  │
│ + OMA behavior              │
│ + optional Doppelganger     │
└──────────────┬──────────────┘
               │
        read / analyze / write
               │
               ▼
       SHARED GOVERNED DRIVE
┌─────────────────────────────┐
│ Mapping sources             │
│ Approved Masters / Drafts   │
│ Evidence / Registries       │
│ Shared personalization      │
│ Request Outputs             │
└─────────────────────────────┘
```

## Practical rule

Stay in the user's current execution surface when it can reliably complete the task.

Select/add the source files required for that task.

Use NotebookLM when a larger source corpus benefits from source-grounded analysis.

No interface or automatic navigation to shared folders is required in the current version.
