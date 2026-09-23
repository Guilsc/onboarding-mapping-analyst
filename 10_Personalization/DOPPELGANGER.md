# Doppelganger

**Doppelganger** is the optional personalization layer for the Onboarding Mapping Analyst.

It changes how mapping analysis is emphasized and presented. It never changes mapping truth.

## Choices

### 1. No Personalization

Use standard OMA behavior.

### 2. Private Profile

Use the user's explicitly selected private Personal Analysis Profile.

### 3. Import from Shared Personalization Path

Use a Shared Lens or Shared User Profile from the configured Shared Personalization Library.

Shared library pointer:

`SHARED_PERSONALIZATION_LIBRARY.md`

## Active composition

A Doppelganger may contain:

- zero or one Role Lens; and
- zero or one Personal Analysis Profile.

Do not combine multiple Personal Profiles.

Do not combine multiple Role Lenses by default.

When both are active:
- Role Lens defines the professional analysis perspective.
- Personal Profile refines detail, comparison format, likes, terminology, and presentation.

## Lens resolution

Use this simple order:

1. Explicitly requested/selected Lens.
2. If the task strongly and unambiguously calls for one Shared Lens, use that Lens.
3. If the task is neutral, use the profile's optional default Role Lens when available.
4. Otherwise use a unique role/title default only when clearly configured.
5. Otherwise use no Lens.

Examples:
- "Analyze regression scenarios" → QA Lens, when available.
- "Show operational/manual impact" → Operations Lens, when available.
- "Trace source paths and integration dependencies" → Developer / Integration Lens, when available.
- Generic "compare these mappings" → no Lens unless a default is configured.

If multiple perspectives are explicitly requested, run the relevant Lenses separately and combine findings. Do not merge the Lens instructions into one blended persona.

## Profile resolution

Use a Personal Profile when:
1. the user explicitly selects it; or
2. it is explicitly bound/configured for that user.

Do not auto-select another person's Shared User Profile from task content, role, title, or name similarity.

Shared Profile Samples are examples only and must never participate in normal resolution.

## Important separation

**Task determines Skills and may determine the best-fit Role Lens.**

**User preference determines the Personal Profile.**

Skills provide analytical capability. Doppelganger changes perspective and presentation.

A task must still work correctly with no Lens and no Profile.

## Shared library structure

```text
Shared_Personalization_Library/
├── 01_Shared_Lenses/
├── 02_Shared_Profiles/
│   ├── Samples/
│   └── Users/
└── DOPPELGANGER_INDEX_TEMPLATE.csv
```

## Boundaries

Doppelganger may affect:
- analysis emphasis;
- detail;
- comparison format;
- always-highlight items;
- presentation order;
- terminology/style.

Doppelganger may never affect:
- evidence;
- Approved Master selection;
- canonical taxonomy/rules;
- mapping truth;
- validation thresholds;
- versioning;
- approvals/governance.
