# Diagnostic queries

`queryStatistics` is the primary diagnostic surface. Call `operation: capabilities` for the
sources you need before composing anything — it returns the current fields, enum vocabularies,
allowed aggregations, filter operators and query defaults for that workspace. Treat that
response, not this file, as the source of truth for what exists today.

## The ladder

Work outward from intake. Stop when the evidence explains the claim.

| Hop | Source | Ask | Key fields |
|---|---|---|---|
| 1. Intake | `events` | Did the trigger fire at all? | `status`, `trigger`, `app`, `retries`, `is_replay`, `is_test` |
| 2. Outcome | `runs` | What happened to the runs it produced? | `status`, `automation_id`, `event_id`, `trigger`, `duration` |
| 3. Reason | `run_steps` | Which step stopped it, and why? | `status`, `type`, `category`, `message`, `run_id` |
| 4. Channel | `emails` / `messages` | Did the message reach the person? | `type`/`status`, `reason`, `sub_type`, `classification`, `error_type`, `code` |
| 5. Configuration | `searchAutomationTriggers` | Does the blueprint match the intent? | the trigger's filters, relationships, delays, safety limits |

The sources join on shared identifiers — `automation_id`, `event_id`, `run_id`, `run_step_id`,
`connection_id`, `template_id`, `conversation_id`. Use them to move between hops instead of
matching on timestamps.

## Constraints that are easy to get wrong

These cost a diagnosis if you learn them by trial and error.

- **Each query needs a `name`, and so does each metric.** A query without them is rejected as invalid.
- **`message` is filterable but not groupable** on `runs` and `run_steps`. Grouping by it fails.
  To see the reasons, aggregate it with `top_k` and group by something that is groupable,
  such as `type` and `status`.
- **The run-level `message` is often empty.** A cancelled or failed run frequently carries no
  reason of its own; the explanation lives on the step. Never conclude "no reason recorded"
  from `runs` alone — always descend to `run_steps` before saying so.
- **`run_steps.type` is the executed task action**, not the step's position. It tells you which
  capability failed (`send_email`, `start_conversation`, `update_field`, `data_lookup`, `path`,
  `delay`, `loop`, `filter`, and others). Group by it to localise the fault fast.
- **One email produces several `emails` rows**, one per provider event. Count unique emails with
  `count_distinct` on `provider_message_id`, never `count` on `id`.
- **`events` are pruned after a retention window.** A period older than the oldest stored event
  is reported as partial. A quiet older window means "not retained", not "nothing happened".
- Defaults worth knowing: the period defaults to the current calendar month and is capped at
  366 days; up to 10 queries per call; default limit 100, maximum 1000. Granularity is derived
  from the period unless you set it.
- `ai_usage` is restricted to super admins, and `credits` — not `runs` — is where spend lives.

## A worked first pass

Given "our interview feedback automation stopped working last week", one call answers most of it:

- query one, source `runs`, metric `count` of `id`, grouped by `status`, filtered to that
  `automation_id`, bucketed by day — shows whether volume or outcome changed, and when;
- query two, source `run_steps`, metrics `count` of `id` plus `top_k` of `message`, grouped by
  `type` and `status`, filtered to `status` in `failed`, `retrying`, `skipped` — names the reason;
- query three, source `events`, metric `count` of `id`, grouped by `status`, same filter and
  period — distinguishes "stopped firing" from "fired and then stopped early".

Read the three together. Falling event volume with unchanged run outcomes is an upstream or
connection problem. Steady events with a new step reason is a defect in the workflow or a
template. Steady events, steady outcomes and an unhappy user is usually a mismatch between the
automation's filters and what the person believed it covered — hop 5, not a repair.
