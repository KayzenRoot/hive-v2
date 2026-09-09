# HIVE V2 — Source Governance Index

Read in this order for canonical-source preservation work:

1. `../checkpoints/CURRENT.md`
2. `HIVE-V2-CANONICAL-SOURCE-MAP.md`
3. `SOURCE-PRESERVATION-MANIFEST.md`
4. `MASTER-IMPORT-PROCEDURE.md`
5. `SOURCE-PRESERVATION-EVIDENCE-TEMPLATE.md`
6. `AGENT-BOOTSTRAP.md`
7. `../transition/V1-TRANSITION-READINESS-SNAPSHOT.md` for the current V1→V2 transition validity basis
8. issue #66 for active consolidation/refreeze evidence

Rules:
- never reconstruct the frozen R01-R20 historical master from model memory or snippets;
- preserve the exact original artifact before compact Source Pack finalization;
- derived summaries/indexes do not replace the archival source;
- only objective preservation evidence may promote `SOURCE_PRESERVATION_STATE`.


Current preservation state at the latest checkpoint is `IMPORTABLE`, not `VERIFIED`. Exact local source evidence is recorded, but the byte-identical Git archive commit remains a hard gate.
