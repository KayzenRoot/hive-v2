# ADR-019 — Impact-Aware Selective Verification

Status: Accepted for V2 consolidation

## Context
Full-suite execution after every change becomes prohibitively slow in mature repositories and does not guarantee real-use correctness.

## Decision
Use change-impact analysis plus risk/uncertainty to select the smallest defensible verification portfolio. Full-suite remains a calibration/release/high-risk mechanism, not the universal default.

## Consequences
Faster normal iteration; selector quality becomes a first-class correctness concern; selector misses must be measured by shadow full-suite calibration; uncertainty always widens verification.
