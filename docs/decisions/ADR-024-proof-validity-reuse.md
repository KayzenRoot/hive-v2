# ADR-024 — Proof Validity Reuse

Status: Experiment Required

## Context
Mature repositories repeatedly rerun expensive proofs even when the full validity basis of those proofs did not change.

## Decision Direction
Permit reuse only when a proof is cryptographically/fingerprint-bound to all relevant validity inputs: code/symbol dependencies, test code, fixtures/data, config, dependency lock state, environment/runtime, schema/database state and required upstream proofs.

Any relevant drift invalidates reuse. Missing dependency knowledge invalidates reuse. HIGH_ASSURANCE policy may forbid reuse for selected obligations.

## Required Experiment
Benchmark speed savings, invalidation accuracy and false-reuse risk against fresh execution before promoting this ADR from EXPERIMENT REQUIRED to ACCEPTED.
