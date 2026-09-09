# HEDS — Engineering Quality & Delivery Scorecard

Status: CANONICAL MEASUREMENT CONTRACT / THRESHOLDS REQUIRE CALIBRATION

## Objective
Optimize engineering as a multi-objective system. Speed alone is not success.

## Non-negotiable dominance rule
Correctness, security, data integrity and required verification dominate speed/cost metrics. A faster flow that misses a HIGH/CRITICAL defect fails promotion.

## Scorecard families

### Quality
- escaped defects by severity;
- regression recurrence;
- first-pass approval rate;
- correction cycles;
- selector false-negative/miss rate;
- invalid proof/cache reuse incidents;
- flaky proof rate.

### Delivery speed
- Time-to-Trusted-Merge;
- executor orientation time;
- implementation wall-clock;
- verification wall-clock;
- Sol review wall-clock;
- correction wall-clock;
- queue/idle time.

### Context/token efficiency
- fresh/cached input tokens;
- retrieved vs sent context;
- context signal ratio;
- context reduction;
- provider/proof/cache reuse;
- deterministic work substituted for LLM calls.

### Architecture/maintainability
- module-boundary violations;
- unexpected blast-radius expansion;
- dependency cycles/coupling trend;
- complexity-budget violations;
- orphan/dead-code candidates validated;
- documentation freshness violations.

### Performance/resource
- user-visible latency/regression;
- CPU/GPU/memory/I/O/storage deltas;
- build/test wall-clock and valid cache hit rate;
- local deployment/recovery time where relevant.

## Anti-gaming rules
- never reward fewer tests without selector-quality evidence;
- never reward lower tokens when required context/evidence was omitted;
- never reward smaller diffs created by hiding generated/migration/dependency impact;
- never reward first-pass approval if review depth was weakened;
- track severity-weighted escapes, not raw bug count alone;
- keep holdout benchmark scenarios to detect overfitting.

## Baselines and targets
Numeric targets are not canonical until measured on declared reference scenarios/environments. Record baseline ID, environment fingerprint, sample period and methodology.

## Review cadence
Use trends to improve HEDS, not to punish individual increments. Investigate regressions and promote process changes only with controlled evidence.