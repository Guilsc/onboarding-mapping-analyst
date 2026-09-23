# Mapping Workspace

The Onboarding Mapping Analyst is specialized for **data-mapping work**, but it is not locked to one source library.

A **Mapping Workspace** tells the agent which mapping sources, governed Masters, evidence, and outputs belong to the current analysis.

## Workspace modes

### 1. Recommended Shared Workspace

The team's governed mapping library.

Use it when the user wants to work with the organization's current onboarding mappings and Approved Masters.

The shared workspace should contain:
- managed historical sources;
- production evidence;
- governed registries;
- Approved and Draft Master Mappings;
- a Current Approved Master Index;
- request outputs.

The actual shared Drive link is configured in:

`SHARED_MAPPING_WORKSPACE.md`

### 2. Custom Mapping Workspace

A user may point the agent to another folder or set of mapping files.

The agent applies the same mapping Skills, but keeps that workspace logically isolated from the Recommended Shared Workspace.

A custom workspace may start with:
- only historical mappings;
- mapping files plus Salesforce/Workfront examples;
- an existing Master Mapping;
- or a complete governed workspace.

The agent must not merge a custom workspace into the shared workspace automatically.

## Workspace selection

Use this order:

1. If the user explicitly provides a source folder/files, use those as the current Custom Mapping Workspace.
2. Otherwise, use the Recommended Shared Workspace when it is configured and accessible.
3. If neither is available, ask the user for a mapping source.

## Scope guardrail

The agent remains specialized in mapping work.

If the supplied files do not appear to represent data mappings, mapping evidence, Salesforce/Workfront mapping behavior, or related onboarding integration context, explain that the source set is outside the supported scope rather than turning the solution into a generic project agent.

## Current Approved Master

The Current Approved Master concept is **workspace-scoped**, not global.

A governed workspace can maintain its own Current Approved Master Index.

For the Recommended Shared Workspace, that index determines the current canonical version.

For a new Custom Mapping Workspace, there may be no Approved Master yet. The agent can run discovery and propose a new V1 through the normal Analysis Review and approval lifecycle.

## Versioning behavior

The workspace uses two layers of versioning:

- **Google native file history** for normal edits and recovery while a Master is still a Draft.
- **OMA logical versions** for governed states such as V1 Approved, V2 Draft, and V2 Approved.

A Draft may be edited repeatedly without creating V2.1, V2.2, or separate copies for each edit.

When a Draft is explicitly approved, promote that same logical version into the Approved location/state when possible and update the Current Approved Master Index.

Once Approved, the artifact is immutable. Any later canonical change begins a new logical Draft version.

Never use Drive modified date or native revision history to resolve the Current Approved Master.

## Outputs

Default behavior:
- Shared Workspace → use the workspace's configured Request Outputs location.
- Custom Workspace → use an `Outputs/` location inside the custom workspace when writable.
- If no writable location exists → return the artifact to the user and state that it has not been persisted.

A user may explicitly request another output destination when the environment supports it.
