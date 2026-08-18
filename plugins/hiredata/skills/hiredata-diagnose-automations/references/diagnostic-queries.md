# Diagnostic queries

`queryStatistics` is the primary diagnostic surface. Call `operation: capabilities` for the
sources you need before composing anything unfamiliar — it returns the current fields, enum
vocabularies, allowed aggregations, filter operators and query defaults for that workspace.
Treat that response, not this file, as the source of truth for what exists today.

Contents:

1. The first pass — one call that answers most claims
2. The ladder
3. Constraints that are easy to get wrong
4. Performance limits and known gaps
5. Reading the three queries together

---

## 1. The first pass

Start here. One call, five queries, and it covers status distribution, step reasons, stuck
runs, volume ratios and trend. Substitute the automation ID and the period.

```json
{
  "workspace": "<id>",
  "operation": "query",
  "arguments": {
    "period": { "from": "<YYYY-MM-DD>", "to": "<YYYY-MM-DD>" },
    "granularity": { "unit": "day" },
    "queries": [
      {
        "name": "outcomes",
        "source": "runs",
        "metrics": [
          { "name": "run_count", "aggregation": "count" },
          { "name": "reasons", "aggregation": "top_k", "field": "message", "amount": 5 },
          { "name": "last_run", "aggregation": "max", "field": "started_at" },
          { "name": "avg_duration", "aggregation": "average", "field": "duration" }
        ],
        "groupBy": ["status"],
        "filters": [{ "field": "automation_id", "operator": "equals", "value": 0 }],
        "sort": [{ "field": "run_count", "direction": "desc" }]
      },
      {
        "name": "identity_and_scale",
        "source": "runs",
        "metrics": [
          { "name": "run_count", "aggregation": "count" },
          { "name": "distinct_records", "aggregation": "count_distinct", "field": "external_record_id" },
          { "name": "distinct_events", "aggregation": "count_distinct", "field": "event_id" }
        ],
        "groupBy": ["object", "app", "trigger"],
        "filters": [{ "field": "automation_id", "operator": "equals", "value": 0 }]
      },
      {
        "name": "step_reasons",
        "source": "run_steps",
        "metrics": [
          { "name": "step_count", "aggregation": "count" },
          { "name": "reasons", "aggregation": "top_k", "field": "message", "amount": 5 }
        ],
        "groupBy": ["type", "status"],
        "filters": [{ "field": "automation_id", "operator": "equals", "value": 0 }],
        "sort": [{ "field": "step_count", "direction": "desc" }],
        "limit": 50
      },
      {
        "name": "stuck_runs",
        "source": "runs",
        "metrics": [
          { "name": "run_count", "aggregation": "count" },
          { "name": "oldest", "aggregation": "min", "field": "started_at" },
          { "name": "newest", "aggregation": "max", "field": "started_at" }
        ],
        "groupBy": ["status"],
        "filters": [
          { "field": "automation_id", "operator": "equals", "value": 0 },
          { "field": "status", "operator": "includes", "value": ["running", "pending", "waiting", "scheduling"] }
        ]
      },
      {
        "name": "trend",
        "source": "runs",
        "metrics": [{ "name": "run_count", "aggregation": "count" }],
        "groupBy": ["time_bucket", "status"],
        "filters": [{ "field": "automation_id", "operator": "equals", "value": 0 }],
        "limit": 300
      }
    ]
  }
}
```

Read the result as a whole before querying anything else:

- `outcomes` gives the status split and, critically, `last_run`. An automation whose last run
  is weeks old has stopped, and that is usually a bigger finding than anything in the split.
- `identity_and_scale` gives you the human descriptor for the report, plus the two ratios in
  "Volume as a diagnosis". `run_count` far above `distinct_records` means records are being
  reprocessed, not changed.
- `step_reasons` names the fault. Group by `type` and `status`, aggregate `message` with
  `top_k` — `message` is filterable but **not groupable**.
- `stuck_runs` catches the runs that appear in no error count. Compare `oldest` to today.
- `trend` distinguishes "always did this" from "changed on a date". A weekday-shaped curve
  points upstream, not at the automation.

Add a `credits` query only when cost is part of the question, and run it as its own call —
see the performance limits below.

## 2. The ladder

Work outward from intake. Stop when the evidence explains the claim.

| Hop | Source | Ask | Key fields |
|---|---|---|---|
| 1. Intake | `events` | Did the trigger fire at all? | `status`, `trigger`, `app`, `object`, `retries`, `is_replay`, `is_test` |
| 2. Outcome | `runs` | What happened to the runs it produced? | `status`, `automation_id`, `event_id`, `trigger`, `duration`, `started_at` |
| 3. Reason | `run_steps` | Which step stopped it, and why? | `status`, `type`, `category`, `message`, `run_id` |
| 4. Channel | `emails` / `messages` | Did the message reach the person? | `type`/`status`, `reason`, `sub_type`, `classification`, `error_type`, `code` |
| 5. Configuration | the app UI | Does the blueprint match the intent? | filters, relationships, delays, safety limits, schedule |

The sources join on shared identifiers — `automation_id`, `event_id`, `run_id`, `run_step_id`,
`connection_id`, `template_id`, `conversation_id`. Use them to move between hops instead of
matching on timestamps.

### Hop 5 has no MCP tool today

This is the ladder's weak rung and it will cost you a diagnosis if you discover it by trial.

`searchAutomationTriggers` does **not** address workspace automations. It lists reusable
trigger blueprints from the template library, keyed by UUID, and it rejects the numeric
`automation_id` that every statistics source returns. Its `list` operation is also restricted
to super admins and commonly returns an empty set for a customer workspace.

So the configured filters, delays, schedule and safety limits are not readable over MCP from
an automation ID. What to do instead:

- Reconstruct what you can from the data. `runs.trigger`, `runs.object` and `runs.app` give
  the trigger type and scope. The `run_steps.type` sequence gives the workflow shape. A
  `send_limits_per_automation_exceeded` reason proves a limit exists and was reached, even
  though you cannot read its configured value.
- Then name explicitly what still needs the app UI, and who should look. "The configured send
  limit is not readable from the API; someone with UI access needs to check that one screen"
  is a legitimate and useful line in a report.
- Do not guess a configured value from behaviour and present it as fact.

## 3. Constraints that are easy to get wrong

- **Each query needs a `name`, and so does each metric.** A query without them is rejected as
  invalid.
- **`message` is filterable but not groupable** on `runs` and `run_steps`. Grouping by it
  fails. To see the reasons, aggregate it with `top_k` and group by something groupable, such
  as `type` and `status`.
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

## 4. Performance limits and known gaps

Learned the hard way. None of these are documented in the tool descriptions.

- **`credits` times out on grouped queries.** A `credits` query with `groupBy` over a multi-month
  period frequently exceeds the 60-second MCP timeout. Run `credits` alone, on the shortest
  period that answers the question, and prefer an ungrouped total. If you need per-automation
  billable volume, use `run_steps` filtered to `type` in `send_email`, `start_conversation`,
  `send_survey` with `status` `completed` — it is the operational equivalent and it is fast.
- **`events` filtered by `automation_id` can return zero rows** even when events plainly exist,
  because connector events are recorded before they are attributed to an automation and the
  field is nullable. Do not read an empty result as "the trigger never fired". Group by `app`,
  `object` and `trigger` over the same period instead, and reason about intake at that level.
- **`emails.template_id` is an integer; the email template library uses UUIDs.** There is no
  join between per-template send volume and template names. Infer the pattern from the
  library and the volume distribution, and say that you inferred it.
- **There is no automation name anywhere in the statistics sources.** See "Naming the
  automation" in SKILL.md.
- **Large `list` results can exceed the response limit** and get written to a file instead.
  When that happens, query the file with `python3`/`jq` rather than re-requesting with a
  smaller limit and losing coverage.

## 5. Reading the three queries together

Falling event volume with unchanged run outcomes is an upstream or connection problem. Steady
events with a new step reason is a defect in the workflow or a template. Steady events, steady
outcomes and an unhappy user is usually a mismatch between the automation's filters and what
the person believed it covered — hop 5, not a repair.

And steady everything with an enormous `runs ÷ finished` ratio is the sixth situation: nothing
is broken, but the automation should never have been invoked that many times. That is a
trigger-scope finding, and it is worth raising even when nobody complained about it.
