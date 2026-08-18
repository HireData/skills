# Email performance queries

All of this comes from `queryStatistics`, source `emails`. Call
`queryStatistics (operation: capabilities)` with `sources: ["emails"]` for the current field
list — it is a wide source and the vocabulary changes.

Contents:

1. The first pass
2. Frequency and template cadence
3. Sender and provider cuts
4. Reputation and the migration window
5. Constraints that are easy to get wrong
6. Reference rates

---

## 1. The first pass

One call. Gives the health baseline, the monthly rate series, and the machine-open split.

```json
{
  "workspace": "<id>",
  "operation": "query",
  "arguments": {
    "period": { "from": "<YYYY-MM-DD>", "to": "<YYYY-MM-DD>" },
    "granularity": { "unit": "month" },
    "queries": [
      {
        "name": "lifecycle_total",
        "source": "emails",
        "metrics": [{ "name": "unique_emails", "aggregation": "count_distinct", "field": "provider_message_id" }],
        "groupBy": ["type"],
        "sort": [{ "field": "unique_emails", "direction": "desc" }]
      },
      {
        "name": "lifecycle_monthly",
        "source": "emails",
        "metrics": [{ "name": "unique_emails", "aggregation": "count_distinct", "field": "provider_message_id" }],
        "groupBy": ["time_bucket", "type"],
        "limit": 300
      },
      {
        "name": "machine_opens",
        "source": "emails",
        "metrics": [{ "name": "unique_emails", "aggregation": "count_distinct", "field": "provider_message_id" }],
        "groupBy": ["time_bucket", "is_machine_open", "is_mpp_open"],
        "filters": [{ "field": "type", "operator": "equals", "value": "open" }],
        "limit": 300
      }
    ]
  }
}
```

From `lifecycle_total`, compute the four baseline rates in the SKILL.md health table. From
`lifecycle_monthly`, build the open- and click-rate series against `delivered` — not against
`processed`, and not against sends. From `machine_opens`, subtract the machine rows to get the
human-only open series.

The first month in the data is the migration month. Note it: it is the "before" the customer is
implicitly comparing against, and it is often unrepresentative because volume was still low.

## 2. Frequency and template cadence

The frequency series, which usually carries the diagnosis:

```json
{
  "name": "audience_size",
  "source": "emails",
  "metrics": [
    { "name": "distinct_recipients", "aggregation": "count_distinct", "field": "email" },
    { "name": "unique_emails", "aggregation": "count_distinct", "field": "provider_message_id" }
  ],
  "groupBy": ["time_bucket"],
  "filters": [{ "field": "type", "operator": "equals", "value": "delivered" }],
  "limit": 50
}
```

`unique_emails ÷ distinct_recipients` is emails per person per month. Put that column next to
the open-rate column in the report; the correlation usually speaks for itself.

For cadence and repetition, list the email templates with `searchEmailTemplates (operation:
list)` and analyse the result:

- Group `name` by prefix. Recurring campaign families (a weekly newsletter per branch or
  segment) show up as a large block of near-identical names.
- Group `createdAt` by date. Ten to fifteen templates created on the same weekday, week after
  week, is a recurring multi-segment blast.
- Count exact duplicate `subject` values. Many templates sharing one subject line, repeated
  across weeks, is the fatigue pattern in its clearest form.

A workspace with hundreds of templates is itself a signal: it means a new template per send
rather than a reused one, which is normal for campaign work but tells you the cadence is high.

## 3. Sender and provider cuts

```json
[
  {
    "name": "senders",
    "source": "emails",
    "metrics": [{ "name": "unique_emails", "aggregation": "count_distinct", "field": "provider_message_id" }],
    "groupBy": ["sender_address", "type"],
    "filters": [{ "field": "type", "operator": "includes", "value": ["delivered", "open", "blocked"] }],
    "sort": [{ "field": "unique_emails", "direction": "desc" }],
    "limit": 40
  },
  {
    "name": "providers",
    "source": "emails",
    "metrics": [{ "name": "unique_emails", "aggregation": "count_distinct", "field": "provider_message_id" }],
    "groupBy": ["email_provider", "type"],
    "filters": [{ "field": "type", "operator": "includes", "value": ["delivered", "open", "click", "blocked", "deferred"] }],
    "sort": [{ "field": "unique_emails", "direction": "desc" }],
    "limit": 60
  }
]
```

For senders, divide each address's `open` by its `delivered`. Expect bulk role addresses in the
single digits and named individuals in the 60–90% range. That contrast is the report's
strongest exhibit.

Also check each sender's block rate — `blocked ÷ (delivered + blocked)`. A role address with a
double-digit block rate has an authentication or configuration problem specific to it, and is
worth a separate finding.

For providers, divide `open` by `delivered` per provider and rank. Compare like with like:
Apple/iCloud is MPP-inflated, so benchmark suspect providers against low-MPP consumer ISPs
rather than against the workspace average. Elevated `blocked` and `deferred` at a single
provider reinforce a placement conclusion.

## 4. Reputation and the migration window

```json
{
  "name": "blocks_by_month",
  "source": "emails",
  "metrics": [{ "name": "unique_emails", "aggregation": "count_distinct", "field": "provider_message_id" }],
  "groupBy": ["time_bucket", "classification"],
  "filters": [{ "field": "type", "operator": "equals", "value": "blocked" }],
  "limit": 100
}
```

Classifications to read carefully:

- **`Reputation`** — the sending domain or IP is distrusted. Concentrated in one month during a
  volume ramp means a warm-up failure. Spread evenly at low level is background noise.
- **`Mailbox Unavailable`** — dead or full mailboxes. A steady monthly figure is list decay and
  argues for hygiene, not for an infrastructure fix.
- **`Frequency or Volume Too High`** — an explicit rate-limit rejection. Rare, and unambiguous
  when it appears.
- **`Content`** — a filter objected to the message body. Small counts are normal; a rising trend
  is worth showing the customer.
- **`Technical`** — receiver-side configuration, including forwarding loops. Usually the
  recipient's own problem, but worth naming so the customer can tell their client.

Also pull `reason` alongside `classification` for the specific SMTP strings — they are quotable
and they make an abstract finding concrete.

## 5. Constraints that are easy to get wrong

- **One email produces several rows**, one per provider event. Always `count_distinct` on
  `provider_message_id`. Using `count` on `id` inflates everything, and `deferred` in particular
  can produce dozens of events for a single message.
- **`processed` and `delivered` will not reconcile exactly** with `blocked` plus `bounce`. Some
  blocks occur after acceptance, so a message can be counted delivered and later rejected.
  Report delivered as the headline and note the later rejections separately rather than forcing
  the arithmetic.
- **Compute rates against `delivered`**, not `processed` and not sends. State which denominator
  you used, because the customer's old system may have used a different one.
- **`emails.template_id` is an integer; the template library uses UUIDs.** There is no join
  between per-template volume and template names. Infer the pattern from the library and say
  that you inferred it.
- **`searchEmailTemplates (operation: list)` can exceed the response limit** on workspaces with
  many templates and be written to a file instead. Query that file with `python3` or `jq`
  rather than re-requesting with a smaller limit and losing coverage. Note in the report what
  fraction of templates you actually analysed.
- **Period is capped at 366 days**, and `email` as a grouping field is the recipient address —
  treat any output containing it as personal data.
- `is_machine_open` and `is_mpp_open` are booleans returned as `0`/`1` in grouped rows.

## 6. Reference rates

Rough benchmarks for recruitment and staffing email in the Dutch market. Use them to say
whether a number is normal, never to set a target.

| Metric | Poor | Typical | Good |
|---|---|---|---|
| Delivery rate | < 95% | 95–98% | > 98% |
| Open rate (headline, incl. machine) | < 15% | 20–35% | > 35% |
| Open rate (human only) | < 8% | 10–20% | > 20% |
| Click rate (on delivered) | < 1% | 1–3% | > 3% |
| Unsubscribe rate | > 0.5% | 0.1–0.3% | < 0.1% |
| Spam complaint rate | > 0.1% | 0.01–0.05% | < 0.01% |

Two cautions. Headline open rates have been structurally inflated since Apple MPP, so a 2021
benchmark is not comparable to a 2026 measurement — which is frequently the real reason a
customer's "previous system" looks better. And a one-to-one recruiter email and a list
newsletter are different products; do not benchmark them against each other or blend them into
one average.
