# Portability and verification

## Source identity

Source: `Dankosik/rust-service-template-rest`, commit `38a3723660b71849be222397699625ef5c308473`. Only the 18 `rust-*` skills were used. Workflow orchestrators, planning methods, task-ledger instructions, and template code were not copied.

All skill bodies were reviewed and rewritten for standalone use. Renames:

| Template | Standalone |
| --- | --- |
| rust-coder | rust-implement |
| rust-structural-quality | rust-design |
| rust-delivery-platform | rust-delivery |

Other skill names are retained. MIT notices are included at repository and skill level.

## Removed assumptions

| Area | Standalone decision |
| --- | --- |
| Crate graph | Reuse the project's module and crate boundaries; no prescribed service/config/health/infra hierarchy |
| Tokio lifecycle | Use the existing task owner; no required bootstrap tracker, token hierarchy, or runtime-lifecycle document |
| axum | Inspect actual middleware ordering and scope; no fixed chain or universal CORS policy |
| API contract | Follow the actual specification source; no mandatory utoipa, generated YAML path, error catalog, or exception registry |
| SQLx | Follow existing pool, transaction, and migration ownership; no profile gate, repository closure API, or all-migrations-in-one-transaction rule |
| Configuration | Keep current sources, namespace, precedence, blank-value semantics, and reload policy; no APP prefix or secrets-directory requirement |
| Errors | Preserve public and recovery contracts; no mandatory thiserror, closed problem catalog, or fixed degradation/exit-code policy |
| Dependencies | Use actual workspace, feature, and lockfile policy; no fixed edition, compiler pin, or telemetry minor-version formula |
| Telemetry | Preserve the existing stack; no prescribed facade, event vocabulary, cached readiness implementation, or diagnostics listener |
| Tests | Reuse the existing harness; no mandatory Compose, rejected testcontainers, fixed process suite, or rule forbidding all loops in test bodies |
| CI and release | Follow existing artifact gates; no named jobs, scripts, Make commands, signing chain, scanner suite, or fixed grace period |
| Safety and scope | Follow repository unsafe/lint policy; review remains read-only and ordinary implementation does not authorize release |

The reusable semantics remain: cancellation and completion differ, blocking work can outlive its waiter, middleware order changes behavior, ambiguous commit outcomes need reconciliation, and a check supports only the boundary it actually exercises.

## Semantic review cases

The following cases guide the author review of the instructions. They are not executed model evaluations or benchmark results.

| Existing project / request | Expected guidance |
| --- | --- |
| Single-crate axum service; add an endpoint | Extend the existing router and owner; no crate split or new middleware architecture |
| Configuration uses SERVICE_ variables and layered TOML | Preserve those sources and precedence; no APP rename |
| OpenAPI YAML is the hand-maintained source of truth | Edit that source and its consumers; do not introduce utoipa |
| Blocking work holds capacity after its requester times out | Keep admission tied to actual execution and observe completion; do not release the permit with the waiter |
| A bounded-channel send loses a select branch | Inspect message loss and capacity reservation against the accepted delivery contract |
| SQLx loses its connection while committing a charged operation | Preserve unknown-outcome classification and reconcile identity before repeating the charge |
| Project uses testcontainers for PostgreSQL | Reuse it; no Compose migration or fake database proof |
| Project permits reviewed unsafe code or non-pedantic Clippy | Preserve policy; inspect relevant invariants rather than imposing template bans |
| A caller asks only for diagnosis or API review | Return evidence and findings; do not edit, publish, or install infrastructure |
| CI build passes; user asks whether production is deployed | Report missing deployment readback; compilation cannot establish rollout |

## API references checked during extraction

The pack has no dependency on these particular versions. Resolve documentation against each consuming project's versions before relying on an API detail.

- [Tokio 1.54.1 select cancellation safety](https://docs.rs/tokio/1.54.1/tokio/macro.select.html#cancellation-safety).
- [Tokio spawn_blocking lifecycle](https://docs.rs/tokio/1.54.1/tokio/task/fn.spawn_blocking.html).
- [axum 0.8.9 middleware ordering](https://docs.rs/axum/0.8.9/axum/middleware/index.html#ordering).
- [SQLx 0.9.0 Transaction lifecycle](https://docs.rs/sqlx/0.9.0/sqlx/struct.Transaction.html).
- [Agent Skills specification](https://agentskills.io/specification).

## Validation boundary

`python scripts/check.py` uses the maintained `skills-ref` validator for the skill format, then checks packaged licenses, manifest identity, catalogue coverage, and local Markdown links. CI runs that same command.

Release verification also uses the skill-creator and plugin-creator validators and the pinned Skills CLI to discover and copy the pack into an isolated project. Native plugin manifest validation does not establish native host installation. No baseline/candidate LLM experiment, cross-model quality result, or production-service validation is claimed.
