---
name: hiredata-diagnose-automations
description: Diagnose why a HireData automation did not do what someone expected, and propose a safe repair. Use when runs are cancelled, failed, timed out or skipped, when an email or WhatsApp message never arrived, when a trigger appears not to fire, when runs are stuck or an automation has gone quiet, when an automation is producing far more runs than results, or when someone pastes a run error and asks what it means. Do not use this for email open, click or deliverability questions — use hiredata-diagnose-email-performance instead.
---

# Diagnose HireData automations

Explain what actually happened to a workflow before changing anything.

Most reports of a "broken" automation are one of six different situations with different fixes. Separate them first.

| Situation | Where the evidence is |
|---|---|
| The trigger never produced an event | `events` |
| Events arrived but runs stopped early | `runs`, then `run_steps` |
| A step errored | `run_steps` |
| The message was sent but not delivered or not read | `emails`, `messages` |
| Runs started and never finished | `runs` filtered to non-terminal statuses |
| Everything worked, but at a volume nobody intended | `runs` volume against distinct records and finished runs |
| Everything worked and the expectation was wrong | the trigger blueprint and the user story |

The last three are the ones people miss. A run stuck in `running` for two months looks like nothing at all in a status chart. An automation producing 600,000 runs to send 8 emails reports no errors whatsoever. Neither will surface unless you look for them.

## Workflow

0. **Read the account history first.** Check the account's known history — CRM notes, the account record, past support tickets — before touching the data. Prior incidents, configuration changes, known data inconsistencies and expert consultations are almost never visible in the statistics, and diagnosing without them produces confident nonsense. If a page describes a past problem, the current one is often its continuation.
1. Establish the claim: which automation, which workspace, which recipient or record, what the person expected, and over what period. Ask only for what you cannot look up.
2. Run the first pass. [references/diagnostic-queries.md](references/diagnostic-queries.md) opens with a single copy-pasteable call that answers most claims — status split, step reasons, stale runs, volume ratios and cost in one round trip. Read that file before composing anything, and call `queryStatistics (operation: capabilities)` for any source whose fields you are unsure of.
3. Walk the ladder in order — intake, run outcome, step reason, channel outcome, configuration. Stop as soon as the evidence explains the claim; do not run every query by reflex.
4. Read [references/failure-patterns.md](references/failure-patterns.md) to interpret the reason you found. Confirm the current vocabulary from live capabilities rather than assuming the reference is complete.
5. Separate expected cancellation from defect. A large share of cancelled runs is normal in healthy workspaces, because a run that does not match a filter or a path is cancelled rather than failed. Never report a cancellation rate as a fault on its own.
6. Check proportion, not just outcome. Ask what the automation produced against what it consumed — see "Volume as a diagnosis" below.
7. State the diagnosis as: what happened, the evidence that shows it, how many records it affected, whether it is still happening, and what remains unexplained.
8. Propose a repair with its trade-off. Show the exact change, and what it will and will not fix.
9. Apply nothing without approval of that exact change. Re-read the trigger, template or form after any approved change and confirm the saved state.

## Naming the automation

The statistics sources identify automations only by numeric `automation_id`. There is no MCP lookup from that number to the automation's name, and `searchAutomationTriggers` does not accept it — that tool addresses the reusable trigger blueprint library by UUID, which is a different thing.

So a report that says "automation 4127" is unreadable to anyone who was not in the session. Always build a human descriptor from the data you do have and lead with it:

> **Automation 4127** — CRM `Contact`, trigger `created_or_updated`, ~30,000 distinct records

`runs` carries `trigger`, `object` and `app`; `run_steps` carries the step `type` sequence; `emails` carries `template_id`. Together these describe what the automation is for, even without its name. Ask the person for the name, or look it up in the app, before anything customer-facing goes out.

## Volume as a diagnosis

An automation can be entirely free of errors and still be the most expensive thing in a workspace. Compute these three ratios on every diagnosis — they cost one query and they catch what status distributions hide:

- **runs ÷ finished runs.** How many invocations it takes to produce one outcome. A filter step that rejects 99.99% of runs is working, but it means the trigger is subscribed to a firehose the automation does not want.
- **runs ÷ distinct `external_record_id`.** How often the same record is reprocessed. A value well above 1 usually means an upstream system is bulk-touching records on a schedule, not that anything changed.
- **runs ÷ billable steps.** What the volume actually bought.

When these are lopsided, the repair is almost never inside the workflow. It is to move the qualifying conditions from the first filter step up into the trigger's event filters, so non-qualifying records are discarded at intake and never spawn a run. Say plainly that this changes cost and noise, not which records get the outcome.

A weekday-shaped volume curve — high Monday to Friday, near zero at weekends — is the signature of a scheduled bulk sync in the connected system, not of user activity. Name it as an upstream finding and route it to whoever owns that sync.

## Runs that never ended

`finished`, `cancelled`, `failed` and `timed_out` are terminal. `running`, `pending`, `waiting` and `scheduling` are not. A handful of non-terminal runs at any moment is normal. Non-terminal runs whose `started_at` is days or weeks old are not — they are stuck, they will never resolve on their own, and nobody is watching them because they appear in no error count.

Check the age of the oldest non-terminal run on every diagnosis. Report stuck runs with their count and the date they stopped moving. A `waiting` run on `email_pending` from two months ago means a message that was never sent and never failed.

## Cost

`credits` records only successful, non-test billable work — emails sent, conversations started, surveys sent. It is the answer to "what did this cost", and it is frequently reassuring: hundreds of thousands of cancelled runs usually cost nothing at all, because nothing billable executed.

Check it before letting anyone panic about volume, and check it before proposing a repair justified on cost. Note that `credits` is slow: see the performance constraints in the query reference.

## Reporting

Internal and customer-facing write-ups are not the same document.

- **Internal**: quote record identifiers, name the connected system and the sending domain, and state what HireData did wrong if HireData did something wrong. If a ramp, a missing warm-up or a default limit contributed, say so — it is cheaper to own it now than to have the customer find it.
- **Customer-facing**: anonymise record identifiers, drop internal automation IDs in favour of the automation's name, and lead with what it means for their candidates rather than with the status vocabulary.

Keep the order in both: what they observed, what actually happened with its evidence, how many records, whether it is still happening, what is unexplained, then the proposed repair and the approval it needs.

## Guardrails

- Never state a workspace count or default, automation configuration, account-history fact, run
  result or channel outcome unless the source returned it in the current turn. If it was not
  queried or the surface is unreachable, call it unknown instead of filling the gap.
- Report a zero as a zero. If a source is partial, pruned or gated, say which one and why the answer is incomplete instead of filling the gap.
- Never infer a reason that no source returned. If the run-level message is empty and no step explains it, say the reason is not recorded and name the next place a human should look.
- Do not treat `cancelled` as an error, `skipped` as a failure, or a single failed run as an outage.
- Diagnose in the workspace the person named. Watch for duplicate workspaces — many customers have a `(testomgeving)` or `(to delete)` twin, and diagnosing the wrong one wastes the whole analysis. Confirm the ID before querying.
- Do not carry one workspace's figures into another workspace's diagnosis.
- Changing, pausing, activating or replaying anything is a consequential action. Preview it and require explicit approval, even when the fix looks obvious and even while diagnosing.
- Re-running or replaying past events can re-send real messages to real candidates. Establish the blast radius and get approval that names it before proposing a replay.
- If a needed surface is unreachable, say what you could not verify rather than working around it silently. Several configuration details genuinely require the app UI today; naming them is a finding, not a failure.
- If the MCP is unavailable, return the diagnostic plan and the exact queries to run, and state clearly that nothing was verified.
- If the diagnosis turns out to be about open rates, click rates or deliverability rather than a broken workflow, hand off to `hiredata-diagnose-email-performance`. In particular, never explain a low open rate by comparing it to a transactional or one-to-one send — that gap is inherent to the product and means nothing.

## This produces a draft, not a decision

The output is material for a human to judge, not an answer to forward. Whoever owns the account knows things the data does not, and this analysis can be confidently wrong when it lacks that context. Hand over the reasoning and the evidence, mark clearly what is inferred rather than measured, and let the account owner decide. When drafting customer-facing text, write it in their language and in a voice the sender would actually use — a reply that reads as machine-generated undermines the credibility of the analysis behind it.
