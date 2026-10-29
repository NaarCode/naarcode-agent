# Architecture and workflow

The supplied version separates CLI entry points, project-agnostic orchestration, specialized product skills, research and AI providers, validation, permissions, limited external tools, and persistent SQLite task/audit records.

## Stages

`QUEUED → RESEARCHING → GENERATING → VALIDATING → READY → PREPARING_MEDIA → CREATING_DRAFT → VERIFYING_WRITE → COMPLETED`

Failure and cancellation transitions are modeled separately. Dry-run execution ends before any remote mutation. A possible ambiguous write is reconciled by lookup rather than blindly repeating a POST.

## Reliability and provenance

Research results retain source identifiers and URLs. A fact resolver evaluates source tiers and disagreements, allowing only verified facts into generation. Typed schemas and deterministic project rules validate the candidate draft.

External actions are performed by narrowly scoped tools, not directly by the text-generation provider. Credentials are passed through a secret store. Write permission requires several independent project switches.

## Scope and caveats

The reviewed source contains an industrial-product-specific skill and WooCommerce draft workflow. It is not a deployed multi-customer autonomous platform. External-provider integration and production acceptance are outstanding. This public overview intentionally leaves out specific endpoints, implementation code, policy internals and business-specific schemas.
