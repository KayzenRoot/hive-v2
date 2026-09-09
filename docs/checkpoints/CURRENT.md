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
- User-facing executor prompts, when authorized, are delivered as one complete copyable OneBox plus a downloadable PDF containing the same canonical prompt.
- Future HIVE implementation/correction executor prompts use the globally installed UADS workflow where applicable and require UADS runtime/bootstrap evidence.
- Material reviews preserve the established verdict/evidence/progress/remaining-work/next-step response pattern.

## Fresh-chat bootstrap minimum
When the user asks to continue from the previous HIVE chat, read at minimum:
1. this checkpoint;
2. `docs/source/AGENT-BOOTSTRAP.md`;
3. `docs/source/HIVE-V2-CANONICAL-SOURCE-MAP.md`;
4. `docs/operations/CHAT-CONTINUITY-PROTOCOL.md`;
5. `docs/operations/RESPONSE-AND-DELIVERY-STANDARD.md`;
6. `docs/operations/REVIEW-STANDARD.md`;
7. the active issue/WO/PR/evidence named by the current state.

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
- Response and executor-prompt delivery standard added.
- Canonical Sol review standard added.
- Frozen R01-R20 master identity verified from authoritative project source: `HIVE-MASTER-SOURCE-V2.0-FROZEN.md`, R20 Architecture Freeze Review, 2026-08-31.

## Exact source preservation status

### Repository-contained
- R21 round specification.
- R22 round specification.
- R21/R22 integrated architecture.
- R21/R22 scope/DoD delta.
- review/evidence/governance contracts.
- workflow continuity and response-format standards.

### Exact Git import still required
- `HIVE-MASTER-SOURCE-V2.0-FROZEN.md` containing complete R01-R20 research provenance and frozen architecture/source definition.

Do not replace this exact historical master with a model-generated reconstruction or summary. A compact Source Pack may be generated only as a derived execution artifact after the immutable master is preserved.

## Pending before V2 implementation bootstrap
1. Import the exact immutable `HIVE-MASTER-SOURCE-V2.0-FROZEN.md` into Git.
2. Record source integrity metadata/hash from the Git-preserved artifact.
3. Reconcile R21/R22 against complete V2 scope, requirements, architecture and DoD.
4. Produce compact canonical V2 Source Pack from repository-contained sources.
5. Perform R22 architecture/source re-freeze audit.
6. If APPROVED, update checkpoint to `MEMORY_INDEPENDENT = true` and authorize first V2 implementation Work Order.

## Blocker
The source itself is known and verified as the approved R20 frozen master, but this environment does not currently expose its raw bytes as a local file that can be uploaded directly through the GitHub connector. Therefore a byte-complete Git import has not been falsely claimed.

## Next necessary increment
Complete exact R01-R20 frozen master Git preservation. No feature implementation before that gate.
