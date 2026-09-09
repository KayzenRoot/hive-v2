# PROJECT QUALITY PLAN

Status: TEMPLATE

## Quality objective
Ship the target version with objective evidence, minimal escaped defects and controlled complexity while optimizing Time-to-Trusted-Merge.

## Required test layers
Define applicability for:
- unit;
- integration;
- contract/API/schema;
- property-based;
- mutation/adversarial test quality;
- fuzzing;
- end-to-end/real-use journeys;
- installer/upgrade/restart/recovery;
- performance/resource behavior;
- security;
- migration/data integrity;
- release/full regression.

## Risk tiers
- LOW
- STANDARD
- ELEVATED
- HIGH_ASSURANCE

Document automatic escalation triggers and full-suite/release triggers.

## Modular quality gates
Each module SHOULD declare:
- owner/responsibility;
- public contract;
- allowed dependencies;
- invariants;
- relevant tests;
- resource/performance budgets;
- security/data classification;
- observability expectations.

## Defect policy
Every HIGH/CRITICAL defect blocks advancement. Material defects become regression tests and structured defect-learning records.

## Performance policy
Define measurable budgets for latency, CPU, memory, storage, network, token/API cost and background work where applicable. Performance regressions must be treated as testable behavior, not subjective review comments.

## Complexity policy
Track meaningful complexity delta per Work Order. New dependencies, cross-module coupling, public surface and mutable state require justification.

## Release policy
Release candidate must execute the project-specific broad/full verification portfolio required by the Definition of Done, regardless of ordinary selective-verification optimization.
