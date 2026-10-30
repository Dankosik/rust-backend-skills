---
name: rust-testing
description: Select, write, or review Rust backend tests for observable behavior, deterministic async coordination, and the boundary that contains the failure mechanism.
license: MIT
---

# Rust Testing

**Behavior.** Name the promise that could break and choose the smallest boundary that contains its mechanism. Reuse adequate existing coverage. Add cases for material failure modes, not for every implementation detail or topic mentioned by a skill.

Choose among a unit, coordinated async task, mounted router, loopback server, real dependency, or process according to the claim. A direct handler call omits middleware; an in-memory store does not prove PostgreSQL locking; a router request does not prove connection timeouts. Preserve the project's test libraries, infrastructure harness, and placement conventions instead of requiring Compose, testcontainers, or a separate integration crate.

Derive expectations independently from accepted behavior. Avoid private fields, call choreography, SQL spelling, or Debug text unless they are the actual contract. Assertions may use clear loops, tables, helpers, or properties when they preserve an independent oracle. A round trip alone can hide a defect shared by the encoder and decoder.

Use the real mechanism where the question depends on it. Doubles can isolate business behavior or inject a fault when they do not implement the behavior being asserted. Prefer protocol-faithful fixtures for external boundaries and keep service identity and credentials out of test data. Do not provision an unavailable environment just to close an optional claim.

Synchronize on explicit state, notification, or completion rather than elapsed sleeps. Bound waits and join or clean up owned tasks and processes. With Tokio paused time, use its clock and account for auto-advance; wall-clock and external-I/O behavior may require a different test. Avoid process-global environment races.

For a reproducible defect, observe the test fail for the reported behavior before accepting a fix; a compiler failure is not that observation. Property testing, mutation testing, fuzzing, Miri, and feature matrices are useful when a concrete invariant or risk warrants them, not universal completion gates.

Run the relevant project checks, ensure the selected tests actually executed, and report unavailable or skipped boundaries. Review assesses whether tests detect the relevant failure; it does not authorize rewriting them.
