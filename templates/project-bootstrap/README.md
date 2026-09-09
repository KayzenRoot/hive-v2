# HIVE Project Bootstrap Template

Status: CANONICAL TEMPLATE
Purpose: make new projects start with the same governance, documentation, review, test and continuity discipline used by HIVE.

## Bootstrap order

1. create repository;
2. copy this template skeleton;
3. fill `PROJECT-CHARTER.md`;
4. define `SCOPE.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md` and `DEFINITION-OF-DONE.md`;
5. create `DECISIONS-LEDGER.md` and first ADRs;
6. create `CURRENT.md` checkpoint;
7. configure Work Order, PR and issue templates;
8. enable review manifest/evidence contracts;
9. define risk policy and test layers;
10. configure CI, required checks and merge policy;
11. create initial project map/module ownership;
12. only then authorize implementation.

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
  requirements/
  review/
  scope/
  work-orders/
project/
  PROJECT-CHARTER.md
  MODULE-MAP.md
  QUALITY-PLAN.md
  RISK-POLICY.md
  TEST-STRATEGY.md
```

## Mandatory operating contracts

Every project bootstrapped from this template inherits these principles unless an explicit ADR overrides them:

- repository truth outranks chat/model memory;
- one current checkpoint;
- one Work Order identity across issue/branch/PR/evidence;
- executor inspects existing repository before changes;
- context is progressive and impact-aware;
- deterministic tools before LLM inference;
- tests are objective proof;
- `Completed` is not evidence;
- reviews are delta-first;
- corrections are reviewed from the rejected→corrected delta first;
- risk tier controls verification depth;
- HIGH/CRITICAL defects block advancement;
- release gates use broader verification than ordinary changes;
- user-facing executor prompts are PDF-only unless explicitly requested otherwise;
- checkpoint is updated after approved material state changes.

## Default project metrics

Track at minimum:
- Time-to-Trusted-Merge;
- executor orientation time;
- implementation wall-clock;
- verification wall-clock;
- review wall-clock;
- correction cycles;
- escaped defects;
- regressions caught pre-merge;
- selected/full test ratio;
- build/test cache hit rate;
- context signal ratio;
- reused proof rate;
- flaky test rate;
- complexity delta;
- rework causes.

## Template philosophy

The template is intentionally modular. New projects should not copy HIVE-specific product architecture. They copy HIVE's engineering discipline, evidence model and delivery system, then define their own product sources.
