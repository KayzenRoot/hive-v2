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
- `CHAT_CONTINUITY_READY = true` for workflow/response-format reconstruction when GitHub is available.
- A fresh HIVE chat receiving `continue do chat anterior` or equivalent MUST bootstrap from repository sources rather than require screenshots, manual checkpoint uploads or user re-explanation.
- Canonical continuity protocol: `docs/operations/CHAT-CONTINUITY-PROTOCOL.md`.
- Canonical response/prompt delivery standard: `docs/operations/RESPONSE-AND-DELIVERY-STANDARD.md`.
- Canonical review standard: `docs/operations/REVIEW-STANDARD.md`.
- User-facing executor prompts, when authorized, are delivered as a downloadable PDF only. Do not provide OneBox/copyable full-prompt duplication unless the user explicitly requests it for that delivery.
- Future HIVE implementation/correction executor prompts use the globally installed UADS workflow where applicable and require UADS runtime/bootstrap evidence.

## HEDS engineering delivery truth
- `HEDS_PROCESS_READY = true` for governance/documentation/process adoption.
- `HEDS_AUTOMATION_IMPLEMENTED = false` until the review manifest generation, context capsule generation, proof/action cache, risk router, merge-queue integration, learning loop and related runtime tooling are actually implemented/tested.
- HEDS automation implementation epic: GitHub issue #75, blocked until the R22 source re-freeze is APPROVED.
- HEDS is the default implementation/review operating model for HIVE V2 once V2 implementation is authorized.
- Future new projects SHOULD bootstrap from `templates/project-bootstrap/` unless an explicit project ADR chooses otherwise.
- Primary delivery metric: `Time-to-Trusted-Merge`, not raw review duration.
- Canonical HEDS source: `docs/operations/ENGINEERING-DELIVERY-SYSTEM.md`.
- Canonical machine-readable review contract: `docs/review/review-manifest.schema.json`.
- Canonical decisions: ADR-025 and ADR-026.
- Engineering Digital Twin (EDT) is recorded by ADR-027 as `IMPORTANT / EXPERIMENT REQUIRED`; it is not a V2 completion blocker and does not expand frozen NECESSARY scope.

## Fresh-chat bootstrap minimum
When the user asks to continue from the previous HIVE chat, read at minimum:
1. this checkpoint;
2. `docs/source/AGENT-BOOTSTRAP.md`;
3. `docs/source/HIVE-V2-CANONICAL-SOURCE-MAP.md`;
4. `docs/operations/CHAT-CONTINUITY-PROTOCOL.md`;
5. `docs/operations/RESPONSE-AND-DELIVERY-STANDARD.md`;
6. `docs/operations/REVIEW-STANDARD.md`;
7. `docs/operations/ENGINEERING-DELIVERY-SYSTEM.md`;
8. the active issue/WO/PR/evidence named by the current state.

Then retrieve only the additional scope/DoD/architecture/requirements/round sources necessary for the requested increment.

## Completed in repository
- Repository initialized.
- R21 canonical round specification added.
- R22 canonical round specification added.
- Integrated test/debug architecture added.
- Impact-aware review operating model added.
- Evidence Bundle contract added.
- Change Impact Manifest schema added.
- R21/R22 ADR ledger and individual ADRs added.
- Canonical R01-R22 source map added.
- Memory-independent agent bootstrap contract added.
- Chat continuity protocol added.
- PDF-only response and executor-prompt delivery standard added.
- Review Standard upgraded to HEDS v2.
- HEDS engineering delivery system documented.
- Review Manifest schema added.
- Future-project bootstrap template added with project charter, quality plan and Work Order template.
- ADR-025 HEDS adoption and ADR-026 template-first bootstrap recorded.
- HEDS automation epic #75 recorded and gated.
- EDT research direction and ADR-027 documented without scope promotion.
- Frozen R01-R20 master identity verified from authoritative project source: `HIVE-MASTER-SOURCE-V2.0-FROZEN.md`, R20 Architecture Freeze Review, 2026-08-31.
- Exact-source preservation manifest added: `docs/source/SOURCE-PRESERVATION-MANIFEST.md`.
- Exact frozen-master import procedure added: `docs/source/MASTER-IMPORT-PROCEDURE.md`.
- Post-preservation reconciliation procedure added: `docs/source/R21-R22-HEDS-RECONCILIATION-PROCEDURE.md`.
- Compact Source Pack contract added: `docs/source/V2-SOURCE-PACK-CONTRACT.md`.
- R22 re-freeze audit checklist added: `docs/review/R22-REFREEZE-AUDIT-CHECKLIST.md`.

## Exact source preservation status

`SOURCE_PRESERVATION_STATE = IDENTIFIED`

### Repository-contained
- R21 round specification.
- R22 round specification.
- R21/R22 integrated architecture.
- R21/R22 scope/DoD delta.
- review/evidence/governance contracts.
- workflow continuity and response-format standards.
- HEDS process/template contracts.
- preservation manifest and import procedure.
- reconciliation, Source Pack and re-freeze readiness procedures.

### Exact Git import still required
- `HIVE-MASTER-SOURCE-V2.0-FROZEN.md` containing complete R01-R20 research provenance and frozen architecture/source definition.

Do not replace this exact historical master with a model-generated reconstruction or summary. Search snippets, partially rendered content and model-visible excerpts are insufficient for byte-complete archival preservation.

## Pending before V2 implementation bootstrap
1. Make the exact original `HIVE-MASTER-SOURCE-V2.0-FROZEN.md` artifact importable by the Git write path.
2. Import it unchanged to `docs/archive/HIVE-MASTER-SOURCE-V2.0-FROZEN.md` following `docs/source/MASTER-IMPORT-PROCEDURE.md`.
3. Record source SHA-256, byte length when available, Git blob SHA and preserving commit SHA.
4. Audit header identity and complete R01-R20 provenance; promote `SOURCE_PRESERVATION_STATE` to VERIFIED only with objective evidence.
5. Execute `docs/source/R21-R22-HEDS-RECONCILIATION-PROCEDURE.md`.
6. Produce compact canonical V2 Source Pack according to `docs/source/V2-SOURCE-PACK-CONTRACT.md`.
7. Perform R22 architecture/source re-freeze using `docs/review/R22-REFREEZE-AUDIT-CHECKLIST.md`.
8. If APPROVED, update checkpoint to `MEMORY_INDEPENDENT = true` and authorize first V2 implementation Work Order using HEDS.
9. Begin HEDS automation implementation under issue #75 as part of the approved implementation program.

## Blocker
The exact R01-R20 frozen master is confirmed in the project File Library and can be inspected, but the current file-search surface exposes rendered/search content rather than a raw local/mounted file suitable for exact Git upload and byte-hash verification. Therefore `SOURCE_PRESERVATION_STATE` remains IDENTIFIED and no reconstructed substitute is permitted.

## Next necessary increment
Obtain an exact importable representation of `HIVE-MASTER-SOURCE-V2.0-FROZEN.md`, then execute the preservation procedure. No HIVE V2 feature implementation before that gate.
