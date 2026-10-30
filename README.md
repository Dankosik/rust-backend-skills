# Rust Backend Skills

Small, independent skills for Rust backend development with Tokio, axum, and SQLx.

These instructions capture practical ways to work with coding agents on Rust services: make task ownership explicit, preserve API and failure contracts, reason about database outcomes, and verify the behavior that changed.

Use them in an existing project. They do not require the author's service template, crate layout, middleware chain, configuration prefix, Make targets, or CI provider. Your project supplies the versions, architecture, and validation policy.

## Install

Install selected skills or the entire pack into your current project:

```sh
npx skills@1.5.25 add "Dankosik/rust-backend-skills#v0.1.0" --agent codex --skill '*' --copy
```

Use `--skill rust-tokio` for one skill or `--agent claude-code` for standalone Claude Code placement. To inspect the pack first:

```sh
npx skills@1.5.25 add "Dankosik/rust-backend-skills#v0.1.0" --list
```

The Skills CLI requires Node.js; the installed skills are Markdown instructions and have no runtime dependency. The repository also includes native Codex and Claude Code plugin manifests. It is not yet registered in the author's marketplace or either provider's public directory. Use one installation method per copy to avoid duplicate skills.

## Choose the decision

| Skill | Focus |
| --- | --- |
| [rust-implement](skills/rust-implement/SKILL.md) | Implement clear requirements within existing architecture and technical choices |
| [rust-idiomatic](skills/rust-idiomatic/SKILL.md) | Ownership, borrowing, types, traits, conversions, and error identity |
| [rust-design](skills/rust-design/SKILL.md) | Cohesion, module and crate boundaries, traits, and useful abstractions |
| [rust-tokio](skills/rust-tokio/SKILL.md) | Task lifetime, cancellation, select branches, blocking work, and shutdown |
| [rust-axum](skills/rust-axum/SKILL.md) | Routes, extractors, middleware ordering, fallbacks, and streaming |
| [rust-api-contract](skills/rust-api-contract/SKILL.md) | OpenAPI, runtime agreement, security declarations, and client compatibility |
| [rust-sqlx](skills/rust-sqlx/SKILL.md) | Pools, queries, transactions, ambiguous commits, and migrations |
| [rust-config](skills/rust-config/SKILL.md) | Sources, precedence, defaults, validation, secrets, and reload behavior |
| [rust-errors](skills/rust-errors/SKILL.md) | Failure distinctions, recovery, public error mapping, and cleanup outcomes |
| [rust-dependencies](skills/rust-dependencies/SKILL.md) | Cargo resolution, features, library choices, and toolchain compatibility |
| [rust-debugging](skills/rust-debugging/SKILL.md) | Reproduction, causal diagnosis, async flakes, and hangs |
| [rust-observability](skills/rust-observability/SKILL.md) | Logs, spans, metrics, health probes, and operational evidence |
| [rust-performance](skills/rust-performance/SKILL.md) | Comparable latency, throughput, CPU, allocation, and memory measurements |
| [rust-reliability](skills/rust-reliability/SKILL.md) | Deadlines, retries, capacity, readiness, drain, and shutdown budgets |
| [rust-security](skills/rust-security/SKILL.md) | Identity, authorization, input boundaries, secrets, and resource exhaustion |
| [rust-testing](skills/rust-testing/SKILL.md) | Observable behavior, appropriate test boundaries, and deterministic coordination |
| [rust-delivery](skills/rust-delivery/SKILL.md) | CI, build artifacts, containers, releases, and exact artifact identity |
| [rust-verification](skills/rust-verification/SKILL.md) | What build, test, runtime, CI, and deployment evidence actually establishes |

Select a skill for the decision that needs attention, not every technology mentioned in the task. Skills are independent; none requires loading the others or following a fixed sequence. The Tokio, axum, and SQLx skills apply when those libraries are already selected, not as a request to migrate to them.

## Use

Ask naturally or select a skill through your agent's explicit invocation:

- “Use rust-implement to add this endpoint within our existing design.”
- “Use rust-tokio to fix a worker that continues after the request times out.”
- “Use rust-axum to check whether authentication changes our unmatched-route response.”
- “Use rust-sqlx to review what happens if the connection drops during commit.”
- “Use rust-config to add a setting without changing our environment-variable prefix.”
- “Use rust-debugging to diagnose this shutdown hang without editing files.”

Review and diagnosis stay read-only unless changes are requested. Implementation includes applicable checks and repair of introduced failures. A skill does not authorize publication, deployment, or an unrelated architecture change. Check official documentation for the versions resolved by your project when API behavior matters.

## Scope and evidence

The pack follows the [Agent Skills format](https://agentskills.io/specification). Structural validation and installation checks establish that the package can be discovered and installed. They do not establish improved code quality across models or prove a performance or security benefit.

See [portability and verification](docs/portability.md) for the extraction decisions, semantic review cases, and validation scope. These are maintainer notes, not prerequisites for using a skill.

For Rust command-line utilities, see [rust-cli-skills](https://github.com/Dankosik/rust-cli-skills). Related backend packs: [Go](https://github.com/Dankosik/golang-backend-skills) and [Java / Spring](https://github.com/Dankosik/java-backend-skills).

## Maintain

Keep instructions independent and decision-focused. Preserve non-obvious failure semantics, remove assumptions about one repository, and improve guidance against a realistic task that exposed a weakness.

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/python scripts/check.py
```

## Origin and license

Adapted from the Rust skills in [rust-service-template-rest at 38a3723660b71849be222397699625ef5c308473](https://github.com/Dankosik/rust-service-template-rest/tree/38a3723660b71849be222397699625ef5c308473/.agents/skills). This standalone pack is maintained here; the template retains its own repository-specific instructions. There is no automatic synchronization between them.

[MIT license](LICENSE). Each installed skill includes its license.
