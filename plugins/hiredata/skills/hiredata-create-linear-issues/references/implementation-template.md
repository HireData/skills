# Implementation issue template

## Summary

Link the product specification and define the implementation slice.

## Technical decisions

Record only decisions supplied or verified by engineering: architecture, data ownership, execution timing, compatibility, and failure strategy.

## Affected layers

Group known components by data model, API or contracts, domain execution, frontend, integrations, and observability. Include file lists only when engineering supplied them.

## Data and API contract

Describe migrations, models, identifiers, versioning, backwards compatibility, and output shape at the required level.

## Execution flow

Describe triggers, ordering, repeat safety, retries, partial failure, and performance implications.

## Implementation checklist

Use ordered, independently verifiable slices.

## Test and rollout plan

Cover automated tests, compatibility, staging and production verification, monitoring, and rollback where relevant.

## Out of scope and follow-ups

Name deliberately deferred surfaces, refactors, or cleanup.

## Open technical questions

Do not invent answers. Resolve them before calling the issue build-ready or mark the estimate provisional.

## Acceptance criteria

Keep criteria outcome-level and traceable to the product specification and implementation checklist.
