# ADR-023 — Delta-First Review

Status: Accepted for V2 consolidation

## Context
Large projects waste review time by repeatedly re-reading unchanged source, re-running unrelated tests and re-evaluating already-validated evidence.

## Decision
Review starts from immutable identity and the smallest trustworthy delta: Work Order, base/head SHA, canonical-source fingerprints, changed symbols/contracts, Change Impact Manifest and Evidence Bundle. Context expands progressively only when risk, uncertainty or failing evidence requires it.

Correction reviews reuse still-valid evidence from the previous audit and inspect only the correction delta unless Context Lock or impact changes invalidate prior evidence.

## Consequences
Review becomes faster and cheaper without reducing assurance. Fingerprint correctness, impact mapping and stale-context detection become critical review infrastructure.
