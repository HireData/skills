# Measurement windows

The single most common error in a results readout is reporting a real number against the wrong
period. It usually makes the customer look worse than they are.

## Never take the period from the requester

People round their own go-live date, and they round it backwards. "We started somewhere in
March" has repeatedly meant a specific date in March that the system already knows precisely.
Read it from the workspace.

The reporting period starts at the creation or first activity of the earliest automation that
is capable of producing the outcome you are reporting. Not the contract date, not the
onboarding kickoff, not the start of the analytics window.

## Communicating versus data-only automations

Two populations, two different claims:

| Kind | Examples | What it can be credited with |
|---|---|---|
| Communicating | application follow-up, availability check, reactivation, auto reply, interview confirmation | assisted placements, replies, re-engaged candidates, response rate |
| Data-only | last-apply-date stamps, source attribution, status or availability writers | saved handling time, data completeness improvements |

An assisted-placement figure hangs off the earliest **communicating** automation. A saved-hours
figure hangs off the earliest automation of any kind. These are often different dates, and when
they are, say both.

If every automation in the workspace was created after the analytics window opened, say so
explicitly. It means the whole result was earned in the shorter period, which is the stronger
and more honest read.

## When the analytics window cannot be changed

Reporting surfaces commonly offer a fixed trailing window, such as the last twelve months, with
no way to align it to go-live. Do not paper over this and do not relabel the window. Carry both,
clearly separated:

```
LIVE SINCE      <date>, first automated outreach
                <N> months of running time to the report date
ANALYTICS       <start> to <end> (<N> months)
WINDOW          the window behind the stock and flow counts
```

Then label each metric with the window it belongs to. A KPI strip mixing
`new placements · 12 mo` with `tasks automated · since go-live` is correct. The same strip with
no labels is not.

## Three kinds of number, never blended

- **Stock**: how many records exist right now. Candidates in the database, dormant candidates,
  clients without an owner. No period at all.
- **Flow**: how many things happened inside the analytics window. New placements, new matches,
  reactivated matches.
- **Delivered**: what the automations did since go-live. Messages, replies, tasks handled,
  attributed outcomes, recovered time.

A share is only meaningful when numerator and denominator are the same kind and the same window.
An assisted-placement share computed as *delivered ÷ stock* will understate performance by an
order of magnitude, and a customer who spots it will stop trusting the whole document.

## Attribution coverage

Before publishing an attributed outcome count, check how far back the attributed records
actually reach. Sort the underlying list oldest-first, or query the earliest attributed event.

If attribution reaches back less far than go-live, the count is a **floor**, not a total.
Publish it anyway when it errs in the customer's favour, label it as a floor, and raise the gap
with the product owner. Never quietly present a partial-coverage count as a full-period total.
