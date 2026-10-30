---
name: rust-delivery
description: Implement or review Rust backend CI, build artifacts, containers, releases, and deployment verification within the existing delivery platform.
license: MIT
---

# Rust Delivery

**Artifact identity.** Follow the source revision through checks, build, packaging, publication, and any requested deployment. Each gate must observe the artifact and behavior it claims. Preserve the existing CI provider, build layout, registry, and release policy.

Read the pipeline's actual triggers, path filters, permissions, job dependencies, and failure propagation. A skipped check can be legitimate, but a successful aggregate must not conceal a required failed or cancelled job. Changes to classifiers and conditions need evidence that the affected surface still reaches its check. Do not introduce a particular job name, Make target, version registry, or pipeline structure.

Keep toolchain, dependency resolution, generated artifacts, and build options coherent according to the project. Check the target platform and runtime requirements of the resulting binary or container, not just the builder. Advisory, secret, license, SBOM, and provenance tools belong where the changed surface or release policy requires them; the pack does not mandate installing a fixed scanner suite.

For an image claim, exercise the image's actual entrypoint, configuration, filesystem permissions, probes, and shutdown behavior at the relevant scope. Tests against a host binary alone do not establish container behavior. Preserve deployment-specific grace periods and listener policy rather than imposing a fixed timeout or base image.

Before a requested release or deployment, keep source, artifact digest, credentials, destination, and applicable approvals explicit. Publication and tag promotion should be verified from the destination. Local success does not prove remote CI, registry content, signing verification, or production rollout. Maintain recovery and rollback appropriate to the requested external effect.

Review reports a broken or missing link with its consequence without mutating external systems. Implementation performs authorized changes and applicable checks; mentioning release mechanics does not authorize publishing or deploying. Report pending external evidence precisely instead of calling a prepared artifact shipped.
