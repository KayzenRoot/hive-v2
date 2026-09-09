# HIVE V2 — Agent Bootstrap Contract

Purpose: allow any fresh chat, coding agent, IDE agent, reviewer, or executor to reconstruct HIVE V2 without prior conversational context.

## Startup sequence

Every new HIVE V2 agent session MUST:

1. read `docs/checkpoints/CURRENT.md`;
2. read `docs/source/HIVE-V2-CANONICAL-SOURCE-MAP.md`;
3. resolve the current Decisions Ledger;
4. resolve frozen scope, DoD, architecture and requirements referenced by the checkpoint/source map;
5. read only the round specifications relevant to the requested increment, expanding context progressively;
6. inspect Git base/head and current Work Order before making changes;
7. treat repository files and objective evidence as higher authority than remembered chat content.

## Memory prohibition

Previous-chat/model memory MAY help locate a source, but MUST NOT be the source of truth for:
- approved functionality;
- scope classification;
- architectural decisions;
- implementation status;
- test status;
- checkpoint state;
- release readiness;
- Definition of Done claims.

When remembered context conflicts with Git, the agent must stop the conflicting assumption and reconcile against repository evidence.

## R01-R22 preservation rule

The complete frozen R01-R20 master plus R21/R22 specifications constitute the research/design provenance of HIVE V2. No round may be dropped from the canonical map merely because a later compact Source Pack summarizes it.

The compact Source Pack is an execution index. It is not permission to delete, rewrite, or discard the comprehensive historical master.

## Implementation authorization gate

Do not generate or execute the first HIVE V2 implementation Work Order until:
- complete exact R01-R20 frozen source is in Git;
- R21/R22 reconciliation is complete;
- compact V2 Source Pack exists;
- R22 architecture/source re-freeze audit verdict is APPROVED;
- checkpoint explicitly authorizes implementation.

## Review rule

Review the smallest trustworthy delta first. Use deterministic evidence, Change Impact Manifest, Evidence Bundle, selected verification, and progressive context expansion. Reuse prior proof only when its validity fingerprint remains unchanged.

## Closure rule

A session may claim project progress only from repository evidence. `Completed` without tests/evidence is not proof.
