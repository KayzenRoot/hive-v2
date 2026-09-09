# Threat Model — <SYSTEM / MODULE>

Status: TEMPLATE

## Assets
List canonical data, credentials, source, models, user-owned files, execution capability and other valuable assets.

## Trust boundaries
| Boundary | Trusted side | Untrusted side | Controls |
|---|---|---|---|

## Entry points
APIs, UI inputs, files, connectors, plugins, agents, network services, CI/CD, dependencies and local IPC.

## Threats
For each material threat record:
- threat ID and scenario;
- affected asset/boundary;
- likelihood and impact;
- existing controls;
- residual risk;
- verification/evidence;
- owner.

## Required categories
Consider at minimum when applicable:
- authentication/authorization bypass;
- injection/untrusted content;
- secret leakage;
- supply-chain/dependency compromise;
- unsafe agent/tool execution;
- path/file traversal and local privilege boundaries;
- canonical-data corruption/loss;
- replay/idempotency failures;
- cross-project/tenant leakage;
- denial/resource exhaustion;
- unsafe migration/rollback;
- audit/provenance tampering.

## Change trigger
A WO touching trust boundaries, auth, canonical persistence, dependency/toolchain, destructive actions or external execution must re-evaluate relevant threats. HIGH/CRITICAL unresolved risk blocks approval.