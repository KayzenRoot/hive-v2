# ADR-022 — Verified Repair Transaction

Status: Accepted for V2 consolidation

## Context
A plausible patch is not proof of repair, especially when the original defect is intermittent, agentic or stateful.

## Decision
A repair transaction must, when technically feasible: preserve/reproduce the original failure, localize the first causal divergence, apply the smallest safe patch, rerun the original reproducer, run impacted verification, create a regression lock and record defect evidence.

## Consequences
Defect repair becomes auditable and reusable by Test Intelligence. Exceptions require explicit technical justification and elevated review.
