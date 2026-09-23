# Shared Personalization Library

This file holds the pointer to the shared Google Drive location used by Doppelganger.

## Shared Personalization Library Path

Replace this placeholder with the shared Drive folder/path/link:

`[SHARED_PERSONALIZATION_LIBRARY_PATH]`

## Recommended structure

```text
Shared_Personalization_Library/
├── 01_Shared_Lenses/
├── 02_Shared_Profiles/
│   ├── Samples/
│   └── Users/
└── DOPPELGANGER_INDEX.csv
```

The package includes a matching template under:

`10_Personalization/Shared_Personalization_Library/`

## 01_Shared_Lenses

Reusable professional perspectives.

A Lens may be:
- explicitly selected;
- selected automatically when the task strongly and unambiguously matches that professional perspective;
- used as an optional configured default for a neutral task.

Do not blend multiple Lenses by default.

## 02_Shared_Profiles/Samples

Examples only.

Samples must use `profile_type: sample` and are ignored during normal Doppelganger resolution.

## 02_Shared_Profiles/Users

Profiles intentionally shared by real users.

Recommended structure:

```text
Users/
└── <User_Name>/
    └── profile.md
```

A Shared User Profile is used only when explicitly selected or explicitly bound to that user.

Never auto-select another person's profile.

## Boundaries

Shared personalization may adapt:
- analysis emphasis;
- response detail;
- comparison format;
- presentation;
- role-relevant focus.

It may never override:
- source evidence;
- Approved Masters;
- canonical mapping rules;
- validation;
- approval/governance.
