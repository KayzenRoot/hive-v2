# Round 21 — Test Intelligence, Selective Verification and Real-Use Quality Engineering

Status: PLANNED / ACCEPTED FOR V2 CANONICAL CONSOLIDATION
Date: 2026-09-08
Owner: Next Labs / HIVE

## Objective

Test every new or changed capability deeply while avoiding indiscriminate full-suite execution after ordinary changes.

Optimization objective: minimize verification wall-clock time, compute and token cost subject to no measurable loss of correctness and no skipped proof obligations.

## Core capabilities

### Feature Verification Contract Registry
Every feature has a machine-readable verification contract: feature ID, requirements, acceptance criteria, owned symbols/modules, dependents, invariants, side effects, resource envelope, required test classes, critical journeys, historical regressions, risk tier and proof freshness rules.

### FIM — Feature Impact Map
Proprietary research direction. Persistent graph connecting feature -> requirement -> symbol -> dependency -> runtime edge -> test -> invariant -> incident -> proof. Deterministic inputs first: Git diff, AST/symbol graph, imports/calls, schema/API/config changes, traces, coverage edges, co-change history and prior failures.

### AITS — Adaptive Impact Test Selector
Proprietary research direction. Chooses the smallest defensible test set using changed symbols, transitive dependents, runtime edges, test coverage, feature contracts, fixtures/config, migrations, concurrency/state edges, security/economic blast radius, co-failures and prior selector misses. Uncertainty widens the suite.

### Verification Confidence Budget
Risk-aware tiers: FAST, IMPACTED, DEEP, FULL and RELEASE. High-risk or low-confidence changes escalate automatically.

### PVR — Proof Validity Reuse
Reuses expensive test/proof results only when fingerprints of code dependencies, tests, fixtures, config, lockfiles, runtime/environment and schema state remain valid.

### SFC — Shadow Full-Suite Calibration
Periodically compares targeted selection with full-suite reality. Any missed regression is recorded as a selector defect, becomes new FIM evidence and tightens future selection.

### RUF — Real-Use Fixture & Journey Layer
Tests actual installation and user/runtime journeys: clean install, first run, upgrade, executor invocation, background execution, visible-conversation behavior, restart/recovery, cancellation, quota exhaustion and degraded dependencies.

### RBG — Resource Behavior Guard
Treats operational behavior as correctness: agent count, visible conversations, retries, token/quota usage, fan-out, CPU/RAM, orphan processes and concurrency envelopes are testable contracts.

### BCR — Behavioral Contract Replay
A production/user-found defect becomes a permanent reproducible regression scenario after correction.

### DGS — Defect Genome Store
Stores defect symptom, first divergence, root cause, fix, escaped test, missing oracle, reproducer, regression lock and affected FIM edges.

### Test Quality Adversary
Uses Round 09 verification techniques such as property-based testing, mutation, fuzzing, differential/model-based and concurrency testing to attack the tests themselves.

### Flake Intelligence
Identifies unstable tests, environmental coupling and timing sensitivity without hiding failures behind unlimited retries.

### Test Scheduling Optimizer
Orders cheap/high-signal tests first, groups reusable setup, uses safe parallelism and stops early only when policy allows.

## Selection policy

A normal change flows through Git diff -> symbol/contract impact -> FIM -> AITS -> verification tier -> selected proof portfolio. Full suite is not the default for every change; it remains mandatory when policy, risk, uncertainty, calibration or release gates require it.

## Mandatory safety rules

- Selector uncertainty can only widen coverage.
- No CRITICAL/HIGH proof obligation may be skipped because of speed.
- Selector false negatives are product defects.
- Full-suite calibration must measure false-negative and over-selection rates.
- Real-use journeys are required before release.
- Resource behavior violations fail verification even when functional outputs are correct.

## Primary metrics

Selected tests / total tests; wall-clock saved; compute saved; selector precision/recall; false-negative rate; proof reuse rate; flake rate; real-use escape rate; mutation score where applicable; regressions caught pre-merge vs post-install.

## Acceptance direction

Round 21 is considered implemented only when machine-readable feature contracts exist, impact-based selection is explainable, selector calibration against full-suite is objective, real-use/resource behavior tests exist, and defect discoveries feed future regression selection.
