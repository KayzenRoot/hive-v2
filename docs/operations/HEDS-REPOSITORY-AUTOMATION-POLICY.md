# HEDS — Repository Automation & Merge Policy

Status: CANONICAL POLICY / CONFIGURATION PENDING REAL CI

## Goal
Minimize manual repository operation and idle time while preserving evidence-first promotion.

## Discovery before configuration
Never invent required check names. Before branch/ruleset configuration, inspect actual workflows/check runs on the target repository and record exact stable names.

## Path/risk-aware CI
Prefer cheap deterministic preflight first, then affected verification. Expand automatically for uncertainty/risk. Full/release verification remains mandatory where project policy requires it.

Suggested layers, only when applicable:
1. source/protocol integrity;
2. formatting/lint/static analysis/typecheck;
3. impacted unit/contract tests;
4. integration/real-use/security/resource checks by risk;
5. broader/full/release suite by policy.

## Required merge invariants
- PR identifies WO/base/head/risk;
- required evidence is current for head SHA;
- unresolved HIGH/CRITICAL defect blocks merge;
- required checks for the actual head pass;
- stale proof/cache cannot satisfy a gate;
- checkpoint delta is promoted only after approval;
- merge queue/revalidation must test the state that will actually enter `main` when platform support is used.

## Auto-merge
Allowed only after all objective gates and review policy are satisfied. Auto-merge is a transport optimization, never approval authority.

## CODEOWNERS
Use ownership for sensitive/module boundaries when it improves routing. Do not create ownership theater where no real owner/reviewer exists.

## Dependency/toolchain changes
Route through dependency-change risk policy: inspect lock/transitive delta, security/provenance/license where applicable, compatibility and rollback.

## Artifacts/evidence
Retain enough raw CI/test/benchmark/security evidence to audit a verdict. Retention duration is project-specific; canonical source/history remains in Git, large generated evidence may use external/local artifact storage with immutable references/hashes.

## Merge strategy
Bounded Work Orders SHOULD prefer squash merge when it preserves useful history and repository policy allows. Never rewrite protected canonical history merely for cosmetic cleanliness.

## Current HIVE V2 gate
Actual protections/required checks remain pending #64 because final inherited V1 workflows/check names are not yet frozen. This document authorizes no fabricated check configuration.