# HIVE — Review Standard v2

Status: CANONICAL OPERATING STANDARD
Purpose: maximize quality and minimize Time-to-Trusted-Merge using risk-adaptive, evidence-driven, delta-first review.

## 1. Review source order

Before a material verdict, consult in this order:
1. `docs/checkpoints/CURRENT.md`
2. `docs/decisions/DECISIONS-LEDGER.md`
3. approved scope
4. Definition of Done
5. architecture
6. requirements
7. relevant Work Order / Review Manifest / Evidence Bundle / round sources

Never silently override an approved decision.

## 2. Review entrypoint

The preferred machine-readable entrypoint is `docs/review/review-manifest.schema.json` instantiated for the active Work Order/PR.

The reviewer begins from immutable identity and the smallest trustworthy evidence surface rather than scanning the whole repository.

Required identity when applicable:
- Work Order / issue;
- repository;
- branch/PR;
- base/head SHA;
- risk tier;
- scope/out-of-scope;
- changed files/symbols;
- impacted requirements/contracts/modules;
- selected verification;
- evidence references;
- uncertainties.

`Completed` is never sufficient proof.

## 3. Risk-adaptive review

### LOW
Documentation, non-executable metadata, narrow cosmetic changes with no contract/runtime impact.
Default: identity, scope, diff, docs/link validation as applicable.

### STANDARD
Ordinary isolated implementation changes.
Default: impact analysis, selected tests, lint/typecheck/build as applicable, contract review, targeted runtime evidence.

### ELEVATED
Cross-module changes, public APIs, persistence, migrations, concurrency, agents, deployment/runtime behavior, dependency/toolchain changes or areas with recent defects.
Default: broader dependency verification, real-use journey, stronger security/data-integrity review, selector confidence checks.

### HIGH_ASSURANCE
Authentication/authorization, secrets, critical persistence, financial/security-sensitive paths, core orchestration, high-blast-radius migrations, release-critical contracts.
Default: independent verification where feasible, adversarial/property/fuzz/mutation/formal techniques where justified, full-suite or policy-mandated broader verification, no aggressive proof reuse.

Uncertainty escalates review depth. It never reduces it.

## 4. Governance verdicts

Every material implementation/correction review MUST end in exactly one verdict:

### APPROVED
The increment satisfies its current acceptance and evidence gate. Sol may update execution truth/checkpoint and define the next NECESSARY increment.

### CORRECTION REQUIRED
The increment has correctable defects or missing evidence. Generate only the corrective increment. Do not advance unrelated work.

### BLOCKED
A prerequisite, access constraint, contradiction or unresolved risk prevents safe progression. Resolve the blocker before advancing.

Known CRITICAL/HIGH-severity defects block advancement.

## 5. Delta-first review sequence

1. Context Lock: base/head/WO/risk/canonical fingerprints.
2. Review Manifest / Change Impact Manifest.
3. Work Intent Graph and impacted contracts.
4. selected verification + Evidence Bundle.
5. highest Review Attention Router targets.
6. changed symbols and patches.
7. runtime/resource behavior when applicable.
8. architecture/security/data integrity/modular-boundary checks.
9. dependency neighborhoods.
10. repo-wide context only when risk/uncertainty justifies expansion.

## 6. Correction Delta Protocol

For CORRECTION REQUIRED, the next review starts from rejected-head → corrected-head.

Re-check:
- unresolved findings;
- files/symbols touched by the correction;
- evidence invalidated by the correction;
- newly introduced impacts;
- newly supplied tests/evidence.

Reuse prior accepted evidence only when its validity fingerprint remains unchanged. Do not restart the complete review from zero by default.

## 7. Proof Cache and proof decay

Reusable proof must declare its validity basis. A changed code/test/fixture/config/lockfile/schema/toolchain/runtime/environment assumption invalidates reuse when relevant.

`Proof Decay Index` may prioritize re-verification. High uncertainty, stale dependencies, flaky history, selector misses or runtime drift increase decay.

Cache reuse MUST be auditable. `cached` is not equivalent to `trusted` without a valid key/fingerprint.

## 8. Review Attention Router

Review order should prioritize expected information value using signals such as:
- consequence of failure;
- uncertainty/novelty;
- contract centrality;
- historical defect density;
- dependency fan-in/fan-out;
- runtime/resource side effects;
- security/data-integrity sensitivity;
- test weakness/selector miss history.

This ranking optimizes time-to-falsification while preserving the right to expand the review.

## 9. Required quality checks

Audit, when applicable, for:
- missing requirements;
- scope creep;
- regressions;
- security defects;
- data-integrity problems;
- broken contracts;
- architecture violations;
- modular-boundary drift/cycles;
- error-handling gaps;
- insufficient/superficial tests;
- operational/resource-behavior failures;
- unnecessary complexity;
- incorrect checkpoint claims;
- stale proof reuse;
- flaky tests;
- performance regressions;
- unexpected background work/agent fan-out/quota use;
- installer/upgrade/restart/recovery behavior.

## 10. Complexity Budget Gate

A Work Order should disclose meaningful increases in:
- modules/dependencies;
- public surface;
- mutable state;
- execution paths;
- background workers/agents;
- external calls;
- configuration;
- long-lived abstractions.

Complexity beyond what approved requirements need requires explicit justification. Prefer simpler compatible implementations.

## 11. Merge confidence

The primary optimization target is `Time-to-Trusted-Merge` (TTTM), measured from executor start until objectively trusted merge.

A faster review that increases correction cycles or escaped defects is not an improvement.

Where platform support and repository policy allow, a Trusted Merge Queue SHOULD revalidate the exact integration state and required checks before merge.

## 12. Defect Learning Loop

Every material escaped defect and useful pre-merge catch SHOULD record:
- triggering change;
- symptom;
- root cause;
- affected feature/module;
- why existing tests/review missed or caught it;
- minimal reproducer;
- permanent regression test;
- selector/impact-map update;
- review rule or architecture lesson, if applicable.

This record feeds R21/R22 defect memory, Regression Escape Radar and future review/test selection.

## 13. User-facing review response

When applicable, present:
1. `VERDICT` prominently;
2. what was reviewed;
3. key findings;
4. evidence/tests/results;
5. defects/corrections;
6. changed files / PR / merge state;
7. risk status;
8. compact project progress snapshot with percentage/time estimate when reasonably inferable;
9. completed vs remaining work;
10. next step;
11. next executor prompt PDF only when the gate authorizes it.

Do not provide OneBox/copyable full prompt unless the user explicitly requests that specific format.

## 14. Review statistics

Track when available:
- TTTM;
- executor orientation time;
- implementation time;
- tests run/pass/fail/skip;
- selected/full-suite ratio;
- time-to-first-failure;
- verification/review wall-clock;
- build/test/proof cache hit rate;
- context tokens and context signal ratio;
- correction cycles;
- regressions caught pre-merge;
- escaped defects;
- selector misses/shadow-suite divergence;
- flaky test rate;
- complexity delta;
- rework cause.

## 15. Repository update after review

After APPROVED merge or material governance transition:
- update `docs/checkpoints/CURRENT.md`;
- update issue/WO/PR state;
- record ADR/decision delta when needed;
- preserve evidence identity;
- make the next necessary increment discoverable from Git alone.

## 16. STOP rule

Do not produce the next implementation Work Order while the current increment is CORRECTION REQUIRED, BLOCKED, awaiting mandatory CI/evidence, or otherwise not objectively validated.
