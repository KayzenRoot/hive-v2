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
- HEDS is the default implementation/review operating model for HIVE V2 once V2 implementation is authorized.
- Future new projects SHOULD bootstrap from `templates/project-bootstrap/` unless an explicit project ADR chooses otherwise.
- Primary delivery metric: `Time-to-Trusted-Merge`, not raw review duration.
- Canonical HEDS source: `docs/operations/ENGINEERING-DELIVERY-SYSTEM.md`.
- Canonical machine-readable review contract: `docs/review/review-manifest.schema.json`.
- Canonical decisions: ADR-025 and ADR-026.

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
- Frozen R01-R20 master identity verified from authoritative project source: `HIVE-MASTER-SOURCE-V2.0-FROZEN.md`, R20 Architecture Freeze Review, 2026-08-31.

## Exact source preservation status

### Repository-contained
- R21 round specification.
- R22 round specification.
- R21/R22 integrated architecture.
- R21/R22 scope/DoD delta.
- review/evidence/governance contracts.
- workflow continuity and response-format standards.
- HEDS process/template contracts.

### Exact Git import still required
- `HIVE-MASTER-SOURCE-V2.0-FROZEN.md` containing complete R01-R20 research provenance and frozen architecture/source definition.

Do not replace this exact historical master with a model-generated reconstruction or summary. A compact Source Pack may be generated only as a derived execution artifact after the immutable master is preserved.

## Pending before V2 implementation bootstrap
1. Import the exact immutable `HIVE-MASTER-SOURCE-V2.0-FROZEN.md` into Git.
2. Record source integrity metadata/hash from the Git-preserved artifact.
3. Reconcile R21/R22 + HEDS process decisions against complete V2 scope, requirements, architecture and DoD without silently altering frozen product architecture.
4. Produce compact canonical V2 Source Pack from repository-contained sources.
5. Perform R22 architecture/source re-freeze audit.
6. If APPROVED, update checkpoint to `MEMORY_INDEPENDENT = true` and authorize first V2 implementation Work Order using HEDS.

## Blocker
The exact R01-R20 frozen master source itself is known and verified, but this environment does not currently expose its raw bytes as a local file that can be uploaded directly through the GitHub connector. Therefore a byte-complete Git import has not been falsely claimed.

## Next necessary increment
Complete exact R01-R20 frozen master Git preservation. No HIVE V2 feature implementation before that gate.
