# Round 22 — Debugging, Defect Localization and Verified Repair Intelligence

Status: PLANNED / ACCEPTED FOR V2 CANONICAL CONSOLIDATION
Date: 2026-09-08
Owner: Next Labs / HIVE

## Objective

Reduce time from observed symptom to reproducible root cause to verified repair, while turning every escaped defect into durable test and diagnostic knowledge.

## Core capabilities

### DCF — Defect Causality Fabric
Proprietary research direction. Builds a causal graph across symptoms, events, agents, tool calls, code symbols, state transitions, database activity, configuration and recent changes.

### FDL — First Divergence Locator
Locates the earliest point where actual execution diverged from an expected invariant, trajectory or state transition instead of debugging only the final stack trace.

### IRC — Incident Replay Capsule
Captures the minimum trusted incident state needed for reproducibility: code/base SHA, configuration fingerprints, inputs, relevant external responses, event trace, state snapshots and nondeterminism metadata.

### MRE — Minimal Reproducer Engine
Systematically reduces a failing incident to the smallest scenario that preserves the failure, lowering diagnosis and regression-test cost.

### GDC — Git-Defect Correlator
Ranks commits, diffs and symbols using recency, ownership, dependency paths, co-change history, failing evidence and historical defect associations.

### Agent Trajectory Debugger
Makes agent systems observable as execution trees: parent/child agents, tool calls, retries, visible/background conversation creation, token usage, quota consumption, cancellation and orphan state.

### RAS — Runtime Anomaly Sentinel
Detects abnormal fan-out, retry storms, conversation proliferation, runaway token use, memory growth, repeated tool loops, stalled agents and unexpected concurrency.

### PDA — Patch Diagnostic Arena
Treats each repair as a falsifiable hypothesis. Candidate patches must reproduce failure before fix, remove failure after fix and survive targeted regression/adversarial tests.

### Counterfactual Debugging
Varies controlled inputs/state one factor at a time, when practical, to distinguish causal conditions from correlated noise.

### Debugging Budget Router
Starts with low-cost deterministic evidence and escalates to deeper tracing, replay and instrumentation only when uncertainty remains.

### Failure Memory + Regression Lock
Verified defects are stored with provenance and linked to FIM, BCR, feature contracts and future test selection.

### Verified Repair Transaction
No fix is accepted because the code looks plausible. Required transaction: reproduce -> localize -> patch -> re-run original reproducer -> run impacted proof portfolio -> check new regressions -> persist defect knowledge.

## Mandatory safety rules

- Preserve the original symptom and reproducer before patching when feasible.
- Root-cause claims must identify evidence, not intuition alone.
- A fix must include a regression lock unless technically impossible and documented.
- High-risk defects require wider independent verification.
- Debug instrumentation must not silently alter production semantics.
- Sensitive incident data follows HIVE security/provenance rules.

## Primary metrics

Mean time to reproduce; mean time to first divergence; mean time to verified repair; percentage of defects with minimal reproducers; recurrence rate; escaped-defect rate; diagnosis precision; instrumentation overhead; agent/resource anomaly detection lead time.

## R21 integration

Round 22 updates Round 21 after every verified defect: defect -> DGS -> new causal/dependency edges -> updated FIM -> BCR regression -> stronger AITS selection. Test intelligence and defect intelligence therefore improve each other over time.
