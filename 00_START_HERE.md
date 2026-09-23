# Onboarding Mapping Analyst

This package contains the operating structure for an AI-assisted onboarding mapping analyst.

## Architecture at a Glance

![Onboarding Mapping Analyst architecture](docs/assets/architecture.svg)

Start with this diagram before configuring the folders or AI surfaces.

Each user works in their own Gemini, Gemini in Drive, or NotebookLM environment. The shared solution layer is the governed Google Drive content that users read from and write outputs to.

## Core principle

The user should be able to ask a mapping question **from the AI environment they are already using**.

The solution applies one common specialist behavior across Gemini, Gemini in Drive, and NotebookLM.

The execution environment is personal. Governed mappings, evidence, shared personalization assets, and durable outputs live in the shared Drive structure.

## The agent's role

Act as a **Senior Data Systems Analyst specialized in onboarding data mappings**, using strong Business Analysis and Data Analysis practices.

## What happens first

The agent identifies the user's **Task Intent**:

1. **Analyze / Compare / Explain**
2. **Generate Mapping from Intake**
3. **Update Existing Mapping**
4. **Discover / Build New Mapping**

Then it resolves the Mapping Workspace, reasoning depth, relevant Skills, optional Doppelganger, and governance level.

## Mapping Workspace

A workspace can be:
- the **Recommended Shared Workspace**; or
- a **Custom Mapping Workspace** supplied by the user.

Explicit user-provided mapping sources take precedence for that task.

## Doppelganger

Choose one:
- **No Personalization**
- **Private Profile**
- **Import from Shared Personalization Path**

Doppelganger may use:
- one Shared Lens;
- one Personal Analysis Profile;
- both;
- or neither.

The task may select the best-fit Lens. The user/profile controls personal preferences.

The Shared Personalization Library is structured as:

```text
Shared_Personalization_Library/
├── 01_Shared_Lenses/
├── 02_Shared_Profiles/
│   ├── Samples/
│   └── Users/
└── DOPPELGANGER_INDEX.csv
```

Samples are examples only. Real shared profiles appear under `Users/<User_Name>/profile.md` after the user explicitly shares one.

Shared library pointer:

`10_Personalization/SHARED_PERSONALIZATION_LIBRARY.md`

Doppelganger is never required for correct analysis.

## Execution policy

Work where the user is.

Do not force a user to switch tools for routine work.

Where model choice is available:
- use fast/lightweight reasoning for simple deterministic work;
- use advanced reasoning for ambiguity, design, cross-object analysis, or material write impact.

Use NotebookLM when many sources and evidence reconciliation are the main challenge.

## Current Approved Master

The concept is workspace-scoped.

For a governed workspace:

Current Approved Master Index → Mapping Family → Current Approved Version → Approved Master.

Never infer "latest" from filenames or dates.

## Package structure

- `00_Workspace/` — mapping workspace guidance/templates
- `01_Agent_Core/` — behavior, routing, execution and Doppelganger policy
- `02_Skills/` — reusable analytical standards
- `03_Registries/` — governed knowledge templates
- `04_Source_Library/` — source/evidence structure
- `05_Production_Evidence/` — representative evidence
- `06_Master_Mappings/` — Approved/Draft lifecycle
- `07_Analysis_Reviews/` — human review layer
- `08_Interface_Setup/` — Gemini / Drive / Notebook guidance
- `09_Request_Outputs/` — generated outputs
- `10_Personalization/` — Doppelganger, profile template, Shared Lenses and Shared Profiles
