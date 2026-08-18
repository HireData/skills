# Failure patterns

How to interpret what a run or step reports, and what the recruitment-side consequence is.

This is interpretation, not a schema. The reason vocabulary changes with the product. Read the
current enums from `queryStatistics (operation: capabilities)` and treat any reason you do not
recognise as undiagnosed rather than forcing it into a row below.

## Cancelled is not broken

`cancelled` is the normal terminal state for a run that correctly decided to do nothing — the
filter did not match, no path applied, or a safety limit held. In a busy workspace, cancelled
runs routinely outnumber finished ones, and that on its own is evidence of nothing.

What matters is the *reason mix*, not the rate. Ask: is the population being cancelled the
population the automation was supposed to skip? A rising share of one specific reason is a
signal. A high steady share across many reasons usually is not.

The vocabulary is actively misleading here, and you have to compensate for it in prose. A
screen reading "600,000 cancelled" and a correct diagnosis of "filtered out 600,000 times,
exactly as designed" are opposite conclusions drawn from the same number. Never repeat the
raw status word to a customer without the reading attached.

The mirror-image mistake is just as common: reporting "the automation ran fine" because runs
finished, when the message bounced at hop 4. Finished means the workflow completed, not that a
human received anything.

## Not every cancellation is equal

A single `cancelled` bucket usually mixes three different things, and the whole value of a
diagnosis is telling them apart. From one real automation's 124 cancelled send steps:

| Reason | Count | What it actually is |
|---|---|---|
| `email_unsubscribed` | 69 | Correct suppression. Working as intended. |
| `send_limits_per_automation_exceeded` | 39 | **Real loss of reach.** These people were in the audience, passed the filter, had a valid address, and got nothing. |
| `email_invalid` | 13 | Data-quality problem at source. |
| `email_bounced` | 3 | Correct suppression of a known-bad address. |

Three of those are healthy. One is a silent failure that nobody would ever see, because it
renders identically to the other three. Always break the cancelled bucket down by reason
before characterising it, and lead the report with the one that cost the customer something.

## Step reasons

Short machine reasons that commonly appear on `run_steps`, and what to do about each.

| Reason | Meaning | First response |
|---|---|---|
| `filter_not_passed` | The record did not match the filter. The run stops here. | Expected behaviour. Only a finding when the pass rate is implausibly low — then it is a trigger-scope problem, not a filter problem. |
| `run_cant_continue` | A step was skipped because the run could no longer proceed. | A consequence, not a cause. Find the step that stopped the run first. |
| `send_limits_per_automation_exceeded` | The automation hit its configured safety cap and stopped sending. | **Treat as a real defect.** Quantify how many recipients were cut off, and check whether the limit was ever raised after the audience grew. The configured value needs the UI. |
| `email_unsubscribed` / `email_bounced` | Suppression fired correctly. | Not a fault. Report as audience hygiene. |
| `email_invalid` | The stored address is malformed or unusable. | Data quality at source. Fix in the ATS, or it recurs on every campaign. |
| `invalid_sender_address` | The channel could not send because the sender address on the step, connection or user is missing or not valid. | Check the sender configured on the step and the connection, and the owning user's address, before touching the template. The template is rarely the fault. |
| `open_conversation_detected` | An outbound conversation was not started because the recipient already has one open on that channel. | A lifecycle collision, not an error. Decide deliberately whether the new message should merge into the open thread, wait, or be dropped. Retrying reproduces it. |
| `no_valid_paths_found` | A path step evaluated every branch and none matched. | Usually an incomplete branch set or a value the design did not anticipate. Inspect the real distribution of the deciding field before adding a branch. |
| `no_result_found_for_match` | A data lookup found no record for the given criteria. | Distinguish "the record does not exist" from "the criteria are wrong". Check the lookup key against live data. |
| `run_timed_out` | The run exceeded its allowed lifetime, commonly while waiting in a delay. | Long delays are the usual cause. Confirm the intended wait against the maximum run lifetime rather than lengthening the delay. |
| `email_pending` | The send was handed off and no outcome was ever recorded. | If recent, wait. If the run has been `waiting` on this for days, it is stuck — see below. |
| `http_invalid_config` | An outbound HTTP or webhook step is misconfigured. | Inspect the step's URL, method, authentication and payload. |

Longer prose messages come from a connected ATS and name the operation and record, in the shape
`Unable to **update candidate(<id>)** — <system> returned an error.` Read these carefully:
they distinguish a temporary outage from a data problem, and the two need different responses.
A transient connector outage resolves and may deserve a replay; invalid data recurs on every
retry until the record or the mapping is fixed.

## Runs that never ended

Non-terminal statuses — `running`, `pending`, `waiting`, `scheduling` — are invisible in every
error count, which is exactly why they accumulate.

Judge them by age, not by count. Compare the oldest non-terminal run's `started_at` to today:

- Hours old: normal, especially with delay steps in the workflow.
- Days old: suspicious. Check whether the step it is sitting on has a plausible wait.
- Weeks old: stuck. It will not resolve on its own.

A stuck run is a message that was never sent and never failed, so nobody was told. Report the
count and the date they stopped moving, and treat clearing them as part of the repair rather
than as housekeeping.

## Channel outcomes

If runs finished but nothing arrived, the answer is at hop 4.

- **Email**: `bounce`, `blocked` and `dropped` each mean something different. A hard bounce is a
  data-quality problem on the recipient. `blocked` and `dropped` are usually sender reputation,
  authentication or suppression, and are properties of the sending domain rather than the
  template. `reason`, `sub_type` and `classification` carry the distinction.
- A step marked `completed` / `email_delivered` means the provider accepted the message. A
  later `blocked` or `bounce` event on the same email can still contradict it, so the count of
  emails that truly landed is delivered minus later rejections. Reconcile the two before
  quoting a delivery figure.
- **Conversational channels**: `error` and `failed` carry `error_type`, `code` and `reason`.
  Template approval state and channel policy are common causes and are not fixed by retrying.
- `delivered` without `open`, or `sent` without `seen`, is an engagement question, not a defect.
  Say so plainly rather than proposing an engineering fix for a copy problem — and hand it to
  `hiredata-diagnose-email-performance`, which is built for exactly that question.

## Variables that resolve to nothing

A template can be valid and still produce an empty or unusable message, because variable
validation checks that a placeholder is *known*, not that it will have a value at send time.

This matters most for template-scoped custom variables, including AI variables. On the send and
test path, every custom variable referenced by the body requires an explicit non-empty value,
and a stored default is deliberately not substituted for it. So a template that previews
correctly can still go out with a hole in it when the automation supplies nothing.

When a recipient reports a message with a missing sentence, an empty greeting or a stray
fragment, check which variables are custom before assuming the copy is wrong. Then confirm what
the step actually supplied. Do not fill the gap by inventing a value — an empty AI variable
means the workflow did not provide its input, and the repair belongs in the workflow.

Never let a repair introduce generated text that asserts a fact. An AI variable that fabricates
a date, a rate, a job detail or a commitment turns a delivery defect into a candidate-facing
false statement.

## Reporting the diagnosis

State it in this order, and keep it short:

1. What the person observed, in their words.
2. What actually happened, with the source and reason that shows it.
3. How many records were affected, and whether it is still happening.
4. What is still unexplained, and where a human should look next.
5. The proposed repair, what it will not fix, and what approval it needs.

Anonymize record identifiers in anything that leaves the workspace. Never carry one workspace's
figures into another workspace's diagnosis.

If HireData contributed to the problem — a default limit that was never raised, a ramp we did
not warm up, a known issue we did not flag — say so in the internal version at minimum, and
usually in the customer version too. Customers forgive a named cause far more readily than one
they discover themselves later.
