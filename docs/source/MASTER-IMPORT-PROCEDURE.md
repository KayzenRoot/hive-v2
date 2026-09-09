# HIVE V2 — Frozen Master Import Procedure

Status: CANONICAL OPERATING PROCEDURE
Applies to: `HIVE-MASTER-SOURCE-V2.0-FROZEN.md`

## Objective
Import the original frozen R01-R20 master into Git without reconstruction or semantic drift, then produce objective preservation evidence.

## Preconditions
- the exact original artifact is available through a path or connector capable of exposing the full file for write/upload;
- target repository is `KayzenRoot/hive-v2`;
- current checkpoint still identifies exact source preservation as the next NECESSARY gate;
- no later ADR has superseded this procedure.

## Procedure

1. Inspect source metadata and first header block.
2. Verify expected identity from `SOURCE-PRESERVATION-MANIFEST.md`.
3. Compute SHA-256 over the exact source artifact before transformation.
4. Record source byte length where available.
5. Do not normalize line endings, rewrap Markdown, re-encode sections, summarize, correct spelling, or otherwise edit the historical source during archival preservation.
6. Commit the exact artifact to `docs/archive/HIVE-MASTER-SOURCE-V2.0-FROZEN.md` on a dedicated documentation/governance branch.
7. Fetch the Git-preserved file and verify expected header identity.
8. Record Git blob SHA and preserving commit SHA.
9. When the execution environment permits raw-byte verification, re-hash the preserved bytes and require equality with the original source SHA-256. If raw-byte re-hash is unavailable, state that limitation and do not falsely claim byte-hash equality.
10. Audit the master for presence of complete R01-R20 provenance and the V0.1 inherited baseline.
11. Update issue #66 with preservation evidence.
12. Update `docs/checkpoints/CURRENT.md` from `IDENTIFIED` to `PRESERVED` or `VERIFIED` only according to actual evidence.
13. Only after VERIFIED preservation proceed to R21/R22/HEDS reconciliation and compact Source Pack generation.

## Failure cases

STOP and keep the gate blocked if:
- only excerpts/search snippets are accessible;
- source is truncated;
- the file is a draft/working variant rather than the frozen artifact;
- source identity differs from the expected header;
- upload requires reconstructing the document from model-visible text;
- hashes disagree;
- an unexplained transformation changes the artifact.

## Required review result

A successful preservation review must report:
- `SOURCE_PRESERVATION_VERDICT = VERIFIED`;
- source SHA-256;
- Git path;
- blob SHA;
- commit SHA;
- header identity PASS;
- R01-R20 provenance PASS;
- reconstruction used: NO;
- remaining reconciliation actions.

Anything less remains `CORRECTION REQUIRED` or `BLOCKED`.
