# HIVE — Engineering Digital Twin (EDT)

Status: IMPORTANT / EXPERIMENT REQUIRED
Purpose: maintain a compact, evidence-backed structural twin of a software project so HIVE can predict and verify change impact without repeatedly scanning the entire repository.

## 1. Problem

Large repositories make executors and reviewers spend time rediscovering relationships already knowable from deterministic project evidence. File lists alone are insufficient because a change can propagate through symbols, contracts, tests, runtime behavior, requirements and prior incidents.

## 2. Concept

The Engineering Digital Twin is a continuously reconcilable projection connecting:

`requirement -> ADR -> module -> symbol -> dependency -> contract -> test -> runtime journey -> incident -> evidence -> performance/resource signal`

It is a derived intelligence layer. It NEVER replaces Git, canonical documentation, PostgreSQL durable truth or approved governance.

## 3. Design rules

1. Deterministic evidence first: Git, AST, dependency graphs, manifests, tests, schemas, runtime traces and hashes outrank LLM inference.
2. Every inferred edge declares provenance, confidence and freshness.
3. Unknown or stale regions increase verification rather than suppress it.
4. The twin is incrementally updated from deltas instead of rebuilt indiscriminately.
5. Project isolation is mandatory.
6. Canonical source remains reconstructible without the twin.
7. The twin must remain bounded enough for local-first operation.
8. Progressive disclosure is mandatory: executors receive relevant projections, not the complete graph.

## 4. Core projections

### Intent projection
Work Order, acceptance criteria, requirements, ADRs and explicit out-of-scope boundaries.

### Code projection
Modules, files, symbols, signatures, imports, calls, ownership and dependency edges.

### Verification projection
Tests, fixtures, properties, contracts, journeys, selectors, proof fingerprints and coverage/impact relationships.

### Operational projection
Processes, services, agent fan-out, queues, resource usage, token/quota effects, persistence effects and runtime traces where observable.

### Defect projection
Symptoms, first divergence, root cause, reproducer, repair, regression lock and recurrence history.

### Economics projection
Execution time, context volume, test/build cost, cache reuse, correction cycles and Time-to-Trusted-Merge.

## 5. Proprietary HEDS mechanisms

### Change Forecast Vector (CFV)
Before execution, produce an explainable prediction of likely impacted modules, contracts, tests and risk surfaces.

### Predicted-vs-Observed Impact Delta (POID)
After execution, compare forecast impact against actual changed symbols, tests, runtime evidence and defects. Large unexplained deltas trigger investigation and teach the impact model.

### Twin Confidence Envelope (TCE)
Assign confidence/freshness to each relevant projection. Low confidence widens context and verification automatically.

### Architecture Drift Pulse (ADP)
Measure newly introduced cycles, forbidden edges, fan-in/fan-out jumps, ownership leakage and contract bypasses relative to approved architecture.

### Verification Blind-Spot Index (VBI)
Rank important code/behavior regions with weak or stale evidence, repeated selector misses, escaped regressions or missing real-use journeys.

### Executor Orientation Score (EOS)
Measure how much repository exploration an executor needed before productive implementation. The target is to reduce unnecessary discovery without hiding necessary context.

## 6. HEDS integration

The EDT feeds:
- Work Intent Graph;
- Context Capsule generation;
- Review Manifest;
- Feature Impact Map;
- Adaptive Impact Test Selector;
- Review Attention Router;
- Modular Boundary Sentinel;
- Regression Escape Radar;
- Defect Causality Fabric;
- Acceptance Evidence Compiler.

R21/R22 remain the testing/debugging authority. EDT is a shared derived projection that may improve those mechanisms after benchmark validation.

## 7. Safety fallbacks

EDT MUST NOT be trusted when:
- repository fingerprint is stale;
- parser/dependency extraction failed;
- generated/dynamic code cannot be resolved reliably;
- runtime behavior contradicts static impact;
- selector calibration detects a miss;
- a core contract/toolchain/schema changed outside the modeled graph.

Fallback: expand deterministic discovery, context and verification up to repo-wide/full-suite when policy requires.

## 8. Promotion evidence

Before promotion from EXPERIMENT REQUIRED, benchmark representative projects and measure:
- impact prediction precision/recall;
- critical false-negative rate;
- executor orientation time;
- context tokens/bytes sent;
- selected verification vs full-suite divergence;
- review wall-clock;
- Time-to-Trusted-Merge;
- architecture drift detection;
- defect escape rate;
- incremental update cost;
- local CPU/RAM/storage overhead.

No performance gain is accepted if it produces a material correctness or safety regression.

## 9. Scope

For HIVE V2: IMPORTANT / EXPERIMENT REQUIRED unless later evidence proves a minimal EDT capability is required to satisfy an already-frozen NECESSARY requirement.

For future new projects: template-compatible research capability, disabled by default until implementation and benchmark promotion.