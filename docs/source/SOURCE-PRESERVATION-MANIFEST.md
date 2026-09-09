# HIVE V2 — Source Preservation Manifest

Status: CANONICAL GOVERNANCE CONTRACT
Purpose: preserve the identity and integrity requirements of the frozen historical HIVE V2 master before any R22 re-freeze or V2 implementation authorization.

## Required historical artifact

Expected filename: `HIVE-MASTER-SOURCE-V2.0-FROZEN.md`

Expected identity:
- title: `HIVE — MASTER SOURCE V2.0 — FROZEN ARCHITECTURE EDITION`
- status: `FROZEN / ARCHITECTURE + SOURCE DEFINITION APPROVED`
- research revision: `R20 — Final Architecture Freeze Review / ADR Ratification`
- date: `2026-08-31`
- organization: `Next Labs`
- project: `HIVE`
- role: frozen comprehensive architecture/source-definition reference preserving the approved V0.1 baseline and complete R01-R20 research provenance
- freeze meaning: architecture/source definition approved; implementation is NOT declared complete

## Integrity rule

The historical master MUST be imported from the original artifact bytes/text. A model-generated reconstruction, paraphrase, summary, regenerated Markdown, copy assembled from search snippets, or manually retyped substitute is not acceptable as the immutable historical source.

## Required Git preservation path

Preferred archival path:

`docs/archive/HIVE-MASTER-SOURCE-V2.0-FROZEN.md`

A different path requires an explicit checkpoint/ADR update. The imported historical artifact must remain immutable after preservation. Corrections or later architecture decisions belong in new versioned sources, ADRs, reconciliation documents or successor masters.

## Required preservation evidence

Before `MEMORY_INDEPENDENT = true` may be declared, record:
- source filename;
- source byte length if available;
- SHA-256 of the exact source artifact;
- Git blob SHA;
- preserving commit SHA;
- archival repository path;
- import timestamp;
- identity/header verification result;
- confirmation that the artifact is not a model reconstruction;
- confirmation that R01-R20 provenance is present;
- reviewer verdict.

## Source availability states

### IDENTIFIED
The artifact identity is known and content can be inspected, but exact bytes are not yet available to the Git import mechanism.

### IMPORTABLE
The exact original source is available as a local/mounted/connector file that can be written to Git without reconstruction.

### PRESERVED
The exact source is committed to the archive path and preservation evidence/hash is recorded.

### VERIFIED
A Sol audit confirms identity, provenance, hash evidence and archive immutability requirements.

Current state: `IMPORTABLE`.

Current raw-source evidence:
- byte length: `1334369`;
- SHA-256: `990c441d5797ee3f8ec81a1f3337f83bb0516fcc0c2a79ef0ef9f4a150b020ee`;
- expected Git blob SHA: `6e2620854cb3180e02ac4c18fe21c93bb5dffdcd`;
- evidence: `docs/evidence/source-preservation/HIVE-MASTER-SOURCE-V2.0-FROZEN-EVIDENCE.md`;
- exact archive commit remains pending.

## Promotion gates

The following remain blocked until state `VERIFIED`:
1. repository-complete R01-R22 canonical history claim;
2. compact canonical V2 Source Pack finalization;
3. R22 architecture/source re-freeze verdict;
4. `MEMORY_INDEPENDENT = true`;
5. first HIVE V2 implementation Work Order.

## No-shortcut rule

No performance, schedule, token or convenience objective may weaken this gate. Preserving exact project truth is cheaper than debugging a silently corrupted architecture history later.
