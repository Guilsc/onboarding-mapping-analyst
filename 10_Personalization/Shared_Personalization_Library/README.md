# Shared Personalization Library

This folder mirrors the recommended shared Drive library structure for Doppelganger assets.

## Structure

```text
Shared_Personalization_Library/
├── 01_Shared_Lenses/
├── 02_Shared_Profiles/
│   ├── Samples/
│   └── Users/
└── DOPPELGANGER_INDEX_TEMPLATE.csv
```

## Shared Lenses

Reusable professional perspectives that may be selected explicitly or, when the task strongly implies one perspective, selected automatically.

## Shared Profiles

### Samples

Examples only. They teach users how a Personal Analysis Profile can be structured.

Samples must never be selected automatically during normal Doppelganger resolution.

### Users

Profiles intentionally shared by real users.

Each user gets a folder:

```text
Users/
└── <User_Name>/
    └── profile.md
```

A Shared User Profile is used only when explicitly selected or explicitly bound to that user. Never infer or auto-select another person's profile.

## Core rule

Doppelganger may use:
- zero or one Shared Lens;
- zero or one Private/Shared Personal Profile.

Skills determine analytical capability. Doppelganger changes emphasis and presentation only.
