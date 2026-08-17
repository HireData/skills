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

The mirror-image mistake is just as common: reporting "the automation ran fine" because runs
finished, when the message bounced at hop 4. Finished means the workflow completed, not that a
human received anything.

## Step reasons

Short machine reasons that commonly appear on `run_steps`, and what to do about each.

| Reason | Meaning | First response |
|---|---|---|
| `invalid_sender_address` | The channel could not send because the sender address on the step, connection or user is missing or not valid. | Check the sender configured on the step and the connection, and the owning user's address, before touching the template. The template is rarely the fault. |
| `open_conversation_detected` | An outbound conversation was not started because the recipient already has one open on that channel. | This is a lifecycle collision, not an error. Decide deliberately whether the new message should merge into the open thread, wait, or be dropped. Retrying reproduces it. |
| `no_valid_paths_found` | A path step evaluated every branch and none matched. | Usually an incomplete branch set or a value the design did not anticipate. Inspect the real distribution of the deciding field before adding a branch. |
| `no_result_found_for_match` | A data lookup found no record for the given criteria. | Distinguish "the record does not exist" from "the criteria are wrong". Check the lookup key against live data. |
| `run_timed_out` | The run exceeded its allowed lifetime, commonly while waiting in a delay. | Long delays are the usual cause. Confirm the intended wait against the maximum run lifetime rather than lengthening the delay. |
| `run_cant_continue` | A step was skipped because the run could no longer proceed. | A consequence, not a cause. Find the step that stopped the run first. |
| `http_invalid_config` | An outbound HTTP or webhook step is misconfigured. | Inspect the step's URL, method, authentication and payload. |

Longer prose messages come from a connected ATS and name the operation and record, in the shape
`Unable to **update candidate(<id>)** — <system> returned an error.` Read these carefully:
they distinguish a temporary outage from a data problem, and the two need different responses.
A transient connector outage resolves and may deserve a replay; invalid data recurs on every
retry until the record or the mapping is fixed.

## Channel outcomes

If runs finished but nothing arrived, the answer is at hop 4.

- **Email**: `bounce`, `blocked` and `dropped` each mean something different. A hard bounce is a
  data-quality problem on the recipient. `blocked` and `dropped` are usually sender reputation,
  authentication or suppression, and are properties of the sending domain rather than the
  template. `reason`, `sub_type` and `classification` carry the distinction.
- **Conversational channels**: `error` and `failed` carry `error_type`, `code` and `reason`.
  Template approval state and channel policy are common causes and are not fixed by retrying.
- `delivered` without `open`, or `sent` without `seen`, is an engagement question, not a defect.
  Say so plainly rather than proposing an engineering fix for a copy problem.

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
4. What is still unexplained.
5. The proposed repair, what it will not fix, and what approval it needs.

Anonymize record identifiers in anything that leaves the workspace. Never carry one workspace's
figures into another workspace's diagnosis.
