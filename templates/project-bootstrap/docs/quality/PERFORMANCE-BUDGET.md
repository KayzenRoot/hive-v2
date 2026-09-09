# Performance & Resource Budget

Status: TEMPLATE

Performance is a contract, not a late optimization phase. Values are project-specific and must be measured on declared reference environments.

## Reference environments
| ID | CPU | GPU | RAM | Storage | OS/runtime | Purpose |
|---|---|---|---|---|---|---|

## User-visible budgets
| Journey/operation | Metric | Target | Hard regression gate | Measurement method |
|---|---|---:|---:|---|

## Service/module budgets
Track only metrics relevant to the project:
- latency p50/p95/p99;
- CPU/GPU time/utilization;
- peak/steady memory;
- I/O and network;
- logical/physical storage;
- startup/recovery time;
- token/context usage for LLM paths;
- cache hit/reuse rate;
- background work.

## Regression policy
1. Compare against a fingerprinted baseline.
2. Attribute the regression to the smallest trustworthy change neighborhood when possible.
3. Do not average away a critical tail-latency/resource regression.
4. A budget exception requires rationale, measured evidence and explicit approval.
5. Faster is not accepted when correctness/security/data integrity regresses.

## Evidence
Every performance-sensitive WO records environment fingerprint, benchmark/scenario ID, base/head measurements, variance/sample count where meaningful, and raw evidence location.