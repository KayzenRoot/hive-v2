# HIVE V2 — Compact Source Pack Contract

Status: CANONICAL GOVERNANCE CONTRACT
Purpose: define the compact execution-oriented source pack generated only after exact R01-R20 preservation and R21/R22/HEDS reconciliation.

## Principle

The Source Pack is a compact navigator and execution contract. It is derived from repository-contained canonical sources and NEVER replaces the immutable R01-R20 frozen master, R21/R22 specifications, ADRs or evidence history.

## Required properties

The Source Pack must be:
- repository-contained;
- reproducible from canonical inputs;
- fingerprinted;
- explicit about source precedence;
- progressive-disclosure friendly;
- compact enough for executor bootstrap;
- complete enough to locate every NECESSARY requirement and governing decision;
- free of silent semantic compression.

## Required sections

1. Project/version identity.
2. Canonical source hierarchy.
3. Current checkpoint and implementation authorization state.
4. Frozen scope summary with links to authoritative source sections.
5. Requirements index.
6. Architecture/module map.
7. Decisions/ADR index.
8. R01-R22 round capability index.
9. NECESSARY / IMPORTANT / EXPERIMENT / FUTURE / OUT classifications.
10. HEDS operating contract.
11. Test/debug/review gates.
12. Security/data-integrity constraints.
13. Deployment/local-first constraints.
14. Definition-of-Done traceability.
15. Work Order/bootstrap instructions.
16. Source fingerprints and generation metadata.

## Progressive disclosure tiers

### Tier 0 — bootstrap
Checkpoint, source hierarchy, active WO, risk, relevant scope/DoD pointers.

### Tier 1 — task intent
Relevant requirements, ADRs, module contracts, out-of-scope boundaries.

### Tier 2 — implementation neighborhood
Relevant code/module/test/evidence maps and dependencies.

### Tier 3 — escalation
Broader architecture, historical rounds and neighboring modules only when risk/uncertainty requires.

### Tier 4 — full canonical source
Exact historical/master source only when a conflict, provenance question or high-assurance audit requires it.

## Integrity

Each generated Source Pack must record:
- generating commit SHA;
- canonical input paths;
- input fingerprints;
- generation tool/version when automated;
- generation timestamp;
- reconciliation report reference;
- re-freeze audit reference when available.

If any canonical input fingerprint changes, the Source Pack becomes stale until regenerated/revalidated.

## Promotion gate

A Source Pack may become the default executor bootstrap only after:
1. exact R01-R20 preservation VERIFIED;
2. R21/R22/HEDS reconciliation APPROVED;
3. traceability completeness checked;
4. Sol review confirms no semantic loss affecting NECESSARY scope or governance.
