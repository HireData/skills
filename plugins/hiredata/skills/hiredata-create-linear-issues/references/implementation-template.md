# Implementation issue template

## Summary

Link the product specification and define the implementation slice.

## Technical decisions

Record only decisions supplied or verified by engineering: architecture, data ownership, execution timing, compatibility, and failure strategy.

## Affected layers

Group known components by database/model, API/contracts, domain/actions/jobs, frontend, integrations, and observability. File lists are appropriate when engineering supplied them.

## Data and API contract

Describe migrations, models, DTOs/resources, identifiers, versioning/backwards compatibility, and output shape at the required level.

## Execution flow

Describe triggers, ordering, idempotency, retries, partial failure, and performance/caching implications.

## Implementation checklist

Use ordered, independently verifiable slices.

## Test and rollout plan

Cover unit/integration/end-to-end tests, migrations, compatibility, staging verification, production verification, and rollback/monitoring where relevant.

## Out of scope and follow-ups

Name deliberately deferred APIs, surfaces, refactors, or cleanup.

## Open technical questions

Do not invent answers. Resolve before calling the issue build-ready or mark the estimate provisional.

## Acceptance criteria

Keep criteria outcome-level and traceable to the implementation checklist and product specification.
