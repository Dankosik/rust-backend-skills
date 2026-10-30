---
name: rust-config
description: Implement or review Rust service configuration sources, precedence, defaults, validation, secret handling, and reload behavior.
license: MIT
---

# Rust Config

**One owner per key.** Trace a configuration value from accepted sources and precedence through decoding and validation to the runtime reader. Preserve the existing loader, namespace, formats, and reload policy.

Distinguish absent, blank, malformed, defaulted, and explicitly disabled values. Their meaning comes from the project's contract, not an automatic fallback. Check how the actual loader coerces booleans, numbers, durations, byte sizes, enums, and paths. Resolve unknown-field behavior intentionally, including compatibility with shared configuration when relevant.

Put a default and its validation with the existing owner. Use types that express the runtime distinction rather than passing unchecked strings deep into the service. Cross-field rules belong where the needed values and policy meet. A budget default needs a reason tied to the workload or accepted operational requirement, not an arbitrary number that makes a check pass.

Secrets may come from the project's environment, mounted files, or secret provider. Preserve the supported sources and ensure errors, Debug output, startup summaries, and examples do not disclose values. Diagnostics should identify the key and rule. A redacting wrapper does not help if another formatting or conversion path exposes its contents.

Read process environment at the existing configuration boundary rather than scattering reads through handlers. Avoid process-global environment mutation in parallel tests; use the existing injection, subprocess, or serialization strategy when needed. For reloadable settings, define snapshot consistency, validation failure behavior, and resource reconfiguration before replacing live values.

Verify the changed precedence, decoding, validation, or redaction behavior using focused cases. Update examples or deployment configuration only where the user-visible contract changes. Do not introduce a new source, format, mandatory policy document, or reload mechanism for an unrelated key addition.
