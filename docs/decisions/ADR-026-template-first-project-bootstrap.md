# ADR-026 — Template-First Project Bootstrap

Status: ACCEPTED
Date: 2026-09-08

## Context
New projects repeatedly spend time recreating repository structure, documentation conventions, review rules, checkpoint behavior and executor guidance. Inconsistent starts increase ambiguity, context hunting and defects.

## Decision
All new projects SHOULD begin from the HEDS project bootstrap template unless an explicit project ADR documents why another process is better.

The template provides governance/process structure, not project-specific product architecture.

Minimum bootstrap includes:
- project charter;
- scope;
- requirements;
- architecture;
- Definition of Done;
- decisions ledger/ADRs;
- current checkpoint;
- module map/ownership;
- quality/test/risk plan;
- Work Order conventions;
- review/evidence schemas;
- issue/PR templates;
- CI/required-check policy;
- continuity/bootstrap instructions.

## Consequences
Executors receive smaller, clearer context and spend less time discovering repository intent. Reviews become more uniform and transferable across projects.
