# HEDS — Innovation Roadmap

Status: CANONICAL PROCESS-RESEARCH BACKLOG
Purpose: preserve promising engineering-delivery improvements without silently expanding HIVE V2 product scope.

## Promotion rule
Ideas move from research to default/required behavior only after evidence shows meaningful improvement without unacceptable correctness, security, data-integrity or defect-detection regression.

## Current process baseline
Already adopted/documented:
- HEDS Engineering Delivery System;
- delta-first review and Correction Delta;
- Review Manifest / Evidence Bundle / Change Impact Manifest;
- risk-adaptive review;
- proof/action validity fingerprints concept;
- Time-to-Trusted-Merge primary delivery metric;
- reusable project bootstrap with module, performance, security, environment and freshness contracts;
- Engineering Digital Twin as experiment.

## Research portfolio

| Issue | Capability | Classification | Primary hypothesis |
|---|---|---|---|
| #81 | Repository automation / CI policy readiness | IMPORTANT | path/risk-aware automation lowers idle/manual merge time safely |
| #82 | Balanced quality scorecard | IMPORTANT | multi-metric scorecard prevents speed-only optimization/gaming |
| #83 | Change Isolation / Blast-Radius Budget | EXPERIMENT | bounded WOs reduce orientation, review and regression cost |
| #84 | Pre-Mortem / rollback readiness | IMPORTANT | risk-routed pre-mortems reduce severe escape/recovery time |
| #85 | Deterministic executor navigation index | EXPERIMENT | compact derived index reduces repository-search/context cost |
| #86 | Contract-first executable acceptance | EXPERIMENT | acceptance compiled before coding reduces ambiguity/rework |
| #87 | Independent Review Adversary | EXPERIMENT | adversarial challenge finds high-value defects missed by normal path |
| #88 | Staleness/documentation drift gate | NECESSARY contract / automation pending | stale guidance can be detected deterministically before misrouting work |
| #89 | Failure-budgeted autonomy | IMPORTANT | bounded retry/correction budgets reduce wasted executor time |
| #90 | Performance regression attribution | EXPERIMENT | causal change neighborhood shortens performance debugging |
| #91 | Reproducible environment contract | NECESSARY template | environment fingerprints reduce setup drift/non-reproducible failures |
| #92 | Dependency Change Firewall | IMPORTANT | dependency-specific evidence catches broad hidden blast radius |
| #93 | HEDS benchmark corpus | IMPORTANT | holdout benchmark enables empirical process evolution |
| #94 | Flaky-test containment/trust | IMPORTANT | explicit flake state lowers wasted cycles without false confidence |
| #95 | Dead-code/orphan-contract intelligence | EXPERIMENT | removing proven ballast improves navigation/test/maintenance cost |
| #96 | Change-aware documentation compiler | EXPERIMENT | staged derived-doc proposals reduce drift/manual update time |
| #97 | Observability-by-contract | NECESSARY proportional template | diagnosis improves when runtime evidence is designed with modules |

## Additional candidate technologies
These remain research candidates until dedicated issues/ADRs are justified:

### Change Entropy Index (CEI)
Quantify structural uncertainty of a change from dependency spread, contract churn, ownership crossings, schema effects and historical defect density. Use as one input to risk routing, never as an autonomous truth oracle.

### Evidence Sufficiency Frontier (ESF)
Estimate the smallest evidence set that satisfies the required confidence for a risk tier. Goal: stop verification once sufficient proof exists while preserving conservative escalation under uncertainty.

### Context Waste Profiler (CWP)
Measure which retrieved/sent context was never causally useful to implementation/review outcomes. Feed improvements to Context Signal Budget and navigation/index design.

### Repair Convergence Index (RCI)
Track whether correction attempts are converging on the causal defect. Repeated non-convergent repairs trigger STOP/escalation instead of consuming executor cycles indefinitely.

### Architecture Friction Map (AFM)
Aggregate recurring cross-boundary changes, repeated exceptions and high-coupling WOs to reveal where module boundaries are causing real engineering friction or have eroded.

### Verification Debt Ledger (VDL)
Record temporarily accepted verification gaps with owner, reason, expiry and compensating evidence. Prevent `temporary` skips from becoming invisible permanent debt.

## Benchmark principles
Every promoted optimization should compare against a baseline on representative and holdout scenarios. Measure at minimum:
- correctness/defects found and escaped by severity;
- Time-to-Trusted-Merge;
- executor orientation and implementation time;
- verification/review/correction wall-clock;
- fresh/cached context/token cost;
- selected/full verification ratio and selector misses;
- valid/invalid proof reuse;
- performance/resource impact;
- human/Sol intervention count.

A missed HIGH/CRITICAL defect or unsafe invalid-proof reuse blocks promotion regardless of speed gains.

## Scope protection
This roadmap is process research. It does not make every listed technology a HIVE V2 product feature or release blocker. Product scope remains governed by canonical Scope/DoD/ADRs and the R22 re-freeze.