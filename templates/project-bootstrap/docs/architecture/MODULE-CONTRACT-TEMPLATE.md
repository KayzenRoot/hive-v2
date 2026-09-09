# Module Contract — <MODULE_ID>

Status: TEMPLATE

## Responsibility
One sentence describing the module's single primary responsibility.

## Owns
- canonical data/state owned by this module;
- APIs/events/contracts owned by this module.

## Does not own
Explicitly list neighboring responsibilities to prevent boundary creep.

## Public interfaces
| Interface | Direction | Consumer/Provider | Stability | Contract reference |
|---|---|---|---|---|

## Dependencies
### Allowed
- <module/service> — reason

### Forbidden
- <module/service> — reason

No hidden dependency is permitted merely for implementation convenience.

## Data and persistence
- canonical store:
- derived/cache state:
- migration ownership:
- retention/deletion rules:

## Failure behavior
- expected failure classes:
- retry/idempotency behavior:
- degraded mode:
- recovery/rollback:

## Security boundary
- trust assumptions:
- authentication/authorization:
- secrets/PII/sensitive data:
- destructive actions:

## Observability contract
- health signal:
- structured events/logs:
- error taxonomy:
- latency/resource signals:
- correlation/trace identity when applicable:

## Performance/resource budget
Reference `docs/quality/PERFORMANCE-BUDGET.md` and declare module-specific budgets.

## Verification contract
- unit/property tests:
- contract/integration tests:
- real-use journey:
- security checks:
- resource/performance checks:

## Requirement / ADR traceability
- requirements:
- ADRs:
- DoD clauses:

## Change rules
Changes to ownership, public contracts, canonical storage or forbidden dependency boundaries require explicit impact analysis and, when architectural, an ADR.