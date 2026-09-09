# HIVE V2 — R21/R22 + HEDS Reconciliation Procedure

Status: CANONICAL OPERATING PROCEDURE
Purpose: define the exact post-preservation reconciliation sequence before the R22 architecture/source re-freeze.

## Entry gate

This procedure starts only after `SOURCE_PRESERVATION_STATE = VERIFIED` for `docs/archive/HIVE-MASTER-SOURCE-V2.0-FROZEN.md`.

## Objectives

1. Reconcile R21 Test Intelligence, R22 Debugging/Defect Intelligence and HEDS process decisions against the complete frozen R01-R20 architecture/source definition.
2. Preserve every inherited approved R01-R20 decision unless an explicit post-freeze ADR supersedes it.
3. Detect contradictions, duplicate concepts, naming collisions, scope inflation and missing traceability.
4. Produce a compact canonical Source Pack suitable for execution without replacing the immutable historical sources.

## Required inputs

- exact archived R01-R20 frozen master;
- R21 canonical round specification;
- R22 canonical round specification;
- R21/R22 integrated architecture;
- R21/R22 scope and DoD delta;
- ADR-019 through latest relevant ADR;
- HEDS Engineering Delivery System;
- Review Standard;
- current checkpoint;
- approved scope, requirements, architecture and DoD sources.

## Reconciliation passes

### Pass A — authority and identity
- fingerprint all canonical inputs;
- confirm source hierarchy;
- identify accepted/experimental/important/future states;
- ensure no derived summary is treated as canonical over source material.

### Pass B — requirements and capability coverage
For every R21/R22/HEDS capability, map:
- source round/ADR;
- existing R01-R20 requirement or architecture relationship;
- scope classification;
- DoD implication;
- implementation phase;
- verification obligation.

Any capability lacking a justified mapping remains IMPORTANT/EXPERIMENT/FUTURE and cannot silently enter NECESSARY scope.

### Pass C — contradiction detection
Check explicitly for:
- conflicts with V0.1 inherited decisions;
- conflicts with R01-R20 frozen decisions;
- incompatible storage/canonical-truth semantics;
- duplicated orchestration responsibilities;
- test/debug/review loops that create circular authority;
- HEDS rules that weaken R21/R22 verification requirements;
- new mandatory infrastructure not justified by frozen scope;
- product-vs-process confusion.

### Pass D — architecture compression
Unify overlapping mechanisms where semantics are equivalent, while preserving provenance. Prefer one canonical concept with aliases/references over parallel names that perform the same job.

### Pass E — scope partitioning
Every item must be classified as exactly one of:
- NECESSARY;
- IMPORTANT;
- EXPERIMENT REQUIRED;
- FUTURE / PLUG-IN;
- OUT OF SCOPE.

Only NECESSARY items may block V2 completion.

### Pass F — traceability closure
Ensure machine- and human-readable links exist across:
`requirement -> decision -> architecture -> module/capability -> test/evidence -> DoD`.

## Required outputs

1. reconciliation report with all detected conflicts and resolutions;
2. explicit list of inherited R01-R20 decisions preserved unchanged;
3. explicit list of post-R20 ADRs that add or supersede behavior;
4. capability classification table;
5. Source Pack inputs/fingerprints;
6. unresolved risks, if any;
7. proposed R22 re-freeze verdict.

## Stop conditions

STOP with `CORRECTION REQUIRED` or `BLOCKED` if:
- any HIGH/CRITICAL contradiction remains unresolved;
- a post-R20 decision silently overrides R01-R20;
- a NECESSARY capability lacks requirements/DoD traceability;
- the preserved master cannot be proven to be the verified archived source;
- compacting the Source Pack would discard required semantics or provenance.

Only a clean reconciliation may proceed to Source Pack finalization and re-freeze audit.
