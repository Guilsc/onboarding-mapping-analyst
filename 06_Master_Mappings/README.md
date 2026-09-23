# Master Mappings

Canonical mapping artifacts are governed within a Mapping Workspace.

## Structure

- `Approved/` — immutable approved versions
- `Drafts/` — proposed future versions under review

## Current-version rule

A governed workspace may maintain a Current Approved Master Index.

Normal request generation uses the version referenced by that workspace's index.

A new Custom Mapping Workspace may have no Approved Master yet. In that case, use Build / Discover rather than forcing a match to the Recommended Shared Workspace.

## Versioning model

OMA uses logical mapping versions on top of Google native file history.

- Google native version history tracks working edits inside a Draft.
- OMA logical versions track governed business states such as V1 Approved, V2 Draft, and V2 Approved.
- Do not create a new logical OMA version for every small file edit.
- Do not use Google modified date or native revision history to determine which Master is current.

## Lifecycle

No Master  
→ discovery  
→ Analysis Review  
→ V1 Draft  
→ normal Draft edits tracked by Google native history  
→ validation  
→ explicit approval  
→ promote V1 to Approved

Later:

V1 Approved  
→ change analysis  
→ create V2 Draft from V1 Approved  
→ normal Draft edits tracked by Google native history  
→ validation  
→ explicit approval  
→ promote V2 to Approved  
→ Current Approved Master Index points to V2  
→ V1 remains retained as historical/superseded

The Draft-to-Approved transition is a governance-state promotion of the same logical version. Avoid creating a duplicate second file solely to represent approval when the governed artifact can be promoted/moved safely.

Approved versions are never edited in place.

Any future canonical change starts a new Draft version, for example V3 Draft from V2 Approved.

## Cross-workspace rule

A Master created in a Custom Workspace does not become part of the Recommended Shared Workspace automatically.

Any incorporation into shared canonical knowledge requires separate governed review.
