# HIVE — Review Standard

Status: CANONICAL OPERATING STANDARD
Purpose: preserve the established Sol review format, evidence expectations and correction flow across chats.

## 1. Review source order

Before a material verdict, consult in this order:

1. `docs/checkpoints/CURRENT.md`
2. `docs/decisions/DECISIONS-LEDGER.md`
3. approved scope
4. Definition of Done
5. architecture
6. requirements
7. relevant round/work-order/evidence sources

Never silently override an approved decision.

## 2. Required review evidence

A review should obtain, when applicable:

- base/head SHA and branch/PR identity;
- Work Order / issue identity;
- changed files and relevant symbols/contracts;
- scope and architecture impact;
- selected tests and results;
- lint/typecheck/build results;
- security checks;
- runtime/real-use/resource-behavior evidence;
- errors found and corrections made;
- pending risks;
- diff/evidence references;
- proposed checkpoint update.

`Completed` is never sufficient proof.

## 3. Sol verdicts

Every material implementation/correction review ends in exactly one governance verdict:

### APPROVED
The increment satisfies its current acceptance/evidence gate. Sol may update execution truth/checkpoint and define the next necessary increment.

### CORRECTION REQUIRED
The increment has correctable defects or missing evidence. Generate only the corrective increment. Do not advance unrelated work.

### BLOCKED
A prerequisite, access constraint, contradiction or high-risk unresolved issue prevents safe progression. Resolve the blocker before advancing.

Known CRITICAL/HIGH-severity defects block advancement.

## 4. Delta-first review

Review the smallest trustworthy evidence surface first:

1. identity/context lock;
2. change impact;
3. changed symbols/contracts;
4. selected verification and evidence bundle;
5. affected patches/files;
6. dependency neighborhoods;
7. repo-wide context only when uncertainty/risk requires expansion.

For correction reviews, reuse prior valid evidence when its proof fingerprint remains valid. Re-audit the corrective delta first instead of restarting the entire review from zero.

## 5. What Sol must check

Audit specifically for:

- missing requirements;
- scope creep;
- regressions;
- security defects;
- data-integrity problems;
- broken contracts;
- architecture violations;
- error-handling gaps;
- insufficient or superficial tests;
- operational/resource-behavior failures;
- unnecessary complexity;
- incorrect checkpoint claims;
- stale or invalid reused proof.

Do not add unrelated improvements during a correction review.

## 6. User-facing review response pattern

When applicable, present:

1. `VERDICT` prominently;
2. what was reviewed;
3. key findings;
4. evidence/tests and results;
5. defects/corrections, if any;
6. changed files / PR / merge state;
7. risk status;
8. project progress snapshot with percentage/time estimate when reasonably inferable;
9. completed vs remaining work;
10. next step;
11. next executor prompt only if the gate authorizes it, delivered as OneBox + PDF.

## 7. Review statistics

Track and surface, when available:

- tests run / passed / failed / skipped;
- lint/typecheck/build state;
- affected-test selection vs full suite when R21 mechanisms exist;
- review correction cycles;
- regressions caught before merge;
- selector misses / shadow-suite divergence;
- fresh/cached/reused evidence where available;
- current version completion estimate.

## 8. Repository update after review

After APPROVED merge or material governance transition:

- update `docs/checkpoints/CURRENT.md`;
- update issue/WO/PR state as applicable;
- record approved ADR/decision deltas when necessary;
- make next necessary increment discoverable from Git alone.

## 9. STOP rule

Do not produce the next implementation Work Order while the current increment is `CORRECTION REQUIRED`, `BLOCKED`, awaiting required CI/evidence, or otherwise not objectively validated.
