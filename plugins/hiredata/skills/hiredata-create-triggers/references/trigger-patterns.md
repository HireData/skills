# Trigger patterns

## Choose the type

| Need | Trigger pattern |
|---|---|
| React to a created, updated, or changed ATS record | Event-based |
| Act relative to a date stored on a record | Date-based |
| Act annually on a person's birth date | Birthday |
| Run a recurring batch or review | Scheduled |
| Let a user deliberately start a workflow | Manual |

Verify the exact types exposed by the current HireData MCP.

## Name clearly

Use the shortest name that identifies object, event, and timing. Event names usually read naturally in the past tense, while schedules and manual actions usually read as present-tense actions. Respect current product length limits returned by the MCP.

Examples:

- `Application Created`
- `Interview Ended + 30m`
- `Candidate Availability Weekly`
- `Send Vacancy Update`

## Filter safely

- Convert the user's population into explicit field/operator/value clauses.
- Distinguish a record's current state from a transition into that state.
- Treat empty, null, absent, and stale values as distinct when the source does.
- Estimate trigger volume before activating high-frequency events.
- Add deduplication or transition checks when updates can fire repeatedly.

## Select relationships for later steps

Work backward from the final action. If a later step needs a candidate, recruiter, vacancy, application, contact, owner, sender, or client, make sure the trigger exposes a valid relationship path to it. Do not guess through an unsupported chain.

For Carerix, keep its domain terms distinct: a Match represents an application relationship; Vacancy and Publication are different objects. Verify exact workspace labels and relationships through the MCP because configurations differ.
