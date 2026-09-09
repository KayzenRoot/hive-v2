# HIVE — Engineering Delivery System (HEDS)

Status: CANONICAL OPERATING STANDARD
Purpose: define a reusable, evidence-driven software construction system for HIVE V2 and future projects.

## 1. Objective

HEDS optimizes for **Time-to-Trusted-Merge**, not raw coding speed.

A change is fast only when it reaches an objectively trustworthy merge with minimal rework, minimal unnecessary context, minimal redundant test/build execution, and no unacceptable quality loss.

Primary outcomes:
- fewer escaped defects;
- faster executor orientation and implementation;
- faster reviews;
- modular repository organization;
- lower token/context waste;
- less repeated build/test work;
- stronger traceability;
- easier recovery across chats/agents;
- predictable project completion.

## 2. Construction pipeline

SOURCE LOCK
→ WORK ORDER
→ CONTEXT PACK
→ IMPLEMENT
→ CHANGE IMPACT MANIFEST
→ RISK ROUTING
→ SELECTED VERIFICATION
→ EVIDENCE BUNDLE
→ DELTA-FIRST REVIEW
→ VERIFIED CORRECTION LOOP if needed
→ TRUSTED MERGE
→ CHECKPOINT UPDATE
→ LEARNING FEEDBACK

No stage may silently substitute conversational memory for repository evidence.

## 3. Core technologies

### 3.1 Review Manifest (RM)
Machine-readable review entrypoint. It contains immutable identity, scope, impact, risk, evidence and verification references.

A reviewer should normally begin with the Review Manifest instead of scanning the repository.

### 3.2 Context Capsule (CC)
A minimal executor/reviewer context package generated from canonical sources and the current Work Order.

It includes only:
- current checkpoint pointer;
- relevant decisions;
- impacted requirements/DoD;
- affected architecture contracts;
- changed or required symbols/files;
- relevant tests/incidents;
- explicit exclusions.

The capsule has a deterministic fingerprint. Unchanged sources are referenced by fingerprint instead of retransmitted wholesale where tooling permits.

### 3.3 Proof Cache (PC)
Reusable evidence indexed by validity fingerprint.

A proof is reusable only when every declared validity input remains unchanged, including code, tests, fixtures, config, lockfiles, schemas, runtime/toolchain and environment assumptions applicable to that proof.

### 3.4 Correction Delta Protocol (CDP)
When a review verdict is CORRECTION REQUIRED, the next review begins from:
- last rejected head SHA;
- corrective head SHA;
- unresolved findings;
- invalidated proof fingerprints;
- newly added evidence.

Prior valid evidence is retained. Unchanged accepted areas are not re-reviewed from zero.

### 3.5 Risk-Adaptive Review Router (RARR)
Every Work Order and PR is assigned one of:
- LOW
- STANDARD
- ELEVATED
- HIGH_ASSURANCE

Risk controls verification depth, independent checks, full-suite triggers, security review, runtime journeys and proof reuse eligibility.

### 3.6 Defect Learning Loop (DLL)
Every escaped or material pre-merge defect becomes structured learning:
change → symptom → root cause → why existing checks missed it → permanent regression → selector/review rule update → defect-memory record.

### 3.7 Trusted Merge Queue (TMQ)
When repository capabilities permit, approved PRs enter a merge queue after required checks. The queue revalidates the exact integration state before merge so individually green branches do not silently create an unverified combined state.

### 3.8 Action Fingerprint Cache (AFC)
Build/test/lint/typecheck actions may reuse outputs when their declared inputs, toolchain and environment fingerprints are identical.

This is conceptually compatible with content-addressed/action caching systems. Cache reuse is evidence, not an assumption: cache key provenance must be inspectable.

### 3.9 Time-to-Trusted-Merge (TTTM)
Primary delivery performance metric:
executor start → objectively trusted merge.

Submetrics:
- executor orientation time;
- implementation time;
- time-to-first-failure;
- verification wall-clock;
- review wall-clock;
- correction cycles;
- context tokens;
- redundant work avoided;
- escaped defects.

## 4. New proprietary HIVE delivery concepts

### HEDS-P01 — Work Intent Graph (WIG)
Graph linking Work Order intent to requirements, ADRs, modules, symbols, tests, runtime journeys and acceptance evidence. It is narrower than the full code graph and optimized for the current increment.

### HEDS-P02 — Context Signal Budget (CSB)
Every executor/reviewer context package has a token/file budget. Context expands only when unresolved uncertainty or risk justifies it. Measure useful canonical references versus total transmitted context.

### HEDS-P03 — Proof Decay Index (PDI)
Scores how likely prior evidence is to have become stale based on changed validity inputs, dependency age, runtime changes, flaky history and prior selector misses. A high score invalidates reuse or escalates verification.

### HEDS-P04 — Review Attention Router (RAR)
Ranks changed areas by expected defect consequence × uncertainty × novelty × historical defect density × contract centrality. Sol reviews highest information-value surfaces first.

### HEDS-P05 — Regression Escape Radar (RER)
Combines defect history, selector calibration, runtime anomalies and change topology to identify areas where tests historically underperform. These areas receive stronger verification until confidence recovers.

### HEDS-P06 — Modular Boundary Sentinel (MBS)
Checks changes for architecture-boundary drift: forbidden dependencies, cross-module leakage, circular dependencies, oversized modules, unstable public contracts and ownership ambiguity.

### HEDS-P07 — Complexity Budget Gate (CBG)
Tracks incremental structural complexity per Work Order. A change that introduces materially more code/dependencies/state paths than necessary must justify the complexity against approved requirements.

### HEDS-P08 — Rework Cost Ledger (RCL)
Records why review cycles repeat: unclear prompt, missing source, architecture ambiguity, weak test, executor error, stale environment, flaky CI, reviewer false positive. This converts delay into process-improvement data.

### HEDS-P09 — Acceptance Evidence Compiler (AEC)
Compiles machine-readable acceptance criteria into an evidence checklist and expected proof artifacts before implementation starts, reducing ambiguity for Codex/Cursor.

### HEDS-P10 — Project Bootstrap Contract Compiler (PBCC)
A new project begins from a template manifest that generates the canonical documentation skeleton, governance, review contracts, CI/test gates, checkpoint, Work Order conventions and project-specific placeholders.

## 5. Executor acceleration rules

Executors MUST receive an explicit Work Order and should receive a Context Capsule whenever available.

Executors MUST NOT be told to broadly inspect the entire repository when deterministic impact/source maps already identify the relevant surface. They may expand inspection if evidence reveals uncertainty.

Prompt instructions should state:
- what to read first;
- what is relevant;
- what is explicitly out of scope;
- what contracts cannot change;
- what tests/evidence are expected;
- what STOP CONDITION applies.

The user-facing prompt artifact remains PDF-only under the Response and Delivery Standard.

## 6. Review acceleration rules

Default review order:
1. Review Manifest identity.
2. Work Intent Graph / impact manifest.
3. risk tier and changed contracts.
4. selected verification and proof validity.
5. changed symbols/patches.
6. runtime/resource behavior when applicable.
7. architecture/security/data integrity.
8. broader repository expansion only if justified.

## 7. Quality guardrails

Speed optimizations fail closed.

Run or escalate toward fuller verification when:
- impact graph is stale or incomplete;
- dependency/config/toolchain change has unknown blast radius;
- selector confidence is below policy;
- a prior selector miss affected the area;
- core contracts/security/persistence/migrations change;
- release candidate/final release gates require it;
- HIGH_ASSURANCE policy requires independent verification.

## 8. Applicability

HIVE V2 uses HEDS during its implementation program after the V2 source re-freeze authorizes construction.

All new projects SHOULD bootstrap from the HEDS project template unless a project-specific ADR explicitly chooses a different process.
