# Evidence Bundle Contract

Every implementation or correction increment must produce an Evidence Bundle.

## Required identity

- work_order_id
- repository
- base_sha
- head_sha
- branch
- canonical_source_fingerprints
- risk_tier

## Required change evidence

- files changed
- symbols/contracts changed when determinable
- Change Impact Manifest
- explicit scope statement
- architecture/ADR implications
- migrations/config/dependency changes

## Required verification evidence

- selected test/proof list
- selection rationale
- test results and duration
- lint/typecheck/build results where applicable
- security checks where applicable
- architecture/contract checks where applicable
- real-use/resource-behavior evidence when applicable
- reused proofs and their fingerprints
- skipped/deferred checks with policy justification

## Required review material

- summary
- decisions made
- errors introduced and fixed
- remaining risks
- raw evidence/artifact references
- proposed Checkpoint Delta

## Invalid bundle conditions

A bundle is invalid if base/head identity is missing, evidence is based on a stale source fingerprint, required proof obligations are skipped without policy authority, or a reused proof cannot demonstrate fingerprint validity.

"Completed" is never evidence.
