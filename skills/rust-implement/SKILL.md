---
name: rust-implement
description: Implement specified Rust backend behavior within the project's existing architecture, runtime, and technical choices.
license: MIT
---

# Rust Implement

**Execution.** Start from the requested behavior and its existing owner. Read the affected code and callers before changing it. Preserve settled technical choices outside the requested change; a clear task does not require a new design phase.

Extend the existing path. A responsibility may belong to a function, module, crate, handler, or lifecycle owner; do not introduce a crate hierarchy, repository layer, task tracker, or dependency injection framework merely because another project uses one. Keep acquisition and effects separate from non-trivial decisions when that makes the current behavior easier to understand and verify.

Reuse the affected code, standard library, and declared dependencies first. A general mechanism may justify a maintained crate when its behavior and maintenance cost fit the requirement. Use supported extension points before custom wrappers. A new abstraction needs a present responsibility, variation, or dependency direction.

Make ownership, effects, and failure paths visible. Inspect the far side of changed boundaries: callers matching an error, resources dropped after cancellation, configuration validation, transaction completion, and shutdown that must now wait. Resolve a borrow conflict from the real lifetime before adding a clone, shared owner, or lock.

Use the project's toolchain, features, formatting, lint, build, and test policy. Select checks for the affected behavior and retain required release gates. A dependency change includes its intended resolution and applicable compatibility checks.

Complete the requested implementation and fix failures it introduces. Reproduce an available reported defect at the boundary that observes it, and retain useful regression coverage. Report changed behavior, actual verification, and material gaps without turning unrelated cleanup, deployment, or new infrastructure into completion requirements.
