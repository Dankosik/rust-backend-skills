---
name: rust-observability
description: Design or change Rust service logs, tracing spans, metrics, and health probes for a concrete operational question.
license: MIT
---

# Rust Observability

**Operator evidence.** Start with the operational question, then choose the smallest signal that answers it. Preserve the project's tracing, logging, metrics, exporter, and health stack; do not assume a telemetry crate or private diagnostics listener exists.

Keep global subscriber or exporter initialization with the application's existing lifecycle owner. Libraries emit signals through the chosen interfaces rather than installing a global subscriber. Check request context propagation before manually threading or duplicating identifiers. A correlation identifier is not authenticated identity.

Metrics labels have a cardinality and disclosure budget. Prefer route templates and bounded outcome categories over raw paths, user identifiers, peer addresses, or error strings. Respect the backend's naming, units, aggregation, and histogram conventions. Add a metric when existing signals cannot answer the question, not to mirror each function.

Use spans to relate operations and events to record meaningful outcomes. Avoid logging bodies, credentials, tokens, or unbounded caller-controlled strings. Redaction must survive error chains and Debug formatting. Check sampling, queue pressure, and export failure behavior when the change affects overhead or signal loss.

Liveness and readiness are control inputs. Define what an unhealthy dependency means for traffic admission before adding a probe. Keep health checks bounded and account for staleness; synchronous and cached probes have different costs and failure semantics. Do not turn a health endpoint into an expensive dependency fan-out by accident.

Verify the changed event, label, span relationship, or probe outcome at the interface the operator consumes. Local emission does not establish exporter delivery, collector ingestion, dashboard correctness, or alert execution. Report those boundaries honestly and do not add dashboards or a lifecycle audit unless requested.
