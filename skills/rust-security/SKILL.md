---
name: rust-security
description: Assess or implement Rust backend controls at identity, authorization, input, secret, network, and resource-consumption boundaries.
license: MIT
---

# Rust Security

**Attacker paths.** Trace caller-controlled input across a trust boundary to the enforcement point, protected resource, and observable outcome. Preserve the requested scope and the project's security policy. Existing middleware or deployment controls may enforce a property outside the handler; inspect them before claiming a missing control.

Separate authentication, resource authorization, and tenant scope. A request identifier, possession of a resource ID, or a CORS policy is not authorization. Test decisions against the actual principal, tenant, action, and resource. Missing identity or policy should follow the accepted denial contract rather than silently selecting a default tenant.

Bound attacker-controlled work before spending it: decode size and complexity, concurrency, connection lifetime, outbound work, and queue growth. Memory safety does not prevent resource exhaustion. Identify which limits belong to the application, server, reverse proxy, or provider, and verify claims at that boundary instead of assuming a hardened chain exists.

Keep credentials and sensitive payloads out of logs, error responses, Debug output, examples, and diagnostic bundles. For configurable outbound destinations, consider redirects, address resolution, network reachability, and credential forwarding; request-controlled destinations need an explicit use-case and policy. Preserve the project's legitimate proxy and provider choices.

Check listener exposure, diagnostic routes, forwarded-header trust, and deployment network policy when changed. Unsafe code and dependency findings need evidence at their relevant boundary; do not infer soundness from compilation or vulnerability from an advisory name without reachability and version context.

For review, report a concrete trigger, enforcement gap, consequence, and confidence; absent tests alone do not establish exploitability. Review stays read-only unless fixing is requested. For implementation, pair a new control with focused denial coverage that would detect its bypass, and keep positive supported use working. Do not expand an ordinary change into a full security audit.
