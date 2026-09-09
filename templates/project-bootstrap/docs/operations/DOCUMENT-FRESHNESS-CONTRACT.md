# Documentation Freshness Contract

Status: TEMPLATE / HEDS CONTROL-PLANE CONTRACT

Documentation that directs executors/reviewers is operational control-plane state. Stale guidance is a defect.

## Canonical vs derived
Every guidance artifact declares one of:
- CANONICAL — authoritative source;
- DERIVED — reproducible navigator/summary/index;
- HISTORICAL — immutable provenance;
- TEMPLATE — bootstrap source.

Derived artifacts never supersede canonical inputs.

## Fingerprint basis
Generated/derived artifacts SHOULD record:
- generating commit SHA;
- canonical input paths;
- input hashes/fingerprints;
- generator/tool version when automated;
- generated timestamp;
- validation status.

## Staleness triggers
Revalidate/regenerate when relevant inputs change, including:
- checkpoint/gate state;
- scope/requirements/DoD;
- ADR/architecture;
- module ownership/contracts;
- schemas/APIs;
- test/verification mappings;
- CI/check names;
- environment/toolchain contracts.

## Review rule
A stale derived artifact may be used only as a locator, never as sufficient proof. If it could misroute implementation or verification, STOP and refresh it.

## Fresh-chat rule
The active checkpoint must point only to current canonical operating standards and explicitly name blockers/next gate.