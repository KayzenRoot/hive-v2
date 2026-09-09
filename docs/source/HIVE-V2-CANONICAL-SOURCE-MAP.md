# HIVE V2 — Canonical Source Map

Status: CANONICAL SOURCE CONSOLIDATION
Date: 2026-09-08
Purpose: make HIVE V2 reconstructible from repository evidence rather than chat/model memory.

## Non-negotiable rule

No implementation agent may rely on conversational memory as project truth. Project truth must resolve from versioned repository sources, immutable artifacts, Git history, approved ADRs, evidence, and the current checkpoint.

## Authority order

1. `docs/checkpoints/CURRENT.md`
2. `docs/decisions/DECISIONS-LEDGER.md`
3. frozen/approved scope sources
4. frozen/approved Definition of Done
5. frozen/approved architecture
6. frozen/approved requirements
7. round specifications and supporting evidence
8. historical research material

A later approved source may supersede an earlier one only through an explicit decision. Never silently reconcile contradictions.

## Program source inventory

| Range | Subject | Repository status | Canonical source |
|---|---|---|---|
| V0.1 | approved inherited baseline | available as project source; repository preservation increment in progress | `HIVE-MASTER-SOURCE-V0.1.md` source artifact |
| R01-R20 | frozen V2 architecture/source-definition research provenance | IMPORTABLE / EXACT GIT ARCHIVAL PRESERVATION PENDING | `HIVE-MASTER-SOURCE-V2.0-FROZEN.md` → target `docs/archive/HIVE-MASTER-SOURCE-V2.0-FROZEN.md` |
| R21 | Test Intelligence, Selective Verification and Real-Use Quality Engineering | versioned | `docs/research/rounds/R21-TEST-INTELLIGENCE.md` |
| R22 | Debugging, Defect Localization and Verified Repair Intelligence | versioned | `docs/research/rounds/R22-DEBUGGING-DEFECT-INTELLIGENCE.md` |
| R21-R22 integrated architecture | test/debug intelligence architecture | versioned | `docs/architecture/TEST-DEBUG-INTELLIGENCE-ARCHITECTURE.md` |

## Frozen R01-R20 source identity

Expected artifact title: `HIVE-MASTER-SOURCE-V2.0-FROZEN.md`

Expected header identity:
- Status: `FROZEN / ARCHITECTURE + SOURCE DEFINITION APPROVED`
- Research revision: `R20 — Final Architecture Freeze Review / ADR Ratification`
- Date: `2026-08-31`
- Organization: `Next Labs`
- Project: `HIVE`
- Freeze meaning: architecture/source definition frozen, NOT implementation complete.

The frozen master explicitly exists to prevent project design from fragmenting across chats, isolated notes, temporary prompts, model memory, or partially overlapping documents. The exact artifact therefore must be preserved in Git before repository-complete R01-R22 canonical history can be claimed.

## Current R01-R20 preservation state

`SOURCE_PRESERVATION_STATE = IMPORTABLE`

The exact original artifact is available and has passed raw-source preflight:
- byte length: `1,334,369`;
- SHA-256: `990c441d5797ee3f8ec81a1f3337f83bb0516fcc0c2a79ef0ef9f4a150b020ee`;
- expected exact Git blob SHA: `6e2620854cb3180e02ac4c18fe21c93bb5dffdcd`;
- V0.1 inherited baseline: PASS;
- R01-R20 provenance: PASS;
- reconstruction used: NO.

This does not yet satisfy repository preservation. The archive path must contain the exact bytes and be independently verified before the state becomes `VERIFIED`.

## Round index

1. R01 — Vision / mission / enterprise AI-native engineering direction
2. R02 — Context / retrieval / RAG evolution
3. R03 — Token & Context Economics
4. R04 — Repository & Code Intelligence
5. R05 — Agent Harness & Orchestration
6. R06 — Long-Horizon Execution & Memory
7. R07 — Security / Zero Trust / Containment
8. R08 — DevSecOps / Software Supply Chain / CI-CD
9. R09 — Verification / Testing / Formal Methods
10. R10 — Local-First & Infrastructure Efficiency
11. R11 — MCP / A2A / Interoperability / UADS / UGAS
12. R12 — Observability / FinOps / Engineering Economics
13. R13 — Platform Engineering / Adaptive Golden Paths / Project Bootstrap Intelligence
14. R14 — Learning / Evals / Distillation / Organizational Intelligence
15. R15 — Emerging Technologies 2027–2030 / Frontier Architecture / Proprietary Research Bets
16. R16 — Commercialization / Multi-Tenant / Enterprise Productization / Sovereign Engineering Intelligence
17. R17 — Failure Modes / Red-Team Architecture / Catastrophic Resilience / Recovery Engineering
18. R18 — Final Gap Analysis / Requirements Coverage / Contradiction Resolution / Architecture Compression
19. R19 — V2 Scope / Requirements / Definition of Done / Backlog Partitioning
20. R20 — Architecture Freeze Review / final ADR ratification
21. R21 — Test Intelligence / Selective Verification / Real-Use Quality Engineering
22. R22 — Debugging / Defect Localization / Verified Repair Intelligence

## Memory independence gate

`MEMORY_INDEPENDENT = true` only when all conditions are satisfied:

- exact immutable R01-R20 frozen master is stored in this repository;
- R21 and R22 are stored in this repository;
- source integrity metadata is recorded;
- R01-R22 reconciliation is complete;
- compact V2 Source Pack is generated from versioned canonical inputs;
- re-freeze audit is APPROVED;
- current checkpoint points only to repository-contained canonical sources.

Until then, the repository must report `MEMORY_INDEPENDENT = false` and block V2 implementation bootstrap.

## Agent bootstrap rule

A new Sol/Codex/Cursor/executor session must be able to start with no previous chat and reconstruct:
- current project state;
- approved architecture;
- scope and non-scope;
- all R01-R22 planned capabilities and classifications;
- approved decisions;
- Definition of Done;
- next necessary increment;
- known blockers;
- required evidence and tests.

If it cannot do this from Git alone, canonical-source consolidation is incomplete.
