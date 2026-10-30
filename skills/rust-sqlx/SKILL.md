---
name: rust-sqlx
description: Implement or review SQLx pools, PostgreSQL queries, transactions, migrations, and database-backed behavior in Rust services.
license: MIT
---

# Rust SQLx

**Durable outcome.** Judge a database change by what is committed, what can race, and what a caller may safely retry. Preserve the project's database ownership, transaction API, and migration policy.

Trace connection configuration, pool creation, acquisition deadlines, transaction scope, and shutdown. Reuse the existing pool where its lifecycle and configuration fit. Account for pool wait time inside the operation's budget, and avoid holding a transaction across unrelated network work. Keep credentials out of DSNs shown in diagnostics.

Use bound parameters for data. Dynamic identifiers and ordering need controlled construction or an allow-list; binding a value cannot make an arbitrary SQL identifier safe. SQLx compile-time macros validate against a schema or offline metadata, not the production transaction semantics. Keep metadata in sync when the project uses offline checking.

Establish which owner commits or rolls back. SQLx initiates rollback when an unfinished Transaction is dropped; this is not an observed successful explicit rollback. A connection failure during commit can leave the outcome unknown. Reconcile by operation identity before repeating a possibly committed effect. Retry recognized serialization or deadlock failures only when the complete transaction and any surrounding effects are safely repeatable.

Use database constraints and suitable locking or isolation for concurrent invariants; an application-level precheck alone does not prevent competing writes. Preserve SQLSTATE and structured error information needed for conflict and retry decisions instead of matching display strings.

Follow the project's migration tool and deployment sequence. Keep applied migration history immutable unless the environment explicitly permits rewriting it. Assess rolling compatibility, lock duration, and backfill cost; do not require every migration to be transactional when PostgreSQL operations or the existing tool need otherwise.

Pure mapping or classification can use unit tests. Commit, isolation, locking, constraint, migration, and pool-lifecycle claims need the relevant behavior against PostgreSQL. Reuse the existing database harness; do not replace it with SQLite, an in-memory store, or a new container framework merely for convenience. Report any unavailable database proof.
