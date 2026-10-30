---
name: rust-errors
description: Preserve Rust backend failure identity, recovery decisions, HTTP error mapping, cleanup outcomes, and process exit semantics.
license: MIT
---

# Rust Errors

**Failure semantics.** Follow a failure from the operation that knows what happened to the boundary that reports it. Preserve distinctions that change caller recovery, durable outcome, or operator action; not every hop needs a new wrapper.

Use the project's typed errors and existing libraries. Classify by variants, codes, or sources rather than matching display strings. Add context that identifies the operation without disclosing credentials, request payloads, or personal data. An opaque application-boundary report may be appropriate; do not impose one error crate or enum per module.

Map errors to HTTP, RPC, job outcomes, or exit codes at the relevant boundary. Keep the documented public format and stable codes. Sanitize unexpected internal failures while retaining diagnostic causes internally. A declared response can be intentionally defensive; absence of a currently reachable producer does not alone make the contract wrong.

Separate failed, cancelled, timed-out, and outcome-unknown operations. A timeout can stop waiting while a remote effect or blocking task continues. A retry is a new attempt with its own safety requirements, not an error-handling default. Do not turn a failure into an empty result, default, or success exit unless that is the accepted degradation policy.

Where completion can fail or lose data, use an explicit operation whose result an owner observes: commit, flush, close, or join. Drop handles best-effort release and cannot by itself establish durable completion; avoid blocking or panicking during destruction. Process exit can bypass destructors, so preserve the existing shutdown path when cleanup matters.

Inspect panic policy and build profile before assuming a panic can be caught. A spawned task's panic needs an observed join result. Treat unwrap and expect according to reachability, invariants, and repository policy rather than introducing blanket lint rules.

For review, explain the false-success or recovery risk. For implementation, check the changed mapping and outcome at the caller-visible boundary, including the underlying effect when relevant. Do not require unrelated failure modes or new error infrastructure.
