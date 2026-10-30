---
name: rust-axum
description: Implement or review axum routes, state, extractors, middleware, fallbacks, response mapping, and streaming behavior.
license: MIT
---

# Rust Axum

**Route tree.** Follow the affected request from the listener through routing and middleware to the handler and back. Layer order and scope are observable behavior. Keep the project's existing middleware policy; do not substitute a universal hardened chain.

Router::layer wraps routes and fallbacks already present when it is called. Successive layer calls put later layers outside earlier ones; ServiceBuilder ordering differs. route_layer runs only for matching routes and is useful when an unmatched path must remain a 404 rather than an authentication failure. Check the resolved axum and Tower versions for nesting, state, error, and fallback behavior.

Place a cross-cutting policy at the scope it actually governs. Check whether a concurrency layer has one shared capacity budget or independent state per route. Authentication, CORS, request identifiers, panic mapping, and overload behavior must cover the intended routes, including public probes and fallbacks. CORS is a browser response policy, not authentication or protection from non-browser callers.

Keep transport rejection mapping at the HTTP boundary using the project's response format. Extraction order, body consumption, content type, and size limits can change which rejection reaches the client. Validate caller-controlled identifiers before reflecting or logging them. Use matched route templates or a bounded fallback label for metrics.

A timeout around the handler future may not cover response-body streaming after headers. Check header, body, idle, and connection lifetimes separately when the requested change concerns them. Connection admission and slow-client protection may belong to the server or proxy rather than a router layer.

Use a mounted-router request to verify changed status, body, headers, rejection, or fallback behavior. Use a real listener for connection and wire claims. For review, trace existing safeguards before claiming one is missing; for implementation, retain framework choices and add only the coverage the changed mechanism needs.
