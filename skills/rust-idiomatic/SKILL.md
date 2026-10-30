---
name: rust-idiomatic
description: Resolve Rust ownership, borrowing, traits, conversions, error identity, and async type boundaries while preserving caller-visible behavior.
license: MIT
---

# Rust Idiomatic

**Contracts.** Identify who owns a value, who may mutate it, what absence and failure mean, and what crosses a task boundary before changing representation. Preserve the requested behavior and the project's Rust baseline.

Borrow through slices, string slices, and paths when ownership is unnecessary; move owned values when responsibility transfers. Before adding a clone, Arc, or Mutex to satisfy the compiler, inspect data flow and borrow scope. Sharing an allocation does not synchronize mutation. A guard across an await needs an explicit atomicity and contention reason; do not shorten it in a way that breaks the invariant.

Use enums for meaningful alternatives and newtypes for distinctions that prevent real misuse. Option and Result preserve absence and failure. A validated type must maintain its invariant through every exposed construction and mutation path, including deserialization, conversions, defaults, and public fields; a validating constructor alone is insufficient.

Implement standard traits only where their semantics fit. Check consistency among equality, ordering, and hashing when mixing derived and manual implementations: equal values hash equally, total comparison agrees with equality, and partial comparison agrees with total comparison. Do not add traits merely to complete a set.

Keep typed errors where callers choose recovery, and preserve useful sources. Values sent to spawned tasks must satisfy that API's ownership, lifetime, and Send requirements; local tasks and borrowed futures have different bounds. Check object safety and supported async-trait patterns against the project's compiler and existing dispatch strategy rather than automatically boxing every future.

Prefer the clearer iterator or loop while preserving ordering, overflow behavior, allocation, and byte-versus-text semantics. Honor the project's unsafe policy; when unsafe is in scope, identify and justify its invariants instead of treating compilation as a soundness proof.

For review, explain the affected contract and consequence without editing. For implementation, make the smallest useful change and run checks that observe its behavior or type contract; neither cloning nor shared ownership is a defect by spelling alone.
