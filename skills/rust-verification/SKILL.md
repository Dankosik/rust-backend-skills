---
name: rust-verification
description: Verify a specified Rust backend claim or assess whether existing build, test, runtime, CI, or deployment evidence supports it.
license: MIT
---

# Rust Verification

**Evidence boundary.** Define the observable whose absence would make the selected check fail. A claim cannot be broader than that boundary. Preserve the requested verification scope and the project's required checks; do not assume a particular workspace, lint level, command, or process suite.

Formatting establishes formatting. A build establishes compilation for its toolchain, target, and features. Tests establish the cases and mechanisms actually exercised. A mounted router covers its chain; a running process can cover startup and shutdown; a real database can establish transactional behavior. Structural validation of skill files establishes packaging, not improved model decisions.

Check command selection and preconditions. A filter matching zero tests, a skipped integration suite, a missing server, or an unrelated aggregate cannot support the intended result. A manifest's minimum Rust version needs actual compiler coverage for a compatibility claim. A dependency tree explains resolution, not runtime correctness.

Reuse evidence while relevant source, configuration, toolchain, and environment remain unchanged. Record the command, selected scope, fresh or reused status, and material gaps. Select extra checks only for a concrete unresolved question or required policy; do not create new infrastructure merely to widen an ordinary completion claim.

Distinguish local behavior from remote CI, container behavior, telemetry delivery, release publication, and production readback. Independent review requires an independent reviewer; a repeated self-review does not become independent by changing its label. A failed check is not automatically a code defect, and missing evidence is not automatically success or failure.

Verification-only work does not edit files unless the user asks for fixes. Finish with supported claims and the exact remaining gaps. If a fix is authorized, repair failures introduced by it and rerun the affected checks without silently weakening the requested proof.
