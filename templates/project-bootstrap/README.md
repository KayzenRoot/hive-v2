# HIVE Project Bootstrap Template

Status: CANONICAL TEMPLATE
Purpose: make new projects start with the same governance, modularity, evidence, performance, security, review and continuity discipline used by HIVE.

## Bootstrap order
1. create repository;
2. copy this template skeleton;
3. fill project charter;
4. define scope, requirements, architecture and Definition of Done;
5. define module ownership/boundaries using `docs/architecture/MODULE-CONTRACT-TEMPLATE.md`;
6. create Decisions Ledger and initial ADRs;
7. create CURRENT checkpoint and canonical source hierarchy;
8. define quality/risk gates and test strategy;
9. define performance/resource budgets and proportional threat model;
10. define reproducible local environment/preflight;
11. configure Work Order, PR, issue, review/evidence contracts;
12. define documentation freshness rules;
13. discover actual CI/check names, then configure merge/protection policy;
14. run `docs/operations/BOOTSTRAP-READINESS-CHECKLIST.md`;
15. only then authorize the first bounded implementation Work Order.

## Required repository skeleton
```text
.github/
  CODEOWNERS
  ISSUE_TEMPLATE/
  pull_request_template.md
docs/
  architecture/
  checkpoints/
    CURRENT.md
    history/
  decisions/
    DECISIONS-LEDGER.md
  definition-of-done/
  evidence/
  operations/
  quality/
  requirements/
  review/
  scope/
  security/
  work-orders/
project/
  PROJECT-CHARTER.md
  MODULE-MAP.md
  QUALITY-PLAN.md
  RISK-POLICY.md
  TEST-STRATEGY.md
```

## Mandatory operating contracts
Every project bootstrapped from this template inherits these principles unless an explicit ADR overrides a project-appropriate default:
- repository truth outranks chat/model memory;
- one current checkpoint;
- one Work Order identity across issue/branch/PR/evidence;
- bounded Work Orders with explicit out-of-scope and expected blast radius;
- executor inspects existing repository before changes;
- executor uses documented reproducible environment/preflight;
- module ownership and dependency boundaries are explicit;
- context is progressive and impact-aware;
- deterministic tools before LLM inference;
- tests/evidence are objective proof and `Completed` is not evidence;
- reviews are delta-first and corrections start from rejected→corrected delta;
- risk tier controls verification depth and uncertainty expands proof;
- HIGH/CRITICAL defects block advancement;
- performance/resource behavior is part of correctness where applicable;
- security/trust-boundary changes receive proportional threat review;
- runtime modules define observability sufficient for diagnosis;
- derived guidance carries freshness/provenance and never replaces canonical source;
- release gates use broader verification than ordinary changes;
- user-facing executor prompts are PDF-only unless explicitly requested otherwise;
- checkpoint is updated after approved material state changes.

## Included hardening templates
- `docs/architecture/MODULE-CONTRACT-TEMPLATE.md`
- `docs/quality/PERFORMANCE-BUDGET.md`
- `docs/quality/RISK-GATE-MATRIX.md`
- `docs/security/THREAT-MODEL-TEMPLATE.md`
- `docs/operations/REPRODUCIBLE-ENVIRONMENT-CONTRACT.md`
- `docs/operations/DOCUMENT-FRESHNESS-CONTRACT.md`
- `docs/operations/BOOTSTRAP-READINESS-CHECKLIST.md`

## Default project metrics
Track at minimum when applicable:
- Time-to-Trusted-Merge;
- first-pass approval rate;
- executor orientation/implementation/verification/review wall-clock;
- correction cycles and rework causes;
- escaped defects by severity and recurrence;
- regressions caught pre-merge;
- selected/full test ratio and selector miss rate;
- build/test/proof cache valid reuse rate;
- context signal ratio;
- flaky test rate;
- architecture boundary/complexity violations;
- performance/resource regressions;
- documentation freshness violations.

Metrics never override correctness, security or data-integrity gates.

## Template philosophy
The template is modular and product-agnostic. New projects copy HIVE's engineering discipline, evidence model and delivery system, not HIVE-specific product architecture. Experimental HEDS technologies remain opt-in/evidence-gated until promoted by explicit project decision.