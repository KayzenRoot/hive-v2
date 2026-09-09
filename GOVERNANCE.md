# HIVE V2 Governance

## Authority

Canonical precedence:
1. latest approved `docs/checkpoints/CURRENT.md`
2. `docs/decisions/DECISIONS-LEDGER.md`
3. canonical scope
4. canonical Definition of Done
5. canonical architecture
6. canonical requirements
7. round specifications and supporting sources

The complete R01-R20 frozen master must be imported before this repository is treated as a complete V2 historical source.

## Change control

Every implementation increment uses one stable Work Order ID across issue, branch, commits, PR, evidence, corrections and checkpoint delta.

## Canonical promotion

Executor claims are staged. Canonical truth changes only after evidence-based audit with APPROVED verdict.

## Review verdicts

- APPROVED: merge/update checkpoint may proceed.
- CORRECTION REQUIRED: same Work Order/PR receives correction delta when safe.
- BLOCKED: blocker resolved before progress.

No HIGH/CRITICAL defect may be knowingly carried into the next increment.

## Scope discipline

New work is classified NECESSARY, IMPORTANT, FUTURE or OUT OF SCOPE. Only NECESSARY enters the current version automatically.

## Evidence discipline

Git, hashes, AST/static analysis, tests and runtime evidence outrank conversational recollection. LLM reasoning is used where deterministic evidence cannot resolve the question.
