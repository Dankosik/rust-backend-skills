---
name: rust-debugging
description: Diagnose an uncertain Rust backend defect, compiler failure, flaky async test, hang, incorrect response, startup problem, or shutdown overrun.
license: MIT
---

# Rust Debugging

**Causality.** Locate the first observable divergence between intended and actual behavior. Choose an observation that can disprove the leading explanation. Preserve the user's diagnostic or fix scope and unrelated technical decisions.

Separate compile and lint failures from configuration, startup, request, task, and shutdown failures. Read structured errors and their causes before inferring a subsystem failure. Establish the meaning of exit codes and event names from the current project.

Reproduce at the smallest boundary that retains the mechanism: a pure function, a coordinated async task, a mounted router, a loopback protocol peer, the database, or the process. Keep relevant input, features, configuration, stdout, stderr, exit status, and timing. Redact secrets before recording captures. Use the existing logging and diagnostic switches rather than changing configuration conventions.

For async flakes, inspect unbounded waits, sleeps used as synchronization, mixed clock sources, unobserved task completion, contention, and select branches that discard partially completed work. A hang is a symptom, not proof of a missing owner: trace the wait and wakeup dependencies. Resolve borrow-checker failures from actual ownership and lifetime before adding sharing or cloning.

Change one causal variable at a time. Minimize a reproducer only while it retains the reported failure. After an ineffective fix, revisit the explanation rather than stacking retries, delays, panic catches, or swallowed errors. Keep unrelated baseline failures distinct.

Diagnosis can finish with a supported cause or the next discriminating observation and does not authorize edits. A requested fix changes the causal owner, replays the failure, retains useful regression coverage, removes temporary instrumentation, and reports actual verification and remaining uncertainty. Do not turn a focused investigation into a repository-wide audit.
