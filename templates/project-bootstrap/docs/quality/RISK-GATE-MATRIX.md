# HEDS Risk & Quality Gate Matrix

Status: TEMPLATE

Risk changes review depth, never the truth standard.

| Tier | Typical change | Minimum evidence |
|---|---|---|
| LOW | docs/non-runtime isolated change | identity, diff/scope, relevant validation |
| STANDARD | bounded feature/refactor | impacted tests, lint/typecheck/build as applicable, contracts, Evidence Bundle |
| ELEVATED | persistence/API/migration/cross-module/performance-sensitive | expanded impact proof, integration/real-use evidence, security/resource review as applicable, rollback reasoning |
| HIGH_ASSURANCE | auth/security/canonical data/destructive actions/critical financial or release path | conservative verification, independent/adversarial evidence where justified, recovery proof, full-suite or equivalent required policy, explicit Sol audit |

## Automatic escalation signals
- uncertain/stale impact graph;
- unexpected blast-radius expansion;
- canonical storage/schema change;
- auth/trust-boundary change;
- dependency/toolchain change with broad transitive impact;
- migration/destructive action;
- selector/cache uncertainty or prior miss;
- flaky/insufficient proof;
- performance/resource regression;
- repeated correction cycles;
- inability to reproduce failure/environment.

## Rule
Optimization mechanisms such as selected tests, proof reuse, cache, Context Capsule or delta review must fail safe toward broader evidence when uncertainty exceeds the project's accepted threshold.