# HIVE V2 — Versioning and Tags Policy

## Purpose

Keep planning, implementation and release history auditable.

## Tag classes

- `v2-arch-r20-frozen`: immutable historical R01-R20 architecture freeze marker after the frozen source is imported.
- `v2-arch-r22-refreeze`: marker created only after R21/R22 reconciliation and APPROVED re-freeze audit.
- `v2.0.0-alpha.N`: implementation integration milestones.
- `v2.0.0-rc.N`: release candidates after DoD closure is near complete.
- `v2.0.0`: only after final DoD and local deployment validation.

## Rules

- Never move or overwrite a published architecture/release tag.
- Never tag a planning state as implementation complete.
- Annotated release tags should reference the approved checkpoint SHA.
- A tag name must correspond to an auditable checkpoint and decision state.
- Experimental benchmarks use non-release refs/artifacts, not release tags.

## Current state

No V2 release tag is authorized yet. `v2-arch-r22-refreeze` becomes eligible only after source consolidation and APPROVED architecture/source audit.
