# ADR-025 — Adopt HIVE Engineering Delivery System (HEDS)

Status: ACCEPTED
Date: 2026-09-08

## Context
HIVE and future projects need higher software quality with lower executor/reviewer time, less context waste, fewer repeated tests/builds, stronger modularity and faster correction cycles.

## Decision
Adopt HEDS as the default engineering delivery model for HIVE V2 implementation and future new projects.

HEDS optimizes Time-to-Trusted-Merge and includes:
- machine-readable Review Manifest;
- Context Capsules;
- proof/action fingerprint reuse with validity gates;
- Correction Delta Protocol;
- risk-adaptive review;
- Defect Learning Loop;
- Trusted Merge Queue when supported;
- Work Intent Graph;
- Context Signal Budget;
- Proof Decay Index;
- Review Attention Router;
- Regression Escape Radar;
- Modular Boundary Sentinel;
- Complexity Budget Gate;
- Rework Cost Ledger;
- Acceptance Evidence Compiler;
- Project Bootstrap Contract Compiler direction.

## Constraints
- HEDS does not bypass approved scope/architecture/governance.
- uncertainty expands verification;
- high-risk areas retain stronger/full checks;
- cached evidence is reusable only with valid fingerprints;
- HIVE V2 implementation remains blocked until its existing source re-freeze gate is approved.

## Consequences
Positive: faster orientation/review, less redundant context/work, stronger traceability, learning from defects, more consistent project starts.

Cost: additional metadata/contracts and initial automation work. This cost is accepted because it is amortized across every subsequent Work Order/project.
