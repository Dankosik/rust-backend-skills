---
name: rust-design
description: Assess or change Rust backend module, crate, trait, and dependency boundaries when cohesion, ownership, or unnecessary structure is the issue.
license: MIT
---

# Rust Design

**Cohesion.** For each proposed structure, name the current responsibility or constraint it carries. Ask what becomes harder if it is removed. Preserve the project's accepted architecture; a single crate and a workspace can both have clear ownership.

Read the existing dependency directions and callers. Put a change with the code that owns its behavior, lifecycle, or contract. A separate crate is useful when it enforces a needed boundary, independent API, dependency direction, or build constraint; a tidy name alone is insufficient. A module can carry a responsibility without becoming a crate.

A trait with one implementation can protect a real consumer boundary or enable dynamic dispatch. A trait whose only purpose is to mock internal choreography may add more coupling than it removes. Judge helpers by the semantic rule they make visible, not their call count. Names such as common or utils invite scrutiny of responsibility, not automatic rejection.

Before adding a parallel path, registry, error classifier, compatibility shim, or wrapper, locate the existing owner and consider extending it. Preserve a compatibility path when current consumers need it; identify activation and removal conditions only when deprecation is in scope. Do not invent a migration to satisfy a preferred architecture.

Make effects and non-trivial decisions easy to distinguish without adding a layer solely for that separation. A file split should clarify independent reasons to change, not satisfy a line-count target. Check a realistic next change to see whether the proposed structure reduces the number of owners that must agree.

Review reports need a reachable maintenance or correctness consequence, not just a named smell. For requested refactoring, preserve public behavior, error identity, ordering, and resource lifetime, and verify at the affected boundaries.
