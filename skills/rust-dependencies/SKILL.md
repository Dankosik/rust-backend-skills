---
name: rust-dependencies
description: Assess or change Cargo dependencies, features, toolchains, editions, and library choices for a Rust backend.
license: MIT
---

# Rust Dependencies

**Resolution.** Explain what Cargo actually selects before changing declarations. Reuse adequate existing code and dependencies; a maintained library is preferable for a general mechanism when its semantics and maintenance cost fit the requirement.

For a meaningful new dependency or upgrade, compare the actual behavior needed, supported Rust version, feature footprint, maintenance, licensing, and relevant advisories. Check official documentation or source for the resolved version. Record the decision where the project normally keeps it; a small change does not require a new research directory or a survey of unrelated alternatives.

Inspect the resolved dependency and feature graph, including duplicate versions when they affect interoperability or size. Cargo feature unification can enable a feature through another edge; default-features = false on one declaration does not disable it everywhere. Check platform-specific, build, and development dependency effects when they matter.

Preserve the project's workspace dependency strategy and lockfile policy. Applications and reusable libraries can have different resolution requirements. Let Cargo update lockfiles, inspect the intended change, and avoid unrelated upgrades or bypassing integrity checks. Do not require every dependency to disable defaults if those defaults are part of the accepted contract.

Keep compiler, minimum supported Rust version, edition, and CI coverage distinct. A rust-version declaration is not a compiler pin or proof of minimum-version compatibility. An edition or toolchain upgrade needs a task-relevant reason and applicable checks. Coordinate integration crates such as telemetry bridges using their documented compatibility, not a permanent minor-version formula.

Build scripts and procedural macros execute code during builds and belong in the trust assessment. Reuse existing advisory and license tools where the changed surface warrants them; adding a dependency does not itself authorize a security audit or release.

Verify affected default and selected feature paths. All-features success does not establish the default build, and mutually exclusive features may intentionally reject all-features. Report runtime compatibility separately from successful compilation.
