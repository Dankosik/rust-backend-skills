---
name: rust-tokio
description: Implement or review Tokio tasks, cancellation, select branches, locks, channels, blocking work, and runtime shutdown.
license: MIT
---

# Rust Tokio

**Ownership.** Identify who admits work, observes failure, requests cancellation, and waits for completion. Reuse the project's existing lifecycle mechanism; do not require a particular tracker, token hierarchy, or runtime layout.

Dropping a JoinHandle detaches its task. Cancellation requests and abort calls do not establish completion: observe the join result where completion matters, including panic and cancellation. Keep service-owned work with an owner that survives a request timeout. Detached best-effort work needs a deliberate lifecycle and effect policy.

select! drops losing branch futures. Check cancellation safety for the exact methods used: read_exact can consume a prefix before cancellation, and cancelling a bounded-channel send can discard the pending message. Preserve state or reserve capacity when the contract requires it. Use biased ordering only for a real priority and account for starvation.

Inspect locks for callback reentry, lock ordering, blocking work, and guards crossing await. Shorten critical sections while preserving atomicity. An await need not yield when the future is immediately ready; bound per-poll work in hot loops. A synchronous blocking call remains blocking inside an async function.

Bound admission before submitting blocking or CPU-heavy work. Move the capacity permit into actual execution until it ends or unwinds; a waiter timing out must not release capacity while work still runs. A started spawn_blocking closure cannot be stopped by aborting its handle. Use cooperative cancellation where possible and account for residual work and side effects during retries and shutdown. Choose a separate CPU executor only when the workload warrants it.

Use Tokio's clock for paused-time tests. Choose interval missed-tick behavior from the job's semantics rather than universally catching up or delaying. Runtime shutdown may wait for blocking work; shutdown_timeout stops waiting without terminating running closures. Signal-handler installation can affect process-wide behavior, so preserve the project's signal ownership.

Verify ordering through explicit coordination, notifications, or joins with bounded waits. Report actual completion separately from cancellation, and keep implementation or review within the requested path.
