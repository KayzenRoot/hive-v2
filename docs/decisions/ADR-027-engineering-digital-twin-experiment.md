# ADR-027 — Engineering Digital Twin as evidence-gated HEDS research

Status: EXPERIMENT REQUIRED
Date: 2026-09-08

## Context
HEDS needs faster executor orientation, stronger change-impact prediction and better review/test targeting, but HIVE must not introduce an unbounded knowledge graph or trust inferred dependencies as canonical truth.

## Decision direction
Define an Engineering Digital Twin (EDT) as a bounded, derived and incrementally reconciled project projection connecting requirements, decisions, modules, symbols, dependencies, contracts, tests, runtime journeys, incidents and evidence.

EDT remains IMPORTANT / EXPERIMENT REQUIRED for HIVE V2. It does not expand frozen NECESSARY scope and cannot block V2 completion unless future evidence proves a minimal portion is required by an existing DoD obligation.

## Constraints
- Git and canonical project documents remain authoritative.
- deterministic evidence precedes inference;
- inferred edges carry provenance/confidence/freshness;
- stale/uncertain twin state widens verification;
- no mandatory new graph database;
- local-first resource budget;
- R21/R22 verification/debugging contracts remain authoritative;
- benchmark promotion is required.

## Evaluation
Measure impact prediction false negatives, orientation time, context reduction, selector divergence, review time, Time-to-Trusted-Merge, architecture drift detection, defect escapes and local resource overhead.

## Consequence
HIVE gains a disciplined path to learn a project's engineering structure without turning a promising idea into premature V2 scope.