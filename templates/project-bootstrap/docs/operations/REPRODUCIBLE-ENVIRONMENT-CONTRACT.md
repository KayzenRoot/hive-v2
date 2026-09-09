# Reproducible Development Environment Contract

Status: TEMPLATE

## Goal
A fresh executor should be able to reproduce the supported local development/test environment without guessing versions or manually discovering setup steps.

## Required declarations
- supported OS/platforms;
- runtime/compiler/tool versions;
- package/dependency manager and lockfile policy;
- container/Compose versions where used;
- bootstrap command;
- health/preflight command;
- test/lint/typecheck/build commands;
- local persistence paths and safe reset rules;
- required environment variables by name, never committed secret values;
- reference hardware where performance matters.

## Environment fingerprint
A diagnostic/preflight artifact SHOULD record non-secret versions and relevant configuration sufficient to explain environment-dependent failures.

## Determinism rules
- dependency installation uses lock/pinned state where supported;
- bootstrap is idempotent where practical;
- destructive reset is explicit and never the default recovery step;
- generated state is distinguishable from canonical/user-owned state;
- secrets are excluded from diagnostics/evidence.

## Executor gate
Before implementation, executor runs the documented preflight. Environment mismatch that can invalidate evidence causes STOP or explicit risk escalation, not silent improvisation.