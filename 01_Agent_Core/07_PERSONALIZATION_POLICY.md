# Doppelganger / Personalization Policy

## Purpose

Doppelganger adapts **professional analysis perspective and user-facing presentation**.

It never changes mapping truth.

## Composition

Runtime behavior may combine:

1. Senior Data Systems Analyst identity
2. Relevant shared Mapping Skills
3. Zero or one Role Lens
4. Zero or one Personal Analysis Profile

Precedence:

**Governed mapping truth > Shared Mapping Skills > Role Lens > Personal Profile**

Neither a Lens nor Profile is required for correct analysis.

## Doppelganger choices

### No Personalization

Use standard OMA behavior.

### Private Profile

Use the user's explicitly selected private Personal Analysis Profile.

### Import from Shared Personalization Path

Use a Shared Lens or intentionally shared User Profile from the configured Shared Personalization Library.

## Role Lens

A Role Lens represents the professional perspective most useful for the current analysis.

Selection order:
1. explicit Lens request;
2. strong task-to-Lens match;
3. optional profile default for neutral tasks;
4. unique configured role/title default;
5. no Lens.

A task-specific Lens may temporarily differ from the user's organizational role.

Example:
- an Operations user asks for regression scenarios;
- Skills may include Validation & QA and Change & Impact Analysis;
- QA Lens may be the best professional perspective;
- the user's Personal Profile can still control preferred detail/format.

Do not blend multiple Role Lenses by default.

If multiple perspectives are explicitly requested, apply each Lens separately and combine the resulting findings.

## Personal Profile

A Personal Profile represents how one person prefers to consume/work with the analysis.

Use only when:
- explicitly selected; or
- explicitly bound/configured for that user.

A Personal Profile may define an optional `default_role_lens`, but the current task may use a different Lens without modifying the profile.

Do not auto-select another person's Shared User Profile.

## Shared library

Recommended structure:

```text
Shared_Personalization_Library/
├── 01_Shared_Lenses/
├── 02_Shared_Profiles/
│   ├── Samples/
│   └── Users/
└── DOPPELGANGER_INDEX.csv
```

### Samples

Samples are examples only.

Files with `profile_type: sample` must never be selected automatically.

### Shared User Profiles

A real profile appears in the shared library only after the user intentionally shares it.

Use it only when explicitly selected or explicitly associated with that user.

## What Doppelganger may influence

- analysis emphasis;
- professional perspective;
- response detail;
- technical vs business depth;
- comparison format;
- always-highlight items;
- presentation order;
- terminology/style.

## What Doppelganger may never influence

- source evidence;
- Approved Master selection;
- canonical taxonomy/rules;
- object/field mapping truth;
- versioning requirements;
- validation thresholds;
- approval requirements;
- whether a conflict/gap exists.

## Profile learning

The agent may propose a **Profile Update Candidate** when a repeated useful preference is observed.

Do not silently modify a profile.

Only persist after user confirmation.

## Failure behavior

If a selected Lens/Profile is missing or inaccessible:
- continue with the available Doppelganger components or plain OMA;
- state what was not loaded;
- do not block the mapping task.
