I've drafted this as an intake issue. The chat message is a customer request with a solution already attached, so I kept the problem as the main point and wrote the bulk endpoint up as one possible approach, not a requirement. Nothing was created in Linear. I couldn't search for duplicates, check customer links or confirm the latest policy pages, so those are marked unverified.

---

**Title:** Messaging: Send One WhatsApp Template to a Whole Talent Pool

**Status:** Triage · **Project:** Messaging · **Label:** Feature · **Assignee / Cycle / Estimate:** unset

## Summary

Customers are asking to send one WhatsApp template to every candidate in a talent pool in a single action. Today the only way is to loop over the pool and send to each candidate in turn. That loop times out at about 200 candidates, so larger pools can't be reached reliably.

Source: internal chat from a colleague (link the message). The customer requests behind it haven't been linked or counted yet.

## Current behaviour

- Messages are sent one candidate at a time by looping over the talent pool.
- At about 200 candidates the loop times out. *(Reported figure, not yet reproduced. It's unknown whether this is a request timeout, a run/step limit or a rate limit.)*
- Unknown: whether candidates before the timeout already received the message, and whether a retry sends duplicates.

## Expected behaviour

A user (or integration) can send one approved WhatsApp template to all candidates in a talent pool, or to a chosen list of candidates, in one action. This works regardless of pool size. Afterwards they can see who it was sent to, who was skipped and who failed.

## Proposed approach (reporter's suggestion, not decided)

A bulk endpoint that takes one template and a list of candidate IDs. Engineering should decide during refinement whether this is the right fix. It might instead be a background/async send job, a talent-pool target in automations, or a fix to whatever is timing out today.

## Steps to reproduce

1. Pick a talent pool with more than about 200 candidates.
2. Send a WhatsApp template to each candidate using the current loop. *(Which mechanism: public API script, automation "for each" or UI? Needs confirming.)*
3. Observe the timeout at about 200 candidates.

Account, pool, run/event links and the exact error: **missing, needed from reporter.**

## Evidence and links

- Source chat message: *(add link)*
- Customer requests (Intercom/Discord): *(add and connect customers)*
- Example failed run or error: *(add)*

## Triage questions

1. **Where does the loop run?** Customer-side API script, HireData automation or something else? This decides whether the fix is an API, an automation feature or a performance fix.
2. **What actually times out?** HTTP request, run duration, Meta/WhatsApp provider rate limit or our own throttling?
3. **Reach:** which customers have asked, how often, and what pool sizes do they need?
4. **Partial sends:** what happens to candidates already messaged when it fails? Is there a risk of duplicate messages on retry?
5. **Eligibility:** how should candidates without a valid phone number, without WhatsApp opt-in/consent, or who have opted out be handled? Skip and report?
6. **Personalisation:** are template variables filled per candidate, or is the message the same for everyone?
7. **Limits:** does Meta's messaging tier or quality rating limit how many messages a customer can send per day? Do we need to queue or throttle?
8. **Target:** talent pool ID, a list of candidate IDs, or both?
9. **Duplicates:** is there an existing issue for bulk/broadcast WhatsApp sending or talent-pool targeting? *(Linear not searched.)*

## Metadata notes

- **Priority: left unset for Triage.** By the matrix, this could be **High** ("widespread slowness or timeouts", or an important customer workflow badly impaired) or **Medium** (a client-requested feature that's partly missing, with no immediate operational blocker). It depends on reach and whether there's a workaround, and neither is known yet. If a value is required, use Medium and leave a comment noting the uncertainty.
- **Relations:** none verified.
- **Recommended next state after Triage:** To Be Refined. Questions 1, 2 and 4 decide what the work actually is.

---

Before filing, the gaps the colleague can probably fill in quickly are the source link, the customer requests, an example of a failed run, and where the loop runs.
