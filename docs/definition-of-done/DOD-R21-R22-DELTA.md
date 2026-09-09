# HIVE V2 — Definition of Done Delta for R21/R22

R21/R22 cannot be declared complete until all applicable items below are objectively demonstrated.

## Test Intelligence
- Feature contracts exist for representative critical capabilities.
- FIM edges are machine-readable and explainable.
- AITS selection is deterministic/reproducible for the same evidence state.
- Selector uncertainty expands, never narrows, the suite.
- Shadow full-suite calibration measures selector false negatives and over-selection.
- No accepted CRITICAL/HIGH regression is missed by the selector benchmark.
- Real-use install/runtime journeys exist.
- Resource behavior tests cover agent/conversation/retry/token/fan-out behavior where applicable.
- Escaped defects can become permanent Behavioral Contract Replays.

## Debugging Intelligence
- Incident Replay Capsule can preserve enough evidence to reproduce representative failures.
- First Divergence Locator identifies an evidence-backed divergence point on benchmark incidents.
- Defect records preserve symptom, cause, fix and regression proof.
- Verified Repair Transaction rejects a patch that does not eliminate the original reproducer.
- Debugging evidence feeds FIM/BCR after approval.

## Review performance
- Review can operate from Context Lock + Change Impact Manifest + Evidence Bundle.
- Correction review can reuse still-valid prior evidence.
- Review benchmark compares delta-first review with repository-wide review on time/tokens and defect detection.
- Faster review is accepted only if defect-detection quality is not materially degraded.

## Closure
- Unit/integration/end-to-end tests applicable to these components pass.
- Lint/typecheck/build pass where applicable.
- Security and provenance boundaries pass.
- Documentation and ADRs match implementation evidence.
- Final architecture/source and implementation audits are APPROVED.
