---
name: rust-api-contract
description: Keep Rust REST behavior and OpenAPI aligned when status, bodies, errors, headers, security requirements, or compatibility change.
license: MIT
---

# Rust API Contract

**Observable contract.** Identify what an existing client can distinguish: status, body presence and shape, media type, header, default, error identity, security requirement, and retry outcome. Follow each affected distinction from the source of truth through the served API to its consumers.

Determine whether the project is specification-first, annotation-generated, or uses another contract workflow. Update its actual source of truth and regeneration path, preserving its router integration and artifact policy. When generation is used, inspect the generated diff instead of silently editing the output.

Check effective security across global requirements, operation overrides, and alternatives. An omitted security declaration and an explicit public override can have different meanings. Document middleware-produced responses where consumers need them, while preserving the project's authentication model and public endpoints.

Keep runtime responses and schemas in agreement: absent versus null fields, defaults, enum evolution, status-specific payloads, error codes, and streaming media types. Compatibility depends on client assumptions as well as schema validity; an added response enum value can break exhaustive consumers. Do not universally label every additive or optional change safe or breaking.

Use the project's existing compatibility and lint tools when available. A deliberate breaking change follows its versioning or approval policy; do not invent an exception registry or require client generation without a consumer. Preserve error distinctions needed for recovery while avoiding disclosure of internal causes.

For review, describe old and proposed behavior and the affected client. For implementation, update the contract and exercise the changed observable through the mounted API. Schema generation proves neither runtime agreement nor consumer compatibility; report the evidence at its actual scope.
