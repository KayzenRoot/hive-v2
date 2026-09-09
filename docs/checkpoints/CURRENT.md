# HIVE V2 — Current Checkpoint

Status: CANONICAL SOURCE PRESERVATION IN PROGRESS
Date: 2026-09-08

## Canonical execution truth
HIVE V1 remains the active implementation line until the formal V2 implementation transition is approved.

## V2 planning truth
- R01-R20: historical architecture freeze preserved externally; exact frozen master artifact is identified but still requires byte-complete Git import.
- R21: Test Intelligence planned and documented in Git.
- R22: Debugging & Defect Intelligence planned and documented in Git.
- V2 target planning sequence: R01-R22.
- Re-freeze after R22: pending exact R01-R20 Git preservation, reconciliation and architecture/source audit.
- `MEMORY_INDEPENDENT = false` until every canonical V2 design source required to reconstruct R01-R22 is repository-contained.

## Operating continuity truth
- `CHAT_CONTINUITY_READY = true` when GitHub is available.
- Fresh HIVE chats bootstrap from repository sources rather than screenshots/manual checkpoint uploads/user re-explanation.
- Canonical continuity: `docs/operations/CHAT-CONTINUITY-PROTOCOL.md`.
- Prompt delivery: `docs/operations/RESPONSE-AND-DELIVERY-STANDARD.md`.
- Review: `docs/operations/REVIEW-STANDARD.md`.
- User-facing executor prompts are downloadable PDF only unless explicitly requested otherwise for a specific delivery.
- Future implementation/correction prompts use globally installed UADS where applicable and require UADS runtime/bootstrap evidence.

## HEDS engineering delivery truth
- `HEDS_PROCESS_READY = true` for governance/documentation/process adoption.
- `HEDS_TEMPLATE_HARDENED = true` after PR #98.
- `HEDS_AUTOMATION_IMPLEMENTED = false` until runtime tooling is implemented/tested.
- HEDS automation epic: #75, blocked until R22 source re-freeze APPROVED.
- HEDS is the default implementation/review model for HIVE V2 once implementation is authorized.
- Future new projects SHOULD bootstrap from `templates/project-bootstrap/` unless an explicit ADR chooses otherwise.
- Template now includes module contracts, performance/resource budgets, risk gates, threat model, reproducible environment/preflight, documentation freshness and implementation-readiness checklist.
- Primary delivery metric: Time-to-Trusted-Merge.
- Canonical HEDS source: `docs/operations/ENGINEERING-DELIVERY-SYSTEM.md`.
- Machine-readable review contract: `docs/review/review-manifest.schema.json`.
- HEDS evidence-gated research portfolio: `docs/operations/HEDS-INNOVATION-ROADMAP.md`.
- ADR-025/026 govern HEDS/template adoption. ADR-027 keeps Engineering Digital Twin as IMPORTANT / EXPERIMENT REQUIRED.
- New process research must not silently become product NECESSARY scope or release blocker.

## Fresh-chat bootstrap minimum
Read:
1. this checkpoint;
2. `docs/source/AGENT-BOOTSTRAP.md`;
3. `docs/source/HIVE-V2-CANONICAL-SOURCE-MAP.md`;
4. `docs/operations/CHAT-CONTINUITY-PROTOCOL.md`;
5. `docs/operations/RESPONSE-AND-DELIVERY-STANDARD.md`;
6. `docs/operations/REVIEW-STANDARD.md`;
7. `docs/operations/ENGINEERING-DELIVERY-SYSTEM.md`;
8. active issue/WO/PR/evidence.
Then retrieve only additional canonical material needed for the requested increment.

## Completed in repository
- R21/R22 specs and integrated architecture.
- impact-aware review, Evidence Bundle, Change Impact Manifest and Review Manifest.
- R21/R22 ADRs and scope/DoD delta.
- canonical R01-R22 source map and memory-independent agent bootstrap contract.
- chat continuity and PDF-only prompt-delivery standards.
- HEDS process, project bootstrap template and HEDS automation epic #75.
- hardened reusable bootstrap template via PR #98, merge `c89eca74d5c7aac040a2a16b643e795d565bcba1`.
- stale pre-transition tracker assumptions reconciled under issue #79 without removing valid V1 transition gates.
- HEDS research backlog/issues #81-#97 captured with evidence-gated classifications.
- exact-source preservation manifest/import procedure.
- post-preservation reconciliation procedure, Source Pack contract and R22 re-freeze checklist.
- Frozen R01-R20 master identity verified as `HIVE-MASTER-SOURCE-V2.0-FROZEN.md`, R20 Architecture Freeze Review, 2026-08-31.

## Exact source preservation status
`SOURCE_PRESERVATION_STATE = IDENTIFIED`

Repository-contained: R21/R22, integrated architecture, scope/DoD delta, review/evidence/governance contracts, HEDS process/templates/research roadmap, source preservation/import procedure, reconciliation/Source Pack/re-freeze procedures.

Exact Git import still required: `HIVE-MASTER-SOURCE-V2.0-FROZEN.md` with complete R01-R20 provenance/frozen architecture. Do not replace it with reconstruction, summary or search snippets.

## Pending before V2 implementation bootstrap
1. make the exact original R01-R20 master importable by Git write path;
2. import unchanged to `docs/archive/HIVE-MASTER-SOURCE-V2.0-FROZEN.md` using the canonical procedure;
3. record SHA-256, byte length where available, Git blob SHA and preserving commit SHA;
4. audit identity/provenance and set source preservation VERIFIED only with objective evidence;
5. execute R21/R22/HEDS reconciliation procedure;
6. produce compact canonical V2 Source Pack;
7. perform R22 re-freeze audit;
8. if APPROVED, set `MEMORY_INDEPENDENT = true`;
9. satisfy still-valid V1→V2 transition/lineage/dogfood/baseline/protection gates;
10. authorize first V2 implementation WO using HEDS;
11. implement/test HEDS automation under #75 as governed.

## Current external blockers
- exact R01-R20 raw artifact bytes are not exposed through the current file-search surface for byte-complete Git upload/hash verification;
- final V1 release/lineage evidence and real inherited CI check names remain separate transition prerequisites where required by issues #3/#5/#63/#64/#65.

## Next necessary increment
Obtain an exact importable representation of `HIVE-MASTER-SOURCE-V2.0-FROZEN.md`, execute preservation, then reconciliation/Source Pack/re-freeze. No HIVE V2 product implementation before those gates.