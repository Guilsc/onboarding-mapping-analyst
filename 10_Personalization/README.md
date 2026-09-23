# Personalization Layer / Doppelganger

Doppelganger is the optional personalization layer for the Onboarding Mapping Analyst.

It does **not** change mapping evidence, Approved Masters, canonical rules, versioning, or governance.

## Composition

The agent may combine:

1. Shared OMA Core
2. Relevant Mapping Skills
3. Optional Shared Lens
4. Optional Personal Analysis Profile

Priority:

**Governed mapping truth > Shared Skills > Role Lens > Personal Profile**

## User-facing choices

- **No Personalization**
- **Private Profile**
- **Import from Shared Personalization Path**

## Shared Personalization Library

The shared library contains two main areas:

```text
Shared_Personalization_Library/
├── 01_Shared_Lenses/
└── 02_Shared_Profiles/
    ├── Samples/
    └── Users/
```

Starter Shared Lenses are usable immediately.

Profile Samples are examples only and are never auto-selected.

Real Shared User Profiles appear under `Users/<User_Name>/profile.md` only after a user intentionally shares one.

## Simple resolver rule

- Skills determine analytical capability.
- A task may select one best-fit Shared Lens.
- A user may supply one Personal Profile.
- Lens + Profile may be used together.
- Neither is required.

Do not blend multiple Profiles or multiple Lenses by default.

See `DOPPELGANGER.md` for the complete resolution rules.

## Profile learning

The agent may propose a **Profile Update Candidate** when a repeated useful preference is observed.

Do not silently update a Personal Profile.

Only persist after user confirmation.
