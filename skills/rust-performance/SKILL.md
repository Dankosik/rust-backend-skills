---
name: rust-performance
description: Audit, measure, or optimize Rust backend latency, throughput, CPU, allocation, memory, startup, or capacity with comparable evidence.
license: MIT
---

# Rust Performance

**Evidence.** Distinguish an audit, a measurement, and an optimization. Define the workload and metric before changing code. Preserve required behavior, quality, and resource limits; a faster but different operation is not a valid improvement.

Separate request latency percentiles, throughput, CPU, allocation rate, retained memory, peak RSS, startup time, and binary size. Use comparable build profiles and run built artifacts directly when measuring process behavior. Hold toolchain, features, inputs, concurrency, and environment constant, and report variance rather than selecting a favorable sample.

Inspect where cost moves as concurrency grows: retained bodies, queues, caches, task populations, pool waits, and blocking execution. Borrowing and streaming can reduce copies but also change lifetime, backpressure, and error timing. Optimize a demonstrated hot-path clone rather than mechanically removing every clone.

Choose evidence that separates causes: a profile for CPU, allocation evidence for churn, a realistic microbenchmark for an isolated operation, or a load test for service behavior. For measured command comparisons, use hyperfine --warmup 3 when available and appropriate; state warm-cache effects. Account for profiler overhead and existing runtime instrumentation.

Treat allocator, LTO, codegen-unit, panic-strategy, and profile-guided changes as alternatives with trade-offs. panic = abort cannot preserve unwind-based panic recovery. Do not introduce unsafe code, a custom allocator, a runtime replacement, or new instrumentation solely because it is commonly associated with speed.

An audit without runtime data reports code-supported properties and bottleneck hypotheses separately. A benchmark can finish without a code change. An authorized optimization includes before-and-after behavior and performance evidence at the claimed scope. If results are inconclusive, retain the simpler correct implementation and state the gap.
