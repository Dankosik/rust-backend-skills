---
name: rust-reliability
description: Reason about Rust backend deadlines, retries, overload, readiness, dependency failures, drain, and shutdown budgets.
license: MIT
---

# Rust Reliability

**Budget arithmetic.** Trace each wait, attempt, and cleanup stage against its parent deadline and terminal outcome. Read the project's existing timeout, admission, readiness, and shutdown owners before adding policy.

Include queue and pool acquisition, each attempt, backoff, response handling, and cleanup where they consume the budget. Propagate a deadline or remaining time rather than resetting a full timeout at every hop. Use accepted budgets where available; resolve routine open choices proportionally to the task and surface missing product or operational constraints when they determine correctness.

A retry needs a transient failure classification, bounded attempts, suitable backoff and jitter, and a safely repeatable effect. A timeout does not establish that a remote operation failed or stopped. Reconcile ambiguous outcomes or use operation identity before repeating effects. Check each proposed attempt count against the complete budget rather than proving one large count does not fit.

Bound queues, tasks, and expensive execution before work is admitted, and define overload behavior visible to callers. A circuit breaker is justified by the failure model, not as a default wrapper. Work accepted beyond a request's lifetime needs an explicit owner; durable guarantees require durable acceptance and recovery rather than an untracked spawn.

Define dependency startup and readiness consequences from the service's actual ability to serve. During shutdown, coordinate traffic withdrawal, accepted-work drain, dependency close, and telemetry within the platform's grace period. Stages draw from remaining time. An abort or expired wait does not prove side effects or blocking work have ended.

Verify the changed failure path with controlled coordination, an occupied capacity permit, a suitable clock, or a real process when lifecycle behavior is claimed. Report final disposition and residual work. Add only the policy and checks required by the requested change.
