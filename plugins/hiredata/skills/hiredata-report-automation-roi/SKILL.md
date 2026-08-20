---
name: hiredata-report-automation-roi
description: Report what recruitment automations have actually delivered for a customer, over the period they have genuinely been running. Use when someone asks for an ROI report, results readout, business review, renewal or upsell evidence, or a "what has this given us so far" summary for a workspace where automations are already live.
---

# Report automation ROI

A results readout is not an activation plan. The customer already bought the thing and switched it on. The only question that matters is what it returned, and whether the number survives being checked by a sceptical reader.

Most of the work is establishing the correct denominator. Get that wrong and every figure below it is wrong.

## First decide which job you are being asked to do

Two different requests arrive in the same words, and answering the wrong one is the most common failure with this skill.

- **A question about the readout**: which window to use, whether a figure can be published, how to handle a gap, whether a number is safe to print. Answer *that question*, with the queries that settle it and the reasoning behind the call. Steps 1 to 6 below apply. **Do not** open `references/report-structure.md`, do not list the sections of the document, and do not recite the standing exclusions. Reciting the template at someone who asked about one metric is padding, and it buries the answer they needed.
- **Build the document**: produce the readout itself. All eight steps apply.

When in doubt, answer the question and offer to build the document.

## Workflow

1. **Confirm the workspace is actually live.** Use the HireData MCP to list automations and their activity. No runs means there is no ROI to report: use `hiredata-plan-activation` instead and say so.
2. **Establish the true reporting period.** Read the creation date and activity of each automation rather than accepting a window from the requester. See [references/measurement-windows.md](references/measurement-windows.md). This is the step people skip and the one that changes the headline most.
3. **Separate communicating automations from data-only automations.** Only outreach can be credited with an assisted placement or a reply. Data-writing automations earn saved handling time, not conversions.
4. **Pull the delivered figures** from the MCP: volumes handled, messages sent, replies, records updated, and attributed outcomes. Never invent a workspace fact and never present a modelled figure as a measured one.
5. **Check attribution coverage, then find out why it is short.** Sort attributed events oldest-first. If they reach back less far than the running period, do not stop at labelling the count a floor: diagnose the cause, because one of them is recoverable. Query the data source's first sync and whether its initial backfill completed, the trigger's created and last-modified timestamps, and whether replies exist in the unmeasured period even though outcomes do not. A missed backfill can be re-run and hands you the real full-period number; a retention limit or a rebuilt trigger cannot. Name the queries you ran and what each ruled out.
6. **Re-derive every number you intend to print, and diagnose the ones that fail.** See [references/number-hygiene.md](references/number-hygiene.md). A figure that fails its own arithmetic is a finding, not just an exclusion: say which query would settle it. Anything unresolved stays out of the report and goes into a separate note for the product owner.
7. **Write the report, if that is what was asked.** Structure and section order are in [references/report-structure.md](references/report-structure.md). Skip this step entirely when the request was a question about the readout rather than a request to build it.
8. **Close with what the next measurement will show**, using metric names and definitions rather than repeating numbers already used earlier.

## Output

Match the length of the answer to the size of the question. A windowing question deserves the windowing answer and the queries that settle it, not a document outline.

Lead with the delivered result and the period it was earned in, in that order and in the same sentence. "1,200 placements in five months" is a different claim from "1,200 placements", and only one of them is checkable.

State each figure's own window next to it. A workspace stock count, a twelve-month flow count, and a since-go-live automation result are three different windows, and a report that blends them silently is wrong even when every individual number is right.

Deliver two artefacts: the customer-facing report, and a separate internal note listing any figure you rejected and the arithmetic that rejected it. The second one is frequently the more valuable of the two.

## Guardrails

- Do not report a headcount of recruiters or users unless a single authoritative source is available, and name that source. Seat counts, active users, ranked users, and synced users are different populations.
- Do not include pricing, credit consumption, margin, or commercial terms. Those follow through the account owner.
- Do not reprint modelled response or conversion assumptions when the workspace has an observed rate for the same thing. Use the observed rate, or omit the projection.
- Do not attribute a projected outcome to a single automation unless the projection is defined per automation at the source.
- Do not present an all-time total inside a report framed as a period, and do not divide a period numerator by an all-time denominator.
- Preview the report with the requester before it is sent onward to a customer, and confirm before sending anything on their behalf.
- If MCP access is unavailable or partial, produce the report skeleton with each figure marked as unverified, and state exactly which queries remain to be run.
