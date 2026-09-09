# HEDS Project Bootstrap Readiness Checklist

Status: TEMPLATE

A new project is implementation-ready only when applicable items below are explicit.

## Truth and governance
- [ ] project charter/goal
- [ ] scope and out-of-scope
- [ ] requirements
- [ ] architecture/module boundaries
- [ ] Definition of Done
- [ ] decisions/ADR process
- [ ] active checkpoint
- [ ] backlog/first bounded WO

## Engineering contracts
- [ ] module ownership/contracts
- [ ] dependency/boundary policy
- [ ] Work Order and evidence format
- [ ] review verdict/gate standard
- [ ] risk matrix
- [ ] performance/resource budgets
- [ ] security/threat model proportional to risk
- [ ] observability expectations
- [ ] reproducible environment/preflight
- [ ] test strategy including real-use journeys where applicable

## Context efficiency
- [ ] canonical source hierarchy
- [ ] progressive-disclosure/bootstrap instructions
- [ ] derived-artifact freshness policy
- [ ] no executor is instructed to read the entire repository by default

## Git/repository
- [ ] branch/PR convention
- [ ] CODEOWNERS/ownership policy where useful
- [ ] real CI/check names discovered before protection rules
- [ ] merge policy
- [ ] evidence/artifact retention
- [ ] dependency/security automation appropriate to stack

## Release/recovery
- [ ] version/tag policy
- [ ] migration/rollback/recovery rules
- [ ] local deployment/runbook
- [ ] release evidence and DoD gate

## HEDS/UADS
- [ ] HEDS process adopted or explicit ADR exception
- [ ] UADS integration rule where available/applicable
- [ ] Time-to-Trusted-Merge baseline planned
- [ ] optional experimental HEDS technologies clearly separated from release-blocking NECESSARY scope

## STOP CONDITION
Do not begin broad product implementation while critical truth, module ownership, DoD, environment or verification gates remain ambiguous.