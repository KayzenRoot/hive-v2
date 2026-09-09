# ADR-021 — Operational Behavior Is Correctness

Status: Accepted for V2 consolidation

## Context
A system can pass unit/integration tests while behaving incorrectly in real use, such as spawning excessive agents, conversations, retries or token usage.

## Decision
Operational side effects are part of functional correctness when the feature contract defines them. HIVE must support resource envelopes and runtime-behavior assertions for agents, conversations, retries, fan-out, tokens/quota, CPU/RAM, orphan state and concurrency.

## Consequences
Release evidence must include applicable real-use journeys. A correct output with prohibited operational behavior is a failed verification result.
