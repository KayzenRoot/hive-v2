# HIVE V2 — Review Operating Model

## Goal

Increase review speed and quality simultaneously by reviewing the smallest trustworthy evidence surface first and escalating only when risk or uncertainty requires it.

## Canonical sequence

1. CONTEXT LOCK — base SHA, head SHA, Work Order ID, canonical-source fingerprints.
2. PREFLIGHT — scope, architecture, risk tier, stale-context detection.
3. CHANGE IMPACT — Git diff, symbols, contracts, dependencies, schemas/config.
4. SELECTED VERIFICATION — explain why each test/proof is required.
5. EVIDENCE BUNDLE — tests, lint/typecheck/build, security/architecture checks, runtime evidence.
6. AUDIT — compare implementation against scope, architecture, requirements, acceptance criteria and DoD.
7. VERDICT — APPROVED / CORRECTION REQUIRED / BLOCKED.
8. CHECKPOINT DELTA — only after objective approval.

## Progressive review disclosure

R0: PR metadata, Work Order, base/head SHA, risk and summary.
R1: changed files/symbols and Change Impact Manifest.
R2: relevant requirements/ADRs/contracts and impacted tests.
R3: targeted patches and evidence failures.
R4: complete affected files and dependency neighborhoods.
R5: repository-wide investigation only when evidence justifies it.

## Fast-review rules

- Do not reread unchanged canonical sources when their fingerprint matches Context Lock.
- Do not rerun deterministic questions through an LLM.
- Cache approved evidence by immutable fingerprint.
- Review changed symbols before whole files.
- Review dependency and contract edges before unrelated modules.
- Prefer machine-generated evidence summaries linked to raw artifacts.
- Corrections stay in the same Work Order/PR when safe.
- A correction review starts from the prior approved evidence plus delta, not from zero.

## Risk policy

LOW: targeted checks and direct regressions.
STANDARD: impacted unit/integration + lint/typecheck/build.
ELEVATED: STANDARD + wider regression, persistence/migration/security/recovery as applicable.
HIGH_ASSURANCE: independent proof obligations, broad regression, rollback/roll-forward evidence and no selective shortcut that reduces required assurance.

## Review quality guards

Review speed must never hide: broken contracts, security issues, data-loss risk, stale checkpoint claims, missing error handling, insufficient tests, unnecessary scope expansion or architectural drift.

## Review metrics

Track review wall-clock, context tokens, unchanged context avoided, evidence reuse, correction cycles, defects caught pre-merge, escaped defects, selector miss rate and false-positive review findings.
