# HIVE V2 — Decisions Ledger

This ledger records V2 decisions added by the R21/R22 extension. R01-R20 frozen decisions remain inherited and must not be silently overridden.

## HIVE-V2-ADR-019 — Impact-aware selective verification
Status: ACCEPTED FOR V2 CONSOLIDATION
Decision: ordinary changes use risk/impact-aware verification instead of indiscriminate full-suite execution. Uncertainty widens coverage. Full/release suites remain mandatory when policy requires.

## HIVE-V2-ADR-020 — Feature Impact Map as verification/debug backbone
Status: ACCEPTED FOR V2 CONSOLIDATION
Decision: maintain machine-readable feature-to-code-to-test-to-incident relationships using deterministic evidence first.

## HIVE-V2-ADR-021 — Operational behavior is correctness
Status: ACCEPTED FOR V2 CONSOLIDATION
Decision: agent fan-out, conversations, retries, token/quota usage, resources, orphan state and other operational side effects can be acceptance criteria and test failures.

## HIVE-V2-ADR-022 — Verified repair transaction
Status: ACCEPTED FOR V2 CONSOLIDATION
Decision: fixes require reproducibility, localization evidence, regression locking and impacted verification before canonical approval.

## HIVE-V2-ADR-023 — Delta-first review
Status: ACCEPTED FOR V2 CONSOLIDATION
Decision: reviews start from immutable identity, fingerprints, changed symbols/contracts and evidence deltas. Repository-wide re-review is escalation, not default.

## HIVE-V2-ADR-024 — Proof validity reuse
Status: EXPERIMENT REQUIRED
Decision direction: expensive proofs may be reused only when all validity-basis fingerprints remain unchanged. Benchmark false-reuse risk before implementation promotion.
