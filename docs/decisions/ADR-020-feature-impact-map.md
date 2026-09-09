# ADR-020 — Feature Impact Map

Status: Accepted for V2 consolidation

## Context
Path-only test selection and human memory are insufficient to model transitive impact in large agent-built systems.

## Decision
Maintain a machine-readable Feature Impact Map linking features, requirements, symbols, dependencies, runtime edges, tests, invariants, incidents and proofs. Deterministic evidence is preferred over LLM inference.

## Consequences
Enables AITS, explainable review, defect correlation and proof reuse. Requires freshness/invalidation rules and explicit confidence. Stale FIM data must never silently narrow verification.
