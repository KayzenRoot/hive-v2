# HIVE V2 — Test & Debug Intelligence Architecture

## Purpose

Unify selective verification, proof reuse, real-use validation, defect localization, replay and verified repair into one evidence loop.

## Runtime flow

Change -> Work Order -> Git/AST impact -> Feature Impact Map -> risk classification -> AITS test selection -> proof portfolio -> review gate.

If a defect occurs: incident capture -> first-divergence localization -> minimal reproducer -> causal analysis -> patch hypothesis -> targeted verification -> regression lock -> defect memory -> FIM update.

## Core data products

- Feature Verification Contract
- Feature Impact Map
- Change Impact Manifest
- Proof Fingerprint
- Evidence Bundle
- Incident Replay Capsule
- Defect Genome Record
- Regression Lock
- Review Verdict

## Deterministic-first rule

Prefer Git diff, AST/symbol graph, dependency graph, test coverage, runtime traces, schema/API/config diff, hashes and static analysis before LLM reasoning. LLMs may interpret ambiguity but must not replace available deterministic evidence.

## Safety fallback

Selective verification is an optimization, not an excuse to reduce assurance. Missing, stale or contradictory impact evidence escalates verification. HIGH_ASSURANCE work defaults to broader independent proof obligations.

## Review integration

Review consumes evidence in layers: metadata/fingerprints -> changed files/symbols -> architecture/contract deltas -> impacted tests -> failing evidence -> expanded context only when needed. This is the canonical review acceleration strategy for V2.
